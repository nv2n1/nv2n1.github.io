---
title: "sc_bitarrayltri(3)"
name: "sc_bitarrayltri"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_bitarrayltri/"
---

sc::BitArrayLTri -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>BitArrayLTri (int=0, int=0)



void set (unsigned int i)



void set (unsigned int i, unsigned int j)



int is_set (unsigned int i, unsigned int j) const



int is_set (unsigned int i) const



int operator() (unsigned int i, unsigned int j) const



int operator() (unsigned int i) const



int operator[] (unsigned int i) const



int dim () const



int nrow () const



int ncol () const



int degree (unsigned int i) const
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
