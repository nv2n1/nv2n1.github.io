---
title: "setcovarparam(3)"
name: "setcovarparam"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setcovarparam/"
description: "QuantLib::LiborForwardModelProcess – libor-forward-model process"
---

<p>QuantLib::LiborForwardModelProcess &#8211; libor-forward-model process </p>
<h2>Synopsis</h2>
<pre><code>LiborForwardModelProcess(Size size, const boost::shared_ptr&lt;IborIndex&gt; &amp;index)

    Disposable&lt;Array&gt; initialValues() const

    returns the initial values of the state variables

    Disposable&lt;Array&gt; drift(Time t, const Array &amp;x) const

    returns the drift part of the equation,
    i.e., $ mu(t, mathrm{x} _t) $

    Disposable&lt;Matrix&gt; diffusion(Time t, const Array &amp;x) const

    returns the diffusion part of the equation,
    i.e.$ igma(t, mathrm{x} _t) $

    Disposable&lt;Matrix&gt; covariance(Time t0, const Array &amp;x0, Time dt) const

    Disposable&lt;Array&gt; apply(const Array &amp;x0, const Array &amp;dx) const

    Disposable&lt;Array&gt; evolve(Time t0, const Array &amp;x0, Time dt, const Array &amp;dw) const

    Size size() const

    returns the number of dimensions of the stochastic process

    Size factors() const

    returns the number of independent factors of the process

    boost::shared_ptr&lt;IborIndex&gt; index() const

    Leg cashFlows(Real amount = 1.0) const

    void setCovarParam(const boost::shared_ptr&lt;LfmCovarianceParameterization&gt; &amp;param)

        boost::shared_ptr&lt;LfmCovarianceParameterization&gt; covarParam() const

    Size nextIndexReset(Time t) const

    const std::vector&lt;Time&gt; &amp;fixingTimes() const

    const std::vector&lt;Date&gt; &amp;fixingDates() const

    const std::vector&lt;Time&gt; &amp;accrualStartTimes() const

    const std::vector&lt;Time&gt; &amp;accrualEndTimes() const

    std::vector&lt;DiscountFactor&gt; discountBond(const std::vector&lt;Rate&gt; &amp;rates) const</code></pre>
<p> Inherits <code>QuantLib::StochasticProcess</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LiborForwardModelProcess(Size size, const boost::shared_ptr&lt;IborIndex&gt; &amp;index)

    Disposable&lt;Array&gt; initialValues() const

    returns the initial values of the state variables

    Disposable&lt;Array&gt; drift(Time t, const Array &amp;x) const

    returns the drift part of the equation,
    i.e., $ mu(t, mathrm{x} _t) $

    Disposable&lt;Matrix&gt; diffusion(Time t, const Array &amp;x) const

    returns the diffusion part of the equation,
    i.e.$ igma(t, mathrm{x} _t) $

    Disposable&lt;Matrix&gt; covariance(Time t0, const Array &amp;x0, Time dt) const

    Disposable&lt;Array&gt; apply(const Array &amp;x0, const Array &amp;dx) const

    Disposable&lt;Array&gt; evolve(Time t0, const Array &amp;x0, Time dt, const Array &amp;dw) const

    Size size() const

    returns the number of dimensions of the stochastic process

    Size factors() const

    returns the number of independent factors of the process

    boost::shared_ptr&lt;IborIndex&gt; index() const

    Leg cashFlows(Real amount = 1.0) const

    void setCovarParam(const boost::shared_ptr&lt;LfmCovarianceParameterization&gt; &amp;param)

        boost::shared_ptr&lt;LfmCovarianceParameterization&gt; covarParam() const

    Size nextIndexReset(Time t) const

    const std::vector&lt;Time&gt; &amp;fixingTimes() const

    const std::vector&lt;Date&gt; &amp;fixingDates() const

    const std::vector&lt;Time&gt; &amp;accrualStartTimes() const

    const std::vector&lt;Time&gt; &amp;accrualEndTimes() const

    std::vector&lt;DiscountFactor&gt; discountBond(const std::vector&lt;Rate&gt; &amp;rates) const</code></pre>
<h2>Detailed Description</h2>
<p>libor-forward-model process </p>
<p> stochastic process of a libor forward model using the rolling forward measure incl. predictor-corrector step </p>
<p> References: </p>
<p> Glasserman, Paul, 2004, Monte Carlo Methods in Financial Engineering, Springer, Section 3.7 </p>
<p> Antoon Pelsser, 2000, Efficient Methods for Valuing Interest Rate Derivatives, Springer, 8 </p>
<p> Hull, John, White, Alan, 1999, <code>Forward</code> Rate Volatilities, <code>Swap</code> Rate Volatilities and the Implementation of the <code>Libor</code> Market Model (&lt;<a rel="nofollow" href="http://www.rotman.utoronto.ca/~amackay/fin/libormktmodel2.pdf">http://www.rotman.utoronto.ca/~amackay/fin/libormktmodel2.pdf</a>&gt;) </p>
<p> <code>Tests</code></p>
<dl>
<dd>the correctness is tested by Monte-Carlo reproduction of caplet &amp; ratchet NPVs and comparison with Black pricing.</dl>
<p> <code>Warning</code></p>
<dl>
<dd>this class does not work correctly with Visual C++ 6.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Disposable</code>&lt;<code>Matrix</code>&gt; covariance (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p>returns the covariance $ V(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; apply (const <code>Array</code> &amp; x0, const <code>Array</code> &amp; dx) const [virtual]</h3>
<p>applies a change to the asset value. By default, it returns $ mathrm{x} + Delta mathrm{x} $. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; evolve (Time t0, const <code>Array</code> &amp; x0, Time dt, const <code>Array</code> &amp; dw) const [virtual]</h3>
<p>returns the asset value after a time interval $ Delta t $ according to the given discretization. By default, it returns [ E(mathrm{x}_0,t_0,Delta t) + S(mathrm{x}_0,t_0,Delta t) dot Delta mathrm{w} ] where $ E $ is the expectation and $ S $ the standard deviation. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
