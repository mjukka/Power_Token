from brownie import PRToken, config, network
from scripts.helpful_scripts import get_account


def deploy_token():
    account = get_account()
    prtoken = PRToken.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"Contract deployed to {prtoken.address}")
    return prtoken


def main():
    deploy_token()
