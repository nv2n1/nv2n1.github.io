---
title: "fundisp(1)"
name: "fundisp"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fundisp/"
description: "fundisp – display data in a Funtools data file"
---

<h2>NAME</h2>
<p> <code>fundisp &#8211; display data in a Funtools data file</code></p>
<h2>SYNOPSIS</h2>
<p> fundisp [-f format] [-l] [-n] [-T] &lt;iname&gt; [columns|bitpix=n]</p>
<h2>OPTIONS</h2>
<pre>
  -f      # format string for display
  -l      # display image as a list containing the columns X, Y, VAL
  -n      # don't output header
  -F [c]  # use specified character as column separator (def: space)
  -T      # output in rdb/starbase format (tab separators)
</pre>
<h2>DESCRIPTION</h2>
<p> <code>fundisp</code> displays the data in the specified <font SIZE="-1">FITS</font> Extension and/or Image Section of a <font SIZE="-1">FITS</font> file, or in a Section of a non-FITS array or raw event file. </p>
<p> The first argument to the program specifies the <font SIZE="-1">FITS</font> input image, array, or raw event file to display. If &#8220;stdin&#8221; is specified, data are read from the standard input. Use Funtools Bracket Notation to specify <font SIZE="-1">FITS</font> extensions, image sections, and filters. </p>
<p> If the data being displayed are columns (either in a <font SIZE="-1">FITS</font> binary table or a raw event file), the individual rows are listed. Filters can be added using bracket notation. Thus: </p>
<pre><code>
[sh] fundisp "test.ev[time-(int)time&gt;.15]" X Y PHA PI TIME DX DY-- -- -- - -- -- -- - -- -- -- - -- -- -- -- - -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --10 8 10 8 17.1600 8.50 10.50 9 9 9 9 17.1600 9.50 9.50 10 9 10 9 18.1600 9.50 10.50 10 9 10 9 18.1700 9.50 10.50 8 10 8 10 17.1600 10.50 8.50 9 10 9 10 18.1600 10.50 9.50 9 10 9 10 18.1700 10.50 9.50 10 10 10 10 19.1600 10.50 10.50 10 10 10 10 19.1700 10.50 10.50 10 10 10 10 19.1800 10.50 10.50
</code></pre>
<p> [<font SIZE="-1">NB:</font> The <font SIZE="-1">FITS</font> binary table test file test.ev, as well as the <font SIZE="-1">FITS</font> image test.fits, are contained in the funtools funtest directory.] </p>
<p> When a table is being displayed using <code>fundisp</code>, a second optional argument can be used to specify the columns to display. For example: </p>
<p>[sh] fundisp &#8220;test.ev[time-(int)time&gt;=.99]&#8221;<br />
             &#8220;x y time&#8221; X Y TIME&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -5 &#8211;<br />
    6 40.99000000 4 &#8211; 5 59.99000000 &#8211; 1 0 154.99000000 &#8211; 2 1 168.99000000 &#8211; 3 2 183.99000000 &#8211; 4 3 199.99000000 &#8211; 5 4 216.99000000 &#8211; 6 5 234.99000000 &#8211; 7 6 253.99000000</p>
<p> The special column <code>$REGION</code> can be specified to display the region id of each row: </p>
<p>[sh $] fundisp &#8220;test.ev[time-(int)time&gt;=.99&amp;&amp;annulus(0 0 0 10 n=3)]&#8221; &#8216;x y time $REGION&#8217; X Y TIME REGION&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211;5 &#8211; 6 40.99000000 3 4 &#8211; 5 59.99000000 2 &#8211; 1 0 154.99000000 1 &#8211; 2 1 168.99000000 1 &#8211; 3 2 183.99000000 2 &#8211; 4 3 199.99000000 2 &#8211; 5 4 216.99000000 2 &#8211; 6 5 234.99000000 3 &#8211; 7 6 253.99000000 3</p>
<p> Here only rows with the proper fractional time and whose position also is within one of the three annuli are displayed. </p>
<p> Columns can be excluded from display using a minus sign before the column: </p>
<p>[sh $] fundisp &#8220;test.ev[time-(int)time&gt;=.99]&#8221;<br />
               &#8220;-time&#8221; X Y PHA PI DX DY&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; -5 &#8211;<br />
    6 5 &#8211; 6 5.50 &#8211; 6.50 4 &#8211; 5 4 &#8211; 5 4.50 &#8211; 5.50 &#8211; 1 0 &#8211; 1 0 &#8211; 1.50 0.50 &#8211; 2 1 &#8211; 2 1 &#8211; 2.50 1.50 &#8211; 3 2 &#8211; 3 2 &#8211; 3.50 2.50 &#8211; 4 3 &#8211; 4 3 &#8211; 4.50 3.50 &#8211; 5 4 &#8211; 5 4 &#8211; 5.50 4.50 &#8211; 6 5 &#8211; 6 5 &#8211; 6.50 5.50 &#8211; 7 6 &#8211; 7 6 &#8211; 7.50 6.50</p>
