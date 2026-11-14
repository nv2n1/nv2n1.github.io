---
title: "qmi-network(1)"
name: "qmi-network"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qmi-network/"
description: "qmi-network – Simple network management of QMI devices"
---

<h2>NAME</h2>
<p> qmi-network &#8211; Simple network management of QMI devices</p>
<h2>SYNOPSIS</h2>
<p> <code>qmi-network</code> [<i>,OPTIONS/</i>] [<i>,DEVICE/</i>] [<i>,COMMAND/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Simple network management of QMI devices</p>
<h3>Commands:</h3>
<dl>
<dt>start</p>
<dd> Start network connection</p>
<dt>stop</p>
<dd> Stop network connection</p>
<dt>status</p>
<dd> Query network connection status</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;profile</code>=<i>,[PATH]/</i></p>
<dd> Use the profile in the specified path</p>
<dt><code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;version</code></p>
<dd> Show version</dl>
<p> Notes:</p>
<dl>
<dt>
<dd> 1) [DEVICE] is given as the full path to the cdc-wdm character device, e.g.:</p>
<dt>
<dd> <i>,/dev/cdc-wdm0/</i></p>
<dt>
<dd> 2) The qmi-network script requires a profile to work. Unless explicitly specified with `&#8211;profile&#8217;, the file is assumed to be available in the following path:</p>
<dt>
<dd> <i>,/etc/qmi-network.conf/</i></p>
<dt>
<dd> 3) The APN to use should be configured in the profile, in the following way (e.g. assuming APN is called &#8216;internet&#8217;):</p>
<dt>
<dd> APN=internet</p>
<dt>
<dd> 4) Optional APN user/password strings may be given in the following way:</p>
<dt>
<dd> APN_USER=user APN_PASS=password</p>
<dt>
<dd> 5) If you want to instruct the qmi-network script to use the qmi-proxy setup, you can do so by configuring the following line in the profile:</p>
<dt>
<dd> PROXY=yes</p>
<dt>
<dd> 6) Once the qmi-network script reports a successful connection you still need to run a DHCP client on the associated WWAN network interface.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (2013-2015) Aleksander Morgado License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl-2.0.html">http://gnu.org/licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>qmi-network</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>qmi-network</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info qmi-network</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
