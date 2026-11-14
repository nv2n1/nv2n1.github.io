---
title: "stdexperimentalpmrset_default_resource(3)"
name: "stdexperimentalpmrset_default_resource"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrset_default_resource/"
---

std::experimental::pmr::set_default_resource - std::experimental::pmr::set_default_resource

<h2>Synopsis</h2>

Defined in header &lt;experimental/memory_resource&gt; 
memory_resource* set_default_resource(memory_resource* r) noexcept; (library fundamentals TS) 
If r is not null, sets the default memory resource pointer to r; otherwise, sets the default memory resource pointer to new_delete_resource(). 
The default memory resource pointer is used by certain facilities when an explicit memory resource is not supplied. The initial default memory resource pointer is the return value of new_delete_resource(). 
This function is thread-safe. Every call to set_default_resource synchronizes with (see std::memory_order) the subsequent set_default_resource and get_default_resource calls. 

<h2>Return value</h2>

Returns the previous value of the default memory resource pointer. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets the default memory_resource 
get_default_resource <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a static program-wide memory_resource that uses the global operator_new and operator_delete to allocate and deallocate memory 
new_delete_resource <i>(function)</i> 
