---
title: "mcarlo(3)"
name: "mcarlo"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mcarlo/"
description: "Monte Carlo framework –"
---

<h2 class="name">NAME</h2>
<p> Monte Carlo framework &#8211; </p>
<h3>Classes</h3>
<p> class <code>BrownianBridge</code><br />
 <i>Builds Wiener process paths using Gaussian variates. </i><br />
 class <code>EarlyExercisePathPricer&lt; PathType, TimeType, ValueType &gt;</code><br />
 <i>base class for early exercise path pricers </i><br />
 class <code>LongstaffSchwartzPathPricer&lt; PathType &gt;</code><br />
 <i>Longstaff-Schwarz path pricer for early exercise options. </i><br />
 class <code>MonteCarloModel&lt; MC, RNG, S &gt;</code><br />
 <i>General-purpose Monte Carlo model for path samples. </i><br />
 class <code>MultiPath</code><br />
 <i>Correlated multiple asset paths. </i><br />
 class <code>MultiPathGenerator&lt; GSG &gt;</code><br />
 <i>Generates a multipath from a random number generator. </i><br />
 class <code>Path</code><br />
 <i>single-factor random walk </i><br />
 class <code>PathGenerator&lt; GSG &gt;</code><br />
 <i>Generates random paths using a sequence generator. </i><br />
 class <code>PathPricer&lt; PathType, ValueType &gt;</code><br />
 <i>base class for path pricers </i><br />
 struct <code>Sample&lt; T &gt;</code><br />
 <i>weighted sample </i></p>
<h2>Detailed Description</h2>
<p> This framework (corresponding to the ql/MonteCarlo directory) contains basic building blocks for Monte Carlo simulations.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
