---
title: "lcp_writepol(8)"
name: "lcp_writepol"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lcp_writepol/"
description: "lcp_writepol – write LCP policy into a TPM NV index"
---

<p>lcp_writepol &#8211; write LCP policy into a TPM NV index</p>
<h2>Synopsis</h2>
<p><code>lcp_writepol</code> <code>-i</code> <i>index-value</i> [<code>-f</code> <i>policy-file</i> |&nbsp;<wbr><code>-e</code>] [<code>-p</code> <i>passwd</i>] [<code>-h</code>]</p>
<h2>Description</h2>
<p><code>lcp_writepol</code> is used to write LCP policy into a (previously-defined) TPM NV index. It also supports writing arbitrary data into a specified index.</p>
<h2>Options</h2>
<dl>
<dt><code>-i&nbsp;<wbr></code><i>index-value</i></p>
<dd>Designate the index for writing. Index can be UINT32 or string. 3 strings are supported for the reserved LCP indices. Strings and default index values for each string are:</p>
<dl>
<dd>
<dl>
<dt>default</p>
<dd>0x50000001(INDEX_LCP_DEF)</p>
<dt>owner</p>
<dd>0x40000001(INDEX_LCP_OWN)</p>
<dt>aux</p>
<dd>0x50000002(INDEX_LCP_AUX)</dl>
</dl>
<dt><code>-f&nbsp;<wbr></code><i>policy-file</i></p>
<dd>File name where the policy data is stored.</p>
<dt><code>-e</code></p>
<dd>Write 0 length data to the index. This is useful for special indices, such as those permission is WRITEDFINE.</p>
<dt><code>-p&nbsp;<wbr></code><i>password</i></p>
<dd>The TPM owner password</p>
<dt><code>-h</code></p>
<dd>Print out the help message</dl>
<h2>Examples</h2>
<p><code>lcp_writepol -i </code><i>default </i><code> -f </code><i>policy-file </p>
<p> </i><code>lcp_writepol -i </code><i>0x00011101 </i><code> -e </p>
<p> lcp_writepol -i </code><i>0x00011101 </i><code> -f </code><i>policy-file </i><code> -p </code><i>123456 </i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lcp_readpol/">lcp_readpol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpol/">lcp_crtpol</a></code>(8). </p>