<p> All columns except the time column are displayed. </p>
<p> The special column <code>$N</code> can be specified to display the ordinal value of each row. Thus, continuing the previous example: </p>
<p>fundisp &#8220;test.ev[time-(int)time&gt;=.99]&#8221; &#8216;-time $n&#8217; X Y PHA PI DX DY N&#8211; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211;5 &#8211; 6 5 &#8211; 6 5.50 &#8211; 6.50 337 4 &#8211; 5 4 &#8211; 5 4.50 &#8211; 5.50 356 &#8211; 1 0 &#8211; 1 0 &#8211; 1.50 0.50 451 &#8211; 2 1 &#8211; 2 1 &#8211; 2.50 1.50 465 &#8211; 3 2 &#8211; 3 2 &#8211; 3.50 2.50 480 &#8211; 4 3 &#8211; 4 3 &#8211; 4.50 3.50 496 &#8211; 5 4 &#8211; 5 4 &#8211; 5.50 4.50 513 &#8211; 6 5 &#8211; 6 5 &#8211; 6.50 5.50 531 &#8211; 7 6 &#8211; 7 6 &#8211; 7.50 6.50 550</p>
<p> Note that the column specification is enclosed in single quotes to protect &#8216;$n&#8217; from begin expanded by the shell. </p>
<p> In general, the rules for activating and de-activating columns are:</p>
<dl>
<dt>*</p>
<dd> If only exclude columns are specified, then all columns but the exclude columns will be activated.</p>
<dt>*</p>
<dd> If only include columns are specified, then only the specified columns are activated.</p>
<dt>*</p>
<dd> If a mixture of include and exclude columns are specified, then all but the exclude columns will be active; this last case is ambiguous and the rule is arbitrary.</dl>
<p> In addition to specifying columns names explicitly, the special symbols <code>+</code> and <code>&#8211;</code> can be used to activate and de-activate <code>all</code> columns. This is useful if you want to activate the <tt>$REGION</tt> column along with all other columns. According to the rules, the syntax &#8220;$REGION&#8221; only activates the region column and de-activates the rest. Use &#8220;+ <tt>$REGION</tt>&#8221; to activate all columns as well as the region column. </p>
<p> If the data being displayed are image data (either in a <font SIZE="-1">FITS</font> primary image, a <font SIZE="-1">FITS</font> image extension, or an array file), an mxn pixel display is produced, where m and n are the dimensions of the image. By default, pixel values are displayed using the same data type as in the file. However, for integer data where the <font SIZE="-1">BSCALE</font> and <font SIZE="-1">BZERO</font> header parameters are present, the data is displayed as floats. In either case, the display data type can be overridden using an optional second argument of the form: </p>
<pre>
  bitpix=n
</pre>
<p> where n is 8,16,32,-32,-64, for unsigned char, short, int, float and double, respectively. </p>
<p> Of course, running <code>fundisp</code> on anything but the smallest image usually results in a display whose size makes it unreadable. Therefore, one can uses bracket notation (see below) to apply section and/or blocking to the image before generating a display. For example: </p>
<p>[sh] fundisp &#8220;test.fits[2:6,2:7]&#8221; bitpix = -32 2 3 4 5 6 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;2 : 3.00 4.00 5.00 6.00 7.00 3 : 4.00 5.00 6.00 7.00 8.00 4 : 5.00 6.00 7.00 8.00 9.00 5 : 6.00 7.00 8.00 9.00 10.00 6 : 7.00 8.00 9.00 10.00 11.00 7 : 8.00 9.00 10.00 11.00 12.00</p>
<p> Note that is is possible to display a <font SIZE="-1">FITS</font> binary table as an image simply by passing the table through <code>funimage</code> first: </p>
<p>[sh]./ funimage test.ev stdout | fundisp &#8220;stdin[2:6,2:7]&#8221; bitpix = 8 2 3 4 5 6 &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; -2 : 3 4 5 6 7 3 : 4 5 6 7 8 4 : 5 6 7 8 9 5 : 6 7 8 9 10 6 : 7 8 9 10 11 7 : 8 9 10 11 12</p>
<p> If the <code>-l</code> (list) switch is used, then an image is displayed as a list containing the columns: X, Y, <font SIZE="-1">VAL</font>. For example: </p>
<p>fundisp &#8211; l &#8220;test1.fits[2:6,2:7]&#8221; bitpix = -32 X Y VAL&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -2 2 6.00 3 2 1.00 4 2 1.00 5 2 1.00 6 2 1.00 2 3 1.00 3 3 5.00 4 3 1.00 5 3 1.00 6 3 1.00 2 4 1.00 3 4 1.00 4 4 4.00 5 4 1.00 6 4 1.00 2 5 1.00 3 5 1.00 4 5 1.00 5 5 3.00 6 5 1.00 2 6 1.00 3 6 1.00 4 6 1.00 5 6 1.00 6 6 2.00 2 7 1.00 3 7 1.00 4 7 1.00 5 7 1.00 6 7 1.00</p>
<p> If the <code>-n</code> (nohead) switch is used, then no header is output for tables. This is useful, for example, when fundisp output is being directed into gnuplot. </p>
<p> The <code>fundisp</code> program uses a default set of display formats: </p>
<p>datatype TFORM format&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8211;double D &#8220;%21.8f&#8221; float E &#8220;%11.2f&#8221; int J &#8220;%10d&#8221; short I &#8220;%8d&#8221; byte B &#8220;%6d&#8221; string A &#8220;%12.12s&#8221; bits X &#8220;%8x&#8221; logical L &#8220;%1x&#8221;</p>
<p> Thus, the default display of 1 double and 2 shorts gives: </p>
<pre>
  [sh] fundisp snr.ev &quot;time x y&quot;
