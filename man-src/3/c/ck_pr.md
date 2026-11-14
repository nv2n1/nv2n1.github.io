---
title: "ck_pr(3)"
name: "ck_pr"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr/"
description: "ck_pr – concurrency primitives interface"
---

<h2>NAME</h2>
<p> <code>ck_pr</code> &#8211; concurrency primitives interface</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h</p>
<h2>DESCRIPTION</h2>
<p> ck_pr.h provides an interface to volatile atomic instructions, memory barriers and busy-wait facilities as provided by the underlying processor. The presence of an atomic operation is detected by the presence of a corresponding CK_F_PR macro. For example, the availability of ck_pr_add_163 would be determined by the presence of CK_F_PR_ADD_16.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_stall3, ck_pr_fence_acquire3, ck_pr_fence_release3, ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_barrier3, ck_pr_fas3, ck_pr_load3, ck_pr_store3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
