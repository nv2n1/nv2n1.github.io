---
title: "guilt-guard(1)"
name: "guilt-guard"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-guard/"
description: "guilt-guard – Assign guards to patches"
---

<h2 class="name">NAME</h2>
<p> guilt-guard &#8211; Assign guards to patches </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-guard</i> [-l | &#8211;list | -n | &#8211;none | [&lt;patchname&gt;] [(+|-)&lt;guard&gt;&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> Assign guards to the specified patch, or to the patch on top of the stack if no patch is given on the command line. </p>
<p> An unguarded patch is always pushed. </p>
<p> A positive guard begins with a +. A patch with a positive guard is pushed <code>only if</code> the guard is selected. </p>
<p> A negative guard begins with a -. A patch with a negative guard is always pushed, <code>unless</code> the guard is selected.</p>
<h2>OPTIONS</h2>
<p> -l|&#8211;list</p>
<dl>
<dt>
<dd> List all patches and their guards</dl>
<p> -n|&#8211;none</p>
<dl>
<dt>
<dd> Remove all guards from a patch</dl>
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
