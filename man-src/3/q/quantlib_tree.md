---
title: "quantlib_tree(3)"
name: "quantlib_tree"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_tree/"
description: "QuantLib::Tree – Tree approximating a single-factor diffusion"
---

<p>QuantLib::Tree &#8211; Tree approximating a single-factor diffusion </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/lattices/tree.hpp&gt; </p>
<p> Inherits <code>CuriouslyRecurringTemplate&lt; T &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Tree</code> (Size columns) </p>
<p> Size <code>columns</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::Tree&lt; T &gt;</h3>
<p>Tree approximating a single-factor diffusion </p>
<p> Derived classes must implement the following interface: </p>
<pre> public:
 Real underlying(Size i, Size index) const;
 Size size(Size i) const;
 Size descendant(Size i, Size index, Size branch) const;
 Real probability(Size i, Size index, Size branch) const;</pre>
<p>&nbsp;<wbr>and provide a public enumeration&nbsp;<wbr> </p>
<pre> enum { branches = N };</pre>
<p>&nbsp;<wbr>where N is a suitable constant&nbsp;<wbr>(2 for binomial, 3 for trinomial&#8230;)&nbsp;<wbr> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
