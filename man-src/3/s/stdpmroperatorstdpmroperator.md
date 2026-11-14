---
title: "stdpmroperatorstdpmroperator(3)"
name: "stdpmroperatorstdpmroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmroperatorstdpmroperator/"
---

std::pmr::operator==,std::pmr::operator!= - std::pmr::operator==,std::pmr::operator!=

<h2>Synopsis</h2>

<pre><code>bool operator==(const std::pmr::memory_resource &amp;a, (1)(since C++ 17)

                                                        const std::pmr::memory_resource &amp;b) noexcept;

bool operator!=(const std::pmr::memory_resource &amp;a, (2)(since C++ 17)

                                                        const std::pmr::memory_resource &amp;b) noexcept;</code></pre> 
Compares the memory_resources a and b for equality. Two memory_resources compare equal if and only if memory allocated from one memory_resource can be deallocated from the other and vice versa. 

<h2>Return value</h2>

1) &amp;a == &amp;b || a.is_equal(b) 
2) !(a == b) 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compare for equality with another memory_resource 
is_equal <i>(public member function)</i> 
