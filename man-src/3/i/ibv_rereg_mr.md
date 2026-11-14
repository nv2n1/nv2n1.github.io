---
title: "ibv_rereg_mr(3)"
name: "ibv_rereg_mr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_rereg_mr/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_rereg_mr - re-register a memory region (MR) 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_rereg_mr(struct ibv_mr *mr,
                 int flags,
                 struct ibv_pd *pd,
                 void *addr,
                 size_t length,
                 int access);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_rereg_mr() Modifies the attributes of an existing memory region (MR) mr. Conceptually, this call performs the functions deregister memory region followed by register memory region. Where possible, resources are reused instead of deallocated and reallocated. 

 flags is a bit-mask used to indicate which of the following properties of the memory region are being modified. Flags should be a combination (bit field) of:
<dl>
<dt>IBV_REREG_MR_CHANGE_TRANSLATION
<dd> Change translation (location and length)
<dt>IBV_REREG_MR_CHANGE_PD
<dd> Change protection domain
<dt>IBV_REREG_MR_CHANGE_ACCESS
<dd> Change access flags</dl>
 

 When IBV_REREG_MR_CHANGE_PD is used, pd represents the new PD this MR should be registered to. 

 When IBV_REREG_MR_CHANGE_TRANSLATION is used, addr. represents the virtual address (user-space pointer) of the new MR, while length represents its length. 

 The access and other flags are represented in the field access. This field describes the desired memory protection attributes; it is either 0 or the bitwise OR of one or more of ibv_access_flags.

<h2>RETURN VALUE</h2>

 

 ibv_rereg_mr() returns 0 on success, otherwise an error has occurred, enum ibv_rereg_mr_err_code represents the error as of below. 

 IBV_REREG_MR_ERR_INPUT - Old MR is valid, an input error was detected by libibverbs. 

 IBV_REREG_MR_ERR_DONT_FORK_NEW - Old MR is valid, failed via don't fork on new address range. 

 IBV_REREG_MR_ERR_DO_FORK_OLD - New MR is valid, failed via do fork on old address range. 

 IBV_REREG_MR_ERR_CMD - MR shouldn't be used, command error. 

 IBV_REREG_MR_ERR_CMD_AND_DO_FORK_NEW - MR shouldn't be used, command error, invalid fork state on new address range.

<h2>NOTES</h2>

 

 Even on a failure, the user still needs to call ibv_dereg_mr on this MR.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_dereg_mr/">ibv_dereg_mr</a>(3), <a HREF="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a>(3)

<h2>AUTHORS</h2>

 

 Matan Barak &lt;matanb [at] mellanox.com&gt;, Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


