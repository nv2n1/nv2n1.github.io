---
title: "freight-init(1)"
name: "freight-init"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freight-init/"
description: "freight-init – initialize a Freight directory"
---

<h2>NAME</h2>
<p> <code>freight-init</code> &#8211; initialize a Freight directory</p>
<h2>SYNOPSIS</h2>
<p> <code>freight init</code> [<code>&#8211;libdir</code> <i>varlib</i>] [<code>&#8211;cachedir</code> <i>varcache</i>] [<code>&#8211;archs</code> <i>archs</i>] [<code>&#8211;origin</code> <i>origin</i>] [<code>&#8211;label</code> <i>label</i>] [<code>-v</code>] [<code>-h</code>] <code>-g</code> <i>gpg</i> <i>dirname</i></p>
<h2>DESCRIPTION</h2>
<p> <code>freight-init</code> will setup a directory to be used by Freight. It will generate small wrappers around the original Freight commands. Use <code><a href="/docs/linux/man/1-freight-add/">freight-add</a></code>(1) and <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1) to work against the <code>VARLIB</code> and <code>VARCACHE</code> given to <code>freight init</code>. </p>
<p> The benefit of using <code>freight-init</code> is to automate the setup of Freight and to configure all data to be stored in one directory. </p>
<p> Configuration is stored in <i>dirname</i><code>/etc/freight.conf</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g</code> <i>gpg</i>, <code>&#8211;gpg=</code><i>gpg</i></p>
<dd> GPG key. May be given multiple times.</p>
<dt><code>&#8211;libdir=</code><i>varlib</i></p>
<dd> VARLIB directory to use. Defaults to <i>dirname</i><code>/var/lib</code></p>
<dt><code>&#8211;cachedir=</code><i>varcache</i></p>
<dd> VARCACHE directory to use. Defaults to <i>dirname</i><code>/var/cache</code></p>
<dt><code>&#8211;archs=</code><i>archs</i></p>
<dd> Architectures to generate archives for. Defaults to <code>i386 amd64</code></p>
<dt><code>&#8211;origin=</code><i>origin</i></p>
<dd> Debian archive Origin field value. Defaults to <code>Freight</code></p>
<dt><code>&#8211;label=</code><i>label</i></p>
<dd> Debian archive Label field value. Defaults to <code>Freight</code></p>
<dt><code>&#8211;suite=</code><i>suite</i></p>
<dd> Debian archive Suite field value.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show a help message.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/freight.conf</i>, <i>~/.freight.conf</i>, <i>etc/freight.conf</i>, <i>.freight.conf</i></p>
<dd> The default configuration files. See <code><a href="/docs/linux/man/5-freight/">freight</a></code>(5).</dl>
<h2>THEME SONG</h2>
<p> The New Pornographers &#8211; &quot;All the Old Showstoppers&quot;</p>
<h2>AUTHOR</h2>
<p> Jens Braeuer <i>braeuer.jens [at] googlemail.com</i></p>
<h2>SEE ALSO</h2>
<p> Part of <code><a href="/docs/linux/man/1-freight/">freight</a></code>(1). </p>
<h2>Index</h2>
