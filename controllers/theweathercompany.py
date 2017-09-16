import requests
from controllers.constants import *


category = {
    'Geo': 'Geophysical',
    'Met': 'Meteorological',
    'Safety': 'Public safety',
    'Security': 'Security',
    'Rescue': 'Rescue and recovery',
    'Fire': 'Fire',
    'Health': 'Public health',
    'Env': 'Environment',
    'Transport': 'Transportation',
    'Infra': 'Infrastructure',
    'CBRNE': 'Chemical, Biological, Radiological, Nuclear or High-Yield Explosive threat or attack',
    'Other': 'Other events',
}

severity = {
    'Extreme': 'Extraordinary threat to life or property',
    'Severe': 'Significant threat to life or property',
    'Moderate': 'Possible threat to life or property',
    'Minor': 'Minimal to no known threat to life or property',
    'Unknown': 'Severity unknown',
}

response_type = {
    'Shelter': 'Take shelter in place or per instruction',
    'Evacuate': 'Relocate as instructed in the instruction',
    'Prepare': 'Make preparations per the instruction',
    'Execute': 'Execute a pre-planned activity identified in instruction',
    'Avoid': 'Avoid the subject event as per the instruction',
    'Monitor': 'Attend to information sources as described in instruction',
    'AllClear': 'The subject event no longer poses a threat or concern and any follow on action is described in the data element instruction',
    'None': 'No action recommended',
    'Assess': '...'
}


class WeatherRegion:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
        self.endangered = None
        self.alerts = []

        self.__get_alerts()

    def __get_alerts(self):
        raw = requests.get(WEATHER_ALERTS_URL.format(self.lat, self.lng))
        json = raw.json()
        self.endangered = json['metadata']['status_code'] == 200

        if self.endangered:
            self.alerts = json['alerts']

    def is_endangered(self):
        return self.endangered

    def get_alerts(self):
        return self.alerts

    def prepare_information(self):
        data = dict()
        alerts = self.get_alerts()
        data['endangered'] = self.is_endangered()
        data['alerts'] = []

        for alert in alerts:
            alert_dict = dict()
            alert_dict['headline'] = alert['headline_text']
            alert_dict['msg_type'] = alert['msg_type']
            alert_dict['event_desc'] = alert['event_desc']
            alert_dict['area_name'] = alert['area_name']
            alert_dict['severity'] = severity[alert['severity']]
            alert_dict['severity_level'] = alert['severity_cd']
            alert_dict['source'] = alert['source']
            alert_dict['categories'] = []
            alert_dict['instructions'] = []

            for cat in alert['categories']:
                alert_dict['categories'].append(category[cat['category']])

            for instruction in alert['response_types']:
                alert_dict['instructions'].append(response_type[instruction['response_type']])

            data['alerts'].append(alert_dict)


        return data

