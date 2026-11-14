---
title: "quantlib_g2_fittingparameter(3)"
name: "quantlib_g2_fittingparameter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_g2_fittingparameter/"
description: "QuantLib::G2::FittingParameter – Analytical term-structure fitting parameter $ te/twofactormodels/g2.hpp>"
---

<p>QuantLib::G2::FittingParameter &#8211; Analytical term-structure fitting parameter $ te/twofactormodels/g2.hpp&gt; </p>
<p> Inherits <code>QuantLib::TermStructureFittingParameter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>FittingParameter</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, <code>Real</code> a, <code>Real</code> sigma, <code>Real</code> b, <code>Real</code> eta, <code>Real</code> rho) </p>
<h2>Detailed Description</h2>
<p>Analytical term-structure fitting parameter $ lytically defined by [ c{1}{2}(ac{igma(1-e^{-at})}{a})^2 + ac{1}{2}(ac{	a(1-e^{-bt})}{b})^2 + hoac{igma(1-e^{-at})}{a}ac{	a(1-e^{-bt})}{b}, ] where $ f(t) $ is the instantaneous forward rate at $ t $. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
