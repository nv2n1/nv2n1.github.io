---
title: "ck_pr_store(3)"
name: "ck_pr_store"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_store/"
description: "ck_pr_store_ptr ck_pr_store_double ck_pr_store_uint ck_pr_store_int ck_pr_store_char ck_pr_store_64 ck_pr_store_32 ck_pr_store_16 ck_pr_store_8 – atomic volatile store operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_store_ptr</code> <code>ck_pr_store_double</code> <code>ck_pr_store_uint</code> <code>ck_pr_store_int</code> <code>ck_pr_store_char</code> <code>ck_pr_store_64</code> <code>ck_pr_store_32</code> <code>ck_pr_store_16</code> <code>ck_pr_store_8</code> &#8211; atomic volatile store operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_store_ptr void *target void *value Ft void Fn ck_pr_store_double double *target double value Ft void Fn ck_pr_store_uint unsigned int *target unsigned int value Ft void Fn ck_pr_store_int int *target int value Ft void Fn ck_pr_store_char char *target char value Ft void Fn ck_pr_store_64 uint64_t *target uint64_t value Ft void Fn ck_pr_store_32 uint32_t *target uint32_t value Ft void Fn ck_pr_store_16 uint16_t *target uint16_t value Ft void Fn ck_pr_store_8 uint8_t *target uint8_t value</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_store 3 family of functions atomically stores the value specified by Fa value into the location pointed to by Fa target . This family of functions always serves as an implicit compiler barrier and is not susceptible to compiler re-ordering.</p>
<h2>RETURN VALUES</h2>
<p> This family of functions has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_add3, ck_pr_load3, ck_pr_fas3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
