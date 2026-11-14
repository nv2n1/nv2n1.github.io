---
title: "funtbl(1)"
name: "funtbl"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funtbl/"
description: "funtbl – extract a table from Funtools ASCII output"
---

<h2>NAME</h2>
<p> <code>funtbl &#8211; extract a table from Funtools ASCII output</code></p>
<h2>SYNOPSIS</h2>
<p> funtable [-c cols] [-h] [-n table] [-p prog] [-s sep] &lt;iname&gt;</p>
<h2>DESCRIPTION</h2>
<p> [<font SIZE="-1">NB:</font> This program has been deprecated in favor of the <font SIZE="-1">ASCII</font> text processing support in funtools. You can now perform fundisp on funtools <font SIZE="-1">ASCII</font> output files (specifying the table using bracket notation) to extract tables and columns.] </p>
<p> The <code>funtbl</code> script extracts a specified table (without the header and comments) from a funtools <font SIZE="-1">ASCII</font> output file and writes the result to the standard output. The first non-switch argument is the <font SIZE="-1">ASCII</font> input file name (i.e. the saved output from funcnts, fundisp, funhist, etc.). If no filename is specified, stdin is read. The -n switch specifies which table (starting from 1) to extract. The default is to extract the first table. The -c switch is a space-delimited list of column numbers to output, e.g. -c &#8220;1 3 5&#8221; will extract the first three odd-numbered columns. The default is to extract all columns. The -s switch specifies the separator string to put between columns. The default is a single space. The -h switch specifies that column names should be added in a header line before the data is output. Without the switch, no header is prepended. The -p program switch allows you to specify an awk-like program to run instead of the default (which is host-specific and is determined at build time). The -T switch will output the data in rdb format (i.e., with a 2-row header of column names and dashes, and with data columns separated by tabs). The -help switch will print out a message describing program usage. </p>
<p> For example, consider the output from the following funcnts command: </p>
<pre>
  [sh] funcnts -sr snr.ev &quot;ann 512 512 0 9 n=3&quot;
  # source
  #   data file:        /proj/rd/data/snr.ev
  #   arcsec/pixel:     8
  # background
  #   constant value:   0.000000
  # column units
  #   area:             arcsec**2
  #   surf_bri:         cnts/arcsec**2
  #   surf_err:         cnts/arcsec**2
</pre>
<pre><code>
#summed background - subtracted results
upto net_counts error background berror area surf_bri surf_err-- -- -- -- -- -- -- -- -- -- -- -- - -- -- -- -- -- -- -- -- -- -- - -- -- -- -- - -- -- -- -- - -- -- -- -- -1 147.000 12.124 0.000 0.000 1600.00 0.092 0.008 2 625.000 25.000 0.000 0.000 6976.00 0.090 0.004 3 1442.000 37.974 0.000 0.000 15936.00 0.090 0.002
</code></pre>
<p>#background &#8211; subtracted results<br />
reg net_counts error background berror area surf_bri surf_err&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -1 147.000 12.124 0.000 0.000 1600.00 0.092 0.008 2 478.000 21.863 0.000 0.000 5376.00 0.089 0.004 3 817.000 28.583 0.000 0.000 8960.00 0.091 0.003</p>
<p>#the following source and background components were used:<br />
source_region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;ann 512 512 0 9 n = 3</p>
<pre><code>
reg counts pixels sumcnts sumpix-- -- -- -- -- -- -- -- -- -- -- -- - -- -- -- -- -- -- -- -- -- -- -1 147.000 25 147.000 25 2 478.000 84 625.000 109 3 817.000 140 1442.000 249
</code></pre>
<p> There are four tables in this output. To extract the last one, you can execute: </p>
<pre>
  [sh] funcnts -s snr.ev &quot;ann 512 512 0 9 n=3&quot; | funtbl -n 4
  1 147.000 25 147.000 25
  2 478.000 84 625.000 109
  3 817.000 140 1442.000 249
</pre>
<p> Note that the output has been re-formatted so that only a single space separates each column, with no extraneous header or comment information. </p>
<p> To extract only columns 1,2, and 4 from the last example (but with a header prepended and tabs between columns), you can execute: </p>
<pre>
  [sh] funcnts -s snr.ev &quot;ann 512 512 0 9 n=3&quot; | funtbl -c &quot;1 2 4&quot; -h -n 4 -s &quot;	&quot;
  #reg    counts  sumcnts
  1       147.000 147.000
  2       478.000 625.000
  3       817.000 1442.000
</pre>
<p> Of course, if the output has previously been saved in a file named foo.out, the same result can be obtained by executing: </p>
<pre>
  [sh] funtbl -c &quot;1 2 4&quot; -h -n 4 -s &quot;	&quot; foo.out
  #reg    counts  sumcnts
  1       147.000 147.000
  2       478.000 625.000
  3       817.000 1442.000
</pre>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
