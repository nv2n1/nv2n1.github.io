---
title: "quantlib_lastfixingquote(3)"
name: "quantlib_lastfixingquote"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lastfixingquote/"
description: "QuantLib::LastFixingQuote – Quote adapter for the last fixing available of a given Index."
---

<p>QuantLib::LastFixingQuote &#8211; <code>Quote</code> adapter for the last fixing available of a given <code>Index</code>. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/quotes/lastfixingquote.hpp&gt; </p>
<p> Inherits <code>QuantLib::Quote</code>, and <code>QuantLib::Observer</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LastFixingQuote</code> (const boost::shared_ptr&lt; <code>Index</code> &gt; &amp;index) </p>
<p> <code>Quote interface</code> </p>
<p> <code>Real</code> <code>value</code> () const<br />
 <i>returns the current value </i><br />
 bool <code>isValid</code> () const<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<p> <code>LastFixingQuote interface</code> </p>
<p> const boost::shared_ptr&lt; <code>Index</code> &gt; &amp; <code>index</code> () const </p>
<p> <code>Date</code> <code>referenceDate</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>Index</code> &gt; <code>index_</code> </p>
<h2>Detailed Description</h2>
<p><code>Quote</code> adapter for the last fixing available of a given <code>Index</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
