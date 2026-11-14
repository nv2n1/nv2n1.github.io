---
title: "rose(3)"
name: "rose"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rose/"
description: "rose_aton, rose_ntoa, rose_cmp – ROSE Address manipulation routines"
---

<p>rose_aton, rose_ntoa, rose_cmp &#8211; ROSE Address manipulation routines</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netrose/rose.h&gt;

int rose_aton(const char *cp, char *inp);

char *rose_ntoa(rose_address *cp);

int rose_cmp(rose_address *a1, rose_address *a2);</code></pre>
<h2>Description</h2>
<p><code>rose_aton()</code> converts the ROSE address <i>cp</i> from an ASCII representation into network format. </p>
<p> <code>rose_ntoa()</code> converts the ROSE address <i>cp</i> that is network format to a string that is the ASCII representation of the address. </p>
<p> <code>rose_cmp()</code> compares the two ROSE address <i>a1</i> and <i>a2</i> that are in network format.</p>
<h2>Return Value</h2>
<p>The <code>rose_ntoa()</code> and <code>rose_aton()</code> functions return zero if all went ok, -1 if not. </p>
<p> The <code>rose_cmp()</code> returns 0 if address <i>a1</i> and <i>a2</i> are identical, 1 otherwise.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/4-rose/">rose</a></code>(4) </p>
