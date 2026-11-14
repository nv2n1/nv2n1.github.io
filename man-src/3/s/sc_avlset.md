---
title: "sc_avlset(3)"
name: "sc_avlset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_avlset/"
description: "sc::AVLSet –"
---

<p>sc::AVLSet &#8211;</p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>iterator</code></p>
<h3>Public Member Functions</h3>
<pre><code>void clear ()



void insert (const K &amp;key)



void remove (const K &amp;key)



int contains (const K &amp;key) const



iterator find (const K &amp;k) const



int height ()



void check ()



int length () const



iterator begin () const



iterator end () const



void operator-= (const AVLSet&lt; K &gt; &amp;s)



void operator|= (const AVLSet&lt; K &gt; &amp;s)



void print ()</code></pre>
<h3>template&lt;class K&gt; class sc::AVLSet&lt; K &gt;</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
