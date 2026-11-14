---
title: "stdpromiseset_value_at_thread_exit(3)"
name: "stdpromiseset_value_at_thread_exit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpromiseset_value_at_thread_exit/"
---

std::promise&lt;R&gt;::set_value_at_thread_exit - std::promise&lt;R&gt;::set_value_at_thread_exit

<h2>Synopsis</h2>

<pre><code>void set_value_at_thread_exit(const R &amp;value);
(1)(member only of generic promise template)(since C++ 11)

    void set_value_at_thread_exit(R &amp;&amp;value);
(2)(member only of generic promise template)(since C++ 11)

    void set_value_at_thread_exit(R &amp;value);
(3)(member only of promise&lt;R &amp;&gt; template specialization)(since C++ 11)

    void set_value_at_thread_exit()(4)(member only of promise&lt;void&gt; template specialization)(since C++ 11)</code></pre> 
Stores the value into the shared state without making the state ready immediately. The state is made ready when the current thread exits, after all variables with thread-local storage duration have been destroyed. 
The operation behaves as though set_value, set_exception, set_value_at_thread_exit, and set_exception_at_thread_exit acquire a single mutex associated with the promise object while updating the promise object. 
An exception is thrown if there is no shared state or the shared state already stores a value or exception. 
Calls to this function do not introduce data races with calls to get_future (but they need not synchronize with each other). 

<h2>Parameters</h2>

value - value to store in the shared state

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

std::future_error on the following conditions: 

 
* *this has no shared state. The error category is set to no_state. 

 

 
* The shared state already stores a value or exception. The error category is set to promise_already_satisfied. 

 
Additionally: 
1-2) Any exception thrown by the copy constructor of value 
3) Any exception thrown by the move constructor of value

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;future&gt;

#include &lt;thread&gt;
int main()

{
    using namespace std::chrono_literals;
    std::promise&lt;int&gt; p;
    std::future&lt;int&gt; f = p.get_future();
    std::thread([&amp;p] {
        std::this_thread::sleep_for(1s);
        p.set_value_at_thread_exit(9);
    }).detach();
    std::cout &lt;&lt; &quot;Waiting...&quot; &lt;&lt; std::flush;
    f.wait();
    std::cout &lt;&lt; &quot;Done!\nResult is: &quot; &lt;&lt; f.get() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Waiting...Done! 
&nbsp;<wbr>&nbsp;Result is: 9

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the result to specific value 
set_value <i>(public member function)</i> 