</pre>
<p>TIME X Y&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;79494546.56818075 546 201 79488769.94469175 548 201 &#8230;</p>
<p> You can change the display format for individual columns or for all columns of a given data types by means of the -f switch. The format string that accompanies -f is a space-delimited list of keyword=format values. The keyword values can either be column names (in which case the associated format pertains only to that column) or <font SIZE="-1">FITS</font> table <font SIZE="-1">TFORM</font> specifiers (in which case the format pertains to all columns having that data type). For example, you can change the double and short formats for all columns like this: </p>
<pre>
  [sh] fundisp -f &quot;D=%22.11f I=%3d&quot; snr.ev &quot;time x y&quot;
</pre>
<p>TIME X Y&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; -79494546.56818075478 546 201 79488769.94469174743 548 201 &#8230;</p>
<p> Alternatively, you can change the format of the time and x columns like this: </p>
<pre>
  [sh] fundisp -f &quot;time=%22.11f x=%3d&quot; snr.ev &quot;time x y&quot;
</pre>
<p>TIME X Y&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8211;79494546.56818075478 546 201 79488769.94469174743 548 201 &#8230;</p>
<p> Note that there is a potential conflict if a column has the same name as one of the <font SIZE="-1">TFORM</font> specifiers. In the examples above, the the &#8220;X&#8221; column in the table has the same name as the X (bit) datatype. To resolve this conflict, the format string is processed such that <font SIZE="-1">TFORM</font> datatype specifiers are checked for first, using a case-sensitive comparison. If the specified format value is not an upper case <font SIZE="-1">TFORM</font> value, then a case-insensitive check is made on the column name. This means that, in the examples above, &#8220;X=%3d&#8221; will refer to the X (bit) datatype, while &#8220;x=%3d&#8221; will refer to the X column: </p>
<pre>
  [sh] fundisp -f &quot;X=%3d&quot; snr.ev &quot;x y&quot;
</pre>
<p>X Y&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;546 201 548 201 &#8230;</p>
<pre>
  [sh] fundisp -f &quot;x=%3d&quot; snr.ev &quot;x y&quot;
