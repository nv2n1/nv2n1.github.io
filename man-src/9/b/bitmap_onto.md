---
title: "bitmap_onto(9)"
name: "bitmap_onto"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_onto/"
description: "bitmap_onto – translate one bitmap relative to another"
---

<p>bitmap_onto &#8211; translate one bitmap relative to another</p>
<h2>Synopsis</h2>
<pre><code>void bitmap_onto(unsigned long *dst, const unsigned long *orig, const unsigned long *relmap, unsigned int bits);</code></pre>
<h2>Arguments</h2>
<p><i>dst</i></p>
<dl>
<dd>
<dd>resulting translated bitmap</dl>
<p> <i>orig</i></p>
<dl>
<dd>original untranslated bitmap</dl>
<p> <i>relmap</i></p>
<dl>
<dd>bitmap relative to which translated</dl>
<p> <i>bits</i></p>
<dl>
<dd>number of bits in each of these bitmaps</dl>
<h2>Description</h2>
<p>Set the n-th bit of <i>dst</i> iff there exists some m such that the n-th bit of <i>relmap</i> is set, the m-th bit of <i>orig</i> is set, and the n-th bit of <i>relmap</i> is also the m-th _set_ bit of <i>relmap</i>. (If you understood the previous sentence the first time your read it, you&#8217;re overqualified for your current job.) </p>
<p> In other words, <i>orig</i> is mapped onto (surjectively) <i>dst</i>, using the map { &lt;n, m&gt; | the n-th bit of <i>relmap</i> is the m-th set bit of <i>relmap</i> }. </p>
<p> Any set bits in <i>orig</i> above bit number W, where W is the weight of (number of set bits in) <i>relmap</i> are mapped nowhere. In particular, if for all bits m set in <i>orig</i>, m &gt;= W, then <i>dst</i> will end up empty. In situations where the possibility of such an empty result is not desired, one way to avoid it is to use the <code>bitmap_fold</code> operator, below, to first fold the <i>orig</i> bitmap over itself so that all its set bits x are in the range 0 &lt;= x &lt; W. The <code>bitmap_fold</code> operator does this by setting the bit (m % W) in <i>dst</i>, for each bit (m) set in <i>orig</i>. </p>
<p> Example [1] for <code>bitmap_onto</code>: Let&#8217;s say <i>relmap</i> has bits 30-39 set, and <i>orig</i> has bits 1, 3, 5, 7, 9 and 11 set. Then on return from this routine, <i>dst</i> will have bits 31, 33, 35, 37 and 39 set. </p>
<p> When bit 0 is set in <i>orig</i>, it means turn on the bit in <i>dst</i> corresponding to whatever is the first bit (if any) that is turned on in <i>relmap</i>. Since bit 0 was off in the above example, we leave off that bit (bit 30) in <i>dst</i>. </p>
<p> When bit 1 is set in <i>orig</i> (as in the above example), it means turn on the bit in <i>dst</i> corresponding to whatever is the second bit that is turned on in <i>relmap</i>. The second bit in <i>relmap</i> that was turned on in the above example was bit 31, so we turned on bit 31 in <i>dst</i>. </p>
<p> Similarly, we turned on bits 33, 35, 37 and 39 in <i>dst</i>, because they were the 4th, 6th, 8th and 10th set bits set in <i>relmap</i>, and the 4th, 6th, 8th and 10th bits of <i>orig</i> (i.e. bits 3, 5, 7 and 9) were also set. </p>
<p> When bit 11 is set in <i>orig</i>, it means turn on the bit in <i>dst</i> corresponding to whatever is the twelfth bit that is turned on in <i>relmap</i>. In the above example, there were only ten bits turned on in <i>relmap</i> (30..39), so that bit 11 was set in <i>orig</i> had no affect on <i>dst</i>. </p>
<p> Example [2] for <code>bitmap_fold</code> + <code>bitmap_onto</code>: Let&#8217;s say <i>relmap</i> has these ten bits set: 40 41 42 43 45 48 53 61 74 95 (for the curious, that&#8217;s 40 plus the first ten terms of the Fibonacci sequence.) </p>
<p> Further lets say we use the following code, invoking <code>bitmap_fold</code> then bitmap_onto, as suggested above to avoid the possibility of an empty <i>dst</i> result: </p>
<p> unsigned long *tmp; // a temporary bitmap&#8217;s bits </p>
<p> bitmap_fold(tmp, orig, bitmap_weight(relmap, bits), bits); bitmap_onto(dst, tmp, relmap, bits); </p>
<p> Then this table shows what various values of <i>dst</i> would be, for various <i>orig</i>&#8216;s. I list the zero-based positions of each set bit. The tmp column shows the intermediate result, as computed by using <code>bitmap_fold</code> to fold the <i>orig</i> bitmap modulo ten (the weight of <i>relmap</i>). </p>
<p> <i>orig</i> tmp <i>dst</i> 0 0 40 1 1 41 9 9 95 10 0 40 (*) 1 3 5 7 1 3 5 7 41 43 48 61 0 1 2 3 4 0 1 2 3 4 40 41 42 43 45 0 9 18 27 0 9 8 7 40 61 74 95 0 10 20 30 0 40 0 11 22 33 0 1 2 3 40 41 42 43 0 12 24 36 0 2 4 6 40 42 45 53 78 102 211 1 2 8 41 42 74 (*) </p>
<p> (*) For these marked lines, if we hadn&#8217;t first done <code>bitmap_fold</code> into tmp, then the <i>dst</i> result would have been empty. </p>
<p> If either of <i>orig</i> or <i>relmap</i> is empty (no set bits), then <i>dst</i> will be returned empty. </p>
<p> If (as explained above) the only set bits in <i>orig</i> are in positions m where m &gt;= W, (where W is the weight of <i>relmap</i>) then <i>dst</i> will once again be returned empty. </p>
<p> All bits in <i>dst</i> not set by the above rule are cleared.</p>
<h2>Copyright</h2>
