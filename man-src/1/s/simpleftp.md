---
title: "simpleftp(1)"
name: "simpleftp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-simpleftp/"
description: "simpleftp – Rudimentary FTP client"
---

<h2 class="name">NAME</h2>
<p> simpleftp &#8211; Rudimentary FTP client </p>
<h2>SYNOPSIS</h2>
<p> <code>simpleftp</code> <i>url</i> [&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>simpleftp</code> is a Perl script that provides basic support for fetching files with <font SIZE="-1">FTP</font> in a batch oriented fashion. It takes one or more <font SIZE="-1">FTP</font> URLs on the command line. The file(s) will be retrieved from the remote server and placed in the current directory with the same basename as on the remote; e.g., &lt;<a href="ftp://ftp.isc.org/pub/usenet/CONFIG/active.gz">ftp://ftp.isc.org/pub/usenet/CONFIG/active.gz</a>&gt; is stored as <i>active.gz</i> in the current directory. </p>
<p> The script properly understands usernames, passwords and ports specified as follows: </p>
<pre>
    <a href="ftp://user:password@host:port/path/file">ftp://user:password@host:port/path/file</a>
</pre>
<h2>BUGS</h2>
<p> <code>simpleftp</code> is an extremely poor substitute for more complete programs like the freely available <code>wget</code> or <code>ncftp</code> utilities. It was written only to provide elementary support in <font SIZE="-1">INN</font> for non-interactive fetching of the files in &lt;<a href="ftp://ftp.isc.org/pub/pgpcontrol/">ftp://ftp.isc.org/pub/pgpcontrol/</a>&gt; or &lt;<a href="ftp://ftp.isc.org/pub/usenet/CONFIG/">ftp://ftp.isc.org/pub/usenet/CONFIG/</a>&gt; without requiring administrators to install yet another package. Its shortcomings as a general purpose program are too numerous to mention, but one that stands out is that downloaded files by <code>simpleftp</code> override existing files with the same name in the local directory.</p>
<h2>HISTORY</h2>
<p> Tossed off by David C Lawrence &lt;tale [at] isc.org&gt; for InterNetNews. Rewritten to use <tt>&quot;Net::FTP&quot;</tt> by Julien Elie. </p>
<p> <tt>$Id:</tt> simple<a href="ftp://ftp.pod">ftp.pod</a> 8357 2009-02-27 17:56:00Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-actsync/">actsync</a></i>(8). </p>
<h2>Index</h2>
