---
title: "osinfo-db-validate(1)"
name: "osinfo-db-validate"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osinfo-db-validate/"
description: "osinfo-db-validate – Validate libosinfo XML data files"
---

<h2 class="name">NAME</h2>
<p> osinfo-db-validate &#8211; Validate libosinfo XML data files </p>
<h2>SYNOPSIS</h2>
<p> osinfo-db-validate [<font SIZE="-1">OPTIONS&#8230;</font>] </p>
<p> osinfo-db-validate [<font SIZE="-1">OPTIONS&#8230;</font>] <font SIZE="-1">LOCAL-PATH1</font> [<font SIZE="-1">LOCAL-PATH2&#8230;</font>] </p>
<p> osinfo-db-validate [<font SIZE="-1">OPTIONS&#8230;</font>] <font SIZE="-1">URI1</font> [<font SIZE="-1">URI2&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>osinfo-db-validate</code> tool is able to validate <font SIZE="-1">XML</font> files in one of the osinfo database locations for compliance with the <font SIZE="-1">RNG</font> schema.</p>
<dl>
<dt><code>system</code></p>
<dd> This is the primary system-wide database location, intended for use by operating system vendors distributing database files in the native package format. The <font SIZE="-1">RNG</font> schema is expected to be present in this location.</p>
<dt><code>local</code></p>
<dd> This is the secondary system-wide database location, intended for use by system administrators wishing to provide an updated database for all users. This location may provide an <font SIZE="-1">RNG</font> schema override, otherwise the <font SIZE="-1">RNG</font> schema from the system location will be used.</p>
<dt><code>user</code></p>
<dd> This is the user private database location, intended for use by unprivileged local users wishing to provide applications they use with an updated database. This location may provide an <font SIZE="-1">RNG</font> schema override, otherwise the <font SIZE="-1">RNG</font> schema from the local location will be used, or failing that the system location.</dl>
<p> If run by a privileged account (ie root), the <code>local</code> database location will be validate by default, otherwise the <code>user</code> location will be validated. </p>
<p> Alternatively it is possible to directly provide a list of files to be validated using the (<tt>&quot;LOCAL-PATH1&quot;</tt> or <tt>&quot;URI1&quot;</tt>) arguments. </p>
<p> Any validation errors will be displayed on the console when detected.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;user</code></p>
<dd> Override the default behaviour to force validating files from the <code>user</code> database location.</p>
<dt><code>&#8211;local</code></p>
<dd> Override the default behaviour to force validating files from the <code>local</code> database location.</p>
<dt><code>&#8211;system</code></p>
<dd> Override the default behaviour to force validating files from the <code>system</code> database location.</p>
<dt><code>&#8211;dir=PATH</code></p>
<dd> Override the default behaviour to force validating files from the custom directory <font SIZE="-1"><code>PATH</code></font>.</p>
<dt><code>&#8211;root=PATH</code></p>
<dd> Prefix the database location with the root directory given by <tt>&quot;PATH&quot;</tt>. This is useful when wishing to validate files that are in a chroot environment or equivalent.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display verbose progress information when validating files</dl>
<h2>EXIT STATUS</h2>
<p> The exit status will be 0 if all files passed validation, or 1 if a validation error was hit.</p>
<h2>SEE ALSO</h2>
<p> <tt>&quot;<a href="/docs/linux/man/1-osinfo-db-path/">osinfo-db-path</a>(1)&quot;</tt></p>
<h2>AUTHORS</h2>
<p> Daniel P. Berrange &lt;berrange [at] redhat.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012-2016 Red Hat, Inc.</p>
<h2>LICENSE</h2>
<p> <tt>&quot;osinfo-db-validate&quot;</tt> is distributed under the terms of the <font SIZE="-1">GNU LGPL</font> v2+ license. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font> </p>
<h2>Index</h2>
