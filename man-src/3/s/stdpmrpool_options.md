---
title: "stdpmrpool_options(3)"
name: "stdpmrpool_options"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpool_options/"
---

std::pmr::pool_options - std::pmr::pool_options

<h2>Synopsis</h2>

Defined in header &lt;memory_resource&gt; 
struct pool_options; <i>(since C++17)</i> 
std::pmr::pool_options is a set of constructor options for pool resources including std::pmr::synchronized_pool_resource and std::pmr::unsynchronized_pool_resource. 
Data members 
Member Meaning 
std::size_t max_blocks_per_chunk; The maximum number of blocks that will be allocated at once from the upstream std::pmr::memory_resource to replenish the pool. If the value of max_blocks_per_chunk is zero or is greater than an implementation-defined limit, that limit is used instead. The implementation may choose to use a smaller value than is specified in this field and may use different values for different pools. <pre><code>std::size_t                              The largest allocation size that is required to be fulfilled using the pooling mechanism. Attempts to allocate a single block larger than this threshold will be allocated directly from the upstream std::pmr::memory_resource. If largest_required_pool_block is zero or is greater than an implementation-defined limit, that limit is used instead. The implementation may choose a pass-through threshold larger than specified in this field.

largest_required_pool_block;



</code></pre>

<h2>See also</h2>

synchronized_pool_resource a thread-safe std::pmr::memory_resource for managing allocations in pools of different block sizes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 
unsynchronized_pool_resource a thread-unsafe std::pmr::memory_resource for managing allocations in pools of different block sizes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 
