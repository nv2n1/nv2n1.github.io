---
title: "stdatomic_refis_lock_free(3)"
name: "stdatomic_refis_lock_free"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refis_lock_free/"
description: "std::atomic_ref<T>::is_lock_free – std::atomic_ref<T>::is_lock_free"
---

<p>std::atomic_ref&lt;T&gt;::is_lock_free &#8211; std::atomic_ref&lt;T&gt;::is_lock_free</p>
<h2>Synopsis</h2>
<p>bool is_lock_free() const noexcept; <i>(since C++20)</i><br />
Checks whether the atomic operations on this object are lock-free. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>true if the atomic operations on this object are lock-free, false otherwise. </p>
<h2>Notes</h2>
<p>All atomic types except for std::atomic_flag may be implemented using mutexes or other locking operations, rather than using the lock-free atomic CPU instructions. Atomic types are also allowed to be sometimes lock-free, e.g. if only aligned memory accesses are naturally atomic on a given architecture, misaligned objects of the same type have to use locks.<br />
The C++ standard recommends (but does not require) that lock-free atomic operations are also address-free, that is, suitable for communication between processes using shared memory. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>is_always_lock_free indicates that the type is always lock-free<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
