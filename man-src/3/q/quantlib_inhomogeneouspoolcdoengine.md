---
title: "quantlib_inhomogeneouspoolcdoengine(3)"
name: "quantlib_inhomogeneouspoolcdoengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_inhomogeneouspoolcdoengine/"
description: "QuantLib::InhomogeneousPoolCDOEngine – CDO engine, loss disctribution bucketing for finite inhomogeneous pool."
---

<p>QuantLib::InhomogeneousPoolCDOEngine &#8211; <code>CDO</code> engine, loss disctribution bucketing for finite inhomogeneous pool. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/syntheticcdoengines.hpp&gt; </p>
<p> Inherits CDOEngine. </p>
<h3>Public Member Functions</h3>
<p><code>InhomogeneousPoolCDOEngine</code> (const <code>Handle</code>&lt; <code>OneFactorCopula</code> &gt; copula, Size nBuckets, <code>Period</code> stepSize=1 *Days) </p>
<h3>Protected Attributes</h3>
<p>const <code>Handle</code>&lt; <code>OneFactorCopula</code> &gt; <code>copula_</code> </p>
<p> Size <code>nBuckets_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class CDOEngine&gt; class QuantLib::InhomogeneousPoolCDOEngine&lt; CDOEngine &gt;</h3>
<p><code>CDO</code> engine, loss disctribution bucketing for finite inhomogeneous pool. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
