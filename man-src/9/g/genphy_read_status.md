---
title: "genphy_read_status(9)"
name: "genphy_read_status"
section: "9"
letter: "g"
url: "/docs/linux/man/9-genphy_read_status/"
---

genphy_read_status - check the link status and update current link state

<h2>Synopsis</h2>

<pre><code>int genphy_read_status(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

Check the link, then figure out the current state by comparing what we advertise with what the link partner advertises. Start by checking the gigabit possibilities, then move on to 10/100.

<h2>Copyright</h2>


