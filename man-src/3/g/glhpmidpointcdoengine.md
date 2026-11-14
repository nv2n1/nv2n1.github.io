---
title: "glhpmidpointcdoengine(3)"
name: "glhpmidpointcdoengine"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glhpmidpointcdoengine/"
description: "ql/experimental/credit/syntheticcdoengines.hpp – Pricing engines for the Synthetic CDO instrument."
---

<p>ql/experimental/credit/syntheticcdoengines.hpp &#8211; Pricing engines for the Synthetic CDO instrument. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/syntheticcdo.hpp&gt;<br />
 #include &lt;ql/experimental/credit/randomdefaultmodel.hpp&gt;<br />
 #include &lt;ql/math/distributions/normaldistribution.hpp&gt;<br />
 #include &lt;ql/math/distributions/bivariatenormaldistribution.hpp&gt; </p>
<h3>Classes</h3>
<p>class <code>engine</code><br />
 <i></i><code>CDO</code> base <code>engine</code>.<br />
 class <code>MidPointCDOEngine</code><br />
 <i></i><code>CDO</code> base engine taking schedule steps.<br />
 class <code>IntegralCDOEngine</code><br />
 <i></i><code>CDO</code> base engine taking (possibly) small time steps.<br />
 class <code>MonteCarloCDOEngine1</code><br />
 <i></i><code>CDO</code> engine, Monte Carlo for the exptected tranche loss distribution.<br />
 class <code>MonteCarloCDOEngine2</code><br />
 <i></i><code>CDO</code> engine, Monte Carlo for the sample payoff.<br />
 class <code>HomogeneousPoolCDOEngine&lt; CDOEngine &gt;</code><br />
 <i></i><code>CDO</code> engine, loss distribution convolution for finite homogeneous pool.<br />
 class <code>InhomogeneousPoolCDOEngine&lt; CDOEngine &gt;</code><br />
 <i></i><code>CDO</code> engine, loss disctribution bucketing for finite inhomogeneous pool.<br />
 class <code>GaussianLHPCDOEngine&lt; CDOEngine &gt;</code> </p>
<h3>Typedefs</h3>
<p>typedef HomogeneousPoolCDOEngine&lt; MidPointCDOEngine &gt; <code>HPMidPointCDOEngine</code> </p>
<p> typedef HomogeneousPoolCDOEngine&lt; IntegralCDOEngine &gt; <code>HPIntegralCDOEngine</code> </p>
<p> typedef InhomogeneousPoolCDOEngine&lt; MidPointCDOEngine &gt; <code>IHPMidPointCDOEngine</code> </p>
<p> typedef InhomogeneousPoolCDOEngine&lt; IntegralCDOEngine &gt; <code>IHPIntegralCDOEngine</code> </p>
<p> typedef GaussianLHPCDOEngine&lt; MidPointCDOEngine &gt; <code>GLHPMidPointCDOEngine</code> </p>
<p> typedef GaussianLHPCDOEngine&lt; IntegralCDOEngine &gt; <code>GLHPIntegralCDOEngine</code> </p>
<h2>Detailed Description</h2>
<p>Pricing engines for the Synthetic CDO instrument. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>Add further engines for analytical expected tranche loss cases &#8211; large homogeneous pool with Normal Inverse Gaussian, Gamma copula</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
