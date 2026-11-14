---
title: "sc_auto_vec(3)"
name: "sc_auto_vec"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_auto_vec/"
description: "sc::auto_vec –"
---

<p>sc::auto_vec &#8211; </p>
<p> The <code>auto_vec</code> class functions much like auto_ptr, except it contains references to arrays.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;autovec.h&gt;

Public Types</code></pre>
<p> typedef T <code>element_type</code></p>
<h3>Public Member Functions</h3>
<p><code>auto_vec</code> (T *d=0) throw ()<br />
 <i>Creates a new </i><code>auto_vec</code> for a vector, d, of type T.<br />
 <code>auto_vec</code> (<code>auto_vec</code> &amp;av) throw ()<br />
 <i>Create a </i><code>auto_vec</code>, transferring the storage from another.<br />
 <code>~auto_vec</code> () throw ()<br />
 <i>This will delete the vector. </i><br />
 <code>auto_vec</code> &amp; <code>operator=</code> (<code>auto_vec</code> &amp;av) throw ()<br />
 <i>This member transfers the data from av to this. </i><br />
 T * <code>get</code> () const throw ()<br />
 <i>Returns the pointer. </i><br />
 T &amp; <code>operator[]</code> (size_t i) throw ()<br />
 <i>Returns the i&#8217;th element. </i><br />
 T * <code>release</code> () throw ()<br />
 <i>Release ownership. </i><br />
 void <code>reset</code> (T *d=0) throw ()<br />
 <i>Assign to a new value. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class sc::auto_vec&lt; T &gt;</h3>
<p>The <code>auto_vec</code> class functions much like auto_ptr, except it contains references to arrays. </p>
<p> The delete[] operator will be used to deallocate data.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;class T&gt; <code>sc::auto_vec</code>&lt; T &gt;::<code>auto_vec</code> (T * d = 0) throw () [inline, explicit]</h3>
<p>Creates a new <code>auto_vec</code> for a vector, d, of type T. The d argument must be created with the vector new operator: new T[&#8230;].</p>
<h3>template&lt;class T&gt; <code>sc::auto_vec</code>&lt; T &gt;::<code>auto_vec</code> (<code>auto_vec</code>&lt; T &gt; &amp; av) throw () [inline]</h3>
<p>Create a <code>auto_vec</code>, transferring the storage from another.</p>
<h3>template&lt;class T&gt; <code>sc::auto_vec</code>&lt; T &gt;::~<code>auto_vec</code> () throw () [inline]</h3>
<p>This will delete the vector.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;class T&gt; T* <code>sc::auto_vec</code>&lt; T &gt;::get () const throw () [inline]</h3>
<p>Returns the pointer.</p>
<h3>template&lt;class T&gt; <code>auto_vec</code>&amp; <code>sc::auto_vec</code>&lt; T &gt;::operator= (<code>auto_vec</code>&lt; T &gt; &amp; av) throw () [inline]</h3>
<p>This member transfers the data from av to this.</p>
<h3>template&lt;class T&gt; T&amp; <code>sc::auto_vec</code>&lt; T &gt;::operator[] (size_t i) throw () [inline]</h3>
<p>Returns the i&#8217;th element.</p>
<h3>template&lt;class T&gt; T* <code>sc::auto_vec</code>&lt; T &gt;::release () throw () [inline]</h3>
<p>Release ownership.</p>
<h3>template&lt;class T&gt; void <code>sc::auto_vec</code>&lt; T &gt;::reset (T * d = 0) throw () [inline]</h3>
<p>Assign to a new value. </p>
<p> Referenced by sc::auto_vec&lt; double &gt;::operator=().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
