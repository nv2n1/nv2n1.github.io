---
title: "git-for-each-ref(1)"
name: "git-for-each-ref"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-for-each-ref/"
description: "git-for-each-ref – Output information on each ref"
---

<h2 class="name">NAME</h2>
<p> git-for-each-ref &#8211; Output information on each ref </p>
<h2>SYNOPSIS</h2>
<pre><code>
git for-each-ref [--count=&lt;count&gt;] [--shell|--perl|--python|--tcl]
                   [(--sort=&lt;key&gt;)...] [--format=&lt;format&gt;] [&lt;pattern&gt;...]
                   [--points-at=&lt;object&gt;]
                   [--merged[=&lt;object&gt;]] [--no-merged[=&lt;object&gt;]]
                   [--contains[=&lt;object&gt;]] [--no-contains[=&lt;object&gt;]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Iterate over all refs that match <code>&lt;pattern&gt;</code> and show them according to the given <code>&lt;format&gt;</code>, after sorting them according to the given set of <code>&lt;key&gt;</code>. If <code>&lt;count&gt;</code> is given, stop after showing that many refs. The interpolated values in <code>&lt;format&gt;</code> can optionally be quoted as string literals in the specified host language allowing their direct evaluation in that language.</p>
<h2>OPTIONS</h2>
<p> &lt;pattern&gt;&#8230;</p>
<dl>
<dt>
<dd> If one or more patterns are given, only refs are shown that match against at least one pattern, either using <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) or literally, in the latter case matching completely or from the beginning up to a slash.</dl>
<p> &#8211;count=&lt;count&gt;</p>
<dl>
<dt>
<dd> By default the command shows all refs that match <code>&lt;pattern&gt;</code>. This option makes it stop after showing that many refs.</dl>
<p> &#8211;sort=&lt;key&gt;</p>
<dl>
<dt>
<dd> A field name to sort on. Prefix <code>&#8211;</code> to sort in descending order of the value. When unspecified, <code>refname</code> is used. You may use the &#8211;sort=&lt;key&gt; option multiple times, in which case the last key becomes the primary key.</dl>
<p> &#8211;format=&lt;format&gt;</p>
<dl>
<dt>
<dd> A string that interpolates <code>%(fieldname)</code> from a ref being shown and the object it points at. If <code>fieldname</code> is prefixed with an asterisk (<code>*</code>) and the ref points at a tag object, use the value for the field in the object which the tag object refers to (instead of the field in the tag object). When unspecified, <code>&lt;format&gt;</code> defaults to <code>%(objectname) SPC %(objecttype) TAB %(refname)</code>. It also interpolates <code>%%</code> to <code>%</code>, and <code>%xx</code> where <code>xx</code> are hex digits interpolates to character with hex code <code>xx</code>; for example <code>%00</code> interpolates to <code>
