---
title: "phy_start_machine(9)"
name: "phy_start_machine"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_start_machine/"
---

phy_start_machine - start PHY state machine tracking

<h2>Synopsis</h2>

<pre><code>void phy_start_machine(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>the phy_device struct</dl>

<h2>Description</h2>

The PHY infrastructure can run a state machine which tracks whether the PHY is starting up, negotiating, etc. This function starts the timer which tracks the state of the PHY. If you want to maintain your own state machine, do not call this function.

<h2>Copyright</h2>


