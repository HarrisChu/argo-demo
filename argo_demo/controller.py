# -*- coding: utf-8 -*-
from datetime import datetime

import requests

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    jsonify
)

blueprint = Blueprint("api", __name__, url_prefix="/api/v1", )


@blueprint.route("/hook", methods=["POST"])
def hook():
    """ receive the hook from GitHub """

    # TODO just a demo here
    data = {"resourceKind": "WorkflowTemplate", "resourceName": "tck",
            "submitOptions": {'parameters': ['name={}'.format(generate_nebula_name()), 'nebula-version=v2-nightly']}}
    resp = requests.post('https://192.168.8.96:30080/api/v1/workflows/argo/submit', verify=False, json=data)
    return jsonify(success=True)


def generate_nebula_name():
    now = datetime.now()
    return 'nebula{}'.format(now.strftime('%M%S%f'))
