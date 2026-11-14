---
title: "ieee1284_find_ports(3)"
name: "ieee1284_find_ports"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_find_ports/"
description: "ieee1284_find_ports – find ports on the system"
---

<h2 class="name">NAME</h2>
<p> ieee1284_find_ports &#8211; find ports on the system </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_find_ports(struct parport_list&nbsp;<wbr>*</code><i>list</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>This function should be called before the other libieee1284 functions. This gives the library a chance to look around and see what&#8217;s available, and gives the program a chance to choose a port to use. </p>
<p> The <i>list</i> is a pointer to a parport_list structure that will be filled in on success. </p>
<p> There are no <i>flags</i> defined; use zero for this parameter.</p>
<h2>RETURN VALUE</h2>
<p> <code>E1284_OK</code></p>
<dl>
<dt>
<dd> Success. <i>list</i> is filled in and must be destroyed using <code><a href="/docs/linux/man/3-ieee1284_free_ports/">ieee1284_free_ports</a></code>(3).</dl>
<p> <code>E1284_NOMEM</code></p>
<dl>
<dt>
<dd> There is not enough memory available.</dl>
<p> <code>E1284_NOTIMPL</code></p>
<dl>
<dt>
<dd> One or more of the supplied flags is not supported in this implementation.</dl>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
