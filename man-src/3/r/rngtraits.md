---
title: "rngtraits(3)"
name: "rngtraits"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rngtraits/"
description: "ql/math/randomnumbers/rngtraits.hpp – random-number generation policies"
---

<p>ql/math/randomnumbers/rngtraits.hpp &#8211; random-number generation policies </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/methods/montecarlo/pathgenerator.hpp&gt;

#include &lt;ql/math/randomnumbers/mt19937uniformrng.hpp&gt;

#include &lt;ql/math/randomnumbers/inversecumulativerng.hpp&gt;

#include &lt;ql/math/randomnumbers/randomsequencegenerator.hpp&gt;

#include &lt;ql/math/randomnumbers/sobolrsg.hpp&gt;

#include &lt;ql/math/randomnumbers/inversecumulativersg.hpp&gt;

#include &lt;ql/math/distributions/normaldistribution.hpp&gt;

#include &lt;ql/math/distributions/poissondistribution.hpp&gt;</code></pre>
<h3>Typedefs</h3>
<p>typedef GenericPseudoRandom&lt; MersenneTwisterUniformRng, InverseCumulativeNormal &gt; <code>PseudoRandom</code><br />
 <i>default traits for pseudo-random number generation </i><br />
 typedef GenericPseudoRandom&lt; MersenneTwisterUniformRng, InverseCumulativePoisson &gt; <code>PoissonPseudoRandom</code><br />
 <i>traits for Poisson-distributed pseudo-random number generation </i><br />
 typedef GenericLowDiscrepancy&lt; SobolRsg, InverseCumulativeNormal &gt; <code>LowDiscrepancy</code><br />
 <i>default traits for low-discrepancy sequence generation </i></p>
<h2>Detailed Description</h2>
<p>random-number generation policies</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
