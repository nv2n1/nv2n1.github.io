---
title: "sc_avlmap(3)"
name: "sc_avlmap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_avlmap/"
description: "sc::AVLMap –"
---

<p>sc::AVLMap &#8211;</p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>iterator</code></p>
<h3>Public Member Functions</h3>
<pre><code>void clear ()



void insert (const K &amp;key, const T &amp;data)



void remove (const K &amp;key)



int contains (const K &amp;k) const



iterator find (const K &amp;) const



T &amp; operator[] (const K &amp;k)



int height ()



void check ()



int length () const



iterator begin () const



iterator end () const



void print ()



Public Attributes</code></pre>
<p> <code>EAVLMMap</code>&lt; K, <code>AVLMapNode</code>&lt; K, T &gt; &gt; <code>map_</code></p>
<h3>template&lt;class K, class T&gt; class sc::AVLMap&lt; K, T &gt;</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
