---
title: "ck_pr_fence_store_atomic(3)"
name: "ck_pr_fence_store_atomic"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_fence_store_atomic/"
description: "ck_pr_fence_store_atomic – enforce ordering of store operations to load operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_fence_store_atomic</code> &#8211; enforce ordering of store operations to load operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_fence_store_atomic void Ft void Fn ck_pr_fence_strict_store_atomic void</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_fence_store_atomic function enfores the ordering of any memory store, Fn ck_pr_store and atomic read-modify-write operations to atomic read-modify-write operations relative to the invocation of the function. This function always serve as an implicit compiler barrier. This functions will emit a fence for PSO and RMO targets. In order to force the emission of a fence use the Fn ck_pr_fence_strict_store_atomic function.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_pr.h&gt;
static int a = 0;
static int b = 0;
void function(void)
{
    ck_pr_store_int(&amp;a, 1);
    /*
     * Guarantee that the store to a is completed
     * with respect to the update of b.
     */
    ck_pr_fence_store_atomic();
    ck_pr_add_int(&amp;b, 2);
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_stall3, ck_pr_fence_atomic3, ck_pr_fence_atomic_store3, ck_pr_fence_atomic_load3, ck_pr_fence_load3, ck_pr_fence_load_atomic3, ck_pr_fence_load_store3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_store_load3, ck_pr_fence_memory3, ck_pr_barrier3, ck_pr_fas3, ck_pr_load3, ck_pr_store3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
