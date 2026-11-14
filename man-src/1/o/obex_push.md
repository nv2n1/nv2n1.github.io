---
title: "obex_push(1)"
name: "obex_push"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obex_push/"
description: "obex_push – Push and Receive Files over the Bluetooth OBEX Push Channel"
---

<h2>NAME</h2>
<p> obex_push &#8211; Push and Receive Files over the Bluetooth OBEX Push Channel</p>
<h2>SYNOPSIS</h2>
<p> obex_push <i>[</i><code>&lt;channel&gt;</code><i>] [</i><code>&lt;bdaddr&gt; &lt;filename&gt;</code><i>] </i></p>
<h2>DESCRIPTION</h2>
<p> obex_push can send and receive files over the Bluetooth OBEX Push Channel. </p>
<p> Link your bluetooth device with your computer. </p>
<p> You can see the SDP services with: </p>
<p> $ sdptool browse &lt;bdaddr&gt; </p>
<h2>OPTIONS</h2>
<p> If no options are given, any files sent over bluetooth will be received over channel 10 and stored in /tmp. </p>
<p> If <i>&lt;bdaddr&gt;</i> and <i>&lt;filename&gt;</i> are given, the file will be send to the device specified with <i>&lt;bdaddr&gt;</i>.</p>
<dl>
<dt><i>&lt;channel&gt;</i> &#8211; The bluetooth channel to use. Lookup the OBEX Push channel with sdptool browse &lt;bdaddr&gt;.</p>
<dd>
<dt><i>&lt;bdaddr&gt;</i> &#8211; The bluetooth address &lt;bdaddr&gt; of the device to send to.</p>
<dd>
<dt><i>&lt;filename&gt;</i> &#8211; The file to send.</p>
<dd></dl>
<h2>AUTHOR</h2>
<p> Harald Hoyer <i>&lt;harald [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
