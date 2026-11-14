---
title: "stdthis_threadget_id(3)"
name: "stdthis_threadget_id"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthis_threadget_id/"
---

std::this_thread::get_id - std::this_thread::get_id

<h2>Synopsis</h2>

Defined in header &lt;thread&gt; 
std::thread::id get_id() noexcept; <i>(since C++11)</i> 
Returns the id of the current thread. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

id of the current thread 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;

#include &lt;mutex&gt;
std::mutex g_display_mutex;
void foo()

{
    std::thread::id this_id = std::this_thread::get_id();
    g_display_mutex.lock();
    std::cout &lt;&lt; &quot;thread &quot; &lt;&lt; this_id &lt;&lt; &quot; sleeping...\n&quot;;
    g_display_mutex.unlock();
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
int main()

{
    std::thread t1(foo);
    std::thread t2(foo);
    t1.join();
    t2.join();
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;thread 0x2384b312 sleeping... 
&nbsp;<wbr>&nbsp;thread 0x228a10fc sleeping...

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the id of the thread 
get_id <i>(public member function of std::thread)</i> 
