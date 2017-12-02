import requests
import os
import base64
import json

def send_request(pull_url):
    # Request
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
     #   print('Response HTTP Status Code: {status_code}'.format(
     #       status_code=response.status_code))
     #   print('Response HTTP Response Body: {content}'.format(
     #       content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    return response.content

def scrape_dfs(year):
    allMonths1 = ['10','11','12']
    allMonths2 = ['01','02','03','04']
    allDays = ['01','02','03','04','05','06','07','08','09'] + list(range(10,32))

    for month in allMonths1:
        for day in allDays:
            pull_url = 'https://api.mysportsfeeds.com/v1.1/pull/nhl/' + str(year) + '-' + str(year+1) + '-regular/daily_dfs.json?fordate=' + str(year) + str(month) + str(day)
            response = json.loads(send_request(2016))
            daily_dfs = response['dailydfs']['dfsentries']
            
            for dfs in daily_dfs:
              print dfs

    for month in allMonths2:
        for day in allDays:
            pull_url = 'https://api.mysportsfeeds.com/v1.1/pull/nhl/' + str(year) + '-' + str(year+1) + '-regular/daily_dfs.json?fordate=' + str(year+1) + str(month) + str(day)

def scrape_teams(year):
    allTeams = ['bos','cbj','tor','wpj','nyr','det','flo','tbl','mtl','ari','col','min','ott','phi','buf',
                'wsh','car','njd','stl','pit','nsh','sjs','ana','lak','van','cgy','nyi','chi','edm','dal']

    for team in allTeams:
        pull_url = 'https://api.mysportsfeeds.com/v1.1/pull/nhl/' + str(year) + '-' + str(year+1) + '-regular/team_gamelogs.json?team=' + team
        response = json.loads(send_request(pull_url))
        team_game_logs = response['teamgamelogs']['gamelogs']

    	for game_log in team_game_logs:
            print game_log

def scrape_player(year):
    allTeams = ['bos','cbj','tor','wpj','nyr','det','flo','tbl','mtl','ari','col','min','ott','phi','buf',
                'wsh','car','njd','stl','pit','nsh','sjs','ana','lak','van','cgy','nyi','chi','edm','dal']
    for team in allTeams:
        pull_url = 'https://api.mysportsfeeds.com/v1.1/pull/nhl/' + str(year) + '-' + str(year+1) + '-regular/player_gamelogs.json?team=' + team
        response = json.loads(send_request(pull_url))
        player_game_logs = response['playergamelogs']['gamelogs']

        for game_log in player_game_logs:
          print game_log

if __name__ == '__main__':
 
  host = 'localhost'
  username ='USERNAME'
  password = 'PASSWORD'
  database = 'DBNAME'

#  scrape_player(2016)
  scrape_teams(2016)

