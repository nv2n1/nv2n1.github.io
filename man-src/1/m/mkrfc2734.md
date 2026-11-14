---
title: "mkrfc2734(1)"
name: "mkrfc2734"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkrfc2734/"
description: "mkrfc2734 – Make Linux 2.4 IP over IEEE 1394 capable."
---

<h2>NAME</h2>
<p> mkrfc2734 &#8211; Make Linux 2.4 IP over IEEE 1394 capable.</p>
<h2>SYNOPSIS</h2>
<p> <code>mkrfc2734</code></p>
<h2>DESCRIPTION</h2>
<p> <code>mkrfc2734</code> adds entries to the Linux IEEE 1394 Configuration ROM to describe itself to other nodes on the bus as being capable of performing IP over IEEE 1394 (RFC 2734) duties. This utility is not necessary for Linux 2.6 as there is a kernel configuration option to enable this. This command takes no arguments and requires raw1394 kernel module, libraw1394 library, and /dev/raw1394 device file. Also, it makes absolutely no sense to run this unless you have also loaded the eth1394 kernel module&#8211;the bits that do the real work! </p>
<h2>AUTHORS</h2>
<p> <code>mkrfc2734</code> and this man page was written by Dan Dennedy &lt;dan [at] dennedy.org&gt;. </p>
<h2>Index</h2>
