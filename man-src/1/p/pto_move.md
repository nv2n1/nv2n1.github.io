---
title: "pto_move(1)"
name: "pto_move"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pto_move/"
description: "pto_move – Move a project file with all images in it."
---

<h2 class="name">NAME</h2>
<p> pto_move &#8211; Move a project file with all images in it. </p>
<h2>SYNOPSIS</h2>
<p> <code>pto_move</code> [options] path1/source.pto path2/dest.pto</p>
<h2>DESCRIPTION</h2>
<p> <code>pto_move</code> Moves a project file and all images to a new destination. Optionally copies; can be recursive, and can overwrite</p>
<h2>USAGE</h2>
<p> <code>pto_move</code> [options] path1/source.pto path2/dest.pto </p>
<p> Rename project file path1/source.pto to path2/dest.pto. All images contained in the project will be moved accordingly. </p>
<p> <code>pto_move</code> [options] sourceFolder destFolder </p>
<p> Moves all project files in the source folder to the destination folder including all images.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;copy</code></p>
<dd> Copy project files and images instead of moving</p>
<dt><code>&#8211;recursive</code></p>
<dd> Only effective in use case 2. Go recursive in the the source folder and move all project files with images to destination folder by maintaining the folder structure relative to source folder.</p>
<dt><code>&#8211;overwrite</code></p>
<dd> Overwrite all existing files. Otherwise you will be asked for each existing file.</dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
<h2>Index</h2>
