---
title: "gethostip(1)"
name: "gethostip"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gethostip/"
description: "gethostip — convert an IP address into various formats"
---

<h2>NAME</h2>
<p> gethostip &#8212; convert an IP address into various formats</p>
<h2>SYNOPSIS</h2>
<p> <code>gethostip</code> [<code>-dxnf</code>] [<i>HOSTNAME|IP</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gethostip</code> command. </p>
<p> The <code>gethostip</code> utility converts the given hostname or IP address into a variety formats. It is provided by the syslinux package to make it easier to calculate the appropriate names for pxelinux configuration files. These filenames can be the complete hexadecimal representation for a given IP address, or a partial hexadecimal representation to match a range of IP addresses. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-d</code></p>
<dd> Output the IP address in decimal format.</p>
<dt><code>-x</code></p>
<dd> Output the IP address in hexadecimal format.</p>
<dt><code>-n</code></p>
<dd> Output the host&#8217;s canonical name.</p>
<dt><code>-f</code></p>
<dd> Full output. Outputs the IP address in all supported formats. Same as <code>-xdn</code>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-syslinux/">syslinux</a></code>(1) </p>
<p> More details can be found in the pxelinux documentation, which can be found in <code>/usr/share/doc/syslinux/pxelinux.doc.gz</code> on <code>Debian GNU/Linux</code> systems. </p>
<h2>AUTHOR</h2>
<p> This manual page was compiled by dann frazier &lt;dannf [at] debian.org&gt; for the <code>Debian GNU/Linux</code> system (but may be used by others). </p>
<h2>Index</h2>
