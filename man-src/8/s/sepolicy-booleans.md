---
title: "sepolicy-booleans(8)"
name: "sepolicy-booleans"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sepolicy-booleans/"
description: "sepolicy-booleans – Query SELinux Policy to see description of booleans"
---

<p>sepolicy-booleans &#8211; Query SELinux Policy to see description of booleans </p>
<h2>Synopsis</h2>
<p><code>sepolicy booleans [-h] [ -a | -b booleanname &#8230; ]</code> </p>
<h2>Description</h2>
<p>sepolicy booleans will show all booleans and their descriptions, or you can choose individual booleans to display </p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help </i></p>
<dd>Display help message</p>
<dt><i>-a, &#8211;all</i></p>
<dd>Display all boolean descriptions</p>
<dt><i>-b, &#8211;boolean</i></p>
<dd>boolean to get description </p>
</dl>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8), <a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-getsebool/">getsebool</a>(8), <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
