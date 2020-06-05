import os

import yaml

with open("../Data/data.yaml","r",encoding="utf-8")as f:
    data_result = yaml.safe_load(f)
    data_list = []
    for i in data_result:
        data_list.append(i.get())


    print(data_result.values())
