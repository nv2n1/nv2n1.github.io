---
title: "checkmoments(3)"
name: "checkmoments"
section: "3"
letter: "c"
url: "/docs/linux/man/3-checkmoments/"
description: "QuantLib::OneFactorCopula – Abstract base class for one-factor copula models."
---

<p>QuantLib::OneFactorCopula &#8211; Abstract base class for one-factor copula models. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/onefactorcopula.hpp&gt; </p>
<p> Inherits <code>QuantLib::LazyObject</code>. </p>
<p> Inherited by <code>OneFactorGaussianCopula</code>, <code>OneFactorGaussianStudentCopula</code>, <code>OneFactorStudentCopula</code>, and <code>OneFactorStudentGaussianCopula</code>. </p>
<h3>Public Member Functions</h3>
<p><code>OneFactorCopula</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;correlation, Real maximum=5, Size integrationSteps=50) </p>
<p> virtual Real <code>density</code> (Real m) const =0<br />
 <i>Density function of M. </i><br />
 virtual Real <code>cumulativeZ</code> (Real z) const =0<br />
 <i>Cumulative distribution of Z. </i><br />
 virtual Real <code>cumulativeY</code> (Real y) const<br />
 <i>Cumulative distribution of Y. </i><br />
 virtual Real <code>inverseCumulativeY</code> (Real p) const<br />
 <i>Inverse cumulative distribution of Y. </i><br />
 Real <code>correlation</code> () const<br />
 <i>Single correlation parameter. </i><br />
 Real <code>conditionalProbability</code> (Real prob, Real m) const<br />
 <i>Conditional probability. </i><br />
 std::vector&lt; Real &gt; <code>conditionalProbability</code> (const std::vector&lt; Real &gt; &amp;prob, Real m) const<br />
 <i>Vector of conditional probabilities. </i><br />
 Real <code>integral</code> (Real p) const </p>
