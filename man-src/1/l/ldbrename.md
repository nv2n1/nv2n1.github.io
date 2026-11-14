---
title: "ldbrename(1)"
name: "ldbrename"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldbrename/"
description: "ldbrename – Edit LDB databases using your favorite editor"
---

<h2 class="name">NAME</h2>
<p> ldbrename &#8211; Edit LDB databases using your favorite editor </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ldbrename</code> [-h] [-o options] {olddn} {newdn}</dl>
<h2>DESCRIPTION</h2>
<dd>ldbrename is a utility that allows you to rename trees in an LDB database based by DN. This utility takes two arguments: the original DN name of the top element and the DN to change it to.</p>
<h2>OPTIONS</h2>
<p> -h</p>
<dl>
<dt>
<dd> Show list of available options.</dl>
<p> -H &lt;ldb-url&gt;</p>
<dl>
<dt>
<dd> LDB URL to connect to. See <a href="/docs/linux/man/3-ldb/">ldb</a>(3) for details.</dl>
<p> -o options</p>
<dl>
<dt>
<dd> Extra ldb options, such as modules.</dl>
<h2>ENVIRONMENT</h2>
<p> LDB_URL</p>
<dl>
<dt>
<dd> LDB URL to connect to (can be overrided by using the -H command-line option.)</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 1.1 of LDB.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-ldb/">ldb</a>(3), ldbmodify, ldbdel, <a href="/docs/linux/man/5-ldif/">ldif</a>(5)</p>
<h2>AUTHOR</h2>
<p> ldb was written by m[blue]<code>Andrew Tridgell</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> If you wish to report a problem or make a suggestion then please see the m[blue]<code><a rel="nofollow" href="http://ldb.samba.org/">http://ldb.samba.org/</a></code>m[] web site for current contact and maintainer information. </p>
<p> This manpage was written by Jelmer Vernooij.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Andrew Tridgell</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://samba.org/~tridge/">http://samba.org/~tridge/</a></dl>
</dl>
<h2>Index</h2>
