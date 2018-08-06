# Ansible Role VOMS Accounts

[![Build Status](https://travis-ci.org/EGI-Foundation/ansible-role-voms-accounts.svg?branch=master)](https://travis-ci.org/EGI-Foundation/ansible-role-voms-accounts)

This is an Ansible role for providing the pool accounts which are required by voms-enabled
UMD endpoints such as worker nodes, CREAM compute elements, storage elements, _etc._.
It follows the [YAIM 4 guide](https://twiki.cern.ch/twiki/bin/view/LCG/YaimGuide400#User_configuration_in_YAIM) on
user and group management.
This role deals with _local_ user management. If you have a site-wide user management system, it
can be used to synchronise or manage that, but the default usage is for creation of accounts 
consonant with VOMS roles on the endpoints directly.

## Requirements

None.

## Role Variables

VOMS roles are used as input to generate the data from which to create the users.

## Dependencies

There are no explicit dependencies, however this role is usually used with the other
roles which express a UMD function such as compute, execute, storage, etc.

## Example Playbook


```yaml
    - hosts: worker-nodes
      roles:
         - { role: EGI-Foundation.umd, release: 4 }
         - { role: EGI-Foundation.voms-client }
         - ansible-role-voms-accounts
```

## License

Apache-2.0

## Author Information

See [AUTHORS.md](AUTHORS.md)