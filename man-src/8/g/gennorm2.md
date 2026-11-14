---
title: "gennorm2(8)"
name: "gennorm2"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gennorm2/"
description: "gennorm2 – Builds binary data file with Unicode normalization data."
---

<p><code>gennorm2</code> &#8211; Builds binary data file with Unicode normalization data.</p>
<h2>Synopsis</h2>
<p><code>gennorm2</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-u</code>, <code>&#8211;unicode</code><i> unicode-version-number</i> ] [ <code>-s</code>, <code>&#8211;sourcedir</code><i> source-directory</i> ] [ <code>-o</code>, <code>&#8211;output</code><i> output-filename</i> ] <code>&#8211;fast</code></p>
<h2>Description</h2>
<p><code>gennorm2</code> reads text files that define Unicode normalization, them, and builds a binary data file.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd>Print help about usage and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print the version of <code>gennorm2</code> and exit.</p>
<dt><code>-c</code>, <code>&#8211;copyright</code></p>
<dd>Include a copyright notice.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display extra informative messages during execution.</p>
<dt><code>-u</code>, <code>&#8211;unicode</code></p>
<dd>Specify Unicode version number, such as 5.2.0.</p>
<dt><code>-s</code>, <code>&#8211;sourcedir</code><i> source-directory</i></p>
<dd>Specify the input directory.</p>
<dt><code>-s</code>, <code>&#8211;sourcedir</code><i> source-directory</i></p>
<dd>Set the name of the output file.</p>
<dt><code>&#8211;fast</code></p>
<dd>optimize the .nrm file for fast normalization, which might increase its size (Writes fully decomposed regular mappings instead of delta mappings. You should measure the runtime speed to make sure that this is a good trade-off.)</dl>
<h2>Copyright</h2>
<p>Copyright (C) 2009-2010 International Business Machines Corporation and others</p>
