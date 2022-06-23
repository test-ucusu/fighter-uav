import logger
import object

# get the logger
logger = logger.Logger(name="interop").logger

# log the script has started
logger.info("started")

# get the competition
competition = object.Competition()

# log the competition
logger.info("competition info: {0} {1}".format(competition.day_name, competition.round_local_name))

# get the vehicle
vehicle = object.Vehicle()

# log the vehicle connection
logger.info("vehicle telemetry connection status: " + str(vehicle.connected))

# wait vehicle to be connected
vehicle.wait_ready()

# log the vehicle connection
logger.info("vehicle telemetry connection status: " + str(vehicle.connected))

# log the flight mode of the vehicle
logger.info("vehicle flight mode: " + str(vehicle.flight_mode))