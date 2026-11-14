---
title: "guilt-patchbomb(1)"
name: "guilt-patchbomb"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-patchbomb/"
description: "guilt-patchbomb – Email a series of commits interactively"
---

<h2 class="name">NAME</h2>
<p> guilt-patchbomb &#8211; Email a series of commits interactively </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-patchbomb</i> [-n] [&#8211;in-reply-to &lt;msgid&gt;] [&#8211;git] [&lt;hash&gt; | &lt;since&gt;..[&lt;until&gt;] | ..&lt;until&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Send a series of commits via email asking for To, CC and other information interactively.</p>
<h2>OPTIONS</h2>
<p> -n</p>
<dl>
<dt>
<dd> Doncqt send</dl>
<p> &#8211;in-reply-to &lt;msgid&gt;</p>
<dl>
<dt>
<dd> Set the In-reply-to header to the specified message id. This allows the patches to be sent as replies to an arbitrary message.</dl>
<p> &#8211;git</p>
<dl>
<dt>
<dd> Generate a patch which uses all the features offered by the git diff format (e.g., rename and copy detection).</dl>
<p> &lt;hash&gt;</p>
<dl>
<dt>
<dd> Only the specified revision.</dl>
<p> &lt;since&gt;..[&lt;until&gt;]</p>
<dl>
<dt>
<dd> Revisions starting from <i>&lt;since&gt;</i> until <i>&lt;until&gt;</i>. The <i>&lt;since&gt;</i> revision it self is NOT included, while <i>&lt;until&gt;</i> is. If <i>&lt;until&gt;</i> is not specified, it is assumed to be HEAD.</dl>
<p> ..&lt;until&gt;</p>
<dl>
<dt>
<dd> All revisions until the <i>&lt;until&gt;</i> revision (inclusive).</dl>
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
