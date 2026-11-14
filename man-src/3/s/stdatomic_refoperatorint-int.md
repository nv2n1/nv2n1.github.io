---
title: "stdatomic_refoperatorint-int(3)"
name: "stdatomic_refoperatorint-int"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refoperatorint-int/"
description: "std::atomic_ref<T>::operator++,++(int),–,–(int) – std::atomic_ref<T>::operator++,++(int),–,–(int)"
---

<p>std::atomic_ref&lt;T&gt;::operator++,++(int),&#8211;,&#8211;(int) &#8211; std::atomic_ref&lt;T&gt;::operator++,++(int),&#8211;,&#8211;(int)</p>
<h2>Synopsis</h2>
<p>member only of atomic_ref&lt;Integral&gt; and atomic_ref&lt;T*&gt; template specializations<br />
value_type operator++() const noexcept; <code>(1)</code> <i>(since C++20)</i><br />
value_type operator++(int) const noexcept; <code>(2)</code> <i>(since C++20)</i><br />
value_type operator&#8211;() const noexcept; <code>(3)</code> <i>(since C++20)</i><br />
value_type operator&#8211;(int) const noexcept; <code>(4)</code> <i>(since C++20)</i> </p>
<pre><code>Atomically increments or decrements the current value of the referenced object. These operations are read-modify-write operations.

1) Performs atomic pre-increment. Equivalent to return fetch_add(1) + 1;.

2) Performs atomic post-increment. Equivalent to return fetch_add(1);.

3) Performs atomic pre-decrement. Equivalent to return fetch_sub(1) - 1;

4) Performs atomic post-decrement. Equivalent to return fetch_sub(1);
.

    For signed Integral types,
    arithmetic is defined to use two’s complement representation.There are no undefined results.

    For T *types,
    the result may be an undefined address, but the operations otherwise have no undefined behavior.The program is ill - formed if T is not an object type.
</code></pre>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1,3) The value of the referenced object after the modification.<br />
2,4) The value of the referenced object before the modification. </p>
<h2>Notes</h2>
<p>Unlike most pre-increment and pre-decrement operators, the pre-increment and pre-decrement operators for atomic_ref do not return a reference to the modified object. They return a copy of the stored value instead. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically adds the argument to the value stored in the referenced object and obtains the value held previously<br />
fetch_add <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically subtracts the argument from the value stored in the referenced object and obtains the value held previously<br />
fetch_sub <i>(public member function)</i> </p>
<pre><code>operator+=

operator-= atomically adds, subtracts, or performs bitwise AND, OR, XOR with the referenced value

operator&amp;= (public member function)

operator|=

operator^=




</code></pre>
