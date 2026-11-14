---
title: "pmix_constants(7)"
name: "pmix_constants"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pmix_constants/"
---

PMIx Constants

<h2>Synopsis</h2>

<pre><code>#include &lt;pmix_common.h&gt;</code></pre>

<h2>Overview</h2>

PMIx relies on the following types of constants: 

 Maximum Sizes : In order to minimize malloc performance penalties, PMIx utilizes constant-sized arrays wherever possible. These constants provide the user with the maximum size of the various array types. 

 Attributes : . 

 Errors : PMIx uses negative error constants, with 0 indicating &quot;success&quot;.

<h2>Maximum Sizes</h2>

The . 

 PMIX_MAX_NSLEN : The maximum length of a namespace. Note that any declaration of an array to hold a key string must include one extra space for the terminating NULL. 

 PMIX_MAX_KEYLEN : Maximum length of the key string used in structures such as the pmixinfo_t_. Note that any declaration of an array to hold a key string must include one extra space for the terminating NULL.

<h2>Attributes</h2>

Define a set of &quot;standard&quot; PMIx attributes that can be queried using the PMIx_Get function. Implementations (and users) are free to extend as desired - thus, functions calling PMIx_Get must be capable of handling the &quot;not found&quot; condition. Note that these are attributes of the system and the job as opposed to values the application (or underlying programming library) might choose to expose - i.e., they are values provided by the resource manager as opposed to the application. Thus, these keys are RESERVED for use by PMIx, and users should avoid defining any attribute starting with the keyword PMIX. 

 A list of the current PMIx attributes, and the type of their associated data value, is provided here. 

 PMIX_ATTR_UNDEF (NULL) : Used to initialize an attribute field, indicating that the attribute has not yet been assigned. 

 PMIX_USERID (uint32_t) : . 

 PMIX_GRPID (uint32_t) : An access domain represents a single logical connection into a fabric. It may map to a single physical or virtual NIC or a port. An access domain defines the boundary across which fabric resources may be associated. Each access domain belongs to a single fabric domain. 

 PMIX_CPUSET (char*) : .

<h2>Error Constants</h2>

. 

 PMIX_SUCCESS : Indicates that the operation was successful. 

 PMIX_ERROR : A general error code - an error occurred, but no specific reason can be provided. 

 fi_rma - Remote Memory Access : RMA transfers are one-sided operations that read or write data directly to a remote memory region. Other than defining the appropriate memory region, RMA operations do not require interaction at the target side for the data transfer to complete. 

 fi_atomic - Atomic : Atomic operations can perform one of several operations on a remote memory region. Atomic operations include well-known functionality, such as atomic-add and compare-and-swap, plus several other pre-defined calls. Unlike other data transfer interfaces, atomic operations are aware of the data formatting at the target memory region.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-pmix/">pmix</a>(7)

<h2>Authors</h2>

PMIx.
