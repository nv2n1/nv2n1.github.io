---
title: "cups-config(1)"
name: "cups-config"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cups-config/"
description: "cups-config – get cups api, compiler, directory, and link information."
---

<h2>NAME</h2>
<p> cups-config &#8211; get cups api, compiler, directory, and link information.</p>
<h2>SYNOPSIS</h2>
<p> <code>cups-config</code> &#8211;api-version<br />
 <code>cups-config</code> &#8211;build<br />
 <code>cups-config</code> &#8211;cflags<br />
 <code>cups-config</code> &#8211;datadir<br />
 <code>cups-config</code> &#8211;help<br />
 <code>cups-config</code> &#8211;ldflags<br />
 <code>cups-config</code> [ <i>&#8211;image</i> ] [ <i>&#8211;static</i> ] &#8211;libs<br />
 <code>cups-config</code> &#8211;serverbin<br />
 <code>cups-config</code> &#8211;serverroot<br />
 <code>cups-config</code> &#8211;version </p>
<h2>DESCRIPTION</h2>
<p> <code>cups-config</code> is the CUPS program configuration utility. It should be used by application developers to determine the necessary command-line options for the compiler and linker, as well as determining installation directories for filters, configuration files, and drivers.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;api-version</p>
<dd>
 Displays the current API version (major.minor).</p>
<dt>&#8211;build</p>
<dd>
 Displays a system-specific build number.</p>
<dt>&#8211;cflags</p>
<dd>
 Displays the necessary compiler options.</p>
<dt>&#8211;datadir</p>
<dd>
 Displays the default CUPS data directory.</p>
<dt>&#8211;help</p>
<dd>
 Displays the program usage message.</p>
<dt>&#8211;image</p>
<dd>
 When used with <i>&#8211;libs</i>, adds the CUPS imaging library to the list of displayed libraries.</p>
<dt>&#8211;ldflags</p>
<dd>
 Displays the necessary linker options.</p>
<dt>&#8211;libs</p>
<dd>
 Displays the necessary librarys to link to.</p>
<dt>&#8211;serverbin</p>
<dd>
 Displays the default CUPS binary directory, where filters and backends are stored.</p>
<dt>&#8211;serverroot</p>
<dd>
 Displays the default CUPS configuration file directory.</p>
<dt>&#8211;static</p>
<dd>
 When used with <i>&#8211;libs</i>, shows the static libraries instead of the default (shared) libraries.</p>
<dt>&#8211;version</p>
<dd>
 Displays the full version number of the CUPS installation (major.minor.patch).</dl>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2013 by Apple Inc. </p>
<h2>Index</h2>
