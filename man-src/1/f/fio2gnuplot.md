---
title: "fio2gnuplot(1)"
name: "fio2gnuplot"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fio2gnuplot/"
description: "fio2gnuplot – Render fio’s output files with gnuplot"
---

<h2>NAME</h2>
<p> <code>fio2gnuplot </code>&#8211; Render fio&#8217;s output files with gnuplot</p>
<h2>SYNOPSIS</h2>
<pre><code>
fio2gnuplot[-ghbiodvk][-t title][-o outputfile]
           [-d output_dir][-p pattern]
           [-G type][-m min_time][-M max_time]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>fio2gnuplot</code> analyze a set of fio&#8217;s log files to turn them into a set of graphical traces using gnuplot tool. Several flavor of plotting are produced</p>
<dl>
<dt><code>Individual 2D Graph</code></p>
<dd> Each file is plotted in a separate image file with several option</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> raw : Plot the exact reported performance. This plotting could be difficult to read</p>
<dt>&bull;</p>
<dd> smooth :a smoother version of the raw print Using csplines option of gnuplot, the rendering is filtered to get an easier to read graph.</p>
<dt>&bull;</p>
<dd> trend : an even smoother version of the raw print to get trends Bezier&#8217;s curves makes much more filtered plots The resulting graph helps at understanding trends.</dl>
</dl>
<dt><code>Grouped 2D graph</code></p>
<dd> All files are plotted in a single image to ease the comparaison. The same rendering options as per the individual 2D graph are used :</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> raw</p>
<dt>&bull;</p>
<dd> smooth</p>
<dt>&bull;</p>
<dd> trend</dl>
</dl>
<dt><code>Grouped 3D graph</code></p>
<dd> All files are plotted into a single 3D graph. The 3D plotting generates a &#8216;surface&#8217; to estimate how close were the performance. A flat surface means a good coherency between traces. A rugged surface means a lack of coherency between traces</p>
<dt><code>Mathemical Plotting</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Average graph</code></p>
<dd> A bar graph to show the average performance of each file. A green line is added to show the global average performance. This green line helps at understanding how far from the average is every individual file.</p>
<dt><code>Min graph</code></p>
<dd> A green line is added to show the global average of minimal performance. This green line helps at understanding how far from the average is every individual file.</p>
<dt><code>Max graph</code></p>
<dd> A bar graph to show the maximum performance of each file. A green line is added to show the global average of maximal performance. This green line helps at understanding how far from the average is every individual file.</p>
<dt><code>Standard Deviation</code></p>
<dd> A bar graph to show the standard deviation of each file. A green line is added to show the global average of standard deviation. This green line helps at understanding how far from the average is every individual file.</dl>
</dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> The option <code>-h</code> displays help</p>
<dt><code>-p</code> &#8216;<i>pattern</i>&#8216; or &#8212;<i>pattern</i> &#8216;<i>pattern</i>&#8216;</p>
<dd> A <i>pattern</i> in regexp to select fio input files. Don&#8217;t forget the simple quotes to avoid shell&#8217;s interactions</p>
<dt><code>-b</code> or <code>&#8211;bandwidth</code></p>
<dd> A predefined <i>pattern</i> for selecting *_bw.log files</p>
<dt><code>-i</code> or <code>&#8211;iops</code></p>
<dd> A predefined <i>pattern</i> for selecting *_iops.log files</p>
<dt><code>-g</code> or <code>&#8211;gnuplot</code></p>
<dd> Render gnuplot traces before exiting</p>
<dt><code>-o</code> file or &#8212;<i>outputfile</i> file</p>
<dd> The basename for gnuplot traces (set with the <i>pattern</i> if defined)</p>
<dt><code>-d</code> dir or <code>&#8211;outputdir</code> dir</p>
<dd> The directory where gnuplot shall render files.</p>
<dt><code>-t</code> <i>title</i> or &#8212;<i>title</i> <i>title</i></p>
<dd> The <i>title</i> of the gnuplot traces. Title is set with the block size detected in fio trace</p>
<dt><code>-G</code> <i>type</i> or <code>&#8211;Global</code> <i>type</i></p>
<dd> Search for &#8216;<i>type</i>&#8216; in .global files match by a <i>pattern</i>. Available types are : min, max, avg, stddev. The .global extension is added automatically to the <i>pattern</i></p>
<dt><code>-m</code> time or &#8212;<i>min_time</i> time</p>
<dd> Only consider data starting from &#8216;time&#8217; seconds. Default is 0</p>
<dt><code>-M</code> time or &#8212;<i>max_time</i> time</p>
<dd> Only consider data ending before &#8216;time&#8217; seconds. Default is <code>-1</code> aka nolimit</p>
<dt><code>-v</code> or <code>&#8211;verbose</code></p>
<dd> Increasing verbosity</p>
<dt><code>-k</code> or <code>&#8211;keep</code></p>
<dd> Keep all temporary files from gnuplot&#8217;s output dir</dl>
<h2>EXAMPLE</h2>
<dl>
<dt><code>To plot all the traces named like &#8216;host*_read_4k_iops.log&#8217;</code></p>
<dd> $ <code>fio2gnuplot</code> <code>-p</code> &#8216;host*_read_4k_iops.log&#8217; <code>-g</code></p>
<dt><code>To plot all IO oriented log files from the current directory</code></p>
<dd> $ <code>fio2gnuplot</code> <code>-g</code> <code>-i</code></p>
<dt><code>To plot all Bandwidth oriented log files from the current directory</code></p>
<dd> $ <code>fio2gnuplot</code> <code>-g</code> <code>-b</code></p>
<dt><code>To plot all Bandwidth oriented log files in a directory name &#8216;outdir&#8217;</code></p>
<dd> $ <code>fio2gnuplot</code> <code>-g</code> <code>-b</code> <code>-d</code> outdir</dl>
<h2>AUTHOR</h2>
<p> Erwan Velu &lt;erwan [at] enovance.com&gt; </p>
<h2>Index</h2>
