---
title: "phy_write_mmd_indirect(9)"
name: "phy_write_mmd_indirect"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_write_mmd_indirect/"
---

phy_write_mmd_indirect - writes data to the MMD registers

<h2>Synopsis</h2>

<pre><code>void phy_write_mmd_indirect(struct phy_device *phydev, int prtad, int devad, u32 data);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>The PHY device</dl>
 

 <i>prtad</i>
<dl><dd>MMD Address</dl>
 

 <i>devad</i>
<dl><dd>MMD DEVAD</dl>
 

 <i>data</i>
<dl><dd>data to write in the MMD register</dl>

<h2>Description</h2>

Write data from the MMD registers of the specified phy address. To write these register we have: 1) Write reg 13 // DEVAD 2) Write reg 14 // MMD Address 3) Write reg 13 // MMD Data Command for MMD DEVAD 3) Write reg 14 // Write MMD data

<h2>Copyright</h2>


