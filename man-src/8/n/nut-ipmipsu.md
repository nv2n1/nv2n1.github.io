---
title: "nut-ipmipsu(8)"
name: "nut-ipmipsu"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nut-ipmipsu/"
description: "nut-ipmipsu – Driver for IPMI Power Supply Units (PSU)"
---

<p>nut-ipmipsu &#8211; Driver for IPMI Power Supply Units (PSU)</p>
<h2>Synopsis</h2>
<p><code>nut-ipmipsu</code> -h <code>nut-ipmipsu</code> -a <i>PSU_NAME</i> [<i>OPTIONS</i>]</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This driver is experimental, and still a work-in-progress. Feedback is encouraged. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This man page only documents the hardware-specific features of the nut-ipmipsu driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8). </p>
<h2>Supported Hardware</h2>
<p>This driver should support a wide range of PSUs through local IPMI interface. </p>
<p> nut-ipmipsu currently use the GNU FreeIPMI project, for IPMI implementation.</p>
<h2>Extra Arguments</h2>
<p>This driver doesn&#8217;t support any optional settings.</p>
<h2>Installation</h2>
<p>This driver is not built by default. You can build it by using &quot;configure &#8211;with-ipmi=yes&quot;. </p>
<p> You also need to give proper permissions on the local IPMI device file (/dev/ipmi0 for example) to allow the NUT user to access it. </p>
<p> An udev rules file (nut-ipmipsu.rules) is provided and automatically installed on udev enabled system. This file is generally installed in /etc/udev/rules.d/ or /lib/udev/rules.d/ on newer systems, to address the permission settings problem. For more information, refer to nut/scripts/udev/README.</p>
<h2>Instant Commands</h2>
<p>This driver doesn&#8217;t support any instant commands.</p>
<h2>Implementation</h2>
<p>The &quot;port&quot; value is used to identify the PSU. For instance, to target FRU 0x2, use the following in <code>ups.conf</code>: </p>
<dl>
<dd>
<pre>[pdu]
 driver = nut-ipmipsu
 port = id2</pre>
</dl>
<p> This driver will report various information related to a PSU, including: </p>
<dl>
<dd>&bull; manufacturer, model, serial and part numbers,</dl>
<dl>
<dd>&bull; nominal voltage and frequency,</dl>
<dl>
<dd>&bull; actual current and voltage,</dl>
<dl>
<dd>&bull; status of the PSU: </p>
<dl>
<dd>&bull; </p>
<p> <i>OL</i> means that the PSU is present and providing power,</dl>
<dl>
<dd>&bull; </p>
<p> <i>OFF</i> means that the PSU is present but not providing power (power cable removed),</dl>
<dl>
<dd>&bull; </p>
<p> <i>stale</i> (no data) means that the PSU is not present (ie physically removed).</dl>
</dl>
<p> Here is an example output for a Dell r610 server: </p>
<dl>
<dd>
<pre>device.mfr: DELL
device.mfr.date: 01/05/11 - 08:51:00
device.model: PWR SPLY,717W,RDNT
device.part: 0RN442A01
device.serial: CN179721130031
device.type: psu
driver.name: nut-ipmipsu
driver.parameter.pollinterval: 2
driver.parameter.port: id2
driver.version: 2.6.1-3139M
driver.version.data: IPMI PSU driver
driver.version.internal: 0.01
input.current: 0.20
input.frequency.high: 63
input.frequency.low: 47
input.voltage: 232.00
input.voltage.maximum: 264
input.voltage.minimum: 90
ups.id: 2
ups.realpower.nominal: 717
ups.status: OL
ups.voltage: 12</pre>
</dl>
<h2>Author</h2>
<p>Arnaud Quette &lt;arnaud.quette [at] free.fr&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> GNU FreeIPMI home page: <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
