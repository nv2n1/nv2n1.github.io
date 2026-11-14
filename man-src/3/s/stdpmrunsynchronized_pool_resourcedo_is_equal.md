---
title: "stdpmrunsynchronized_pool_resourcedo_is_equal(3)"
name: "stdpmrunsynchronized_pool_resourcedo_is_equal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrunsynchronized_pool_resourcedo_is_equal/"
description: "std::pmr::unsynchronized_pool_resource::do_is_equal – std::pmr::unsynchronized_pool_resource::do_is_equal"
---

<p>std::pmr::unsynchronized_pool_resource::do_is_equal &#8211; std::pmr::unsynchronized_pool_resource::do_is_equal</p>
<h2>Synopsis</h2>
<p>virtual bool do_is_equal(const std::pmr::memory_resource&amp; other) const noexcept; <i>(since C++17)</i><br />
Compare *this with other for identity &#8211; memory allocated using a unsynchronized_pool_resource can only be deallocated using that same resource. </p>
<h2>Return value</h2>
<p>this == &amp;other<br />
Defect report<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_3000 C++17 unnecessary dynamic_cast was performed removed </p>
<h2>See also</h2>
<p>do_is_equal compare for equality with another memory_resource<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(virtual private member function of std::pmr::memory_resource)<br />
<code>[virtual]</code> </p>
