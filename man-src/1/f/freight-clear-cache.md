---
title: "freight-clear-cache(1)"
name: "freight-clear-cache"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freight-clear-cache/"
description: "freight-clear-cache – clears existing package repositories"
---

<h2>NAME</h2>
<p> <code>freight-clear-cache</code> &#8211; clears existing package repositories</p>
<h2>SYNOPSIS</h2>
<p> <code>freight clear-cache</code> [<code>-c</code> <i>conf</i>] [<code>-v</code>] [<code>-h</code>] [<i>manager</i>/<i>distro</i>][&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>freight-clear-cache</code> clears the cache generated during <code>freight-cache</code> runs so that it can be regenerated on the next <code>freight-cache</code> invocation.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>conf</i>, <code>&#8211;conf=</code><i>conf</i></p>
<dd> Use an alternate configuration file.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show a help message.</dl>
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
<p> Part of <code><a href="/docs/linux/man/1-freight/">freight</a></code>(1). </p>
<p> <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1) can be used to build the repository again. </p>
<h2>Index</h2>
