---
title: "rpdump(1)"
name: "rpdump"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpdump/"
description: "rpdump – alpine remote data utility"
---

<h2>NAME</h2>
<p> rpdump &#8211; alpine remote data utility</p>
<h2>SYNTAX</h2>
<p> <code>rpdump</code> [ -f ] -l Local_file -r Remote_folder</p>
<h2>DESCRIPTION</h2>
<p> Rpdump may be used to copy the actual data from remote Alpine configuration files or address books into a local file. It is intended to be used by system administrators. Regular users should normally use the facilities provided within Alpine. </p>
<p> Local_file will normally be a local temporary file. Remote_folder is the IMAP folder being used as a remote Alpine configuration (with the help of Alpine&#8217;s -P, -p, and -x commands or PINECONF, PINERC, and PINERCEX environment variables) or remote Alpine address book folder. A copy of the data from Remote_folder will be copied to Local_file.</p>
<dl>
<dt><code>-f</code></p>
<dd> Force the dump even if the remote folder is in an unrecognized format.</p>
<dt><code>-l</code>&nbsp;<wbr><code>Local_file</code></p>
<dd> The file on this system that is to be copied to.</p>
<dt><code>-r</code>&nbsp;<wbr><code>Remote_folder</code></p>
<dd> A remote folder name to be copied from. See the Alpine documentation for the syntax of a remote folder name. One example is<br />
 {my.imap.server}remote_pinerc.</dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is zero if all goes well, -1 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rpload/">Rpload</a>(1). </p>
<p> Copyright 1989-2007 by the University of Washington. </p>
<p> $Date: 2005/01/14 20:40:14 $ </p>
<h2>Index</h2>
