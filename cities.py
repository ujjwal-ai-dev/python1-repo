cities={'ktm':{'population':9999999,'country':'nepal','fact':'capital city of Nepal'},
        'Patna':{'population':5677567,'country':'India','fact':'capital of bihar'},
        'paris':{'population':342332,'country':'France','fact':'capital of France'}}


for c,v in cities.items():
    print(c)
    print(f"\tpopulation: {v['population']} country: {v['country']} \n\tfact: {v['fact']}")
