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
<dt>*</dt>
<dd>Samsung SWC-U200</dd>
<dt>*</dt>
<dd>Samsung SWC-E100</dd>
<dt>*</dt>
<dd>Samsung SWM-S10R (it is built in Samsung NC-10 netbook)</dd></dl>
<p> The driver is completely user-space. It requires libusb-1.0 and TUN/TAP driver to work.</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;daemonize</code></dt>
<dd>Daemonize after startup.</dd>
<dt><code>&#8211;device</code>=<i>VID:PID</i></dt>
<dd>Specify the USB device by <i>VID:PID</i> combination.</dd>
<dt><code>-e</code> <i>FILE</i>, <code>&#8211;event-script</code>=<i>FILE</i></dt>
<dd>Specify path to the event script.</dd>
<dt><code>&#8211;exact-device</code>=<i>BUS/DEVICE</i></dt>
<dd>Specify the exact USB <i>BUS/DEVICE</i> (use with care!).</dd>
<dt><code>-f, &#8211;detach-dvd</code></dt>
<dd>Detach pseudo-DVD kernel driver on startup.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display help.</dd>
<dt><code>-l</code> <i>FILE</i>, <code>&#8211;log-file</code>=<i>FILE</i></dt>
<dd>Write log to the specified <i>FILE</i> instead of the other methods.</dd>
<dt><code>-o, &#8211;diode-off</code></dt>
<dd>Turn off the diode (diode is turned on by default).</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd>Switch off logging.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Print the program version number.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Increase the log level.</dd>
<dt><code>&#8211;ssid</code>=<i>SSID</i></dt>
<dd>Specify service set identifier, or SSID, which is a friendly name that identifies a particular 802.16e wireless network.</dd></dl>
<h2>Exit Status</h2>
<dl>
<dt><code>0</code></dt>
<dd>Success</dd>
<dt><code>1</code></dt>
<dd>Failure (syntax or usage error; hardware error; underlying software error; unexpected error).</dd></dl>
<h2>Bugs</h2>
<p>See the madwimax issue tracker: <a href="lahttp://code.google.com/p/madwimax/issues/listra">lahttp://code.google.com/p/madwimax/issues/listra</a></p>
<h2>Author</h2>
<p>Written by Alexander Gordeev, &lt;mailto:lasaine [at] lvk.cs.msu.su&gt;</p>
<h2>Resources</h2>
<p>Main web site: <a href="lahttp://code.google.com/p/madwimax/ra">lahttp://code.google.com/p/madwimax/ra</a></p>
<h2>Copying</h2>
<p>Copyright (C) 2008-2009 Alexander Gordeev. Free use of this software is granted under the terms of the GNU General Public License (GPL).</p>
