---
title: "usbredirserver(1)"
name: "usbredirserver"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usbredirserver/"
description: "usbredirserver – exporting an USB device for use from another (virtual) machine"
---

<h2>NAME</h2>
<p> usbredirserver &#8211; exporting an USB device for use from another (virtual) machine</p>
<h2>SYNOPSIS</h2>
<p> <code>usbredirserver</code> [<i>-p|&#8211;port &lt;port&gt;</i>] [<i>-v|&#8211;verbose &lt;0-5&gt;</i>] <i>&lt;usbbus-usbaddr|vendorid:prodid&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> usbredirserver is a small standalone server for exporting an USB device for use from another (virtual) machine through the usbredir protocol. </p>
<p> You can specify the USB device to export either by USB id in the form of <i>&lt;vendorid&gt;:&lt;prodid&gt;</i>, or by USB bus number and device address in the form of <i>&lt;usbbus&gt;-&lt;usbaddr&gt;</i>. </p>
<p> Notice that an instance of usbredirserver can only be used to export a single USB device. If you want to export multiple devices you can start multiple instances listening on different TCP ports.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> Set the TCP port to listen on to <i>PORT</i></p>
<dt><code>-v</code>, <code>&#8211;verbose</code>=<i>VERBOSE</i></p>
<dd> Set usbredirserver&#8217;s verbosity level to <i>VERBOSE</i>, this mostly affects USB redirection related messages. Valid values are 0-5:<br />
 0:Silent 1:Errors 2:Warnings 3:Info 4:Debug 5:Debug++</dl>
<h2>AUTHOR</h2>
<p> Written by Hans de Goede &lt;hdegoede [at] redhat.com&gt;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the spice-devel mailinglist: <a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/spice-devel">http://lists.freedesktop.org/mailman/listinfo/spice-devel</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2010-2012 Red Hat, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
