---
title: "ieee1284_claim(3)"
name: "ieee1284_claim"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_claim/"
description: "ieee1284_claim – claim access to the port"
---

<h2 class="name">NAME</h2>
<p> ieee1284_claim &#8211; claim access to the port </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_claim(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>With the exception of <code><a href="/docs/linux/man/3-ieee1284_get_deviceid/">ieee1284_get_deviceid</a></code>(3), <code>ieee1284_claim</code> must be called on an open port before any other libieee1284 function for accessing a device on it.</p>
<h2>RETURN VALUE</h2>
<p> <code>E1284_OK</code></p>
<dl>
<dt>
<dd> Success. Note that, unless the <code>F1284_EXCL</code> flag was specified to start with, the port should be released within a &#8220;reasonable&#8221; amount of time.</dl>
<p> <code>E1284_NOMEM</code></p>
<dl>
<dt>
<dd> There is not enough memory.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid (for instance, it might not have been opened yet).</dl>
<p> <code>E1284_SYS</code></p>
<dl>
<dt>
<dd> There was a problem at the operating system level. The global variable <i>errno</i> has been set appropriately.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ieee1284_release/">ieee1284_release</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
