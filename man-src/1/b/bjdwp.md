---
title: "bjdwp(1)"
name: "bjdwp"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bjdwp/"
description: "bjdwp – Command line USB Blackberry Java Debug Wire Protocol"
---

<h2 class="name">NAME</h2>
<p> <code>bjdwp</code> &#8211; Command line USB Blackberry Java Debug Wire Protocol </p>
<h2>SYNOPSIS</h2>
<p> <code>bjdwp</code> [-h][-p pin][-P password][-v] address port </p>
<h2>DESCRIPTION</h2>
<p> <code>bjdwp</code> is a program that supports the Java Debug Wire Protocol over USB, which enables debugging of Java programs directly on your Blackberry. </p>
<p> Support is experimental, and development is focused primarily on the BlackBerry Storm. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p pin</code></p>
<dd> PIN of device to talk with. Only needed if you have more than one Blackberry connected at once.</p>
<dt><code>-P password</code></p>
<dd> Simplistic method to specify device password. In a real application, this would be done using a more secure prompt.</p>
<dt><code>-v</code></p>
<dd> Dump verbose protocol data during operation.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options. </p>
</dl>
<h2>ARGUMENTS</h2>
<p> The following arguments are required, in order to provide a socket where the JDWP server will listen for connections from the debugger.</p>
<dl>
<dt><code>address</code></p>
<dd> Most often &#8216;localhost&#8217; but can be any IP or hostname on the machine running bjdwp.</p>
<dt><code>port</code></p>
<dd> Port to listen on. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Start the server and the USB connection to the device: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bjdwp localhost 8000</p>
<p> Then start your java debugger: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>jdb -connect com.sun.jdi.SocketAttach:hostname=localhost,port=8000</p>
<h2>AUTHOR</h2>
<p> <code>bjdwp</code> was initially written for the Barry project by Nicolas VIVIEN. This manual page was written by Chris Frey.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a> </p>
<h2>Index</h2>
