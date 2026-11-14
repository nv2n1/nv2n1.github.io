---
title: "stdexperimentalpmrunsynchronized_pool_resourcerelease(3)"
name: "stdexperimentalpmrunsynchronized_pool_resourcerelease"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrunsynchronized_pool_resourcerelease/"
---

std::experimental::pmr::unsynchronized_pool_resource::release - std::experimental::pmr::unsynchronized_pool_resource::release

<h2>Synopsis</h2>

<pre><code>void release();
(library fundamentals TS)</code></pre> 
Releases all memory owned by this resource by calling the deallocate function of the upstream memory resource as needed. 
Memory is released back to the upstream resource even if deallocate has not been called for some of the allocated blocks. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates memory 
deallocate <i>(public member function of std::experimental::pmr::memory_resource)</i> 
