import tu_settings

tu_interop_compat_time = {
    "hour": {"locale": "saat", "type": int},  # local server time hour
    "minute": {"locale": "dakika", "type": int},  # local server time minute
    "second": {"locale": "saniye", "type": int},  # local server time second
    "millisecond": {"locale": "milisaniye", "type": int}  # local server time millisecond
}
"""
Time compatability declaration
"""

tu_interop_compat_team = {
    "team": {"locale": "takim_numarasi", "type": int},  # foe team number
    "latitude": {"locale": "iha_enlem", "type": float},  # foe team vehicle latitude
    "longitude": {"locale": "iha_boylam", "type": float},  # foe team vehicle longitude
    "altitude": {"locale": "iha_irtifa", "type": float},  # foe team vehicle altitude
    "roll": {"locale": "iha_yatis", "type": int},  # foe team vehicle roll
    "pitch": {"locale": "iha_dikilme", "type": int},  # foe team vehicle pitch
    "heading": {"locale": "iha_yonelme", "type": int},  # foe team vehicle heading
    "time": {"locale": "zaman_farki", "type": int}  # foe team time difference
}
"""
Team telemetry compatability declaration
"""

tu_interop_compat_send = {
    "team": {"locale": "takim_numarasi", "type": int},  # our team number
    "latitude": {"locale": "IHA_enlem", "type": float},  # our vehicle latitude
    "longitude": {"locale": "IHA_boylam", "type": float},  # our vehicle longitude
    "altitude": {"locale": "IHA_irtifa", "type": float},  # our vehicle altitude
    "roll": {"locale": "IHA_yatis", "type": int},  # our vehicle roll
    "pitch": {"locale": "IHA_dikilme", "type": int},  # our vehicle pitch
    "heading": {"locale": "IHA_yonelme", "type": int},  # our vehicle heading
    "speed": {"locale": "IHA_hiz", "type": int},  # our vehicle ground speed
    "battery": {"locale": "IHA_batarya", "type": int},  # our vehicle battery percentage
    "auto": {"locale": "IHA_otonom", "type": int},  # our vehicle is flying autonomous
    "target_lock": {"locale": "IHA_kilitlenme", "type": int},  # our target is locked
    "target_x": {"locale": "Hedef_merkez_X", "type": int},  # our target x position in frame
    "target_y": {"locale": "Hedef_merkez_Y", "type": int},  # our target y position in frame
    "target_width": {"locale": "Hedef_genislik", "type": int},  # our target width in frame
    "target_height": {"locale": "Hedef_yukseklik", "type": int},  # our target height in frame
    "time": {"locale": "GPSSaati", "type": dict}  # our system time
}
"""
Telemetry send compatability declaration
"""

tu_interop_compat_receive = {
    "time": {"locale": "sistemSaati", "type": dict},  # server time
    "team": {"locale": "konumBilgileri", "type": list}  # list of foe team telemetry
}
"""
Telemetry receive compatability declaration
"""

tu_interop_compat_lock = {
    "lock_start": {"locale": "kilitlenmeBaslangicZamani", "type": dict},  # target lock start time
    "lock_end": {"locale": "kilitlenmeBitisZamani", "type": dict},  # target lock end time
    "lock_auto": {"locale": "otonom_kilitlenme", "type": int},  # target lock in autonomous flight
}
"""
Target lock compatability declaration
"""

tu_interop_compat_login = {
    "user_name": {"locale": "kadi", "type": str},  # user name of server login system
    "user_password": {"locale": "sifre", "type": str},  # user password of server login system
}
"""
Server login compatability declaration
"""

tu_interop_compat_path_server_time = "http://{0}:{1}/api/{2}".format(tu_settings.tu_judge_server_ip,
                                                                     tu_settings.tu_judge_server_port,
                                                                     "sunucusaati")
"""
Server path to get server system time
"""

tu_interop_compat_path_server_send = "http://{0}:{1}/api/{2}".format(tu_settings.tu_judge_server_ip,
                                                                     tu_settings.tu_judge_server_port,
                                                                     "telemetri_gonder")
"""
Server path to post telemetry data and get foe team telemetry data
"""

tu_interop_compat_path_server_lock = "http://{0}:{1}/api/{2}".format(tu_settings.tu_judge_server_ip,
                                                                     tu_settings.tu_judge_server_port,
                                                                     "kilitlenme_bilgisi")
"""
Server path to post target lock data
"""

tu_interop_compat_path_server_login = "http://{0}:{1}/api/{2}".format(tu_settings.tu_judge_server_ip,
                                                                      tu_settings.tu_judge_server_port,
                                                                      "giris")
"""
Server path to login the competition round
"""

tu_interop_compat_path_server_logout = "http://{0}:{1}/api/{2}".format(tu_settings.tu_judge_server_ip,
                                                                       tu_settings.tu_judge_server_port,
                                                                       "cikis")
"""
Server path to logout the competition round
"""
