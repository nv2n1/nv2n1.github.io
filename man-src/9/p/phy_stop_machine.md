---
title: "phy_stop_machine(9)"
name: "phy_stop_machine"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_stop_machine/"
---

phy_stop_machine - stop the PHY state machine tracking

<h2>Synopsis</h2>

<pre><code>void phy_stop_machine(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

Stops the state machine timer, sets the state to UP (unless it wasn't up yet). This function must be called BEFORE phy_detach.

<h2>Copyright</h2>


