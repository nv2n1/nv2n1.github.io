---
title: "quantlib_forwardvaluequote(3)"
name: "quantlib_forwardvaluequote"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_forwardvaluequote/"
description: "QuantLib::ForwardValueQuote – quote for the forward value of an index"
---

<p>QuantLib::ForwardValueQuote &#8211; quote for the forward value of an index </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/quotes/forwardvaluequote.hpp&gt; </p>
<p> Inherits <code>QuantLib::Quote</code>, and <code>QuantLib::Observer</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ForwardValueQuote</code> (const boost::shared_ptr&lt; <code>Index</code> &gt; &amp;index, const <code>Date</code> &amp;fixingDate) </p>
<p> void <code>update</code> () </p>
<p> <code>Quote interface</code> </p>
<p> <code>Real</code> <code>value</code> () const<br />
 <i>returns the current value </i><br />
 bool <code>isValid</code> () const<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value</p>
<h2>Detailed Description</h2>
<p>quote for the forward value of an index</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
