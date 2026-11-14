---
title: "stdexperimentalpromiseconcurrencyts(3)"
name: "stdexperimentalpromiseconcurrencyts"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpromiseconcurrencyts/"
description: "std::experimental::promise(concurrencyTS) – std::experimental::promise(concurrencyTS)"
---

<p>std::experimental::promise(concurrencyTS) &#8211; std::experimental::promise(concurrencyTS)</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/future&gt;<br />
template&lt; class R &gt; class promise; <code>(1)</code> (concurrency TS)<br />
template&lt; class R &gt; class promise&lt;R&amp;&gt;; <code>(2)</code> (concurrency TS)<br />
template&lt;&gt; class promise&lt;void&gt;; <code>(3)</code> (concurrency TS)<br />
std::experimental::concurrency_v1::promise is a modified version of std::promise provided by the concurrency TS that works with std::experimental::future.<br />
The only change from std::promise is that the get_future() member function returns a std::experimental::future. </p>
