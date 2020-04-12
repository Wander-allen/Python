def builtd_profile(first,last,**use_info):
    "创建一个字典，其中包含我们知道有关用户的一切"
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key,value in use_info.items():
        profile[key] = value
    return profile

user_profile = builtd_profile("tan","minhang",location = 'shanghai',field = 'math')

print(user_profile)
    
