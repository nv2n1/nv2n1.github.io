---
title: "stdpmrset_default_resource(3)"
name: "stdpmrset_default_resource"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrset_default_resource/"
---

std::pmr::set_default_resource - std::pmr::set_default_resource

<h2>Synopsis</h2>

Defined in header &lt;memory_resource&gt; 
std::pmr::memory_resource* set_default_resource(std::pmr::memory_resource* r) noexcept; <i>(since C++17)</i> 
If r is not null, sets the default memory resource pointer to r; otherwise, sets the default memory resource pointer to std::pmr::new_delete_resource(). 
The default memory resource pointer is used by certain facilities when an explicit memory resource is not supplied. The initial default memory resource pointer is the return value of std::pmr::new_delete_resource. 
This function is thread-safe. Every call to std::pmr::set_default_resource synchronizes with (see std::memory_order) the subsequent std::pmr::set_default_resource and std::pmr::get_default_resource calls. 

<h2>Return value</h2>

Returns the previous value of the default memory resource pointer. 

<h2>See also</h2>

get_default_resource gets the default std::pmr::memory_resource 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
new_delete_resource returns a static program-wide std::pmr::memory_resource that uses the global operator_new and operator_delete to allocate and deallocate memory 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
