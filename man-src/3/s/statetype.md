---
title: "statetype(3)"
name: "statetype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-statetype/"
description: "QuantLib::EarlyExercisePathPricer – base class for early exercise path pricers"
---

<p>QuantLib::EarlyExercisePathPricer &#8211; base class for early exercise path pricers </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/montecarlo/earlyexercisepathpricer.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef EarlyExerciseTraits&lt; PathType &gt;::StateType <code>StateType</code> </p>
<h3>Public Member Functions</h3>
<p>virtual ValueType <code>operator()</code> (const PathType &amp;path, TimeType t) const =0 </p>
<p> virtual StateType <code>state</code> (const PathType &amp;path, TimeType t) const =0 </p>
<p> virtual std::vector&lt; boost::function1&lt; ValueType, StateType &gt; &gt; <code>basisSystem</code> () const =0 </p>
<h2>Detailed Description</h2>
<h3>template&lt;class PathType, class TimeType = Size, class ValueType = Real&gt; class QuantLib::EarlyExercisePathPricer&lt; PathType, TimeType, ValueType &gt;</h3>
<p>base class for early exercise path pricers </p>
<p> Returns the value of an option on a given path and given time. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
