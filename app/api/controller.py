from flask import Blueprint, request, abort, jsonify
import logging, os
from flask_restful import Resource, Api
from flasgger import swag_from
from concurrent.futures import ThreadPoolExecutor
from api.prometheus import track_requests
from domain.reefer_simulator import ReeferSimulator

controller_bp = Blueprint("control", __name__)
api = Api(controller_bp)

class SimulationController(Resource):

    def __init__(self):
        print("Simulation Controller created")
        self.simulator = ReeferSimulator()

    @swag_from('version.yaml')
    def get(self):
        return jsonify({"version": "v0.0.1"})
    
    @track_requests
    @swag_from('controlapi.yml')
    def post(self):
        logging.info("post control received: ")
        control = request.get_json(force=True)
        logging.info(control)
        metrics = {"nb_records": 100}
        return metrics,202

api.add_resource(SimulationController, "/control")