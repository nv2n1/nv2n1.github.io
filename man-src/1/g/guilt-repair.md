---
title: "guilt-repair(1)"
name: "guilt-repair"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-repair/"
description: "guilt-repair – Repair the repository state"
---

<h2 class="name">NAME</h2>
<p> guilt-repair &#8211; Repair the repository state </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-repair</i> &#8211;full | &#8211;status</p>
<h2>DESCRIPTION</h2>
<p> Perform various repository repairs. You must specify one mode of repair: </p>
<p> &#8211;full</p>
<dl>
<dt>
<dd> Tries to repair everything possible. Additionally, it resets the repository state by reseting the HEAD to whatcqs believed to be the proper commit, and reseting the applied stack. The end result should be a repository with no patches applied. </p>
<dl>
<dt>
<dd>
<pre>
WARNING: Running this command may result in commits and working
directory changes being lost. You may want to create a new reference
(e.g., branch, or reflog) to the original HEAD before using
guilt-repair.
</pre>
</dl>
</dl>
<p> &#8211;status</p>
<dl>
<dt>
<dd> Upgrade the status file from old format to new.</dl>
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
