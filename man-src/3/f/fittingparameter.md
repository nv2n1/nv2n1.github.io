---
title: "fittingparameter(3)"
name: "fittingparameter"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fittingparameter/"
description: "QuantLib::ExtendedCoxIngersollRoss::FittingParameter – Analytical term-structure fitting parameter $ te/onefactormodels/extendedcoxingersollross.hpp>"
---

<p>QuantLib::ExtendedCoxIngersollRoss::FittingParameter &#8211; Analytical term-structure fitting parameter $ te/onefactormodels/extendedcoxingersollross.hpp&gt; </p>
<p> Inherits <code>QuantLib::TermStructureFittingParameter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>FittingParameter</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, <code>Real</code> theta, <code>Real</code> k, <code>Real</code> sigma, <code>Real</code> x0) </p>
<h2>Detailed Description</h2>
<p>Analytical term-structure fitting parameter $ lytically defined by [ c{2k heta(e^{th}-1)}{2h+(k+h)(e^{th}-1)} &#8211; ac{4 x_0 h^2 e^{th}}{(2h+(k+h)(e^{th}-1))^1}, ] where $ f(t) $ is the instantaneous forward rate at $ t $ and $ h = qrt{k^2 + 2igma^2} $. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
