'use strict';
const AWS = require('aws-sdk');
const sns = new AWS.SNS();
const snsTopicArn = process.env.NOTIFICATIONS_TOPIC_ARN;
exports.handler = function(event, context, callback) {
  const requestItems = buildRequestItems(event.Records);
  const requests = buildRequests(requestItems);
  Promise.all(requests)
    .then(() => callback(null, `Delivered ${event.Records.length} records`))
    .catch(callback);
};
function buildRequestItems(records) {
  return records.map((record) => {
    const json = Buffer.from(record.kinesis.data, 'base64').toString('ascii');
    const item = JSON.parse(json);
    return item;
  });
}
function buildRequests(requestItems) {
  const requests = [];
  while (requestItems.length > 0) {
    const request = publishSns(requestItems.splice(0, 25));
    requests.push(request);
  }
  return requests;
}
function publishSns(requestItems, attempt = 0) {
  let delay = 0;
  if (attempt > 0) {
    delay = 50 * Math.pow(2, attempt);
  }
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      sns.publish({
        TopicArn: snsTopicArn,
        Subject: 'Warning: Container Anomaly Detected',
        Message: `Container ${requestItems[0].container_id} Anomaly Detected.`
      }).promise()
        .then(resolve)
        .catch(reject);
    }, delay);
  });
}