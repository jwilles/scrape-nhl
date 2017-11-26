import requests
import os
import base64

def send_request():
    # Request
    pull_url = 'https://api.mysportsfeeds.com/v1.1/pull/nhl/2016-2017-regular/daily_player_stats.json?fordate=20161026&playerstats=G,A,Pts,Sh'
    username = os.environ['sportUser']
    password = os.environ['sportPass']
    

    try:
        response = requests.get(
            url=pull_url,
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')



if __name__ == '__main__':
  send_request()

