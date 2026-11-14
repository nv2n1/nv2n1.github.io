---
title: "freight(1)"
name: "freight"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freight/"
description: "freight – a modern take on the Debian archive"
---

<h2>NAME</h2>
<p> <code>freight</code> &#8211; a modern take on the Debian archive</p>
<h2>SYNOPSIS</h2>
<p> <code>freight</code> <i>command</i> [<i>&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>freight</code> programs create the files needed to serve a Debian archive. The actual serving is done via your favorite HTTP server.</p>
<dl>
<dt><code><a href="/docs/linux/man/1-freight-add/">freight-add</a></code>(1)</p>
<dd> Add a package to Freight.</p>
<dt><code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1)</p>
<dd> (Re)builds package repositories.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/freight.conf</i>, <i>~/.freight.conf</i>, <i>etc/freight.conf</i>, <i>.freight.conf</i></p>
<dd> The default configuration files. See <code><a href="/docs/linux/man/5-freight/">freight</a></code>(5).</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>FREIGHT_CONF</code></p>
<dd> The pathname of an alternate configuration file. See <code><a href="/docs/linux/man/5-freight/">freight</a></code>(5).</dl>
<h2>THEME SONG</h2>
<p> The New Pornographers &#8211; &quot;All the Old Showstoppers&quot;</p>
<h2>AUTHOR</h2>
<p> Richard Crowley <i>r@rcrowley.org</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-reprepro/">reprepro</a></code>(1) manages Debian archives, too, if Freight isn&#8217;t your thing. </p>
<h2>Index</h2>
