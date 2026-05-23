// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleStorage
 * @dev 一个最小的存储合约——只能存一个数字，然后读取它。
 * 
 * 这个合约只有两个函数：
 * - set(uint256): 写入一个数字（需要签名，花费 Gas）
 * - get(): 读取存储的数字（免费，不需要签名）
 * 
 * 用途：理解"写入"和"读取"的本质区别
 * - 写入 = 修改链上状态 = 需要交易 = 需要签名 = 需要 Gas
 * - 读取 = 查看链上状态 = 免费 = 不需要签名
 */
contract SimpleStorage {
    
    // 状态变量：存储一个数字
    uint256 private storedNumber;
    
    // 事件：当数字被修改时触发（方便在区块浏览器上看到变化）
    event NumberChanged(address indexed setter, uint256 oldValue, uint256 newValue);
    
    /**
     * @dev 写入函数：设置一个新的数字
     * 这是一个"写入"操作，会修改链上状态
     * 需要：钱包签名 + Gas 费
     */
    function set(uint256 _number) public {
        uint256 oldValue = storedNumber;
        storedNumber = _number;
        emit NumberChanged(msg.sender, oldValue, _number);
    }
    
    /**
     * @dev 读取函数：获取当前存储的数字
     * 这是一个"读取"操作，不会修改链上状态
     * 不需要：钱包签名 + Gas 费（完全免费）
     */
    function get() public view returns (uint256) {
        return storedNumber;
    }
}
