---
title: "osinfo-db-path(1)"
name: "osinfo-db-path"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osinfo-db-path/"
description: "osinfo-db-path – Report database locations"
---

<h2 class="name">NAME</h2>
<p> osinfo-db-path &#8211; Report database locations </p>
<h2>SYNOPSIS</h2>
<p> osinfo-db-path [<font SIZE="-1">OPTIONS&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>osinfo-db-path</code> tool will report the paths associated with the standard osinfo database locations:</p>
<dl>
<dt><code>system</code></p>
<dd> This is the primary system-wide database location, intended for use by operating system vendors distributing database files in the native package format.</p>
<dt><code>local</code></p>
<dd> This is the secondary system-wide database location, intended for use by system administrators wishing to provide an updated database for all users.</p>
<dt><code>user</code></p>
<dd> This is the user private database location, intended for use by unprivileged local users wishing to provide applications they use with an updated database.</dl>
<p> If run by a privileged account (ie root), the <code>local</code> database location will be reported by default, otherwise the <code>user</code> location will be reported.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;user</code></p>
<dd> Override the default behaviour to force reporting of the <code>user</code> database location.</p>
<dt><code>&#8211;local</code></p>
<dd> Override the default behaviour to force reporting of the <code>local</code> database location.</p>
<dt><code>&#8211;system</code></p>
<dd> Override the default behaviour to force reporting of the <code>system</code> database location.</p>
<dt><code>&#8211;dir=PATH</code></p>
<dd> Override the default behaviour to force reporting of the custom directory <font SIZE="-1"><code>PATH</code></font>.</p>
<dt><code>&#8211;root=PATH</code></p>
<dd> Prefix the database location with the root directory given by <tt>&quot;PATH&quot;</tt>. This is useful when wishing to report paths relative to a chroot environment or equivalent.</dl>
<h2>EXIT STATUS</h2>
<p> The exit status will be 0 if the requested path was reported, or 1 if the arguments were invalid.</p>
<h2>SEE ALSO</h2>
<p> <tt>&quot;<a href="/docs/linux/man/1-osinfo-db-export/">osinfo-db-export</a>(1)&quot;</tt>, <tt>&quot;<a href="/docs/linux/man/1-osinfo-db-import/">osinfo-db-import</a>(1)&quot;</tt></p>
<h2>AUTHORS</h2>
<p> Daniel P. Berrange &lt;berrange [at] redhat.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2016 Red Hat, Inc.</p>
<h2>LICENSE</h2>
<p> <tt>&quot;osinfo-db-import&quot;</tt> is distributed under the terms of the <font SIZE="-1">GNU LGPL</font> v2+ license. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font> </p>
<h2>Index</h2>
