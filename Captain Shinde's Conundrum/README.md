# Navy Encode 

The **INS Vikramaditya** is considered the most powerful Indian Navy Vessel. The carrier was purchased by India on 20 January 2004 after years of negotiations at a final price of $2.35 billion. <br> <br> 
The Navy wish to test the capabilities of the warship and the people aboard it. For this purpose, they planned a field day where the ships firepower and the crew's efficiency was to be tested. <br> <br> 
There were to be a large number of dummy targets at different places throughouh a region of the sea, surrounding the ship. Each of these targets were of different sizes and could handle different levels of damage from Vikramaditya's guns and missiles. To land damage on each target, the warship needs a **specific ammo**. For example, ship with damage resistance 7 needs to be hit by ammo of damage capability 7 **ONLY**. However the ship could **not** fire simulateneously at the targets. This was meant to test how well the crew was able to allocate different sections of the ship for a task. If this was not enough, for each day of testing, the ship could only use **two** of its main guns ( both which are to be empty at the start of the day ). <br> The  ship also had to change its ammo and make sure to destory all of the targets in a certain timeframe to pass the test. Assume that there was no time waste in reloading, nor was there any lack of ammo. <br> <br. 
Captain Shinde realized that he instead of handling each target induvidually, he could choose targets and the ammo smartly, keeping in mind the time required to change the ammo required for each target. <br> <br> 
Help Captain Shinde out with this dilemna by creating a code to get the minimum number of times the ship requires to change ammo. 

**Input Format**

x, which gives the number of cases, <br> 
y, which gives the length of each case, <br> 
z, which contains the actual sequence of damage resistances

**Constraints**

1 ≤ x ≤ 5, 
1 ≤ y ≤ 100,
1 ≤ z ≤ 15

**Output Format**

For each case, your code should output the minimum number of times Captain Shinde needs to change the ships ammo

**Sample Input 0**

```
3
4
6 6 11 6 
6
5 2 7 8 5 5 
9
12 2 8 7 12 12 11 8 7
```

**Sample Output 0**

```
2
4
6
```

**Sample Explanation 0**

To be smart about the order in which ammo is changed, Capt. Shinde comes up with a great idea. For example, in the first sequence, he could start by loading ammo-6 to the first gun, and use the first gun two times to demolish two level-6 targets. Then he could use the second gun with ammo-11. This leaves the first gun still with ammo-6, which he can use for the last time. As a result, he changed the ammo **2 times**
