---
title: "phy_ethtool_sset(9)"
name: "phy_ethtool_sset"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_ethtool_sset/"
description: "phy_ethtool_sset – generic ethtool sset function, handles all the details"
---

<p>phy_ethtool_sset &#8211; generic ethtool sset function, handles all the details</p>
<h2>Synopsis</h2>
<pre><code>int phy_ethtool_sset(struct phy_device *phydev, struct ethtool_cmd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>phydev</i></p>
<dl>
<dd>
<dd>target phy_device struct</dl>
<p> <i>cmd</i></p>
<dl>
<dd>ethtool_cmd</dl>
<h2>Description</h2>
<p>A few notes about parameter checking: &#8211; We don&#8217;t set port or transceiver, so we don&#8217;t care what they were set to. &#8211; <code>phy_start_aneg</code> will make sure forced settings are sane, and choose the next best ones from the ones selected, so we don&#8217;t care if ethtool tries to give us bad values.</p>
<h2>Copyright</h2>
