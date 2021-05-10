# -*- coding: utf-8 -*-
import requests


def test():
    resp = requests.get('https://192.168.8.96:30080/api/v1/workflows/argo/deploy-nebula-75c7m', verify=False)
    print(resp.json())

    data = {"resourceKind": "WorkflowTemplate", "resourceName": "deploy-nebula",
            "submitOptions": {'parameters': ['name=harris', 'nebula-version=v2-nightly']}}
    # resp = requests.post('https://192.168.8.96:30080/api/v1/workflows/argo/submit', verify=False, json=data)
    print(resp.content)
