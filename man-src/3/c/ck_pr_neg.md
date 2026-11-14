---
title: "ck_pr_neg(3)"
name: "ck_pr_neg"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_neg/"
description: "ck_pr_neg_ptr ck_pr_neg_ptr_zero ck_pr_neg_double ck_pr_neg_double_zero ck_pr_neg_char ck_pr_neg_char_zero ck_pr_neg_uint ck_pr_neg_uint_zero ck_pr_neg_int ck_pr_neg_int_zero ck_pr_neg_64 ck_pr_neg..."
---

<h2>NAME</h2>
<p> <code>ck_pr_neg_ptr</code> <code>ck_pr_neg_ptr_zero</code> <code>ck_pr_neg_double</code> <code>ck_pr_neg_double_zero</code> <code>ck_pr_neg_char</code> <code>ck_pr_neg_char_zero</code> <code>ck_pr_neg_uint</code> <code>ck_pr_neg_uint_zero</code> <code>ck_pr_neg_int</code> <code>ck_pr_neg_int_zero</code> <code>ck_pr_neg_64</code> <code>ck_pr_neg_64_zero</code> <code>ck_pr_neg_32</code> <code>ck_pr_neg_32_zero</code> <code>ck_pr_neg_16</code> <code>ck_pr_neg_16_zero</code> <code>ck_pr_neg_8</code> <code>ck_pr_neg_8_zero</code> &#8211; atomic negation operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_neg_ptr void *target Ft void Fn ck_pr_neg_ptr_zero void *target bool *z Ft void Fn ck_pr_neg_double double *target Ft void Fn ck_pr_neg_double_zero double *target bool *z Ft void Fn ck_pr_neg_char char *target Ft void Fn ck_pr_neg_char_zero char *target bool *z Ft void Fn ck_pr_neg_uint unsigned int *target Ft void Fn ck_pr_neg_uint_zero unsigned int *target bool *z Ft void Fn ck_pr_neg_int int *target Ft void Fn ck_pr_neg_int_zero int *target bool *z Ft void Fn ck_pr_neg_64 uint64_t *target Ft void Fn ck_pr_neg_64_zero uint64_t *target bool *z Ft void Fn ck_pr_neg_32 uint32_t *target Ft void Fn ck_pr_neg_32_zero uint32_t *target bool *z Ft void Fn ck_pr_neg_16 uint16_t *target Ft void Fn ck_pr_neg_16_zero uint16_t *target bool *z Ft void Fn ck_pr_neg_8 uint8_t *target Ft void Fn ck_pr_neg_8_zero uint8_t *target bool *z</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_neg 3 family of functions atomically negate the value pointed to by Fa target .</p>
<h2>RETURN VALUES</h2>
<p> The ck_pr_neg_zero functions set the value pointed to by Fa z if the result of the negation operation was 0. They set the pointed to value to false otherwise.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_load3, ck_pr_store3, ck_pr_fas3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
