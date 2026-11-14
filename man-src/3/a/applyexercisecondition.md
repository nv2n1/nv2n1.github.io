---
title: "applyexercisecondition(3)"
name: "applyexercisecondition"
section: "3"
letter: "a"
url: "/docs/linux/man/3-applyexercisecondition/"
description: "QuantLib::DiscretizedOption – Discretized option on a given asset."
---

<p>QuantLib::DiscretizedOption &#8211; Discretized option on a given asset. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/discretizedasset.hpp&gt; </p>
<p> Inherits <code>QuantLib::DiscretizedAsset</code>. </p>
<p> Inherited by DiscretizedSwaption. </p>
<h3>Public Member Functions</h3>
<p><code>DiscretizedOption</code> (const boost::shared_ptr&lt; <code>DiscretizedAsset</code> &gt; &amp;underlying, Exercise::Type exerciseType, const std::vector&lt; <code>Time</code> &gt; &amp;exerciseTimes) </p>
<p> void <code>reset</code> (Size size) </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>mandatoryTimes</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>postAdjustValuesImpl</code> () </p>
<p> void <code>applyExerciseCondition</code> () </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>DiscretizedAsset</code> &gt; <code>underlying_</code> </p>
<p> Exercise::Type <code>exerciseType_</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>exerciseTimes_</code> </p>
<h2>Detailed Description</h2>
<p>Discretized option on a given asset. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>it is advised that derived classes take care of creating and initializing themselves an instance of the underlying.</dl>
<h2>Member Function Documentation</h2>
<h3>void reset (Size size) [virtual]</h3>
<p>This method should initialize the asset values to an <code>Array</code> of the given size and with values depending on the particular asset. </p>
<p> Implements <code>DiscretizedAsset</code>.</p>
<h3>std::vector&lt; <code>Time</code> &gt; mandatoryTimes () const [virtual]</h3>
<p>This method returns the times at which the numerical method should stop while rolling back the asset. Typical examples include payment times, exercise times and such. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The returned values are not guaranteed to be sorted.</dl>
<p> Implements <code>DiscretizedAsset</code>.</p>
<h3>void postAdjustValuesImpl () [protected, virtual]</h3>
<p>This method performs the actual post-adjustment </p>
<p> Reimplemented from <code>DiscretizedAsset</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
