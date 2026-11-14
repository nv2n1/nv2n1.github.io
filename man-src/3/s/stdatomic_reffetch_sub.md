---
title: "stdatomic_reffetch_sub(3)"
name: "stdatomic_reffetch_sub"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_reffetch_sub/"
---

std::atomic_ref&lt;T&gt;::fetch_sub - std::atomic_ref&lt;T&gt;::fetch_sub

<h2>Synopsis</h2>

<pre><code>member only of atomic_ref&lt;Integral&gt; and atomic_ref&lt;Floating&gt; template specializations

    T
    fetch_sub(T arg, (1)

                         std::memory_order order = std::memory_order_seq_cst) const noexcept;

member only of atomic_ref&lt;T *&gt; template specialization

    T *
    fetch_sub(std::ptrdiff_t arg, (2)

                                      std::memory_order order = std::memory_order_seq_cst) const noexcept;</code></pre> 
Atomically replaces the current value of the referenced object with the result of arithmetic subtraction of the value and arg. This operation is a read-modify-write operation. Memory is affected according to the value of order. 
For signed integral types, arithmetic is defined to use two’s complement representation. There are no undefined results. 
For floating-point types, the floating-point_environment in effect may be different from the calling thread's floating-point environment. The operation need not be conform to the corresponding std::numeric_limits traits but is encouraged to do so. If the result is not a representable value for its type, the result is unspecified but the operation otherwise has no undefined behavior. 
For T* types, the result may be an undefined address, but the operation otherwise has no undefined behavior. The program is ill-formed if T is not an object type. 

<h2>Parameters</h2>

arg - the other argument of arithmetic subtraction 
order - memory order constraints to enforce

<h2>Return value</h2>

The value of the referenced object, immediately preceding the effects of this function. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
