---
title: "ypwhich(1)"
name: "ypwhich"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ypwhich/"
description: "ypwhich – return name of NIS server or map master"
---

<h2>NAME</h2>
<p> ypwhich &#8211; return name of NIS server or map master</p>
<h2>SYNOPSIS</h2>
<p> <code>ypwhich</code> [ <code>-d</code><i> domain</i> ] [ <code>-V</code>n ] [ <i>hostname</i> ]<br />
 <code>ypwhich</code> [ <code>-d</code><i> domain</i> ] [ <code>-t</code> ] <code>-m</code> [ <i>mname</i> ]<br />
 <code>ypwhich</code> <code>-x</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ypwhich</code> returns the name of the NIS server that supplies the NIS services to a NIS client, or which is the master for a map. If invoked without arguments, it gives the NIS server for the local machine. If <i>hostname</i> is specified, that machine is queried to find out which NIS master it is using.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> domain</i></p>
<dd> Specify a domain other than the default domain.</p>
<dt><code>-t</code></p>
<dd> This option inhibits map nickname translation.</p>
<dt><code>-m</code><i> mname</i></p>
<dd> Find the master NIS server for a map. No <i>hostname</i> can be specified with the <code>-m</code> option. <i>mname</i> can be a mapname or nickname for a map. If <i>mname</i> is omitted, <code>ypwhich</code> will produce a list of available maps.</p>
<dt><code>-x</code></p>
<dd> Display the map nickname translation table.</p>
<dt><code>-Vn</code></p>
<dd> Version of <code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8), V2 is default. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/var/yp/nicknames</code></p>
<dd> map nickname translation table.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-domainname/">domainname</a></code>(8), <code><a href="/docs/linux/man/5-nicknames/">nicknames</a></code>(5), <code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8), <code><a href="/docs/linux/man/1-ypcat/">ypcat</a></code>(1), <code><a href="/docs/linux/man/1-ypmatch/">ypmatch</a></code>(1), <code><a href="/docs/linux/man/8-yppoll/">yppoll</a></code>(8), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-ypset/">ypset</a></code>(8) </p>
<h2>AUTHOR</h2>
<p> <code>ypwhich</code> is part of the <code>yp-tools</code> package, which was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;. </p>
<h2>Index</h2>
