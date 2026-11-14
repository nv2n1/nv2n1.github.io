---
title: "sc_identifier(3)"
name: "sc_identifier"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_identifier/"
---

sc::Identifier - 

 Identifier's are used to distinguish and order objects.

<h2>Synopsis</h2>

<pre><code>

#include &lt;identity.h&gt;

Public Member Functions
Identifier ()


Create an Identifier for a null object.


Identifier (const Identity *i)


Create an Identifier for the given object.


Identifier (const Identifier &amp;i)


Create an Identifier for the given object.


~Identifier ()


The destructor does nothing.


void operator= (const Identifier &amp;i)


Assign to the given Identifier.


int operator&lt; (const Identifier &amp;i) const


Less than.


int operator&gt; (const Identifier &amp;i) const


Greater than.


int operator== (const Identifier &amp;i) const


Equal.


int operator&lt;= (const Identifier &amp;i) const


Less than or equal.


int operator&gt;= (const Identifier &amp;i) const


Greater than or equal.


int operator!= (const Identifier &amp;i) const


Not equal.


void print (std::ostream &amp;) const</code></pre>

<h2>Detailed Description</h2>

Identifier's are used to distinguish and order objects. 

 On many architectures a pointer to the object will suffice, but the C++ standard only guarantees that this works for two pointers pointing within the same structure or array. Classes need to inherit from <b>Identity</b> to use this mechanism. <b>Identity</b>, <b>Identifier</b>, and the shorthand boolean operations may have to be modified for certain architectures.

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
