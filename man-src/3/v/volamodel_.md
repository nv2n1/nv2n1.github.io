---
title: "volamodel_(3)"
name: "volamodel_"
section: "3"
letter: "v"
url: "/docs/linux/man/3-volamodel_/"
description: "QuantLib::LfmCovarianceProxy – proxy for a libor forward model covariance parameterization"
---

<p>QuantLib::LfmCovarianceProxy &#8211; proxy for a libor forward model covariance parameterization </p>
<h2>Synopsis</h2>
<pre><code>LfmCovarianceProxy (const boost::shared_ptr&lt; LmVolatilityModel &gt; &amp;volaModel, const boost::shared_ptr&lt; LmCorrelationModel &gt; &amp;corrModel)



boost::shared_ptr&lt; LmVolatilityModel &gt; volatilityModel () const



boost::shared_ptr&lt; LmCorrelationModel &gt; correlationModel () const



Disposable&lt; Matrix &gt; diffusion (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Disposable&lt; Matrix &gt; covariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



virtual Real integratedCovariance (Size i, Size j, Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Protected Attributes
const boost::shared_ptr&lt; LmVolatilityModel &gt; volaModel_



const boost::shared_ptr&lt; LmCorrelationModel &gt; corrModel_



Friends</code></pre>
<p> Inherits <code>QuantLib::LfmCovarianceParameterization</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LfmCovarianceProxy (const boost::shared_ptr&lt; LmVolatilityModel &gt; &amp;volaModel, const boost::shared_ptr&lt; LmCorrelationModel &gt; &amp;corrModel)



boost::shared_ptr&lt; LmVolatilityModel &gt; volatilityModel () const



boost::shared_ptr&lt; LmCorrelationModel &gt; correlationModel () const



Disposable&lt; Matrix &gt; diffusion (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Disposable&lt; Matrix &gt; covariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



virtual Real integratedCovariance (Size i, Size j, Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Protected Attributes
const boost::shared_ptr&lt; LmVolatilityModel &gt; volaModel_



const boost::shared_ptr&lt; LmCorrelationModel &gt; corrModel_



Friends</code></pre>
<p> class <code>Var_Helper</code></p>
<h2>Detailed Description</h2>
<p>proxy for a libor forward model covariance parameterization</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
