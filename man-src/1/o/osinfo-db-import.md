---
title: "osinfo-db-import(1)"
name: "osinfo-db-import"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osinfo-db-import/"
description: "osinfo-db-import – Import an osinfo database archive"
---

<h2 class="name">NAME</h2>
<p> osinfo-db-import &#8211; Import an osinfo database archive </p>
<h2>SYNOPSIS</h2>
<p> osinfo-db-import [<font SIZE="-1">OPTIONS&#8230;</font>] ARCHIVE-FILE</p>
<h2>DESCRIPTION</h2>
<p> The <code>osinfo-db-import</code> tool will take an osinfo database archive and extract its contents into one of the standard database locations on the current host:</p>
<dl>
<dt><code>system</code></p>
<dd> This is the primary system-wide database location, intended for use by operating system vendors distributing database files in the native package format.</p>
<dt><code>local</code></p>
<dd> This is the secondary system-wide database location, intended for use by system administrators wishing to provide an updated database for all users.</p>
<dt><code>user</code></p>
<dd> This is the user private database location, intended for use by unprivileged local users wishing to provide applications they use with an updated database.</dl>
<p> If run by a privileged account (ie root), the <code>local</code> database location will be used by default, otherwise the <code>user</code> location will be used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;user</code></p>
<dd> Override the default behaviour to force installation into the <code>user</code> database location.</p>
<dt><code>&#8211;local</code></p>
<dd> Override the default behaviour to force installation into the <code>local</code> database location.</p>
<dt><code>&#8211;system</code></p>
<dd> Override the default behaviour to force installation into the <code>system</code> database location.</p>
<dt><code>&#8211;dir=PATH</code></p>
<dd> Override the default behaviour to force installation into the custom directory <font SIZE="-1"><code>PATH</code></font>.</p>
<dt><code>&#8211;root=PATH</code></p>
<dd> Prefix the installation location with the root directory given by <tt>&quot;PATH&quot;</tt>. This is useful when wishing to install into a chroot environment or equivalent.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display verbose progress information when installing files</dl>
<h2>EXIT STATUS</h2>
<p> The exit status will be 0 if all files were installed successfully, or 1 if at least one file could not be installed.</p>
<h2>SEE ALSO</h2>
<p> <tt>&quot;<a href="/docs/linux/man/1-osinfo-db-export/">osinfo-db-export</a>(1)&quot;</tt>, <tt>&quot;<a href="/docs/linux/man/1-osinfo-db-path/">osinfo-db-path</a>(1)&quot;</tt></p>
<h2>AUTHORS</h2>
<p> Daniel P. Berrange &lt;berrange [at] redhat.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2016 Red Hat, Inc.</p>
<h2>LICENSE</h2>
<p> <tt>&quot;osinfo-db-import&quot;</tt> is distributed under the terms of the <font SIZE="-1">GNU LGPL</font> v2+ license. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font> </p>
<h2>Index</h2>
