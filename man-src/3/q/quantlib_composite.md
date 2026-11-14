---
title: "quantlib_composite(3)"
name: "quantlib_composite"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_composite/"
description: "QuantLib::Composite – Composite pattern."
---

<p>QuantLib::Composite &#8211; Composite pattern. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/patterns/composite.hpp&gt; </p>
<p> Inherits T. </p>
<h3>Protected Types</h3>
<p>typedef std::list&lt; boost::shared_ptr&lt; T &gt; &gt;::iterator <code>iterator</code> </p>
<p> typedef std::list&lt; boost::shared_ptr&lt; T &gt; &gt;::const_iterator <code>const_iterator</code> </p>
<h3>Protected Member Functions</h3>
<p>void <code>add</code> (const boost::shared_ptr&lt; T &gt; &amp;c) </p>
<h3>Protected Attributes</h3>
<p>std::list&lt; boost::shared_ptr&lt; T &gt; &gt; <code>components_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::Composite&lt; T &gt;</h3>
<p>Composite pattern. </p>
<p> The typical use of this class is: </p>
<pre> class CompositeFoo : public Composite&lt;Foo&gt; {
 ...
 };</pre>
<p>&nbsp;<wbr>which causes CompositeFoo to inherit from Foo and provides it with methods for adding components. Of course, any abstract Foo interface must still be implemented.&nbsp;<wbr> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
