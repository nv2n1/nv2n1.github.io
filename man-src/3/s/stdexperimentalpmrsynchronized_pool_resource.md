---
title: "stdexperimentalpmrsynchronized_pool_resource(3)"
name: "stdexperimentalpmrsynchronized_pool_resource"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrsynchronized_pool_resource/"
description: "std::experimental::pmr::synchronized_pool_resource – std::experimental::pmr::synchronized_pool_resource"
---

<p>std::experimental::pmr::synchronized_pool_resource &#8211; std::experimental::pmr::synchronized_pool_resource</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/memory_resource&gt;<br />
class synchronized_pool_resource : public memory_resource; (library fundamentals TS)<br />
The class std::experimental::pmr::synchronized_pool_resource is a general-purpose memory resource class with the following properties:<br />
* It owns the allocated memory and frees it on destruction, even if deallocate has not been called for some of the allocated blocks.<br />
* It consists of a collection of pools that serves request for different block sizes. Each pool manages a collection of chunks that are then divided into blocks of uniform size.<br />
* Calls to do_allocate are dispatched to the pool serving the smallest blocks accommodating the requested size.<br />
* Exhausting memory in the pool causes the next allocation request for that pool to allocate an additional chunk of memory from the upstream allocator to replenish the pool. The chunk size obtained increases geometrically.<br />
* Allocations requests that exceed the largest block size are served from the upstream allocator directly.<br />
* The largest block size and maximum chunk size may be tuned by passing a std::experimental::pmr::pool_options struct to its constructor.<br />
synchronized_pool_resource may be accessed from multiple threads without external synchronization, and may have thread-specific pools to reduce synchronization costs. If the memory resource is only accessed from one thread, unsynchronized_pool_resource is more efficient. </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Constructs a synchronized_pool_resource<br />
constructor <i>(public member function)</i> </p>
<p>destructor Destroys a synchronized_pool_resource, releasing all allocated memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function)</i><br />
<code>[virtual]</code> </p>
<p>operator= Copy assignment operator is deleted. synchronized_pool_resource is not copy assignable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
[deleted]</p>
<h2>Public member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Release all allocated memory<br />
release <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Returns a pointer to the upstream memory resource<br />
upstream_resource <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Returns the options that control the pooling behavior of this resource<br />
options <i>(public member function)</i></p>
<h2>Protected member functions</h2>
<p>do_allocate Allocate memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
<p>do_deallocate Return memory to the pool<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
<p>do_is_equal Compare for equality with another memory_resource<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code></p>
