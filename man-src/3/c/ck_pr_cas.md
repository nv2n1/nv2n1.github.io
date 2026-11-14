---
title: "ck_pr_cas(3)"
name: "ck_pr_cas"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_cas/"
description: "ck_pr_cas_ptr ck_pr_cas_ptr_value ck_pr_cas_ptr_2 ck_pr_cas_ptr_2_value ck_pr_cas_double ck_pr_cas_double_value ck_pr_cas_char ck_pr_cas_char_value ck_pr_cas_uint ck_pr_cas_uint_value ck_pr_cas_int..."
---

<h2>NAME</h2>
<p> <code>ck_pr_cas_ptr</code> <code>ck_pr_cas_ptr_value</code> <code>ck_pr_cas_ptr_2</code> <code>ck_pr_cas_ptr_2_value</code> <code>ck_pr_cas_double</code> <code>ck_pr_cas_double_value</code> <code>ck_pr_cas_char</code> <code>ck_pr_cas_char_value</code> <code>ck_pr_cas_uint</code> <code>ck_pr_cas_uint_value</code> <code>ck_pr_cas_int</code> <code>ck_pr_cas_int_value</code> <code>ck_pr_cas_64_2</code> <code>ck_pr_cas_64_2_value</code> <code>ck_pr_cas_64</code> <code>ck_pr_cas_64_value</code> <code>ck_pr_cas_32</code> <code>ck_pr_cas_32_value</code> <code>ck_pr_cas_16</code> <code>ck_pr_cas_16_value</code> <code>ck_pr_cas_8</code> <code>ck_pr_cas_8_value</code> &#8211; atomic compare-and-swap operations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft bool Fn ck_pr_cas_ptr void *target void *old_value void *new_value Ft bool Fn ck_pr_cas_ptr_value void *target void *old_value void *new_value void *original_value Ft bool Fn ck_pr_cas_ptr_2 void *target void *old_value void *new_value Ft bool Fn ck_pr_cas_ptr_2_value void *target void *old_value void *new_value void *original_value Ft bool Fn ck_pr_cas_double double *target double old_value double new_value Ft bool Fn ck_pr_cas_double_value double *target double old_value double new_value double *original_value Ft bool Fn ck_pr_cas_char char *target char old_value char new_value Ft bool Fn ck_pr_cas_char_value char *target char old_value char new_value char *original_value Ft bool Fn ck_pr_cas_uint unsigned int *target unsigned int old_value unsigned int new_value Ft bool Fn ck_pr_cas_uint_value unsigned int *target unsigned int old_value unsigned int new_value unsigned int *original_value Ft bool Fn ck_pr_cas_int int *target int old_value int new_value Ft bool Fn ck_pr_cas_int_value int *target int old_value int new_value int *original_value Ft bool Fn ck_pr_cas_64_2 uint64_t target[static 2] uint64_t old_value[static 2] uint64_t new_value[static 2] Ft bool Fn ck_pr_cas_64_2_value uint64_t target[static 2] uint64_t old_value[static 2] uint64_t new_value[static 2] uint64_t original_value[static 2] Ft bool Fn ck_pr_cas_64 uint64_t *target uint64_t old_value uint64_t new_value Ft bool Fn ck_pr_cas_64_value uint64_t *target uint64_t old_value uint64_t new_value uint64_t *original_value Ft bool Fn ck_pr_cas_32 uint32_t *target uint32_t old_value uint32_t new_value Ft bool Fn ck_pr_cas_32_value uint32_t *target uint32_t old_value uint32_t new_value uint32_t *original_value Ft bool Fn ck_pr_cas_16 uint16_t *target uint16_t old_value uint16_t new_value Ft bool Fn ck_pr_cas_16_value uint16_t *target uint16_t old_value uint16_t new_value uint16_t *original_value Ft bool Fn ck_pr_cas_8 uint8_t *target uint8_t old_value uint8_t new_value Ft bool Fn ck_pr_cas_8_value uint8_t *target uint8_t old_value uint8_t new_value uint8_t *original_value</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_cas 3 family of functions atomically compare the value in Fa target for equality with Fa old_value and if so, replace the value pointed to by Fa target with the value specified by Fa new_value . If the value in Fa target was not equal to the value specified by Fa old_value then no modifications occur to the value in Fa target . The *_value form of these functions unconditionally update Fa original_value .</p>
<h2>RETURN VALUES</h2>
<p> This family of functions return true if the value in Fa target was modified as a result of the operation. Otherwise, they return false.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_load3, ck_pr_store3, ck_pr_fas3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_add3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
