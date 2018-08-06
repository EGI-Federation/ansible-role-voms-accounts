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
This data is taken from the [Operations Portal](http://cclavoisier01.in2p3.fr:8080/lavoisier/vo-idcard?accept=json), and used to generate
the local user and group configurations.

Variables which guide the behaviour of the role are kept as usual in 
`defaults/main.yml` and `vars/main.yml`, or the site's `group_vars/`

Special attention should be paid to:

  - `vos` - A list of VO's which you want enabled on your site. This array has a few attributes:
    - `vos[vo_item][name]` - the name of the VO as written in the Operations Portal
    - `vos[vo_item][roles]`  -  the array of roles associated with the VO
      - `vos[vo_item][roles][role_item][name]` -  the name of the role as defined on the VOMS and Operations portal
      - `vos[vo_item][roles][role_item][pool_size]` - the size of the pool to create for the users mapped from this role.

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