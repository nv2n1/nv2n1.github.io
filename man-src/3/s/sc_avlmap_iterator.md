---
title: "sc_avlmap_iterator(3)"
name: "sc_avlmap_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_avlmap_iterator/"
---

sc::AVLMap::iterator -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>iterator (const EAVLMMap&lt; K, AVLMapNode&lt; K, T &gt; &gt; *m, AVLMapNode&lt; K, T &gt; *n)



iterator (const eavl_typename AVLMap&lt; K, T &gt;::iterator &amp;i)



void operator++ ()



void operator++ (int)



int operator== (const eavl_typename AVLMap&lt; K, T &gt;::iterator &amp;i) const



int operator!= (const eavl_typename AVLMap&lt; K, T &gt;::iterator &amp;i) const



void operator= (const eavl_typename AVLMap&lt; K, T &gt;::iterator &amp;i)



const K &amp; key () const



T &amp; data ()</code></pre>

<h3>template&lt;class K, class T&gt; class sc::AVLMap&lt; K, T &gt;::iterator</h3>



<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
