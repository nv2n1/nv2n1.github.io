---
title: "guilt-new(1)"
name: "guilt-new"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-new/"
description: "guilt-new – Create a new patch"
---

<h2 class="name">NAME</h2>
<p> guilt-new &#8211; Create a new patch </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-new</i> [-f] [-s] [-e|-m message] &lt;patchname&gt;</p>
<h2>DESCRIPTION</h2>
<p> Create a new patch and push it on top of the stack. An optional patch description can be supplied either interactively on via the command line.</p>
<h2>OPTIONS</h2>
<p> -f</p>
<dl>
<dt>
<dd> Force patch creation if there are unrefreshed changes. These changes will get automatically imported into the new patch.</dl>
<p> -s</p>
<dl>
<dt>
<dd> Add a Signed-off-by with your committer identifier string to the patch message.</dl>
<p> -e</p>
<dl>
<dt>
<dd> Edit the patch message interactively. This option can be combined with -s to easily sign off on the patch.</dl>
<p> -m &lt;message&gt;</p>
<dl>
<dt>
<dd> The &quot;&lt;message&gt;&quot; string will used as the commit message. This option can be combined with -s to easily sign off on the patch.</dl>
<p> &lt;patchname&gt;</p>
<dl>
<dt>
<dd> Name of the patch to create. This must be a legal relative pathname string. For example, &quot;foo&quot;, &quot;foo/bar&quot;, and &quot;foo/bar/foobar&quot; are all valid.</dl>
<h2>EXAMPLES</h2>
<p> Create a new patch called <i>foobar</i>: </p>
<dl>
<dt>
<dd>
<pre>
$ guilt-new foobar
</pre>
</dl>
<p> Create a patch called <i>foo</i> and supply a patch description interactively: </p>
<dl>
<dt>
<dd>
<pre>
$ guilt-new -e foo
</pre>
</dl>
<p> Create a patch called <i>bar</i> with a provided patch description and sign off on the patch: </p>
<dl>
<dt>
<dd>
<pre>
$ guilt-new -s -m patch-fu bar
</pre>
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
