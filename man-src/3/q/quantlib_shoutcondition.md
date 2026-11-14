---
title: "quantlib_shoutcondition(3)"
name: "quantlib_shoutcondition"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_shoutcondition/"
description: "QuantLib::ShoutCondition – Shout option condition."
---

<p>QuantLib::ShoutCondition &#8211; Shout option condition. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/shoutcondition.hpp&gt; </p>
<p> Inherits QuantLib::CurveDependentStepCondition&lt; Array &gt;. </p>
<h3>Public Member Functions</h3>
<p><code>ShoutCondition</code> (Option::Type type, Real strike, Time resTime, Rate rate) </p>
<p> <code>ShoutCondition</code> (const <code>Array</code> &amp;intrinsicValues, Time resTime, Rate rate) </p>
<p> void <code>applyTo</code> (<code>Array</code> &amp;a, Time t) const </p>
<h2>Detailed Description</h2>
<p>Shout option condition. </p>
<p> A shout option is an option where the holder has the right to lock in a minimum value for the payoff at one (shout) time during the option&#8217;s life. The minimum value is the option&#8217;s intrinsic value at the shout time. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
