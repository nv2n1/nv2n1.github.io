---
title: "shorttermvolatility(3)"
name: "shorttermvolatility"
section: "3"
letter: "s"
url: "/docs/linux/man/3-shorttermvolatility/"
description: "QuantLib::AbcdFunction – Abcd functional form for instantaneous volatility"
---

<p>QuantLib::AbcdFunction &#8211; Abcd functional form for instantaneous volatility </p>
<h2>Synopsis</h2>
<pre><code>AbcdFunction (Real a=-0.06, Real b=0.17, Real c=0.54, Real d=0.17)



Real operator() (Time u) const


volatility function value at time u: [ f(u) ]


Real maximumLocation () const


time at which the volatility function reaches maximum (if any)


Real maximumVolatility () const


maximum value of the volatility function


Real shortTermVolatility () const


volatility function value at time 0: [ f(0) ]


Real longTermVolatility () const


volatility function value at time +inf: [ f(inf) ]


Real covariance (Time t, Time T, Time S) const



Real covariance (Time t1, Time t2, Time T, Time S) const



Real volatility (Time T, Time tMax, Time tMin) const



Real variance (Time T, Time tMax, Time tMin) const



Real instantaneousVolatility (Time t, Time T) const



Real instantaneousVariance (Time t, Time T) const



Real instantaneousCovariance (Time u, Time T, Time S) const



Real primitive (Time t, Time T, Time S) const



Real a () const



Real b () const



Real c () const



Real d () const</code></pre>
<p> Inherits std::unary_function&lt;Real, Real&gt;.</p>
<h3>Public Member Functions</h3>
<pre><code>AbcdFunction (Real a=-0.06, Real b=0.17, Real c=0.54, Real d=0.17)



Real operator() (Time u) const


volatility function value at time u: [ f(u) ]


Real maximumLocation () const


time at which the volatility function reaches maximum (if any)


Real maximumVolatility () const


maximum value of the volatility function


Real shortTermVolatility () const


volatility function value at time 0: [ f(0) ]


Real longTermVolatility () const


volatility function value at time +inf: [ f(inf) ]


Real covariance (Time t, Time T, Time S) const



Real covariance (Time t1, Time t2, Time T, Time S) const



Real volatility (Time T, Time tMax, Time tMin) const



Real variance (Time T, Time tMax, Time tMin) const



Real instantaneousVolatility (Time t, Time T) const



Real instantaneousVariance (Time t, Time T) const



Real instantaneousCovariance (Time u, Time T, Time S) const



Real primitive (Time t, Time T, Time S) const



Real a () const



Real b () const



Real c () const



Real d () const</code></pre>
<h2>Detailed Description</h2>
<p>Abcd functional form for instantaneous volatility </p>
<p> [ f(T-t) = [ a + b(T-t) ] e^{-c(T-t)} + d ] following Rebonato&#8217;s notation.</p>
<h2>Member Function Documentation</h2>
<h3><code>Real</code> covariance (<code>Time</code> t, <code>Time</code> T, <code>Time</code> S) const</h3>
<p>instantaneous covariance function at time t between T-fixing and S-fixing rates [ f(T-t)f(S-t) ]</p>
<h3><code>Real</code> covariance (<code>Time</code> t1, <code>Time</code> t2, <code>Time</code> T, <code>Time</code> S) const</h3>
<p>integral of the instantaneous covariance function between time t1 and t2 for T-fixing and S-fixing rates [ int_{t1}^{t2} f(T-t)f(S-t)dt ]</p>
<h3><code>Real</code> volatility (<code>Time</code> T, <code>Time</code> tMax, <code>Time</code> tMin) const</h3>
<p>average volatility in [tMin,tMax] of T-fixing rate: [ qrt{ int_{tMin}^{tMax} f^2(T-u)du }]</p>
<h3><code>Real</code> variance (<code>Time</code> T, <code>Time</code> tMax, <code>Time</code> tMin) const</h3>
<p>variance between tMin and tMax of T-fixing rate: [ int_{tMin}^{tMax} f^2(T-u)du ]</p>
<h3><code>Real</code> instantaneousVolatility (<code>Time</code> t, <code>Time</code> T) const</h3>
<p>instantaneous volatility at time t of the T-fixing rate: [ f(T-t) ]</p>
<h3><code>Real</code> instantaneousVariance (<code>Time</code> t, <code>Time</code> T) const</h3>
<p>instantaneous variance at time t of T-fixing rate: [ f(T-t)f(T-t) ]</p>
<h3><code>Real</code> instantaneousCovariance (<code>Time</code> u, <code>Time</code> T, <code>Time</code> S) const</h3>
<p>instantaneous covariance at time t between T and S fixing rates: [ f(T-u)f(S-u) ]</p>
<h3><code>Real</code> primitive (<code>Time</code> t, <code>Time</code> T, <code>Time</code> S) const</h3>
<p>indefinite integral of the instantaneous covariance function at time t between T-fixing and S-fixing rates [ int f(T-t)f(S-t)dt ]</p>
<h3><code>Real</code> a () const</h3>
<p>Inspectors</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
