---
title: "guilt-delete(1)"
name: "guilt-delete"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-delete/"
description: "guilt-delete – Delete a patch"
---

<h2 class="name">NAME</h2>
<p> guilt-delete &#8211; Delete a patch </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-delete</i> [-f] &lt;patchname&gt;</p>
<h2>DESCRIPTION</h2>
<p> Delete an unapplied patch from the series.</p>
<h2>OPTIONS</h2>
<p> -f</p>
<dl>
<dt>
<dd> Remove the patch from the series and disk</dl>
<p> &lt;patchname&gt;</p>
<dl>
<dt>
<dd> Name of the patch to delete.</dl>
<h2>EXAMPLES</h2>
<p> Delete a patch called <i>foobar</i>: </p>
<dl>
<dt>
<dd>
<pre>
$ guilt-delete foobar
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Written by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Brandon Philips &lt;m[blue]<code>brandon [at] ifup.org</code>m[]<font SIZE="-2">[2]</font>&gt;</p>
<h2>GUILT</h2>
<p> Part of the linkguilt:guilt[7] suite (Generated for Guilt v0.33)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> jeffpc [at] josefsipek.net</p>
<dl>
<dt>
<dd> mailto:jeffpc [at] josefsipek.net</dl>
<dt> 2.</p>
<dd> brandon [at] ifup.org</p>
<dl>
<dt>
<dd> mailto:brandon [at] ifup.org</dl>
</dl>
<h2>Index</h2>
