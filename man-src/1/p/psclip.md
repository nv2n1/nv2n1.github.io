---
title: "psclip(1)"
name: "psclip"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psclip/"
description: "psclip – Initialize or terminate polygonal clip paths"
---

<h2>NAME</h2>
<p> psclip &#8211; Initialize or terminate polygonal clip paths</p>
<h2>SYNOPSIS</h2>
<p> <code>psclip</code> [ <i>table</i> ] <i>parameters</i> [<i>n</i>] <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] [ [<code>m</code>|<code>p</code>|<code>x</code>|<code>y</code>] ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] <code>z</code>|<code>Z</code><i>parameters</i> ] [ ] [ ] [ ] [ ] [ ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psclip</code> reads (x,y) file(s) [or standard input] and draws polygons that are activated as clipping paths. Several files may be read to create complex paths consisting of several non-connecting segments. Only marks that are subsequently drawn inside the clipping path will be shown. To determine what is inside or outside the clipping path, <code>psclip</code> uses the even-odd rule. When a ray drawn from any point, regardless of direction, crosses the clipping path segments an odd number of times, the point is inside the clipping path. If the number is even, the point is outside. The <code>-N</code> option, reverses the sense of what is the inside and outside of the paths by plotting a clipping path along the map boundary. After subsequent plotting, which will be clipped against these paths, the clipping may be deactivated by running <code>psclip</code> a second time with the <code>-C</code> option only.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-C</code>[|<i>n</i>]</p>
<dd> Mark end of existing clip path(s). No input file will be processed. No projection information is needed unless <code>-B</code> has been selected as well. With no arguments we terminate all active clipping paths. Experts may restrict the termination to just <i>n</i> of the active clipping path by passing that as the argument. Remember to supply <code>-X</code> and <code>-Y</code> settings if you have moved since the clip started.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code>[<code>m</code>|<code>p</code>|<code>x</code>|<code>y</code>]</p>
<dd> By default, geographic line segments are connected as great circle arcs. To connect them as straight lines, use the <code>-A</code> flag. Alternatively, add <code>m</code> to connect the line by first following a meridian, then a parallel. Or append <code>p</code> to start following a parallel, then a meridian. (This can be practical to connect lines along parallels, for example). For Cartesian data, points are simply connected, unless you append <code>x</code> or <code>y</code> to construct stair-case paths whose first move is along <i>x</i> or <i>y</i>, respectively.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-N</code></p>
<dd> Invert the sense of what is inside and outside. For example, when using a single path, this means that only points outside that path will be shown. Cannot be used together with <code>-B</code>.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-T</code></p>
<dd> Rather than read any input files, simply turn on clipping for the current map region. Basically, <code>-T</code> is a convenient way to run <code>psclip</code> with the arguments <code>-N</code> /dev/null (or, under Windows, <code>-N</code> NUL). Cannot be used together with <code>-B</code>.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view.</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
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
<h2>EXAMPLES</h2>
<p> To make an overlay PostScript file that will set up a complex clip area to which subsequent plotting will be confined, run: </p>
<pre>
gmt psclip my_region.xy -R0/40/0/40 -Jm0.3i -O -K &gt; clip_mask_on.ps
</pre>
<p> To deactivate the clipping in an existing plotfile, run: </p>
<pre>
gmt psclip -C -O &gt;&gt; complex_plot.ps
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdmask</code>, <code>psbasemap</code>, <code>psmask</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
