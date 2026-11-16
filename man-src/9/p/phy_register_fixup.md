---
title: "phy_register_fixup(9)"
name: "phy_register_fixup"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_register_fixup/"
---

phy_register_fixup - creates a new phy_fixup and adds it to the list

<h2>Synopsis</h2>

<pre><code>int phy_register_fixup(const char *bus_id, u32 phy_uid, u32 phy_uid_mask, int (*run)(struct phy_device *));</code></pre>

<h2>Arguments</h2>

<i>bus_id</i>
<dl><dd></dd><dd>A string which matches phydev-&gt;mdio.dev.bus_id (or PHY_ANY_ID)</dd></dl>
 

 <i>phy_uid</i>
<dl><dd>Used to match against phydev-&gt;phy_id (the UID of the PHY) It can also be PHY_ANY_UID</dd></dl>
 

 <i>phy_uid_mask</i>
<dl><dd>Applied to phydev-&gt;phy_id and fixup-&gt;phy_uid before comparison</dd></dl>
 

 <i>run</i>
<dl><dd>The actual code to be run when a matching PHY is found</dd></dl>

<h2>Copyright</h2>


