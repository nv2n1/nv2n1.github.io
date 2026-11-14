---
title: "numberofevaluations(3)"
name: "numberofevaluations"
section: "3"
letter: "n"
url: "/docs/linux/man/3-numberofevaluations/"
description: "QuantLib::AnalyticHestonEngine – analytic Heston-model engine based on Fourier transform"
---

<p>QuantLib::AnalyticHestonEngine &#8211; analytic Heston-model engine based on Fourier transform </p>
<h2>Synopsis</h2>
<pre><code>AnalyticHestonEngine (const boost::shared_ptr&lt; HestonModel &gt; &amp;model, Real relTolerance, Size maxEvaluations)



AnalyticHestonEngine (const boost::shared_ptr&lt; HestonModel &gt; &amp;model, Size integrationOrder=144)



AnalyticHestonEngine (const boost::shared_ptr&lt; HestonModel &gt; &amp;model, ComplexLogFormula cpxLog, const Integration &amp;itg)



void calculate () const



Size numberOfEvaluations () const



Static Public Member Functions
static void doCalculation (Real riskFreeDiscount, Real dividendDiscount, Real spotPrice, Real strikePrice, Real term, Real kappa, Real theta, Real sigma, Real v0, Real rho, const TypePayoff &amp;type, const Integration &amp;integration, const ComplexLogFormula cpxLog, const AnalyticHestonEngine *const enginePtr, Real &amp;value, Size &amp;evaluations)



Protected Member Functions</code></pre>
<p> Inherits <code>GenericModelEngine&lt; HestonModel, VanillaOption::arguments, VanillaOption::results &gt;</code>. Inherited by <code>AnalyticHestonHullWhiteEngine</code>, BatesDoubleExpEngine, and <code>BatesEngine</code>.</p>
<h3>Public Types</h3>
<p>enum <code>ComplexLogFormula</code> { <code>Gatheral</code>, <code>BranchCorrection</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>AnalyticHestonEngine (const boost::shared_ptr&lt; HestonModel &gt; &amp;model, Real relTolerance, Size maxEvaluations)



AnalyticHestonEngine (const boost::shared_ptr&lt; HestonModel &gt; &amp;model, Size integrationOrder=144)



AnalyticHestonEngine (const boost::shared_ptr&lt; HestonModel &gt; &amp;model, ComplexLogFormula cpxLog, const Integration &amp;itg)



void calculate () const



Size numberOfEvaluations () const



Static Public Member Functions
static void doCalculation (Real riskFreeDiscount, Real dividendDiscount, Real spotPrice, Real strikePrice, Real term, Real kappa, Real theta, Real sigma, Real v0, Real rho, const TypePayoff &amp;type, const Integration &amp;integration, const ComplexLogFormula cpxLog, const AnalyticHestonEngine *const enginePtr, Real &amp;value, Size &amp;evaluations)



Protected Member Functions</code></pre>
<p> virtual std::complex&lt; Real &gt; <code>addOnTerm</code> (Real phi, Time t, Size j) const</p>
<h2>Detailed Description</h2>
<p>analytic Heston-model engine based on Fourier transform </p>
<p> Integration detail: Two algebraically equivalent formulations of the complex logarithm of the Heston model exist. Gatherals [2005] (also Duffie, Pan and <code>Singleton</code> [2000], and Schoutens, Simons and Tistaert[2004]) version does not cause discoutinuities whereas the original version (e.g. Heston [1993]) needs some sort of &#8216;branch correction&#8217; to work properly. Gatheral&#8217;s version does also work with adaptive integration routines and should be preferred over the original Heston version. </p>
<p> References: </p>
<p> Heston, Steven L., 1993. A Closed-Form Solution for Options with Stochastic Volatility with Applications to <code>Bond</code> and <code>Currency</code> Options. The review of Financial Studies, Volume 6, Issue 2, 327-343. </p>
<p> A. Sepp, Pricing European-Style Options under Jump Diffusion Processes with Stochastic Volatility: Applications of Fourier Transform (&lt;<a rel="nofollow" href="http://math.ut.ee/~spartak/papers/stochjumpvols.pdf">http://math.ut.ee/~spartak/papers/stochjumpvols.pdf</a>&gt;) </p>
<p> R. Lord and C. Kahl, Why the rotation count algorithm works, <a rel="nofollow" href="http://papers.ssrn.com/sol3/papers.cfm?abstract_id=921335">http://papers.ssrn.com/sol3/papers.cfm?abstract_id=921335</a> </p>
<p> H. Albrecher, P. Mayer, W.Schoutens and J. Tistaert, The Little Heston Trap, <a rel="nofollow" href="http://www.schoutens.be/HestonTrap.pdf">http://www.schoutens.be/HestonTrap.pdf</a> </p>
<p> J. Gatheral, The Volatility <code>Surface</code>: A Practitioner&#8217;s Guide, Wiley Finance </p>
<p> <code>Tests</code></p>
<dl>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature and comparison with Black pricing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
