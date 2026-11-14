---
title: "partialrollback(3)"
name: "partialrollback"
section: "3"
letter: "p"
url: "/docs/linux/man/3-partialrollback/"
description: "QuantLib::DiscretizedAsset – Discretized asset class used by numerical methods."
---

<p>QuantLib::DiscretizedAsset &#8211; Discretized asset class used by numerical methods. </p>
<h2>Synopsis</h2>
<pre><code>virtual void reset (Size size)=0



void preAdjustValues ()



void postAdjustValues ()



void adjustValues ()



virtual std::vector&lt; Time &gt; mandatoryTimes () const =0



Protected Member Functions</code></pre>
<p> Inherited by DiscretizedCallableFixedRateBond, DiscretizedCapFloor, DiscretizedConvertible, <code>DiscretizedDiscountBond</code>, <code>DiscretizedOption</code>, DiscretizedSwap, and DiscretizedVanillaOption.</p>
<h3>Public Member Functions</h3>
<p><code>inspectors</code> </p>
<p> Time <code>time</code> () const </p>
<p> Time &amp; <code>time</code> () </p>
<p> const <code>Array</code> &amp; <code>values</code> () const </p>
<p> <code>Array</code> &amp; <code>values</code> () </p>
<p> const boost::shared_ptr&lt; <code>Lattice</code> &gt; &amp; <code>method</code> () const<br />
 <code>High-level interface</code><br />
 Users of discretized assets should use these methods in order to initialize, evolve and take the present value of the assets. They call the corresponding methods in the <code>Lattice</code> interface, to which we refer for documentation. virtual void reset (Size size)=0</p>
<p>void preAdjustValues ()</p>
<p>void postAdjustValues ()</p>
<p>void adjustValues ()</p>
<p>virtual std::vector&lt; Time &gt; mandatoryTimes () const =0</p>
<p>Protected Member Functions <code>Low-level interface</code><br />
 These methods (that developers should override when deriving from <code>DiscretizedAsset</code>) are to be used by numerical methods and not directly by users, with the exception of <code>adjustValues()</code>, <code>preAdjustValues()</code> and <code>postAdjustValues()</code> that can be used together with partialRollback(). </p>
<pre><code>virtual void reset (Size size)=0



void preAdjustValues ()



void postAdjustValues ()



void adjustValues ()



virtual std::vector&lt; Time &gt; mandatoryTimes () const =0



Protected Member Functions</code></pre>
<p> bool <code>isOnTime</code> (Time t) const </p>
<p> virtual void <code>preAdjustValuesImpl</code> () </p>
<p> virtual void <code>postAdjustValuesImpl</code> ()</p>
<h3>Protected Attributes</h3>
<p>Time <code>time_</code> </p>
<p> Time <code>latestPreAdjustment_</code> </p>
<p> Time <code>latestPostAdjustment_</code> </p>
<p> <code>Array</code> <code>values_</code></p>
<h2>Detailed Description</h2>
<p>Discretized asset class used by numerical methods.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void reset (Size size) [pure virtual]</h3>
<p>This method should initialize the asset values to an <code>Array</code> of the given size and with values depending on the particular asset. </p>
<p> Implemented in <code>DiscretizedDiscountBond</code>, and <code>DiscretizedOption</code>.</p>
<h3>void preAdjustValues ()</h3>
<p>This method will be invoked after rollback and before any other asset (i.e., an option on this one) has any chance to look at the values. For instance, payments happening at times already spanned by the rollback will be added here. </p>
<p> This method is not virtual; derived classes must override the protected <code>preAdjustValuesImpl()</code> method instead.</p>
<h3>void postAdjustValues ()</h3>
<p>This method will be invoked after rollback and after any other asset had their chance to look at the values. For instance, payments happening at the present time (and therefore not included in an option to be exercised at this time) will be added here. </p>
<p> This method is not virtual; derived classes must override the protected <code>postAdjustValuesImpl()</code> method instead.</p>
<h3>void adjustValues ()</h3>
<p>This method performs both pre- and post-adjustment</p>
<h3>virtual std::vector&lt;Time&gt; mandatoryTimes () const [pure virtual]</h3>
<p>This method returns the times at which the numerical method should stop while rolling back the asset. Typical examples include payment times, exercise times and such. </p>
<p> <code>Note:</code></p>
<dl>
<dd>The returned values are not guaranteed to be sorted.</dl>
<p> Implemented in <code>DiscretizedDiscountBond</code>, and <code>DiscretizedOption</code>.</p>
<h3>bool isOnTime (Time t) const [protected]</h3>
<p>This method checks whether the asset was rolled at the given time.</p>
<h3>virtual void preAdjustValuesImpl () [protected, virtual]</h3>
<p>This method performs the actual pre-adjustment</p>
<h3>virtual void postAdjustValuesImpl () [protected, virtual]</h3>
<p>This method performs the actual post-adjustment </p>
<p> Reimplemented in <code>DiscretizedOption</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
