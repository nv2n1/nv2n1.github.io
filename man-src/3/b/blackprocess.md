---
title: "blackprocess(3)"
name: "blackprocess"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackprocess/"
description: "QuantLib::BlackProcess – Black (1976) stochastic process."
---

<p>QuantLib::BlackProcess &#8211; Black (1976) stochastic process. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/blackscholesprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::GeneralizedBlackScholesProcess</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BlackProcess</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;x0, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeTS, const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;blackVolTS, const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;d=boost::shared_ptr&lt; <code>discretization</code> &gt;(new <code>EulerDiscretization</code>)) </p>
<h2>Detailed Description</h2>
<p>Black (1976) stochastic process. </p>
<p> This class describes the stochastic process for a forward or futures contract given by [ dS(t, S) = ac{igma(t, S)^2}{2} dt + igma dW_t. ] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
