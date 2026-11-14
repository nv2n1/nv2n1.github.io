---
title: "ck_pr_fence_memory(3)"
name: "ck_pr_fence_memory"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_fence_memory/"
description: "ck_pr_fence_memory – enforce partial ordering of all memory operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_fence_memory</code> &#8211; enforce partial ordering of all memory operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_fence_memory Ft void Fn ck_pr_fence_strict_memory</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_fence_memory 3 function enforces the ordering of any memory operations with respect to the invocation of the function. This function always serves as an implicit compiler barrier. Achitectures implementing CK_MD_TSO do not emit a barrier, but compiler barrier semantics remain. Architectures implementing CK_MD_PSO and CK_MD_RMO always emit an instructions which provides the specified ordering guarantees. To force the unconditional emission of a memory fence, use Fn ck_pr_fence_strict_memory .</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_pr.h&gt;
static int a = 0;
static int b;
static int c;
static int d;
void function(void)
{
    int snapshot_a;
    ck_pr_store_int(&amp;b, 1);
    snapshot_a = ck_pr_load_int(&amp;a);
    /*
     * Make sure previous memory operations are
     * ordered with respect to memory operations
     * following the ck_pr_fence_memory.
     */
    ck_pr_fence_memory();
    ck_pr_store_int(&amp;d, 3);
    ck_pr_store_int(&amp;c, 2);
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_stall3, ck_pr_fence_atomic3, ck_pr_fence_atomic_store3, ck_pr_fence_atomic_load3, ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_barrier3, ck_pr_fas3, ck_pr_load3, ck_pr_store3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
