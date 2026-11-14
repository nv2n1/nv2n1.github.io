---
title: "maxiterations_(3)"
name: "maxiterations_"
section: "3"
letter: "m"
url: "/docs/linux/man/3-maxiterations_/"
description: "QuantLib::EndCriteria – Criteria to end optimization process:."
---

<p>QuantLib::EndCriteria &#8211; Criteria to end optimization process:. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/endcriteria.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>None</code>, <code>MaxIterations</code>, <code>StationaryPoint</code>, <code>StationaryFunctionValue</code>, <code>StationaryFunctionAccuracy</code>, <code>ZeroGradientNorm</code>, <code>Unknown</code> } </p>
<h3>Public Member Functions</h3>
<p><code>EndCriteria</code> (Size maxIterations, Size maxStationaryStateIterations, <code>Real</code> rootEpsilon, <code>Real</code> functionEpsilon, <code>Real</code> gradientNormEpsilon)<br />
 <i>Initialization constructor. </i><br />
 Size <code>maxIterations</code> () const </p>
<p> Size <code>maxStationaryStateIterations</code> () const </p>
<p> <code>Real</code> <code>rootEpsilon</code> () const </p>
<p> <code>Real</code> <code>functionEpsilon</code> () const </p>
<p> <code>Real</code> <code>gradientNormEpsilon</code> () const </p>
<p> bool <code>operator()</code> (const Size iteration, Size &amp;statState, const bool positiveOptimization, const <code>Real</code> fold, const <code>Real</code> normgold, const <code>Real</code> fnew, const <code>Real</code> normgnew, EndCriteria::Type &amp;ecType) const </p>
<p> bool <code>checkMaxIterations</code> (const Size iteration, EndCriteria::Type &amp;ecType) const </p>
<p> bool <code>checkStationaryPoint</code> (const <code>Real</code> xOld, const <code>Real</code> xNew, Size &amp;statStateIterations, EndCriteria::Type &amp;ecType) const </p>
<p> bool <code>checkStationaryFunctionValue</code> (const <code>Real</code> fxOld, const <code>Real</code> fxNew, Size &amp;statStateIterations, EndCriteria::Type &amp;ecType) const </p>
<p> bool <code>checkStationaryFunctionAccuracy</code> (const <code>Real</code> f, const bool positiveOptimization, EndCriteria::Type &amp;ecType) const </p>
<p> bool <code>checkZeroGradientNorm</code> (const <code>Real</code> gNorm, EndCriteria::Type &amp;ecType) const </p>
<h3>Protected Attributes</h3>
<p>Size <code>maxIterations_</code><br />
 <i>Maximum number of iterations. </i><br />
 Size <code>maxStationaryStateIterations_</code><br />
 <i>Maximun number of iterations in stationary state. </i><br />
 <code>Real</code> <code>rootEpsilon_</code><br />
 <i>root, function and gradient epsilons </i><br />
 <code>Real</code> <code>functionEpsilon_</code> </p>
<p> <code>Real</code> <code>gradientNormEpsilon_</code> </p>
<h2>Detailed Description</h2>
<p>Criteria to end optimization process:. </p>
<dl COMPACT>
<dt>*</p>
<dd>maximum number of iterations AND minimum number of iterations around stationary point</p>
<dt> *</p>
<dd>x (independent variable) stationary point</p>
<dt> *</p>
<dd>y=f(x) (dependent variable) stationary point</p>
<dt> *</p>
<dd>stationary gradient</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>bool operator() (const Size iteration, Size &amp; statState, const bool positiveOptimization, const <code>Real</code> fold, const <code>Real</code> normgold, const <code>Real</code> fnew, const <code>Real</code> normgnew, EndCriteria::Type &amp; ecType) const</h3>
<p>Test if the number of iterations is not too big and if a minimum point is not reached</p>
<h3>bool checkMaxIterations (const Size iteration, EndCriteria::Type &amp; ecType) const</h3>
<p>Test if the number of iteration is below MaxIterations</p>
<h3>bool checkStationaryPoint (const <code>Real</code> xOld, const <code>Real</code> xNew, Size &amp; statStateIterations, EndCriteria::Type &amp; ecType) const</h3>
<p>Test if the root variation is below rootEpsilon</p>
<h3>bool checkStationaryFunctionValue (const <code>Real</code> fxOld, const <code>Real</code> fxNew, Size &amp; statStateIterations, EndCriteria::Type &amp; ecType) const</h3>
<p>Test if the function variation is below functionEpsilon</p>
<h3>bool checkStationaryFunctionAccuracy (const <code>Real</code> f, const bool positiveOptimization, EndCriteria::Type &amp; ecType) const</h3>
<p>Test if the function value is below functionEpsilon</p>
<h3>bool checkZeroGradientNorm (const <code>Real</code> gNorm, EndCriteria::Type &amp; ecType) const</h3>
<p>Test if the gradient norm variation is below gradientNormEpsilon </p>
<p> Test if the gradient norm value is below gradientNormEpsilon </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
