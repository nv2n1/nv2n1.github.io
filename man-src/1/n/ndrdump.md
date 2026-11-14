---
title: "ndrdump(1)"
name: "ndrdump"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndrdump/"
description: "ndrdump – DCE/RPC Packet Parser and Dumper"
---

<h2 class="name">NAME</h2>
<p> ndrdump &#8211; DCE/RPC Packet Parser and Dumper </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndrdump</code> [-c context] {pipe} {function} {in|out} {filename}</p>
<dt> <code>ndrdump</code> [pipe]</p>
<dt> <code>ndrdump</code></dl>
<h2>DESCRIPTION</h2>
<dd>ndrdump tries to parse the specified <i>filename</i> using Samba&#8217;s parser for the specified pipe and function. The third argument should be either <i>in</i> or <i>out</i>, depending on whether the data should be parsed as a request or a reply. </p>
<p> Running ndrdump without arguments will list the pipes for which parsers are available. </p>
<p> Running ndrdump with one argument will list the functions that Samba can parse for the specified pipe. </p>
<p> The primary function of ndrdump is debugging Samba&#8217;s internal DCE/RPC parsing functions. The file being parsed is usually one exported by wiresharks &#8220;Export selected packet bytes&#8221; function. </p>
<p> The context argument can be used to load context data from the request packet when parsing reply packets (such as array lengths).</p>
<h2>VERSION</h2>
<p> This man page is correct for version 4.0 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> wireshark, pidl</p>
<h2>AUTHOR</h2>
<p> This utility is part of the m[blue]<code>Samba</code>m[]<font SIZE="-2">[1]</font> suite, which is developed by the global m[blue]<code>Samba Team</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> ndrdump was written by Andrew Tridgell. </p>
<p> This manpage was written by Jelmer Vernooij.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Samba</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.samba.org/">http://www.samba.org/</a></dl>
<dt> 2.</p>
<dd> Samba Team</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.samba.org/samba/team/">http://www.samba.org/samba/team/</a></dl>
</dl>
<h2>Index</h2>
