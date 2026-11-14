---
title: "flatpak-repo(1)"
name: "flatpak-repo"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-repo/"
description: "flatpak-repo – Show information about a local repository"
---

<h2 class="name">NAME</h2>
<p> flatpak-repo &#8211; Show information about a local repository </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak repo</code> [OPTION&#8230;] LOCATION</dl>
<h2>DESCRIPTION</h2>
<dd>Show information about a local repository. </p>
<p> If you need to modify a local repository, see the <code>flatpak build-update-repo</code> command, or use the <code>ostree</code> tool.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;info</code></p>
<dl>
<dt>
<dd> Print general information about a local repository.</dl>
<p> <code>&#8211;branches</code></p>
<dl>
<dt>
<dd> List the branches in a local repository.</dl>
<p> <code>&#8211;metadata=BRANCH</code></p>
<dl>
<dt>
<dd> Print metadata for a branch in the repository.</dl>
<p> <code>&#8211;commits=BRANCH</code></p>
<dl>
<dt>
<dd> Show commits and deltas for a branch in the repository.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak repo &#8211;info ~/my-repo</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-info/">flatpak-info</a></code>(1) <code><a href="/docs/linux/man/1-flatpak-build-update-repo/">flatpak-build-update-repo</a></code>(1) <code><a href="/docs/linux/man/1-ostree/">ostree</a></code>(1) </p>
<h2>Index</h2>
