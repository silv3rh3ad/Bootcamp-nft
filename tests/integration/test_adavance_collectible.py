from brownie import network
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENV
from scripts.Advance_Collectible.deploy_and_create import deploy_create
import time


def test_can_create_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("Only for integration testing")
    adv_collectible, tx = deploy_create()
    time.sleep(60)

    assert adv_collectible.tokenCounter() == 1
