---
title: "kst(1)"
name: "kst"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kst/"
description: "kst – A plotting and data viewing program"
---

<h2>NAME</h2>
<p> kst &#8211; A plotting and data viewing program</p>
<h2>SYNOPSIS</h2>
<p> The options are:</p>
<dl>
<dt> <code>kst</code> [Qt-options] [KDE-options] [options] [<i>file</i>&#8230;] </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>[file&#8230;]</i></p>
<dd>
<dd>A .kst file, or one or more data files. Supported formats are ASCII columns, BOOMERANG frame files, BLAST dirfile files, and other optionally supported types. A .kst files stores all options that can be set by other flags. The following flags can be used to override the options set in the .kst file: <code>-F datafile</code>, <code>-n NS</code>, <code>-s NS</code>, <code>-f F0</code>, <code>-a</code>. The rest can not be overridden. If an override flag is given, it is applied to all vectors in the plot. </p>
<p> ASCII data from stdin can be plotted by including &quot;stdin&quot; in the list <code>[file&#8230;]</code>. </p>
<dt><code>-y Y</code></p>
<dd> The source for the Y axis data. For ASCII files, this is the column. For binary files, this is the field name. To plot multiple curves, this may be specified multiple times. The same source file, sample ranges, and X axis data are assumed. </p>
<dt><code>&#8211;ye equation</code></p>
<dd> The values for the Y axis data are calculated from the equation sepcified. Multiple equations are allowed. </p>
<dt><code>&#8211;xe X</code></p>
<dd> Use equation <code>x0:x1:n</code> to specify the X vector (INDEX). x0:x1 specifies the range of the vector, and n specifies the the number of values in X vector. </p>
<p> e.g. -10:10:21 creates this static vector: X = {-10,-9,-8,&#8230;0&#8230;8,9,10} </p>
<dt><code>-E text</code></p>
<dd> Pass argument to extension. <code>text</code> is of format <code>extensionname:argumentlist</code> </p>
<p> e.g. <code>kst -E js:&quot;loadScript(&#8216;intplTest.js&#8217;)&quot;</code> </p>
<dt><code>-e E</code></p>
<dd> Error bars for Y axis data. For ASCII file, refer to the column holding the data. For binary files use the field name. If multiple <code>-y Y</code> options are given, this may also be used multiple times. Individual Y entries are associated in order with multiple E entries. </p>
<dt><code>-x X</code></p>
<dd> The source for the X axis data. For ASCII files, this is the column. For readata files, this is the field name. If this option is not specified, the row number in the file is used. This option can only be given once. </p>
<dt><code>-z Z</code></p>
<dd> The source for the Z matrix data (which gets displayed as an image). For ASCII files, this is the column containing the z data. For other optional formats (HEALPix, FITS image, etc), this is the name of the desired matrix field, as displayed in the matrix dialog. Some matrix-compatible datasources also allow using an alias which is the number of the desired matrix field. To plot multiple matrices, this may be specified multiple times. </p>
<dt><code>-p P</code></p>
<dd> The source for power spectra. For ASCII files, this is the column. For binary files, this is the field name. To plot power spectra of multiple curves, this may be specified multiple times. The same source file, sample ranges and fft lengths are used for all Power Spectra requested from the command line. </p>
<dt><code>-l P</code></p>
<dd> The length of the FFT used in power specra estimation is 2^P. </p>
<dt><code>-r f</code></p>
<dd> Specify sample rate: <code>f</code> for power spectrum </p>
<dt><code>&#8211;ru U</code></p>
<dd> Specify the units <code>U</code> for psd sample rate </p>
<dt><code>&#8211;yu U</code></p>
<dd> Specify the units <code>U</code> for psd sample rate </p>
<dt><code>-h H</code></p>
<dd> The source for histograms. For ASCII files, this is the column. For binary files, this is the field name. Multiple histograms can be defined from the command line. </p>
<dt><code>-m NC</code></p>
<dd> Used when multiple curves have been defined. Rather than plotting all curves in the same plot, plot each in its own plot, </p>
<dt><code>-f F0</code></p>
<dd> The starting frame number (for readdata files) or row (for ASCII files) to read. </p>
<dt><code>-n</code></p>
<dd> The number of frames (for readdata files) or rows (for ASCII files) to read. </p>
<dt><code>-s NS</code></p>
<dd> The number of frames or rows to skip each read. This is useful when working with very large data files, to speed up response and conserve memory, in the case that the data are slowly varying. </p>
<dt><code>-g</code></p>
<dd> Provide a legend box </p>
<dt><code>-w file</code></p>
<dd> Display the data wizard </p>
<dt><code>&#8211;nq</code></p>
<dd> Bypass the quickstart dialog </p>
<dt><code>-a</code></p>
<dd> Used in with the <code> -s NS</code>: rather than skipping each NS frames, average them. This provides a combination of very basic high pass filtering, and memory conservation. </p>
<dt><code>-F Datafile</code></p>
<dd> Override the file to read the data from for all vectors listed in the .kst file. Can only be used in conjunction with a kst file. </p>
<dt><code>&#8211;print psfile</code></p>
<dd> Rather than displaying the plot, export the image to a postscript file and exit. *BUG note: even though no windows are opened on screen, access to the X server is still required.* </p>
<dt><code>&#8211;png pngfile</code></p>
<dd> Rather than displaying the plot, export the image to a png file of dimensions 640&#215;480 and exit. *BUG note: even though no windows are opened on screen, access to the X server is still required.* </p>
</dl>
<h2>COMMAND LINE EXAMPLES</h2>
<p> Several examples of typical use follow. </p>
<dl>
<dt>
<dd>
</dl>
<p> To plot column 1 a file (tmp.dat) of ASCII data: </p>
<dl>
<dt>
<dd> <code> kst -y 1 tmp.dat</code> </p>
<dt>
<dd>
</dl>
<p> To plot column 2, 3, and 4 vs. column 1 of an ASCII file, in 1 plot: </p>
<dl>
<dt>
<dd> <code>kst -x 1 -y 2 -y 3 -y 4 tmp.dat</code> </p>
<dt>
<dd>
</dl>
<p> To plot column 2, 3, and 4 vs. column 1 of an ASCII file, in 3 plots, arranged in 1 column: </p>
<dl>
<dt>
<dd> <code>kst -x 1 -y 2 -y 3 -y 4 -m 1 tmp.dat</code> </p>
<dt>
<dd>
</dl>
<p> To plot 500 rows of column 2 of an ASCII file, starting at line 100: </p>
<dl>
<dt>
<dd> <code>kst -y 2 -f 100 -n 500 tmp.dat</code> </p>
<dt>
<dd>
</dl>
<p> To plot the first 100,000 rows of column 2 of an ASCII file, averaging every 100 rows: </p>
<dl>
<dt>
<dd> <code>kst -y 2 -f 0 -n 100000 -s 100 -a tmp.dat</code> </p>
<dt>
<dd>
</dl>
<p> Using command to plot a spectrum from a data field of an ASCII data file with sample rate = 10HZ and FFT length = 2^14 </p>
<dl>
<dt>
<dd>
<p> <code> kst -p 2 /usr/share/apps/kst/tutorial/gytodata.dat -r 10 -l 14 </code><br />
&nbsp;<wbr> </p>
<dt>
<dd>
</dl>
<p> (Using optional HEALPix Data Source) To plot the first 3 maps in a HEALPix FITS file in a 2&#215;2 grid: </p>
<dl>
<dt>
<dd> <code>kst -z 1 -z 2 -z 3 -m 2 healpix_example_sm.fits</code> </p>
<dt>
<dd>
</dl>
<p> (Using optional HEALPix Data Source) To plot a map with a specific field name in a HEALPix FITS file: </p>
<dl>
<dt>
<dd> <code>kst -z &quot;1 &#8211; TEMPERATURE (Kelvin)&quot; healpix_example_sm.fits</code> </p>
</dl>
<h2>AUTHORS</h2>
<p> Duncan Hanson, Rick Chern, Philip Rodrigues, Barth Netterfield, Yiwen Mao. </p>
<h2>Index</h2>
