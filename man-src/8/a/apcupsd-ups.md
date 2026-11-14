---
title: "apcupsd-ups(8)"
name: "apcupsd-ups"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apcupsd-ups/"
description: "apcupsd-ups – Driver for apcupsd client access"
---

<p>apcupsd-ups &#8211; Driver for apcupsd client access</p>
<h2>Note</h2>
<p>This man page only documents the specific features of the <code>apcupsd-ups</code> driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Description</h2>
<p>This driver is a client to <code>apcupsd</code>. </p>
<p> <code>apcupsd-ups</code> acts as an <code>apcupsd</code> client, simply forwarding data. This can be useful in cases where both protocols are required in a network, or in case apcupsd has a required UPS access mode missing from NUT.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in <code><a href="/docs/linux/man/5-nut-conf/">nut.conf</a></code>(5): </p>
<p> <code>port</code>=&lt;hostname&gt;[:&lt;port&gt;]</p>
<dl>
<dd>This is the name of a remote host running apcupsd (plus an optional port).</dl>
<p> For instance: </p>
<dl>
<dd>
<pre>[apcupsd]
 driver = apcupsd-ups
 port = localhost
 desc = &quot;apcupsd client&quot;</pre>
</dl>
<h2>Background</h2>
<p>This driver was originally written in one evening to allow interworking with <code>apcupsd</code>.</p>
<h2>Supported Variables</h2>
<p>The following variables are translated from <code>apcupsd</code> to NUT. All times should be converted to seconds (please file a bug if you notice a mismatch in units). </p>
<table BORDER>
<tr VALIGN=top>
<td><code> apcupsd variable </code></td>
<td><code> NUT variable(s) </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> BCHARGE </td>
<td>
<p> battery.charge
</td>
</tr>
<tr VALIGN=top>
<td>
<p> MBATTCHG </td>
<td>
<p> battery.charge.low
</td>
</tr>
<tr VALIGN=top>
<td>
<p> RETPCT </td>
<td>
<p> battery.charge.restart
</td>
</tr>
<tr VALIGN=top>
<td>
<p> BATTDATE </td>
<td>
<p> battery.date
</td>
</tr>
<tr VALIGN=top>
<td>
<p> TIMELEFT </td>
<td>
<p> battery.runtime
</td>
</tr>
<tr VALIGN=top>
<td>
<p> MINTIMEL </td>
<td>
<p> battery.runtime.low
</td>
</tr>
<tr VALIGN=top>
<td>
<p> BATTV </td>
<td>
<p> battery.voltage
</td>
</tr>
<tr VALIGN=top>
<td>
<p> NOMBATTV </td>
<td>
<p> battery.voltage.nominal
</td>
</tr>
<tr VALIGN=top>
<td>
<p> LINEFREQ </td>
<td>
<p> input.frequency
</td>
</tr>
<tr VALIGN=top>
<td>
<p> SENSE </td>
<td>
<p> input.sensitivity
</td>
</tr>
<tr VALIGN=top>
<td>
<p> HITRANS </td>
<td>
<p> input.transfer.high
</td>
</tr>
<tr VALIGN=top>
<td>
<p> LOTRANS </td>
<td>
<p> input.transfer.low
</td>
</tr>
<tr VALIGN=top>
<td>
<p> LASTXFER </td>
<td>
<p> input.transfer.reason
</td>
</tr>
<tr VALIGN=top>
<td>
<p> LINEV </td>
<td>
<p> input.voltage
</td>
</tr>
<tr VALIGN=top>
<td>
<p> MAXLINEV </td>
<td>
<p> input.voltage.maximum
</td>
</tr>
<tr VALIGN=top>
<td>
<p> MINLINEV </td>
<td>
<p> input.voltage.minimum
</td>
</tr>
<tr VALIGN=top>
<td>
<p> NOMINV </td>
<td>
<p> input.voltage.nominal
</td>
</tr>
<tr VALIGN=top>
<td>
<p> LINEFREQ </td>
<td>
<p> output.frequency
</td>
</tr>
<tr VALIGN=top>
<td>
<p> OUTPUTV </td>
<td>
<p> output.voltage
</td>
</tr>
<tr VALIGN=top>
<td>
<p> NOMOUTV </td>
<td>
<p> output.voltage.nominal
</td>
</tr>
<tr VALIGN=top>
<td>
<p> DATE </td>
<td>
<p> ups.date, ups.time
</td>
</tr>
<tr VALIGN=top>
<td>
<p> DSHUTD </td>
<td>
<p> ups.delay.shutdown
</td>
</tr>
<tr VALIGN=top>
<td>
<p> DWAKE </td>
<td>
<p> ups.delay.start
</td>
</tr>
<tr VALIGN=top>
<td>
<p> FIRMWARE </td>
<td>
<p> ups.firmware, ups.firmware.aux
</td>
</tr>
<tr VALIGN=top>
<td>
<p> UPSNAME </td>
<td>
<p> ups.id
</td>
</tr>
<tr VALIGN=top>
<td>
<p> LOADPCT </td>
<td>
<p> ups.load
</td>
</tr>
<tr VALIGN=top>
<td>
<p> MANDATE </td>
<td>
<p> ups.mfr.date
</td>
</tr>
<tr VALIGN=top>
<td>
<p> NOMPOWER </td>
<td>
<p> ups.realpower.nominal
</td>
</tr>
<tr VALIGN=top>
<td>
<p> SERIALNO </td>
<td>
<p> ups.serial
</td>
</tr>
<tr VALIGN=top>
<td>
<p> STATUS </td>
<td>
<p> ups.status
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ITEMP </td>
<td>
<p> ups.temperature
</td>
</tr>
<tr VALIGN=top>
<td>
<p> STESTI </td>
<td>
<p> ups.test.interval
</td>
</tr>
<tr VALIGN=top>
<td>
<p> SELFTEST </td>
<td>
<p> ups.test.result
</td>
</tr>
</table>
<h2>Limitations</h2>
<p>Access to <code>apcupsd</code> is strictly read only: no commands can be issued. This stems from the design of <code>apcupsd</code>, where the settings are changed in <code>apctest</code>. In order to run <code>apctest</code>, <code>apcupsd</code> must be stopped (and <code>apcupsd</code> exposes the UPS to the network).</p>
<h2>Author</h2>
<p>Andreas Steinmetz</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet Resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> The apcupsd home page: <a rel="nofollow" href="http://www.apcupsd.org/">http://www.apcupsd.org/</a> </p>
