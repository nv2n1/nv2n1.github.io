---
title: "quantlib_liborforwardmodel(3)"
name: "quantlib_liborforwardmodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_liborforwardmodel/"
description: "QuantLib::LiborForwardModel – Libor forward model"
---

<p>QuantLib::LiborForwardModel &#8211; Libor forward model </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/liborforwardmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::CalibratedModel</code>, and <code>QuantLib::AffineModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LiborForwardModel</code> (const boost::shared_ptr&lt; <code>LiborForwardModelProcess</code> &gt; &amp;process, const boost::shared_ptr&lt; <code>LmVolatilityModel</code> &gt; &amp;volaModel, const boost::shared_ptr&lt; <code>LmCorrelationModel</code> &gt; &amp;corrModel) </p>
<p> <code>Rate</code> <code>S_0</code> (Size alpha, Size beta) const </p>
<p> virtual boost::shared_ptr&lt; <code>SwaptionVolatilityMatrix</code> &gt; <code>getSwaptionVolatilityMatrix</code> () const </p>
<p> <code>DiscountFactor</code> <code>discount</code> (Time t) const<br />
 <i>Implied discount curve. </i><br />
 Real <code>discountBond</code> (Time now, Time maturity, <code>Array</code> factors) const </p>
<p> Real <code>discountBondOption</code> (Option::Type type, Real strike, Time maturity, Time bondMaturity) const </p>
<p> void <code>setParams</code> (const <code>Array</code> &amp;params) </p>
<h3>Protected Member Functions</h3>
<p><code>Disposable</code>&lt; <code>Array</code> &gt; <code>w_0</code> (Size alpha, Size beta) const </p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; Real &gt; <code>f_</code> </p>
<p> std::vector&lt; Time &gt; <code>accrualPeriod_</code> </p>
<p> const boost::shared_ptr&lt; <code>LfmCovarianceProxy</code> &gt; <code>covarProxy_</code> </p>
<p> const boost::shared_ptr&lt; <code>LiborForwardModelProcess</code> &gt; <code>process_</code> </p>
<p> boost::shared_ptr&lt; <code>SwaptionVolatilityMatrix</code> &gt; <code>swaptionVola</code> </p>
<h2>Detailed Description</h2>
<p>Libor forward model </p>
<p> References: </p>
<p> Stefan Weber, 2005, Efficient Calibration for <code>Libor</code> Market Models, (&lt;<a rel="nofollow" href="http://workshop.mathfinance.de/2005/papers/weber/slides.pdf">http://workshop.mathfinance.de/2005/papers/weber/slides.pdf</a>&gt;) </p>
<p> Damiano Brigo, Fabio Mercurio, Massimo Morini, 2003, Different Covariance Parameterizations of <code>Libor</code> Market Model and Joint Caps/Swaptions Calibration, (&lt;<a rel="nofollow" href="http://www.business.uts.edu.au/qfrc/conferences/qmf2001/Brigo_D.pdf">http://www.business.uts.edu.au/qfrc/conferences/qmf2001/Brigo_D.pdf</a>&gt; </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness is tested using Monte-Carlo Simulation to reproduce swaption npvs, model calibration and exact cap pricing</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
