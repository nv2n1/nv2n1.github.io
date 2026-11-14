---
title: "x2sys_solve(1)"
name: "x2sys_solve"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_solve/"
description: "x2sys_solve – Determine least-squares systematic correction from crossovers"
---

<h2>NAME</h2>
<p> x2sys_solve &#8211; Determine least-squares systematic correction from crossovers</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_solve</code> <i>column</i> <i>TAG</i> <i>mode</i> [ <i>COE_list.d</i> ] [ [<i>level</i>] ] [ <code>[u]</code> ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-x</code>[[-]<i>n</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_solve</code> will use the supplied crossover information to solve for systematic corrections that can then be applied per track to improve data quality. Several systematic corrections can be solved for using a least-squares approach. Note: Only one data column can be processed at the time.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>COE_list.d</i></p>
<dd> Name of file with the required crossover columns as produced by <code>x2sys_list</code>. NOTE: If <code>-bi</code> is used then the first two columns are expected to hold the integer track IDs; otherwise we expect those columns to hold the text string names of the two tracks. If no file is given we will read from <i>stdin</i>.</p>
<dt><code>-T</code><i>TAG</i></p>
<dd> Specify the x2sys <i>TAG</i> which tracks the attributes of this data type.</p>
<dt><code>-C</code><i>column</i></p>
<dd> Specify which data column you want to process. Needed for proper formatting of the output correction table and must match the same option used in <code>x2sys_list</code> when preparing the input data.</p>
<dt><code>-E</code><i>mode</i></p>
<dd> The correction type you wish to model. Choose among the following functions f(<i>p</i>) , where <i>p</i> are the <i>m</i> parameters per track that we will fit simultaneously using a least squares approach: </p>
<p> <code>c</code> will fit f(<i>p</i>) = <i>a</i> (a constant offset); records must contain cruise ID1, ID2, COE. </p>
<p> <code>d</code> will fit f(<i>p</i>) = <i>a</i> + <i>b</i> * <i>d</i> (linear drift; <i>d</i> is distance; records must contain cruise ID1, ID2, d1, d2, COE. </p>
<p> <code>g</code> will fit f(<i>p</i>) = <i>a</i> + <i>b</i> sin(y)^2 (1980-1930 gravity correction); records must contain cruise ID1, ID2, latitude y, COE. </p>
<p> <code>h</code> will fit f(<i>p</i>) = <i>a</i> + <i>b</i> cos(H) + <i>c</i> <a href="//www.systutorials.com/docs/linux/man/2H-cos/">cos</a>(2H) + <i>d</i> sin(H) + <i>e</i> <a href="//www.systutorials.com/docs/linux/man/2H-sin/">sin</a>(2H) (magnetic heading correction); records must contain cruise ID1, ID2, heading H, COE. </p>
<p> <code>s</code> will fit f(<i>p</i>) = <i>a</i> * z (a unit scale correction); records must contain cruise ID1, ID2, z1, z2. </p>
<p> <code>t</code> will fit f(<i>p</i>) = <i>a</i> + <i>b</i> * (<i>t &#8211; t0</i>) (linear drift; <i>t0</i> is the start time of the track); records must contain cruise ID1, ID2, t1-t0, t2-t0, COE.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code></p>
<dd> Means that each input records has an extra column with the composite weight for each crossover record. These are used to obtain a weighted least squares solution [no weights]. Append <code>u</code> to report unweighted mean/std [Default, report weighted stats].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input.</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-x</code>[[-]<i>n</i>] <i>(more &#8230;)</i></p>
<dd> Limit number of cores used in multi-threaded algorithms (OpenMP required).</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit.</dl>
<h2>NOTES</h2>
<p> Most of the model corrections in involve a constant offset. Because crossovers are differences between values, any absolute level will cancel out and hence the constant offsets we obtain are relative to an undetermined absolute level. To obtain a solvable solution we add the constraint that the sum of all constant offsets equal zero. If the tracks form clusters in which no tracks from one cluster cross any track from another cluster then these are two independent data sets and require they own constraint equation for their offsets. We determine the number of clusters and automatically add the required constraint equations. If you need a particular reference track to have a particular offset (e.g., 0) then you can subtract the offset you found from every track correction and add in the desired offset.</p>
<h2>EXAMPLES</h2>
<p> To fit a simple bias offset to faa for all tracks under the MGD77 tag, try </p>
<pre>
gmt x2sys_list COE_data.txt -V -TMGD77 -Cfaa -Fnc &gt; faa_coe.txt
gmt x2sys_solve faa_coe.txt -V -TMGD77 -Cfaa -Ec &gt; coe_table.txt
</pre>
<p> To fit a faa linear drift with time instead, try </p>
<pre>
gmt x2sys_list COE_data.txt -V -TMGD77 -Cfaa -FnTc &gt; faa_coe.txt
gmt x2sys_solve faa_coe.txt -V -TMGD77 -Cfaa -Et &gt; coe_table.txt
</pre>
<p> To estimate heading corrections based on magnetic crossovers associated with the tag MGD77 from the file COE_data.txt, try </p>
<pre>
gmt x2sys_list COE_data.txt -V -TMGD77 -Cmag -Fnhc &gt; mag_coe.txt
gmt x2sys_solve mag_coe.txt -V -TMGD77 -Cmag -Eh &gt; coe_table.txt
</pre>
<p> To estimate unit scale corrections based on bathymetry crossovers, try </p>
<pre>
gmt x2sys_list COE_data.txt -V -TMGD77 -Cdepth -Fnz &gt; depth_coe.txt
gmt x2sys_solve depth_coe.txt -V -TMGD77 -Cdepth -Es &gt; coe_table.txt
</pre>
<h2>SEE ALSO</h2>
<p> <code>x2sys_binlist</code>, <code>x2sys_cross</code>, <code>x2sys_datalist</code>, <code>x2sys_get</code>, <code>x2sys_init</code>, <code>x2sys_list</code>, <code>x2sys_put</code>, <code>x2sys_report</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
