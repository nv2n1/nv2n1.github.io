---
title: "sh64_teardown_tlb_slot(9)"
name: "sh64_teardown_tlb_slot"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sh64_teardown_tlb_slot/"
description: "sh64_teardown_tlb_slot – Teardown a translation."
---

<p>sh64_teardown_tlb_slot &#8211; Teardown a translation.</p>
<h2>Synopsis</h2>
<pre><code>void sh64_teardown_tlb_slot(unsigned long long config_addr);</code></pre>
<h2>Arguments</h2>
<p><i>config_addr</i></p>
<dl>
<dd>
<dd>Address of TLB slot.</dl>
<h2>Description</h2>
<p>Teardown any existing mapping in the TLB slot <i>config_addr</i>.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
