---
title: "stg-files(1)"
name: "stg-files"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-files/"
description: "stg-files – Show the files modified by a patch (or the current patch)"
---

<h2 class="name">NAME</h2>
<p> stg-files &#8211; Show the files modified by a patch (or the current patch) </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg files[options][--][[&lt;branch&gt;:]&lt;patch&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> List the files modified by the given patch (defaulting to the current one). Passing the <i>&#8211;stat</i> option shows the diff statistics for the given patch. Note that this command doesn&#8217;t show the files modified in the working tree and not yet included in the patch by a <i>refresh</i> command. Use the <i>diff</i> or <i>status</i> commands for these files.</p>
<h2>OPTIONS</h2>
<p> -s, &#8211;stat</p>
<dl>
<dt>
<dd> Show the diffstat.</dl>
<p> &#8211;bare</p>
<dl>
<dt>
<dd> Bare file names (useful for scripting).</dl>
<p> -O OPTIONS, &#8211;diff-opts OPTIONS</p>
<dl>
<dt>
<dd> Extra options to pass to &quot;git diff&quot;.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
