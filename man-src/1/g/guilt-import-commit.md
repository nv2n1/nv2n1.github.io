---
title: "guilt-import-commit(1)"
name: "guilt-import-commit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-import-commit/"
description: "guilt-import-commit – Import one or more commits as patches"
---

<h2 class="name">NAME</h2>
<p> guilt-import-commit &#8211; Import one or more commits as patches </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-import-commit</i> [&lt;hash&gt; | &lt;since&gt;..[&lt;until&gt;] | ..&lt;until&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Import one or more commits as individual patches.</p>
<h2>OPTIONS</h2>
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
