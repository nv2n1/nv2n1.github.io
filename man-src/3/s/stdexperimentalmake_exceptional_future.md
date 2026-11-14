---
title: "stdexperimentalmake_exceptional_future(3)"
name: "stdexperimentalmake_exceptional_future"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalmake_exceptional_future/"
---

std::experimental::make_exceptional_future - std::experimental::make_exceptional_future

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / future&gt;

    template &lt;class T&gt;
    (1)(concurrency TS)

        future&lt;T&gt; make_exceptional_future(std::exception_ptr ex);

template &lt;class T, class E&gt;
(2)(concurrency TS)

    future&lt;T&gt; make_exceptional_future(E ex);
1) Creates a shared state of type T that is immediately ready and stores the exception pointer ex, then return a future associated with that shared state, as if by promise&lt;T&gt; p;
p.set_exception(ex);
return p.get_future();. The behavior is undefined if ex is null.

2) Creates a shared state of type T that is immediately ready and stores an exception pointer created from ex, then return a future associated with that shared state, as if by promise&lt;T&gt; p;
p.set_exception(std::make_exception_ptr(ex));
return p.get_future();
</code></pre>

<h2>Return value</h2>

A future object associated with the shared state that was created. 

<h2>See also</h2>

make_ready_future produces a future that is ready immediately and holds the given value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(concurrency TS) 
