---
title: "ck_pr_fas(3)"
name: "ck_pr_fas"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_fas/"
description: "ck_pr_fas_ptr ck_pr_fas_double ck_pr_fas_char ck_pr_fas_uint ck_pr_fas_int ck_pr_fas_64 ck_pr_fas_32 ck_pr_fas_16 ck_pr_fas_8 – atomic swap operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_fas_ptr</code> <code>ck_pr_fas_double</code> <code>ck_pr_fas_char</code> <code>ck_pr_fas_uint</code> <code>ck_pr_fas_int</code> <code>ck_pr_fas_64</code> <code>ck_pr_fas_32</code> <code>ck_pr_fas_16</code> <code>ck_pr_fas_8</code> &#8211; atomic swap operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void * Fn ck_pr_fas_ptr void *target void *new_value Ft double Fn ck_pr_fas_double double *target double new_value Ft char Fn ck_pr_fas_char char *target char new_value Ft unsigned int Fn ck_pr_fas_uint unsigned int *target unsigned int new_value Ft int Fn ck_pr_fas_int int *target int new_value Ft uint64_t Fn ck_pr_fas_64 uint64_t *target uint64_t new_value Ft uint32_t Fn ck_pr_fas_32 uint32_t *target uint32_t new_value Ft uint16_t Fn ck_pr_fas_16 uint16_t *target uint16_t new_value Ft uint8_t Fn ck_pr_fas_8 uint8_t *target uint8_t new_value</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_fas 3 family of functions atomically fetch the value pointed to by Fa target and replace the value pointed to by Fa target with the value specified by Fa new_value .</p>
<h2>RETURN VALUES</h2>
<p> This function returns the value pointed to by Fa target at the time of operation invocation before it was atomically replaced with Fa new_value .</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_load3, ck_pr_store3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
