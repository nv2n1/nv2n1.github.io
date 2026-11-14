---
title: "sc_eavlmmap(3)"
name: "sc_eavlmmap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_eavlmmap/"
description: "sc::EAVLMMap –"
---

<p>sc::EAVLMMap &#8211;</p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>iterator</code></p>
<h3>Public Member Functions</h3>
<p>T *&amp; <code>rlink</code> (T *n) const </p>
<p> T * <code>rlink</code> (const T *n) const </p>
<p> T *&amp; <code>llink</code> (T *n) const </p>
<p> T * <code>llink</code> (const T *n) const </p>
<p> T *&amp; <code>uplink</code> (T *n) const </p>
<p> T * <code>uplink</code> (const T *n) const </p>
<p> int &amp; <code>balance</code> (T *n) const </p>
<p> int <code>balance</code> (const T *n) const </p>
<p> K &amp; <code>key</code> (T *n) const </p>
<p> const K &amp; <code>key</code> (const T *n) const </p>
<p> int <code>compare</code> (T *n, T *m) const </p>
<p> int <code>compare</code> (T *n, const K &amp;m) const </p>
<p> <code>EAVLMMap</code> (<code>EAVLMMapNode</code>&lt; K, T &gt; T::*node) </p>
<p> void <code>initialize</code> (<code>EAVLMMapNode</code>&lt; K, T &gt; T::*node) </p>
<p> void <code>clear_without_delete</code> () </p>
<p> void <code>clear</code> () </p>
<p> void <code>insert</code> (T *) </p>
<p> void <code>remove</code> (T *) </p>
<p> T * <code>find</code> (const K &amp;) const </p>
<p> int <code>height</code> (T *node) </p>
<p> int <code>height</code> () </p>
<p> void <code>check</code> () </p>
<p> void <code>check_node</code> (T *) const </p>
<p> T * <code>start</code> () const </p>
<p> void <code>next</code> (const T *&amp;) const </p>
<p> void <code>next</code> (T *&amp;) const </p>
<p> <code>iterator</code> <code>begin</code> () </p>
<p> <code>iterator</code> <code>end</code> () </p>
<p> void <code>print</code> () </p>
<p> int <code>length</code> () const </p>
<p> int <code>depth</code> (T *)</p>
<h3>template&lt;class K, class T&gt; class sc::EAVLMMap&lt; K, T &gt;</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
