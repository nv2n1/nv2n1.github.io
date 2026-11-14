---
title: "stdpmrmonotonic_buffer_resourcedo_deallocate(3)"
name: "stdpmrmonotonic_buffer_resourcedo_deallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrmonotonic_buffer_resourcedo_deallocate/"
description: "std::pmr::monotonic_buffer_resource::do_deallocate – std::pmr::monotonic_buffer_resource::do_deallocate"
---

<p>std::pmr::monotonic_buffer_resource::do_deallocate &#8211; std::pmr::monotonic_buffer_resource::do_deallocate</p>
<h2>Synopsis</h2>
<p>virtual void do_deallocate(void* p, std::size_t bytes, std::size_t alignment); <i>(since C++17)</i><br />
This function has no effect. Memory used by a monotonic_buffer_resource, as its name indicates, increases monotonically until the resource is destroyed. </p>
<h2>Exceptions</h2>
<p>Throws nothing.</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates memory<br />
deallocate <i>(public member function of std::pmr::memory_resource)</i><br />
do_deallocate deallocates memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(virtual private member function of std::pmr::memory_resource)<br />
<code>[virtual]</code> </p>
