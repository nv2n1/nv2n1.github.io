---
title: "hugin_hdrmerge(1)"
name: "hugin_hdrmerge"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hugin_hdrmerge/"
description: "hugin_hdrmerge – Merge overlapping images"
---

<h2 class="name">NAME</h2>
<p> hugin_hdrmerge &#8211; Merge overlapping images </p>
<h2>SYNOPSIS</h2>
<p> <code>hugin_hdrmerge</code> [options] <code>-o</code> <i>output.exr</i> <i>input-files</i></p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">TODO.</font></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> <i>prefix</i></p>
<dd> Output file</p>
<dt><code>-m</code> <i>mode</i></p>
<dd> Merge mode, can be one of: avg, avg_slow, khan (default), if avg, no <code>-i</code>, <code>-s</code>, or <code>-d</code> options apply</p>
<dt><code>-i</code> <i>iter</i></p>
<dd> Number of iterations to execute (default is 1)</p>
<dt><code>-c</code></p>
<dd> Only consider pixels that are defined in all images (avg mode only)</p>
<dt><code>-s</code> <i>file</i></p>
<dd> Debug files to save each iteration, can be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt>a &#8211; all debug files (can only be used alone)</p>
<dd>
<dt>w &#8211; calculated weights from each iteration</p>
<dd>
<dt>r &#8211; result image from each iteration</p>
<dd>
<dt>s &#8211; source images before processing</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> If verbose &gt;= 3, all debug files are output unless specified</dl>
<dt><code>-a</code> <i>calcs</i></p>
<dd> Apply one or more advanced calculations, can be one or more of:</p>
<dl>
<dt>
<dd>
<dl>
<dt>b &#8211; biasing weights logarithmically</p>
<dd>
<dt>c &#8211; choose pixels with highest weight instead of averaging (overrides options <code>-a</code> <i>b</i> and <code>-a</code> <i>d</i>)</p>
<dd>
<dt>d &#8211; choose a pixel with the highest weight instead of averaging when all pixel weights are within 10% of each other</p>
<dd>
<dt>h &#8211; favour a high signal to noise ratio</p>
<dd>
<dt>i &#8211; ignore alpha channel</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-e</code></p>
<dd> Export each initial weight to &lt;input_file_paths&gt;_iw.&lt;ext&gt;</p>
<dt><code>-l</code></p>
<dd> Load a previously exported initial weight with respect to the input file names </p>
<p> <font SIZE="-1">NOTE:</font> if both <code>-e</code> and <code>-l</code> options are on, the program will calculate and save the initial weights, then wait until user indicates that it can continue by loading the previously saved weights</p>
<dt><code>-v</code></p>
<dd> Verbose, print progress messages, repeat for even more verbose output</p>
<dt><code>-h</code></p>
<dd> Display help summary.</dl>
<h2>AUTHORS</h2>
<p> Written by Jing Jin. Also contains contributions from Pablo d&#8217;Angelo, Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
<h2>Index</h2>
