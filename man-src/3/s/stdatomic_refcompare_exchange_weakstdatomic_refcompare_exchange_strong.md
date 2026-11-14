---
title: "stdatomic_refcompare_exchange_weakstdatomic_refcompare_exchange_strong(3)"
name: "stdatomic_refcompare_exchange_weakstdatomic_refcompare_exchange_strong"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refcompare_exchange_weakstdatomic_refcompare_exchange_strong/"
description: "std::atomic_ref<T>::compare_exchange_weak,std::atomic_ref<T>::compare_exchange_strong – std::atomic_ref<T>::compare_exchange_weak,std::atomic_ref<T>::compare_exchange_strong"
---

<p>std::atomic_ref&lt;T&gt;::compare_exchange_weak,std::atomic_ref&lt;T&gt;::compare_exchange_strong &#8211; std::atomic_ref&lt;T&gt;::compare_exchange_weak,std::atomic_ref&lt;T&gt;::compare_exchange_strong</p>
<h2>Synopsis</h2>
<pre><code>bool compare_exchange_weak(T &amp;expected, T desired,

                           std::memory_order success, (1)(since C++ 20)

                                                          std::memory_order failure) const noexcept;

bool compare_exchange_weak(T &amp;expected, T desired,

                           std::memory_order order = (2)(since C++ 20)

                               std::memory_order_seq_cst) const noexcept;

bool compare_exchange_strong(T &amp;expected, T desired,

                             std::memory_order success, (3)(since C++ 20)

                                                            std::memory_order failure) const noexcept;

bool compare_exchange_strong(T &amp;expected, T desired,

                             std::memory_order order = (4)(since C++ 20)

                                 std::memory_order_seq_cst) const noexcept;</code></pre>
<p>Atomically compares the value_representation of the referenced object with that of expected, and if those are bitwise-equal, replaces the former with desired (performs a read-modify-write operation). Otherwise, loads the actual value stored in the referenced object into expected (performs a load operation).<br />
The memory models for the read-modify-write and load operations are success and failure respectively. In the <code>(2)</code> and <code>(4)</code> versions order is used for both read-modify-write and load operations, except that std::memory_order_acquire and std::memory_order_relaxed are used for the load operation if order == std::memory_order_acq_rel, or order == std::memory_order_release respectively. </p>
<h2>Parameters</h2>
<p>expected &#8211; reference to the value expected to be found in the object referenced by the atomic_ref object<br />
desired &#8211; the value to store in the the referenced object if it is as expected<br />
success &#8211; the memory synchronization ordering for the read-modify-write operation if the comparison succeeds. All values are permitted.<br />
failure &#8211; the memory synchronization ordering for the load operation if the comparison fails. Cannot be std::memory_order_release or std::memory_order_acq_rel<br />
order &#8211; the memory synchronization ordering for both operations</p>
<h2>Return value</h2>
<p>true if the referenced object was successfully changed, false otherwise. </p>
<h2>Notes</h2>
<p>The comparison and copying are bitwise (similar to std::memcmp and std::memcpy); no constructor, assignment operator, or comparison operator are used.<br />
The weak forms (1-2) of the functions are allowed to fail spuriously, that is, act as if *this != expected even if they are equal. When a compare-and-exchange is in a loop, the weak version will yield better performance on some platforms.<br />
When a weak compare-and-exchange would require a loop and a strong one would not, the strong one is preferable unless the object representation of T may include trap bits, or offers multiple object representations for the same value (e.g. floating-point NaN). In those cases, weak compare-and-exchange typically works because it quickly converges on some stable object representation.<br />
For a union with bits that participate in the value representations of some members but not the others, compare-and-exchange might always fail because such padding bits have indeterminate values when they do not participate in the value representation of the active member.<br />
Padding bits that never participate in an object&#8217;s value representation are ignored. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
