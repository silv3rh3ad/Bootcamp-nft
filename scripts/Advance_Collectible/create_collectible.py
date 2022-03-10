from web3 import Web3
from scripts.helpful_scripts import get_account, fund_with_link
from brownie import AdvanceCollectible


def main():
    account = get_account()
    advancecollectible = AdvanceCollectible[-1]
    fund_with_link(advancecollectible.address, amount=Web3.toWei(0.1, "ether"))
    tx = advancecollectible.createCollectible({"from": account})
    tx.wait(1)
    print("[+] Collectible Created")
