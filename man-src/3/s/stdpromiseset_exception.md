---
title: "stdpromiseset_exception(3)"
name: "stdpromiseset_exception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpromiseset_exception/"
---

std::promise&lt;R&gt;::set_exception - std::promise&lt;R&gt;::set_exception

<h2>Synopsis</h2>

<pre><code>void set_exception(std::exception_ptr p);
(since C++ 11)</code></pre> 
Atomically stores the exception pointer p into the shared state and makes the state ready. 
The operation behaves as though set_value, set_exception, set_value_at_thread_exit, and set_exception_at_thread_exit acquire a single mutex associated with the promise object while updating the promise object. 
An exception is thrown if there is no shared state or the shared state already stores a value or exception. 
Calls to this function do not introduce data races with calls to get_future (but they need not synchronize with each other). 

<h2>Parameters</h2>

p - exception pointer to store. The behavior is undefined if p is null.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

std::future_error on the following conditions: 

 
* *this has no shared state. The error category is set to no_state. 

 

 
* The shared state already stores a value or exception. The error category is set to promise_already_satisfied.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;thread&gt;

#include &lt;iostream&gt;

#include &lt;future&gt;
int main()

{
    std::promise&lt;int&gt; p;
    std::future&lt;int&gt; f = p.get_future();
    std::thread t([&amp;p] {
        try {
            // code that may throw
            throw std::runtime_error(&quot;Example&quot;);
        } catch (...) {
            try {
                // store anything thrown in the promise
                p.set_exception(std::current_exception());
            } catch (...) {
            } // set_exception() may throw too
        }
    });
    try {
        std::cout &lt;&lt; f.get();
    } catch (const std::exception &amp;e) {
        std::cout &lt;&lt; &quot;Exception from the thread: &quot; &lt;&lt; e.what() &lt;&lt; '\n';
    }
    t.join();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Exception from the thread: Example

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the result to indicate an exception while delivering the notification only at thread exit 
set_exception_at_thread_exit <i>(public member function)</i> 
