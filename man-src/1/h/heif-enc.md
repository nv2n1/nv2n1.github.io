---
title: "heif-enc(1)"
name: "heif-enc"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heif-enc/"
description: "heif-enc – convert image to HEIC/HEIF"
---

<h2 class="name">NAME</h2>
<p> heif-enc &#8211; convert image to HEIC/HEIF </p>
<h2>SYNOPSIS</h2>
<p> <code>heif-enc</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-q</code> <i>QUALITY</i>|<code>&#8211;quality</code> <i>QUALITY</i>] [<code>-L</code>|<code>&#8211;lossless</code>] [<code>-t</code> <i>SIZE</i>|<code>&#8211;thumb</code> <i>SIZE</i>] [<code>&#8211;no-alpha</code>] [<code>&#8211;no-thumb-alpha</code>] [<code>-o</code> <i>FILENAME</i>|<code>&#8211;output</code> <i>FILENAME</i>] [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-P</code>|<code>&#8211;params</code>] [<code>-b</code> <i>DEPTH</i>] [<code>-p</code> <i>NAME</i><code>=</code><i>VALUE</i>] <i>filename[.jpg|.png|.y4m]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>heif-enc</code> Convert image to HEIC/HEIF.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code>&nbsp;<i>QUALITY</i>, <code>&#8211;quality</code>&nbsp;<i>QUALITY</i></p>
<dd> Defines quality level between 0 and 100 for the generated output file.</p>
<dt><code>-L</code>, &#8211;lossless</p>
<dd> Generate lossless output (<code>-q</code> has no effect)</p>
<dt><code>-t</code>&nbsp;<i>SIZE</i>, <code>&#8211;thumb</code>&nbsp;<i>SIZE</i></p>
<dd> Generate thumbnail with maximum size <i>SIZE</i> pixels (default: off).</p>
<dt><code>&#8211;no-alpha</code></p>
<dd> Do not save alpha channel.</p>
<dt><code>&#8211;no-thumb-alpha</code></p>
<dd> Do not save alpha channel in thumbnail image.</p>
<dt><code>-o</code>&nbsp;<i>FILENAME</i>, <code>&#8211;output</code>&nbsp;<i>FILENAME</i></p>
<dd> Output filename (optional).</p>
<dt><code>-v</code>, &#8211;verbose</p>
<dd> Enable logging output (more <code>-v</code> will increase logging level).</p>
<dt><code>-P</code>, &#8211;params</p>
<dd> Show all encoder parameters.</p>
<dt><code>-b</code>&nbsp;<i>DEPTH</i></p>
<dd> Bit-depth of generated HEIF file when using 16-bit PNG input (default: 10 bit).</p>
<dt><code>-p</code>&nbsp;<i>NAME</i><code>=</code><i>VALUE</i></p>
<dd> Set additional encoder parameters. See <code>NOTES</code> below.</dl>
<h2>EXIT STATUS</h2>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Success</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Failure (syntax or usage error; error while loading, converting or writing image).</dl>
<h2>NOTES</h2>
<p> The available input formats depend on the libraries that were available at compile time. Supported are JPEG, PNG and Y4M, the file type is determined based on the extension of the input file. </p>
<p> When specifying multiple source images, they will all be saved into the same HEIF file. </p>
<p> When using the x265 encoder, you may pass it any of its parameters by prefixing the parameter name with <code>x265:</code>. Hence, to set the <code>ctu</code> parameter, you will have to set <code>x265:ctu</code> in libheif (e.g.: <code>-p x265:ctu=64</code>). </p>
<p> Note that there is no checking for valid parameters when using the prefix.</p>
<h2>BUGS</h2>
<p> Please reports bugs or issues at <a rel="nofollow" href="https://github.com/strukturag/libheif">https://github.com/strukturag/libheif</a></p>
<h2>AUTHORS</h2>
<p> Dirk Farin, struktur AG</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2017 struktur AG </p>
<h2>Index</h2>
