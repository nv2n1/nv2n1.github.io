---
title: "quantlib_singlevariate(3)"
name: "quantlib_singlevariate"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_singlevariate/"
description: "QuantLib::SingleVariate – default Monte Carlo traits for single-variate models"
---

<p>QuantLib::SingleVariate &#8211; default Monte Carlo traits for single-variate models </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/montecarlo/mctraits.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum { <code>allowsErrorEstimate</code> = RNG::allowsErrorEstimate } </p>
<p> typedef RNG <code>rng_traits</code> </p>
<p> typedef <code>Path</code> <code>path_type</code> </p>
<p> typedef <code>PathPricer</code>&lt; <code>path_type</code> &gt; <code>path_pricer_type</code> </p>
<p> typedef RNG::rsg_type <code>rsg_type</code> </p>
<p> typedef <code>PathGenerator</code>&lt; rsg_type &gt; <code>path_generator_type</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom&gt; struct QuantLib::SingleVariate&lt; RNG &gt;</h3>
<p>default Monte Carlo traits for single-variate models </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
