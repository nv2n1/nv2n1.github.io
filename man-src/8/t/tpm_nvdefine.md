---
title: "tpm_nvdefine(8)"
name: "tpm_nvdefine"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_nvdefine/"
description: "tpm_nvdefine"
---

<p>tpm_nvdefine</p>
<h2>Synopsis</h2>
<p><code>tpm_nvdefine [</code><font SIZE="-1"><code>OPTIONS</code></font><code>]</code></p>
<h2>Description</h2>
<p><code>tpm_nvdefine</code> defines a new <font SIZE="-1">NVRAM</font> area at the given index and of given size. The user has to provide the permissions that control access to the <font SIZE="-1">NVRAM</font> area. </p>
<p> Owner authentication is necessary once the <font SIZE="-1">NVRAM</font> area 0xFFFFFFFF has been defined. The owner password may be provided on the command line using the owner password option. </p>
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
<dt><code>-z, &#8211;area-well-known</code></p>
<dd>Use a secret of all zeros (20 bytes of zeros) as the <font SIZE="-1">NVRAM</font> area&#8217;s secret.</p>
<dt><code>-o, &#8211;pwdo</code> (optional parameter)</p>
<dd>The owner password. </p>
<p> A password may be directly provided for example by using &#8216;&#8211;pwdo=password&#8217; or &#8216;-opassword&#8217;. If no password is provided with this option then the program will prompt the user for the password.</p>
<dt><code>-a, &#8211;pwda</code> (optional parameter)</p>
<dd>The <font SIZE="-1">NVRAM</font> area password. </p>
<p> A password may be directly provided for example by using &#8216;&#8211;pwda=password&#8217; or &#8216;-apassword&#8217;. If no password is provided with this option then the program will prompt the user for the password.</p>
<dt><code>-i, &#8211;index</code></p>
<dd>The index of the <font SIZE="-1">NVRAM</font> area. The parameter must either be a decimal number or a hexadecimal number starting with &#8216;0x&#8217;. </p>
<p> To select the <font SIZE="-1">NVRAM</font> area with index 0x100, the command line parameter should be &#8216;-i 0x100&#8217; or &#8216;&#8211;index 0x100&#8217;.</p>
<dt><code>-s, &#8211;size</code></p>
<dd>The size of the <font SIZE="-1">NVRAM</font> area. The parameter must either be a decimal number or a hexadecimal number starting with &#8216;0x&#8217;.</p>
<dt><code>-p, &#8211;permissions</code></p>
<dd>The access permissions associated with the <font SIZE="-1">NVRAM</font> area. The parameter must either be a decimal number or a hexadecimal number staring with &#8216;0x&#8217;. It is possible to logically &#8216;or&#8217; numbers or strings. The following strings are supported:</p>
<dl>
<dd>
<dl>
<dt><font SIZE="-1"><code>AUTHREAD</code></font></p>
<dd>Reading requires <font SIZE="-1">NVRAM</font> area authorization.</p>
<dt><font SIZE="-1"><code>AUTHWRITE</code></font></p>
<dd>Writing requires <font SIZE="-1">NVRAM</font> area authorization.</p>
<dt><font SIZE="-1"><code>PPREAD</code></font></p>
<dd>Reading requires physical presence.</p>
<dt><font SIZE="-1"><code>PPWRITE</code></font></p>
<dd>Writing requires physical presence.</p>
<dt><font SIZE="-1"><code>OWNERREAD</code></font></p>
<dd>Reading requires owner authorization.</p>
<dt><font SIZE="-1"><code>OWNERWRITE</code></font></p>
<dd>Writing requires owner authorization.</p>
<dt><font SIZE="-1"><code>GLOBALLOCK</code></font></p>
<dd>A write to index 0 locks the <font SIZE="-1">NVRAM</font> area until the next TPM_Startup(<font SIZE="-1">ST_CLEAR</font>)</p>
<dt><font SIZE="-1"><code>READ_STCLEAR</code></font></p>
<dd>A read with size 0 on the same index prevents further reading until the next TPM_Startup(<font SIZE="-1">ST_CLEAR</font>)</p>
<dt><font SIZE="-1"><code>WRITE_STCLEAR</code></font></p>
<dd>A write with size 0 to the same index prevents further writing until the next TPM_Startup(<font SIZE="-1">ST_CLEAR</font>)</p>
<dt><font SIZE="-1"><code>WRITEDEFINE</code></font></p>
<dd>A write with size 0 to the same index locks the <font SIZE="-1">NVRAM</font> area permanently</p>
<dt><font SIZE="-1"><code>WRITEALL</code></font></p>
<dd>The value must be written in a single operation</dl>
</dl>
<dl>
<dd>An example of a permission parameter is: </p>
<p> &#8211;permissions=&#8220;OWNERREAD|OWNERWRITE&#8221;</dl>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_nvread/">tpm_nvread</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvwrite/">tpm_nvwrite</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvrelease/">tpm_nvrelease</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvinfo/">tpm_nvinfo</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
