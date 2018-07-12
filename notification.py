# -*- coding: utf-8 -*-

import json

import requests
from WazeRouteCalculator import WazeRouteCalculator

def last_notifiaction_time(actual_time):
    file = open("last_notification_data.json", "r+")
    data = json.load(file)
    last_notification_time = data['last_notification_time']
    data['last_notification_time'] = actual_time
    file.seek(0)  # rewind
    json.dump(data, file)
    file.truncate()
    return last_notification_time


def notification_color(actual_time):
    last_time = last_notifiaction_time(actual_time)
    if actual_time == last_time:
        return "#0000FF"
    elif actual_time < last_time:
        return "#088A08"
    return "#FF0000"


def notification():
    file = open("config.json", "r")
    data = json.load(file)
    url = data['url']
    for user in data['users']:
        route = WazeRouteCalculator(user['from_address'], user['to_address'], user['region'])
        result = route.calc_route_info()
        color = notification_color(result[0])
        notification = {
            "attachments": [
                {
                    "color": color,
                    "author_name": "oxydedefer",
                    "author_link": "https://github.com/oxydedefer",
                    "author_icon": "https://png.icons8.com/metro/1600/car.png",
                    "text": "@{0}".format(user['username']),
                    "link_names":1,
                    "fields": [
                        {
                            "title": "Time of your ride:",
                            "value": "{0:.2f} for {1:.2f} km".format(result[0], result[1]),
                            "short": False
                        }
                    ]
                }
            ]
        }

        requests.post(url, json=notification)


if __name__ == '__main__':
    notification()
