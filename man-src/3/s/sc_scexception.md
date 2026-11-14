---
title: "sc_scexception(3)"
name: "sc_scexception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scexception/"
description: "sc::SCException –"
---

<p>sc::SCException &#8211; </p>
<p> This is a std::exception specialization that records information about where an exception took place.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherited by <code>sc::AlgorithmException</code>, <code>sc::InputError</code>, <code>sc::LimitExceeded&lt; T &gt;</code>, <code>sc::ProgrammingError</code>, and <code>sc::SystemException</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCException</code> (const char *description=0, const char *file=0, int line=0, const <code>ClassDesc</code> *class_desc=0, const char *exception_type=&#8217;SCException&#8217;) throw () </p>
<p> <code>SCException</code> (const <code>SCException</code> &amp;) throw () </p>
<p> const char * <code>what</code> () const throw ()<br />
 <i>Reimplementation of std::exception::what(). </i><br />
 const char * <code>description</code> () const throw () </p>
<p> const char * <code>file</code> () const throw () </p>
<p> int <code>line</code> () const throw () </p>
<p> const <code>ClassDesc</code> * <code>class_desc</code> () const throw () </p>
<p> const char * <code>exception_type</code> () const throw () </p>
<p> std::ostream &amp; <code>elaborate</code> ()<br />
 <i>Returns a stream where addition information about the exception can be written. </i></p>
<h2>Detailed Description</h2>
<p>This is a std::exception specialization that records information about where an exception took place.</p>
<h2>Member Function Documentation</h2>
<h3>std::ostream&amp; sc::SCException::elaborate ()</h3>
<p>Returns a stream where addition information about the exception can be written. This will throw if a valid stream cannot be returned (possibly due to low memory).</p>
<h3>const char* sc::SCException::what () const throw ()</h3>
<p>Reimplementation of std::exception::what(). The returned std::string is only valid for the lifetime of this object.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
