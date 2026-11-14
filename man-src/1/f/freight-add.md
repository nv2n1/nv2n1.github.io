---
title: "freight-add(1)"
name: "freight-add"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freight-add/"
description: "freight-add – add a package to Freight"
---

<h2>NAME</h2>
<p> <code>freight-add</code> &#8211; add a package to Freight</p>
<h2>SYNOPSIS</h2>
<p> <code>freight add</code> [<code>-c</code> <i>conf</i>] [<code>-v</code>] [<code>-h</code>] <i>package</i> <i>manager</i>/<i>distro</i>[/<i>component</i>][&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>freight-add</code> registers <i>package</i> with one or more <i>manager</i>/<i>distro</i>[/<i>component</i>] pairs (or triples). Currently, <code>apt</code> is the only supported <i>manager</i> and <i>package</i> must be one of <i>*.deb</i>, <i>*.dsc *.debian.tar.gz *.orig.tar.gz</i>, <i>*.dsc *.diff.gz *.orig.tar.gz</i>, or <i>*.dsc *.tar.gz</i>. <i>distro</i> may be any arbitrary value but is best suited to naming a particular version of the target operating system (for example, &quot;wheezy&quot; or &quot;precise&quot;). <i>component</i> is optional and for <code>apt</code> defaults to <code>main</code>. </p>
<p> The package files are organized in the Freight library so <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1) has an easy time of creating package repositories for each <i>manager</i>/<i>distro</i>[/<i>component</i>] later.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>conf</i>, <code>&#8211;conf=</code><i>conf</i></p>
<dd> Use an alternate configuration file.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode.</p>
<dt><code>-e</code>, <code>&#8211;add-error</code></p>
<dd> Raises an error if the package to add is already registered.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show a help message.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/freight.conf</i>, <i>~/.freight.conf</i>, <i>etc/freight.conf</i>, <i>.freight.conf</i></p>
<dd> The default configuration files. See <code><a href="/docs/linux/man/5-freight/">freight</a></code>(5).</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>FREIGHT_CONF</code></p>
<dd> The pathname of an alternate configuration file. See <code><a href="/docs/linux/man/5-freight/">freight</a></code>(5).</p>
<dt><code>FREIGHT_ADD_ERROR</code></p>
<dd> If not empty acts as &#8211;add-error option.</dl>
<h2>THEME SONG</h2>
<p> The New Pornographers &#8211; &quot;All the Old Showstoppers&quot;</p>
<h2>AUTHOR</h2>
<p> Richard Crowley <i>r@rcrowley.org</i></p>
<h2>SEE ALSO</h2>
<p> Part of <code><a href="/docs/linux/man/1-freight/">freight</a></code>(1). </p>
<p> <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1) builds package repositories from the intermediate &quot;Freight library&quot; managed by <code>freight-add</code>. </p>
<h2>Index</h2>
