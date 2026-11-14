---
title: "quantlib_gaussianrandomdefaultmodel(3)"
name: "quantlib_gaussianrandomdefaultmodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_gaussianrandomdefaultmodel/"
description: "QuantLib::GaussianRandomDefaultModel –"
---

<p>QuantLib::GaussianRandomDefaultModel &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/randomdefaultmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::RandomDefaultModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>GaussianRandomDefaultModel</code> (boost::shared_ptr&lt; Pool &gt; pool, <code>Handle</code>&lt; <code>OneFactorCopula</code> &gt; copula, Real accuracy, long seed) </p>
<p> void <code>nextSequence</code> (Real tmax=QL_MAX_REAL) </p>
<h2>Detailed Description</h2>
<p>Random default times using a one-factor Gaussian copula.</p>
<h2>Member Function Documentation</h2>
<h3>void nextSequence (Real tmax = QL_MAX_REAL) [virtual]</h3>
<p>Generate a sequence of random default times, one for each name in the pool, and store the result in the Pool using method setTime(name). tmax denotes the maximum relevant time- default times &gt; tmax are not computed but set to tmax + 1 instead to save coputation time. </p>
<p> Implements <code>RandomDefaultModel</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
