---
title: "calibratedmodel(3)"
name: "calibratedmodel"
section: "3"
letter: "c"
url: "/docs/linux/man/3-calibratedmodel/"
description: "QuantLib::CalibratedModel – Calibrated model class."
---

<p>QuantLib::CalibratedModel &#8211; Calibrated model class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/model.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observer</code>, and <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>GJRGARCHModel</code>, <code>HestonModel</code>, <code>LiborForwardModel</code>, and <code>ShortRateModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CalibratedModel</code> (Size nArguments) </p>
<p> void <code>update</code> () </p>
<p> void <code>calibrate</code> (const std::vector&lt; boost::shared_ptr&lt; <code>CalibrationHelper</code> &gt; &gt; &amp;, <code>OptimizationMethod</code> &amp;method, const <code>EndCriteria</code> &amp;endCriteria, const <code>Constraint</code> &amp;constraint=<code>Constraint</code>(), const std::vector&lt; <code>Real</code> &gt; &amp;weights=std::vector&lt; <code>Real</code> &gt;())<br />
 <i>Calibrate to a set of market instruments (caps/swaptions). </i><br />
 <code>Real</code> <code>value</code> (const <code>Array</code> &amp;params, const std::vector&lt; boost::shared_ptr&lt; <code>CalibrationHelper</code> &gt; &gt; &amp;) </p>
<p> const boost::shared_ptr&lt; <code>Constraint</code> &gt; &amp; <code>constraint</code> () const </p>
<p> EndCriteria::Type <code>endCriteria</code> ()<br />
 <i>returns end criteria result </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>params</code> () const<br />
 <i>Returns array of arguments on which calibration is done. </i><br />
 virtual void <code>setParams</code> (const <code>Array</code> &amp;params) </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>generateArguments</code> () </p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; <code>Parameter</code> &gt; <code>arguments_</code> </p>
<p> boost::shared_ptr&lt; <code>Constraint</code> &gt; <code>constraint_</code> </p>
<p> EndCriteria::Type <code>shortRateEndCriteria_</code> </p>
<h3>Friends</h3>
<p>class <code>CalibrationFunction</code> </p>
<h2>Detailed Description</h2>
<p>Calibrated model class.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>.</p>
<h3>void calibrate (const std::vector&lt; boost::shared_ptr&lt; <code>CalibrationHelper</code> &gt; &gt; &amp;, <code>OptimizationMethod</code> &amp; method, const <code>EndCriteria</code> &amp; endCriteria, const <code>Constraint</code> &amp; constraint = <code>Constraint</code>(), const std::vector&lt; <code>Real</code> &gt; &amp; weights = std::vector&lt; <code>Real</code> &gt;())</h3>
<p>Calibrate to a set of market instruments (caps/swaptions). </p>
<p> An additional constraint can be passed which must be satisfied in addition to the constraints of the model. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
