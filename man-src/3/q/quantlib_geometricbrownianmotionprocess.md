---
title: "quantlib_geometricbrownianmotionprocess(3)"
name: "quantlib_geometricbrownianmotionprocess"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_geometricbrownianmotionprocess/"
description: "QuantLib::GeometricBrownianMotionProcess – Geometric brownian-motion process."
---

<p>QuantLib::GeometricBrownianMotionProcess &#8211; Geometric brownian-motion process. </p>
<h2>Synopsis</h2>
<p> #include &lt;ql/processes/geometricbrownianprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess1D</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>GeometricBrownianMotionProcess</code> (double initialValue, double mue, double sigma) </p>
<p> Real <code>x0</code> () const<br />
 <i>returns the initial value of the state variable </i><br />
 Real <code>drift</code> (Time t, Real x) const<br />
 <i>returns the drift part of the equation, i.e. $ mu(t, x_t) $ </i><br />
 Real <code>diffusion</code> (Time t, Real x) const<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, x_t) $ </i></p>
<h3>Protected Attributes</h3>
<p> double <code>initialValue_</code> </p>
<p> double <code>mue_</code> </p>
<p> double <code>sigma_</code> </p>
<h2>Detailed Description</h2>
<p> Geometric brownian-motion process. </p>
<p> This class describes the stochastic process governed by [ dS(t, S)= mu S dt + igma S dW_t. ] </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code.</p>
