---
title: "tpm_nvwrite(8)"
name: "tpm_nvwrite"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_nvwrite/"
description: "tpm_nvwrite"
---

<p>tpm_nvwrite</p>
<h2>Synopsis</h2>
<p><code>tpm_nvwrite [</code><font SIZE="-1"><code>OPTIONS</code></font><code>]</code></p>
<h2>Description</h2>
<p><code>tpm_nvwrite</code> writes data to an <font SIZE="-1">NVRAM</font> area. The user must provide the index of the <font SIZE="-1">NVRAM</font> area as well as the data to write into the <font SIZE="-1">NVRAM</font> area. Optionally an offset into the <font SIZE="-1">NVRAM</font> area can be given where the writing of the data is to start. Similarly the use may provide the number of bytes to write into the <font SIZE="-1">NVRAM</font> area. Some <font SIZE="-1">NVRAM</font> areas only allow write sizes of zero, i.e., <font SIZE="-1">NVRAM</font> area index 0. If the <font SIZE="-1">NVRAM</font> area has permission bits set that require owner or <font SIZE="-1">NVRAM</font> area authentication, then the password must be provided via the password option. </p>
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
<dt><code>-z, &#8211;well-known</code></p>
<dd>Use a secret of all zeros (20 bytes of zeros) as either the <font SIZE="-1">NVRAM</font> area or owner secret.</p>
<dt><code>-p, &#8211;password</code></p>
<dd>Depending on what type of authentication is required for the <font SIZE="-1">NVRAM</font> area, this must either be the <font SIZE="-1">NVRAM</font> area or owner password. </p>
<p> A password may be directly provided for example by using &#8216;&#8211;password=password&#8217; or -ppassword. If no password is provided then the program will prompt the user for the password.</p>
<dt><code>-i, &#8211;index</code> (optional parameter)</p>
<dd>The index of the <font SIZE="-1">NVRAM</font> area. The parameter may either be a decimal number or a hexadecimal number starting with &#8216;0x&#8217;.</p>
<dt><code>-s, &#8211;size</code></p>
<dd>The number of bytes to write to the <font SIZE="-1">NVRAM</font> area. This parameter may be used to truncating the data that are for example read from a file. The parameter may either be a decimal number or a hexadecimal number starting with &#8216;0x&#8217;.</p>
<dt><code>-n, &#8211;offset</code> (optional parameter)</p>
<dd>The offset into the <font SIZE="-1">NVRAM</font> area where to start writing. The parameter may either be a decimal number or a hexadecimal number starting with &#8216;0x&#8217;.</p>
<dt><code>-f, &#8211;filename</code> (optional parameter)</p>
<dd>The name of a file from which to read data and copy them into the <font SIZE="-1">NVRAM</font> area.</p>
<dt><code>-d, &#8211;data</code> (optional parameter)</p>
<dd>The data to write into the <font SIZE="-1">NVRAM</font> area passed in the command line.</p>
<dt><code>-m, &#8211;fill-value</code> (optional parameter)</p>
<dd>The byte to fill the <font SIZE="-1">NVRAM</font> area with.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_nvdefine/">tpm_nvdefine</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvinfo/">tpm_nvinfo</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvread/">tpm_nvread</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvrelease/">tpm_nvrelease</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
