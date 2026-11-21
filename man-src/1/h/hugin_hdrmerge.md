---

title: "hugin_hdrmerge(1)"
name: "hugin_hdrmerge"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hugin_hdrmerge/"
description: "hugin_hdrmerge – Merge overlapping images"
---

<p> <code>hugin_hdrmerge</code> [options] <code>-o</code> <i>output.exr</i> <i>input-files</i></p>
<p> <font SIZE="-1">TODO.</font></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> <i>prefix</i></dt>
<dd> Output file</dd>
<dt><code>-m</code> <i>mode</i></dt>
<dd> Merge mode, can be one of: avg, avg_slow, khan (default), if avg, no <code>-i</code>, <code>-s</code>, or <code>-d</code> options apply</dd>
<dt><code>-i</code> <i>iter</i></dt>
<dd> Number of iterations to execute (default is 1)</dd>
<dt><code>-c</code></dt>
<dd> Only consider pixels that are defined in all images (avg mode only)</dd>
<dt><code>-s</code> <i>file</i></dt>
<dd> Debug files to save each iteration, can be one of:</dd>
<dl>
<dl>
<dt>a &#8211; all debug files (can only be used alone)</dt>
<dd>
</dd><dt>w &#8211; calculated weights from each iteration</dt>
<dd>
</dd><dt>r &#8211; result image from each iteration</dt>
<dd>
</dd><dt>s &#8211; source images before processing</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> If verbose &gt;= 3, all debug files are output unless specified</dd></dl>
<dt><code>-a</code> <i>calcs</i></dt>
<dd> Apply one or more advanced calculations, can be one or more of:</dd>
<dl>
<dl>
<dt>b &#8211; biasing weights logarithmically</dt>
<dd>
</dd><dt>c &#8211; choose pixels with highest weight instead of averaging (overrides options <code>-a</code> <i>b</i> and <code>-a</code> <i>d</i>)</dt>
<dd>
</dd><dt>d &#8211; choose a pixel with the highest weight instead of averaging when all pixel weights are within 10% of each other</dt>
<dd>
</dd><dt>h &#8211; favour a high signal to noise ratio</dt>
<dd>
</dd><dt>i &#8211; ignore alpha channel</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-e</code></dt>
<dd> Export each initial weight to &lt;input_file_paths&gt;_iw.&lt;ext&gt;</dd>
<dt><code>-l</code></dt>
<dd> Load a previously exported initial weight with respect to the input file names </dd>
<p> <font SIZE="-1">NOTE:</font> if both <code>-e</code> and <code>-l</code> options are on, the program will calculate and save the initial weights, then wait until user indicates that it can continue by loading the previously saved weights</p>
<dt><code>-v</code></dt>
<dd> Verbose, print progress messages, repeat for even more verbose output</dd>
<dt><code>-h</code></dt>
<dd> Display help summary.</dd></dl>
<h2>AUTHORS</h2>
<p> Written by Jing Jin. Also contains contributions from Pablo d&#8217;Angelo, Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
