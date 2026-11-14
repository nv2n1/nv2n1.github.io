---
title: "rpmdev-newinit(1)"
name: "rpmdev-newinit"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmdev-newinit/"
description: "rpmdev-newinit – manual page for rpmdev-newinit version 1.1"
---

<h2>NAME</h2>
<p> rpmdev-newinit &#8211; manual page for rpmdev-newinit version 1.1</p>
<h2>SYNOPSIS</h2>
<p> <code>rpmdev-newinit</code> [<i>option</i>]&#8230; [<i>appname</i>[<i>.init</i>]]</p>
<h2>DESCRIPTION</h2>
<p> rpmdev-newinit generates new init script from a template</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> FILE</p>
<dd> Output the init script to FILE. &quot;-&quot; means stdout. The default is derived from &lt;appname&gt;, or &quot;newinitscript.init&quot; if appname is not given.</p>
<dt><code>-h</code></p>
<dd> Show this usage message and exit.</p>
<dt><code>-v</code></p>
<dd> Print version information and exit.</dl>
<p> The template used is <i>/etc/rpmdevtools/template.init</i>.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt;, component rpmdevtools, or at &lt;<a rel="nofollow" href="https://fedorahosted.org/rpmdevtools/">https://fedorahosted.org/rpmdevtools/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Ville Skyttä &lt;ville.skytta [at] iki.fi&gt; This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
