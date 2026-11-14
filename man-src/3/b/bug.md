---
title: "bug(3)"
name: "bug"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bug/"
description: "bug – Known Bugs"
---

<h2 class="name">NAME</h2>
<p> bug &#8211; Known Bugs<br />
&nbsp;<wbr></p>
<dl>
<dt><code>Class AssetSwap</code></p>
<dd> fair prices are not calculated correctly when using indexed coupons.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackCalculator</code></p>
<dd> When the variance is null, division by zero occur during the calculation of delta, delta forward, gamma, gamma forward, rho, dividend rho, vega, and strike sensitivity.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CapHelper</code></p>
<dd> This helper does not register with the passed IBOR index and with the evaluation date. Furthermore, the ATM strike rate is not recalculated when any of its observables change.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CompoundForward</code></p>
<dd> swap rates are not reproduced exactly when using indexed coupons. Apparently, some assumption about the swap fixings is hard-coded into the bootstrapping algorithm.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CoxIngersollRoss</code></p>
<dd> this class was not tested enough to guarantee its functionality.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ExtendedCoxIngersollRoss</code></p>
<dd> this class was not tested enough to guarantee its functionality.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class G2</code></p>
<dd> This class was not tested enough to guarantee its functionality.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class HullWhite</code></p>
<dd> When the term structure is relinked, the r0 parameter of the underlying Vasicek model is not updated.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class HybridHestonHullWhiteProcess</code></p>
<dd> This class was not tested enough to guarantee its functionality&#8230; work in progress</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class LocalVolSurface</code></p>
<dd> this class is untested, probably unreliable.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MultiCubicSpline&lt; i &gt;</code></p>
<dd> cannot interpolate at the grid points on the boundary surface of the N-dimensional region</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SwaptionHelper</code></p>
<dd> This helper does not register with the passed IBOR index and with the evaluation date. Furthermore, the ATM exercise rate is not recalculated when any of its observables change.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member FDDividendAmericanEngine</code></p>
<dd> results are not overly reliable.</dl>
<p> method impliedVolatility() utterly fails </p>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member FDDividendShoutEngine</code></p>
<dd> results are not overly reliable.</dl>
<hr>
<h2>Index</h2>
