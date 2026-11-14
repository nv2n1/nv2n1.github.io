---
title: "ck_pr_dec(3)"
name: "ck_pr_dec"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_dec/"
description: "ck_pr_dec_ptr ck_pr_dec_ptr_zero ck_pr_dec_double ck_pr_dec_double_zero ck_pr_dec_char ck_pr_dec_char_zero ck_pr_dec_uint ck_pr_dec_uint_zero ck_pr_dec_int ck_pr_dec_int_zero ck_pr_dec_64 ck_pr_dec..."
---

<h2>NAME</h2>
<p> <code>ck_pr_dec_ptr</code> <code>ck_pr_dec_ptr_zero</code> <code>ck_pr_dec_double</code> <code>ck_pr_dec_double_zero</code> <code>ck_pr_dec_char</code> <code>ck_pr_dec_char_zero</code> <code>ck_pr_dec_uint</code> <code>ck_pr_dec_uint_zero</code> <code>ck_pr_dec_int</code> <code>ck_pr_dec_int_zero</code> <code>ck_pr_dec_64</code> <code>ck_pr_dec_64_zero</code> <code>ck_pr_dec_32</code> <code>ck_pr_dec_32_zero</code> <code>ck_pr_dec_16</code> <code>ck_pr_dec_16_zero</code> <code>ck_pr_dec_8</code> <code>ck_pr_dec_8_zero</code> &#8211; atomic decrement operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_dec_ptr void *target Ft void Fn ck_pr_dec_ptr_zero void *target bool *z Ft void Fn ck_pr_dec_double double *target Ft void Fn ck_pr_dec_double_zero double *target bool *z Ft void Fn ck_pr_dec_char char *target Ft void Fn ck_pr_dec_char_zero char *target bool *z Ft void Fn ck_pr_dec_uint unsigned int *target Ft void Fn ck_pr_dec_uint_zero unsigned int *target bool *z Ft void Fn ck_pr_dec_int int *target Ft void Fn ck_pr_dec_int_zero int *target bool *z Ft void Fn ck_pr_dec_64 uint64_t *target Ft void Fn ck_pr_dec_64_zero uint64_t *target bool *z Ft void Fn ck_pr_dec_32 uint32_t *target Ft void Fn ck_pr_dec_32_zero uint32_t *target bool *z Ft void Fn ck_pr_dec_16 uint16_t *target Ft void Fn ck_pr_dec_16_zero uint16_t *target bool *z Ft void Fn ck_pr_dec_8 uint8_t *target Ft void Fn ck_pr_dec_8_zero uint8_t *target bool *z</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_dec 3 family of functions atomically decrement the value pointed to by Fa target .</p>
<h2>RETURN VALUES</h2>
<p> The ck_pr_dec_zero family of functions set the value pointed to by Fa z to true if the result of the decrement operation was 0. They set the value pointed to by Fa z to false otherwise.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_load3, ck_pr_store3, ck_pr_fas3, ck_pr_faa3, ck_pr_inc3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
