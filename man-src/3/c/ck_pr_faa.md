---
title: "ck_pr_faa(3)"
name: "ck_pr_faa"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_faa/"
description: "ck_pr_faa_ptr ck_pr_faa_double ck_pr_faa_char ck_pr_faa_uint ck_pr_faa_int ck_pr_faa_64 ck_pr_faa_32 ck_pr_faa_16 ck_pr_faa_8 – atomic fetch-and-add operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_faa_ptr</code> <code>ck_pr_faa_double</code> <code>ck_pr_faa_char</code> <code>ck_pr_faa_uint</code> <code>ck_pr_faa_int</code> <code>ck_pr_faa_64</code> <code>ck_pr_faa_32</code> <code>ck_pr_faa_16</code> <code>ck_pr_faa_8</code> &#8211; atomic fetch-and-add operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft uintptr_t Fn ck_pr_faa_ptr void *target uintptr_t delta Ft double Fn ck_pr_faa_double double *target double delta Ft char Fn ck_pr_faa_char char *target char delta Ft unsigned int Fn ck_pr_faa_uint unsigned int *target unsigned int delta Ft int Fn ck_pr_faa_int int *target int delta Ft uint64_t Fn ck_pr_faa_64 uint64_t *target uint64_t delta Ft uint32_t Fn ck_pr_faa_32 uint32_t *target uint32_t delta Ft uint16_t Fn ck_pr_faa_16 uint16_t *target uint16_t delta Ft uint8_t Fn ck_pr_faa_8 uint8_t *target uint8_t delta</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_faa 3 family of functions atomically fetch the value pointed to by Fa target and add the value specified by Fa delta to the value pointed to by Fa target .</p>
<h2>RETURN VALUES</h2>
<p> This function returns the value pointed to by Fa target at the time of operation invocation before the addition operation is applied.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_load3, ck_pr_store3, ck_pr_fas3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
