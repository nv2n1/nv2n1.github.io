---
title: "sc_ref(3)"
name: "sc_ref"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_ref/"
description: "sc::Ref –"
---

<p>sc::Ref &#8211; </p>
<p> A template class that maintains references counts.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;ref.h&gt;</code></pre>
<p> Inherits <code>sc::RefBase</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Ref</code> ()<br />
 <i>Create a reference to a null object. </i><br />
 <code>Ref</code> (T *a)<br />
 <i>Create a reference to the object a. </i><br />
 <code>Ref</code> (const <code>Ref</code>&lt; T &gt; &amp;a)<br />
 <i>Create a reference to the object referred to by a. </i><br />
 template&lt;class A &gt; <code>Ref</code> (const <code>Ref</code>&lt; A &gt; &amp;a)<br />
 <i>Create a reference to the object referred to by a. </i><br />
 <code>~Ref</code> ()<br />
 <i>Create a reference to the object a. </i><br />
 T * <code>operator-&gt;</code> () const<br />
 <i>Returns the reference counted object. </i><br />
 T * <code>pointer</code> () const<br />
 <i>Returns a pointer the reference counted object. </i><br />
 <code>RefCount</code> * <code>parentpointer</code> () const<br />
 <i>Implements the parentpointer pure virtual in the base class. </i><br />
 <code>operator T *</code> () const </p>
<p> T &amp; <code>operator*</code> () const<br />
 <i>Returns a C++ reference to the reference counted object. </i><br />
 int <code>null</code> () const<br />
 <i>Return 1 if this is a reference to a null object. </i><br />
 int <code>nonnull</code> () const<br />
 <i>Return !null(). </i><br />
 template&lt;class A &gt; int <code>operator==</code> (const <code>Ref</code>&lt; A &gt; &amp;a) const<br />
 <i>A variety of ordering and equivalence operators are provided using the </i><code>Identity</code> class.<br />
 template&lt;class A &gt; int <code>operator&gt;=</code> (const <code>Ref</code>&lt; A &gt; &amp;a) const </p>
<p> template&lt;class A &gt; int <code>operator&lt;=</code> (const <code>Ref</code>&lt; A &gt; &amp;a) const </p>
<p> template&lt;class A &gt; int <code>operator&gt;</code> (const <code>Ref</code>&lt; A &gt; &amp;a) const </p>
<p> template&lt;class A &gt; int <code>operator&lt;</code> (const <code>Ref</code>&lt; A &gt; &amp;a) const </p>
<p> template&lt;class A &gt; int <code>operator!=</code> (const <code>Ref</code>&lt; A &gt; &amp;a) const </p>
<p> int <code>compare</code> (const <code>Ref</code>&lt; T &gt; &amp;a) const<br />
 <i>Compare two objects returning -1, 0, or 1. </i><br />
 void <code>clear</code> ()<br />
 <i>Refer to the null object. </i><br />
 <code>Ref</code>&lt; T &gt; &amp; <code>operator=</code> (const <code>Ref</code>&lt; T &gt; &amp;c)<br />
 <i>Assignment to c. </i><br />
 template&lt;class A &gt; <code>Ref</code>&lt; T &gt; &amp; <code>operator=</code> (const <code>Ref</code>&lt; A &gt; &amp;c)<br />
 <i>Assignment to c. </i><br />
 <code>Ref</code>&lt; T &gt; &amp; <code>operator&lt;&lt;</code> (const <code>RefBase</code> &amp;a)<br />
 <i>Assignment to the object that a references using dynamic_cast. </i><br />
 <code>Ref</code>&lt; T &gt; &amp; <code>operator&lt;&lt;</code> (<code>RefCount</code> *a)<br />
 <i>Assigns to the given base class pointer using dynamic_cast. </i><br />
 <code>Ref</code>&lt; T &gt; &amp; <code>operator=</code> (T *cr)<br />
 <i>Assignment to cr. </i><br />
 void <code>assign_pointer</code> (T *cr)<br />
 <i>Assignment to cr. </i><br />
 void <code>check_pointer</code> () const<br />
 <i>Check the validity of the pointer. </i><br />
 void <code>ref_info</code> (std::ostream &amp;os) const<br />
 <i>Print information about the reference to os. </i><br />
 void <code>warn</code> (const char *s) const<br />
 <i>Print a warning concerning the reference. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class sc::Ref&lt; T &gt;</h3>
<p>A template class that maintains references counts. </p>
<p> Several of these operations can cause a reference to an object to be replaced by a reference to a different object. If a reference to a nonnull object is eliminated, the object&#8217;s reference count is decremented and the object is deleted if the reference count becomes zero. </p>
<p> There also may be a to convert to T*, where T is the type of the object which <code>Ref</code> references. Some compilers have bugs that prevent the use of operator T*(). The <code>pointer()</code> member should be used instead.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;class T&gt; <code>sc::Ref</code>&lt; T &gt;::~<code>Ref</code> () [inline]</h3>
<p>Create a reference to the object a. Do a dynamic_cast to convert a to the appropiate type. Create a reference to the object a. Do a dynamic_cast to convert a to the appropiate type. Delete this reference to the object. Decrement the object&#8217;s reference count and delete the object if the count is zero.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;class T&gt; int <code>sc::Ref</code>&lt; T &gt;::compare (const <code>Ref</code>&lt; T &gt; &amp; a) const [inline]</h3>
<p>Compare two objects returning -1, 0, or 1. Similar to the C library routine strcmp.</p>
<h3>template&lt;class T&gt; int <code>sc::Ref</code>&lt; T &gt;::null () const [inline]</h3>
<p>Return 1 if this is a reference to a null object. Otherwise return 0.</p>
<h3>template&lt;class T&gt; T&amp; <code>sc::Ref</code>&lt; T &gt;::operator* () const [inline]</h3>
<p>Returns a C++ reference to the reference counted object. The behaviour is undefined if the object is null.</p>
<h3>template&lt;class T&gt; T* <code>sc::Ref</code>&lt; T &gt;::operator-&gt; () const [inline]</h3>
<p>Returns the reference counted object. The behaviour is undefined if the object is null.</p>
<h3>template&lt;class T&gt; <code>Ref</code>&lt;T&gt;&amp; <code>sc::Ref</code>&lt; T &gt;::operator&lt;&lt; (<code>RefCount</code> * a) [inline]</h3>
<p>Assigns to the given base class pointer using dynamic_cast. If the dynamic_cast fails and the argument is nonnull and has a reference count of zero, then it is deleted. </p>
<p> Reimplemented in <code>sc::RefSCDimension</code>.</p>
<h3>template&lt;class T&gt; template&lt;class A &gt; int <code>sc::Ref</code>&lt; T &gt;::operator== (const <code>Ref</code>&lt; A &gt; &amp; a) const [inline]</h3>
<p>A variety of ordering and equivalence operators are provided using the <code>Identity</code> class.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
