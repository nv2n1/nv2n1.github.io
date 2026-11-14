---
title: "shortratetree(3)"
name: "shortratetree"
section: "3"
letter: "s"
url: "/docs/linux/man/3-shortratetree/"
description: "QuantLib::OneFactorModel::ShortRateTree – Recombining trinomial tree discretizing the state variable."
---

<p>QuantLib::OneFactorModel::ShortRateTree &#8211; Recombining trinomial tree discretizing the state variable. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodel.hpp&gt; </p>
<p> Inherits <code>TreeLattice1D&lt; OneFactorModel::ShortRateTree &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ShortRateTree</code> (const boost::shared_ptr&lt; <code>TrinomialTree</code> &gt; &amp;tree, const boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; &amp;dynamics, const <code>TimeGrid</code> &amp;timeGrid)<br />
 <i>Plain tree build-up from short-rate dynamics. </i><br />
 <code>ShortRateTree</code> (const boost::shared_ptr&lt; <code>TrinomialTree</code> &gt; &amp;tree, const boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; &amp;dynamics, const boost::shared_ptr&lt; TermStructureFittingParameter::NumericalImpl &gt; &amp;phi, const <code>TimeGrid</code> &amp;timeGrid)<br />
 <i></i><code>Tree</code> build-up + numerical fitting to term-structure.<br />
 Size <code>size</code> (Size i) const </p>
<p> <code>DiscountFactor</code> <code>discount</code> (Size i, Size index) const </p>
<p> <code>Real</code> <code>underlying</code> (Size i, Size index) const </p>
<p> Size <code>descendant</code> (Size i, Size index, Size branch) const </p>
<p> <code>Real</code> <code>probability</code> (Size i, Size index, Size branch) const </p>
<h2>Detailed Description</h2>
<p>Recombining trinomial tree discretizing the state variable. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
