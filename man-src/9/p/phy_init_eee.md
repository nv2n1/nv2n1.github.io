---
title: "phy_init_eee(9)"
name: "phy_init_eee"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_init_eee/"
---

phy_init_eee - init and check the EEE feature

<h2>Synopsis</h2>

<pre><code>int phy_init_eee(struct phy_device *phydev, bool clk_stop_enable);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>
 

 <i>clk_stop_enable</i>
<dl><dd>PHY may stop the clock during LPI</dl>

<h2>Description</h2>

it checks if the Energy-Efficient Ethernet (EEE) is supported by looking at the MMD registers 3.20 and 7.60/61 and it programs the MMD register 3.0 setting the "Clock stop enable" bit if required.

<h2>Copyright</h2>


