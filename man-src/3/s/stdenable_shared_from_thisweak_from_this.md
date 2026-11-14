---
title: "stdenable_shared_from_thisweak_from_this(3)"
name: "stdenable_shared_from_thisweak_from_this"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdenable_shared_from_thisweak_from_this/"
description: "std::enable_shared_from_this<T>::weak_from_this – std::enable_shared_from_this<T>::weak_from_this"
---

<p>std::enable_shared_from_this&lt;T&gt;::weak_from_this &#8211; std::enable_shared_from_this&lt;T&gt;::weak_from_this</p>
<h2>Synopsis</h2>
<p>std::weak_ptr&lt;T&gt; weak_from_this() noexcept; <code>(1)</code> <i>(since C++17)</i><br />
std::weak_ptr&lt;T const&gt; weak_from_this() const noexcept; <code>(2)</code> <i>(since C++17)</i><br />
Returns a std::weak_ptr&lt;T&gt; that tracks ownership of *this by all existing std::shared_ptr that refer to *this. </p>
<h2>Notes</h2>
<p>This is a copy of the the private mutable weak_ptr member that is part of enable_shared_from_this. </p>
<h2>Return value</h2>
<p>std::weak_ptr&lt;T&gt; that shares ownership of *this with pre-existing std::shared_ptrs </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>shared_ptr smart pointer with shared object ownership semantics<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
