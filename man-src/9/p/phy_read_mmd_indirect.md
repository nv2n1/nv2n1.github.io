---
title: "phy_read_mmd_indirect(9)"
name: "phy_read_mmd_indirect"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_read_mmd_indirect/"
---

phy_read_mmd_indirect - reads data from the MMD registers

<h2>Synopsis</h2>

<pre><code>int phy_read_mmd_indirect(struct phy_device *phydev, int prtad, int devad);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>The PHY device bus</dl>
 

 <i>prtad</i>
<dl><dd>MMD Address</dl>
 

 <i>devad</i>
<dl><dd>MMD DEVAD</dl>

<h2>Description</h2>

it reads data from the MMD registers (clause 22 to access to clause 45) of the specified phy address. To read these register we have: 1) Write reg 13 // DEVAD 2) Write reg 14 // MMD Address 3) Write reg 13 // MMD Data Command for MMD DEVAD 3) Read reg 14 // Read MMD data

<h2>Copyright</h2>


