---

title: "ieee1284_free_ports(3)"
name: "ieee1284_free_ports"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_free_ports/"
description: "ieee1284_free_ports – safely deallocate a port list"
---

<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>void ieee1284_free_ports(struct parport_list&nbsp;<wbr>*</code><i>list</i><code>);</code></dt></dl>
<dd>When the port list will no longer be used, the program should call <code>ieee1284_free_ports</code> giving it a pointer to the parport_list structure that holds the list of ports returned by <code>ieee1284_find_ports</code>(3). The ports are reference counted with the <code>ieee1284_open</code> and <code>ieee1284_close</code> functions, and so the port list may be freed even if it contains pointers to ports that are still open.</dd>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
