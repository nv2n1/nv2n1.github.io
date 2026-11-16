---
title: "dnf-plugin-download(8)"
name: "dnf-plugin-download"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnf-plugin-download/"
description: "dnf.plugin.download – DNF download Plugin"
---

<p>dnf.plugin.download &#8211; DNF download Plugin </p>
<p> Download binary or source packages.</p>
<h2>Synopsis</h2>
<p><code>dnf download [options] &lt;pkg-spec&gt;&#8230;</code></p>
<h2>Arguments</h2>
<dl>
<dt><code>&lt;pkg-spec&gt;</code></dt>
<dd>Package specification for the package to download.</dd></dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help-cmd</code></dt>
<dd>Show this help.</dd>
<dt><code>&#8211;source</code></dt>
<dd>Download the source rpm. Enables source repositories of all enabled binary repositories.</dd>
<dt><code>&#8211;destdir</code></dt>
<dd>Download directory, default is the current directory (the directory must exist).</dd>
<dt><code>&#8211;resolve</code></dt>
<dd>Resolve and download dependencies, not installed on the local system.</dd></dl>
<h2>Examples</h2>
<dl>
<dt><code>dnf download dnf</code></dt>
<dd>Download the latest dnf package to the current directory.</dd>
<dt><code>dnf download dnf &#8211;destdir /tmp/dnl</code></dt>
<dd>Download the latest dnf package to the /tmp/dnl directory (the directory must exist).</dd>
<dt><code>dnf download dnf &#8211;source</code></dt>
<dd>Download the latest dnf source package to the current directory.</dd>
<dt><code>dnf download btanks &#8211;resolve</code></dt>
<dd>Download the latest btanks package and the uninstalled dependencies to the current directory.</dd></dl>
<h2>Author</h2>
<p>See AUTHORS in your Core DNF Plugins distribution</p>
<h2>Copyright</h2>
<p>2014, Red Hat, Licensed under GPLv2+</p>
