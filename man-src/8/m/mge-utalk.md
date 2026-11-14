---
title: "mge-utalk(8)"
name: "mge-utalk"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mge-utalk/"
description: "mge-utalk – Driver for MGE UPS SYSTEMS UTalk protocol equipment"
---

<p>mge-utalk &#8211; Driver for MGE UPS SYSTEMS UTalk protocol equipment</p>
<h2>Synopsis</h2>
<p><code>mge-utalk</code> -h <code>mge-utalk</code> -a <i>UPS_NAME</i> [<i>OPTIONS</i>]</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This man page only documents the hardware-specific features of the mge-utalk driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8). </p>
<h2>Supported Hardware</h2>
<p>mge-utalk supports the following legacy units, using the MGE UTalk protocol: </p>
<dl>
<dd>
<pre>Pulsar ESV+,
Pulsar ES+,
Pulsar EL,
Pulsar EX,
Pulsar EXtreme,
Comet EXtreme,
Comet (Utalk Serial Card, ref 66060),
Galaxy (Utalk Serial Card, ref 66060).</pre>
</dl>
<p> This driver also support some newer models with backward UTalk compatibility, such as Pulsar Evolution and Pulsar EXtreme C. As these models also support the SHUT protocol, prefer mge-shut for serial communication, or use the USB port, if available, with the usbhid-ups driver.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>lowbatt</code>=<i>num</i></p>
<dl>
<dd>Set the low battery warning threshold at which shutdown is initiated by <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8). </p>
<p> The factory default value is 30 (in percent), and can be settable depending on the exact model.</dl>
<p> <code>offdelay</code>=<i>num</i></p>
<dl>
<dd>Set the timer before the UPS is turned off after the kill power command is sent (via the <code>-k</code> switch). </p>
<p> The default value is 20 (in seconds).</dl>
<p> <code>ondelay</code>=<i>num</i></p>
<dl>
<dd>Set the delay before the UPS is turned on, after the power returns. </p>
<p> The default value is 1 (in minutes).</dl>
<p> <code>oldmac</code></p>
<dl>
<dd>Set this flag if you are running Linux on an Oldworld Macintosh box (all beige Apple Macintosh). This might also be needed for other OSs (like *BSD) running on PowerMac.</dl>
<h2>Known Issues</h2>
<h3>Repetitive timeout and staleness</h3>
<p>Older models, such as ES/ESV ones, might report repetitive &quot;data stale&quot; errors. This is due to the fact that these models don&#8217;t support too much polling. To solve this problem, add &quot;pollinterval=20&quot; in ups.conf, and change the value of MAXAGE to 25 in upsd.conf, and DEADTIME to 25 in upsmon.conf.</p>
<h2>Author</h2>
<p>Hans Ekkehard Plesser, Arnaud Quette, Martin Loyer, Patrick Agrain, Nicholas Reilly, Dave Abbott, Marek Kralewski</p>
<h2>See Also</h2>
<h3>The core driver</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
