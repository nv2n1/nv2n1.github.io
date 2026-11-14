---
title: "ibv_advise_mr(3)"
name: "ibv_advise_mr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_advise_mr/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_advise_mr - Gives advice or directions to the kernel about an address range belongs to a memory region (MR). 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_advise_mr(struct ibv_pd *pd,
                  enum ibv_advise_mr_advice advice,
                  uint32_t flags,
                  struct ibv_sge *sg_list,
                  uint32_t num_sge)
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_advise_mr() Give advice or directions to the kernel about an address range belonging to a memory region (MR). Applications that are aware of future access patterns can use this verb in order to leverage this knowledge to improve system or application performance. 

 Conventional advice values
<dl>
<dt>IBV_ADVISE_MR_ADVICE_PREFETCH
<dd> Pre-fetch a range of an on-demand paging MR. Make pages present with read-only permission before the actual IO is conducted. This would provide a way to reduce latency by overlapping paging-in and either compute time or IO to other ranges.
<dt>IBV_ADVISE_MR_ADVICE_PREFETCH_WRITE
<dd> Like IBV_ADVISE_MR_ADVICE_PREFETCH but with read-access and write-access permission to the fetched memory.</dl>

<h2>ARGUMENTS</h2>

<dl>
<dt>pd
<dd> The protection domain (PD) associated with the MR.
<dt>advice
<dd> The requested advise value (as listed above).
<dt>flags
<dd> Describes the properties of the advise operation Conventional advice values IBV_ADVISE_MR_FLAG_FLUSH : Request to be a synchronized operation. Return to the caller after the operation is completed.
<dt>sg_list
<dd> Pointer to the s/g array When using IBV_ADVISE_OP_PREFETCH advise value, all the lkeys of all the scatter gather elements (SGEs) must be associated with ODP MRs (MRs that were registered with IBV_ACCESS_ON_DEMAND).
<dt>num_sge
<dd> Number of elements in the s/g array</dl>

<h2>RETURN VALUE</h2>

 

 ibv_advise_mr() returns 0 when the call was successful, or the value of errno on failure (which indicates the failure reason).
<dl>
<dt>EOPNOTSUPP
<dd> libibverbs or provider driver doesn't support the ibv_advise_mr() verb (ENOSYS may sometimes be returned by old versions of libibverbs).
<dt>ENOTSUP
<dd> The advise operation isn't supported.
<dt>EFAULT
<dd> In one of the following: o When the range requested is out of the MR bounds, or when parts of it are not part of the process address space. o One of the lkeys provided in the scatter gather list is invalid or with wrong write access.
<dt>EINVAL
<dd> In one of the following: o The PD is invalid. o The flags are invalid.</dl>

<h2>NOTES</h2>

 

 An application may pre-fetch any address range within an ODP MR when using the IBV_ADVISE_MR_ADVICE_PREFETCH or IBV_ADVISE_MR_ADVICE_PREFETCH_WRITE advice. Semantically, this operation is best-effort. That means the kernel does not guarantee that underlying pages are updated in the HCA or the pre-fetched pages would remain resident. 

 When using IBV_ADVISE_MR_ADVICE_PREFETCH or IBV_ADVISE_MR_ADVICE_PREFETCH_WRITE advice, the operation will be done in the following stages: o Page in the user pages to memory (pages aren't pinned). o Get the dma mapping of these user pages. o Post the underlying page translations to the HCA. 

 If IBV_ADVISE_MR_FLAG_FLUSH is specified then the underlying pages are guaranteed to be updated in the HCA before returning SUCCESS. Otherwise the driver can choose to postpone the posting of the new translations to the HCA. When performing a local RDMA access operation it is recommended to use IBV_ADVISE_MR_FLAG_FLUSH flag with one of the pre-fetch advices to increase probability that the pages translations are valid in the HCA and avoid future page faults.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a>(3), <a HREF="/docs/linux/man/3-ibv_rereg_mr/">ibv_rereg_mr</a>(3), <a HREF="/docs/linux/man/3-ibv_dereg_mr/">ibv_dereg_mr</a>(3)

<h2>AUTHOR</h2>

 

 Aviad Yehezkel &lt;aviadye [at] mellanox.com&gt; 

<h2>Index</h2>


