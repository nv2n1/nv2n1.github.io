---
title: "ck_pr_sub(3)"
name: "ck_pr_sub"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_sub/"
description: "ck_pr_sub_ptr ck_pr_sub_double ck_pr_sub_char ck_pr_sub_uint ck_pr_sub_int ck_pr_sub_64 ck_pr_sub_32 ck_pr_sub_16 ck_pr_sub_8 – atomic subtraction operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_sub_ptr</code> <code>ck_pr_sub_double</code> <code>ck_pr_sub_char</code> <code>ck_pr_sub_uint</code> <code>ck_pr_sub_int</code> <code>ck_pr_sub_64</code> <code>ck_pr_sub_32</code> <code>ck_pr_sub_16</code> <code>ck_pr_sub_8</code> &#8211; atomic subtraction operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_sub_ptr void *target uintptr_t delta Ft void Fn ck_pr_sub_double double *target double delta Ft void Fn ck_pr_sub_char char *target char delta Ft void Fn ck_pr_sub_uint unsigned int *target unsigned int delta Ft void Fn ck_pr_sub_int int *target int delta Ft void Fn ck_pr_sub_64 uint64_t *target uint64_t delta Ft void Fn ck_pr_sub_32 uint32_t *target uint32_t delta Ft void Fn ck_pr_sub_16 uint16_t *target uint16_t delta Ft void Fn ck_pr_sub_8 uint8_t *target uint8_t delta</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_sub 3 family of functions atomically subtract the value specified by Fa delta from the value pointed to by Fa target .</p>
<h2>RETURN VALUES</h2>
<p> This family of functions does not have a return value.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_load3, ck_pr_store3, ck_pr_fas3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
