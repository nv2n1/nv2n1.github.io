---
title: "stdpmrmemory_resourceis_equal(3)"
name: "stdpmrmemory_resourceis_equal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrmemory_resourceis_equal/"
description: "std::pmr::memory_resource::is_equal – std::pmr::memory_resource::is_equal"
---

<p>std::pmr::memory_resource::is_equal &#8211; std::pmr::memory_resource::is_equal</p>
<h2>Synopsis</h2>
<p>bool is_equal(const memory_resource&amp; other) const noexcept; <i>(since C++17)</i><br />
Compares *this for equality with other. Two memory_resources compare equal if and only if memory allocated from one memory_resource can be deallocated from the other and vice versa.<br />
Equivalent to return do_is_equal(other);. </p>
<h2>See also</h2>
<p>do_is_equal compare for equality with another memory_resource<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(virtual private member function)<br />
<code>[virtual]</code> </p>
