---
title: "lcp_crtpolelt(8)"
name: "lcp_crtpolelt"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lcp_crtpolelt/"
description: "lcp_crtpolelt – create an Intel(R) TXT policy element of specified type."
---

<p>lcp_crtpolelt &#8211; create an Intel(R) TXT policy element of specified type.</p>
<h2>Synopsis</h2>
<p><code>lcp_crtpolelt</code> <i>COMMAND</i> [<i>OPTION</i>]</p>
<h2>Description</h2>
<p><code>lcp_crtpolelt</code> is used to create an Intel(R) TXT policy element of specified type.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;create</p>
<dd>create an policy element</p>
<dl>
<dd>
<dl>
<dt>&#8211;type&nbsp;<wbr></code><i>type</i></p>
<dd>type of element; must be first option; see below for type strings and their options</p>
<dt><code>&#8211;out&nbsp;<wbr></code><i>file</i></p>
<dd>output file name</p>
<dt>[<code>&#8211;ctrl&nbsp;<wbr></code><i>pol-elt-ctr1</i>]</p>
<dd>PolEltControl field (hex or decimal)</dl>
</dl>
<dt><code>&#8211;show&nbsp;<wbr></code><i>file</i></p>
<dd>show policy element</p>
<dt><code>&#8211;verbose</code></p>
<dd>enable verbose output; can be specified with any command</p>
<dt><code>&#8211;help</code></p>
<dd>print out the help message</dl>
<h3>Available type options:</h3>
<dl>
<dt><code>mle&nbsp;<wbr></code>[<code>&#8211;minver&nbsp;<wbr></code><i>ver</i>]</p>
<dd>minimum version of SINIT</p>
<dt><code>mle&nbsp;<wbr></code>[<i>file1</i>][<i>file2</i>]&#8230;</p>
<dd>one or more files containing MLE hash(es); each file can contain multiple hashes</p>
<dt><code>pconf&nbsp;<wbr></code>[<i>file1</i>][<i>file2</i>]&#8230;</p>
<dd>one or more files containing PCR numbers and the desired digest of each; each file will be a PCONF</p>
<dt><code>custom&nbsp;<wbr></code>[<code>&#8211;uuid&nbsp;<wbr></code><i>UUID</i>]</p>
<dd>UUID in format: {0xaabbccdd, 0xeeff, 0xgghh, 0xiijj, {0xkk 0xll, 0xmm, 0xnn, 0xoo, 0xpp}} or &quot;&#8211;uuid tboot&quot; to use default</p>
<dt><code>custom&nbsp;<wbr></code>[<i>file</i>]</p>
<dd>file containing element data</dl>
<h2>Examples</h2>
<h3>Create an MLE element:</h3>
<table>
<tr VALIGN=top>
<td>1</td>
<td> <code>lcp_mlehash -c </code><i>&quot;logging=serial,vga,memory&quot; /boot/tboot.gz </i>&gt; <i>mle-hash </i>
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> <code>lcp_crtpolelt &#8211;create &#8211;type </code><i>mle </i><code>&#8211;ctrl </code><i>0x00 </i><code>&#8211;minver </code><i>17 </i><code>&#8211;out </code><i>mle.elt mle-hash </i>
</td>
</tr>
</table>
<h3>Create a PCONF element:</h3>
<table>
<tr VALIGN=top>
<td>1</td>
<td> <code>cat </code><i>/sys/devices/platform/tpm_tis/pcrs </i>| <code>grep -e </code><i>PCR-00 </i><code>-e </code><i>PCR-01 </i>&gt; <i>pcrs </i>
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> <code>lcp_crtpolelt &#8211;create &#8211;type </code><i>pconf </i><code>&#8211;out </code><i>pconf.elt pcrs </i>
</td>
</tr>
</table>
<h3>Create an SBIOS element:</h3>
<table>
<tr VALIGN=top>
<td>1</td>
<td> Create hash file containing BIOS hash(es), e.g. named <i>sbios-hash </i>
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> <code>lcp_crtpolelt &#8211;create &#8211;type </code><i>sbios </i><code>&#8211;out </code><i>sbios.elt sbios-hash </i>
</td>
</tr>
</table>
<h3>Create a CUSTOM element:</h3>
<table>
<tr VALIGN=top>
<td>1</td>
<td> Create or determine the UUID that will identify this data format (e.g. using <code><a href="/docs/linux/man/1-uuidgen/">uuidgen</a></code>(1)).
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> Create the data file that will be placed in this element (e.g. the policy file from <code><a href="/docs/linux/man/8-tb_polgen/">tb_polgen</a></code>(8)).
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td> <code>lcp_crtpolelt &#8211;create &#8211;type </code><i>custom </i><code>&#8211;out </code><i>custom.elt </i><code>&#8211;uuid </code><i>uuid-value data-file </i>
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lcp_crtpol2/">lcp_crtpol2</a></code>(8), <code><a href="/docs/linux/man/8-lcp_mlehash/">lcp_mlehash</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpollist/">lcp_crtpollist</a></code>(8), <code><a href="/docs/linux/man/1-uuidgen/">uuidgen</a></code>(1), <code><a href="/docs/linux/man/8-tb_polgen/">tb_polgen</a></code>(8). </p>
