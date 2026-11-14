---
title: "sc_eavlmmap_iterator(3)"
name: "sc_eavlmmap_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_eavlmmap_iterator/"
---

sc::EAVLMMap::iterator -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>iterator (EAVLMMap&lt; K, T &gt; *m, T *n)



iterator (const eavl_typename EAVLMMap&lt; K, T &gt;::iterator &amp;i)



void operator++ ()



void operator++ (int)



int operator== (const eavl_typename EAVLMMap&lt; K, T &gt;::iterator &amp;i) const



int operator!= (const eavl_typename EAVLMMap&lt; K, T &gt;::iterator &amp;i) const



void operator= (const eavl_typename EAVLMMap&lt; K, T &gt;::iterator &amp;i)



const K &amp; key () const



T &amp; operator* ()



T * operator-&gt; ()</code></pre>

<h3>template&lt;class K, class T&gt; class sc::EAVLMMap&lt; K, T &gt;::iterator</h3>



<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
