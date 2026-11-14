---
title: "ck_pr_barrier(3)"
name: "ck_pr_barrier"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_barrier/"
description: "ck_pr_barrier – compiler optimization barrier"
---

<h2>NAME</h2>
<p> <code>ck_pr_barrier</code> &#8211; compiler optimization barrier</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_barrier void</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_barrier 3 function is used to disable code movement optimizations across the invocation of the function.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_fas3, ck_pr_load3, ck_pr_store3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
