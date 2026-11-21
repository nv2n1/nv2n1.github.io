---

title: "bug(3)"
name: "bug"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bug/"
description: "bug – Known Bugs"
---

<p> bug &#8211; Known Bugs<br />
&nbsp;<wbr></p>
<dl>
<dt><code>Class AssetSwap</code></dt>
<dd> fair prices are not calculated correctly when using indexed coupons.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackCalculator</code></dt>
<dd> When the variance is null, division by zero occur during the calculation of delta, delta forward, gamma, gamma forward, rho, dividend rho, vega, and strike sensitivity.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CapHelper</code></dt>
<dd> This helper does not register with the passed IBOR index and with the evaluation date. Furthermore, the ATM strike rate is not recalculated when any of its observables change.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CompoundForward</code></dt>
<dd> swap rates are not reproduced exactly when using indexed coupons. Apparently, some assumption about the swap fixings is hard-coded into the bootstrapping algorithm.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CoxIngersollRoss</code></dt>
<dd> this class was not tested enough to guarantee its functionality.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ExtendedCoxIngersollRoss</code></dt>
<dd> this class was not tested enough to guarantee its functionality.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class G2</code></dt>
<dd> This class was not tested enough to guarantee its functionality.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class HullWhite</code></dt>
<dd> When the term structure is relinked, the r0 parameter of the underlying Vasicek model is not updated.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class HybridHestonHullWhiteProcess</code></dt>
<dd> This class was not tested enough to guarantee its functionality&#8230; work in progress</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class LocalVolSurface</code></dt>
<dd> this class is untested, probably unreliable.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MultiCubicSpline&lt; i &gt;</code></dt>
<dd> cannot interpolate at the grid points on the boundary surface of the N-dimensional region</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SwaptionHelper</code></dt>
<dd> This helper does not register with the passed IBOR index and with the evaluation date. Furthermore, the ATM exercise rate is not recalculated when any of its observables change.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member FDDividendAmericanEngine</code></dt>
<dd> results are not overly reliable.</dd></dl>
<p> method impliedVolatility() utterly fails </p>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member FDDividendShoutEngine</code></dt>
<dd> results are not overly reliable.</dd></dl>
<hr>
