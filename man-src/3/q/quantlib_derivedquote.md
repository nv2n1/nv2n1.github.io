---
title: "quantlib_derivedquote(3)"
name: "quantlib_derivedquote"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_derivedquote/"
description: "QuantLib::DerivedQuote – market quote whose value depends on another quote"
---

<p>QuantLib::DerivedQuote &#8211; market quote whose value depends on another quote </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/quotes/derivedquote.hpp&gt; </p>
<p> Inherits <code>QuantLib::Quote</code>, and <code>QuantLib::Observer</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DerivedQuote</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;element, const UnaryFunction &amp;f) </p>
<p> <code>Quote interface</code> </p>
<p> <code>Real</code> <code>value</code> () const<br />
 <i>returns the current value </i><br />
 bool <code>isValid</code> () const<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<h2>Detailed Description</h2>
<h3>template&lt;class UnaryFunction&gt; class QuantLib::DerivedQuote&lt; UnaryFunction &gt;</h3>
<p>market quote whose value depends on another quote </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dl>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
