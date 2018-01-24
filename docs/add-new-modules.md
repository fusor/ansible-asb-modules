# Adding New Modules

This document will cover the basics of creating a new apb module and testing the module.


## Writing the module

Modules go under the library folder and should be named after the module they provide. For example the module for providing a last_operation update is named: ```asb_last_operation.py```

The module should be well documented with clear examples provided.

Before writing a new module, it is recommended to create an issue on this repo outlining the functionality that you would like to see the module provide. This will promote discussion and a sharing of ideas to come up with the correct solution before any code has been written.

## Testing the module

The apb modules are intended to run from within the context of a Docker image as part of a POD running in a Kubernetes or Openshift environment. They regularly will need to interact with resources created within these environments. In order to test your module you will need to take the following steps.

1) Create or reuse an existing APB

2) Modify your Docker image to add your python module file to the following location:
``` /etc/ansible/roles/ansibleplaybookbundle.asb-modules/library/ ```

Example:

``` 
COPY asb_last_operation.py /etc/ansible/roles/ansibleplaybookbundle.asb-modules/library/ 
```

3) In your apb playbooks add calls to your new module.

4) Build a new image and push it to your docker org

5) Ensure your ansible service broker is configured to look for apbs in the docker org where you have pushed the test apb

6) Perform the action that will call the playbook where your module is called from (provision,bind,update,deprovision, unbind)

## Debugging 

To debug the module, you can login to your cluster as a cluster admin then view the logs of the apb pod that is created, if there is a problem with your module, these logs should give you insight into what is happening.