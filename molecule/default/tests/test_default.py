import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_chronyd_installed(host):
    assert host.package("chrony").is_installed


def test_chronyd_service(host):
    service = host.service("chronyd")

    assert service.is_enabled


def test_gpsd_installed(host):
    assert host.package("gpsd").is_installed


def test_gpsd_service(host):
    service = host.service("gpsd")

    assert service.is_enabled
