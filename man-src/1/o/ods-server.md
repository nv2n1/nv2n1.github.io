---
title: "ods-server(1)"
name: "ods-server"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ods-server/"
description: "ods-server – minimal OBEX server based on obex-data-server"
---

<h2 class="name">NAME</h2>
<p> ods-server &#8211; minimal OBEX server based on obex-data-server </p>
<h2>SYNOPSIS</h2>
<p> <code>ods-server</code> [<i>options</i>] <i>profile path</i></p>
<h2>DESCRIPTION</h2>
<p> ods-server provides a minimal OBEX server based on obex-data-server for receiving files over bluetooth. <i>profile</i> selects the UUID-128 profile ID to use, currently <i>opp</i> and <i>ftp</i> can be used as aliases for object push and obex ftp respectively. <i>path</i> is the target directory for received files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-l</code> ADDRESS, <code>&#8211;local</code>=<i>ADDRESS</i></p>
<dd> ADDRESS of Bluetooth adapter to listen on. Default is 00:00:00:00:00:00</p>
<dt><code>-p</code>, <code>&#8211;pairing</code></p>
<dd> Require remote devices to be paired before allowing them to connect. Disabled by default</p>
<dt><code>-r</code>, <code>&#8211;readonly</code></p>
<dd> Disallow any write operations. Allowed by default</p>
<dt><code>-t</code>, <code>&#8211;thumbnails</code></p>
<dd> Require remote device to send thumbnails when using Imaging (BIP) server</p>
<dt><code>-a</code>, <code>&#8211;ask-to-accept</code></p>
<dd> Prompt user to accept or reject every file. By default all files are accepted</dl>
<h2>AUTHOR</h2>
<p> <code>ods-server</code> was written by Tadas Dailyda &lt;tadas [at] dailyda.com&gt; and is shipped as ods-server-test.py in the obex-data-server distribution </p>
<p> This manual page was written by Filippo Giunchedi &lt;filippo [at] debian.org&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
