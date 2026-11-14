---
title: "victronups(8)"
name: "victronups"
section: "8"
letter: "v"
url: "/docs/linux/man/8-victronups/"
description: "victronups – Driver for IMV/Victron UPS unit Match, Match Lite, NetUps"
---

<p>victronups &#8211; Driver for IMV/Victron UPS unit Match, Match Lite, NetUps</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the the victronups driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The victronups driver should recognize all Victron models that use a serial protocol at 1200 bps. These include Match Lite, Match and the NetUps line. </p>
<p> The Match Lite line may only report a handful of variables. This is usually not a bug &#8211; they just don&#8217;t support anything else.</p>
<h2>Cabling</h2>
<p>If your Victron cable is broken or missing, use this diagram to build a clone: </p>
<p> docs/cables/victron.txt</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional setting in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>modelname</code>=<i>name</i></p>
<dl>
<dd>Set model name</dl>
<p> <code>usd</code>=<i>delay</i></p>
<dl>
<dd>Set delay before shutdown on UPS</dl>
<h2>Bugs</h2>
<p>The protocol for this UPS is not officially documented.</p>
<h2>Author</h2>
<p>Radek Benedikt &lt;benedikt [at] lphard.cz&gt;, Daniel Prynych &lt;Daniel.Prynych [at] hornet.cz&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
