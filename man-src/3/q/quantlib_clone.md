---
title: "quantlib_clone(3)"
name: "quantlib_clone"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_clone/"
description: "QuantLib::Clone – cloning proxy to an underlying object"
---

<p>QuantLib::Clone &#8211; cloning proxy to an underlying object </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/utilities/clone.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Clone</code> (std::auto_ptr&lt; T &gt;) </p>
<p> <code>Clone</code> (const T &amp;) </p>
<p> <code>Clone</code> (const <code>Clone</code>&lt; T &gt; &amp;) </p>
<p> <code>Clone</code>&lt; T &gt; &amp; <code>operator=</code> (const T &amp;) </p>
<p> <code>Clone</code>&lt; T &gt; &amp; <code>operator=</code> (const <code>Clone</code>&lt; T &gt; &amp;) </p>
<p> T &amp; <code>operator*</code> () const </p>
<p> T * <code>operator-&gt;</code> () const </p>
<p> bool <code>empty</code> () const </p>
<p> void <code>swap</code> (<code>Clone</code>&lt; T &gt; &amp;t) </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 template&lt;class T &gt; void <code>swap</code> (<code>Clone</code>&lt; T &gt; &amp;, <code>Clone</code>&lt; T &gt; &amp;) </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::Clone&lt; T &gt;</h3>
<p>cloning proxy to an underlying object </p>
<p> When copied, this class will make a clone of its underlying object (which must provide a clone() method returning a std::auto_ptr to a newly-allocated instance.)</p>
<h2>Friends And Related Function Documentation</h2>
<h3>void swap (<code>Clone</code>&lt; T &gt; &amp;, <code>Clone</code>&lt; T &gt; &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
