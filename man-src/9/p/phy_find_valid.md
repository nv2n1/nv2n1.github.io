---
title: "phy_find_valid(9)"
name: "phy_find_valid"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_find_valid/"
---

phy_find_valid - find a PHY setting that matches the requested features mask

<h2>Synopsis</h2>

<pre><code>unsigned int phy_find_valid(unsigned int idx, u32 features);</code></pre>

<h2>Arguments</h2>

<i>idx</i>
<dl><dd><dd>The first index in settings[] to search</dl>
 

 <i>features</i>
<dl><dd>A mask of the valid settings</dl>

<h2>Description</h2>

Returns the index of the first valid setting less than or equal to the one pointed to by idx, as determined by the mask in features. Returns the index of the last setting if nothing else matches.

<h2>Copyright</h2>


