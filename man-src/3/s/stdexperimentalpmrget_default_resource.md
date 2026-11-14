---
title: "stdexperimentalpmrget_default_resource(3)"
name: "stdexperimentalpmrget_default_resource"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrget_default_resource/"
---

std::experimental::pmr::get_default_resource - std::experimental::pmr::get_default_resource

<h2>Synopsis</h2>

Defined in header &lt;experimental/memory_resource&gt; 
memory_resource* get_default_resource() noexcept; (library fundamentals TS) 
Gets the default memory resource pointer. 
The default memory resource pointer is used by certain facilities when an explicit memory resource is not supplied. The initial default memory resource pointer is the return value of new_delete_resource(). 
This function is thread-safe. Previous call to set_default_resource synchronizes with (see std::memory_order) the subsequent get_default_resource calls. 

<h2>Return value</h2>

Returns the value of the default memory resource pointer. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the default memory_resource 
set_default_resource <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a static program-wide memory_resource that uses the global operator_new and operator_delete to allocate and deallocate memory 
new_delete_resource <i>(function)</i> 
