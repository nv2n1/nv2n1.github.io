---
title: "guilt-refresh(1)"
name: "guilt-refresh"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-refresh/"
description: "guilt-refresh – Refresh topmost applied patch"
---

<h2 class="name">NAME</h2>
<p> guilt-refresh &#8211; Refresh topmost applied patch </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-refresh</i> [&#8211;git] [&#8211;diffstat]</p>
<h2>DESCRIPTION</h2>
<p> Refresh topmost applied patch with changes in the working copy.</p>
<h2>OPTIONS</h2>
<p> &#8211;git</p>
<dl>
<dt>
<dd> Generate a patch which uses all the features offered by the git diff format (e.g., rename and copy detection).</dl>
<p> &#8211;diffstat</p>
<dl>
<dt>
<dd> Include a diffstat output in the patch file. Useful for cases where patches will be submitted with other tools. </p>
<p> If the command line option is omitted, the corresponding git-config option &quot;guilt.diffstat&quot; will be queried. So this would enable diffstat output by default: </p>
<dl>
<dt>
<dd>
<pre>
git config --global guilt.diffstat true
</pre>
</dl>
</dl>
<h2>AUTHOR</h2>
<p> Written by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>GUILT</h2>
<p> Part of the linkguilt:guilt[7] suite (Generated for Guilt v0.33)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> jeffpc [at] josefsipek.net</p>
<dl>
<dt>
<dd> mailto:jeffpc [at] josefsipek.net</dl>
</dl>
<h2>Index</h2>
