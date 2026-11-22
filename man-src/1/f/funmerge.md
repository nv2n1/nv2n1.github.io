---

title: "funmerge(1)"
name: "funmerge"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funmerge/"
description: "funmerge – merge one or more Funtools table files"
---

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
<p> <code>funmerge</code> merges FITS data from one or more FITS Binary Table files or raw event files. </p>
<p> The first argument to the program specifies the first input FITS table or raw event file. If &#8220;stdin&#8221; is specified, data are read from the standard input. Use Funtools Bracket Notation to specify FITS extensions and row filters. Subsequent arguments specify additional event files and tables to merge. (NB: Stdin cannot not be used for any of these additional input file arguments.) The last argument is the output FITS file. The columns in each input table must be identical. </p>
<p> If an input file begins with the &#8216;@&#8217; character, it is processed as an include file, i.e., as a text file containing event file names (as well as blank lines and/or comment lines starting with the &#8216;#&#8217; sign). If standard input is specified as an include file (&#8216;@stdin&#8217;), then file names are read from the standard input until EOF (^D). Event files and include files can be mixed on a command line. </p>
<p> Rows from each table are written sequentially to the output file. If the switch <code>-f [colname]</code> is specified on the command line, an additional column is added to each row containing the number of the file from which that row was taken (starting from one). In this case, the corresponding file names are stored in the header parameters having the prefix <code>FUNFIL</code>, i.e., FUNFIL01, FUNFIL02, etc. </p>
<p> Using the <code>-w</code> switch (or <code>-x</code> switch as described below), <code>funmerge</code> also can adjust the position column values using the WCS information in each file. (By position columns, we mean the columns that the table is binned on, i.e., those columns defined by the <code>bincols=</code> switch, or (X,Y) by default.) To perform WCS alignment, the WCS of the first file is taken as the base WCS. Each position in subsequent files is adjusted by first converting it to the sky coordinate in its own WCS coordinate system, then by converting this sky position to the sky position of the base WCS, and finally converting back to a pixel position in the base system. Note that in order to perform WCS alignment, the appropriate WCS and TLMIN/TLMAX keywords must already exist in each FITS file. </p>
<p> When performing WCS alignment, you can save the original positions in the output file by using the <code>-x</code> (for &#8220;xtra&#8221;) switch instead of the <code>-w</code> switch (i.e., using this switch also implies using <code>-w</code>) The old positions are saved in columns having the same name as the original positional columns, with the added prefix &#8220;OLD_&#8221;. </p>
<p> Examples: </p>
<p> Merge two tables, and preserve the originating file number for each row in the column called &#8220;FILE&#8221; (along with the corresponding file name in the header): </p>
<pre>
  [sh] funmerge -f &quot;FILE&quot; test.ev test2.ev merge.ev
</pre>
<p> Merge two tables with WCS alignment, saving the old position values in 2 additional columns: </p>
<pre>
  [sh] funmerge -x test.ev test2.ev merge.ev
</pre>
<p> This program only works on raw event files and binary tables. We have not yet implemented image and array merging.</p>
<h2>SEE ALSO</h2>
<p> See funtools(n) for a list of Funtools help pages </p>
