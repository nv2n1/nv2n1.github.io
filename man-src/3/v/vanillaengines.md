---
title: "vanillaengines(3)"
name: "vanillaengines"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vanillaengines/"
description: "Vanilla option engines –"
---

<p>Vanilla option engines &#8211;</p>
<h3>Classes</h3>
<p>class <code>FdBlackScholesVanillaEngine</code><br />
 <i>Finite-Differences Black Scholes vanilla option engine. </i><br />
 class <code>FdHestonVanillaEngine</code><br />
 <i>Finite-Differences Heston Vanilla </i><code>Option</code> engine.<br />
 class <code>AnalyticBSMHullWhiteEngine</code><br />
 <i>analytic european option pricer including stochastic interest rates </i><br />
 class <code>AnalyticDigitalAmericanEngine</code><br />
 <i>Analytic pricing engine for American vanilla options with digital payoff. </i><br />
 class <code>AnalyticDividendEuropeanEngine</code><br />
 <i>Analytic pricing engine for European options with discrete dividends. </i><br />
 class <code>AnalyticEuropeanEngine</code><br />
 <i>Pricing engine for European vanilla options using analytical formulae. </i><br />
 class <code>AnalyticGJRGARCHEngine</code><br />
 <i>GJR-GARCH(1,1) engine. </i><br />
 class <code>AnalyticHestonEngine</code><br />
 <i>analytic Heston-model engine based on Fourier transform </i><br />
 class <code>AnalyticHestonHullWhiteEngine</code><br />
 <i>Analytic Heston engine incl. stochastic interest rates. </i><br />
 class <code>BaroneAdesiWhaleyApproximationEngine</code><br />
 <i>Barone-Adesi and Whaley pricing engine for American options (1987). </i><br />
 class <code>BatesEngine</code><br />
 <i>Bates model engines based on Fourier transform. </i><br />
 class <code>BinomialVanillaEngine&lt; T &gt;</code><br />
 <i>Pricing engine for vanilla options using binomial trees. </i><br />
 class <code>BjerksundStenslandApproximationEngine</code><br />
 <i>Bjerksund and Stensland pricing engine for American options (1993). </i><br />
 class <code>FDBermudanEngine</code><br />
 <i>Finite-differences Bermudan engine. </i><br />
 class <code>FDDividendEngineMerton73</code><br />
 <i>Finite-differences pricing engine for dividend options using. </i><br />
 class <code>FDDividendEngineShiftScale</code><br />
 <i>Finite-differences engine for dividend options using shifted dividends. </i><br />
 class <code>FDEuropeanEngine</code><br />
 <i>Pricing engine for European options using finite-differences. </i><br />
 class <code>FDStepConditionEngine</code><br />
 <i>Finite-differences pricing engine for American-style vanilla options. </i><br />
 class <code>FDVanillaEngine</code><br />
 <i>Finite-differences pricing engine for BSM one asset options. </i><br />
 class <code>IntegralEngine</code><br />
 <i>Pricing engine for European vanilla options using integral approach. </i><br />
 class <code>JumpDiffusionEngine</code><br />
 <i>Jump-diffusion engine for vanilla options. </i><br />
 class <code>JuQuadraticApproximationEngine</code><br />
 <i>Pricing engine for American options with Ju quadratic approximation. </i><br />
 class <code>MCAmericanEngine&lt; RNG, S &gt;</code><br />
 <i>American Monte Carlo engine. </i><br />
 class <code>MCDigitalEngine&lt; RNG, S &gt;</code><br />
 <i>Pricing engine for digital options using Monte Carlo simulation. </i><br />
 class <code>MCEuropeanEngine&lt; RNG, S &gt;</code><br />
 <i>European option pricing engine using Monte Carlo simulation. </i><br />
 class <code>MCEuropeanGJRGARCHEngine&lt; RNG, S &gt;</code><br />
 <i>Monte Carlo GJR-GARCH-model engine for European options. </i><br />
 class <code>MCEuropeanHestonEngine&lt; RNG, S &gt;</code><br />
 <i>Monte Carlo Heston-model engine for European options. </i><br />
 class <code>MCVanillaEngine&lt; MC, RNG, S, Inst &gt;</code><br />
 <i>Pricing engine for vanilla options using Monte Carlo simulation. </i></p>
<h3>Typedefs</h3>
<p>typedef FDEngineAdapter&lt; FDAmericanCondition&lt; FDStepConditionEngine &gt;, OneAssetOption::engine &gt; <code>FDAmericanEngine</code><br />
 <i>Finite-differences pricing engine for American one asset options. </i><br />
 typedef FDEngineAdapter&lt; FDAmericanCondition&lt; FDDividendEngine &gt;, DividendVanillaOption::engine &gt; <code>FDDividendAmericanEngine</code><br />
 <i>Finite-differences pricing engine for dividend American options. </i><br />
 typedef FDEngineAdapter&lt; FDDividendEngine, DividendVanillaOption::engine &gt; <code>FDDividendEuropeanEngine</code><br />
 <i>Finite-differences pricing engine for dividend European options. </i><br />
 typedef FDEngineAdapter&lt; FDShoutCondition&lt; FDDividendEngine &gt;, DividendVanillaOption::engine &gt; <code>FDDividendShoutEngine</code><br />
 <i>Finite-differences shout engine with dividends. </i><br />
 typedef FDEngineAdapter&lt; FDShoutCondition&lt; FDStepConditionEngine &gt;, VanillaOption::engine &gt; <code>FDShoutEngine</code><br />
 <i>Finite-differences pricing engine for shout vanilla options. </i></p>
<h2>Detailed Description</h2>
<h2>Typedef Documentation</h2>
<h3>typedef FDEngineAdapter&lt;FDAmericanCondition&lt;FDStepConditionEngine&gt;, OneAssetOption::engine&gt; FDAmericanEngine</h3>
<p>Finite-differences pricing engine for American one asset options. </p>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dl>
</dl>
<p> <code>Examples: </code> <code>EquityOption.cpp</code>.</p>
<h3>typedef FDEngineAdapter&lt;FDAmericanCondition&lt;FDDividendEngine&gt;, DividendVanillaOption::engine&gt; FDDividendAmericanEngine</h3>
<p>Finite-differences pricing engine for dividend American options. </p>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</p>
<dt>*</p>
<dd>the invariance of the results upon addition of null dividends is tested.</dl>
</dl>
<p> <code>Bug</code></p>
<dl>
<dd>results are not overly reliable. </p>
<p> method impliedVolatility() utterly fails</dl>
<h3>typedef FDEngineAdapter&lt;FDDividendEngine, DividendVanillaOption::engine&gt; FDDividendEuropeanEngine</h3>
<p>Finite-differences pricing engine for dividend European options. </p>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</p>
<dt>*</p>
<dd>the invariance of the results upon addition of null dividends is tested.</dl>
</dl>
<h3>typedef FDEngineAdapter&lt;FDShoutCondition&lt;FDDividendEngine&gt;, DividendVanillaOption::engine&gt; FDDividendShoutEngine</h3>
<p>Finite-differences shout engine with dividends. </p>
<p> <code>Bug</code></p>
<dl>
<dd>results are not overly reliable.</dl>
<h3>typedef FDEngineAdapter&lt;FDShoutCondition&lt;FDStepConditionEngine&gt;, VanillaOption::engine&gt; FDShoutEngine</h3>
<p>Finite-differences pricing engine for shout vanilla options. </p>
<p> <code>Tests</code></p>
<dl>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
