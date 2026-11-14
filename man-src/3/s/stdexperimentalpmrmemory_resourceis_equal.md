---
title: "stdexperimentalpmrmemory_resourceis_equal(3)"
name: "stdexperimentalpmrmemory_resourceis_equal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrmemory_resourceis_equal/"
---

std::experimental::pmr::memory_resource::is_equal - std::experimental::pmr::memory_resource::is_equal

<h2>Synopsis</h2>

bool is_equal(const memory_resource&amp; other) const noexcept; (library fundamentals TS) 
Compares *this for equality with other. Two memory_resources compare equal if and only if memory allocated from one memory_resource can be deallocated from the other and vice versa. 
Equivalent to return do_is_equal(other);. 

<h2>See also</h2>

do_is_equal compare for equality with another memory_resource 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i> 
<b>[virtual]</b> 
