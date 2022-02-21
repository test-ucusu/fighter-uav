import tu_log.tu_log_object
import tu_interop.tu_interop_object

# get the logger
import tu_settings

tu_logger = tu_log.tu_log_object.Logger(name="tu_core_interop")

# log the script has started
tu_logger.logger.info("started")

# get the competition
tu_competition = tu_interop.tu_interop_object.Competition()

# log the competition
tu_logger.logger.info("competition info: {0} {1}".format(tu_competition.day_name, tu_competition.round_local_name))

# get the vehicle
tu_vehicle = tu_interop.tu_interop_object.Vehicle()

# log the vehicle connection
tu_logger.logger.info("vehicle telemetry connection status: " + str(tu_vehicle.connected))

# connect to the vehicle
tu_vehicle.telemetry_connect(ip=tu_settings.tu_telem_stream_ip,
                             port=tu_settings.tu_telem_stream_port_interop)

# log the vehicle connection
tu_logger.logger.info("vehicle telemetry connection status: " + str(tu_vehicle.connected))
