---
title: "errno(1)"
name: "errno"
section: "1"
letter: "e"
url: "/docs/linux/man/1-errno/"
description: "errno – look up errno names and descriptions"
---

<h2 class="name">NAME</h2>
<p> errno &#8211; look up errno names and descriptions </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>errno</code> {<i>name-or-code</i>}</p>
<dt> <code>errno</code> [-ls] [&#8211;list]</p>
<dt> <code>errno</code> [-s] [&#8211;search] {<i>word</i>}</p>
<dt> <code>errno</code> [-S] [&#8211;search-all-locales] {<i>word</i>}</dl>
<h2>DESCRIPTION</h2>
<p> <code>errno</code></p>
<dd>looks up errno macro names, errno codes, and the corresponding descriptions. For example, if given ENOENT on a Linux system, it prints out the code 2 and the description &quot;No such file or directory&quot;. If given the code 2, it prints ENOENT and the same description.</p>
<h2>OPTIONS</h2>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> List all errno values.</dl>
<p> <code>-s</code>, <code>&#8211;search</code></p>
<dl>
<dt>
<dd> Search for errors whose description contains all the given words (case-insensitive).</dl>
<p> <code>-S</code>, <code>&#8211;search-all-locales</code></p>
<dl>
<dt>
<dd> Like <code>&#8211;search</code>, but searches all installed locales.</dl>
<h2>AUTHOR</h2>
<p> Lars Wirzenius</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3) </p>
<h2>Index</h2>
