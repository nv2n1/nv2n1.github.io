---
title: "plmpower(8)"
name: "plmpower"
section: "8"
letter: "p"
url: "/docs/linux/man/8-plmpower/"
description: "plmpower – control Insteon/X10 devices via SmartLabs PLM 2412S"
---

<p>plmpower &#8211; control Insteon/X10 devices via SmartLabs PLM 2412S</p>
<h2>Synopsis</h2>
<p><code>plmpower</code> <i>&#8211;device serial-port</i> </p>
<h2>Description</h2>
<p><code>plmpower</code> is a helper program for <code>powerman</code> which enables communication with Insteon/X10 devices via SmartLabs Power Line Modem, model 2412S. It is run interactively by the powerman daemon. It can also be useful as a standalone tool for debugging X10/Insteon networks based on the above device.</p>
<h2>Network Setup</h2>
<p>Note the addresses of your Insteon/X10 devices. Plug the PLM into an AC outlet, preferably on the same electrical phase as the devices under control. Devices are available to bridge phases if this is not possible. </p>
<p> Attach the PLM&#8217;s serial port to your computer, and ensure that nothing else is using the serial port such as the system console or <a href="/docs/linux/man/8-getty/">getty</a>(8). Run <code>plmpower</code> and try the interactive commands below to see if the devices respond reliably. </p>
<p> Once everything is working, configure <code>powermand</code> to run <code>plmpower</code> as a coprocess as described in <a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a>(5).</p>
<h2>Options</h2>
<dl>
<dt><i>-d, &#8211;device serial-port</i></p>
<dd>Specify the path to the special file connected to the PLM&#8217;s serial port.</p>
<dt><i>-t, &#8211;timeout msec</i></p>
<dd>Set the Insteon timeout to the specified number of milliseconds (default 1000).</p>
<dt><i>-x, &#8211;x10-attempts number</i></p>
<dd>Set the number of times to run every X10 command (default 3). X10 does not provide an ACK/NAK mechanism like Insteon so we cannot be certain that any particular X10 command completed, therefore X10 commands are issued multiple times to increase confidence.</dl>
<h2>Interactive Commands</h2>
<p>The following commands are accepted at the plmpower&gt; prompt. Address arguments may be Insteon (e.g. 1A.2B.3C) or X10 (e.g. G12).</p>
<dl>
<dt><i>help</i></p>
<dd>Display help on the available commands.</p>
<dt><i>info</i></p>
<dd>Get info about the PLM.</p>
<dt><i>reset</i></p>
<dd>Reset the PLM (clears the all-link db).</p>
<dt><i>on addr</i></p>
<dd>Turn on device.</p>
<dt><i>off addr</i></p>
<dd>Turn off device.</p>
<dt><i>status addr</i></p>
<dd>Query status of device (Insteon only).</p>
<dt><i>ping addr</i></p>
<dd>Time round trip request/response to device (Insteon only). </p>
</dl>
<h2>Files</h2>
<p>/usr/sbin/plmpower<br />
 /etc/powerman/powerman.conf</p>
<h2>Origin</h2>
<p>PowerMan was originally developed by Andrew Uselton on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the GNU GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-powerman/">powerman</a></code>(1), <code><a href="/docs/linux/man/8-powermand/">powermand</a></code>(8), <code><a href="/docs/linux/man/8-httppower/">httppower</a></code>(8), <code><a href="/docs/linux/man/8-plmpower/">plmpower</a></code>(8), <code><a href="/docs/linux/man/8-vpcd/">vpcd</a></code>(8), <code><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a></code>(5), <code><a href="/docs/linux/man/5-powerman-dev/">powerman.dev</a></code>(5). <code><a rel="nofollow" href="http://code.google.com/p/powerman">http://code.google.com/p/powerman</a></code> </p>
