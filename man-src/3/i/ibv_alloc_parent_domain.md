---
title: "ibv_alloc_parent_domain(3)"
name: "ibv_alloc_parent_domain"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_alloc_parent_domain/"
description: "ibv_alloc_parent_domain(), ibv_dealloc_pd() – allocate and deallocate the parent domain object"
---

<h2 class="name">NAME</h2>
<p> ibv_alloc_parent_domain(), ibv_dealloc_pd() &#8211; allocate and deallocate the parent domain object </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_pd *ibv_alloc_parent_domain(struct ibv_context *context, structibv_parent_domain_init_attr *attr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_alloc_parent_domain()</code> allocates a parent domain object for the RDMA device context <i>context</i>. </p>
<p> The parent domain object extends the normal protection domain with additional objects, such as a thread domain. </p>
<p> A parent domain is completely interchangeable with the <i>struct ibv_pd</i> used to create it, and can be used as an input argument to any function accepting a <i>struct ibv_pd.</i> </p>
<p> The behavior of each verb may be different if the verb is passed a parent domain <i>struct ibv_pd</i> that contains a <i>struct ibv_td pointer</i>. For instance the verb my choose to share resources between objects using the same thread domain. The exact behavior is provider dependent. </p>
<p> The <i>attr</i> argument specifies the following: </p>
<pre><code>
enum ibv_parent_domain_init_attr_mask {
    IBV_PARENT_DOMAIN_INIT_ATTR_ALLOCATORS = 1 &lt;&lt; 0,
    IBV_PARENT_DOMAIN_INIT_ATTR_PD_CONTEXT = 1 &lt;&lt; 1,
};
struct ibv_parent_domain_init_attr {
    struct ibv_pd *pd; /* referance to a protection domain, can't be NULL */
    struct ibv_td *td; /* referance to a thread domain, or NULL */
    uint32_t comp_mask;
    void *(*alloc)(struct ibv_pd *pd, void *pd_context, size_t size,
                   size_t alignment, uint64_t resource_type);
    void (*free)(struct ibv_pd *pd, void *pd_context, void *ptr,
                 uint64_t resource_type);
    void *pd_context;
};
</code></pre>
<p> <code>ibv_dealloc_pd()</code> will deallocate the parent domain as its exposed as an ibv_pd <i>pd</i>. All resources created with the parent domain should be destroyed prior to deallocating the parent domain.</p>
<h2>ARGUMENTS</h2>
<p> <code>pd</code> Reference to the protection domain that this parent domain uses. </p>
<p> <code>td</code> An optional thread domain that the parent domain uses. </p>
<p> <code>comp_mask</code> Bit-mask of optional fields in the ibv_parent_domain_init_attr struct. </p>
<p> <code>alloc</code> Custom memory allocation function for this parent domain. Provider memory allocations will use this function to allocate the needed memory. The allocation function is passed the parent domain <code>pd</code> and the user-specified context <code>pd_context.</code> In addition, the callback receives the <code>size</code> and the <code>alignment</code> of the requested buffer, as well a vendor-specific <code>resource_type</code> , which is derived from the rdma_driver_id enum (upper 32 bits) and a vendor specific resource code. The function returns the pointer to the allocated buffer, or NULL to designate an error. It may also return <code>IBV_ALLOCATOR_USE_DEFAULT</code> asking the callee to allocate the buffer using the default allocator. </p>
<p> The callback makes sure the allocated buffer is initialized with zeros. It is also the responsibility of the callback to make sure the memory cannot be COWed, e.g. by using madvise(MADV_DONTFORK) or by allocating anonymous shared memory. </p>
<p> <code>free</code> Callback to free memory buffers that were allocated using a successful alloc(). </p>
<p> <code>pd_context</code> A pointer for additional user-specific data to be associated with this parent domain. The pointer is passed back to the custom allocator functions.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_alloc_parent_domain()</code> returns a pointer to the allocated struct <i>ibv_pd</i> object, or NULL if the request fails (and sets errno to indicate the failure reason). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_parent_domain/">ibv_alloc_parent_domain</a></code>(3), <code><a href="/docs/linux/man/3-ibv_dealloc_pd/">ibv_dealloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_alloc_td/">ibv_alloc_td</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Alex Rosenbaum &lt;alexr [at] mellanox.com&gt;</p>
<dd>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
