---
title: "tpm_nvinfo(8)"
name: "tpm_nvinfo"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_nvinfo/"
description: "tpm_nvinfo"
---

<p>tpm_nvinfo</p>
<h2>Synopsis</h2>
<p><code>tpm_nvinfo [</code><font SIZE="-1"><code>OPTIONS</code></font><code>]</code></p>
<h2>Description</h2>
<p><code>tpm_nvinfo</code> displays information about defined <font SIZE="-1">NVRAM</font> areas. The user may restrict it to display only a single <font SIZE="-1">NVRAM</font> area by providing an index or may choose ton only list available <font SIZE="-1">NVRAM</font> areas indices without displaying the <font SIZE="-1">NVRAM</font> areas&#8217; detailed information. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display command usage info.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd>Display command version info.</dd>
<dt><code>-l, &#8211;log [none|error|info|debug]</code></dt>
<dd>Set logging level.</dd>
<dt><code>-i, &#8211;index</code> (optional parameter)</dt>
<dd>Only display the <font SIZE="-1">NVRAM</font> area with the given index. If this option is not provided all <font SIZE="-1">NVRAM</font> areas will be displayed.</dd>
<dt><code>-n, &#8211;list-only</code> (optional parameter)</dt>
<dd>Only display the defined <font SIZE="-1">NVRAM</font> areas&#8217; indices.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_nvdefine/">tpm_nvdefine</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvread/">tpm_nvread</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvwrite/">tpm_nvwrite</a></code>(8), <code><a href="/docs/linux/man/8-tpm_nvrelease/">tpm_nvrelease</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
