---
title: "sepolicy-manpage(8)"
name: "sepolicy-manpage"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sepolicy-manpage/"
description: "sepolicy-manpage – Generate a man page based on the installed SELinux Policy"
---

<p>sepolicy-manpage &#8211; Generate a man page based on the installed SELinux Policy </p>
<h2>Synopsis</h2>
<p><code>sepolicy manpage [-w] [-h] [-p PATH ] [-r ROOTDIR ] [-a | -d ]</code> </p>
<h2>Description</h2>
<p>Use sepolicy manpage to generate manpages based on SELinux Policy. </p>
<h2>Options</h2>
<dl>
<dt><i>-a, &#8211;all </i></p>
<dd>Generate Man Pages for All Domains</p>
<dt><i>-d, &#8211;domain </i></p>
<dd>Generate a Man Page for the specified domain. (Supports multiple commands)</p>
<dt><i>-h, &#8211;help </i></p>
<dd>Display help message</p>
<dt><i>-p, &#8211;path</i></p>
<dd>Specify the directory to store the created man pages. (Default to /tmp)</p>
<dt><i>-r, &#8211;root</i></p>
<dd>Specify alternate root directory to generate man pages from. (Default to /)</p>
<dt><i>-w, &#8211;web</i></p>
<dd>Generate an additional HTML man pages for the specified domain(s). </p>
</dl>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8), <a href="/docs/linux/man/8-selinux/">selinux</a>(8) </p>
