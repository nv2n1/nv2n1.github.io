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
<dt><code>&#8211;create</code></dt>
<dd>Create an TXT policy. The following options are available:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>&#8211;type&nbsp;<wbr></code><i>any|list</i></dt>
<dd>type</dd>
<dt><code>&#8211;pol&nbsp;<wbr></code><i>file</i></dt>
<dd>policy file</dd>
<dt>[<code>&#8211;ver&nbsp;<wbr></code><i>version</i>]</dt>
<dd>version</dd>
<dt>[<code>&#8211;minver&nbsp;<wbr></code><i>ver</i>]</dt>
<dd>SINITMinVersion</dd>
<dt>[<code>&#8211;rev&nbsp;<wbr></code><i>ctr1</i>,<i>ctrN</i>]</dt>
<dd>revocation values (comma separated, no spaces)</dd>
<dt>[<code>&#8211;ctrl&nbsp;<wbr></code><i>pol-ctrl</i>]</dt>
<dd>policy control</dd>
<dt>[<code>&#8211;data&nbsp;<wbr></code><i>file</i>]</dt>
<dd>policy data file</dd>
<dt>[<i>file</i>]&#8230;</dt>
<dd>policy list files</dd></dl>
</dl>
<dt><code>&#8211;show</code></dt>
<dd>Show the content of policy file or policy data file. Available options are:</dd>
<dl>
<dd>
</dd><dl>
<dt>[<code>&#8211;brief</code>]</dt>
<dd>breif format output</dd>
<dt>[<i>policy-file</i>]</dt>
<dd>policy file</dd>
<dt>[<i>policy-data-file</i>]</dt>
<dd>policy data file</dd></dl>
</dl>
<dt><code>&#8211;help</code></dt>
<dd>Print out the help message.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd>Enable verbose output; can be specified with any command.</dd></dl>
<h2>Examples</h2>
<p>Assuming a policy list file <i>list-unsig.lst</i> has been created by the command <code>lcp_crtpolist(8).</code> The following example will create a policy and policy data file. </p>
<p> <code>lcp_crtpol2 &#8211;create &#8211;type </code><i>list </i><code>&#8211;pol </code><i>list.pol </i><code>&#8211;data </code><i>list.data list-unsig.lst </i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lcp_crtpol/">lcp_crtpol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_mlehash/">lcp_mlehash</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpolelt/">lcp_crtpolelt</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpollist/">lcp_crtpollist</a></code>(8). </p>
