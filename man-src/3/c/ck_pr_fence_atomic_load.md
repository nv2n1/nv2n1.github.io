---
title: "ck_pr_fence_atomic_load(3)"
name: "ck_pr_fence_atomic_load"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_fence_atomic_load/"
description: "ck_pr_fence_atomic_load – enforce ordering of atomic read-modify-write operations to load operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_fence_atomic_load</code> &#8211; enforce ordering of atomic read-modify-write operations to load operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_fence_atomic_load void Ft void Fn ck_pr_fence_strict_atomic_load void</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_fence_atomic_load function enfores the ordering of any atomic read-modify-write operations relative to any load operations following the function invocation. This function always serve as an implicit compiler barrier. On architectures implementing CK_MD_TSO, this operation only serves as a compiler barrier and no fences are emitted. To force the unconditional emission of a fence, use Fn ck_pr_fence_strict_atomic_load .</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_pr.h&gt;
static int a = 0;
static int b = 0;
void function(void)
{
    int c;
    ck_pr_fas_int(&amp;a, 1);
    /*
     * Guarantee that the update to a is completed
     * with respect to the load of *b.
     */
    ck_pr_fence_atomic_load();
    c = ck_pr_load_int(&amp;b);
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_stall3, ck_pr_fence_atomic3, ck_pr_fence_atomic_store3, ck_pr_fence_store3, ck_pr_fence_load3, ck_pr_fence_load_atomic3, ck_pr_fence_load_store3, ck_pr_fence_load_depends3, ck_pr_fence_memory3, ck_pr_barrier3, ck_pr_fas3, ck_pr_load3, ck_pr_store3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
