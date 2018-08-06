# Tests for the infrastructure VOs - dteam, ops
import os
import testinfra.utils.ansible_runner as runner
testinfra_hosts = runner.AnsibleRunner(
  os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')



# ops group fixtures
def test_ops_groups(host, groupname):


# ops user fixtures.
def test_ops_users(host, username)