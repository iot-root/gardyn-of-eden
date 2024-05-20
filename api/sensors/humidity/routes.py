from flask import Blueprint, jsonify
from api.lib.lib import check_sensor_guard
from .humidity import humidity_sensor

humidity_blueprint = Blueprint('humidity', __name__)
check_sensor = check_sensor_guard(sensor=humidity_sensor, sensor_name='Humidity')

@humidity_blueprint.route('', methods=['GET'])
@check_sensor
def get_humidity():
    try:    
        return jsonify(value='{:.2f}'.format(humidity_sensor.get_value()))
    except Exception as e:
        log(e)
        return jsonify(error=str(e)), 400