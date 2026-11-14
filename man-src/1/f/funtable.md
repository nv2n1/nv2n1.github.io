---
title: "funtable(1)"
name: "funtable"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funtable/"
description: "funtable – copy selected rows from a Funtools file to a FITS binary table"
---

<h2>NAME</h2>
<p> <code>funtable &#8211; copy selected rows from a Funtools file to a FITS binary table</code></p>
<h2>SYNOPSIS</h2>
<p> funtable [-a] [-i|-z] [-m] [-s cols] &lt;iname&gt; &lt;oname&gt; [columns]</p>
<h2>OPTIONS</h2>
<pre><code>
  -a    # append to existing output file as a table extension
  -i    # for image data, only generate X and Y columns
  -m    # for tables, write a separate file for each region
  -s "col1 ..." # columns on which to sort
  -z    # for image data, output zero-valued pixels
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>funtable</code> selects rows from the specified <font SIZE="-1">FITS</font> Extension (binary table only) of a <font SIZE="-1">FITS</font> file, or from a non-FITS raw event file, and writes those rows to a <font SIZE="-1">FITS</font> binary table file. It also will create a <font SIZE="-1">FITS</font> binary table from an image or a raw array file. </p>
<p> The first argument to the program specifies the <font SIZE="-1">FITS</font> file, raw event file, or raw array file. If &#8220;stdin&#8221; is specified, data are read from the standard input. Use Funtools Bracket Notation to specify <font SIZE="-1">FITS</font> extensions, and filters. The second argument is the output <font SIZE="-1">FITS</font> file. If &#8220;stdout&#8221; is specified, the <font SIZE="-1">FITS</font> binary table is written to the standard output. By default, all columns of the input file are copied to the output file. Selected columns can be output using an optional third argument in the form: </p>
<pre>
  &quot;column1 column1 ... columnN&quot;
</pre>
<p> The <code>funtable</code> program generally is used to select rows from a <font SIZE="-1">FITS</font> binary table using Table Filters and/or Spatial Region Filters. For example, you can copy only selected rows (and output only selected columns) by executing in a command such as: </p>
<p>[sh] funtable &#8220;test.ev[pha==1&amp;&amp;pi==10]&#8221; stdout &#8220;x y pi pha&#8221; | fundisp stdin<br />
                                                                  X Y PHA PI&#8211; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10</p>
<p> The special column <code>$REGION</code> can be specified to write the region id of each row: </p>
<p>[sh $] funtable &#8220;test.ev[time-(int)time&gt;=.99&amp;&amp;annulus(0 0 0 10 n=3)]&#8221; stdout &#8216;x y time $REGION&#8217; | fundisp stdin<br />
                                                                                                          X Y TIME REGION&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211;5 &#8211;<br />
                                                                                                      6 40.99000000 3 4 &#8211; 5 59.99000000 2 &#8211; 1 0 154.99000000 1 &#8211; 2 1 168.99000000 1 &#8211; 3 2 183.99000000 2 &#8211; 4 3 199.99000000 2 &#8211; 5 4 216.99000000 2 &#8211; 6 5 234.99000000 3 &#8211; 7 6 253.99000000 3</p>
<p> Here only rows with the proper fractional time and whose position also is within one of the three annuli are written. </p>
<p> Columns can be excluded from display using a minus sign before the column: </p>
<p>[sh $] funtable &#8220;test.ev[time-(int)time&gt;=.99]&#8221; stdout &#8220;-time&#8221; | fundisp stdin<br />
                                                                        X Y PHA PI DX DY&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; -5 &#8211;<br />
                                                                    6 5 &#8211; 6 5.50 &#8211; 6.50 4 &#8211; 5 4 &#8211; 5 4.50 &#8211; 5.50 &#8211; 1 0 &#8211; 1 0 &#8211; 1.50 0.50 &#8211; 2 1 &#8211; 2 1 &#8211; 2.50 1.50 &#8211; 3 2 &#8211; 3 2 &#8211; 3.50 2.50 &#8211; 4 3 &#8211; 4 3 &#8211; 4.50 3.50 &#8211; 5 4 &#8211; 5 4 &#8211; 5.50 4.50 &#8211; 6 5 &#8211; 6 5 &#8211; 6.50 5.50 &#8211; 7 6 &#8211; 7 6 &#8211; 7.50 6.50</p>
<p> All columns except the time column are written. </p>
<p> In general, the rules for activating and de-activating columns are:</p>
<dl>
<dt>*</p>
<dd> If only exclude columns are specified, then all columns but the exclude columns will be activated.</p>
<dt>*</p>
<dd> If only include columns are specified, then only the specified columns are activated.</p>
<dt>*</p>
<dd> If a mixture of include and exclude columns are specified, then all but the exclude columns will be active; this last case is ambiguous and the rule is arbitrary.</dl>
<p> In addition to specifying columns names explicitly, the special symbols <i>+</i> and <i>&#8211;</i> can be used to activate and de-activate <i>all</i> columns. This is useful if you want to activate the <tt>$REGION</tt> column along with all other columns. According to the rules, the syntax &#8220;$REGION&#8221; only activates the region column and de-activates the rest. Use &#8220;+ <tt>$REGION</tt>&#8221; to activate all columns as well as the region column. </p>
<p> Ordinarily, only the selected table is copied to the output file. In a <font SIZE="-1">FITS</font> binary table, it sometimes is desirable to copy all of the other <font SIZE="-1">FITS</font> extensions to the output file as well. This can be done by appending a &#8216;+&#8217; sign to the name of the extension in the input file name. For example, the first command below copies only the <font SIZE="-1">EVENT</font> table, while the second command copies other extensions as well: </p>
<p>[sh] funtable &#8220;/proj/rd/data/snr.ev[EVENTS]&#8221; events.ev<br />
    [sh] funtable &#8220;/proj/rd/data/snr.ev[EVENTS+]&#8221; eventsandmore.ev</p>
