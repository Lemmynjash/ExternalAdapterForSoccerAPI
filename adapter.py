from bridge import Bridge


class Adapter:
    player_id = '90026531'
    round_id = '1'
    base_url = 'https://api.sportsdata.io/v3/soccer/stats/json/PlayerSeasonStatsByPlayer/' + \
        round_id+'/'+player_id+'?key=c356df0197c44f239dbd4faf213fbcd1'

    def __init__(self, input):
        self.bridge = Bridge()
        self.create_request()

    def create_request(self):
        try:
            response = self.bridge.request(self.base_url)
            data = response.json()
            self.result_success(data)
        except Exception as e:
            self.result_error(e)
        finally:
            self.bridge.close()

    def result_success(self, data):
        self.result = {
            'jobRunID': 1,
            'data': data,
            'result': data[0]['PlayerId'],
            'statusCode': 200,
        }

    def result_error(self, error):
        self.result = {
            'jobRunID': 1,
            'status': 'errored',
            'error': f'There was an error: {error}',
            'statusCode': 500,
        }
