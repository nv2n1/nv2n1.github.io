---
title: "optiups(8)"
name: "optiups"
section: "8"
letter: "o"
url: "/docs/linux/man/8-optiups/"
description: "optiups – Driver for Opti-UPS (Viewsonic) UPS and Zinto D (ONLINE-USV) equipment"
---

<p>optiups &#8211; Driver for Opti-UPS (Viewsonic) UPS and Zinto D (ONLINE-USV) equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the optiups driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p><code>optiups</code> was originally written against a PowerES 280es in nut-0.45. It was revised for nut-2.0.1 and tested against a PowerES 420E. It is expected to work with at least the PowerES, PowerPS, and PowerVS models. </p>
<p> This driver additionally supports a Zinto D from ONLINE USV-Systeme AG because of their very similar commands, but it is unknown if it also works with other UPS from them. </p>
<p> This driver will not work with the PowerES stock serial cable. You will need to construct your own three conductor cable: </p>
<dl>
<dd>
<pre>UPS 6 -&gt; PC 3
UPS 9 -&gt; PC 2
UPS 4 -&gt; PC 5</pre>
</dl>
<p> The cable for Online-USV uses pin UPS 7 (not UPS 4) → PC 5.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) file: </p>
<p> <code>status_only</code></p>
<dl>
<dd>Only poll for critical status information. Without this, <code>optiups</code> (and all NUT drivers) poll all sorts of information from the UPS fairly often. It is probably not often enough to hurt anything, so this option probably is not very useful, unless you have a flaky serial connection or a highly loaded machine.</dl>
<p> <code>nowarn_noimp</code></p>
<dl>
<dd>Does not print warnings when the UPS reports that a variable is not implemented or not pollable. Without the option you will get a message sent to your system logs each time NUT polls the UPS. If you specify <code>nowarn_noimp</code>, this message will only be logged once.</dl>
<p> <code>fake_lowbatt</code></p>
<dl>
<dd>This forces the low battery flag true. Without it, if you want to test your UPS, you will have to unplug it and wait until the battery drops to a low/critical voltage level before NUT will respond and power down your system. With the flag, NUT should power down the system soon after you pull the plug. When you are done testing, you should remove this flag. </p>
<p> For basic shutdown configuration testing, the command <i>upsmon -c fsd</i> is preferred.</dl>
<p> <code>powerup</code></p>
<dl>
<dd>Zinto D from ONLINE-USV cannot be identified when switched to standby. Set this flag to allow the driver to power-up your Zinto UPS. This will also power-up your equipment connected to the UPS!</dl>
<h2>Bugs</h2>
<p>On the 420E, ups.serial and ups.temperature are unsupported features. This is not a bug in NUT or the NUT driver, just the way things are with this UPS.</p>
<h2>Author</h2>
<p>Russell Kroll, Scott Heavner, Matthias Goebl</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
