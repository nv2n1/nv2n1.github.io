---
title: "sc_scdimension(3)"
name: "sc_scdimension"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scdimension/"
description: "sc::SCDimension –"
---

<p>sc::SCDimension &#8211; </p>
<p> The <code>SCDimension</code> class is used to determine the size and blocking of matrices.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;dim.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCDimension (int n, const char *name=0)


Create a dimension with an optional name.


SCDimension (const Ref&lt; SCBlockInfo &gt; &amp;, const char *name=0)



SCDimension (int n, int nblocks, const int *blocksizes=0, const char *name=0)



SCDimension (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


SCDimension (StateIn &amp;s)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


int equiv (const SCDimension *) const


Test to see if two dimensions are equivalent.


int n () const


Return the dimension.


const char * name () const


Return the name of the dimension.


Ref&lt; SCBlockInfo &gt; blocks ()


Return the blocking information for this dimension.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about this dimension to o.



Protected Member Functions
SCDimension (const char *name=0)



Protected Attributes
char * name_



int n_



Ref&lt; SCBlockInfo &gt; blocks_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SCDimension</code> class is used to determine the size and blocking of matrices. </p>
<p> The blocking information is stored by an object of class <code>SCBlockInfo</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SCDimension::SCDimension (int n, const char * name = 0)</h3>
<p>Create a dimension with an optional name. The name is a copy of the &#8216;0&#8217; terminated string name.</p>
<h3>sc::SCDimension::SCDimension (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;n&quot; 1c This gives size of the dimension. One of n or blocks is required. </p>
<dl>
<dt>blocks</p>
<dd>The block information for the dimension can be given as a <code>SCBlockInfo</code> object. One of n or blocks is required.</dl>
<h2>Member Function Documentation</h2>
<h3>const char* sc::SCDimension::name () const [inline]</h3>
<p>Return the name of the dimension. If no name was given to the constructor, then return 0.</p>
<h3>void sc::SCDimension::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
