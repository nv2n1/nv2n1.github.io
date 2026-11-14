---
title: "funjoin(1)"
name: "funjoin"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funjoin/"
description: "funjoin – join two or more FITS binary tables on specified columns"
---

<h2>NAME</h2>
<p> <code>funjoin &#8211; join two or more FITS binary tables on specified columns</code></p>
<h2>SYNOPSIS</h2>
<p> funjoin [switches] &lt;ifile1&gt; &lt;ifile2&gt; &#8230; &lt;ifilen&gt; &lt;ofile&gt;</p>
<h2>OPTIONS</h2>
<pre><code>
  -a  cols             # columns to activate in all files
  -a1 cols ... an cols # columns to activate in each file
  -b  'c1:bvl,c2:bv2'  # blank values for common columns in all files
  -bn 'c1:bv1,c2:bv2'  # blank values for columns in specific files
  -j  col              # column to join in all files
  -j1 col ... jn col   # column to join in each file
  -m min               # min matches to output a row
  -M max               # max matches to output a row
  -s                   # add 'jfiles' status column
  -S col               # add col as status column
  -t tol               # tolerance for joining numeric cols [2 files only]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>funjoin</code> joins rows from two or more (up to 32) <font SIZE="-1">FITS</font> Binary Table files, based on the values of specified join columns in each file. <font SIZE="-1">NB:</font> the join columns must have an index file associated with it. These files are generated using the <code>funindex</code> program. </p>
<p> The first argument to the program specifies the first input <font SIZE="-1">FITS</font> table or raw event file. If &#8220;stdin&#8221; is specified, data are read from the standard input. Subsequent arguments specify additional event files and tables to join. The last argument is the output <font SIZE="-1">FITS</font> file. </p>
<p> <font SIZE="-1">NB:</font> Do <code>not</code> use Funtools Bracket Notation to specify <font SIZE="-1">FITS</font> extensions and row filters when running funjoin or you will get wrong results. Rows are accessed and joined using the index files directly, and this bypasses all filtering. </p>
<p> The join columns are specified using the <code>-j col</code> switch (which specifies a column name to use for all files) or with <code>-j1 col1</code>, <code>-j2 col2</code>, &#8230; <code>-jn coln</code> switches (which specify a column name to use for each file). A join column must be specified for each file. If both <code>-j col</code> and <code>-jn coln</code> are specified for a given file, then the latter is used. Join columns must either be of type string or type numeric; it is illegal to mix numeric and string columns in a given join. For example, to join three files using the same key column for each file, use: </p>
<pre>
  funjoin -j key in1.fits in2.fits in3.fits out.fits
</pre>
<p> A different key can be specified for the third file in this way: </p>
<pre>
  funjoin -j key -j3 otherkey in1.fits in2.fits in3.fits out.fits
</pre>
<p> The <code>-a &#8220;cols&#8221;</code> switch (and <code>-a1 &#8220;col1&#8221;</code>, <code>-a2 &#8220;cols2&#8221;</code> counterparts) can be used to specify columns to activate (i.e. write to the output file) for each input file. By default, all columns are output. </p>
<p> If two or more columns from separate files have the same name, the second (and subsequent) columns are renamed to have an underscore and a numeric value appended. </p>
<p> The <code>-m min</code> and <code>-M max</code> switches specify the minimum and maximum number of joins required to write out a row. The default minimum is 0 joins (i.e. all rows are written out) and the default maximum is 63 (the maximum number of possible joins with a limit of 32 input files). For example, to write out only those rows in which exactly two files have columns that match (i.e. one join): </p>
<pre>
  funjoin -j key -m 1 -M 1 in1.fits in2.fits in3.fits ... out.fits
</pre>
<p> A given row can have the requisite number of joins without all of the files being joined (e.g. three files are being joined but only two have a given join key value). In this case, all of the columns of the non-joined file are written out, by default, using blanks (zeros or NULLs). The <code>-b c1:bv1,c2:bv2</code> and <code>-b1 &#8216;c1:bv1,c2:bv2&#8217; -b2 &#8216;c1:bv1,c2:bv2&#8217; &#8230;</code> switches can be used to set the blank value for columns common to all files and/or columns in a specified file, respectively. Each blank value string contains a comma-separated list of column:blank_val specifiers. For floating point values (single or double), a case-insensitive string value of &#8220;nan&#8221; means that the <font SIZE="-1">IEEE</font> NaN (not-a-number) should be used. Thus, for example: </p>
<pre>
  funjoin -b &quot;AKEY:???&quot; -b1 &quot;A:-1&quot; -b3 &quot;G:NaN,E:-1,F:-100&quot; ...
