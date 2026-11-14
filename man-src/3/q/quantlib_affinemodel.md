---
title: "quantlib_affinemodel(3)"
name: "quantlib_affinemodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_affinemodel/"
description: "QuantLib::AffineModel – Affine model class."
---

<p>QuantLib::AffineModel &#8211; Affine model class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/model.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>G2</code>, <code>LiborForwardModel</code>, and <code>OneFactorAffineModel</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>DiscountFactor</code> <code>discount</code> (Time t) const =0<br />
 <i>Implied discount curve. </i><br />
 virtual Real <code>discountBond</code> (Time now, Time maturity, <code>Array</code> factors) const =0 </p>
<p> virtual Real <code>discountBondOption</code> (Option::Type type, Real strike, Time maturity, Time bondMaturity) const =0 </p>
<h2>Detailed Description</h2>
<p>Affine model class. </p>
<p> Base class for analytically tractable models. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
