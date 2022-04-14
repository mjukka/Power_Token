// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";

// PRToken contract

contract PRToken is ERC20, Ownable, ERC20Burnable, ERC20Snapshot {
    mapping(address => uint256) balances;
    mapping(address => mapping(address => uint256)) allowed;

    constructor() ERC20("Power Token", "PRT") {
        // 18 decimals
        _mint(msg.sender, 1000 * 10**decimals());
    }

    function snapshot() public onlyOwner {
        _snapshot();
    }

    function mint(address to, uint256 amount) public onlyOwner {
        require(amount <= totalSupply());
        _mint(to, amount);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) {
        super._beforeTokenTransfer(from, to, amount);
    }

    fallback() external payable {
        revert();
    }

    receive() external payable {
        // custom function code
    }
}
