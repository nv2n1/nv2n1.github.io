---
title: "stdexperimentalmake_ready_future(3)"
name: "stdexperimentalmake_ready_future"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalmake_ready_future/"
description: "std::experimental::make_ready_future – std::experimental::make_ready_future"
---

<p>std::experimental::make_ready_future &#8211; std::experimental::make_ready_future</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/future&gt;<br />
template &lt; class T &gt; <code>(1)</code> (concurrency TS)<br />
future&lt;V /* see below */&gt; make_ready_future(T&amp;&amp; value);<br />
future&lt;void&gt; make_ready_future(); <code>(2)</code> (concurrency TS)<br />
1) If std::decay_t&lt;T&gt; is std::reference_wrapper&lt;X&gt;, then the type V is X&amp;, otherwise, V is std::decay_t&lt;T&gt;.<br />
Creates a shared state of type V that is immediately ready, with the result constructed from std::forward&lt;T&gt;(value), then returns a std::experimental::future associated with that shared state.<br />
2) Creates a shared state of type void that is immediately ready, then returns a std::experimental::future associated with that shared state. </p>
<h2>Return value</h2>
<p>A std::experimental::future associated with the shared state that is created. </p>
<h2>See also</h2>
<p>make_exceptional_future produces a future that is ready immediately and holds the given exception<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(concurrency TS) </p>
