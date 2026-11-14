---
title: "quantlib_endeulerdiscretization(3)"
name: "quantlib_endeulerdiscretization"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_endeulerdiscretization/"
description: "QuantLib::EndEulerDiscretization – Euler end-point discretization for stochastic processes."
---

<p>QuantLib::EndEulerDiscretization &#8211; Euler end-point discretization for stochastic processes. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/endeulerdiscretization.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess::discretization</code>, and <code>QuantLib::StochasticProcess1D::discretization</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Disposable</code>&lt; <code>Array</code> &gt; <code>drift</code> (const <code>StochasticProcess</code> &amp;, Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> Real <code>drift</code> (const <code>StochasticProcess1D</code> &amp;, Time t0, Real x0, Time dt) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (const <code>StochasticProcess</code> &amp;, Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> Real <code>diffusion</code> (const <code>StochasticProcess1D</code> &amp;, Time t0, Real x0, Time dt) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> (const <code>StochasticProcess</code> &amp;, Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> Real <code>variance</code> (const <code>StochasticProcess1D</code> &amp;, Time t0, Real x0, Time dt) const </p>
<h2>Detailed Description</h2>
<p>Euler end-point discretization for stochastic processes. </p>
<h2>Member Function Documentation</h2>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; drift (const <code>StochasticProcess</code> &amp;, Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p>Returns an approximation of the drift defined as $ mu(t_0 + Delta t, mathbf{x}_0) Delta t $. </p>
<p> Implements <code>discretization</code>.</p>
<h3>Real drift (const <code>StochasticProcess1D</code> &amp;, Time t0, Real x0, Time dt) const [virtual]</h3>
<p>Returns an approximation of the drift defined as $ mu(t_0 + Delta t, x_0) Delta t $. </p>
<p> Implements <code>discretization</code>.</p>
<h3><code>Disposable</code>&lt;<code>Matrix</code>&gt; diffusion (const <code>StochasticProcess</code> &amp;, Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p>Returns an approximation of the diffusion defined as $ igma(t_0 + Delta t, mathbf{x}_0) qrt{Delta t} $. </p>
<p> Implements <code>discretization</code>.</p>
<h3>Real diffusion (const <code>StochasticProcess1D</code> &amp;, Time t0, Real x0, Time dt) const [virtual]</h3>
<p>Returns an approximation of the diffusion defined as $ igma(t_0 + Delta t, x_0) qrt{Delta t} $. </p>
<p> Implements <code>discretization</code>.</p>
<h3><code>Disposable</code>&lt;<code>Matrix</code>&gt; covariance (const <code>StochasticProcess</code> &amp;, Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p>Returns an approximation of the covariance defined as $ igma(t_0 + Delta t, mathbf{x}_0)^2 Delta t $. </p>
<p> Implements <code>discretization</code>.</p>
<h3>Real variance (const <code>StochasticProcess1D</code> &amp;, Time t0, Real x0, Time dt) const [virtual]</h3>
<p>Returns an approximation of the variance defined as $ igma(t_0 + Delta t, x_0)^2 Delta t $. </p>
<p> Implements <code>discretization</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
