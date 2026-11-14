---
title: "stdexperimentalpackaged_taskconcurrencyts(3)"
name: "stdexperimentalpackaged_taskconcurrencyts"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpackaged_taskconcurrencyts/"
---

std::experimental::packaged_task(concurrencyTS) - std::experimental::packaged_task(concurrencyTS)

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/future&gt;

template&lt; class &gt; class packaged_task; //not defined (1) (concurrency TS)

template&lt; class R, class ...Args &gt;                   (2) (concurrency TS)

class packaged_task&lt;R(Args...)&gt;;</code></pre> 
std::experimental::concurrency_v1::packaged_task is a modified version of std::packaged_task provided by the concurrency TS that works with std::experimental::future. 
The only change from std::packaged_task is that the get_future() member function returns a std::experimental::future&lt;R&gt;. 