</pre>
<p> means that a non-joined <font SIZE="-1">AKEY</font> column in any file will contain the string &#8220;???&#8221;, the non-joined A column of file 1 will contain a value of -1, the non-joined G column of file 3 will contain <font SIZE="-1">IEEE</font> NaNs, while the non-joined E and F columns of the same file will contain values -1 and -100, respectively. Of course, where common and specific blank values are specified for the same column, the specific blank value is used. </p>
<p> To distinguish which files are non-blank components of a given row, the <code>-s</code> (status) switch can be used to add a bitmask column named &#8220;<font SIZE="-1">JFILES</font>&#8221; to the output file. In this column, a bit is set for each non-blank file composing the given row, with bit 0 corresponds to the first file, bit 1 to the second file, and so on. The file names themselves are stored in the <font SIZE="-1">FITS</font> header as parameters named <font SIZE="-1">JFILE1</font>, <font SIZE="-1">JFILE2</font>, etc. The <code>-S col</code> switch allows you to change the name of the status column from the default &#8220;<font SIZE="-1">JFILES</font>&#8221;. </p>
<p> A join between rows is the Cartesian product of all rows in one file having a given join column value with all rows in a second file having the same value for its join column and so on. Thus, if file1 has 2 rows with join column value 100, file2 has 3 rows with the same value, and file3 has 4 rows, then the join results in 2*3*4=24 rows being output. </p>
<p> The join algorithm directly processes the index file associated with the join column of each file. The smallest value of all the current columns is selected as a base, and this value is used to join equal-valued columns in the other files. In this way, the index files are traversed exactly once. </p>
<p> The <code>-t tol</code> switch specifies a tolerance value for numeric columns. At present, a tolerance value can join only two files at a time. (A completely different algorithm is required to join more than two files using a tolerance, somethng we might consider implementing in the future.) </p>
<p> The following example shows many of the features of funjoin. The input files t1.fits, t2.fits, and t3.fits contain the following columns: </p>
<p>[sh] fundisp t1.fits<br />
    AKEY KEY A B&#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;aaa 0 0 1 bbb 1 3 4 ccc 2 6 7 ddd 3 9 10 eee 4 12 13 fff 5 15 16 ggg 6 18 19 hhh 7 21 22</p>
<p> fundisp t2.fits<br />
&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">AKEY</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">KEY</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>D&nbsp;<wbr><br />
&nbsp;<wbr>&#8212;&#8212;&#8212;&#8211; &#8212;&#8212; &#8212;&#8212; &#8212;&#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>iii&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>24&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>25<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ggg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>18&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>19<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>eee&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ccc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>7<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>aaa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1 </p>
<p> fundisp t3.fits<br />
&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">AKEY</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">KEY</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>E&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G &#8212;&#8212;&#8212;&#8212; &#8212;&#8212; &#8212;&#8212;&#8211; &#8212;&#8212;&#8211; &#8212;&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ggg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>18&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>19&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>100.10<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>jjj&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>27&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>28&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>200.20<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>aaa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>300.30<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ddd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>400.40 </p>
<p> Given these input files, the following funjoin command: </p>
<pre>
  funjoin -s -a1 &quot;-B&quot; -a2 &quot;-D&quot; -a3 &quot;-E&quot; -b \
  &quot;AKEY:???&quot; -b1 &quot;AKEY:XXX,A:255&quot; -b3 &quot;G:NaN,E:-1,F:-100&quot; \
  -j key t1.fits t2.fits t3.fits foo.fits
</pre>
<p> will join the files on the <font SIZE="-1">KEY</font> column, outputting all columns except B (in t1.fits), D (in t2.fits) and E (in t3.fits), and setting blank values for <font SIZE="-1">AKEY</font> (globally, but overridden for t1.fits) and A (in file 1) and G, E, and F (in file 3). A <font SIZE="-1">JFILES</font> column will be output to flag which files were used in each row: </p>
<pre><code>
AKEY KEY A AKEY_2 KEY_2 C AKEY_3 KEY_3 F G JFILES-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - -- -- -- --aaa 0 0 aaa 0 0 aaa 0 1 300.30 7 bbb 1 3 ? ? ? 0 0 ? ? ? 0 - 100 nan 1 ccc 2 6 ccc 2 6 ? ? ? 0 - 100 nan 3 ddd 3 9 ? ? ? 0 0 ddd 3 10 400.40 5 eee 4 12 eee 4 12 ? ? ? 0 - 100 nan 3 fff 5 15 ? ? ? 0 0 ? ? ? 0 - 100 nan 1 ggg 6 18 ggg 6 18 ggg 6 19 100.10 7 hhh 7 21 ? ? ? 0 0 ? ? ? 0 - 100 nan 1 XXX 0 255 iii 8 24 ? ? ? 0 - 100 nan 2 XXX 0 255 ? ? ? 0 0 jjj 9 28 200.20 4
</code></pre>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
