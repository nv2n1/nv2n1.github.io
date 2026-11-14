---
title: "state(3)"
name: "state"
section: "3"
letter: "s"
url: "/docs/linux/man/3-state/"
description: "QuantLib::EarlyExercisePathPricer – base class for early exercise path pricers"
---

<p>QuantLib::EarlyExercisePathPricer &#8211; base class for early exercise path pricers </p>
<h2>Synopsis</h2>
<pre><code>virtual ValueType operator() (const PathType &amp;path, TimeType t) const =0



virtual StateType state (const PathType &amp;path, TimeType t) const =0



virtual std::vector&lt; boost::function1&lt; ValueType, StateType &gt; &gt; basisSystem () const =0</code></pre>
<h3>Public Types</h3>
<p>typedef EarlyExerciseTraits&lt; PathType &gt;::StateType <code>StateType</code></p>
<h3>Public Member Functions</h3>
<pre><code>virtual ValueType operator() (const PathType &amp;path, TimeType t) const =0



virtual StateType state (const PathType &amp;path, TimeType t) const =0



virtual std::vector&lt; boost::function1&lt; ValueType, StateType &gt; &gt; basisSystem () const =0</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class PathType, class TimeType = Size, class ValueType = Real&gt; class QuantLib::EarlyExercisePathPricer&lt; PathType, TimeType, ValueType &gt;</h3>
<p>base class for early exercise path pricers </p>
<p> Returns the value of an option on a given path and given time.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
