---
title: "stdpmrpolymorphic_allocatorpolymorphic_allocator(3)"
name: "stdpmrpolymorphic_allocatorpolymorphic_allocator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatorpolymorphic_allocator/"
---

std::pmr::polymorphic_allocator&lt;T&gt;::polymorphic_allocator - std::pmr::polymorphic_allocator&lt;T&gt;::polymorphic_allocator

<h2>Synopsis</h2>

<pre><code>polymorphic_allocator() noexcept;
(1)

    polymorphic_allocator(const polymorphic_allocator &amp;other) = default;
(2)

    template &lt;class U&gt;
    (3)

        polymorphic_allocator(const polymorphic_allocator&lt;U&gt; &amp;other) noexcept;

polymorphic_allocator(memory_resource *r);                              (4)
Constructs a new polymorphic_allocator.

1) Constructs a polymorphic_allocator using the return value of std::pmr::get_default_resource() as the underlying memory resource.

2-3) Constructs a polymorphic_allocator using other.resource() as the underlying memory resource.

4) Constructs a polymorphic_allocator using r as the underlying memory resource. This constructor provides an implicit conversion from memory_resource*.
</code></pre>

<h2>Parameters</h2>

other - another polymorphic_allocator to copy from 
r - pointer to the memory resource to use. May not be null.

<h2>Exceptions</h2>

4) Throws nothing.

<h2>Notes</h2>

Copying a container using a polymorphic_allocator will not call the allocator's copy constructor. Instead, the new container will use the return value of select_on_container_copy_construction (a default-constructed polymorphic_allocator) as its allocator. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Create a new polymorphic_allocator for use by a container's copy constructor 
select_on_container_copy_construction <i>(public member function)</i> 
