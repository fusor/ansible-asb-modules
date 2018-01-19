#!/usr/bin/python

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: asb_last_operation
short_description: Adds a annotation to the pod running the apb with a last operation description
description:
     - Takes a string containting the last operation description this decription should be clear and concise. 
       This description is then added an an annotation to the pod executing the apb and read by the broker.
notes: []
requirements: []
author:
    - "Red Hat, Inc."
options:
  description:
    description:
      - 'string describing the last operation'
    required: true
    default: ""
env:
        - Set via the downward API on the APB Pod
        - name: ENV_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: ENV_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace      
'''

EXAMPLES = '''
- name: update last operation
  asb_last_operation:
    description:
      "10%: creating service route"
'''
RETURN = '''

'''

import json
import base64
import os
from ansible.module_utils.basic import AnsibleModule
try:
    from kubernetes import client, config
    config.load_kube_config()
    api = client.CoreV1Api()
except Exception as error:
    ansible_module.fail_json(msg="Error attempting to load kubernetes client: {}".format(error))

LAST_OPERATION_ANNOTATION = "apb_last_operation"
ENV_NAME = "POD_NAME"
ENV_NAMESPACE = "POD_NAMESPACE"


def main():

    argument_spec = string 

    ansible_module = AnsibleModule(argument_spec=argument_spec)

    if 'description' not in ansible_module.params:
        error, last operation requires a description
    
    if ENV_NAME not in os.environ:
        error, expected a POD_NAME in the environment

    if ENV_NAMESPACE not in os.environ:
        error, expected a POD_NAMESPACE in the environment

    lastOp = ansible_module.params['description']
    name = os.environ[ENV_NAME]
    namespace = os.environ[ENV_NAMESPACE]
    
    try:    
        pod = api.read_namespaced_pod(
        name=name,
        namespace=namespace
        )    

        pod.metadata.annotations[LAST_OPERATION_ANNOTATION] = lastOp
        api.replace_namespaced_pod(name=name,namespace=namespace,body=pod,pretty='true')
    except Exception as error:
        ansible_module.fail_json(msg="Error attempting to update pod with last operation annotation: {}".format(error))

    ansible_module.exit_json(changed=True, last_operation=lastOp)


if __name__ == '__main__':
    main()
