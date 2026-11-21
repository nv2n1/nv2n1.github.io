---

title: "autooptimiser(1)"
name: "autooptimiser"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autooptimiser/"
description: "autooptimiser – Optimize image positions"
---

<p> <code>autooptimiser</code> [options] <i>project.pto</i> </p>
<p> (<code>&#8211;</code> can be specified to read the project from stdio.)</p>
<p> autooptimiser works similarly to PToptimizer but with extra command-line options. </p>
<p> It is also different in that PToptimizer appends its output onto the input file in the form of &#8216;o&#8217; lines which need further processing. autooptimiser simply updates the project and writes it to a new file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> <i>file.pto</i></dt>
<dd> Output file. If omitted, stdout is used.</dd></dl>
<p> Optimisation options (if not specified, no optimisation takes place):</p>
<dl>
<dt><code>-a</code></dt>
<dd> Auto align mode, includes various optimisation stages, depending on the amount and distribution of the control points</dd>
<dt><code>-p</code></dt>
<dd> Pairwise optimisation of yaw, pitch and roll, starting from first image</dd>
<dt><code>-m</code></dt>
<dd> Optimise photometric parameters</dd>
<dt><code>-n</code></dt>
<dd> Optimize parameters specified in script file (like PToptimizer).</dd></dl>
<p> Post-processing options:</p>
<dl>
<dt><code>-l</code></dt>
<dd> Level horizon (works best for horizontal panoramas)</dd>
<dt><code>-s</code></dt>
<dd> Automatically select a suitable output projection and size</dd></dl>
<p> Other options:</p>
<dl>
<dt><code>-q</code></dt>
<dd> Quiet operation (no progress is reported)</dd>
<dt><code>-v</code> <i></i><font SIZE="-1"><i>HFOV</i></font><i></i></dt>
<dd> Specify horizontal field of view of input images. Used if the .pto file contains invalid <font SIZE="-1">HFOV</font> values (autopano-SIFT writes .pto files with invalid <font SIZE="-1">HFOV</font>)</dd></dl>
<p> When <code>-a</code>, <code>-l</code>, <code>-m</code> and <code>-s</code> options are used together, an operation similar to the one of the &#8220;Align&#8221; button in hugin is performed.</p>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo. Also contains contributions from Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
