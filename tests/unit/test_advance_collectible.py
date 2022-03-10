from random import random
from brownie import network
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENV, get_account, get_contract
from scripts.Advance_Collectible.deploy_and_create import deploy_create


def test_can_create_advanced_collectible():
    # deploy the contract
    # create an NFT
    # get a random breed back
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("Only for local testing")
    adv_collectible, tx = deploy_create()
    requestId = tx.events["requestCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, adv_collectible.address, {"from": get_account()}
    )

    assert adv_collectible.tokenCounter() == 1
    assert adv_collectible.tokenIdtoBreed(0) == random_number % 3
