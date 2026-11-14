---
title: "stdatomic_flag(3)"
name: "stdatomic_flag"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_flag/"
---

std::atomic_flag - std::atomic_flag

<h2>Synopsis</h2>

Defined in header &lt;atomic&gt; 
class atomic_flag; <i>(since C++11)</i> 
std::atomic_flag is an atomic boolean type. Unlike all specializations of std::atomic, it is guaranteed to be lock-free. Unlike std::atomic&lt;bool&gt;, std::atomic_flag does not provide load or store operations. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an atomic_flag 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the assignment operator 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically sets flag to false 
clear <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically sets the flag to true and obtains its previous value 
test_and_set <i>(public member function)</i>

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
        while (lock.test_and_set(std::memory_order_acquire)) // acquire lock
            ;                                                // spin
        std::cout &lt;&lt; &quot;Output from thread &quot; &lt;&lt; n &lt;&lt; '\n';
        lock.clear(std::memory_order_release); // release lock
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

atomic_flag_test_and_set 
atomic_flag_test_and_set_explicit atomically sets the flag to true and returns its previous value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
atomic_flag_clear 
atomic_flag_clear_explicit atomically sets the value of the flag to false 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
ATOMIC_FLAG_INIT initializes an std::atomic_flag to false 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(macro constant) 
<i>(C++11)</i> 
