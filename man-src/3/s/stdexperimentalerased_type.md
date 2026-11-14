---
title: "stdexperimentalerased_type(3)"
name: "stdexperimentalerased_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalerased_type/"
---

std::experimental::erased_type - std::experimental::erased_type

<h2>Synopsis</h2>

Defined in header &lt;experimental/utility&gt; 
struct erased_type { }; (library fundamentals TS) 
The struct erased_type is an empty struct that serves as a placeholder for a type in situations where the actual type is determined at runtime. For example, in classes that use type-erased_allocators, the nested typedef allocator_type is an alias for erased_type. 
