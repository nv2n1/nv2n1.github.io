---
title: "stdatomicoperatorint-int(3)"
name: "stdatomicoperatorint-int"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicoperatorint-int/"
description: "std::atomic<T>::operator++,++(int),–,–(int) – std::atomic<T>::operator++,++(int),–,–(int)"
---

<p>std::atomic&lt;T&gt;::operator++,++(int),&#8211;,&#8211;(int) &#8211; std::atomic&lt;T&gt;::operator++,++(int),&#8211;,&#8211;(int)</p>
<h2>Synopsis</h2>
<p>T operator++() noexcept; <code>(1)</code> (member only of atomic&lt;Integral&gt; template specialization)<br />
T operator++() volatile noexcept; <i>(since C++11)</i><br />
T* operator++() noexcept; <code>(1)</code> (member only of atomic&lt;T*&gt; template specialization)<br />
T* operator++() volatile noexcept; <i>(since C++11)</i><br />
T operator++( int ) noexcept; <code>(2)</code> (member only of atomic&lt;Integral&gt; template specialization)<br />
T operator++( int ) volatile noexcept; <i>(since C++11)</i><br />
T* operator++( int ) noexcept; <code>(2)</code> (member only of atomic&lt;T*&gt; template specialization)<br />
T* operator++( int ) volatile noexcept; <i>(since C++11)</i><br />
T operator&#8211;() noexcept; <code>(3)</code> (member only of atomic&lt;Integral&gt; template specialization)<br />
T operator&#8211;() volatile noexcept; <i>(since C++11)</i><br />
T* operator&#8211;() noexcept; <code>(3)</code> (member only of atomic&lt;T*&gt; template specialization)<br />
T* operator&#8211;() volatile noexcept; <i>(since C++11)</i><br />
T operator&#8211;( int ) noexcept; <code>(4)</code> (member only of atomic&lt;Integral&gt; template specialization)<br />
T operator&#8211;( int ) volatile noexcept; <i>(since C++11)</i><br />
T* operator&#8211;( int ) noexcept; <code>(4)</code> (member only of atomic&lt;T*&gt; template specialization)<br />
T* operator&#8211;( int ) volatile noexcept; <i>(since C++11)</i><br />
Atomically increments or decrements the current value. The operation is read-modify-write operation.<br />
1) Performs atomic pre-increment. Equivalent to <a href="/docs/linux/man/1-fetch_add/">fetch_add</a><code>(1)</code>+1.<br />
2) Performs atomic post-increment. Equivalent to <a href="/docs/linux/man/1-fetch_add/">fetch_add</a><code>(1)</code>.<br />
3) Performs atomic pre-decrement. Equivalent to <a href="/docs/linux/man/1-fetch_sub/">fetch_sub</a><code>(1)</code>-1<br />
4) Performs atomic post-decrement. Equivalent to <a href="/docs/linux/man/1-fetch_sub/">fetch_sub</a><code>(1)</code>.<br />
For signed Integral types, arithmetic is defined to use two’s complement representation. There are no undefined results.<br />
For T* types, the result may be an undefined address, but the operations otherwise have no undefined behavior. The program is ill-formed if T is not an object type. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1,3) The value of the atomic variable after the modification. Formally, the result of incrementing/decrementing the value immediately preceding the effects of this function in the modification_order of *this.<br />
2,4) The value of the atomic variable before the modification. Formally, the value immediately preceding the effects of this function in the modification_order of *this. </p>
<h2>Notes</h2>
<p>Unlike most pre-increment and pre-decrement operators, the pre-increment and pre-decrement operators for atomic types do not return a reference to the modified object. They return a copy of the stored value instead.<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
P0558R1 C++11 arithmetic permitted on pointers to cv void or function made ill-formed </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically adds the argument to the value stored in the atomic object and obtains the value held previously<br />
fetch_add <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically subtracts the argument from the value stored in the atomic object and obtains the value held previously<br />
fetch_sub <i>(public member function)</i> </p>
<pre><code>operator+=

operator-= adds, subtracts, or performs bitwise AND, OR, XOR with the atomic value

operator&amp;= (public member function)

operator|=

operator^=




</code></pre>
