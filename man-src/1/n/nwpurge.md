---
title: "nwpurge(1)"
name: "nwpurge"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwpurge/"
description: "nwpurge – Permanently delete previously erased files"
---

<h2>NAME</h2>
<p> nwpurge &#8211; Permanently delete previously erased files</p>
<h2>SYNOPSIS</h2>
<p> <code>nwpurge</code> [ <code>-h</code> ] [ <code>-a</code> ] [ <code>-l</code> ] [ <code>-s</code> ] [ <code>directory</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwpurge</code> purges files from specified NetWare directory. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> <code>-h</code> is used to print out a short help text.</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> <code>-a</code> is used to specify that not only specified directory, but also its subdirectories have to be purged.</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> <code>-l</code> is used to disable purge. Files are only printed out.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> <code>-s</code> specifies silent mode (no print output, only total is printed).</dl>
<p> <code>directory</code></p>
<dl>
<dt>
<dd> You can specify the directory in which you want to purge files. Current working directory is used by default. You have to specify path in Linux format, not in NetWare format. </p>
</dl>
<h2>EXAMPLES</h2>
<p> nwpurge -a /NetWare/server/sys </p>
<p> With this example, all files from directory /NetWare/server/sys and from all its subdirectories are purged. </p>
<h2>AUTHORS</h2>
<p> nwpurge was written by Petr Vandrovec with the corresponding NetWare utility in mind. See the Changes file of ncpfs for other contributors. </p>
<h2>Index</h2>
