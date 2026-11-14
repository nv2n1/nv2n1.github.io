---
title: "stdatomic_flag_test_and_setstdatomic_flag_test_and_set_explicit(3)"
name: "stdatomic_flag_test_and_setstdatomic_flag_test_and_set_explicit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_flag_test_and_setstdatomic_flag_test_and_set_explicit/"
---

std::atomic_flag_test_and_set,std::atomic_flag_test_and_set_explicit - std::atomic_flag_test_and_set,std::atomic_flag_test_and_set_explicit

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;atomic&gt;

bool atomic_flag_test_and_set( volatile std::atomic_flag* p ) noexcept;

bool atomic_flag_test_and_set( std::atomic_flag* p ) noexcept;

bool atomic_flag_test_and_set_explicit( volatile std::atomic_flag* p,   (1) (since C++11)

std::memory_order order ) noexcept;                                                       (2) (since C++11)

bool atomic_flag_test_and_set_explicit( std::atomic_flag* p,

std::memory_order order ) noexcept;</code></pre> 
Atomically changes the state of a std::atomic_flag pointed to by p to set (true) and returns the value it held before. 

<h2>Parameters</h2>

p - pointer to std::atomic_flag to access 
order - the memory synchronization order for this operation

<h2>Return value</h2>

The value previously held by the flag pointed to by p 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;bool atomic_flag_test_and_set(volatile std::atomic_flag* p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return p-&gt;test_and_set(); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;bool atomic_flag_test_and_set(std::atomic_flag* p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return p-&gt;test_and_set(); 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;bool atomic_flag_test_and_set_explicit(volatile std::atomic_flag* p, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::memory_order order) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return p-&gt;test_and_set(order); 
&nbsp;<wbr>&nbsp;} 

 
Fourth version 

 
&nbsp;<wbr>&nbsp;bool atomic_flag_test_and_set_explicit(std::atomic_flag* p, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::memory_order order) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return p-&gt;test_and_set(order); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

A spinlock mutex can be implemented in userspace using an atomic_flag 
 // Run this code <pre><code>#include &lt;thread&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;atomic&gt;
std::atomic_flag lock = ATOMIC_FLAG_INIT;
void f(int n)

{
    for (int cnt = 0; cnt &lt; 100; ++cnt) {
        while (std::atomic_flag_test_and_set_explicit(&amp;lock, std::memory_order_acquire))
            ; // spin until the lock is acquired
        std::cout &lt;&lt; &quot;Output from thread &quot; &lt;&lt; n &lt;&lt; '\n';
        std::atomic_flag_clear_explicit(&amp;lock, std::memory_order_release);
    }
}
int main()

{
    std::vector&lt;std::thread&gt; v;
    for (int n = 0; n &lt; 10; ++n) {
        v.emplace_back(f, n);
    }
    for (auto &amp;t : v) {
        t.join();
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Output from thread 2 
&nbsp;<wbr>&nbsp;Output from thread 6 
&nbsp;<wbr>&nbsp;Output from thread 7 
&nbsp;<wbr>&nbsp;...&lt;exactly 1000 lines&gt;...

<h2>See also</h2>

atomic_flag the lock-free boolean atomic type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
atomic_flag_clear 
atomic_flag_clear_explicit atomically sets the value of the flag to false 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
memory_order defines memory ordering constraints for the given atomic operation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
