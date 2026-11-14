---
title: "stdexperimentalpmrmemory_resourcedeallocate(3)"
name: "stdexperimentalpmrmemory_resourcedeallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrmemory_resourcedeallocate/"
description: "std::experimental::pmr::memory_resource::deallocate – std::experimental::pmr::memory_resource::deallocate"
---

<p>std::experimental::pmr::memory_resource::deallocate &#8211; std::experimental::pmr::memory_resource::deallocate</p>
<h2>Synopsis</h2>
<pre><code>void *deallocate(void *p, std::size_t bytes, std::size_t alignment = alignof(std::max_align_t));
(library fundamentals TS)
    Deallocates the storage pointed to by p.p shall have been returned by a prior call to allocate(bytes, alignment)
on a memory_resource that compares equal to *this, and the storage it points to shall not yet have been deallocated.

                                                       Equivalent to return do_deallocate(p, bytes, alignment);
.
</code></pre>
<h2>Exceptions</h2>
<p>Throws nothing.</p>
<h2>See also</h2>
<p>do_deallocate deallocates memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
