---
title: "path_type(3)"
name: "path_type"
section: "3"
letter: "p"
url: "/docs/linux/man/3-path_type/"
---

QuantLib::SingleVariate - default Monte Carlo traits for single-variate models 

<h2>Synopsis</h2>

<pre><code>enum { allowsErrorEstimate =  RNG::allowsErrorEstimate }



typedef RNG rng_traits



typedef Path path_type



typedef PathPricer&lt; path_type &gt; path_pricer_type



typedef RNG::rsg_type rsg_type



typedef PathGenerator&lt; rsg_type &gt; path_generator_type</code></pre>

<h3>Public Types</h3>

<pre><code>enum { allowsErrorEstimate =  RNG::allowsErrorEstimate }



typedef RNG rng_traits



typedef Path path_type



typedef PathPricer&lt; path_type &gt; path_pricer_type



typedef RNG::rsg_type rsg_type



typedef PathGenerator&lt; rsg_type &gt; path_generator_type</code></pre>

<h2>Detailed Description</h2>

<h3>template&lt;class RNG = PseudoRandom&gt; struct QuantLib::SingleVariate&lt; RNG &gt;</h3>

default Monte Carlo traits for single-variate models

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
