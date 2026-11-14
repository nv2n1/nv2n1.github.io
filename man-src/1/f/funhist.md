---
title: "funhist(1)"
name: "funhist"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funhist/"
description: "funhist – create a 1D histogram of a column (from a FITS binary table or raw event file) or an image"
---

<h2>NAME</h2>
<p> <code>funhist &#8211; create a 1D histogram of a column (from a FITS binary table or raw event file) or an image</code></p>
<h2>SYNOPSIS</h2>
<p> funhist [-n|-w|-T] &lt;iname&gt; [column] [[lo:hi:]bins]</p>
<h2>OPTIONS</h2>
<pre>
  -n    # normalize bin value by the width of each bin
  -w    # specify bin width instead of number of bins in arg3
  -T    # output in rdb/starbase format (tab separators)
</pre>
<h2>DESCRIPTION</h2>
<p> <code>funhist</code> creates a one-dimensional histogram from the specified columns of a <font SIZE="-1">FITS</font> Extension binary table of a <font SIZE="-1">FITS</font> file (or from a non-FITS raw event file), or from a <font SIZE="-1">FITS</font> image or array, and writes that histogram as an <font SIZE="-1">ASCII</font> table. Alternatively, the program can perform a 1D projection of one of the image axes. </p>
<p> The first argument to the program is required, and specifies the Funtools file: <font SIZE="-1">FITS</font> table or image, raw event file, or array. If &#8220;stdin&#8221; is specified, data are read from the standard input. Use Funtools Bracket Notation to specify <font SIZE="-1">FITS</font> extensions, and filters. </p>
<p> For a table, the second argument also is required. It specifies the column to use in generating the histogram. If the data file is of type image (or array), the column is optional: if &#8220;x&#8221; (or &#8220;X&#8221;), &#8220;y&#8221; (or &#8220;Y&#8221;) is specified, then a projection is performed over the x (dim1) or y (dim2) axes, respectively. (That is, this projection will give the same results as a histogram performed on a table containing the equivalent x,y event rows.) If no column name is specified or &#8220;xy&#8221; (or &#8220;<font SIZE="-1">XY</font>&#8221;) is specified for the image, then a histogram is performed on the values contained in the image pixels. </p>
<p> The argument that follows is optional and specifies the number of bins to use in creating the histogram and, if desired, the range of bin values. For image and table histograms, the range should specify the min and max data values. For image histograms on the x and y axes, the range should specify the min and max image bin values. If this argument is omitted, the number of output bins for a table is calculated either from the <font SIZE="-1">TLMIN/TLMAX</font> headers values (if these exist in the table <font SIZE="-1">FITS</font> header for the specified column) or by going through the data to calculate the min and max value. For an image, the number of output bins is calculated either from the <font SIZE="-1">DATAMIN/DATAMAX</font> header values, or by going through the data to calculate min and max value. (Note that this latter calculation might fail if the image cannot be fit in memory.) If the data are floating point (table or image) and the number of bins is not specified, an arbitrary default of 128 is used. </p>
<p> For binary table processing, the <code>-w</code> (bin width) switch can be used to specify the width of each bin rather than the number of bins. Thus: </p>
<pre>
  funhist test.ev pha 1:100:5
</pre>
<p> means that 5 bins of width 20 are used in the histogram, while: </p>
<pre>
  funhist -w test.ev pha 1:100:5
</pre>
<p> means that 20 bins of width 5 are used in the histogram. </p>
<p> The data are divvied up into the specified number of bins and the resulting 1D histogram (or projection) is output in <font SIZE="-1">ASCII</font> table format. For a table, the output displays the low_edge (inclusive) and hi_edge (exclusive) values for the data. For example, a 15-row table containing a &#8220;pha&#8221; column whose values range from -7.5 to 7.5 can be processed thus: </p>
<pre>
  [sh] funhist test.ev pha
  # data file:        /home/eric/data/test.ev
  # column:           pha
  # min,max,bins:     -7.5 7.5 15
