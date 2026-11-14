---
title: "stdthreadget_id(3)"
name: "stdthreadget_id"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthreadget_id/"
---

std::thread::get_id - std::thread::get_id

<h2>Synopsis</h2>

std::thread::id get_id() const noexcept; <i>(since C++11)</i> 
Returns a value of std::thread::id identifying the thread associated with *this. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A value of type std::thread::id identifying the thread associated with *this. If there is no thread associated, default constructed std::thread::id is returned. 

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
    std::thread t1(foo);
    std::thread::id t1_id = t1.get_id();
    std::thread t2(foo);
    std::thread::id t2_id = t2.get_id();
    std::cout &lt;&lt; &quot;t1's id: &quot; &lt;&lt; t1_id &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;t2's id: &quot; &lt;&lt; t2_id &lt;&lt; '\n';
    t1.join();
    t2.join();
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;t1's id: 0x35a7210f 
&nbsp;<wbr>&nbsp;t2's id: 0x35a311c4

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;represents the id of a thread 
id <i>(public member class)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the thread is joinable, i.e. potentially running in parallel context 
joinable <i>(public member function)</i> 
