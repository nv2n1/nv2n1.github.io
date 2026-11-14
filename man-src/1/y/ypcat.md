---
title: "ypcat(1)"
name: "ypcat"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ypcat/"
description: "ypcat – print values of all keys in a NIS database"
---

<h2>NAME</h2>
<p> ypcat &#8211; print values of all keys in a NIS database</p>
<h2>SYNOPSIS</h2>
<p> <code>ypcat</code> [ <code>-kt</code> ] [ <code>-d</code><i> domain</i> ] [ <code>-h</code><i> hostname</i> ] <i>mapname</i><br />
 <code>ypcat</code> <code>-x</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ypcat</code> prints the values of all keys from the NIS database specified by <i>mapname,</i> which may be a map name or a map nickname.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> domain</i></p>
<dd> Specify a domain other than the default domain as returned by <code><a href="/docs/linux/man/8-domainname/">domainname</a></code>(8).</p>
<dt><code>-h</code><i> hostname</i></p>
<dd> Specify a hostname other than the default one as found by <code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8).</p>
<dt><code>-k</code></p>
<dd> Display map keys. This option is useful with maps in which the values are null or the key is not part of the value.</p>
<dt><code>-t</code></p>
<dd> This option inhibits map nickname translation.</p>
<dt><code>-x</code></p>
<dd> Display the map nickname translation table.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/var/yp/nicknames</code></p>
<dd> map nickname translation table.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-domainname/">domainname</a></code>(8), <code><a href="/docs/linux/man/5-nicknames/">nicknames</a></code>(5), <code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8), <code><a href="/docs/linux/man/1-ypmatch/">ypmatch</a></code>(1), <code><a href="/docs/linux/man/8-yppoll/">yppoll</a></code>(8), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-ypset/">ypset</a></code>(8), <code><a href="/docs/linux/man/1-ypwhich/">ypwhich</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> <code>ypcat</code> is part of the <code>yp-tools</code> package, which was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;. </p>
<h2>Index</h2>
