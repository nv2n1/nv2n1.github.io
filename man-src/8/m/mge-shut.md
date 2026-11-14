---
title: "mge-shut(8)"
name: "mge-shut"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mge-shut/"
description: "mge-shut – Driver for SHUT Protocol UPS equipment"
---

<p>mge-shut &#8211; Driver for SHUT Protocol UPS equipment</p>
<h2>Synopsis</h2>
<p><code>mge-shut</code> -h <code>mge-shut</code> -a <i>UPS_NAME</i> [<i>OPTIONS</i>]</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This man page only documents the hardware-specific features of the mge-shut driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8). </p>
<h2>Supported Hardware</h2>
<p>mge-shut supports all recent Eaton, MGE and Dell UPS models which use the SHUT (Serial HID UPS Transfer) protocol. </p>
<p> Older MGE models, such as Pulsar ESV+, Pulsar EX and Pulsar ES+, use the U-Talk protocol and should use the mge-utalk driver.</p>
<h2>Extra Arguments</h2>
<p>This driver also supports the following optional settings: </p>
<p> <code>lowbatt</code>=<i>num</i></p>
<dl>
<dd>Set the low battery warning threshold at which shutdown is initiated by <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8). </p>
<p> The factory default value is 30 (in percent), and can be settable depending on the exact model.</dl>
<p> <code>offdelay</code>=<i>num</i></p>
<dl>
<dd>Set the timer before the UPS is turned off after the kill power command is sent (via the <code>-k</code> switch). </p>
<p> The default value is 20 (in seconds). Usually this <code>must be lower</code> than <i>ondelay</i>, but the driver will <code>not</code> warn you upon startup if it isn&#8217;t.</dl>
<p> <code>ondelay</code>=<i>num</i></p>
<dl>
<dd>Set the timer for the UPS to switch on in case the power returns after the kill power command had been sent but before the actual switch off. This ensures the machines connected to the UPS are, in all cases, rebooted after a power failure. </p>
<p> The default value is 30 (in seconds). Usually this <code>must be greater</code> than offdelay, but the driver will <code>not</code> warn you upon startup if it isn&#8217;t. Some UPS&#8217;es will restart no matter what, even if the power is (still) out at the moment this timer elapses. In that case, you could try if setting <i>ondelay = -1</i> in <code>ups.conf</code> helps. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 ondelay parameter was set in ten seconds unit in the legacy mge-shut driver ( 3 for 30 seconds) . It is now set in seconds ( 30 for 30 seconds). Make sure you use the correct unit in your configuration. </p>
</dl>
</dl>
<p> <code>notification</code>=<i>num</i></p>
<dl>
<dd>Set notification type to 1 (no), 2 (light) or 3 (yes). </p>
<p> This argument is ignored. It is only here for backward compatibility.</dl>
<h2>Known Issues</h2>
<h3>Repetitive timeout and staleness</h3>
<p>Some models tends to be unresponsive with the default polling frequency. The result is that you have some &quot;data stale&quot; errors in your system log. </p>
<p> In this case, simply modify the general parameter &quot;pollinterval&quot; to a higher value (like 10 for 10 seconds). This should solve the issue. </p>
<p> Using <i>notification=3</i> might also help.</p>
<h2>Author</h2>
<p>Arnaud Quette</p>
<h2>See Also</h2>
<h3>The core driver</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
