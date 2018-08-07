# Tests for the infrastructure VOs - dteam, ops
import os
import pytest
import testinfra.utils.ansible_runner as runner
testinfra_hosts = runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# ops group fixtures
@pytest.mark.parametrize("groupname,gid", [
    ("ops", 45000),
    ("dteam", 46000)
    ])
def test_ops_groups(host, groupname, gid):
    assert host.group(groupname).exists
    assert host.group(groupname).gid == gid


# ops user fixtures.
@pytest.mark.parametrize("username,uid", [
    ("ops001", 45001)
    ])
def test_ops_users(host, username, uid):
    assert host.user(username).name == username
    assert host.user(username).uid == uid
