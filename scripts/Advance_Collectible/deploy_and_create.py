from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    get_contract,
)
from brownie import AdvanceCollectible, config, network


def deploy_create():
    account = get_account()
    print("[+] Deploying Contract ...")
    advanced_collectible = AdvanceCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=False,
    )
    print("[+] Contract Deployed!")

    fund_with_link(advanced_collectible.address)
    tx = advanced_collectible.createCollectible({"from": account})
    tx.wait(1)
    print("[+] New Token Has Been Created!")
    return advanced_collectible, tx


def main():
    deploy_create()
