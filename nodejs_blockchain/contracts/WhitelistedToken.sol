// contracts/MyToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract WhitelistedToken is ERC20 {
    address public owner;
    mapping(address => bool) public whitelist;

    constructor(uint256 initialSupply) ERC20("WhitelistedToken", "WTK") {
        owner = msg.sender;
        _mint(owner, initialSupply);
    }

    // Function to add an address to the whitelist
    function addToWhitelist(address account) public {
        require(msg.sender == owner, "Only the owner can add to whitelist");
        whitelist[account] = true;
    }
    function removeFromWhitelist(address account) public {
        require(msg.sender == owner, "Only the owner can remove from whitelist");
        whitelist[account] = false;
    }

    // Override the transfer function to restrict it to whitelisted addresses
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(whitelist[recipient], "Recipient is not whitelisted");
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to restrict it to whitelisted addresses
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(whitelist[recipient], "Recipient is not whitelisted");
        return super.transferFrom(sender, recipient, amount);
    }

    // Award tokens function for owner to distribute
    function awardTokens(address recipient, uint256 amount) public {
        require(msg.sender == owner, "Only owner can award tokens");
        _transfer(owner, recipient, amount);
    }

    function decimals() public view virtual override returns (uint8){
        return 0;
    }
}