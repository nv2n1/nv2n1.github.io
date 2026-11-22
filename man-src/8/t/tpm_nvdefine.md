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
<p><code>tpm_nvdefine [</code><code>OPTIONS</code><code>]</code></p>
<h2>Description</h2>
<p><code>tpm_nvdefine</code> defines a new NVRAM area at the given index and of given size. The user has to provide the permissions that control access to the NVRAM area. </p>
<p> Owner authentication is necessary once the NVRAM area 0xFFFFFFFF has been defined. The owner password may be provided on the command line using the owner password option. </p>
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
<dt><code>-z, &#8211;area-well-known</code></dt>
<dd>Use a secret of all zeros (20 bytes of zeros) as the NVRAM area&#8217;s secret.</dd>
<dt><code>-o, &#8211;pwdo</code> (optional parameter)</dt>
<dd>The owner password. </dd>
<p> A password may be directly provided for example by using &#8216;&#8211;pwdo=password&#8217; or &#8216;-opassword&#8217;. If no password is provided with this option then the program will prompt the user for the password.</p>
<dt><code>-a, &#8211;pwda</code> (optional parameter)</dt>
<dd>The NVRAM area password. </dd>
<p> A password may be directly provided for example by using &#8216;&#8211;pwda=password&#8217; or &#8216;-apassword&#8217;. If no password is provided with this option then the program will prompt the user for the password.</p>
<dt><code>-i, &#8211;index</code></dt>
<dd>The index of the NVRAM area. The parameter must either be a decimal number or a hexadecimal number starting with &#8216;0x&#8217;. </dd>
<p> To select the NVRAM area with index 0x100, the command line parameter should be &#8216;-i 0x100&#8217; or &#8216;&#8211;index 0x100&#8217;.</p>
<dt><code>-s, &#8211;size</code></dt>
<dd>The size of the NVRAM area. The parameter must either be a decimal number or a hexadecimal number starting with &#8216;0x&#8217;.</dd>
<dt><code>-p, &#8211;permissions</code></dt>
<dd>The access permissions associated with the NVRAM area. The parameter must either be a decimal number or a hexadecimal number staring with &#8216;0x&#8217;. It is possible to logically &#8216;or&#8217; numbers or strings. The following strings are supported:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>AUTHREAD</code></dt>
<dd>Reading requires NVRAM area authorization.</dd>
<dt><code>AUTHWRITE</code></dt>
<dd>Writing requires NVRAM area authorization.</dd>
<dt><code>PPREAD</code></dt>
<dd>Reading requires physical presence.</dd>
<dt><code>PPWRITE</code></dt>
<dd>Writing requires physical presence.</dd>
<dt><code>OWNERREAD</code></dt>
<dd>Reading requires owner authorization.</dd>
<dt><code>OWNERWRITE</code></dt>
<dd>Writing requires owner authorization.</dd>
<dt><code>GLOBALLOCK</code></dt>
<dd>A write to index 0 locks the NVRAM area until the next TPM_Startup(ST_CLEAR)</dd>
<dt><code>READ_STCLEAR</code></dt>
<dd>A read with size 0 on the same index prevents further reading until the next TPM_Startup(ST_CLEAR)</dd>
<dt><code>WRITE_STCLEAR</code></dt>
<dd>A write with size 0 to the same index prevents further writing until the next TPM_Startup(ST_CLEAR)</dd>
<dt><code>WRITEDEFINE</code></dt>
<dd>A write with size 0 to the same index locks the NVRAM area permanently</dd>
<dt><code>WRITEALL</code></dt>
<dd>The value must be written in a single operation</dd></dl>
</dl>
<dl>
<dd>An example of a permission parameter is: </dd>
<p> &#8211;permissions=&#8220;OWNERREAD|OWNERWRITE&#8221;</dl>
<dd></dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_nvread/">tpm_nvread</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvwrite/">tpm_nvwrite</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvrelease/">tpm_nvrelease</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvinfo/">tpm_nvinfo</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
