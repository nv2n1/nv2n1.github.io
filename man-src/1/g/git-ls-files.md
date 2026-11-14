---
title: "git-ls-files(1)"
name: "git-ls-files"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-ls-files/"
description: "git-ls-files – Show information about files in the index and the working tree"
---

<h2 class="name">NAME</h2>
<p> git-ls-files &#8211; Show information about files in the index and the working tree </p>
<h2>SYNOPSIS</h2>
<pre><code>
git ls - files[-z][-t][-v][-f](--[cached | deleted | others | ignored | stage | unmerged | killed | modified]) *
             (-[c | d | o | i | s | u | k | m]) *
             [--eol]
                 [--deduplicate]
                 [-x&lt;pattern&gt; | --exclude = &lt;pattern&gt;]
                 [-X&lt;file&gt; | --exclude - from = &lt;file&gt;]
                 [--exclude - per - directory = &lt;file&gt;]
                 [--exclude - standard]
                 [--error - unmatch][--with - tree = &lt;tree - ish&gt;]
                 [--full - name][--recurse - submodules]
                 [--abbrev[=&lt;n&gt;]][--][&lt;file&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This merges the file listing in the index with the actual working directory list, and shows different combinations of the two. </p>
<p> One or more of the options below may be used to determine the files shown:</p>
<h2>OPTIONS</h2>
<p> -c, &#8211;cached</p>
<dl>
<dt>
<dd> Show cached files in the output (default)</dl>
<p> -d, &#8211;deleted</p>
<dl>
<dt>
<dd> Show deleted files in the output</dl>
<p> -m, &#8211;modified</p>
<dl>
<dt>
<dd> Show modified files in the output</dl>
<p> -o, &#8211;others</p>
<dl>
<dt>
<dd> Show other (i.e. untracked) files in the output</dl>
<p> -i, &#8211;ignored</p>
<dl>
<dt>
<dd> Show only ignored files in the output. When showing files in the index, print only those matched by an exclude pattern. When showing &quot;other&quot; files, show only those matched by an exclude pattern. Standard ignore rules are not automatically activated, therefore at least one of the <code>&#8211;exclude*</code> options is required.</dl>
<p> -s, &#8211;stage</p>
<dl>
<dt>
<dd> Show staged contents&#8217; mode bits, object name and stage number in the output.</dl>
<p> &#8211;directory</p>
<dl>
<dt>
<dd> If a whole directory is classified as &quot;other&quot;, show just its name (with a trailing slash) and not its whole contents.</dl>
<p> &#8211;no-empty-directory</p>
<dl>
<dt>
<dd> Do not list empty directories. Has no effect without &#8211;directory.</dl>
<p> -u, &#8211;unmerged</p>
<dl>
<dt>
<dd> Show unmerged files in the output (forces &#8211;stage)</dl>
<p> -k, &#8211;killed</p>
<dl>
<dt>
<dd> Show files on the filesystem that need to be removed due to file/directory conflicts for checkout-index to succeed.</dl>
<p> -z</p>
<dl>
<dt>
<dd> 
