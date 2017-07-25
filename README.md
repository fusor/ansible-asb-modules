asb-modules
=========

This role loads modules for [Ansible Service Broker](https://github.com/openshift/ansible-service-broker) and is intended for execution from [Ansible Playbook Bundles](https://github.com/fusor/ansible-playbook-bundle).  It is included in apb-base so all modules should be available if your image is built `FROM ansibleplaybookbundle/apb-base`


Installation and use
----------------

Use the Galaxy client to install the role:

```
$ ansible-galaxy install ansibleplaybookbundle.asb-modules
```

Once installed, use the modules in playbook or role:
```yaml
- name: Encodes fields for Ansible Service Broker
  roles:
    - ansibleplaybookbundle.asb-modules
  tasks:
    - name: encode bind credentials
      asb_encode_binding:
        fields:
          ENV_VAR: "value"
          ENV_VAR2: "value2"
```
Ansible Service Broker will read the encoded credentials as part of running a task (e.g. provision, bind)

License
-------

Apache V2