</pre>
<p>X Y&#8211; &#8211; &#8212; &#8212; &#8212; &#8211;546 201 548 201 &#8230;</p>
<p> As a rule, therefore, it is best always to specify the column name in lower case and <font SIZE="-1">TFORM</font> data types in upper case. </p>
<p> The <code>-f [format]</code> will change the format for a single execution of fundisp. You also can use the <font SIZE="-1"><code>FUN_FORMAT</code></font> envronment variable to change the format for all invocations of fundisp. The format of this environment variable&#8217;s value is identical to that used with the <code>-f</code> switch. This global value can be overridden in individual cases by use of the <code>-f [format]</code> switch. </p>
<p> Caveats: Please also note that it is the user&#8217;s responsibility to match the format specifier to the column data type correctly. Also note that, in order to maintain visual alignment between names and columns, the column name will be truncated (on the left) if the format width is less than the length of the name. However, truncation is not performed if the output is in <font SIZE="-1">RDB</font> format (using the -T switch). </p>
<p> [An older-style format string is supported but deprecated. It consists of space-delimited C format statements for all data types, specified in the following order: </p>
<p>double float int short byte string bit.</p>
<p> This order of the list is based on the assumption that people generally will want to change the float formats. </p>
<p> If &#8220;-&#8221; is entered instead of a format statement for a given data type, the default format is used. Also, the format string can be terminated without specifying all formats, and defaults will be used for the rest of the list. Note that you must supply a minimum field width, i.e., &#8220;%6d&#8221; and &#8220;%-6d&#8221; are legal, &#8220;%d&#8221; is not legal. </p>
<p> By using -f [format], you can change the double and short formats like this: </p>
<pre>
  [sh] fundisp -f &quot;22.11f - - 3d&quot; snr.ev &quot;time x y&quot;
</pre>
<p>TIME X Y&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; -79494546.56818075478 546 201 79488769.94469174743 548 201 &#8230;</p>
<p> <font SIZE="-1">NB:</font> This format is deprecated and will be removed in a future release.] </p>
<p> The <code>-F[c]</code> switch can be used to specify a (single-character) column separator (where the default is a space). Note that column formatting will almost certainly also add spaces to pad individual columns to the required width. These can be removed with a program such as sed, at the cost of generating unaligned columns. For example: </p>
<p> fundisp -F&#8217;,&#8217; snr.ev'[cir 512 512 .1]&#8217;<br />
&nbsp;<wbr>X,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Y,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">PHA</font>,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">PI</font>,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">TIME</font>,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">DX</font>,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">DY</font> &#8212;&#8212;&#8211;,&#8212;&#8212;&#8211;,&#8212;&#8212;&#8211;,&#8212;&#8212;&#8211;,&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;,&#8212;&#8212;&#8211;,&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>7,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>79493997.45854475,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>578,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>574<br />
&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>9,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>79494575.58943175,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>579,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>573<br />
&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>79493631.03866175,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>578,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>575<br />
&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>79493290.86521725,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>578,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>575<br />
&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>512,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>9,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>79493432.00990875,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>579,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>573 </p>
<p> fundisp -F&#8217;,&#8217; snr.ev'[cir 512 512 .1]&#8217; | sed &#8216;s/ *, */,/g&#8217;<br />
&nbsp;<wbr>X,Y,PHA,PI,TIME,DX,DY &#8212;&#8212;&#8211;,&#8212;&#8212;&#8211;,&#8212;&#8212;&#8211;,&#8212;&#8212;&#8211;,&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;,&#8212;&#8212;&#8211;,&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>512,512,6,7,79493997.45854475,578,574<br />
&nbsp;<wbr>&nbsp;<wbr>512,512,8,9,79494575.58943175,579,573<br />
&nbsp;<wbr>&nbsp;<wbr>512,512,5,6,79493631.03866175,578,575<br />
&nbsp;<wbr>&nbsp;<wbr>512,512,5,5,79493290.86521725,578,575<br />
&nbsp;<wbr>&nbsp;<wbr>512,512,8,9,79493432.00990875,579,573 </p>
<p> fundisp -f &#8220;x=%3d y=%3d pi=%1d pha=%1d time=%20.11f dx=%3d dy=%3d&#8221; -F&#8217;,&#8217; snr.ev'[cir 512 512 .1]&#8217; | sed &#8216;s/ *, */,/g&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>X,Y,A,I,TIME,DX,DY &#8212;,&#8212;,-,-,&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;,&#8212;,&#8212; 512,512,6,7,79493997.45854474604,578,574 512,512,8,9,79494575.58943174779,579,573 512,512,5,6,79493631.03866174817,578,575 512,512,5,5,79493290.86521725357,578,575 512,512,8,9,79493432.00990875065,579,573 </p>
<p> If the <code>-T</code> (rdb table) switch is used, the output will conform to starbase/rdb data base format: tabs will be inserted between columns rather than spaces. This format is not available when displaying image pixels (except in conjunction with the <code>-l</code> switch). </p>
<p> Finally, note that <code>fundisp</code> can be used to create column filters from the auxiliary tables in a <font SIZE="-1">FITS</font> file. For example, the following shell code will generate a good-time interval (<font SIZE="-1">GTI</font>) filter for X-ray data files that contain a standard <font SIZE="-1">GTI</font> extension: </p>
<pre><code>
#!/ bin / sh
sed '1,/---- .*/d / ^$ /, $d ' | awk ' tot &gt; 0 {
                                                 printf "||"};
{
    printf "time=" $1 ":" $2;
    tot++
}
'
</code></pre>
<p> If this script is placed in a file called &#8220;mkgti&#8221;, it can be used in a command such as: </p>
<pre>
  fundisp foo.fits&quot;[GTI]&quot; | mkgti &gt; gti.filter
</pre>
<p> The resulting filter file can then be used in various funtools programs: </p>
<pre>
  funcnts foo.fits&quot;[@gti.filter]&quot; ...
</pre>
<p> to process only the events in the good-time intervals.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
