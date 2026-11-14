---
title: "fccharsetfirstpage(3)"
name: "fccharsetfirstpage"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetfirstpage/"
description: "FcCharSetFirstPage – Start enumerating charset contents"
---

<p>FcCharSetFirstPage &#8211; Start enumerating charset contents </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar32 FcCharSetFirstPage (const FcCharSet *</code><i>a</i><code>, FcChar32[FC_CHARSET_MAP_SIZE] </code><i>map</i><code>, FcChar32 *</code><i>next</i><code>); </code></p>
<h2>Description</h2>
<p>Builds an array of bits in <i>map</i> marking the first page of Unicode coverage of <i>a</i>. <i>*next</i> is set to contains the base code point for the next page in <i>a</i>. Returns the base code point for the page, or FC_CHARSET_DONE if <i>a</i> contains no pages. As an example, if <code>FcCharSetFirstPage</code> returns 0x300 and fills <i>map</i> with </p>
<pre>0xffffffff 0xffffffff 0x01000008 0x44300002 0xffffd7f0 0xfffffffb 0xffff7fff 0xffff0003</pre>
<p>Then the page contains code points 0x300 through 0x33f (the first 64 code points on the page) because <i>map[0]</i> and <i>map[1]</i> both have all their bits set. It also contains code points 0x343 (<i>0x300 + 32*2 + (4-1)</i>) and 0x35e (<i>0x300 + 32*2 + (31-1)</i>) because <i>map[2]</i> has the 4th and 31st bits set. The code points represented by map[3] and later are left as an excercise for the reader ;).</p>
