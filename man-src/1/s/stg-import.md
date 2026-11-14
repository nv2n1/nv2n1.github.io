---
title: "stg-import(1)"
name: "stg-import"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-import/"
description: "stg-import – Import a GNU diff file as a new patch"
---

<h2 class="name">NAME</h2>
<p> stg-import &#8211; Import a GNU diff file as a new patch </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg import[options][--][&lt;file&gt; | &lt;url&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Create a new patch and apply the given GNU diff file (or the standard input). By default, the file name is used as the patch name but this can be overridden with the <i>&#8211;name</i> option. The patch can either be a normal file with the description at the top or it can have standard mail format, the Subject, From and Date headers being used for generating the patch information. The command can also read series and mbox files. </p>
<p> If a patch does not apply cleanly, the failed diff is written to the .stgit-failed.patch file and an empty StGIT patch is added to the stack. </p>
<p> The patch description has to be separated from the data with a <i>&#8212;</i> line.</p>
<h2>OPTIONS</h2>
<p> -m, &#8211;mail</p>
<dl>
<dt>
<dd> Import the patch from a standard e-mail file.</dl>
<p> -M, &#8211;mbox</p>
<dl>
<dt>
<dd> Import a series of patches from an mbox file.</dl>
<p> -s, &#8211;series</p>
<dl>
<dt>
<dd> Import a series of patches from a series file or a tar archive.</dl>
<p> -u, &#8211;url</p>
<dl>
<dt>
<dd> Import a patch from a URL.</dl>
<p> -n NAME, &#8211;name NAME</p>
<dl>
<dt>
<dd> Use NAME as the patch name.</dl>
<p> -p N, &#8211;strip N</p>
<dl>
<dt>
<dd> Remove N leading slashes from diff paths (default 1).</dl>
<p> -t, &#8211;stripname</p>
<dl>
<dt>
<dd> Strip numbering and extension from patch name.</dl>
<p> -i, &#8211;ignore</p>
<dl>
<dt>
<dd> Ignore the applied patches in the series.</dl>
<p> &#8211;replace</p>
<dl>
<dt>
<dd> Replace the unapplied patches in the series.</dl>
<p> -b BASE, &#8211;base BASE</p>
<dl>
<dt>
<dd> Use BASE instead of HEAD for file importing.</dl>
<p> &#8211;reject</p>
<dl>
<dt>
<dd> Leave the rejected hunks in corresponding *.rej files.</dl>
<p> -e, &#8211;edit</p>
<dl>
<dt>
<dd> Invoke an editor for the patch description.</dl>
<p> -d, &#8211;showdiff</p>
<dl>
<dt>
<dd> Show the patch content in the editor buffer.</dl>
<p> -a &quot;NAME &lt;EMAIL&gt;&quot;, &#8211;author &quot;NAME &lt;EMAIL&gt;&quot;</p>
<dl>
<dt>
<dd> Use &quot;NAME &lt;EMAIL&gt;&quot; as the author details.</dl>
<p> &#8211;authname AUTHNAME</p>
<dl>
<dt>
<dd> Use AUTHNAME as the author name.</dl>
<p> &#8211;authemail AUTHEMAIL</p>
<dl>
<dt>
<dd> Use AUTHEMAIL as the author e-mail.</dl>
<p> &#8211;authdate AUTHDATE</p>
<dl>
<dt>
<dd> Use AUTHDATE as the author date.</dl>
<p> &#8211;sign</p>
<dl>
<dt>
<dd> Add a &quot;Signed-off-by:&quot; to the end of the patch.</dl>
<p> &#8211;ack</p>
<dl>
<dt>
<dd> Add an &quot;Acked-by:&quot; line to the end of the patch.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
