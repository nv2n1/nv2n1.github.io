---
title: "funmerge(1)"
name: "funmerge"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funmerge/"
description: "funmerge – merge one or more Funtools table files"
---

<h2>NAME</h2>
<p> <code>funmerge &#8211; merge one or more Funtools table files</code></p>
<h2>SYNOPSIS</h2>
<p> funmerge [-w|-x] -f [colname] &lt;iname1&gt; &lt;iname2&gt; &#8230; &lt;oname&gt;</p>
<h2>OPTIONS</h2>
<pre>
  -f    # output a column specifying file from which this event came
  -w    # adjust position values using WCS info
  -x    # adjust position values using WCS info and save old values
</pre>
<h2>DESCRIPTION</h2>
<p> <code>funmerge</code> merges <font SIZE="-1">FITS</font> data from one or more <font SIZE="-1">FITS</font> Binary Table files or raw event files. </p>
<p> The first argument to the program specifies the first input <font SIZE="-1">FITS</font> table or raw event file. If &#8220;stdin&#8221; is specified, data are read from the standard input. Use Funtools Bracket Notation to specify <font SIZE="-1">FITS</font> extensions and row filters. Subsequent arguments specify additional event files and tables to merge. (<font SIZE="-1">NB:</font> Stdin cannot not be used for any of these additional input file arguments.) The last argument is the output <font SIZE="-1">FITS</font> file. The columns in each input table must be identical. </p>
<p> If an input file begins with the &#8216;@&#8217; character, it is processed as an include file, i.e., as a text file containing event file names (as well as blank lines and/or comment lines starting with the &#8216;#&#8217; sign). If standard input is specified as an include file (&#8216;@stdin&#8217;), then file names are read from the standard input until <font SIZE="-1">EOF</font> (^D). Event files and include files can be mixed on a command line. </p>
<p> Rows from each table are written sequentially to the output file. If the switch <code>-f [colname]</code> is specified on the command line, an additional column is added to each row containing the number of the file from which that row was taken (starting from one). In this case, the corresponding file names are stored in the header parameters having the prefix <font SIZE="-1"><code>FUNFIL</code></font>, i.e., <font SIZE="-1">FUNFIL01</font>, <font SIZE="-1">FUNFIL02</font>, etc. </p>
<p> Using the <code>-w</code> switch (or <code>-x</code> switch as described below), <code>funmerge</code> also can adjust the position column values using the <font SIZE="-1">WCS</font> information in each file. (By position columns, we mean the columns that the table is binned on, i.e., those columns defined by the <code>bincols=</code> switch, or (X,Y) by default.) To perform <font SIZE="-1">WCS</font> alignment, the <font SIZE="-1">WCS</font> of the first file is taken as the base <font SIZE="-1">WCS</font>. Each position in subsequent files is adjusted by first converting it to the sky coordinate in its own <font SIZE="-1">WCS</font> coordinate system, then by converting this sky position to the sky position of the base <font SIZE="-1">WCS</font>, and finally converting back to a pixel position in the base system. Note that in order to perform <font SIZE="-1">WCS</font> alignment, the appropriate <font SIZE="-1">WCS</font> and <font SIZE="-1">TLMIN/TLMAX</font> keywords must already exist in each <font SIZE="-1">FITS</font> file. </p>
<p> When performing <font SIZE="-1">WCS</font> alignment, you can save the original positions in the output file by using the <code>-x</code> (for &#8220;xtra&#8221;) switch instead of the <code>-w</code> switch (i.e., using this switch also implies using <code>-w</code>) The old positions are saved in columns having the same name as the original positional columns, with the added prefix &#8220;<font SIZE="-1">OLD_</font>&#8221;. </p>
<p> Examples: </p>
<p> Merge two tables, and preserve the originating file number for each row in the column called &#8220;<font SIZE="-1">FILE</font>&#8221; (along with the corresponding file name in the header): </p>
<pre>
  [sh] funmerge -f &quot;FILE&quot; test.ev test2.ev merge.ev
</pre>
<p> Merge two tables with <font SIZE="-1">WCS</font> alignment, saving the old position values in 2 additional columns: </p>
<pre>
  [sh] funmerge -x test.ev test2.ev merge.ev
</pre>
<p> This program only works on raw event files and binary tables. We have not yet implemented image and array merging.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
