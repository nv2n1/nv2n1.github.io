---
title: "batesengine(3)"
name: "batesengine"
section: "3"
letter: "b"
url: "/docs/linux/man/3-batesengine/"
description: "QuantLib::BatesEngine – Bates model engines based on Fourier transform."
---

<p>QuantLib::BatesEngine &#8211; Bates model engines based on Fourier transform. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/batesengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::AnalyticHestonEngine</code>. </p>
<p> Inherited by BatesDetJumpEngine. </p>
<h3>Public Member Functions</h3>
<p><code>BatesEngine</code> (const boost::shared_ptr&lt; <code>BatesModel</code> &gt; &amp;model, Size integrationOrder=144) </p>
<p> <code>BatesEngine</code> (const boost::shared_ptr&lt; <code>BatesModel</code> &gt; &amp;model, Real relTolerance, Size maxEvaluations) </p>
<h3>Protected Member Functions</h3>
<p>std::complex&lt; Real &gt; <code>addOnTerm</code> (Real phi, Time t, Size j) const </p>
<h2>Detailed Description</h2>
<p>Bates model engines based on Fourier transform. </p>
<p> this classes price european options under the following processes </p>
<p> 1. Jump-Diffusion with Stochastic Volatility </p>
<p> [ ^J &#8211; 1) S dN \ dv(t, S) &amp;=&amp; ppa ( heta &#8211; v) dt + igma qrt{v} dW_2 \ dW_1 dW_2 &amp;=&amp; ho dt 
d{array} ].PP N is a Poisson process with the intensity $ </p>
<hr>
<p> $. When a jump occurs the magnitude J has the probability distribution function $ al Jump Diffusion: <code>BatesEngine</code> </p>
<p> Logarithm of the jump size J is normally distributed [ p Diffusion: BatesDoubleExpEngine </p>
<p> The jump size has an asymmetric double exponential distribution [ terministic Jump Intensity </p>
<p> [ ^J &#8211; 1) S dN \ dv(t, S) &amp;=&amp; ppa ( heta &#8211; v) dt + igma qrt{v} dW_2 \ d</p>
<hr>
<p>(t) &amp;=&amp; ppa_</p>
<hr>
<p>( heta_</p>
<hr>
<p>&#8211;</p>
<hr>
<p>) dt \ dW_1 dW_2 &amp;=&amp; ho dt 
d{array} ].PP 2.1 Log-Normal Jump Diffusion with Deterministic Jump Intensity BatesDetJumpEngine </p>
<p> 2.2 Double-Exponential Jump Diffusion with Deterministic Jump Intensity BatesDoubleExpDetJumpEngine </p>
<p> References: </p>
<p> D. Bates, Jumps and stochastic volatilit: exchange rate processes implicit in Deutsche mark options&#8217;, Review of Financial Sudies 9, 69-107. </p>
<p> A. Sepp, Pricing European-Style Options under Jump Diffusion Processes with Stochastic Volatility: Applications of Fourier Transform (&lt;<a rel="nofollow" href="http://math.ut.ee/~spartak/papers/stochjumpvols.pdf">http://math.ut.ee/~spartak/papers/stochjumpvols.pdf</a>&gt;) </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature, testing against QuantLib&#8217;s jump diffusion engine and comparison with Black pricing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
