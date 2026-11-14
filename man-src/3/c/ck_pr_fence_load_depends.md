---
title: "ck_pr_fence_load_depends(3)"
name: "ck_pr_fence_load_depends"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_fence_load_depends/"
description: "ck_pr_fence_load_depends – data dependency barrier"
---

<h2>NAME</h2>
<p> <code>ck_pr_fence_load_depends</code> &#8211; data dependency barrier</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_fence_load_depends void</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_fence_load_depends 3 emits necessary fences for pure data-dependent loads. It currently only serves as a compiler barrier for Concurrency Kit&#8217;s supported platforms. Unless you&#8217;re on architecture which re-orders data-dependent loads (such as the defunct Alpha), this function is unnecessary.</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_stall3, ck_pr_fence_atomic3, ck_pr_fence_atomic_store3, ck_pr_fence_atomic_load3, ck_pr_fence_load3, ck_pr_fence_load_atomic3, ck_pr_fence_load_store3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_barrier3, ck_pr_fas3, ck_pr_load3, ck_pr_store3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
