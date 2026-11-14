---
title: "lcp_crtpol2(8)"
name: "lcp_crtpol2"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lcp_crtpol2/"
description: "lcp_crtpol2 – create an Intel(R) TXT policy (and policy data file)"
---

<p>lcp_crtpol2 &#8211; create an Intel(R) TXT policy (and policy data file)</p>
<h2>Synopsis</h2>
<p><code>lcp_crtpol2</code> <i>COMMAND</i> [<i>OPTION</i>]</p>
<h2>Description</h2>
<p><code>lcp_crtpol2</code> is used to create an Intel(R) TXT policy (and policy data file) for platforms produced after 2008.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;create</code></p>
<dd>Create an TXT policy. The following options are available:</p>
<dl>
<dd>
<dl>
<dt><code>&#8211;type&nbsp;<wbr></code><i>any|list</i></p>
<dd>type</p>
<dt><code>&#8211;pol&nbsp;<wbr></code><i>file</i></p>
<dd>policy file</p>
<dt>[<code>&#8211;ver&nbsp;<wbr></code><i>version</i>]</p>
<dd>version</p>
<dt>[<code>&#8211;minver&nbsp;<wbr></code><i>ver</i>]</p>
<dd>SINITMinVersion</p>
<dt>[<code>&#8211;rev&nbsp;<wbr></code><i>ctr1</i>,<i>ctrN</i>]</p>
<dd>revocation values (comma separated, no spaces)</p>
<dt>[<code>&#8211;ctrl&nbsp;<wbr></code><i>pol-ctrl</i>]</p>
<dd>policy control</p>
<dt>[<code>&#8211;data&nbsp;<wbr></code><i>file</i>]</p>
<dd>policy data file</p>
<dt>[<i>file</i>]&#8230;</p>
<dd>policy list files</dl>
</dl>
<dt><code>&#8211;show</code></p>
<dd>Show the content of policy file or policy data file. Available options are:</p>
<dl>
<dd>
<dl>
<dt>[<code>&#8211;brief</code>]</p>
<dd>breif format output</p>
<dt>[<i>policy-file</i>]</p>
<dd>policy file</p>
<dt>[<i>policy-data-file</i>]</p>
<dd>policy data file</dl>
</dl>
<dt><code>&#8211;help</code></p>
<dd>Print out the help message.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Enable verbose output; can be specified with any command.</dl>
<h2>Examples</h2>
<p>Assuming a policy list file <i>list-unsig.lst</i> has been created by the command <code><a href="/docs/linux/man/8-lcp_crtpolist/">lcp_crtpolist</a>(8).</code> The following example will create a policy and policy data file. </p>
<p> <code>lcp_crtpol2 &#8211;create &#8211;type </code><i>list </i><code>&#8211;pol </code><i>list.pol </i><code>&#8211;data </code><i>list.data list-unsig.lst </i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lcp_crtpol/">lcp_crtpol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_mlehash/">lcp_mlehash</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpolelt/">lcp_crtpolelt</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpollist/">lcp_crtpollist</a></code>(8). </p>
