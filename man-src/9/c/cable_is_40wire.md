---
title: "cable_is_40wire(9)"
name: "cable_is_40wire"
section: "9"
letter: "c"
url: "/docs/linux/man/9-cable_is_40wire/"
description: "cable_is_40wire – 40/80/SATA decider"
---

<p>cable_is_40wire &#8211; 40/80/SATA decider</p>
<h2>Synopsis</h2>
<pre><code>int cable_is_40wire(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>port to consider</dl>
<h2>Description</h2>
<p>This function encapsulates the policy for speed management in one place. At the moment we don&#8217;t cache the result but there is a good case for setting ap-&gt;cbl to the result when we are called with unknown cables (and figuring out if it impacts hotplug at all). </p>
<p> Return 1 if the cable appears to be 40 wire.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
