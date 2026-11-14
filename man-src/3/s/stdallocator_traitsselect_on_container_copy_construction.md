---
title: "stdallocator_traitsselect_on_container_copy_construction(3)"
name: "stdallocator_traitsselect_on_container_copy_construction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocator_traitsselect_on_container_copy_construction/"
---

std::allocator_traits&lt;Alloc&gt;::select_on_container_copy_construction - std::allocator_traits&lt;Alloc&gt;::select_on_container_copy_construction

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
static Alloc select_on_container_copy_construction( const Alloc&amp; a ); <i>(since C++11)</i> 
If possible, obtains the copy-constructed version of the allocator a, by calling a.select_on_container_copy_construction(). If the above is not possible (e.g. a does not have the member function select_on_container_copy_construction(), then returns a, unmodified. 
This function is called by the copy constructors of all standard library containers. It allows the allocator used by the constructor's argument to become aware that the container is being copied and modify state if necessary. 

<h2>Parameters</h2>

a - allocator used by a standard container passed as an argument to a container copy constructor

<h2>Return value</h2>

The allocator to use by the copy-constructed standard containers. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies the state of scoped_allocator_adaptor and all its allocators 
select_on_container_copy_construction <i>(public member function of std::scoped_allocator_adaptor&lt;OuterAlloc,InnerAlloc...&gt;)</i> 
