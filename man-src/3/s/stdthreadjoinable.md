---
title: "stdthreadjoinable(3)"
name: "stdthreadjoinable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthreadjoinable/"
---

std::thread::joinable - std::thread::joinable

<h2>Synopsis</h2>

bool joinable() const noexcept; <i>(since C++11)</i> 
Checks if the thread object identifies an active thread of execution. Specifically, returns true if get_id() != std::thread::id(). So a default constructed thread is not joinable. 
A thread that has finished executing code, but has not yet been joined is still considered an active thread of execution and is therefore joinable. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the thread object identifies an active thread of execution, false otherwise 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;
void foo()

{
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
int main()

{
    std::thread t;
    std::cout &lt;&lt; &quot;before starting, joinable: &quot; &lt;&lt; std::boolalpha &lt;&lt; t.joinable()
              &lt;&lt; '\n';
    t = std::thread(foo);
    std::cout &lt;&lt; &quot;after starting, joinable: &quot; &lt;&lt; t.joinable()
              &lt;&lt; '\n';
    t.join();
    std::cout &lt;&lt; &quot;after joining, joinable: &quot; &lt;&lt; t.joinable()
              &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;before starting, joinable: false 
&nbsp;<wbr>&nbsp;after starting, joinable: true 
&nbsp;<wbr>&nbsp;after joining, joinable: false

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the id of the thread 
get_id <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for a thread to finish its execution 
join <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;permits the thread to execute independently from the thread handle 
detach <i>(public member function)</i> 

<h2>References</h2>

* C++11 standard (ISO/IEC 14882:2011): 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* 30.3.1.5 thread members [thread.thread.member]
