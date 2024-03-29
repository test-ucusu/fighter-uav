import datetime
import cv2
import pyfakewebcam
import tu_video_util
import tu_telem.tu_telem_object
import settings

# drawing related settings
hit_area_top_left = (int(tu_settings.video_stream_width * 0.25), int(tu_settings.video_stream_height * 0.1))
hit_area_bottom_right = (tu_settings.video_stream_width - hit_area_top_left[0],
                         tu_settings.video_stream_height - hit_area_top_left[1])
hit_area_color = (0, 255, 0)
hit_area_thickness = 5
osd_font = cv2.FONT_HERSHEY_SIMPLEX
osd_font_scale = 1
osd_font_color = (0, 255, 0)
osd_font_thickness = 2
osd_font_line_type = cv2.LINE_AA

# create dummy sink for judge server streaming
sink_osd = pyfakewebcam.FakeWebcam(video_device=tu_settings.video_stream_port_local_osd,
                                   width=tu_settings.video_stream_width,
                                   height=tu_settings.video_stream_height)

# create capture device
capture_device = tu_video_util.capture_device_create(port=tu_settings.video_stream_port_local_raw)

# create telemetry receiver
telemetry_receiver = tu_telem.tu_telem_object.Receiver()

# do below always
while True:

    # try to do below
    try:

        # get time
        current_date = "DATE: " + str(datetime.datetime.now())[:10:].replace("-", "/")

        # get telemetry data
        telemetry_data = telemetry_receiver.telemetry_get

        # process received telemetry data for stamping
        current_time = "TIME: {0:02d}:{1:02d}:{2:02d}.{3:03d}".format(
            telemetry_data.get("judge", {}).get("time", {}).get("hour", 0),
            telemetry_data.get("judge", {}).get("time", {}).get("minute", 0),
            telemetry_data.get("judge", {}).get("time", {}).get("second", 0),
            telemetry_data.get("judge", {}).get("time", {}).get("millisecond", 0))
        current_mode = "MODE: {0}".format(telemetry_data.get("flight_mode", "UNKNOWN"))
        current_auto = "ARMED: {0}".format(telemetry_data.get("armed", "UNKNOWN")).upper()
        current_latitude = "LAT: {0:.6f}".format(telemetry_data.get("location", {}).get("latitude", 0))
        current_longitude = "LON: {0:.6f}".format(telemetry_data.get("location", {}).get("longitude", 0))
        current_altitude = "ALT: {0:.2f}".format(telemetry_data.get("location", {}).get("altitude", 0))
        current_roll = "RLL: {0:.2f}".format(telemetry_data.get("attitude", {}).get("roll", 0))
        current_pitch = "PIT: {0:.2f}".format(telemetry_data.get("attitude", {}).get("pitch", 0))
        current_heading = "HDG: {0:.2f}".format(telemetry_data.get("attitude", {}).get("heading", 0))
        current_speed = "SPD: {0:.2f}".format(telemetry_data.get("speed", 0))
        current_battery = "BAT: {0:.2f}".format(telemetry_data.get("battery", 0))
        current_team_number = "ID: {0}".format(telemetry_data.get("team", 0))
        current_target_time_start = "TLS: {0:02d}:{1:02d}:{2:02d}.{3:03d}".format(
            telemetry_data.get("target", {}).get("time_start", {}).get("hour", 0),
            telemetry_data.get("target", {}).get("time_start", {}).get("minute", 0),
            telemetry_data.get("target", {}).get("time_start", {}).get("second", 0),
            telemetry_data.get("target", {}).get("time_start", {}).get("millisecond", 0))
        current_target_time_end = "TLE: {0:02d}:{1:02d}:{2:02d}.{3:03d}".format(
            telemetry_data.get("target", {}).get("time_end", {}).get("hour", 0),
            telemetry_data.get("target", {}).get("time_end", {}).get("minute", 0),
            telemetry_data.get("target", {}).get("time_end", {}).get("second", 0),
            telemetry_data.get("target", {}).get("time_end", {}).get("millisecond", 0))
        current_target_lock = "LOCK: {0}".format(telemetry_data.get("target", {}).get("lock", 0))
        current_target_lock_x = "TLX: {0:04d}".format(telemetry_data.get("target", {}).get("x", 0))
        current_target_lock_y = "TLY: {0:04d}".format(telemetry_data.get("target", {}).get("y", 0))
        current_target_lock_width = "TLW: {0:04d}".format(telemetry_data.get("target", {}).get("width", 0))
        current_target_lock_height = "TLH: {0:04d}".format(telemetry_data.get("target", {}).get("height", 0))
        current_target_latitude = "TLAT: {0:.6f}".format(
            telemetry_data.get("foe", {}).get("location", {}).get("latitude", 0))
        current_target_longitude = "TLON: {0:.6f}".format(
            telemetry_data.get("foe", {}).get("location", {}).get("longitude", 0))
        current_target_altitude = "TALT: {0:.2f}".format(
            telemetry_data.get("foe", {}).get("location", {}).get("altitude", 0))
        current_target_roll = "TRLL: {0:.2f}".format(
            telemetry_data.get("foe", {}).get("attitude", {}).get("roll", 0))
        current_target_pitch = "TPIT: {0:.2f}".format(
            telemetry_data.get("foe", {}).get("attitude", {}).get("pitch", 0))
        current_target_heading = "THDG: {0:.2f}".format(
            telemetry_data.get("foe", {}).get("attitude", {}).get("heading", 0))
        current_target_team_number = "TID: {0}".format(telemetry_data.get("foe", {}).get("team", 0))
        current_day = "DAY: {0}".format(telemetry_data.get("competition", {}).get("day", 0))
        current_round_local = "RND: {0}".format(telemetry_data.get("competition", {}).get("round_local", 0))
        current_connected_vehicle = "TELEM: {0}".format(telemetry_data.get("connected", "UNKNOWN")).upper()
        current_connected_judge = "JUDGE: {0}".format(
            telemetry_data.get("judge", {}).get("logged_in", "UNKNOWN")).upper()
        current_allowed_interop = "INTEROP: {0}".format(
            telemetry_data.get("judge", {}).get("allowed_interop", "UNKNOWN")).upper()

        # get the image frame
        my_success, my_image = capture_device.read()

        # check frame capture was successful
        if my_success:

            # check image
            if tu_video_util.is_valid_image(my_image):

                # manipulate frame
                my_image = cv2.rectangle(my_image, hit_area_top_left, hit_area_bottom_right, hit_area_color,
                                         hit_area_thickness)
                my_image = cv2.putText(my_image, current_day, (5, 30),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_round_local, (5, 60),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_mode, (5, 120),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_auto, (5, 150),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_latitude, (5, 210),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_longitude, (5, 240),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_altitude, (5, 270),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_roll, (5, 330),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_pitch, (5, 360),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_heading, (5, 390),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_speed, (5, 440),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_battery, (5, 470),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_team_number, (5, 530),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_connected_vehicle, (5, 590),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_connected_judge, (5, 620),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_allowed_interop, (5, 650),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, "TEST UCUSU", (5, 710),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_date, (970, 30),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_time, (970, 60),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_time_start, (970, 120),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_time_end, (970, 150),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_lock, (970, 210),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_lock_x, (970, 240),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_lock_y, (970, 270),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_lock_width, (970, 300),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_lock_height, (970, 330),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_latitude, (970, 390),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_longitude, (970, 420),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_altitude, (970, 450),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_roll, (970, 510),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_pitch, (970, 540),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_heading, (970, 570),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, current_target_team_number, (970, 630),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
                my_image = cv2.putText(my_image, "TEKNOFEST 2022", (1005, 710),
                                       osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)

                # change color space if testing
                if tu_settings.video_stream_test:
                    # convert image to RGB
                    my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)

                # send image frame to judge sink
                sink_osd.schedule_frame(my_image)

    # catch all exceptions
    except Exception as e:
        print(e)
