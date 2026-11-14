---
title: "phy_check_valid(9)"
name: "phy_check_valid"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_check_valid/"
description: "phy_check_valid – check if there is a valid PHY setting which matches speed, duplex, and feature mask"
---

<p>phy_check_valid &#8211; check if there is a valid PHY setting which matches speed, duplex, and feature mask</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool phy_check_valid(int&nbsp;<wbr></code><i>speed</i><code>, int&nbsp;<wbr></code><i>duplex</i><code>, u32&nbsp;<wbr></code><i>features</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>speed</i></p>
<dl>
<dd>
<dd>speed to match</dl>
<p> <i>duplex</i></p>
<dl>
<dd>duplex to match</dl>
<p> <i>features</i></p>
<dl>
<dd>A mask of the valid settings</dl>
<h2>Description</h2>
<p>Returns true if there is a valid setting, false otherwise.</p>
<h2>Copyright</h2>
