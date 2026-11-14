---
title: "stdshared_futurewait(3)"
name: "stdshared_futurewait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_futurewait/"
---

std::shared_future&lt;T&gt;::wait - std::shared_future&lt;T&gt;::wait

<h2>Synopsis</h2>

<pre><code>void wait() const;
(since C++ 11)</code></pre> 
Blocks until the result becomes available. valid() == true after the call. 
The behavior is undefined if valid()== false before the call to this function. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

The implementations are encouraged to detect the case when valid == false before the call and throw a std::future_error with an error condition of std::future_errc::no_state. 
Calling wait on the same std::shared_future from multiple threads is not safe; the intended use is for each thread that waits on the same shared state to have a copy of a std::shared_future. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;future&gt;

#include &lt;thread&gt;
int fib(int n)

{
    if (n &lt; 3)
        return 1;
    else
        return fib(n - 1) + fib(n - 2);
}
int main()

{
    std::shared_future&lt;int&gt; f1 = std::async(std::launch::async, []() {
        return fib(20);
    });
    std::shared_future&lt;int&gt; f2 = std::async(std::launch::async, []() {
        return fib(25);
    });
    std::cout &lt;&lt; &quot;waiting...\n&quot;;
    f1.wait();
    f2.wait();
    std::cout &lt;&lt; &quot;f1: &quot; &lt;&lt; f1.get() &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;f2: &quot; &lt;&lt; f2.get() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;waiting... 
&nbsp;<wbr>&nbsp;f1: 6765 
&nbsp;<wbr>&nbsp;f2: 75025

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available for the specified timeout duration 
wait_for <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available until specified time point has been reached 
wait_until <i>(public member function)</i> 
