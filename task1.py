import requests, time, json

deltatime = list()

iterations = 5

for i in range(iterations): 

    t = time.time()
    r = requests.get('https://yandex.com/time/sync.json?geo=213')
    print(r.text)

    timestamp_s = ((r.json())['time']) / 1000
    first_key = next(iter((r.json())['clocks']))
    utc = (r.json())['clocks'][first_key]['offsetString']
    print(time.asctime(time.localtime(timestamp_s)), utc)

    print("Δt:", timestamp_s - t)
    deltatime.append(timestamp_s - t)

print("avg Δt:", sum(deltatime) / iterations)
