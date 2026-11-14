---
title: "stg-pop(1)"
name: "stg-pop"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-pop/"
description: "stg-pop – Pop one or more patches from the stack"
---

<h2 class="name">NAME</h2>
<p> stg-pop &#8211; Pop one or more patches from the stack </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg pop[options][--][&lt;patch1&gt;][&lt;patch2&gt;][&lt;patch3&gt;..&lt;patch4&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Pop the topmost patch or a range of patches from the stack. The command fails if there are conflicts or local changes (and &#8211;keep was not specified). </p>
<p> A series of pop and push operations are performed so that only the patches passed on the command line are popped from the stack. Some of the push operations may fail because of conflicts (&quot;stg undo&quot; would revert the last push operation).</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> Pop all the applied patches.</dl>
<p> -n NUMBER, &#8211;number NUMBER</p>
<dl>
<dt>
<dd> Pop the specified number of patches. </p>
<p> With a negative number, pop all but that many patches.</dl>
<p> -k, &#8211;keep</p>
<dl>
<dt>
<dd> Keep the local changes.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
