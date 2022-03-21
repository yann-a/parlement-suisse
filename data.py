import requests, json

def get_sessions():
    sessions = []
    page = 1
    while True:
        try:
            sessions_r = requests.get(f'http://ws-old.parlament.ch/sessions?pageNumber={page}&format=json', headers={'Accept': 'application/json', 'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
            sessions.extend(sessions_r.json())
            page += 1
        except:
            break

    return sessions

def get_legislative_periods():
    periods_r = requests.get(f'http://ws-old.parlament.ch/legislativeperiods?format=json', headers={'Accept': 'application/json', 'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
    periods = periods_r.json()

    return periods

def get_councillors(period):
    councillors = []
    page = 1
    while True:
        try:
            sessions_r = requests.get(f'http://ws-old.parlament.ch/councillors/historic?legislativePeriodFromFilter={period}&pageNumber={page}&format=json', headers={'Accept': 'application/json', 'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
            councillors.extend(sessions_r.json())
            page += 1
        except:
            break

    return councillors

def get_councillor(id):
    councillor_r = requests.get(f'http://ws-old.parlament.ch/councillors/{id}?format=json', headers={'Accept': 'application/json', 'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
    return councillor_r.json()

def get_votes_affairs(period):
    affairs = []
    page = 1
    while True:
        try:
            affairs_r = requests.get(f'http://ws-old.parlament.ch/votes/affairs?legislativePeriodFilter={period}&pageNumber={page}&format=json', headers={'Accept': 'application/json', 'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
            affairs.extend(affairs_r.json())
            page += 1
        except:
            break

    return affairs

def get_votes_affair(id):
    affair_r = requests.get(f'http://ws-old.parlament.ch/votes/affairs/{id}?format=json', headers={'Accept': 'application/json', 'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
    return affair_r.json()

def get_affair(id):
    affair_r = requests.get(f'http://ws-old.parlament.ch/affairs/{id}?format=json', headers={'Accept': 'application/json', 'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
    return affair_r.json()

def get_votes_councillor(id, page):
    number = get_councillor(id)['number']
    
    try:
        votes = requests.get(f'http://ws-old.parlament.ch/votes/councillors/{number}?pageNumber={page}&format=json', headers={'Accept': 'application/json', 'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
        return votes.json()
    except:
        return []