<p> If the input file is an image or a raw array file, then <code>funtable</code> will generate a <font SIZE="-1">FITS</font> binary table from the pixel values in the image. Note that it is not possible to specify the columns to output (using command-line argument 3). Instead, there are two ways to create such a binary table from an image. By default, a 3-column table is generated, where the columns are &#8220;X&#8221;, &#8220;Y&#8221;, and &#8220;<font SIZE="-1">VALUE</font>&#8221;. For each pixel in the image, a single row (event) is generated with the &#8220;X&#8221; and &#8220;Y&#8221; columns assigned the dim1 and dim2 values of the image pixel, respectively and the &#8220;<font SIZE="-1">VALUE</font>&#8221; column assigned the value of the pixel. With sort of table, running <code>funhist</code> on the &#8220;<font SIZE="-1">VALUE</font>&#8221; column will give the same results as running <code>funhist</code> on the original image. </p>
<p> If the <code>-i</code> (&#8220;individual&#8221; rows) switch is specified, then only the &#8220;X&#8221; and &#8220;Y&#8221; columns are generated. In this case, each positive pixel value in the image generates n rows (events), where n is equal to the integerized value of that pixel (plus 0.5, for floating point data). In effect, <code>-i</code> approximately recreates the rows of a table that would have been binned into the input image. (Of course, this is only approximately correct, since the resulting x,y positions are integerized.) </p>
<p> If the <code>-s [col1 col2 &#8230; coln]</code> (&#8220;sort&#8221;) switch is specified, the output rows of a binary table will be sorted using the specified columns as sort keys. The sort keys must be scalar columns and also must be part of the output file (i.e. you cannot sort on a column but not include it in the output). This facility uses the <code>_sort</code> program (included with funtools), which must be accessible via your path. </p>
<p> For binary tables, the <code>-m</code> (&#8220;multiple files&#8221;) switch will generate a separate file for each region in the filter specification i.e. each file contains only the rows from that region. Rows which pass the filter but are not in any region also are put in a separate file. </p>
<p> The separate output file names generated by the <code>-m</code> switch are produced automatically from the root output file to contain the region id of the associated region. (Note that region ids start at 1, so that the file name associated with id 0 contains rows that pass the filter but are not in any given region.) Output file names are generated as follows:</p>
<dl>
<dt>*</p>
<dd> A <tt>$n</tt> specification can be used anywhere in the root file name (suitably quoted to protect it from the shell) and will be expanded to be the id number of the associated region. For example: </p>
<p>funtable &#8211; m input.fits &#8216;[cir(512,512,1);cir(520,520,1)&#8230;]&#8217; &#8216;foo.goo_$n.fits&#8217;</p>
<p> will generate files named foo.goo_0.fits (for rows not in any region but still passing the filter), foo.goo_1.fits (rows in region id #1, the first region), foo.goo_2.fits (rows in region id #2), etc. Note that single quotes in the output root are required to protect the &#8216;$&#8217; from the shell.</p>
<dt>*</p>
<dd> If <tt>$n</tt> is not specified, then the region id will be placed before the first dot (.) in the filename. Thus: </p>
<p>funtable &#8211; m input.fits &#8216;[cir(512,512,1);cir(520,520,1)&#8230;]&#8217; foo.evt.fits</p>
<p> will generate files named foo0.evt.fits (for rows not in any region but still passing the filter), foo1.evt.fits (rows in region id #1), foo2.evt.fits (rows in region id #2), etc.</p>
<dt>*</p>
<dd> If no dot is specified in the root output file name, then the region id will be appended to the filename. Thus: </p>
<pre><code>
funtable - m input.fits '[cir(512,512,1);cir(520,520,1)...]' 'foo_evt'
</code></pre>
<p> will generate files named foo_evt0 (for rows not in any region but still passing the filter), foo_evt1 (rows in region id #1), foo_evt2 (rows in region id #2), etc.</dl>
<p> The multiple file mechanism provide a simple way to generate individual source data files with a single pass through the data. </p>
<p> By default, a new <font SIZE="-1">FITS</font> file is created and the binary table is written to the first extension. If the <code>-a</code> (append) switch is specified, the table is appended to an existing <font SIZE="-1">FITS</font> file as a <font SIZE="-1">BINTABLE</font> extension. Note that the output <font SIZE="-1">FITS</font> file must already exist. </p>
<p> If the <code>-z</code> (&#8220;zero&#8221; pixel values) switch is specified and <code>-i</code> is not specified, then pixels having a zero value will be output with their &#8220;<font SIZE="-1">VALUE</font>&#8221; column set to zero. Obviously, this switch does not make sense when individual events are output.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
