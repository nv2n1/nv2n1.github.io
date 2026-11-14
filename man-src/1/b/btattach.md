---
title: "btattach(1)"
name: "btattach"
section: "1"
letter: "b"
url: "/docs/linux/man/1-btattach/"
description: "btattach – Attach serial devices to BlueZ stack"
---

<h2 class="name">NAME</h2>
<p> btattach &#8211; Attach serial devices to BlueZ stack </p>
<h2>SYNOPSIS</h2>
<p> <code>btattach</code> [<code>-B</code> <i>device</i>] [<code>-A</code> <i>device</i>] [<code>-P</code> <i>protocol</i>] [<code>-R</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-btattach/">btattach</a>(1)</code> is used to attach a serial UART to the Bluetooth stack as a transport interface.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-B</code><i>&nbsp;device</i>,<code>&nbsp;&#8211;brder</code><i>&nbsp;device</i></p>
<dd> Attach a BR/EDR controller</p>
<dt><code>-A</code><i>&nbsp;device</i>,<code>&nbsp;&#8211;amp</code><i>&nbsp;device</i></p>
<dd> Attach an AMP controller</p>
<dt><code>-P</code><i>&nbsp;protocol</i>,<code>&nbsp;&#8211;protocol</code><i>&nbsp;protocol</i></p>
<dd> Specify the protocol type for talking to the device. </p>
<p> Supported values are: <center></p>
<table>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>protocol</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> h4
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> bcsp
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 3wire
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> h4ds
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> ll
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> ath3k
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> intel
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> bcm
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> qca
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>-S</code><i>&nbsp;baudrate</i>,<code>&nbsp;&#8211;speed</code><i>&nbsp;baudrate</i></p>
<dd> Specify wich baudrate to use</p>
<dt><code>-N</code>,<code> &#8211;noflowctl</code></p>
<dd> Disable flow control</p>
<dt><code>-v</code>,<code> &#8211;version</code></p>
<dd> Show version</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Show help options</dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
<h2>Index</h2>
