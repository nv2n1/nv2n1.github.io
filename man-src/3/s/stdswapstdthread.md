---
title: "stdswapstdthread(3)"
name: "stdswapstdthread"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdthread/"
---

std::swap(std::thread) - std::swap(std::thread)

<h2>Synopsis</h2>

<pre><code>void swap(thread &amp;lhs, thread &amp;rhs) noexcept;
(since C++ 11)</code></pre> 
Overloads the std::swap algorithm for std::thread. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - threads whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;
void foo()

{
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
void bar()

{
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
int main()

{
    std::thread t1(foo);
    std::thread t2(bar);
    std::cout &lt;&lt; &quot;thread 1 id: &quot; &lt;&lt; t1.get_id() &lt;&lt; std::endl;
    std::cout &lt;&lt; &quot;thread 2 id: &quot; &lt;&lt; t2.get_id() &lt;&lt; std::endl;
    std::swap(t1, t2);
    std::cout &lt;&lt; &quot;after std::swap(t1, t2):&quot; &lt;&lt; std::endl;
    std::cout &lt;&lt; &quot;thread 1 id: &quot; &lt;&lt; t1.get_id() &lt;&lt; std::endl;
    std::cout &lt;&lt; &quot;thread 2 id: &quot; &lt;&lt; t2.get_id() &lt;&lt; std::endl;
    t1.swap(t2);
    std::cout &lt;&lt; &quot;after t1.swap(t2):&quot; &lt;&lt; std::endl;
    std::cout &lt;&lt; &quot;thread 1 id: &quot; &lt;&lt; t1.get_id() &lt;&lt; std::endl;
    std::cout &lt;&lt; &quot;thread 2 id: &quot; &lt;&lt; t2.get_id() &lt;&lt; std::endl;
    t1.join();
    t2.join();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;thread 1 id: 1892 
&nbsp;<wbr>&nbsp;thread 2 id: 2584 
&nbsp;<wbr>&nbsp;after std::swap(t1, t2): 
&nbsp;<wbr>&nbsp;thread 1 id: 2584 
&nbsp;<wbr>&nbsp;thread 2 id: 1892 
&nbsp;<wbr>&nbsp;after t1.swap(t2): 
&nbsp;<wbr>&nbsp;thread 1 id: 1892 
&nbsp;<wbr>&nbsp;thread 2 id: 2584

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two thread objects 
swap <i>(public member function)</i> 
