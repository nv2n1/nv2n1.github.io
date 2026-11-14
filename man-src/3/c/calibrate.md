---
title: "calibrate(3)"
name: "calibrate"
section: "3"
letter: "c"
url: "/docs/linux/man/3-calibrate/"
description: "QuantLib::LongstaffSchwartzPathPricer – Longstaff-Schwarz path pricer for early exercise options."
---

<h2 class="name">NAME</h2>
<p> QuantLib::LongstaffSchwartzPathPricer &#8211; Longstaff-Schwarz path pricer for early exercise options. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/methods/montecarlo/longstaffschwartzpathpricer.hpp&gt; </p>
<p> Inherits <code>PathPricer&lt; PathType &gt;</code>. </p>
<h3>Public Types</h3>
<p> typedef EarlyExerciseTraits&lt; PathType &gt;::StateType <code>StateType</code> </p>
<h3>Public Member Functions</h3>
<p> <code>LongstaffSchwartzPathPricer</code> (const <code>TimeGrid</code> &amp;times, const boost::shared_ptr&lt; <code>EarlyExercisePathPricer</code>&lt; PathType &gt; &gt; &amp;, const boost::shared_ptr&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure) </p>
<p> <code>Real</code> <code>operator()</code> (const PathType &amp;path) const </p>
<p> virtual void <code>calibrate</code> () </p>
<h3>Protected Attributes</h3>
<p> bool <code>calibrationPhase_</code> </p>
<p> const boost::shared_ptr&lt; <code>EarlyExercisePathPricer</code>&lt; PathType &gt; &gt; <code>pathPricer_</code> </p>
<p> boost::scoped_array&lt; <code>Array</code> &gt; <code>coeff_</code> </p>
<p> boost::scoped_array&lt; <code>DiscountFactor</code> &gt; <code>dF_</code> </p>
<p> std::vector&lt; PathType &gt; <code>paths_</code> </p>
<p> const std::vector&lt; boost::function1&lt; <code>Real</code>, StateType &gt; &gt; <code>v_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class PathType&gt; class QuantLib::LongstaffSchwartzPathPricer&lt; PathType &gt;</h3>
<p> Longstaff-Schwarz path pricer for early exercise options. </p>
<p> References: </p>
<p> Francis Longstaff, Eduardo Schwartz, 2001. Valuing American Options by Simulation: A Simple Least-Squares Approach, The Review of Financial Studies, Volume 14, No. 1, 113-147 </p>
<p> <code>Tests</code></p>
<dl>
<dt>
<dd> the correctness of the returned value is tested by reproducing results available in web/literature</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
