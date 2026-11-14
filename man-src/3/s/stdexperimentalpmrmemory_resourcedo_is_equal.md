---
title: "stdexperimentalpmrmemory_resourcedo_is_equal(3)"
name: "stdexperimentalpmrmemory_resourcedo_is_equal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrmemory_resourcedo_is_equal/"
---

std::experimental::pmr::memory_resource::do_is_equal - std::experimental::pmr::memory_resource::do_is_equal

<h2>Synopsis</h2>

<pre><code>virtual bool is_equal(const memory_resource &amp;other) const noexcept = 0;
(library fundamentals TS)</code></pre> 
Compares *this for equality with other. 
Two memory_resources compare equal if and only if memory allocated from one memory_resource can be deallocated from the other and vice versa. 

<h2>Notes</h2>

The most-derived type of other may not match the most derived type of *this. A derived class implementation therefore must typically check whether the most derived types of *this and other match using dynamic_cast, and immediately return false if the cast fails. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compare for equality with another memory_resource 
is_equal <i>(public member function)</i> 
