---
title: "gausskronrodadaptive(3)"
name: "gausskronrodadaptive"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gausskronrodadaptive/"
description: "QuantLib::GaussKronrodAdaptive – Integral of a 1-dimensional function using the Gauss-Kronrod methods."
---

<p>QuantLib::GaussKronrodAdaptive &#8211; Integral of a 1-dimensional function using the Gauss-Kronrod methods. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/integrals/kronrodintegral.hpp&gt; </p>
<p> Inherits QuantLib::Integrator. </p>
<h3>Public Member Functions</h3>
<p><code>GaussKronrodAdaptive</code> (Real tolerance, Size maxFunctionEvaluations=<code>Null</code>&lt; Size &gt;()) </p>
<h3>Protected Member Functions</h3>
<p>Real <code>integrate</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b) const </p>
<h2>Detailed Description</h2>
<p>Integral of a 1-dimensional function using the Gauss-Kronrod methods. </p>
<p> This class provide an adaptive integration procedure using 15 points Gauss-Kronrod integration rule. This is more robust in that it allows to integrate less smooth functions (though singular functions should be integrated using dedicated algorithms) but less efficient beacuse it does not reuse precedently computed points during computation steps. </p>
<p> References: </p>
<p> Gauss-Kronrod Integration &lt;<a rel="nofollow" href="http://mathcssun1.emporia.edu/~oneilcat/ExperimentApplet3/ExperimentApplet3.html">http://mathcssun1.emporia.edu/~oneilcat/ExperimentApplet3/ExperimentApplet3.html</a>&gt; </p>
<p> NMS &#8211; Numerical Analysis Library &lt;<a rel="nofollow" href="http://www.math.iastate.edu/burkardt/f_src/nms/nms.html">http://www.math.iastate.edu/burkardt/f_src/nms/nms.html</a>&gt; </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the result is tested by checking it against known good values.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
