---
title: "ck_pr_load(3)"
name: "ck_pr_load"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_load/"
description: "ck_pr_load_ptr ck_pr_load_double ck_pr_load_uint ck_pr_load_int ck_pr_load_char ck_pr_load_64 ck_pr_load_32 ck_pr_load_16 ck_pr_load_8 – atomic volatile load operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_load_ptr</code> <code>ck_pr_load_double</code> <code>ck_pr_load_uint</code> <code>ck_pr_load_int</code> <code>ck_pr_load_char</code> <code>ck_pr_load_64</code> <code>ck_pr_load_32</code> <code>ck_pr_load_16</code> <code>ck_pr_load_8</code> &#8211; atomic volatile load operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void * Fn ck_pr_load_ptr const void *target Ft double Fn ck_pr_load_double const double *target Ft unsigned int Fn ck_pr_load_uint const unsigned int *target Ft int Fn ck_pr_load_int const int *target Ft char Fn ck_pr_load_char const char *target Ft uint64_t Fn ck_pr_load_64 const uint64_t *target Ft uint32_t Fn ck_pr_load_32 const uint32_t *target Ft uint16_t Fn ck_pr_load_16 const uint16_t *target Ft uint8_t Fn ck_pr_load_8 const uint8_t *target</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_load 3 family of functions atomically loads the value pointed to by Fa target and returns it. This family of functions always serves as an implicit compiler barrier and is not susceptible to re-ordering by the compiler.</p>
<h2>RETURN VALUES</h2>
<p> This family of functions returns the value contained in the location pointed to by the first argument.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_add3, ck_pr_store3, ck_pr_fas3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
