---
title: "ck_pr_bts(3)"
name: "ck_pr_bts"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_bts/"
description: "ck_pr_bts_ptr ck_pr_bts_uint ck_pr_bts_int ck_pr_bts_64 ck_pr_bts_32 ck_pr_bts_16 – atomic bit test-and-set operations"
---

<h2>NAME</h2>
<p> <code>ck_pr_bts_ptr</code> <code>ck_pr_bts_uint</code> <code>ck_pr_bts_int</code> <code>ck_pr_bts_64</code> <code>ck_pr_bts_32</code> <code>ck_pr_bts_16</code> &#8211; atomic bit test-and-set operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft bool Fn ck_pr_bts_ptr void *target unsigned int bit_index Ft bool Fn ck_pr_bts_uint uint *target unsigned int bit_index Ft bool Fn ck_pr_bts_int int *target unsigned int bit_index Ft bool Fn ck_pr_bts_64 uint64_t *target unsigned int bit_index Ft bool Fn ck_pr_bts_32 uint32_t *target unsigned int bit_index Ft bool Fn ck_pr_bts_16 uint16_t *target unsigned int bit_index</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_bts 3 family of functions atomically fetch the value of the bit in Fa target at index Fa bit_index and set that bit to 1.</p>
<h2>RETURN VALUES</h2>
<p> This family of functions returns the original value of the bit at offset Fa bit_index that is in the value pointed to by Fa target .</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_load3, ck_pr_store3, ck_pr_fas3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_add3, ck_pr_btc3, ck_pr_btr3, ck_pr_cas3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
