---
title: "sc_refscdimension(3)"
name: "sc_refscdimension"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_refscdimension/"
description: "sc::RefSCDimension –"
---

<p>sc::RefSCDimension &#8211; </p>
<p> The <code>RefSCDimension</code> class is a smart pointer to an <code>SCDimension</code> specialization.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;dim.h&gt;</code></pre>
<p> Inherits <code>Ref&lt; SCDimension &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RefSCDimension ()


Initializes the dimension pointer to 0.


RefSCDimension (const RefSCDimension &amp;d)


Make this and d refer to the same SCDimension.


RefSCDimension (SCDimension *d)


Make this refer to d.


RefSCDimension &amp; operator= (SCDimension *d)


Make this refer to d.


RefSCDimension &amp; operator&lt;&lt; (RefCount *)


Assigns to the given base class pointer using dynamic_cast.


RefSCDimension &amp; operator&lt;&lt; (const RefBase &amp;)


Assignment to the object that a references using dynamic_cast.


RefSCDimension &amp; operator= (const RefSCDimension &amp;d)


Make this and d refer to the same SCDimension.


operator int () const


Return the dimension.


int n () const



void print (std::ostream &amp;o=ExEnv::out0()) const</code></pre>
<h2>Detailed Description</h2>
<p>The <code>RefSCDimension</code> class is a smart pointer to an <code>SCDimension</code> specialization.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::RefSCDimension::RefSCDimension ()</h3>
<p>Initializes the dimension pointer to 0. The reference must be initialized before it is used.</p>
<h2>Member Function Documentation</h2>
<h3><code>RefSCDimension</code>&amp; sc::RefSCDimension::operator&lt;&lt; (<code>RefCount</code> * a)</h3>
<p>Assigns to the given base class pointer using dynamic_cast. If the dynamic_cast fails and the argument is nonnull and has a reference count of zero, then it is deleted. </p>
<p> Reimplemented from <code>sc::Ref&lt; SCDimension &gt;</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
