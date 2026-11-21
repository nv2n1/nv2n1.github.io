---
title: "tpm_sealdata(1)"
name: "tpm_sealdata"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tpm_sealdata/"
description: "tpm_sealdata – seal input data to the system’s TPM"
---

<p>TPM Management &#8211; tpm_sealdata<br />
 </center></p>
<h2 class="name">NAME</h2>
<p> tpm_sealdata &#8211; seal input data to the system&#8217;s TPM </p>
<h2>SYNOPSIS</h2>
<p> <code>tpm_sealdata</code> [<code>OPTION</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>tpm_sealdata</code> seals sensitive input data to the SRK of the system&#8217;s TPM and optionally a PCR configuration. Backup your data, it is unrecoverable from this format if the SRK changes or the specified PCR configuration is unreproducable. The result can be unsealed by functions in libtpm_unseal, such as <code><a href="/docs/linux/man/3-tpmunsealfile/">tpmUnsealFile</a></code>(3). </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display command usage info.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display command version info.</dd>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</dt>
<dd> Set logging level.</dd>
<dt><code>-i</code>, <code>&#8211;infile FILE</code></dt>
<dd> File containing input data to seal.</dd>
<dt><code>-o</code>, <code>&#8211;outfile FILE</code></dt>
<dd> Output file. Default is STDOUT.</dd>
<dt><code>-p</code>, <code>&#8211;pcr NUMBER</code></dt>
<dd> Seal data to the current value of the specified pcr. This option can be given NUM_PCRS times. The specified pcr is in the range of 0 to NUM_PCRS-1. NUM_PCRS is at least 16 but may vary by platform.</dd>
<dt><code>-z</code>, <code>&#8211;well-known</code></dt>
<dd> Use TSS_WELL_KNOWN_SECRET (20 zero bytes) as the SRK password. You will not be prompted for the SRK password with this option.</dd>
<dt><code>-u</code>, <code>&#8211;unicode</code></dt>
<dd> Use TSS UNICODE encoding for the SRK password to comply with applications using TSS popup boxes. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/3-tpmunsealfile/">tpmUnsealFile</a></code>(3) </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt; </p>
