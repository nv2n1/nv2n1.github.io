---
title: "stdthreaddetach(3)"
name: "stdthreaddetach"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthreaddetach/"
---

std::thread::detach - std::thread::detach

<h2>Synopsis</h2>

<pre><code>void detach();
(since C++ 11)</code></pre> 
Separates the thread of execution from the thread object, allowing execution to continue independently. Any allocated resources will be freed once the thread exits. 
After calling detach *this no longer owns any thread. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Postconditions</h2>

joinable is false

<h2>Exceptions</h2>

std::system_error if joinable() == false or an error occurs.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;thread&gt;
void independentThread()

{
    std::cout &lt;&lt; &quot;Starting concurrent thread.\n&quot;;
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout &lt;&lt; &quot;Exiting concurrent thread.\n&quot;;
}
void threadCaller()

{
    std::cout &lt;&lt; &quot;Starting thread caller.\n&quot;;
    std::thread t(independentThread);
    t.detach();
    std::this_thread::sleep_for(std::chrono::seconds(1));
    std::cout &lt;&lt; &quot;Exiting thread caller.\n&quot;;
}
int main()

{
    threadCaller();
    std::this_thread::sleep_for(std::chrono::seconds(5));
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Starting thread caller. 
&nbsp;<wbr>&nbsp;Starting concurrent thread. 
&nbsp;<wbr>&nbsp;Exiting thread caller. 
&nbsp;<wbr>&nbsp;Exiting concurrent thread.

<h2>References</h2>

* C++11 standard (ISO/IEC 14882:2011): 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* 30.3.1.5 thread members [thread.thread.member]

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for a thread to finish its execution 
join <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the thread is joinable, i.e. potentially running in parallel context 
joinable <i>(public member function)</i> 
