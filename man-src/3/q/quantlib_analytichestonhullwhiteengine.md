---
title: "quantlib_analytichestonhullwhiteengine(3)"
name: "quantlib_analytichestonhullwhiteengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analytichestonhullwhiteengine/"
description: "QuantLib::AnalyticHestonHullWhiteEngine – Analytic Heston engine incl. stochastic interest rates."
---

<p>QuantLib::AnalyticHestonHullWhiteEngine &#8211; Analytic Heston engine incl. stochastic interest rates. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/analytichestonhullwhiteengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::AnalyticHestonEngine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticHestonHullWhiteEngine</code> (const boost::shared_ptr&lt; <code>HestonModel</code> &gt; &amp;hestonModel, const boost::shared_ptr&lt; <code>HullWhite</code> &gt; &amp;hullWhiteModel, Size integrationOrder=144) </p>
<p> <code>AnalyticHestonHullWhiteEngine</code> (const boost::shared_ptr&lt; <code>HestonModel</code> &gt; &amp;model, const boost::shared_ptr&lt; <code>HullWhite</code> &gt; &amp;hullWhiteModel, Real relTolerance, Size maxEvaluations) </p>
<p> void <code>update</code> () </p>
<p> void <code>calculate</code> () const </p>
<h3>Protected Member Functions</h3>
<p>std::complex&lt; Real &gt; <code>addOnTerm</code> (Real phi, Time t, Size j) const </p>
<h2>Detailed Description</h2>
<p>Analytic Heston engine incl. stochastic interest rates. </p>
<p> This class is pricing a european options under the following processes </p>
<p> [ ta &#8211; v) dt + igma qrt{v} dW_2 \ dr(t) &amp;=&amp; ( heta(t) &#8211; a r) dt + 	a dW_3 \ dW_1 dW_2 &amp;=&amp; ho dt \ dW_1 dW_3 &amp;=&amp; 0 \ dW_2 dW_3 &amp;=&amp; 0 \ 
d{array} ].PP References: </p>
<p> Karel in&#8217;t Hout, Joris Bierkens, Antoine von der Ploeg, Joe in&#8217;t Panhuis, A Semi closed-from analytic pricing formula for call options in a hybrid Heston-Hull-White Model. </p>
<p> A. Sepp, Pricing European-Style Options under Jump Diffusion Processes with Stochastic Volatility: Applications of Fourier Transform (&lt;<a rel="nofollow" href="http://math.ut.ee/~spartak/papers/stochjumpvols.pdf">http://math.ut.ee/~spartak/papers/stochjumpvols.pdf</a>&gt;) </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature, testing against QuantLib&#8217;s analytic Heston and Black-Scholes-Merton Hull-White engine</dl>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>GenericEngine&lt; VanillaOption::arguments, VanillaOption::results &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
