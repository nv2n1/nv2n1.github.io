---
title: "dnf-plugin-builddep(8)"
name: "dnf-plugin-builddep"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnf-plugin-builddep/"
description: "dnf.plugin.builddep – DNF builddep Plugin"
---

<p>dnf.plugin.builddep &#8211; DNF builddep Plugin </p>
<p> Install whatever is needed to build the given .src.rpm, .nosrc.rpm or .spec file.</p>
<h2>Synopsis</h2>
<p><code>dnf builddep &lt;file&gt;&#8230;</code></p>
<h2>Arguments</h2>
<dl>
<dt><code>&lt;file&gt;</code></p>
<dd>The path to .src.rpm, .nosrc.rpm or .spec file, to read the needed build requirements from.</dl>
<h2>Examples</h2>
<dl>
<dt><code>dnf builddep foobar.spec</code></p>
<dd>Install the needed build requirements, defined in the foobar.spec file.</p>
<dt><code>dnf builddep foobar-1.0-1.src.rpm</code></p>
<dd>Install the needed build requirements, defined in the foobar-1.0-1.src.rpm file.</dl>
<h2>Author</h2>
<p>See AUTHORS in your Core DNF Plugins distribution</p>
<h2>Copyright</h2>
<p>2014, Red Hat, Licensed under GPLv2+</p>
