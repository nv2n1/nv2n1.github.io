---
title: "phy_trigger_machine(9)"
name: "phy_trigger_machine"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_trigger_machine/"
---

phy_trigger_machine - trigger the state machine to run

<h2>Synopsis</h2>

<pre><code>void phy_trigger_machine(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>the phy_device struct</dl>

<h2>Description</h2>

There has been a change in state which requires that the state machine runs.

<h2>Copyright</h2>


