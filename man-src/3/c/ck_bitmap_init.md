---
title: "ck_bitmap_init(3)"
name: "ck_bitmap_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_init/"
description: "ck_bitmap_init – initialize a bitmap"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_init</code> &#8211; initialize a bitmap</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft void Fn ck_bitmap_init ck_bitmap_t *bitmap unsigned int n_bits bool set</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_init function initializes the bitmap pointed to by the Fa bitmap pointer. The argument Fa n_bits specifies the number of bits that are to be stored in the bitmap. The argument Fa set determines whether the values of the bits in Fa bitmap are to be initialized to <code>1</code> or <code>0</code> </p>
<p> It is expected that Fa bitmap points to a contiguous region of memory containing at least the number of bytes specified by ck_bitmap_size3.</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>ERRORS</h2>
<dl>
<p> The behavior of Fn ck_bitmap_init is undefined if Fa bitmap is not a pointer to a region of bytes of at least ck_bitmap_size3 length.</dl>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_size3, ck_bitmap_set3, ck_bitmap_reset3, ck_bitmap_clear3, ck_bitmap_test3, ck_bitmap_bits3, ck_bitmap_buffer3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
