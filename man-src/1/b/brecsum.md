---
title: "brecsum(1)"
name: "brecsum"
section: "1"
letter: "b"
url: "/docs/linux/man/1-brecsum/"
description: "brecsum – Generate SHA1 sums of raw Blackberry database records."
---

<h2 class="name">NAME</h2>
<p> <code>brecsum</code> &#8211; Generate SHA1 sums of raw Blackberry database records. </p>
<h2>SYNOPSIS</h2>
<p> <code>brecsum</code> [-d db][-h][-p pin][-P pass][-v]</p>
<h2>DESCRIPTION</h2>
<p> <code>brecsum</code> downloads the specified database(s) and computes a SHA1 checksum on each raw record it finds. The SHA1 sums are written to stdout. </p>
<p> This is mainly useful for verifying the integrity of restored data during testing.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d db</code></p>
<dd> Specify the database to download and sum. This option may be given multiple times to fetch more than one database. See btool&#8217;s -t option to retrieve a list of databases on your device.</p>
<dt><code>-p pin</code></p>
<dd> Specify the PIN of the device to talk to. Only needed if there are multiple Blackberries plugged into your system at once.</p>
<dt><code>-P pass</code></p>
<dd> Simplistic method to specify device password. In a real application, this would be done using a more secure prompt.</p>
<dt><code>-v</code></p>
<dd> Dump verbose protocol data during operation.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options. </p>
</dl>
<h2>RETURN STATUS</h2>
<p> In the event of a fatal error, the message will be written to stderr, with an error code of 1. </p>
<h2>AUTHOR</h2>
<p> <code>brecsum</code> is part of the Barry project. This manual page was written by Chris Frey.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a> </p>
<h2>Index</h2>
