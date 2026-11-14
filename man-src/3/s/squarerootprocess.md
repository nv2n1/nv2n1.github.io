---
title: "squarerootprocess(3)"
name: "squarerootprocess"
section: "3"
letter: "s"
url: "/docs/linux/man/3-squarerootprocess/"
description: "QuantLib::SquareRootProcess – Square-root process class."
---

<p>QuantLib::SquareRootProcess &#8211; Square-root process class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/squarerootprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess1D</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SquareRootProcess</code> (Real b, Real a, <code>Volatility</code> sigma, Real x0=0.0, const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;d=boost::shared_ptr&lt; <code>discretization</code> &gt;(new <code>EulerDiscretization</code>)) </p>
<p> <code>StochasticProcess interface</code> </p>
<p> Real <code>x0</code> () const<br />
 <i>returns the initial value of the state variable </i><br />
 Real <code>drift</code> (Time t, Real x) const<br />
 <i>returns the drift part of the equation, i.e. $ mu(t, x_t) $ </i><br />
 Real <code>diffusion</code> (Time t, Real x) const<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, x_t) $ </i></p>
<h2>Detailed Description</h2>
<p>Square-root process class. </p>
<p> This class describes a square-root process governed by [ dx = a (b &#8211; x_t) dt + igma qrt{x_t} dW_t. ] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
