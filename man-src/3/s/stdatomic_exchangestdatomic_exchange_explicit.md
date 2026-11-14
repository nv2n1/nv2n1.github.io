---
title: "stdatomic_exchangestdatomic_exchange_explicit(3)"
name: "stdatomic_exchangestdatomic_exchange_explicit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_exchangestdatomic_exchange_explicit/"
---

std::atomic_exchange,std::atomic_exchange_explicit - std::atomic_exchange,std::atomic_exchange_explicit

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;atomic&gt;

template&lt; class T &gt;

T atomic_exchange( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type desr ) noexcept;

template&lt; class T &gt;

T atomic_exchange( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type desr ) noexcept;

template&lt; class T &gt;                                       (1) (since C++11)

T atomic_exchange_explicit( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type desr,

std::memory_order order ) noexcept;                                         (2) (since C++11)

template&lt; class T &gt;

T atomic_exchange_explicit( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type desr,

std::memory_order order ) noexcept;</code></pre> 
1) Atomically replaces the value pointed to by obj with the value of desr and returns the value obj held previously, as if by obj-&gt;exchange(desr) 
2) Atomically replaces the value pointed to by obj with the value of desr and returns the value obj held previously, as if by obj-&gt;exchange(desr, order) 

<h2>Parameters</h2>

obj - pointer to the atomic object to modify 
desr - the value to store in the atomic object 
order - the memory synchronization ordering for this operation: all values are permitted.

<h2>Return value</h2>

The value held previously by the atomic object pointed to by obj 

<h2>Example</h2>

A spinlock mutex can be implemented in userspace using an atomic exchange operation, similar to std::atomic_flag_test_and_set: 
 // Run this code #include &lt;thread&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;atomic&gt; 
&nbsp;<wbr>&nbsp;std::atomic&lt;bool&gt; lock(false); // holds true when locked 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// holds false when unlocked <pre><code>void f(int n)

{
    for (int cnt = 0; cnt &lt; 100; ++cnt) {
        while (std::atomic_exchange_explicit(&amp;lock, true, std::memory_order_acquire))
            ; // spin until acquired
        std::cout &lt;&lt; &quot;Output from thread &quot; &lt;&lt; n &lt;&lt; '\n';
        std::atomic_store_explicit(&amp;lock, false, std::memory_order_release);
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

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
P0558R1 C++11 exact type match required because T is deduced from multiple arguments T is deduced from the atomic argument only

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically replaces the value of the atomic object and obtains the value held previously 
exchange <i>(public member function of std::atomic&lt;T&gt;)</i> 
atomic_compare_exchange_weak 
atomic_compare_exchange_weak_explicit 
atomic_compare_exchange_strong 
atomic_compare_exchange_strong_explicit atomically compares the value of the atomic object with non-atomic argument and performs atomic exchange if equal or atomic load if not 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes atomic operations for std::shared_ptr 
std::atomic_exchange(std::shared_ptr)_ <i>(function template)</i> 
std::atomic_exchange_explicit(std::shared_ptr) 
