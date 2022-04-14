from brownie import PRToken
from scripts.helpful_scripts import get_account, get_contract


def mint():
    account = get_account()
    prtoken = get_contract("prtoken")
    owner = prtoken.owner()
    amount = input("Enter the amount of tokens to mint: ")
    amount = int(amount) * 1000000000000000000
    print("Minting tokens...")
    tx = prtoken.mint(owner, amount, {"from": account})
    tx.wait(1)


def burn():
    account = get_account()
    prtoken = get_contract("prtoken")
    previousSupply = prtoken.totalSupply()
    amount = input("Enter the amount of tokens to burn: ")
    amount2 = int(amount) * 1000000000000000000
    tx = prtoken.burn(amount2, {"from": account})
    tx.wait(1)
    percent = amount2 / previousSupply * 100
    print(f"Burnt {amount} tokens, equal to {percent}% of the total supply!")


def total_supply():
    prtoken = get_contract("prtoken")
    supply = prtoken.totalSupply()
    print(f"The total supply is {supply / 10 ** 18} PRT")


def main():
    burn()
    total_supply()
