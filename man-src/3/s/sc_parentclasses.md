---
title: "sc_parentclasses(3)"
name: "sc_parentclasses"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_parentclasses/"
---

sc::ParentClasses - 

 Gives a list of parent classes of a class.

<h2>Synopsis</h2>

<pre><code>

#include &lt;class.h&gt;

Public Member Functions
void init (const char *)



ParentClass &amp; parent (int i)



const ParentClass &amp; parent (int i) const



ParentClass &amp; operator[] (int i)



const ParentClass &amp; operator[] (int i) const



int n () const



void change_parent (ClassDesc *oldcd, ClassDesc *newcd)</code></pre>

<h2>Detailed Description</h2>

Gives a list of parent classes of a class.

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
