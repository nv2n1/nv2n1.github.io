---
title: "git-quiltimport(1)"
name: "git-quiltimport"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-quiltimport/"
description: "git-quiltimport – Applies a quilt patchset onto the current branch"
---

<h2>SYNOPSIS</h2>
<pre><code>
git quiltimport[--dry - run | -n][--author&lt;author&gt;][--patches&lt;dir&gt;]
               [--series&lt;file&gt;][--keep - non - patch]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Applies a quilt patchset onto the current Git branch, preserving the patch boundaries, patch order, and patch descriptions present in the quilt patchset. </p>
<p> For each patch the code attempts to extract the author from the patch description. If that fails it falls back to the author specified with &#8211;author. If the &#8211;author flag was not given the patch description is displayed and the user is asked to interactively enter the author of the patch. </p>
<p> If a subject is not found in the patch description the patch name is preserved as the 1 line subject in the Git description.</p>
<h2>OPTIONS</h2>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
</dt><dd> Walk through the patches in the series and warn if we cannot find all of the necessary information to commit a patch. At the time of this writing only missing author information is warned about.</dd></dl>
<p> &#8211;author Author Name &lt;Author Email&gt;</p>
<dl>
<dt>
</dt><dd> The author name and email address to use when no author information can be found in the patch description.</dd></dl>
<p> &#8211;patches &lt;dir&gt;</p>
<dl>
<dt>
</dt><dd> The directory to find the quilt patches. </dd>
<p> The default for the patch directory is patches or the value of the <code>$QUILT_PATCHES</code> environment variable.</dl>
<p> &#8211;series &lt;file&gt;</p>
<dl>
<dt>
</dt><dd> The quilt series file. </dd>
<p> The default for the series file is &lt;patches&gt;/series or the value of the <code>$QUILT_SERIES</code> environment variable.</dl>
<p> &#8211;keep-non-patch</p>
<dl>
<dt>
</dt><dd> Pass <code>-b</code> flag to <i>git mailinfo</i> (see <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)).</dd></dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
