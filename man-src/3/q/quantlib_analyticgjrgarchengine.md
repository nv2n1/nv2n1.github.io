---
title: "quantlib_analyticgjrgarchengine(3)"
name: "quantlib_analyticgjrgarchengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analyticgjrgarchengine/"
description: "QuantLib::AnalyticGJRGARCHEngine – GJR-GARCH(1,1) engine."
---

<p>QuantLib::AnalyticGJRGARCHEngine &#8211; GJR-GARCH(1,1) engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/analyticgjrgarchengine.hpp&gt; </p>
<p> Inherits <code>GenericModelEngine&lt; GJRGARCHModel, VanillaOption::arguments, VanillaOption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticGJRGARCHEngine</code> (const boost::shared_ptr&lt; <code>GJRGARCHModel</code> &gt; &amp;model) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>GJR-GARCH(1,1) engine. </p>
<p> References: </p>
<p> Jin-Chuan Duan, Genevieve Gauthier, Jean-Guy Simonato, Caroline Sasseville, 2006. Approximating the GJR-GARCH and EGARCH option pricing models analytically Journal of Computational Finance, Volume 9, Number 3, Spring 2006 </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in the Duan et al&#8217;s 2006 paper.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
