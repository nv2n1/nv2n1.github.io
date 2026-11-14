---
title: "quantlib_randomdefaultmodel(3)"
name: "quantlib_randomdefaultmodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_randomdefaultmodel/"
description: "QuantLib::RandomDefaultModel – Base class for random default models."
---

<p>QuantLib::RandomDefaultModel &#8211; Base class for random default models. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/randomdefaultmodel.hpp&gt; </p>
<p> Inherited by <code>GaussianRandomDefaultModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>RandomDefaultModel</code> (boost::shared_ptr&lt; Pool &gt; pool) </p>
<p> virtual void <code>nextSequence</code> (Real tmax=QL_MAX_REAL)=0 </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; Pool &gt; <code>pool_</code> </p>
<h2>Detailed Description</h2>
<p>Base class for random default models. </p>
<p> Provides sequences of random default times for each name in the pool.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void nextSequence (Real tmax = QL_MAX_REAL) [pure virtual]</h3>
<p>Generate a sequence of random default times, one for each name in the pool, and store the result in the Pool using method setTime(name). tmax denotes the maximum relevant time- default times &gt; tmax are not computed but set to tmax + 1 instead to save coputation time. </p>
<p> Implemented in <code>GaussianRandomDefaultModel</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
