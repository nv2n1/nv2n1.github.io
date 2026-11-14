---
title: "guilt-select(1)"
name: "guilt-select"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-select/"
description: "guilt-select – Select guards to apply when pushing patches"
---

<h2 class="name">NAME</h2>
<p> guilt-select &#8211; Select guards to apply when pushing patches </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-select</i> [ -n | &#8211;none | -s | &#8211;series | [&#8211;pop|&#8211;reapply] &lt;guards&#8230;&gt; ]</p>
<h2>DESCRIPTION</h2>
<p> Select guards to apply when pushing patches. </p>
<p> Guards are selected without the + or &#8211; prefix. Patches are applied in the following way: </p>
<dl>
<dt>
<dd> * An unguarded patch is always applied.</dl>
<dl>
<dt>
<dd> * A patch with a positive guard is applied <code>only</code> if the guard is selected with guilt-select.</dl>
<dl>
<dt>
<dd> * A patch with a negative guard is applied <code>unless</code> the guard is selected with guilt-select.</dl>
<h2>OPTIONS</h2>
<p> -n|&#8211;none</p>
<dl>
<dt>
<dd> Remove all selected guards</dl>
<p> &#8211;pop</p>
<dl>
<dt>
<dd> Pop back to the first guarded patch</dl>
<p> &#8211;reapply</p>
<dl>
<dt>
<dd> Pop back to first guarded patch, select a new guard, and push</dl>
<p> -s|&#8211;series</p>
<dl>
<dt>
<dd> List all guards listed in the series file</dl>
<h2>AUTHOR</h2>
<p> Written by Eric Lesh &lt;m[blue]<code>eclesh [at] ucla.edu</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Eric Lesh &lt;m[blue]<code>eclesh [at] ucla.edu</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>GUILT</h2>
<p> Part of the linkguilt:guilt[7] suite (Generated for Guilt v0.33)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> eclesh [at] ucla.edu</p>
<dl>
<dt>
<dd> mailto:eclesh [at] ucla.edu</dl>
</dl>
<h2>Index</h2>
