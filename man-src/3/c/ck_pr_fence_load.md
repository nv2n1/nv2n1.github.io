---
title: "ck_pr_fence_load(3)"
name: "ck_pr_fence_load"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_fence_load/"
description: "ck_pr_fence_load – enforce partial ordering of load operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_fence_load</code> &#8211; enforce partial ordering of load operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_fence_load void Ft void Fn ck_pr_fence_strict_load void</p>
<h2>DESCRIPTION</h2>
<p> This function enforces the ordering of any memory load and Fn ck_pr_load 3 operations relative to the invocation of the function. Any store operations that were committed on remote processors and received by the calling processor before the invocation of Fn ck_pr_fence_load is also be made visible only after a call to Fn ck_pr_fence_load . This function always serves as an implicit compiler barrier. On architectures with CK_MD_TSO or CK_MD_PSO specified (total store ordering and partial store ordering respectively), this operation only serves as a compiler barrier and no fence instructions will be emitted. To force the unconditional emission of a load fence, use Fn ck_pr_fence_strict_load . Architectures implementing CK_MD_RMO always emit a load fence.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_pr.h&gt;
static unsigned int a;
static unsigned int b;
void function(void)
{
    unsigned int snapshot_a, snapshot_b;
    snapshot_a = ck_pr_load_uint(&amp;a);
    /*
     * Guarantee that the load from "a" completes
     * before the load from "b".
     */
    ck_pr_fence_load();
    snapshot_b = ck_pr_load_uint(&amp;b);
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_stall3, ck_pr_fence_atomic3, ck_pr_fence_atomic_store3, ck_pr_fence_atomic_load3, ck_pr_fence_load_atomic3, ck_pr_fence_load_store3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_barrier3, ck_pr_fas3, ck_pr_load3, ck_pr_store3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
