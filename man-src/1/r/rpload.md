---
title: "rpload(1)"
name: "rpload"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpload/"
description: "rpload – alpine remote data utility"
---

<h2>NAME</h2>
<p> rpload &#8211; alpine remote data utility</p>
<h2>SYNTAX</h2>
<p> <code>rpload</code> [ -f ] [ -s trimSize ] -t Type -l Local_file -r Remote_folder</p>
<h2>DESCRIPTION</h2>
<p> Rpload may be used to convert local Alpine configuration files or address books into remote configurations or address books. It is intended to be used by system administrators. Regular users should normally use the facilities provided within Alpine. </p>
<p> Local_file will usually be a user&#8217;s alpine configuration file, and Remote_folder is the IMAP folder which will be used (with the help of Alpine&#8217;s <code>-p</code>, <code>-P</code>, and <code>-x</code> commands or PINECONF, PINERC, and PINERCEX environment variables) as the user&#8217;s remote configuration folder. A copy of Local_file will be placed in the folder with the correct header lines to satisfy Alpine.</p>
<dl>
<dt><code>-f</code></p>
<dd> Force the load even if the remote folder is in the wrong format. This will <code>delete</code> the contents of the folder so use it carefully.</p>
<dt><code>-s</code>&nbsp;<wbr><code>trimSize</code></p>
<dd> If the number of messages in the remote folder is more than one plus trimsize (one is for the header message), then messages 2, 3, and so on will be deleted until there are only one plus trimsize messages left. If this option is not set no trimming will be done.</p>
<dt><code>-t</code>&nbsp;<wbr><code>Type</code></p>
<dd> The possible Types are <code>pinerc</code>, <code>abook</code>, and <code>sig</code>. (Sig is mostly obsolete. Literal signatures contained within the remote pinerc should be used instead.)</p>
<dt><code>-l</code>&nbsp;<wbr><code>Local_file</code></p>
<dd> The file on this system that is to be copied.</p>
<dt><code>-r</code>&nbsp;<wbr><code>Remote_folder</code></p>
<dd> A remote folder name to be copied to. See the Alpine documentation for the syntax of a remote folder name. One example is<br />
 {my.imap.server}remote_pinerc.</dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is zero if all goes well, -1 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rpdump/">Rpdump</a>(1). </p>
<p> Copyright 1989-2007 by the University of Washington. </p>
<p> $Date: 2005/01/14 20:40:14 $ </p>
<h2>Index</h2>
