---
title: "stdfuture(3)"
name: "stdfuture"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfuture/"
description: "std::future – std::future"
---

<p>std::future &#8211; std::future</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;future&gt;<br />
template&lt; class T &gt; class future; <code>(1)</code> <i>(since C++11)</i><br />
template&lt; class T &gt; class future&lt;T&amp;&gt;; <code>(2)</code> <i>(since C++11)</i><br />
template&lt;&gt; class future&lt;void&gt;; <code>(3)</code> <i>(since C++11)</i><br />
The class template std::future provides a mechanism to access the result of asynchronous operations:<br />
* An asynchronous operation (created via std::async, std::packaged_task, or std::promise) can provide a std::future object to the creator of that asynchronous operation.<br />
* The creator of the asynchronous operation can then use a variety of methods to query, wait for, or extract a value from the std::future. These methods may block if the asynchronous operation has not yet provided a value.<br />
* When the asynchronous operation is ready to send a result to the creator, it can do so by modifying shared state (e.g. std::promise::set_value) that is linked to the creator&#8217;s std::future.<br />
Note that std::future references shared state that is not shared with any other asynchronous return objects (as opposed to std::shared_future). </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the future object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the future object<br />
destructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the future object<br />
operator= <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transfers the shared state from *this to a shared_future and returns it<br />
share <i>(public member function)</i></p>
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
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;future&gt;

#include &lt;thread&gt;
int main()

{
    // future from a packaged_task
    std::packaged_task&lt;int()&gt; task([] { return 7; }); // wrap the function
    std::future&lt;int&gt; f1 = task.get_future();          // get a future
    std::thread t(std::move(task));                   // launch on a thread
                                                      // future from an async()
    std::future&lt;int&gt; f2 = std::async(std::launch::async, [] { return 8; });
    // future from a promise
    std::promise&lt;int&gt; p;
    std::future&lt;int&gt; f3 = p.get_future();
    std::thread([&amp;p] { p.set_value_at_thread_exit(9); }).detach();
    std::cout &lt;&lt; &quot;Waiting...&quot; &lt;&lt; std::flush;
    f1.wait();
    f2.wait();
    f3.wait();
    std::cout &lt;&lt; &quot;Done!
Results are: &quot;
              &lt;&lt; f1.get() &lt;&lt; ' ' &lt;&lt; f2.get() &lt;&lt; ' ' &lt;&lt; f3.get() &lt;&lt; '
';
    t.join();
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Waiting&#8230;Done!<br />
&nbsp;<wbr>&nbsp;Results are: 7 8 9</p>
<h2>See also</h2>
<p>async runs a function asynchronously (potentially in a new thread) and returns a std::future that will hold the result<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
shared_future waits for a value (possibly referenced by other futures) that is set asynchronously<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
