---
title: "genphy_config_advert(9)"
name: "genphy_config_advert"
section: "9"
letter: "g"
url: "/docs/linux/man/9-genphy_config_advert/"
---

genphy_config_advert - sanitize and advertise auto-negotiation parameters

<h2>Synopsis</h2>

<pre><code>int genphy_config_advert(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

Writes MII_ADVERTISE with the appropriate values, after sanitizing the values to make sure we only advertise what is supported. Returns &lt; 0 on error, 0 if the PHY's advertisement hasn't changed, and &gt; 0 if it has changed.

<h2>Copyright</h2>


