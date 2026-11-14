---
title: "gio-querymodules(1)"
name: "gio-querymodules"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gio-querymodules/"
description: "gio-querymodules – GIO module cache creation"
---

<h2 class="name">NAME</h2>
<p> gio-querymodules &#8211; GIO module cache creation </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gio-querymodules</code> {DIRECTORY&#8230;}</dl>
<h2>DESCRIPTION</h2>
<p> <code>gio-querymodules</code></p>
<dd>creates a giomodule.cache file in the listed directories. This file lists the implemented extension points for each module that has been found. It is used by GIO at runtime to avoid opening all modules just to find out which extension points they are implementing. </p>
<p> GIO modules are usually installed in the gio/modules subdirectory of libdir. </p>
<h2>Index</h2>
