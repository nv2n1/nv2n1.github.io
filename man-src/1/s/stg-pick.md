---
title: "stg-pick(1)"
name: "stg-pick"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-pick/"
description: "stg-pick – Import a patch from a different branch or a commit object"
---

<h2 class="name">NAME</h2>
<p> stg-pick &#8211; Import a patch from a different branch or a commit object </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg pick[options][--]([&lt;patch1&gt;][&lt;patch2&gt;][&lt;patch3&gt;..&lt;patch4&gt;]) | &lt;commit&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Import one or more patches from a different branch or a commit object into the current series. By default, the name of the imported patch is used as the name of the current patch. It can be overridden with the <i>&#8211;name</i> option. A commit object can be reverted with the <i>&#8211;revert</i> option. The log and author information are those of the commit object.</p>
<h2>OPTIONS</h2>
<p> -n NAME, &#8211;name NAME</p>
<dl>
<dt>
<dd> Use NAME as the patch name.</dl>
<p> -B REF-BRANCH, &#8211;ref-branch REF-BRANCH</p>
<dl>
<dt>
<dd> Pick patches from BRANCH.</dl>
<p> -r, &#8211;revert</p>
<dl>
<dt>
<dd> Revert the given commit object.</dl>
<p> -p COMMITID, &#8211;parent COMMITID</p>
<dl>
<dt>
<dd> Use COMMITID as parent.</dl>
<p> -x, &#8211;expose</p>
<dl>
<dt>
<dd> Append the imported commit id to the patch log.</dl>
<p> &#8211;fold</p>
<dl>
<dt>
<dd> Fold the commit object into the current patch.</dl>
<p> &#8211;update</p>
<dl>
<dt>
<dd> Like fold but only update the current patch files.</dl>
<p> -f FILE, &#8211;file FILE</p>
<dl>
<dt>
<dd> Only fold the given file (can be used multiple times).</dl>
<p> &#8211;unapplied</p>
<dl>
<dt>
<dd> Keep the patch unapplied.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
