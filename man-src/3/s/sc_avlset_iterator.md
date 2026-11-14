---
title: "sc_avlset_iterator(3)"
name: "sc_avlset_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_avlset_iterator/"
---

sc::AVLSet::iterator -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>iterator (const EAVLMMap&lt; K, AVLMapNode&lt; K, int &gt; &gt; *m, const AVLMapNode&lt; K, int &gt; *n)



iterator (const eavl_typename AVLSet&lt; K &gt;::iterator &amp;i)



void operator++ ()



void operator++ (int)



int operator== (const eavl_typename AVLSet&lt; K &gt;::iterator &amp;i) const



int operator!= (const eavl_typename AVLSet&lt; K &gt;::iterator &amp;i) const



void operator= (const eavl_typename AVLSet&lt; K &gt;::iterator &amp;i)



const K &amp; key () const



const K &amp; operator* () const</code></pre>

<h3>template&lt;class K&gt; class sc::AVLSet&lt; K &gt;::iterator</h3>



<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
