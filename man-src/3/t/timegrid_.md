---
title: "timegrid_(3)"
name: "timegrid_"
section: "3"
letter: "t"
url: "/docs/linux/man/3-timegrid_/"
description: "QuantLib::TrinomialTree – Recombining trinomial tree class."
---

<p>QuantLib::TrinomialTree &#8211; Recombining trinomial tree class. </p>
<h2>Synopsis</h2>
<pre><code>enum Branches { branches = 3 }

Public Member Functions
TrinomialTree(const boost::shared_ptr&lt;StochasticProcess1D&gt; &amp;process, const TimeGrid &amp;timeGrid, bool isPositive = false)

    Real dx(Size i) const

    const TimeGrid &amp;timeGrid() const

    Size size(Size i) const

    Real underlying(Size i, Size index) const

    Size descendant(Size i, Size index, Size branch) const

    Real probability(Size i, Size index, Size branch) const

    Protected Attributes</code></pre>
<p> Inherits <code>Tree&lt; TrinomialTree &gt;</code>.</p>
<h3>Public Types</h3>
<pre><code>enum Branches { branches = 3 }

Public Member Functions
TrinomialTree(const boost::shared_ptr&lt;StochasticProcess1D&gt; &amp;process, const TimeGrid &amp;timeGrid, bool isPositive = false)

    Real dx(Size i) const

    const TimeGrid &amp;timeGrid() const

    Size size(Size i) const

    Real underlying(Size i, Size index) const

    Size descendant(Size i, Size index, Size branch) const

    Real probability(Size i, Size index, Size branch) const

    Protected Attributes</code></pre>
<p> std::vector&lt; Branching &gt; <code>branchings_</code> </p>
<p> <code>Real</code> <code>x0_</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>dx_</code> </p>
<p> <code>TimeGrid</code> <code>timeGrid_</code></p>
<h2>Detailed Description</h2>
<p>Recombining trinomial tree class. </p>
<p> This class defines a recombining trinomial tree approximating a 1-D stochastic process. </p>
<p> <code>Warning</code></p>
<dl>
<dd>The diffusion term of the SDE must be independent of the underlying process.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
