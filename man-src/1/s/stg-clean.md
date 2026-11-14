---
title: "stg-clean(1)"
name: "stg-clean"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-clean/"
description: "stg-clean – Delete the empty patches in the series"
---

<h2 class="name">NAME</h2>
<p> stg-clean &#8211; Delete the empty patches in the series </p>
<h2>SYNOPSIS</h2>
<pre>
<i>stg</i> clean
</pre>
<h2>DESCRIPTION</h2>
<p> Delete the empty patches in the whole series or only those applied or unapplied. A patch is considered empty if the two commit objects representing its boundaries refer to the same tree object.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;applied</p>
<dl>
<dt>
<dd> Delete the empty applied patches.</dl>
<p> -u, &#8211;unapplied</p>
<dl>
<dt>
<dd> Delete the empty unapplied patches.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
