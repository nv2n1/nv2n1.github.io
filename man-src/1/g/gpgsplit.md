---
title: "gpgsplit(1)"
name: "gpgsplit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpgsplit/"
description: "gpgsplit – Split an OpenPGP message into packets"
---

<h2 class="name">NAME</h2>
<p> gpgsplit &#8211; Split an OpenPGP message into packets</p>
<h2>SYNOPSIS</h2>
<p> <code>gpgsplit </code> [<i>OPTIONS</i>] [<i>FILES</i>] </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gpgsplit</code> command. </p>
<p> <code>gpgsplit</code> splits an OpenPGP message into packets. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>,<code>&#8211;verbose</code></p>
<dd> Verbose.</p>
<dt><code>-p</code>,<code>&#8211;prefix </code><i>STRING</i></p>
<dd> Prepend filenames with <i>STRING</i>.</p>
<dt><code>&#8211;uncompress</code></p>
<dd> Uncompress a packet.</p>
<dt><code>&#8211;secret-to-public</code></p>
<dd> Convert secret keys to public keys.</p>
<dt><code>&#8211;no-split</code></p>
<dd> Write to stdout and don&#8217;t actually split. </p>
</dl>
<h2>AUTHOR</h2>
<p> Copyright (C) 2002 Free Software Foundation, Inc. Please report bugs to &lt;bug-gnupg [at] gnu.org&gt;. </p>
<p> This manpage was written by Francois Wendling &lt;frwendling [at] free.fr&gt;. </p>
<h2>Index</h2>
