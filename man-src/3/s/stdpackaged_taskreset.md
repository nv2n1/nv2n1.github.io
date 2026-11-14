---
title: "stdpackaged_taskreset(3)"
name: "stdpackaged_taskreset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpackaged_taskreset/"
---

std::packaged_task&lt;R(Args...)&gt;::reset - std::packaged_task&lt;R(Args...)&gt;::reset

<h2>Synopsis</h2>

<pre><code>void reset();
(since C++ 11)</code></pre> 
Resets the state abandoning the results of previous executions. New shared state is constructed. 
Equivalent to *this = packaged_task(std::move(f)), where f is the stored task. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

* std::future_error if *this has no shared state. The error condition is set to no_state. 
* std::bad_alloc if there was not enough memory for a new shared state. 
* any exception thrown by the move_constructor of the new packaged_task

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;thread&gt;

#include &lt;future&gt;
int main()

{
    std::packaged_task&lt;int(int, int)&gt; task([](int a, int b) {
        return std::pow(a, b);
    });
    std::future&lt;int&gt; result = task.get_future();
    task(2, 9);
    std::cout &lt;&lt; &quot;2^9 = &quot; &lt;&lt; result.get() &lt;&lt; '\n';
    task.reset();
    result = task.get_future();
    std::thread task_td(std::move(task), 2, 10);
    task_td.join();
    std::cout &lt;&lt; &quot;2^10 = &quot; &lt;&lt; result.get() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;2^9 = 512 
&nbsp;<wbr>&nbsp;2^10 = 1024
