---
title: "stdatomic_fetch_xorstdatomic_fetch_xor_explicit(3)"
name: "stdatomic_fetch_xorstdatomic_fetch_xor_explicit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_fetch_xorstdatomic_fetch_xor_explicit/"
---

std::atomic_fetch_xor,std::atomic_fetch_xor_explicit - std::atomic_fetch_xor,std::atomic_fetch_xor_explicit

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;atomic&gt;

template&lt; class T &gt;

T atomic_fetch_xor( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type arg ) noexcept;

template&lt; class T &gt;

T atomic_fetch_xor( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type arg ) noexcept;

template&lt; class T &gt;                                        (1) (since C++11)

T atomic_fetch_xor_explicit( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type arg,

std::memory_order order) noexcept;                                           (2) (since C++11)

template&lt; class T &gt;

T atomic_fetch_xor_explicit( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type arg,

std::memory_order order) noexcept;
</code></pre> 
Atomically replaces the value pointed by obj with the result of bitwise XOR between the old value of obj and arg. Returns the value obj held previously. 
The operation is performed as if the following is executed: 
1) obj-&gt;fetch_xor(arg) 
2) obj-&gt;fetch_xor(arg, order) 
If std::atomic&lt;T&gt; has no fetch_xor member (this member is only provided for integral_types), the program is ill-formed. 

<h2>Parameters</h2>

obj - pointer to the atomic object to modify 
arg - the value to bitwise XOR to the value stored in the atomic object 
order - the memory synchronization ordering for this operation: all values are permitted.

<h2>Return value</h2>

The value immediately preceding the effects of this function in the modification_order of *obj. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;T atomic_fetch_xor( std::atomic&lt;T&gt;* obj, typename std::atomic&lt;T&gt;::value_type arg ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return obj-&gt;fetch_xor(arg); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
P0558R1 C++11 exact type match required because T is deduced from multiple arguments T is deduced from the atomic argument only 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically performs bitwise XOR between the argument and the value of the atomic object and obtains the value held previously 
fetch_xor <i>(public member function of std::atomic&lt;T&gt;)</i> 
atomic_fetch_or 
atomic_fetch_or_explicit replaces the atomic object with the result of bitwise OR with a non-atomic argument and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
atomic_fetch_and 
atomic_fetch_and_explicit replaces the atomic object with the result of bitwise AND with a non-atomic argument and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
