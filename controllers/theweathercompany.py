
class WeatherRegion:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def is_endangered(self):
        return True

    def parse(self):
        data = dict()
        data['type'] = 'hurricane'
        data['level'] = 6

        return data