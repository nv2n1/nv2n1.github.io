---
title: "stdthreadjoin(3)"
name: "stdthreadjoin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthreadjoin/"
---

std::thread::join - std::thread::join

<h2>Synopsis</h2>

<pre><code>void join();
(since C++ 11)</code></pre> 
Blocks the current thread until the thread identified by *this finishes its execution. 
The completion of the thread identified by *this synchronizes with the corresponding successful return from join(). 
No synchronization is performed on *this itself. Concurrently calling join() on the same std::thread object from multiple threads constitutes a data race that results in undefined behavior. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Postconditions</h2>

joinable() is false

<h2>Exceptions</h2>

std::system_error if an error occurs.

<h2>Error Conditions</h2>

* resource_deadlock_would_occur if this-&gt;get_id() == std::this_thread::get_id() <i>(deadlock detected)</i> 
* no_such_process if the thread is not valid 
* invalid_argument if joinable() is false

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;
void foo()

{
    // simulate expensive operation
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
void bar()

{
    // simulate expensive operation
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
int main()

{
    std::cout &lt;&lt; &quot;starting first helper...\n&quot;;
    std::thread helper1(foo);
    std::cout &lt;&lt; &quot;starting second helper...\n&quot;;
    std::thread helper2(bar);
    std::cout &lt;&lt; &quot;waiting for helpers to finish...&quot; &lt;&lt; std::endl;
    helper1.join();
    helper2.join();
    std::cout &lt;&lt; &quot;done!\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;starting first helper... 
&nbsp;<wbr>&nbsp;starting second helper... 
&nbsp;<wbr>&nbsp;waiting for helpers to finish... 
&nbsp;<wbr>&nbsp;done!

<h2>References</h2>

* C++11 standard (ISO/IEC 14882:2011): 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* 30.3.1.5 thread members [thread.thread.member]

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;permits the thread to execute independently from the thread handle 
detach <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the thread is joinable, i.e. potentially running in parallel context 
joinable <i>(public member function)</i> 
