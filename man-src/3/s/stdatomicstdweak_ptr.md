---
title: "stdatomicstdweak_ptr(3)"
name: "stdatomicstdweak_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicstdweak_ptr/"
description: "std::atomic(std::weak_ptr) – std::atomic(std::weak_ptr)"
---

<p>std::atomic(std::weak_ptr) &#8211; std::atomic(std::weak_ptr)</p>
<h2>Synopsis</h2>
<p>template &lt;class T&gt; struct std::atomic&lt;std::weak_ptr&lt;T&gt;&gt;; <i>(since C++20)</i><br />
The partial template specialization of std::atomic for std::weak_ptr&lt;T&gt; allows users to manipulate weak_ptr objects atomically.<br />
If multiple threads of execution access the same std::weak_ptr object without synchronization and any of those accesses uses a non-const member function of weak_ptr then a data race will occur unless all such access is performed through an instance of std::atomic&lt;std::weak_ptr&gt;&gt;.<br />
Associated use_count increments are guaranteed to be part of the atomic operation. Associated use_count decrements are sequenced after the atomic operation, but are not required to be part of it, except for the use_count change when overriding expected in a failed CAS. Any associated deletion and deallocation are sequenced after the atomic update step and are not part of the atomic operation.<br />
Note that the control block used by std::weak_ptr and std::shared_ptr is thread-safe: different non-atomic std::weak_ptr objects can be accessed using mutable operations, such as operator= or reset, simultaneously by multiple threads, even when these instances are copies or otherwise share the same control block internally.<br />
The type T may be an incomplete type. </p>
<h2>Member types</h2>
<p>Member type Definition<br />
value_type std::weak_ptr&lt;T&gt;</p>
<h2>Member functions</h2>
<p>All non-specialized std::atomic functions are also provided by this specialization, and no additional member functions. </p>
<p>&nbsp;atomic&lt;weak_ptr&lt;T&gt;&gt;::atomic </p>
<p>constexpr atomic() noexcept = default; <code>(1)</code><br />
atomic(std::weak_ptr&lt;T&gt; desired) noexcept; <code>(2)</code><br />
atomic(const atomic&amp;) = delete; <code>(3)</code> </p>
<p>1) Initializes the underlying weak_ptr&lt;T&gt; to default-constructed value<br />
2) Initializes the underlying weak_ptr&lt;T&gt; to a copy of desired. As with any std::atomic type, initialization is not an atomic operation.<br />
3) Atomic types are not copy/move constructible </p>
<p>&nbsp;atomic&lt;weak_ptr&lt;T&gt;&gt;::operator= </p>
<p>void operator=(const atomic&amp;) = delete; <code>(1)</code><br />
void operator=(std::weak_ptr&lt;T&gt; desired) noexcept; <code>(2)</code> </p>
<p>1) Atomic types are not copy/move assignable<br />
2) Value assignment, equivalent to store(desired) </p>
<p>&nbsp;atomic&lt;weak_ptr&lt;T&gt;&gt;::is_lock_free </p>
<p>bool is_lock_free() const noexcept; </p>
<p>Returns true if the atomic operations on all objects of this type are lock-free, false otherwise. </p>
<p>&nbsp;atomic&lt;weak_ptr&lt;T&gt;&gt;::store </p>
<p>void store(std::weak_ptr&lt;T&gt; desired,<br />
std::memory_order order = std::memory_order_seq_cst) noexcept; </p>
<p>Atomically replaces the value of *this with the value of desired as if by p.swap(desired) where p is the underlying std::weak_ptr&lt;T&gt;. Memory is ordered according to order. The behavior is undefined if order is std::memory_order_consume, std::memory_order_acquire, or std::memory_order_acq_rel </p>
<p>&nbsp;atomic&lt;weak_ptr&lt;T&gt;&gt;::load </p>
<p>std::weak_ptr&lt;T&gt; load(std::memory_order order = std::memory_order_seq_cst) const noexcept; </p>
<p>Atomically returns a copy of the underlying std::weak_ptr&lt;T&gt;. Memory is ordered according to order. The behavior is undefined if order is std::memory_order_release or std::memory_order_acq_rel. </p>
<p>&nbsp;atomic&lt;weak_ptr&lt;T&gt;&gt;::operator std::weak_ptr&lt;T&gt; </p>
<p>operator std::weak_ptr&lt;T&gt;() const noexcept; </p>
<p>Equivalent to return load(); </p>
<p>&nbsp;atomic&lt;weak_ptr&lt;T&gt;&gt;::exchange </p>
<p>std::weak_ptr&lt;T&gt; exchange(std::weak_ptr&lt;T&gt; desired,<br />
std::memory_order order = std::memory_order_seq_cst) noexcept; </p>
<p>Atomically replaces the underlying std::weak_ptr&lt;T&gt; with desired as if by p.swap(desired) where p is the underlying std::weak_ptr&lt;T&gt;, and returns a copy of the value that p had immediately before the swap. Memory is ordered according to order. This is an atomic read-modify-write operation. </p>
<p>&nbsp;atomic&lt;weak_ptr&lt;T&gt;&gt;::compare_exchange_weak, compare_exchange_strong </p>
<p>bool compare_exchange_strong(std::weak_ptr&lt;T&gt;&amp; expected, std::weak_ptr&lt;T&gt; desired, <code>(1)</code><br />
std::memory_order success, std::memory_order failure) noexcept;<br />
bool compare_exchange_weak(std::weak_ptr&lt;T&gt;&amp; expected, std::weak_ptr&lt;T&gt; desired, <code>(2)</code><br />
std::memory_order success, std::memory_order failure) noexcept;<br />
bool compare_exchange_strong(std::weak_ptr&lt;T&gt;&amp; expected, std::weak_ptr&lt;T&gt; desired, <code>(3)</code><br />
std::memory_order order = std::memory_order_seq_cst) noexcept;<br />
bool compare_exchange_weak(std::weak_ptr&lt;T&gt;&amp; expected, std::weak_ptr&lt;T&gt; desired, <code>(4)</code><br />
std::memory_order order = std::memory_order_seq_cst) noexcept; </p>
<p>1) If the underlying std::weak_ptr&lt;T&gt; stores the same pointer value as expected and shares ownership with it, or if both underlying and expected are empty, assigns from desired to the underlying std::weak_ptr&lt;T&gt;, returns true, and orders memory according to success, otherwise assigns from the underlying std::weak_ptr&lt;T&gt; to expected, returns false, and orders memory according to failure. The behavior is undefined if failure is std::memory_order_release or std::memory_order_acq_rel. On success, the operation is an atomic read-modify-write operation on *this and expected is not accessed after the atomic update. On failure, the operation is an atomic load operation on *this and expected is updated with the existing value read from the atomic object. This update to expected&#8217;s use_count is part of this atomic operation, although the write itself (and any subsequent deallocation/destruction) is not required to be.<br />
2) Same as <code>(1)</code>, but may also fail spuriously.<br />
3) Equivalent to: return compare_exchange_strong(expected, desired, order, fail_order);, where fail_order is the same as order except that std:memory_order_acq_rel is replaced by std::memory_order_acquire and std::memory_order_release is replaced by std::memory_order_relaxed.<br />
4) Equivalent to: return compare_exchange_weak(expected, desired, order, fail_order); where fail_order is the same as order except that std::memory_order_acq_rel is replaced by std::memory_order_acquire and std::memory_order_release is replaced by std::memory_order_relaxed.</p>
<h2>Member constants</h2>
<p>The only standard std::atomic member constant is_always_lock_free is also provided by this specialization. </p>
<p>&nbsp;atomic&lt;weak_ptr&lt;T&gt;&gt;::is_always_lock_free </p>
<p>static constexpr bool is_always_lock_free = /*implementation-defined*/;</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>atomic atomic class template and specializations for bool, integral, and pointer types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
