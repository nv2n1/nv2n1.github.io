---
title: "comps2solv(1)"
name: "comps2solv"
section: "1"
letter: "c"
url: "/docs/linux/man/1-comps2solv/"
description: "comps2solv – convert rpm-md comps.xml file into a solv file"
---

<h2 class="name">NAME</h2>
<p> comps2solv &#8211; convert rpm-md comps.xml file into a solv file </p>
<h2>SYNOPSIS</h2>
<p> <code>comps2solv</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The comps.xml file is Fedora&#8217;s way to implement package groups. The comps2solv tool reads the comps xml file from stdin and writes the parsed data as solv file to standard output. The parser will create <code>group:</code> and <code>category:</code> pseudo packages for each comps entry.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mergesolv/">mergesolv</a>(1), <a href="/docs/linux/man/8-createrepo/">createrepo</a>(8)</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
