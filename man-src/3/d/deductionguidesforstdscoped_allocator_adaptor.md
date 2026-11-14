---
title: "deductionguidesforstdscoped_allocator_adaptor(3)"
name: "deductionguidesforstdscoped_allocator_adaptor"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdscoped_allocator_adaptor/"
---

deductionguidesforstd::scoped_allocator_adaptor - deductionguidesforstd::scoped_allocator_adaptor
<h2>Synopsis</h2>Defined in header &lt;scoped_allocator&gt; 
template&lt;class OuterAlloc, class... InnerAllocs&gt; 
scoped_allocator_adaptor(OuterAlloc, InnerAllocs...) <i>(since C++17)</i> 
-&gt; scoped_allocator_adaptor&lt;OuterAllocator, InnerAllocs...&gt;; 

 
One deduction_guide is provided for std::scoped_allocator_adaptor to make it possible to deduce its outer allocator. 

<h2>Example</h2>&nbsp;This section is incomplete 
&nbsp;Reason: no example
