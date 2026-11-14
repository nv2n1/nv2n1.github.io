---
title: "stg-uncommit(1)"
name: "stg-uncommit"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-uncommit/"
description: "stg-uncommit – Turn regular git commits into StGit patches"
---

<h2 class="name">NAME</h2>
<p> stg-uncommit &#8211; Turn regular git commits into StGit patches </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg uncommit[--]&lt;patch - name - 1&gt;[&lt;patch - name - 2&gt;...] stg uncommit - n NUM[--][&lt;prefix&gt;] stg uncommit - t&lt;committish&gt;[-x]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Take one or more git commits at the base of the current stack and turn them into StGIT patches. The new patches are created as applied patches at the bottom of the stack. This is the opposite of <i>stg commit</i>. </p>
<p> By default, the number of patches to uncommit is determined by the number of patch names provided on the command line. First name is used for the first patch to uncommit, i.e. for the newest patch. </p>
<p> The -n/&#8211;number option specifies the number of patches to uncommit. In this case, at most one patch name may be specified. It is used as prefix to which the patch number is appended. If no patch names are provided on the command line, StGIT automatically generates them based on the first line of the patch description. </p>
<p> The -t/&#8211;to option specifies that all commits up to and including the given commit should be uncommitted. </p>
<p> Only commits with exactly one parent can be uncommitted; in other words, you can&#8217;t uncommit a merge.</p>
<h2>OPTIONS</h2>
<p> -n NUMBER, &#8211;number NUMBER</p>
<dl>
<dt>
<dd> Uncommit the specified number of commits.</dl>
<p> -t TO, &#8211;to TO</p>
<dl>
<dt>
<dd> Uncommit to the specified commit.</dl>
<p> -x, &#8211;exclusive</p>
<dl>
<dt>
<dd> Exclude the commit specified by the &#8211;to option.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
