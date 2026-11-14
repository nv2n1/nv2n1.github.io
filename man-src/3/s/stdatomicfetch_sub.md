---
title: "stdatomicfetch_sub(3)"
name: "stdatomicfetch_sub"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicfetch_sub/"
---

std::atomic&lt;T&gt;::fetch_sub - std::atomic&lt;T&gt;::fetch_sub

<h2>Synopsis</h2>

<pre><code>member only of atomic&lt;Integral&gt;(C++11) and atomic&lt;Floating&gt;(C++20) template specializations

T fetch_sub( T arg,

std::memory_order order = std::memory_order_seq_cst ) noexcept;

T fetch_sub( T arg,

std::memory_order order = std::memory_order_seq_cst ) volatile noexcept;

member only of atomic&lt;T*&gt; template specialization                                           (1)

T* fetch_sub( std::ptrdiff_t arg,

std::memory_order order = std::memory_order_seq_cst ) noexcept;                                 (2)

T* fetch_sub( std::ptrdiff_t arg,

std::memory_order order = std::memory_order_seq_cst ) volatile noexcept;</code></pre> 
Atomically replaces the current value with the result of arithmetic subtraction of the value and arg. The operation is read-modify-write operation. Memory is affected according to the value of order. 
For signed Integral types, arithmetic is defined to use two’s complement representation. There are no undefined results. 
For floating-point types, the floating-point_environment in effect may be different from the calling thread's floating-point environment. The operation need not be conform to the corresponding std::numeric_limits traits but is encouraged to do so. If the result is not a representable value for its type, the result is unspecified but the operation otherwise has no undefined behavior. <i>(since C++20)</i> 
For T* types, the result may be an undefined address, but the operation otherwise has no undefined behavior. The program is ill-formed if T is not an object type. 

<h2>Parameters</h2>

arg - the other argument of arithmetic subtraction 
order - memory order constraints to enforce

<h2>Return value</h2>

The value immediately preceding the effects of this function in the modification_order of *this. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
P0558R1 C++11 arithmetic permitted on pointers to cv void or function made ill-formed 

<h2>See also</h2>

atomic_fetch_sub 
atomic_fetch_sub_explicit subtracts a non-atomic value from an atomic object and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
