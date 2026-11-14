---
title: "termstructurehandle_(3)"
name: "termstructurehandle_"
section: "3"
letter: "t"
url: "/docs/linux/man/3-termstructurehandle_/"
description: "QuantLib::FixedRateBondHelper – fixed-coupon bond helper"
---

<p>QuantLib::FixedRateBondHelper &#8211; fixed-coupon bond helper </p>
<h2>Synopsis</h2>
<pre><code>void accept (AcyclicVisitor &amp;)



Protected Attributes</code></pre>
<p> Inherits <code>BootstrapHelper&lt; YieldTermStructure &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p>void accept (AcyclicVisitor &amp;)</p>
<p>Protected Attributes <code>BootstrapHelper interface</code> </p>
<p> <code>Real</code> <code>impliedQuote</code> () const </p>
<p> void <code>setTermStructure</code> (<code>YieldTermStructure</code> *)<br />
 <i>sets the term structure to be used for pricing </i> <code>additional inspectors</code> </p>
<p> boost::shared_ptr&lt; <code>FixedRateBond</code> &gt; <code>bond</code> () const<br />
 <code>Visitability</code> </p>
<pre><code>void accept (AcyclicVisitor &amp;)



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>FixedRateBond</code> &gt; <code>bond_</code> </p>
<p> <code>RelinkableHandle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructureHandle_</code></p>
<h2>Detailed Description</h2>
<p>fixed-coupon bond helper </p>
<p> <code>Warning</code></p>
<dl>
<dd>This class assumes that the reference date does not change between calls of <code>setTermStructure()</code>.</dl>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>, and <code>FittedBondCurve.cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>FixedRateBondHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp; cleanPrice, const boost::shared_ptr&lt; <code>FixedRateBond</code> &gt; &amp; bond)</h3>
<p><code>Warning</code></p>
<dl>
<dd>Setting a pricing engine to the passed bond from external code will cause the bootstrap to fail or to give wrong results. It is advised to discard the bond after creating the helper, so that the helper has sole ownership of it.</dl>
<h2>Member Function Documentation</h2>
<h3>void setTermStructure (<code>YieldTermStructure</code> *) [virtual]</h3>
<p>sets the term structure to be used for pricing </p>
<p> <code>Warning</code></p>
<dl>
<dd>Being a pointer and not a shared_ptr, the term structure is not guaranteed to remain allocated for the whole life of the rate helper. It is responsibility of the programmer to ensure that the pointer remains valid. It is advised that this method is called only inside the term structure being bootstrapped, setting the pointer to <code>this</code>, i.e., the term structure itself.</dl>
<p> Reimplemented from <code>BootstrapHelper&lt; YieldTermStructure &gt;</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
