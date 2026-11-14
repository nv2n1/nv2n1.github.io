---
title: "ck_pr_stall(3)"
name: "ck_pr_stall"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_stall/"
description: "ck_pr_stall – busy-wait primitive"
---

<h2>NAME</h2>
<p> <code>ck_pr_stall</code> &#8211; busy-wait primitive</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft void Fn ck_pr_stall void</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_pr_stall 3 function should be used inside retry paths of busy-wait loops. It not only serves as a compiler barrier, but on some architectures it emits cycle-saving instructions.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_pr.h&gt;
static int ready = 0;
void function(void)
{
    /* Busy-wait until ready is non-zero. */
    while (ck_pr_load_int(&amp;ready) == 0)
        ck_pr_stall();
    return;
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_barrier3, ck_pr_fas3, ck_pr_load3, ck_pr_store3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_add3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_cas3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
