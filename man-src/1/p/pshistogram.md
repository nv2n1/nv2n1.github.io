---
title: "pshistogram(1)"
name: "pshistogram"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pshistogram/"
description: "pshistogram – Calculate and plot histograms"
---

<h2>NAME</h2>
<p> pshistogram &#8211; Calculate and plot histograms</p>
<h2>SYNOPSIS</h2>
<p> <code>pshistogram</code> [ <i>table</i> ] <code>x</code>|<code>X</code><i>parameters</i> <i>bin_width</i>[<code>+l</code>|<code>h</code>|<code>b</code>] [ ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>cpt</i> ] [ [<code>+b</code>][<code>+f</code><i>font</i>][<code>+o</code><i>off</i>][<code>+r</code>] ] [ ] [ <i>fill</i> ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ [<code>o</code>|<code>O</code>] ] [ ] [ <i>pen</i> ] [ [<i>mode</i>][<code>+p</code><i>pen</i>] ] [ ] [ ] [ ] [ <i>region</i> ] [ ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <i>type</i> ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>pshistogram</code> reads <i>file</i> [or standard input] and examines the first data column (or use <code>-i</code>) to calculate histogram parameters based on the bin-width provided. Using these parameters, scaling, and optional range parameters it will generate PostScript code that plots a histogram. A cumulative histogram may also be specified.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-Jx</code></p>
<dd> <i>xscale[/yscale]</i> (Linear scale(s) in distance unit/data unit).</p>
<dt><code>-W</code><i>bin_width</i>[<code>+l</code>|<code>h</code>|<code>b</code>]</p>
<dd> Sets the bin width used for histogram calculations. The modifiers specify the handling of extreme values that fall outside the range set by <code>-R</code>. By default these values are ignored. Use <code>+b</code> to let these values be included in the first or last bins. To only include extreme values below first bin into the first bin, use <code>+l</code>, and to only include extreme values above the last bin into that last bin, use <code>+h</code>.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code></p>
<dd> Plot the histogram horizontally from x = 0 [Default is vertically from y = 0].</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code><i>cpt</i></p>
<dd> Give a CPT file. The mid x-value for each bar is used to look-up the bar color.</p>
<dt><code>-D</code>[<code>+b</code>][<code>+f</code><i>font</i>][<code>+o</code><i>off</i>][<code>+r</code>]</p>
<dd> Annotate each bar with the count it represents. Append any of the following modifiers: Use <code>+b</code> to place the labels beneath the bars instead of above; use <code>+f</code> to change to another font than the default annotation font; use <code>+o</code> to change the offset between bar and label [6p]; use <code>+r</code> to rotate the labels from horizontal to vertical.</p>
<dt><code>-F</code></p>
<dd> Center bin on each value. [Default is left edge].</p>
<dt><code>-G</code><i>fill</i></p>
<dd> Select filling of bars [Default is no fill].</p>
<dt><code>-I</code>[<code>o</code>|<code>O</code>]</p>
<dd> Inquire about min/max x and y after binning. The <i>xmin xmax ymin ymax</i> is output; no plotting is done. Append <code>o</code> to output an ASCII table of the resulting x,y data instead. Upper case <code>O</code> will output all x,y bin data even when y == 0.</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code><i>pen</i></p>
<dd> Draw bar outline using the specified pen thickness. [Default is no outline].</p>
<dt><code>-N</code>[<i>mode</i>][<code>+p</code><i>pen</i>]</p>
<dd> Draw the equivalent normal distribution; append desired pen [0.5p,black]. The <i>mode</i> selects which central location and scale to use:</p>
<dt>&bull;</p>
<dd> 0 = mean and standard deviation [Default];</p>
<dt>&bull;</p>
<dd> 1 = median and L1 scale;</p>
<dt>&bull;</p>
<dd> 2 = LMS mode and scale. </p>
<p> The <code>-N</code> option may be repeated to draw several of these curves.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code></p>
<dd> Draw a cumulative histogram.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i> If not given, <code>pshistogram</code> will automatically find reasonable values for the region.</p>
<dt><code>-S</code></p>
<dd> Draws a stairs-step diagram which does not include the internal bars of the default histogram.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-Z</code><i>type</i></p>
<dd> Choose between 6 types of histograms:</p>
<dt>&bull;</p>
<dd> 0 = counts [Default]</p>
<dt>&bull;</p>
<dd> 1 = frequency_percent</p>
<dt>&bull;</p>
<dd> 2 = log (1.0 + count)</p>
<dt>&bull;</p>
<dd> 3 = log (1.0 + frequency_percent)</p>
<dt>&bull;</p>
<dd> 4 = log10 (1.0 + count)</p>
<dt>&bull;</p>
<dd> 5 = log10 (1.0 + frequency_percent).</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view.</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
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
<p> To draw a histogram of the data v3206.t containing seafloor depths, using a 250 meter bin width, center bars, and draw bar outline, use: </p>
<pre>
gmt pshistogram v3206.t -JXh -W250 -F -LP0.5p -V &gt; plot.ps
</pre>
<p> If you know the distribution of your data, you may explicitly specify range and scales. E.g., to plot a histogram of the y-values (2nd column) in the file errors.xy using a 1 meter bin width, plot from -10 to +10 meters @ 0.75 cm/m, annotate every 2 m and 100 counts, and use black bars, run: </p>
<pre>
gmt pshistogram errors.xy -W1 -R-10/10/0/0 -Jxc/0.01c \
                -Bx2+lError -By100+lCounts: -Gblack -i1 -V &gt; plot.ps
</pre>
<p> Since no y-range was specified, pshistogram will calculate ymax in even increments of 100.</p>
<h2>BUGS</h2>
<p> The <code>-W</code> option does not yet work properly with time series data (e.g., <code>-f</code>0T). Thus, such variable intervals as months and years are not calculated. Instead, specify your interval in the same units as the current setting of <code>TIME_UNIT</code>.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtcolors</code>, <code>psbasemap</code>, <code>psrose</code>, <code>psxy</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