</pre>
<pre><code>
bin value lo_edge hi_edge-- -- -- -- -- -- -- - -- -- -- -- -- -- -- -- -- -- - -- -- -- -- -- -- -- -- -- -- -1 22 - 7.50000000 - 6.50000000 2 21 - 6.50000000 - 5.50000000 3 20 - 5.50000000 - 4.50000000 4 19 - 4.50000000 - 3.50000000 5 18 - 3.50000000 - 2.50000000 6 17 - 2.50000000 - 1.50000000 7 16 - 1.50000000 - 0.50000000 8 30 - 0.50000000 0.50000000 9 16 0.50000000 1.50000000 10 17 1.50000000 2.50000000 11 18 2.50000000 3.50000000 12 19 3.50000000 4.50000000 13 20 4.50000000 5.50000000 14 21 5.50000000 6.50000000 15 22 6.50000000 7.50000000
</code></pre>
<pre>
  [sh] funhist test.ev pha 1:6
  # data file:          /home/eric/data/test.ev
  # column:             pha
  # min,max,bins:       0.5 6.5 6
</pre>
<p>bin value lo_edge hi_edge&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 16 0.50000000 1.50000000 2 17 1.50000000 2.50000000 3 18 2.50000000 3.50000000 4 19 3.50000000 4.50000000 5 20 4.50000000 5.50000000 6 21 5.50000000 6.50000000</p>
<pre>
  [sh] funhist test.ev pha 1:6:3
  # data file:          /home/eric/data/test.ev
  # column:             pha
  # min,max,bins:       0.5 6.5 3
</pre>
<p>bin value lo_edge hi_edge&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 33 0.50000000 2.50000000 2 37 2.50000000 4.50000000 3 41 4.50000000 6.50000000</p>
<p> For a table histogram, the <code>-n</code>(normalize) switch can be used to normalize the bin value by the width of the bin (i.e., hi_edge-lo_edge): </p>
<pre>
  [sh] funhist -n test.ev pha 1:6:3 
  # data file:          test.ev
  # column:             pha
  # min,max,bins:       0.5 6.5 3
  # width normalization (val/(hi_edge-lo_edge)) is applied
</pre>
<p>bin value lo_edge hi_edge&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 16.50000000 0.50000000 2.50000000 2 6.16666667 2.50000000 4.50000000 3 4.10000000 4.50000000 6.50000000</p>
<p> This could used, for example, to produce a light curve with values having units of counts/second instead of counts. </p>
<p> For an image histogram, the output displays the low and high image values (both inclusive) used to generate the histogram. For example, in the following example, 184 pixels had a value of 1, 31 had a value of 2, while only 2 had a value of 3,4,5,6, or 7: </p>
<pre>
  [sh] funhist test.fits
  # data file:           /home/eric/data/test.fits
  # min,max,bins:        1 7 7
</pre>
<p>bin value lo_val hi_val&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 184.00000000 1.00000000 1.00000000 2 31.00000000 2.00000000 2.00000000 3 2.00000000 3.00000000 3.00000000 4 2.00000000 4.00000000 4.00000000 5 2.00000000 5.00000000 5.00000000 6 2.00000000 6.00000000 6.00000000 7 2.00000000 7.00000000 7.00000000</p>
<p> For the axis projection of an image, the output displays the low and high image bins (both inclusive) used to generate the projection. For example, in the following example, 21 counts had their X bin value of 2, etc.: </p>
<pre>
  [sh] funhist test.fits x 2:7
  # data file:            /home/eric/data/test.fits
  # column:               X
  # min,max,bins: 2 7 6
</pre>
<p>bin value lo_bin hi_bin&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 21.00000000 2.00000000 2.00000000 2 20.00000000 3.00000000 3.00000000 3 19.00000000 4.00000000 4.00000000 4 18.00000000 5.00000000 5.00000000 5 17.00000000 6.00000000 6.00000000 6 16.00000000 7.00000000 7.00000000</p>
<pre>
  [sh] funhist test.fits x 2:7:2
  # data file:            /home/eric/data/test.fits
  # column:               X
  # min,max,bins: 2 7 2
</pre>
<p>bin value lo_bin hi_bin&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 60.00000000 2.00000000 4.00000000 2 51.00000000 5.00000000 7.00000000</p>
<p> You can use gnuplot or other plotting programs to graph the results, using a script such as: </p>
<pre><code>
#!/ bin / sh
sed - e '1,/---- .*/d / ^$ /, $d ' | \
  awk ' BEGIN{
                                  print "set nokey; set title \"funhist\"; set xlabel \"bin\"; set ylabel \"counts\"; plot \"-\" with boxes"}
{
    print $3, $2, $4 - $3
}
'        | \
  gnuplot -persist - 1&gt;/dev/null 2&gt;&amp;1
</code></pre>
<p> Similar plot commands are supplied in the script <code>funhist.plot</code>: </p>
<pre>
  funhist test.ev pha ...  | funhist.plot gnuplot
</pre>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
