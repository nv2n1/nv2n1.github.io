---
title: "rpmdev-newspec(1)"
name: "rpmdev-newspec"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmdev-newspec/"
description: "rpmdev-newspec – manual page for rpmdev-newspec version 2.2"
---

<h2>NAME</h2>
<p> rpmdev-newspec &#8211; manual page for rpmdev-newspec version 2.2</p>
<h2>SYNOPSIS</h2>
<p> <code>rpmdev-newspec</code> [<i>option</i>]&#8230; [<i>appname</i>[<i>.spec</i>]]</p>
<h2>DESCRIPTION</h2>
<p> rpmdev-newspec generates new rpm .spec files from templates.</p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>-o</code> FILE, <code>&#8211;output</code> FILE</p>
<dt>
<dd>
<dd>Output the specfile to FILE. &quot;-&quot; means stdout. The default is derived from &lt;appname&gt;, or &quot;newpackage.spec&quot; if &lt;appname&gt; is not given.</p>
<dt> <code>-t</code> TYPE, <code>&#8211;type</code> TYPE</p>
<dt>
<dd>
<dd>Force use of the TYPE spec template. The default is guessed from &lt;appname&gt;, falling back to &quot;minimal&quot; if the guesswork does not result in a more specific one or if &lt;appname&gt; is not given.</p>
<dt><code>-m</code>, <code>&#8211;macros</code></p>
<dd> Emit templates using macros instead of shell style variables. Configuration variable: NEWSPEC_PREFER_MACROS, default is off.</p>
<dt> <code>-r</code> VERSION, <code>&#8211;rpm-version</code> VERSION</p>
<dt>
<dd>
<dd>Filter out some spec file constructs not needed by the specified rpm(build) version and newer ones. Configuration variable: NEWSPEC_MIN_RPMVER, default is system rpm version.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show this usage message and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>FILES</h2>
<p> <i>/etc/rpmdevtools</i></p>
<dl>
<dt>
<dd> Directory for specfile templates.</dl>
<p> <i>/etc/rpmdevtools/newspec.conf</i></p>
<dl>
<dt>
<dd> System wide configuration.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt;, component rpmdevtools, or at &lt;<a rel="nofollow" href="https://fedorahosted.org/rpmdevtools/">https://fedorahosted.org/rpmdevtools/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; Warren Togami &lt;warren [at] togami.com&gt;, Ville Skyttä &lt;ville.skytta [at] iki.fi&gt; This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
