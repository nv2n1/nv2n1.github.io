---
title: "phy_find_setting(9)"
name: "phy_find_setting"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_find_setting/"
---

phy_find_setting - find a PHY settings array entry that matches speed &amp; duplex

<h2>Synopsis</h2>

<pre><code>unsigned int phy_find_setting(int speed, int duplex);</code></pre>

<h2>Arguments</h2>

<i>speed</i>
<dl><dd><dd>speed to match</dl>
 

 <i>duplex</i>
<dl><dd>duplex to match</dl>

<h2>Description</h2>

Searches the settings array for the setting which matches the desired speed and duplex, and returns the index of that setting. Returns the index of the last setting if none of the others match.

<h2>Copyright</h2>


