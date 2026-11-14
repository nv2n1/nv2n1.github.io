---
title: "sh64_setup_tlb_slot(9)"
name: "sh64_setup_tlb_slot"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sh64_setup_tlb_slot/"
description: "sh64_setup_tlb_slot – Load up a translation in a wired slot."
---

<p>sh64_setup_tlb_slot &#8211; Load up a translation in a wired slot.</p>
<h2>Synopsis</h2>
<pre><code>void sh64_setup_tlb_slot(unsigned long long config_addr, unsigned long eaddr, unsigned long asid, unsigned long paddr);</code></pre>
<h2>Arguments</h2>
<p><i>config_addr</i></p>
<dl>
<dd>
<dd>Address of TLB slot.</dl>
<p> <i>eaddr</i></p>
<dl>
<dd>Virtual address.</dl>
<p> <i>asid</i></p>
<dl>
<dd>Address Space Identifier.</dl>
<p> <i>paddr</i></p>
<dl>
<dd>Physical address.</dl>
<h2>Description</h2>
<p>Load up a virtual&lt;-&gt;physical translation for <i>eaddr</i>&lt;-&gt;<i>paddr</i> in the pre-allocated TLB slot <i>config_addr</i> (see sh64_get_wired_dtlb_entry).</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
