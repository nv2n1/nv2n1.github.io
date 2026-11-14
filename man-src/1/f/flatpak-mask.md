---
title: "flatpak-mask(1)"
name: "flatpak-mask"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-mask/"
description: "flatpak-mask – Mask out updates and automatic installation"
---

<h2 class="name">NAME</h2>
<p> flatpak-mask &#8211; Mask out updates and automatic installation </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak mask</code> [OPTION&#8230;] PATTERN&#8230;</dl>
<h2>DESCRIPTION</h2>
<dd>Flatpak maintains a list of patterns that define which refs are masked. A masked ref will never be updated or automatically installed (for example a masked extension marked auto-download will not be downloaded). You can still manually install such refs, but once they are installed the version will be pinned. </p>
<p> The patterns are just a partial ref, with the * character matching anything within that part of the ref. Here are some example patterns: </p>
<dl>
<dt>
<dd>
<pre>
org.some.App
org.some.App//unstable
app/org.domain.*
org.some.App/arm
</pre>
</dl>
<p> To list the current set of masks, run this command without any patterns.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;remove</code></p>
<dl>
<dt>
<dd> Instead of adding the patterns, remove matching patterns.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Mask refs in a per-user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Mask refs in the default system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Mask refs in a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak mask</code> </p>
<p> <code>$ flatpak mask org.broken.App</code> </p>
<p> <code>$ flatpak mask &#8211;remove org.broken.App</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-update/">flatpak-update</a></code>(1), </p>
<h2>Index</h2>
