---
title: "deltainfoxml2solv(1)"
name: "deltainfoxml2solv"
section: "1"
letter: "d"
url: "/docs/linux/man/1-deltainfoxml2solv/"
description: "deltainfoxml2solv – convert rpm-md’s deltainfo format into a solv file"
---

<h2 class="name">NAME</h2>
<p> deltainfoxml2solv &#8211; convert rpm-md&#8217;s deltainfo format into a solv file </p>
<h2>SYNOPSIS</h2>
<p> <code>deltainfoxml2solv</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The deltainfoxml2solv tool reads rpm-md&#8217;s <code>deltainfo.xml</code> data from stdin, and writes it as solv file to standard output. Some distributions name the input <code>prestodelta.xml</code> instead. Each delta rpm element is converted and added as <code>repository:deltainfo</code> element to the meta section of the solv file.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mergesolv/">mergesolv</a>(1), <a href="/docs/linux/man/8-createrepo/">createrepo</a>(8)</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
