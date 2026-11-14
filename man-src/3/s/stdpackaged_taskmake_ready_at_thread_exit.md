---
title: "stdpackaged_taskmake_ready_at_thread_exit(3)"
name: "stdpackaged_taskmake_ready_at_thread_exit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpackaged_taskmake_ready_at_thread_exit/"
---

std::packaged_task&lt;R(Args...)&gt;::make_ready_at_thread_exit - std::packaged_task&lt;R(Args...)&gt;::make_ready_at_thread_exit

<h2>Synopsis</h2>

<pre><code>void make_ready_at_thread_exit(ArgTypes... args);
(since C++ 11)</code></pre> 
Calls the stored task with forwarded args as the arguments. The return value of the task or any exception thrown by it is stored in the shared state of *this. 
The shared state is only made ready after the current thread exits and all objects of thread local storage duration are destroyed. 

<h2>Parameters</h2>

args - the parameters to pass on invocation of the stored task

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

std::future_error on the following error conditions: 

 
* The stored task has already been invoked. The error category is set to promise_already_satisfied. 
* *this has no shared state. The error category is set to no_state.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;future&gt;

#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;thread&gt;

#include &lt;functional&gt;

#include &lt;utility&gt;
void worker(std::future&lt;void&gt; &amp;output)

{
    std::packaged_task&lt;void(bool &amp;)&gt; my_task{[](bool &amp;done) { done = true; }};
    auto result = my_task.get_future();
    bool done = false;
    my_task.make_ready_at_thread_exit(done); // execute task right away
    std::cout &lt;&lt; &quot;worker: done = &quot; &lt;&lt; std::boolalpha &lt;&lt; done &lt;&lt; std::endl;
    auto status = result.wait_for(std::chrono::seconds(0));
    if (status == std::future_status::timeout)
        std::cout &lt;&lt; &quot;worker: result is not ready yet&quot; &lt;&lt; std::endl;
    output = std::move(result);
}

int main()

{
    std::future&lt;void&gt; result;
    std::thread{worker, std::ref(result)}.join();
    auto status = result.wait_for(std::chrono::seconds(0));
    if (status == std::future_status::ready)
        std::cout &lt;&lt; &quot;main: result is ready&quot; &lt;&lt; std::endl;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;worker: done = true 
&nbsp;<wbr>&nbsp;worker: result is not ready yet 
&nbsp;<wbr>&nbsp;main: result is ready

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;executes the function 
operator() <i>(public member function)</i> 
