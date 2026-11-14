---
title: "check_lft_balance(8)"
name: "check_lft_balance"
section: "8"
letter: "c"
url: "/docs/linux/man/8-check_lft_balance/"
description: "CHECK_LFT_BALANCE –"
---

<p>CHECK_LFT_BALANCE &#8211;</p>
<h2>Check Infiniband Unicast Forwarding Tables Balance</h2>
<h3>Synopsis</h3>
<p>check_lft_balance.sh [-hRv]</p>
<h3>Description</h3>
<p>check_lft_balance.sh is a script which checks for balancing in Infiniband unicast forwarding tables. It analyzes the output of <code><a href="/docs/linux/man/8-dump_lfts/">dump_lfts</a>(8)</code> and <code><a href="/docs/linux/man/8-iblinkinfo/">iblinkinfo</a>(8)</code></p>
<h3>Options</h3>
<dl>
<dt><code>-h</code></p>
<dd>show help</p>
<dt><code>-R</code></p>
<dd>Recalculate dump_lfts information, ie do not use the cached information. This option is slower but should be used if the diag tools have not been used for some time or if there are other reasons to believe that the fabric has changed.</p>
<dt><code>-v</code></p>
<dd>verbose output</dl>
<h3>See Also</h3>
<p><code><a href="/docs/linux/man/8-dump_lfts/">dump_lfts</a>(8)</code> <code><a href="/docs/linux/man/8-iblinkinfo/">iblinkinfo</a>(8)</code></p>
<h3>Authors</h3>
<dl>
<dt><code>Albert Chu</code></p>
<dd>&lt; <i>chu11 [at] llnl.gov</i> &gt; </p>
</dl>
