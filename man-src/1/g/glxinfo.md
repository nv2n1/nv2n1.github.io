---
title: "glxinfo(1)"
name: "glxinfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glxinfo/"
description: "glxinfo – show information about the GLX implementation"
---

<h2 class="name">NAME</h2>
<p> glxinfo &#8211; show information about the GLX implementation </p>
<h2>SYNOPSIS</h2>
<p> <code>glxinfo</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <i>glxinfo</i> program shows information about the OpenGL and GLX implementations running on a given X display. </p>
<p> The information includes details about the server- and client-side GLX implementation, the OpenGL and GLU implementations as well as a list of available GLX visuals.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></dt>
<dd> Print visuals info in verbose form.</dd>
<dt><code>-t</code></dt>
<dd> Print verbose table.</dd>
<dt><code>-display </code><i>display</i></dt>
<dd> Specify the X display to interrogate.</dd>
<dt><code>-h</code></dt>
<dd> Print usage information.</dd>
<dt><code>-i</code></dt>
<dd> Force an indirect rendering context.</dd>
<dt><code>-b</code></dt>
<dd> Find the &quot;best&quot; visual and print its number.</dd>
<dt><code>-l</code></dt>
<dd> Print interesting OpenGL limits.</dd></dl>
<h2>AUTHOR</h2>
<p> glxinfo was written by Brian Paul &lt;brian.paul [at] tungstengraphics.com&gt;. </p>
<p> This manual page was written by Thierry Reding &lt;thierry [at] gilfi.de&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
