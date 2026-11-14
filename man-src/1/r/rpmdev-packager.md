---
title: "rpmdev-packager(1)"
name: "rpmdev-packager"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmdev-packager/"
description: "rpmdev-packager – manual page for rpmdev-packager version 1.1"
---

<h2>NAME</h2>
<p> rpmdev-packager &#8211; manual page for rpmdev-packager version 1.1</p>
<h2>SYNOPSIS</h2>
<p> <code>rpmdev-packager</code> [<i>option</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> rpmdev-packager guesses rpm packager info from various sources:</p>
<dl>
<dt>$RPM_PACKAGER</p>
<dd> from environment (full name + email address)</p>
<dt>%packager</p>
<dd> from rpm configuration (full name + email address)</p>
<dt><i>/etc/passwd</i></p>
<dd> gecos (full name)</p>
<dt>certificates</p>
<dd> ~/.fedora.cert (email address)</p>
<dt>$MAILTO</p>
<dd> from environment (email address)</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help message and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt;, component rpmdevtools, or at &lt;<a rel="nofollow" href="https://fedorahosted.org/rpmdevtools/">https://fedorahosted.org/rpmdevtools/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Ville Skyttä &lt;ville.skytta [at] iki.fi&gt; This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
