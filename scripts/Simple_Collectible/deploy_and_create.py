from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

simple_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=pug.pn"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy_create():
    account = get_account()
    simplecollectible = SimpleCollectible.deploy({"from": account})
    tx = simplecollectible.createCollectible(simple_token_uri, {"from": account})
    tx.wait(2)

    print(
        f"[+] NFT can be visible at : {OPENSEA_URL.format(simplecollectible.address, simplecollectible.tokenCounter() - 1)}"
    )
    return simplecollectible


def main():
    deploy_create()
