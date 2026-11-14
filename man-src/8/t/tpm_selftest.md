---
title: "tpm_selftest(8)"
name: "tpm_selftest"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_selftest/"
description: "tpm_selftest – request TPM perform selftest and report"
---

<p>TPM Management &#8211; tpm_selftest<br />
 </center></p>
<h2>Name</h2>
<p>tpm_selftest &#8211; request TPM perform selftest and report</p>
<h2>Synopsis</h2>
<p><code>tpm_selftest</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_selftest</code> requests that the system&#8217;s TPM perform a self test (via the TPM_SelfTestFull API) and report the results. The <code>&#8211;results</code> option reports the outcome of the last self test operation without requesting that another test be executed. If the TPM fails the self test, it enters failure mode where no commands are accepted. The results are reported in a manufacturer specific format. The TPM&#8217;s self test is always executed automatically at every boot.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd>Set logging level.</p>
<dt><code>-r</code>, <code>&#8211;results</code></p>
<dd>Report results only. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setownable/">tpm_setownable</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
