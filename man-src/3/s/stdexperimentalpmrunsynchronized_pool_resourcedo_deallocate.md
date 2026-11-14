---
title: "stdexperimentalpmrunsynchronized_pool_resourcedo_deallocate(3)"
name: "stdexperimentalpmrunsynchronized_pool_resourcedo_deallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrunsynchronized_pool_resourcedo_deallocate/"
description: "std::experimental::pmr::unsynchronized_pool_resource::do_deallocate – std::experimental::pmr::unsynchronized_pool_resource::do_deallocate"
---

<p>std::experimental::pmr::unsynchronized_pool_resource::do_deallocate &#8211; std::experimental::pmr::unsynchronized_pool_resource::do_deallocate</p>
<h2>Synopsis</h2>
<p>virtual void do_deallocate(void* p, std::size_t bytes, std::size_t alignment); (library fundamentals TS)<br />
Returns the memory at p to the pool. It is unspecified if or under what circumstances this operation will result in a call to deallocate() on the upstream memory resource. </p>
<h2>Exceptions</h2>
<p>Throws nothing.</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates memory<br />
deallocate <i>(public member function of std::experimental::pmr::memory_resource)</i><br />
do_deallocate deallocates memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::experimental::pmr::memory_resource)</i><br />
<code>[virtual]</code> </p>
