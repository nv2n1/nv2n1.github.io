---
title: "stdshared_future(3)"
name: "stdshared_future"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_future/"
description: "std::shared_future – std::shared_future"
---

<p>std::shared_future &#8211; std::shared_future</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;future&gt;<br />
template&lt; class T &gt; class shared_future; <code>(1)</code> <i>(since C++11)</i><br />
template&lt; class T &gt; class shared_future&lt;T&amp;&gt;; <code>(2)</code> <i>(since C++11)</i><br />
template&lt;&gt; class shared_future&lt;void&gt;; <code>(3)</code> <i>(since C++11)</i><br />
The class template std::shared_future provides a mechanism to access the result of asynchronous operations, similar to std::future, except that multiple threads are allowed to wait for the same shared state. Unlike std::future, which is only moveable (so only one instance can refer to any particular asynchronous result), std::shared_future is copyable and multiple shared future objects may refer to the same shared state.<br />
Access to the same shared state from multiple threads is safe if each thread does it through its own copy of a shared_future object. </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the future object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the future object<br />
destructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the contents<br />
operator= <i>(public member function)</i></p>
<h2>Getting the result</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the result<br />
get <i>(public member function)</i></p>
<h2>State</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the future has a shared state<br />
valid <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result to become available<br />
wait <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available for the specified timeout duration<br />
wait_for <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available until specified time point has been reached<br />
wait_until <i>(public member function)</i></p>
<h2>Example</h2>
<p>A shared_future may be used to signal multiple threads simultaneously, similar to std::condition_variable::notify_all()<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;future&gt;

#include &lt;chrono&gt;
int main()

{
    std::promise&lt;void&gt; ready_promise, t1_ready_promise, t2_ready_promise;
    std::shared_future&lt;void&gt; ready_future(ready_promise.get_future());
    std::chrono::time_point&lt;std::chrono::high_resolution_clock&gt; start;
    auto fun1 = [&amp;, ready_future]() -&gt; std::chrono::duration&lt;double, std::milli&gt; {
        t1_ready_promise.set_value();
        ready_future.wait(); // waits for the signal from main()
        return std::chrono::high_resolution_clock::now() - start;
    };

    auto fun2 = [&amp;, ready_future]() -&gt; std::chrono::duration&lt;double, std::milli&gt; {
        t2_ready_promise.set_value();
        ready_future.wait(); // waits for the signal from main()
        return std::chrono::high_resolution_clock::now() - start;
    };
    auto fut1 = t1_ready_promise.get_future();
    auto fut2 = t2_ready_promise.get_future();
    auto result1 = std::async(std::launch::async, fun1);
    auto result2 = std::async(std::launch::async, fun2);
    // wait for the threads to become ready
    fut1.wait();
    fut2.wait();
    // the threads are ready, start the clock
    start = std::chrono::high_resolution_clock::now();
    // signal the threads to go
    ready_promise.set_value();
    std::cout &lt;&lt; &quot;Thread 1 received the signal &quot;
              &lt;&lt; result1.get().count() &lt;&lt; &quot; ms after start
&quot;
              &lt;&lt; &quot;Thread 2 received the signal &quot;
              &lt;&lt; result2.get().count() &lt;&lt; &quot; ms after start
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Thread 1 received the signal 0.072 ms after start<br />
&nbsp;<wbr>&nbsp;Thread 2 received the signal 0.041 ms after start</p>
