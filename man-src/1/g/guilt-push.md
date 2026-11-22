---

title: "guilt-push(1)"
name: "guilt-push"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-push/"
description: "guilt-push – Push patches onto the tree"
---

<p> guilt-push &#8211; Push patches onto the tree </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-push</i> [ -f ] [-a | &#8211;all | -n &lt;num&gt; | &lt;patchname&gt;]</p>
<h2>OPTIONS</h2>
<p> -f</p>
<dl>
<dt>
</dt><dd> Force the push if the patch doesncqt apply cleanly</dd></dl>
<p> &#8211;all, -a</p>
<dl>
<dt>
</dt><dd> Push all patches on the tree</dd></dl>
<p> -n &lt;num&gt;</p>
<dl>
<dt>
</dt><dd> Push specified number of patches</dd></dl>
<p> &lt;patchname&gt;</p>
<dl>
<dt>
</dt><dd> Push all patches up to and including this patch on the tree</dd></dl>
<p> If no patchname is given, push the next patch in the series onto the tree.</p>
<h2>AUTHOR</h2>
<p> Written by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[][1]&gt;</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Brandon Philips &lt;m[blue]<code>brandon [at] ifup.org</code>m[][2]&gt;</p>
<h2>GUILT</h2>
<p> Part of the linkguilt:guilt[7] suite (Generated for Guilt v0.33)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> jeffpc [at] josefsipek.net</dd>
<dl>
<dt>
</dt><dd> mailto:jeffpc [at] josefsipek.net</dd></dl>
<dt> 2.</dt>
<dd> brandon [at] ifup.org</dd>
<dl>
<dt>
</dt><dd> mailto:brandon [at] ifup.org</dd></dl>
</dl>
