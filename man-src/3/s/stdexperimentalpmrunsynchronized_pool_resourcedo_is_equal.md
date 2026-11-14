---
title: "stdexperimentalpmrunsynchronized_pool_resourcedo_is_equal(3)"
name: "stdexperimentalpmrunsynchronized_pool_resourcedo_is_equal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrunsynchronized_pool_resourcedo_is_equal/"
description: "std::experimental::pmr::unsynchronized_pool_resource::do_is_equal – std::experimental::pmr::unsynchronized_pool_resource::do_is_equal"
---

<p>std::experimental::pmr::unsynchronized_pool_resource::do_is_equal &#8211; std::experimental::pmr::unsynchronized_pool_resource::do_is_equal</p>
<h2>Synopsis</h2>
<p>virtual bool do_is_equal(const memory_resource&amp; other) const noexcept; (library fundamentals TS)<br />
Compare *this with other for identity &#8211; memory allocated using a unsynchronized_pool_resource can only be deallocated using that same resource. </p>
<h2>Return value</h2>
<p>this == dynamic_cast&lt;const unsynchronized_pool_resource*&gt;(&amp;other) </p>
<h2>See also</h2>
<p>do_is_equal compare for equality with another memory_resource<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::experimental::pmr::memory_resource)</i><br />
<code>[virtual]</code> </p>
