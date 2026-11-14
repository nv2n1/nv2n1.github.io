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
<p><code>tpm_nvrelease [</code><font SIZE="-1"><code>OPTIONS</code></font><code>]</code></p>
<h2>Description</h2>
<p><code>tpm_nvrelease</code> releases an <font SIZE="-1">NVRAM</font> area. The user must provide the index of the <font SIZE="-1">NVRAM</font> area. If owner authentication is required then the user must provide the owner password. </p>
<p> Note that some areas cannot be released since they are permanent. Others can be release only after a reboot of the system. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l, &#8211;log [none|error|info|debug]</code></p>
<dd>Set logging level.</p>
<dt><code>-u, &#8211;unicode</code></p>
<dd>Use <font SIZE="-1">TSS</font> <font SIZE="-1">UNICODE</font> encoding for passwords to comply with applications using <font SIZE="-1">TSS</font> popup boxes</p>
<dt><code>-y, &#8211;owner-well-known</code></p>
<dd>Use a secret of all zeros (20 bytes of zeros) as the owner&#8217;s secret.</p>
<dt><code>-o, &#8211;pwdo</code></p>
<dd>The owner password. </p>
<p> A password may be directly provided for example by using &#8216;&#8211;pwdo=password&#8217; or &#8216;-opassword&#8217;. If no password is provided with this option then the program will prompt the user for the password.</p>
<dt><code>-i, &#8211;index</code></p>
<dd>The index of the <font SIZE="-1">NVRAM</font> area that is to be released. The parameter may either be a decimal number or a hexadecimal number starting with &#8216;0x&#8217;.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_nvdefine/">tpm_nvdefine</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvinfo/">tpm_nvinfo</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvread/">tpm_nvread</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvwrite/">tpm_nvwrite</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
