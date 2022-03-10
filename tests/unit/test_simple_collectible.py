import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENV, get_account
from brownie import network
from scripts.Simple_Collectible.deploy_and_create import deploy_create


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip()
    simple_collectible = deploy_create()
    assert simple_collectible.owner0f(0) == get_account()
