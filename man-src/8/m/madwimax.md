---
title: "madwimax(8)"
name: "madwimax"
section: "8"
letter: "m"
url: "/docs/linux/man/8-madwimax/"
description: "madwimax – driver for mobile WiMAX equipment based on Samsung CMC-730"
---

<p>madwimax &#8211; driver for mobile WiMAX equipment based on Samsung CMC-730</p>
<h2>Synopsis</h2>
<p><code>madwimax</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p><code>madwimax</code> is an experimental reverse-engineered linux driver for mobile WiMAX (802.16e) devices based on Samsung CMC-730 chip. These devices are currently supported:</p>
<dl>
<dt>*</p>
<dd>Samsung SWC-U200</p>
<dt>*</p>
<dd>Samsung SWC-E100</p>
<dt>*</p>
<dd>Samsung SWM-S10R (it is built in Samsung NC-10 netbook)</dl>
<p> The driver is completely user-space. It requires libusb-1.0 and TUN/TAP driver to work.</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;daemonize</code></p>
<dd>Daemonize after startup.</p>
<dt><code>&#8211;device</code>=<i>VID:PID</i></p>
<dd>Specify the USB device by <i>VID:PID</i> combination.</p>
<dt><code>-e</code> <i>FILE</i>, <code>&#8211;event-script</code>=<i>FILE</i></p>
<dd>Specify path to the event script.</p>
<dt><code>&#8211;exact-device</code>=<i>BUS/DEVICE</i></p>
<dd>Specify the exact USB <i>BUS/DEVICE</i> (use with care!).</p>
<dt><code>-f, &#8211;detach-dvd</code></p>
<dd>Detach pseudo-DVD kernel driver on startup.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Display help.</p>
<dt><code>-l</code> <i>FILE</i>, <code>&#8211;log-file</code>=<i>FILE</i></p>
<dd>Write log to the specified <i>FILE</i> instead of the other methods.</p>
<dt><code>-o, &#8211;diode-off</code></p>
<dd>Turn off the diode (diode is turned on by default).</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Switch off logging.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print the program version number.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Increase the log level.</p>
<dt><code>&#8211;ssid</code>=<i>SSID</i></p>
<dd>Specify service set identifier, or SSID, which is a friendly name that identifies a particular 802.16e wireless network.</dl>
<h2>Exit Status</h2>
<dl>
<dt><code>0</code></p>
<dd>Success</p>
<dt><code>1</code></p>
<dd>Failure (syntax or usage error; hardware error; underlying software error; unexpected error).</dl>
<h2>Bugs</h2>
<p>See the madwimax issue tracker: <a href="lahttp://code.google.com/p/madwimax/issues/listra">lahttp://code.google.com/p/madwimax/issues/listra</a></p>
<h2>Author</h2>
<p>Written by Alexander Gordeev, &lt;mailto:lasaine [at] lvk.cs.msu.su&gt;</p>
<h2>Resources</h2>
<p>Main web site: <a href="lahttp://code.google.com/p/madwimax/ra">lahttp://code.google.com/p/madwimax/ra</a></p>
<h2>Copying</h2>
<p>Copyright (C) 2008-2009 Alexander Gordeev. Free use of this software is granted under the terms of the GNU General Public License (GPL).</p>
