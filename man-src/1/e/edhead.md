---
title: "edhead(1)"
name: "edhead"
section: "1"
letter: "e"
url: "/docs/linux/man/1-edhead/"
description: "edhead – Edit header of FITS or IRAF image file"
---

<h2>Name</h2>
<p> edhead &#8211; Edit header of FITS or IRAF image file</p>
<h2>Synopsis</h2>
<p> edhead [options] FITS or IRAF file(s)</p>
<h2>Description</h2>
<p> Edit the header of the specified image file using the editor defined by the EDITOR environment variable. <i>edhead</i> takes care of trailing spaces so they can be ignored while using the editor.</p>
<h2>Options</h2>
<dl>
<dt><code>-e &lt;editor path&gt;</code></p>
<dd> Set editor, overiding environment EDITOR</p>
<dt><code>-n</code></p>
<dd> Write a new file with .e before the file type extension. The default is to overwrite the input file</p>
<dt><code>-v</code></p>
<dd> List processing steps</dl>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
