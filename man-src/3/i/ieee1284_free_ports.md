---
title: "ieee1284_free_ports(3)"
name: "ieee1284_free_ports"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_free_ports/"
description: "ieee1284_free_ports – safely deallocate a port list"
---

<h2 class="name">NAME</h2>
<p> ieee1284_free_ports &#8211; safely deallocate a port list </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>void ieee1284_free_ports(struct parport_list&nbsp;<wbr>*</code><i>list</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>When the port list will no longer be used, the program should call <code>ieee1284_free_ports</code> giving it a pointer to the parport_list structure that holds the list of ports returned by <code><a href="/docs/linux/man/3-ieee1284_find_ports/">ieee1284_find_ports</a></code>(3). The ports are reference counted with the <code>ieee1284_open</code> and <code>ieee1284_close</code> functions, and so the port list may be freed even if it contains pointers to ports that are still open.</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
