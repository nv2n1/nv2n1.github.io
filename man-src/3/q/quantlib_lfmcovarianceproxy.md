---
title: "quantlib_lfmcovarianceproxy(3)"
name: "quantlib_lfmcovarianceproxy"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lfmcovarianceproxy/"
description: "QuantLib::LfmCovarianceProxy – proxy for a libor forward model covariance parameterization"
---

<p>QuantLib::LfmCovarianceProxy &#8211; proxy for a libor forward model covariance parameterization </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lfmcovarproxy.hpp&gt; </p>
<p> Inherits <code>QuantLib::LfmCovarianceParameterization</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LfmCovarianceProxy</code> (const boost::shared_ptr&lt; <code>LmVolatilityModel</code> &gt; &amp;volaModel, const boost::shared_ptr&lt; <code>LmCorrelationModel</code> &gt; &amp;corrModel) </p>
<p> boost::shared_ptr&lt; <code>LmVolatilityModel</code> &gt; <code>volatilityModel</code> () const </p>
<p> boost::shared_ptr&lt; <code>LmCorrelationModel</code> &gt; <code>correlationModel</code> () const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> virtual <code>Real</code> <code>integratedCovariance</code> (Size i, Size j, Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<h3>Protected Attributes</h3>
<p>const boost::shared_ptr&lt; <code>LmVolatilityModel</code> &gt; <code>volaModel_</code> </p>
<p> const boost::shared_ptr&lt; <code>LmCorrelationModel</code> &gt; <code>corrModel_</code> </p>
<h3>Friends</h3>
<p>class <code>Var_Helper</code> </p>
<h2>Detailed Description</h2>
<p>proxy for a libor forward model covariance parameterization </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
