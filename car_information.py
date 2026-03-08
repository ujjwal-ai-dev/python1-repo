def car_info(manufacturer,moodel_name,*special_request,**others):
    profile={}
    profile['manufaturer name']=manufacturer
    profile['model name']=moodel_name
    profile['special_request']=special_request
    for key,values in others.items():
        profile[key]=values
    return profile  