<p> template&lt;class F &gt; Real <code>integral</code> (const F &amp;f, std::vector&lt; Real &gt; &amp;probabilities) const </p>
<p> template&lt;class F &gt; Distribution <code>integral</code> (const F &amp;f, const std::vector&lt; Real &gt; &amp;nominals, const std::vector&lt; Real &gt; &amp;probabilities) const </p>
<p> int <code>checkMoments</code> (Real tolerance) const </p>
<h3>Protected Attributes</h3>
<p><code>Handle</code>&lt; <code>Quote</code> &gt; <code>correlation_</code> </p>
<p> Real <code>max_</code> </p>
<p> Size <code>steps_</code> </p>
<p> std::vector&lt; Real &gt; <code>y_</code> </p>
<p> std::vector&lt; Real &gt; <code>cumulativeY_</code> </p>
<h2>Detailed Description</h2>
<p>Abstract base class for one-factor copula models. </p>
<p> Reference: John Hull and Alan White, The Perfect Copula, June 2006 </p>
<p> Let $Q_i(t)$ be the cumulative probability of default of counterparty i before time t. </p>
<p> In a one-factor model, consider random variables [ Y_i = a_i,M+qrt{1-a_i^2}:Z_i ] where $M$ and $Z_i$ have independent zero-mean unit-variance distributions and $-1</p>
<hr>
<p>lation between $Y_i$ and $Y_j$ is then $a_i a_j$. </p>
<p> Let $F_Y(y)$ be the cumulative distribution function of $Y_i$. $y$ is mapped to $t$ such that percentiles match, i.e. $F_Y(y)=Q_i(t)$ or $y=F_Y^{-1}(Q_i(t))$. </p>
<p> Now let $F_Z(z)$ be the cumulated distribution function of $Z_i$. For given realization of $M$, this determines the distribution of $y$: [ Prob ,(Y_i &lt; y|M) = F_Z </p>
<hr>
<p> specified in derived classes. The distribution function of $ Y $ is then given by the convolution [ F_Y(y) = Prob,(Y&lt;y) = int_{-infty}^infty,int_{-infty}^{infty}: D_Z(z),D_M(m) quad Theta </p>
<hr>
<p>ta (x) = </p>
<hr>
<p>re $ D_Z(z) $ and $ D_M(m) $ are the probability densities of $ Z$ and $ M, $ respectively. </p>
<p> This convolution can also be written [ F(y) = Prob ,(Y &lt; y) = int_{-infty}^infty D_M(m),dm: int_{-infty}^{g(y,a,m)} D_Z(z),dz, qquad g(y,a,m) = ac{y &#8211; adot m}{qrt{1-a^2}}, qquad a &lt; 1 ]</p>
<p> or </p>
<p> [ F(y) = Prob ,(Y &lt; y) = int_{-infty}^infty D_Z(z),dz: int_{-infty}^{h(y,a,z)} D_M(m),dm, qquad h(y,a,z) = ac{y &#8211; qrt{1 &#8211; a^2}dot z}{a}, qquad a &gt; 0. ].PPIn general, $ F_Y(y) $ needs to be computed numerically. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>Improve on simple Euler integration</dl>
<h2>Member Function Documentation</h2>
<h3>virtual Real density (Real m) const [pure virtual]</h3>
<p>Density function of M. </p>
<p> Derived classes must override this method and ensure zero mean and unit variance. </p>
<p> Implemented in <code>OneFactorGaussianCopula</code>, <code>OneFactorStudentCopula</code>, <code>OneFactorGaussianStudentCopula</code>, and <code>OneFactorStudentGaussianCopula</code>.</p>
<h3>virtual Real cumulativeZ (Real z) const [pure virtual]</h3>
<p>Cumulative distribution of Z. </p>
<p> Derived classes must override this method and ensure zero mean and unit variance. </p>
<p> Implemented in <code>OneFactorGaussianCopula</code>, <code>OneFactorStudentCopula</code>, <code>OneFactorGaussianStudentCopula</code>, and <code>OneFactorStudentGaussianCopula</code>.</p>
<h3>virtual Real cumulativeY (Real y) const [virtual]</h3>
<p>Cumulative distribution of Y. </p>
<p> This is the default implementation based on tabulated data. The table needs to be filled by derived classes. If analytic calculation is feasible, this method can also be overridden. </p>
<p> Reimplemented in <code>OneFactorGaussianCopula</code>.</p>
<h3>virtual Real inverseCumulativeY (Real p) const [virtual]</h3>
<p>Inverse cumulative distribution of Y. </p>
<p> This is the default implementation based on tabulated data. The table needs to be filled by derived classes. If analytic calculation is feasible, this method can also be overridden. </p>
<p> Reimplemented in <code>OneFactorGaussianCopula</code>.</p>
<h3>Real conditionalProbability (Real prob, Real m) const</h3>
<p>Conditional probability. </p>
<p> [ l&gt; conditionalProbability (const std::vector&lt; Real &gt; &amp; prob, Real m) const&quot; </p>
<p> Vector of conditional probabilities. </p>
<p> [ l integral (Real p) const&quot; </p>
<p> Integral over the density $ ho(m) $ of M and the conditional probability related to p: </p>
<p> [ int_{-infty}^infty,dm,ho(m), F_Z </p>
<hr>
<p>al integral (const F &amp; f, std::vector&lt; Real &gt; &amp; probabilities) const&quot; </p>
<p> Integral over the density $ ho(m) $ of M and a one-dimensional function $ f $ of conditional probabilities related to the input vector of probabilities p: </p>
<p> [ int_{-infty}^infty,dm,ho(m), f (ls, const std::vector&lt; Real &gt; &amp; probabilities) const&quot; </p>
<p> Integral over the density $ ho(m) $ of M and a multi-dimensional function $ f $ of conditional probabilities related to the input vector of probabilities p: </p>
<p> [ int_{-infty}^infty,dm,ho(m), f (n and unit variance) of the distributions of M, Z, and Y by numerically integrating the respective density. <code>Parameter</code> tolerance is the maximum tolerable absolute error. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
