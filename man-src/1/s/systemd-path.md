---
title: "systemd-path(1)"
name: "systemd-path"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-path/"
description: "systemd-path – List and query system and user paths"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-path</code> [OPTIONS&#8230;] [NAME&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-path</code></p>
<dd>may be used to query system and user paths. The tool makes many of the paths described in <code><a href="/docs/linux/man/7-file-hierarchy/">file-hierarchy</a></code>(7) available for querying. </dd>
<p> When invoked without arguments, a list of known paths and their current values is shown. When at least one argument is passed, the path with this name is queried and its value shown. The variables whose name begins with &quot;search-&quot; do not refer to individual paths, but instead to a list of colon-separated search paths, in their order of precedence.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;suffix=</code></p>
<dl>
<dt>
</dt><dd> Printed paths are suffixed by the specified string.</dd></dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Print a short help text and exit.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print a short version string and exit.</dd></dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-file-hierarchy/">file-hierarchy</a></code>(7) </p>
