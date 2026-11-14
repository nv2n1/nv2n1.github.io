---
title: "sc_rangelockitem(3)"
name: "sc_rangelockitem"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_rangelockitem/"
description: "sc::RangeLockItem –"
---

<p>sc::RangeLockItem &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<p><code>RangeLockItem</code> (<code>RangeLockItem</code> *p, <code>RangeLockItem</code> *n, int s, int f, int v)</p>
<h3>Static Public Member Functions</h3>
<pre><code>static void * operator new (size_t, Pool *)



static void operator delete (void *, Pool *)



Public Attributes</code></pre>
<p> <code>RangeLockItem</code> * <code>prev</code> </p>
<p> <code>RangeLockItem</code> * <code>next</code> </p>
<p> int <code>start</code> </p>
<p> int <code>fence</code> </p>
<p> int <code>value</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
