---

title: "guilt-pop(1)"
name: "guilt-pop"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-pop/"
description: "guilt-pop – Pop patches from the tree"
---

<p> <i>guilt-pop</i> [-f] [-a | &#8211;all | -n &lt;num&gt; | &lt;patchname&gt;]</p>
<h2>OPTIONS</h2>
<p> &#8211;all, -a</p>
<dl>
<dt>
</dt><dd> Pop all patches off the tree</dd></dl>
<p> -f</p>
<dl>
<dt>
</dt><dd> Force; discards any unrefreshed changes</dd></dl>
<p> -n &lt;num&gt;</p>
<dl>
<dt>
</dt><dd> Push specified number of patches</dd></dl>
<p> &lt;patchname&gt;</p>
<dl>
<dt>
</dt><dd> Pop all patches up to and including this patch off the tree</dd></dl>
<p> If no patchname is given, pop the top-most patch.</p>
<h2>AUTHOR</h2>
<p> Written by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Brandon Philips &lt;m[blue]<code>brandon [at] ifup.org</code>m[]<font SIZE="-2">[2]</font>&gt;</p>
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
