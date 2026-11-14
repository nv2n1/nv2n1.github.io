---
title: "ck_pr_not(3)"
name: "ck_pr_not"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_not/"
description: "ck_pr_not_ptr ck_pr_not_double ck_pr_not_char ck_pr_not_uint ck_pr_not_int ck_pr_not_64 ck_pr_not_32 ck_pr_not_16 ck_pr_not_8 – atomic complement operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_not_ptr</code> <code>ck_pr_not_double</code> <code>ck_pr_not_char</code> <code>ck_pr_not_uint</code> <code>ck_pr_not_int</code> <code>ck_pr_not_64</code> <code>ck_pr_not_32</code> <code>ck_pr_not_16</code> <code>ck_pr_not_8</code> &#8211; atomic complement operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_not_ptr void *target Ft void Fn ck_pr_not_double double *target Ft void Fn ck_pr_not_char char *target Ft void Fn ck_pr_not_uint unsigned int *target Ft void Fn ck_pr_not_int int *target Ft void Fn ck_pr_not_64 uint64_t *target Ft void Fn ck_pr_not_32 uint32_t *target Ft void Fn ck_pr_not_16 uint16_t *target Ft void Fn ck_pr_not_8 uint8_t *target</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_not 3 family of functions atomically complement the value pointed to by Fa target .</p>
<h2>RETURN VALUES</h2>
<p> These functions have no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_load3, ck_pr_store3, ck_pr_fas3, ck_pr_faa3, ck_pr_inc3, ck_pr_not3, ck_pr_neg3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
