---
title: "ck_pr_rtm(3)"
name: "ck_pr_rtm"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_pr_rtm/"
description: "ck_pr_rtm_begin ck_pr_rtm_end ck_pr_rtm_abort ck_pr_rtm_test – restricted transactional memory"
---

<h2>NAME</h2>
<p> <code>ck_pr_rtm_begin</code> <code>ck_pr_rtm_end</code> <code>ck_pr_rtm_abort</code> <code>ck_pr_rtm_test</code> &#8211; restricted transactional memory</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_pr.h Ft unsigned int Fn ck_pr_rtm_begin void Ft void Fn ck_pr_rtm_end void Ft void Fn ck_pr_rtm_abort const unsigned int status Ft bool Fn ck_pr_rtm_test void</p>
<h2>DESCRIPTION</h2>
<p> These family of functions implement support for restricted transactional memory, if available on the underlying platform. Currently, support is only provided for Intel Haswell and newer x86 microarchitectures that have the TSX-NI feature. </p>
<p> The Fn ck_pr_rtm_begin function returns CK_PR_RTM_STARTED if a transaction was successfully started. In case of an abort, either internal (through a ck_pr_rtm_abort) or external, program flow will return to the point which the function was called except the return value will consist of a bitmap with one or more of the following bits set:</p>
<dl>
<dt><code>CK_PR_RTM_EXPLICIT</code></p>
<dd> Set if the transactionally was explicitly aborted through Fn ck_pr_rtm_abort .</p>
<dt><code>CK_PR_RTM_RETRY</code></p>
<dd> Set if the transaction failed but can still succeed if retried.</p>
<dt><code>CK_PR_RTM_CONFLICT</code></p>
<dd> The transaction failed due to a conflict in one of the memory addresses that are part of the working set of the transaction.</p>
<dt><code>CK_PR_RTM_CAPACITY</code></p>
<dd> Set if the architecture-defined transaction size limit was exceeded.</p>
<dt><code>CK_PR_RTM_DEBUG</code></p>
<dd> Set if a hardware breakpoint was triggered.</p>
<dt><code>CK_PR_RTM_NESTED</code></p>
<dd> Set if a nested transaction failed.</dl>
<p> The user is also able to specify a one byte abort status by calling Fn ck_pr_rtm_abort . This status byte can be extracted by calling the Fn CK_PR_RTM_CODE function with the return value of Fn ck_pr_rtm_begin as an argument. The return value of Fn CK_PR_RTM_CODE will be the value of this status byte. For additional information, please see the Intel instruction set manuals.</p>
<h2>SEE ALSO</h2>
<p> ck_pr_fence_load3, ck_pr_fence_load_depends3, ck_pr_fence_store3, ck_pr_fence_memory3, ck_pr_load3, ck_pr_store3, ck_pr_fas3, ck_pr_faa3, ck_pr_inc3, ck_pr_dec3, ck_pr_neg3, ck_pr_not3, ck_pr_sub3, ck_pr_and3, ck_pr_or3, ck_pr_xor3, ck_pr_add3, ck_pr_btc3, ck_pr_bts3, ck_pr_btr3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
