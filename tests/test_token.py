from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy_token import deploy_token
from brownie import network, accounts, exceptions
import pytest


def test_can_mint():
    account = get_account()
    prtoken = deploy_token()
    previousSupply = prtoken.totalSupply()
    owner = prtoken.owner()
    amount = 400 * 1000000000000000000
    tx = prtoken.mint(owner, amount, {"from": account})
    tx.wait(1)
    assert amount <= previousSupply
    assert prtoken.totalSupply() == previousSupply + amount


def test_can_burn():
    account = get_account()
    prtoken = deploy_token()
    previousSupply = prtoken.totalSupply()
    amount = 400 * 1000000000000000000
    tx = prtoken.burn(amount, {"from": account})
    tx.wait(1)
    assert prtoken.totalSupply() > 0
    assert prtoken.totalSupply() == previousSupply - amount


def test_owner():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    prtoken = deploy_token()
    bad_actor = accounts.add()
    amount = 400 * 1000000000000000000
    with pytest.raises(exceptions.VirtualMachineError):
        prtoken.mint(bad_actor, amount, {"from": bad_actor})
