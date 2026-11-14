---
title: "ieee1284_set_timeout(3)"
name: "ieee1284_set_timeout"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_set_timeout/"
description: "ieee1284_set_timeout – modify inactivity timeout"
---

<h2 class="name">NAME</h2>
<p> ieee1284_set_timeout &#8211; modify inactivity timeout </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>struct timeval *ieee1284_set_timeout(struct parport&nbsp;<wbr>*</code><i>port</i><code>, struct timeval&nbsp;<wbr>*</code><i>timeout</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>This function sets a new value for the inactivity timeout (used for block transfer functions), and returns the old value. </p>
<p> The <i>port</i> must be claimed. </p>
<p> The <i>timeout</i> parameter may be <code>NULL</code>, in which case the old value is left unchanged.</p>
<h2>RETURN VALUE</h2>
<p> This function returns a pointer to a struct timeval representing the old value. This uses the same storage as the <i>port</i> structure, and so is not valid after closing the port.</p>
<h2>NOTES</h2>
<p> Note that this is an inactivity time-out, not an absolute time-out. During a data transfer, if the peripheral is inactive for the length of time specified then the host gives up. </p>
<p> It is also advisory; no guarantee is made that the transfer will ever complete.</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
