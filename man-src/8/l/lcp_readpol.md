---
title: "lcp_readpol(8)"
name: "lcp_readpol"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lcp_readpol/"
description: "lcp_readpol – read the contents of an LCP policy index"
---

<p>lcp_readpol &#8211; read the contents of an LCP policy index</p>
<h2>Synopsis</h2>
<p><code>lcp_readpol</code> <code>-i</code> <i>index-value</i> [<code>-f</code> <i>policy-file</i>] [-s <i>size</i>] [-p <i>passwd</i>] [<code>-h</code>]</p>
<h2>Description</h2>
<p><code>lcp_readpol</code> is used to read the contents of an LCP policy index. Any index can be specified but the output will be parsed as if it contained a policy.</p>
<h2>Options</h2>
<dl>
<dt><code>-i&nbsp;<wbr></code><i>index-value</i></p>
<dd>Designate the index for reading. Index can be UINT32 or string. 3 strings are supported for the reserved LCP indices. Strings and default index values for each string are:</p>
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
<dd>File name to write the policy data to. If no file name is specified then the contents will be displayed.</p>
<dt><code>-s&nbsp;<wbr></code><i>size</i></p>
<dd>Value size to read from NV store. If no size inputted, read by length as this index defined.</p>
<dt><code>-p&nbsp;<wbr></code><i>password</i></p>
<dd>The TPM owner password</p>
<dt><code>-h</code></p>
<dd>Print out the help message</dl>
<h2>Examples</h2>
<p><code>lcp_readpol -i </code><i>default </i><code> -f </code><i>policy-file </p>
<p> </i><code>lcp_readpol -i </code><i>0x00011101 </i><code> -s </code><i>10 </p>
<p> </i><code>lcp_readpol -i </code><i>0x00011101 </i><code> -f </code><i>policy-file </i><code> -p </code><i>123456 </i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lcp_writepol/">lcp_writepol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpol/">lcp_crtpol</a></code>(8). </p>
