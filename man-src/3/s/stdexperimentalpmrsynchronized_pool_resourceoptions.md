---
title: "stdexperimentalpmrsynchronized_pool_resourceoptions(3)"
name: "stdexperimentalpmrsynchronized_pool_resourceoptions"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrsynchronized_pool_resourceoptions/"
---

std::experimental::pmr::synchronized_pool_resource::options - std::experimental::pmr::synchronized_pool_resource::options

<h2>Synopsis</h2>

pool_options options() const; (library fundamentals TS) 
Returns the options that controls the pooling behavior of this resource. 
The values in the returned struct may differ from those supplied to the constructor in the following ways: 
* Values of zero will be replaced with implementation-specified defaults; 
* Sizes may be rounded to an unspecified granularity. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Constructs a synchronized_pool_resource 
constructor <i>(public member function)</i> 
