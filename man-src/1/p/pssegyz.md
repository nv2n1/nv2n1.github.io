---
title: "pssegyz(1)"
name: "pssegyz"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pssegyz/"
description: "pssegyz – Create imagemasked postscript from SEGY file"
---

<h2>NAME</h2>
<p> pssegyz &#8211; Create imagemasked postscript from SEGY file</p>
<h2>SYNOPSIS</h2>
<p> <code>pssegyz</code> <i>SEGYfile</i> <i>parameters</i> <code>z</code>|<code>Z</code><i>parameters</i> <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] <i>deviation</i> [<i>color</i>] <code>-W</code> [ <i>clip</i> ] [ ] [ ] [ <i>nsamp</i> ] [ <i>ntrace</i> ] [ ] [ ] [ ] [ <i>&lt;mode&gt;&lt;value&gt;</i> ] [ <i>header_x</i>/<i>header_y</i> ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>pssegyz</code> reads a native (IEEE) format SEGY file and produces a PostScript image of the seismic data. The <i>imagemask</i> operator is used so that the seismic data are plotted as a 1-bit deep bitmap in a single (user-specified) color or gray shade, with a transparent background. The bitmap resolution is taken from the current GMT defaults. The seismic traces may be plotted at their true locations using information in the trace headers (in which case order of the traces in the file is not significant). Standard GMT geometry routines are used so that in principle any map projection may be used, however it is likely that the geographic projections will lead to unexpected results. Beware that a couple of the options for <code>pssegy</code> are not available in <code>pssegyz</code>. </p>
<p> Note that the order of operations before the seismic data are plotted is deviation*[clip]([bias]+[normalize](sample value)). Deviation determines how far <i>in the plot coordinates</i> a [normalized][biased][clipped] sample value of 1 plots from the trace location. </p>
<p> The SEGY file should be a disk image of the tape format (i.e., 3200 byte text header, which is ignored, 400 byte binary reel header, and 240 byte header for each trace) with samples as native real*4 (IEEE real on all the platforms to which I have access).</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>SEGYfile</i></p>
<dd> Seismic SEGY data set to be imaged.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</p>
<dt><code>-D</code><i>deviation</i></p>
<dd> gives the deviation in X units of the plot for 1.0 on the scaled trace, This may be a single number (applied equally in X and Y directions) or the pair <i>devX</i>/<i>devY</i>.</p>
<dt><code>-F</code>[<i>color</i>]</p>
<dd> Fill trace (variable area, defaults to filling positive). Specify the <i>color</i> with which the imagemask is filled.</p>
<dt><code>-W</code></p>
<dd> Draw wiggle trace. </p>
<p> You <i>must</i> specify at least one of <code>-W</code> and <code>-F</code>.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Flip the default byte-swap state (default assumes data have a bigendian byte-order).</p>
<dt><code>-C</code><i>clip</i></p>
<dd> Sample value at which to clip data (clipping is applied to both positive and negative values).</p>
<dt><code>-I</code></p>
<dd> Fill negative rather than positive excursions.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code><i>nsamp</i></p>
<dd> Override number of samples per trace in reel header (program attempts to determine number of samples from each trace header if possible to allow for variable length traces).</p>
<dt><code>-M</code><i>ntrace</i></p>
<dd> Override number of traces specified in reel header. Program detects end of file (relatively) gracefully, but this parameter limits number of traces that the program attempts to read.</p>
<dt><code>-N</code></p>
<dd> Normalize trace by dividing by rms amplitude over full trace length.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code><i>&lt;mode&gt;&lt;value&gt;</i></p>
<dd>
<dt><code>Can be used to change 5 different settings depending on </code><i>mode</i>:</p>
<dd> <code>-Qb</code><i>bias</i> to bias scaled traces (-Qb-0.1 subtracts 0.1 from values). </p>
<p> <code>-Qi</code><i>dpi</i> sets the dots-per-inch resolution of the image [300]. </p>
<p> <code>-Qu</code><i>redvel</i> to apply reduction velocity (-ve removes reduction already present). </p>
<p> <code>-Qx</code><i>mult</i> to multiply trace locations by <i>mult</i>. </p>
<p> <code>-Qy</code><i>dy</i> to override sample interval in reel header.</p>
<dt><code>-S</code><i>header_x</i>/<i>header_y</i></p>
<dd> Read trace locations from trace headers: headers is either <code>c</code> for CDP, <code>o</code> for offset, <code>b</code> *num* to read a long starting at byte <i>num</i> in the header (first byte corresponds to num=0), or a number to fix the location. First parameter for x, second for y. Default has X and Y given by trace number.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-Z</code></p>
<dd> Do not plot traces with zero rms amplitude.</p>
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
<p> To plot the SEGY file wa1.segy with normalized traces plotted at true offset locations, clipped at +/-3 and with wiggle trace and positive variable area shading in black, use </p>
<pre>
gmt pssegyz wa1.segy -JX5i/-5i -D1 -Jz0.05i -E180/5 -R0/100/0/10/0/10 \
        -C3 -N -So -W -Fblack &gt; segy.ps
</pre>
<h2>BUGS</h2>
<p> Variable area involves filling four-sided figures of distressing generality. I <i>know</i> that some of the more complex degenerate cases are not dealt with correctly or at all; the incidence of such cases increases as viewing angles become more oblique, and particularly as the viewing elevation increases. Wiggle-trace plotting is not affected.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>pssegy</code>, <code>segy2grd</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
