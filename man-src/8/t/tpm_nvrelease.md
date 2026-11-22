---
title: "tpm_nvrelease(8)"
name: "tpm_nvrelease"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_nvrelease/"
description: "tpm_nvrelease"
---

<p>tpm_nvrelease</p>
<h2>Synopsis</h2>
<p><code>tpm_nvrelease [</code><code>OPTIONS</code><code>]</code></p>
<h2>Description</h2>
<p><code>tpm_nvrelease</code> releases an NVRAM area. The user must provide the index of the NVRAM area. If owner authentication is required then the user must provide the owner password. </p>
<p> Note that some areas cannot be released since they are permanent. Others can be release only after a reboot of the system. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display command usage info.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd>Display command version info.</dd>
<dt><code>-l, &#8211;log [none|error|info|debug]</code></dt>
<dd>Set logging level.</dd>
<dt><code>-u, &#8211;unicode</code></dt>
<dd>Use TSS UNICODE encoding for passwords to comply with applications using TSS popup boxes</dd>
<dt><code>-y, &#8211;owner-well-known</code></dt>
<dd>Use a secret of all zeros (20 bytes of zeros) as the owner&#8217;s secret.</dd>
<dt><code>-o, &#8211;pwdo</code></dt>
<dd>The owner password. </dd>
<p> A password may be directly provided for example by using &#8216;&#8211;pwdo=password&#8217; or &#8216;-opassword&#8217;. If no password is provided with this option then the program will prompt the user for the password.</p>
<dt><code>-i, &#8211;index</code></dt>
<dd>The index of the NVRAM area that is to be released. The parameter may either be a decimal number or a hexadecimal number starting with &#8216;0x&#8217;.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_nvdefine/">tpm_nvdefine</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvinfo/">tpm_nvinfo</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvread/">tpm_nvread</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvwrite/">tpm_nvwrite</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
