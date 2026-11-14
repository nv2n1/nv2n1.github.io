---
title: "shortrateendcriteria_(3)"
name: "shortrateendcriteria_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-shortrateendcriteria_/"
description: "QuantLib::CalibratedModel – Calibrated model class."
---

<p>QuantLib::CalibratedModel &#8211; Calibrated model class. </p>
<h2>Synopsis</h2>
<pre><code>CalibratedModel (Size nArguments)



void update ()



void calibrate (const std::vector&lt; boost::shared_ptr&lt; CalibrationHelper &gt; &gt; &amp;, OptimizationMethod &amp;method, const EndCriteria &amp;endCriteria, const Constraint &amp;constraint=Constraint(), const std::vector&lt; Real &gt; &amp;weights=std::vector&lt; Real &gt;())


Calibrate to a set of market instruments (caps/swaptions).


Real value (const Array &amp;params, const std::vector&lt; boost::shared_ptr&lt; CalibrationHelper &gt; &gt; &amp;)



const boost::shared_ptr&lt; Constraint &gt; &amp; constraint () const



EndCriteria::Type endCriteria ()


returns end criteria result


Disposable&lt; Array &gt; params () const


Returns array of arguments on which calibration is done.


virtual void setParams (const Array &amp;params)



Protected Member Functions</code></pre>
<p> Inherits <code>QuantLib::Observer</code>, and <code>QuantLib::Observable</code>. Inherited by <code>GJRGARCHModel</code>, <code>HestonModel</code>, <code>LiborForwardModel</code>, and <code>ShortRateModel</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>CalibratedModel (Size nArguments)



void update ()



void calibrate (const std::vector&lt; boost::shared_ptr&lt; CalibrationHelper &gt; &gt; &amp;, OptimizationMethod &amp;method, const EndCriteria &amp;endCriteria, const Constraint &amp;constraint=Constraint(), const std::vector&lt; Real &gt; &amp;weights=std::vector&lt; Real &gt;())


Calibrate to a set of market instruments (caps/swaptions).


Real value (const Array &amp;params, const std::vector&lt; boost::shared_ptr&lt; CalibrationHelper &gt; &gt; &amp;)



const boost::shared_ptr&lt; Constraint &gt; &amp; constraint () const



EndCriteria::Type endCriteria ()


returns end criteria result


Disposable&lt; Array &gt; params () const


Returns array of arguments on which calibration is done.


virtual void setParams (const Array &amp;params)



Protected Member Functions</code></pre>
<p> virtual void <code>generateArguments</code> ()</p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; <code>Parameter</code> &gt; <code>arguments_</code> </p>
<p> boost::shared_ptr&lt; <code>Constraint</code> &gt; <code>constraint_</code> </p>
<p> EndCriteria::Type <code>shortRateEndCriteria_</code></p>
<h3>Friends</h3>
<p>class <code>CalibrationFunction</code></p>
<h2>Detailed Description</h2>
<p>Calibrated model class.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>.</p>
<h3>void calibrate (const std::vector&lt; boost::shared_ptr&lt; <code>CalibrationHelper</code> &gt; &gt; &amp;, <code>OptimizationMethod</code> &amp; method, const <code>EndCriteria</code> &amp; endCriteria, const <code>Constraint</code> &amp; constraint = <code>Constraint</code>(), const std::vector&lt; <code>Real</code> &gt; &amp; weights = std::vector&lt; <code>Real</code> &gt;())</h3>
<p>Calibrate to a set of market instruments (caps/swaptions). </p>
<p> An additional constraint can be passed which must be satisfied in addition to the constraints of the model.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
