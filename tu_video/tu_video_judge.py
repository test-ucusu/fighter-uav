import datetime
import cv2
import pyfakewebcam
import tu_video_util
import tu_settings

# drawing related settings
hit_area_top_left = (int(tu_settings.tu_video_stream_width * 0.25), int(tu_settings.tu_video_stream_height * 0.1))
hit_area_bottom_right = (tu_settings.tu_video_stream_width - hit_area_top_left[0],
                         tu_settings.tu_video_stream_height - hit_area_top_left[1])
hit_area_color = (0, 0, 255)
hit_area_thickness = 5
osd_font = cv2.FONT_HERSHEY_SIMPLEX
osd_font_scale = 1
osd_font_color = (0, 255, 0)
osd_font_thickness = 2
osd_font_line_type = cv2.LINE_AA

# create dummy sink for judge server streaming
sink_judge = pyfakewebcam.FakeWebcam(video_device=tu_settings.tu_video_stream_port_local_judge,
                                     width=tu_settings.tu_video_stream_width,
                                     height=tu_settings.tu_video_stream_height)

# create capture device
capture_device = tu_video_util.capture_device_create(port=tu_settings.tu_video_stream_port_local_raw)

while True:

    # get time
    current_time = str(datetime.datetime.now())[:-3:].split(" ")

    # get the image frame
    my_success, my_image = capture_device.read()

    # check frame capture was successful
    if my_success:

        # check image
        if tu_video_util.is_valid_image(my_image):

            # manipulate frame
            my_image = cv2.rectangle(my_image, hit_area_top_left, hit_area_bottom_right, osd_font_color, hit_area_thickness)
            my_image = cv2.putText(my_image, current_time[0], (5, 30),
                                   osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
            my_image = cv2.putText(my_image, current_time[1], (5, 60),
                                   osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
            my_image = cv2.putText(my_image, "TEST UCUSU", (5, 710),
                                   osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)
            my_image = cv2.putText(my_image, "TEKNOFEST 2022", (1005, 710),
                                   osd_font, osd_font_scale, osd_font_color, osd_font_thickness, osd_font_line_type)

            # change color space if testing
            if tu_settings.tu_video_stream_test:

                # convert image to RGB
                my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)

            # send image frame to judge sink
            sink_judge.schedule_frame(my_image)
