---
title: "ieee1284_release(3)"
name: "ieee1284_release"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_release/"
description: "ieee1284_release – release a port"
---

<h2 class="name">NAME</h2>
<p> ieee1284_release &#8211; release a port </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>void ieee1284_release(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>This function undoes the effect of <code><a href="/docs/linux/man/3-ieee1284_claim/">ieee1284_claim</a></code>(3) by releasing the port for use by other drivers. It is good practice to release the port whenever convenient. If it is never convenient to do so, the <code>F1284_EXCL</code> flag should be specified at initialization.</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
