---
title: "stdatomicfetch_add(3)"
name: "stdatomicfetch_add"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicfetch_add/"
---

std::atomic&lt;T&gt;::fetch_add - std::atomic&lt;T&gt;::fetch_add

<h2>Synopsis</h2>

<pre><code>member only of atomic&lt;Integral&gt;(C++11) and atomic&lt;Floating&gt;(C++20) template specializations

T fetch_add( T arg,

std::memory_order order = std::memory_order_seq_cst ) noexcept;

T fetch_add( T arg,

std::memory_order order = std::memory_order_seq_cst ) volatile noexcept;

member only of atomic&lt;T*&gt; template specialization                                           (1)

T* fetch_add( std::ptrdiff_t arg,

std::memory_order order = std::memory_order_seq_cst ) noexcept;                                 (2)

T* fetch_add( std::ptrdiff_t arg,

std::memory_order order = std::memory_order_seq_cst ) volatile noexcept;</code></pre> 
Atomically replaces the current value with the result of arithmetic addition of the value and arg. The operation is read-modify-write operation. Memory is affected according to the value of order. 
For signed Integral types, arithmetic is defined to use two’s complement representation. There are no undefined results. 
For floating-point types, the floating-point_environment in effect may be different from the calling thread's floating-point environment. The operation need not be conform to the corresponding std::numeric_limits traits but is encouraged to do so. If the result is not a representable value for its type, the result is unspecified but the operation otherwise has no undefined behavior. <i>(since C++20)</i> 
For T* types, the result may be an undefined address, but the operation otherwise has no undefined behavior. The program is ill-formed if T is not an object type. 

<h2>Parameters</h2>

arg - the other argument of arithmetic addition 
order - memory order constraints to enforce

<h2>Return value</h2>

The value immediately preceding the effects of this function in the modification_order of *this. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;thread&gt;

#include &lt;atomic&gt;
std::atomic&lt;long long&gt; data;

void do_work()

{
    data.fetch_add(1, std::memory_order_relaxed);
}
int main()

{
    std::thread th1(do_work);
    std::thread th2(do_work);
    std::thread th3(do_work);
    std::thread th4(do_work);
    std::thread th5(do_work);
    th1.join();
    th2.join();
    th3.join();
    th4.join();
    th5.join();
    std::cout &lt;&lt; &quot;Result:&quot; &lt;&lt; data &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Result:5 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
P0558R1 C++11 arithmetic permitted on pointers to cv void or function made ill-formed

<h2>See also</h2>

atomic_fetch_add 
atomic_fetch_add_explicit adds a non-atomic value to an atomic object and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
