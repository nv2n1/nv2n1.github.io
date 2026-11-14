---
title: "upldif(1)"
name: "upldif"
section: "1"
letter: "u"
url: "/docs/linux/man/1-upldif/"
description: "upldif – Barry Project’s LDIF contact uploader"
---

<h2 class="name">NAME</h2>
<p> <code>upldif</code> &#8211; Barry Project&#8217;s LDIF contact uploader </p>
<h2>SYNOPSIS</h2>
<p> <code>upldif</code> [-p pin][-P password][-u][-h][-v]</p>
<h2>DESCRIPTION</h2>
<p> <code>upldif</code> reads a list of contacts in LDAP LDIF format from stdin, and overwrites the Blackberry&#8217;s Address Book database with those contents.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p pin</code></p>
<dd> Specify the PIN of the device to talk to. Only needed if there are multiple Blackberries plugged into your system at once.</p>
<dt><code>-P password</code></p>
<dd> Simplistic method to specify device password.</p>
<dt><code>-u</code></p>
<dd> Actually do the upload. If not specified, upldif only dumps the parsed LDIF data to stdout for verification. </p>
<p> Note! If this option is specified, all existing contacts on your Blackberry will be deleted and replaced with the LDIF contacts.</p>
<dt><code>-v</code></p>
<dd> Dump verbose protocol data during operation.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options. </p>
</dl>
<h2>RETURN STATUS</h2>
<p> In the event of a fatal error, the message will be written to stderr, with an error code of 1. </p>
<h2>AUTHOR</h2>
<p> <code>upldif</code> is part of the Barry project. This manual page was written by Chris Frey.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a> </p>
<h2>Index</h2>
