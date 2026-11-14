---
title: "ieee1284_unref(3)"
name: "ieee1284_unref"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_unref/"
description: "ieee1284_ref, ieee1284_unref – modify a port’s reference count"
---

<h2 class="name">NAME</h2>
<p> ieee1284_ref, ieee1284_unref &#8211; modify a port&#8217;s reference count </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_ref(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></p>
<dt> <code>int ieee1284_unref(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>If you want to free the port list from <code>ieee1284_find_ports</code> but open one of the ports later on, you will need to prevent it from being destroyed in <code>ieee1284_free_ports</code>. Each port has a reference count, and you can use <code>ieee1284_ref</code> to increment it and <code>ieee1284_unref</code> to decrement it. </p>
<p> If you use <code>ieee1284_ref</code> at any stage, you must later call <code>ieee1284_unref</code> to relinquish the extra reference. If you do not do this, the resources associated with the port will not be cleaned up. </p>
<p> If you have not previously used <code>ieee1284_ref</code> on a port, you must not use <code>ieee1284_unref</code> on it.</p>
<h2>RETURN VALUE</h2>
<p> These functions return the number of references held after the increment or decrement.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ieee1284_open/">ieee1284_open</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
