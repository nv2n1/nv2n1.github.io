---
title: "quantlib_twofactormodel_shortratetree(3)"
name: "quantlib_twofactormodel_shortratetree"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_twofactormodel_shortratetree/"
description: "QuantLib::TwoFactorModel::ShortRateTree – Recombining two-dimensional tree discretizing the state variable."
---

<p>QuantLib::TwoFactorModel::ShortRateTree &#8211; Recombining two-dimensional tree discretizing the state variable. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/twofactormodel.hpp&gt; </p>
<p> Inherits <code>TreeLattice2D&lt; TwoFactorModel::ShortRateTree, TrinomialTree &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ShortRateTree</code> (const boost::shared_ptr&lt; <code>TrinomialTree</code> &gt; &amp;tree1, const boost::shared_ptr&lt; <code>TrinomialTree</code> &gt; &amp;tree2, const boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; &amp;dynamics)<br />
 <i>Plain tree build-up from short-rate dynamics. </i><br />
 <code>DiscountFactor</code> <code>discount</code> (Size i, Size index) const </p>
<h2>Detailed Description</h2>
<p>Recombining two-dimensional tree discretizing the state variable. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
