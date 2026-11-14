---
title: "funcone(1)"
name: "funcone"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funcone/"
description: "funcone – cone search of a binary table containing RA, Dec columns"
---

<h2>NAME</h2>
<p> <code>funcone &#8211; cone search of a binary table containing RA, Dec columns</code></p>
<h2>SYNOPSIS</h2>
<p> funcone &lt;switches&gt; &lt;iname&gt; &lt;oname&gt; &lt;ra[hdr]&gt; &lt;dec[hdr]&gt; &lt;radius[dr&#8217;&quot;]&gt; [columns]</p>
<h2>OPTIONS</h2>
<pre><code>
- d deccol:[hdr] #Dec column name, units(def:DEC:d) - j #join columns from list file - J #join columns from list file, output all rows - l listfile #read centers and radii from a list - L listfile #read centers and radii from a list, output list rows - n #don't use cone limits as a filter - r racol:[hdr] #RA column name, units(def:RA:h) - x #append RA_CEN, DEC_CEN, RAD_CEN, CONE_KEY cols - X #append RA_CEN, DEC_CEN, RAD_CEN, CONE_KEY cols, output all rows
</code></pre>
<h2>DESCRIPTION</h2>
<p> Funcone performs a cone search on the <font SIZE="-1">RA</font> and Dec columns of a <font SIZE="-1">FITS</font> binary table. The distance from the center <font SIZE="-1">RA</font>, Dec position to the <font SIZE="-1">RA</font>, Dec in each row in the table is calculated. Rows whose distance is less than the specified radius are output. </p>
<p> The first argument to the program specifies the <font SIZE="-1">FITS</font> file, raw event file, or raw array file. If &#8220;stdin&#8221; is specified, data are read from the standard input. Use Funtools Bracket Notation to specify <font SIZE="-1">FITS</font> extensions, and filters. The second argument is the output <font SIZE="-1">FITS</font> file. If &#8220;stdout&#8221; is specified, the <font SIZE="-1">FITS</font> binary table is written to the standard output. </p>
<p> The third and fourth required arguments are the <font SIZE="-1">RA</font> and Dec center position. By default, <font SIZE="-1">RA</font> is specified in hours while Dec is specified in degrees. You can change the units of either of these by appending the character &#8220;d&#8221; (degrees), &#8220;h&#8221; (hours) or &#8220;r&#8221; (radians). Sexagesimal notation is supported, with colons or spaces separating hms and dms. (When using spaces, please ensure that the entire string is quoted.) </p>
<p> The fifth required argument is the radius of the cone search. By default, the radius value is given in degrees. The units can be changed by appending the character &#8220;d&#8221; (degrees), &#8220;r&#8221; (radians), &#8220;&#8221;&#8217; (arc minutes) or &#8216;&quot;&#8217; (arc seconds). </p>
<p> By default, all columns of the input file are copied to the output file. Selected columns can be output using an optional sixth argument in the form: </p>
<pre>
  &quot;column1 column1 ... columnN&quot;
</pre>
<p> A seventh argument allows you to output selected columns from the list file when <code>-j</code> switch is used. Note that the <font SIZE="-1">RA</font> and Dec columns used in the cone calculation must not be de-selected. </p>
<p> Also by default, the <font SIZE="-1">RA</font> and Dec column names are named &#8220;<font SIZE="-1">RA</font>&#8221; and &#8220;Dec&#8221;, and are given in units of hours and degrees respectively. You can change both the name and the units using the -r [<font SIZE="-1">RA</font>] and/or -d [Dec] switches. Once again, one of &#8220;h&#8221;, &#8220;d&#8221;, or &#8220;r&#8221; is appended to the column name to specify units but in this case, there must be a colon &#8220;:&#8221; between the name and the unit specification. </p>
<p> If the <code>-l [listfile]</code> switch is used, then one or more of the center <font SIZE="-1">RA</font>, center Dec, and radius can be taken from a list file (which can be a <font SIZE="-1">FITS</font> table or an <font SIZE="-1">ASCII</font> column text file). In this case, the third (center <font SIZE="-1">RA</font>), fourth (center Dec), and fifth (radius) command line arguments can either be a column name in the list file (if that parameter varies) or else a numeric value (if that parameter is static). When a column name is specified for the <font SIZE="-1">RA</font>, Dec, or radius, you can append a colon followed by &#8220;h&#8221;, &#8220;d&#8221;, or &#8220;r&#8221; to specify units (also &#8216; and &quot; for radius). The cone search algorithm is run once for each row in the list, taking <font SIZE="-1">RA</font>, Dec, and radius values from the specified columns or from static numeric values specified on the command line. </p>
<p> When using a list, all valid rows from each iteration are written to a single output file. Use the <code>-x</code> switch to help delineate which line of the list file was used to produce the given output row(s). This switch causes the values for the center <font SIZE="-1">RA</font>, Dec, radius, and row number to be appended to the output file, in columns called <font SIZE="-1">RA_CEN</font>, <font SIZE="-1">DEC_CEN</font>, <font SIZE="-1">RAD_CEN</font> and <font SIZE="-1">CONE_KEY</font>, respectively. Alternatively, the <code>-j</code> (join) switch will append all columns from the list row to the output row (essentially a join of the list row and input row), along with the <font SIZE="-1">CONE_KEY</font> row number. These two switches are mutually exclusive. </p>
<p> The <code>-X</code> and <code>-J</code> switches write out the same data as their lower case counterparts for each row satisfying a cone search. In addition, these switches also write out rows from the event file that do not satisfy any cone search. In such cases, that <font SIZE="-1">CONE_KEY</font> column will be given a value of -1 and the center and list position information will be set to zero for the given row. Thus, all rows of the input event file are guaranteed to be output, with rows satisfying at least one cone search having additional search information. </p>
<p> The <code>-L</code> switch acts similarly to the <code>-l</code> switch in that it takes centers from a list file. However, it also implicitly sets the -j switch, so that output rows are the join of the input event row and the center position row. In addition, this switch also writes out all center position rows for which no event satisfies the cone search criteria of that row. The <font SIZE="-1">CONE_KEY</font> column will be given a value of -2 for center rows that were not close to any data row and the event columns will be zeroed out for such rows. In this way, all centers rows are guaranteed to be output at least once. </p>
<p> If any of &#8220;all row&#8221; switches (<code>-X</code>, <code>-J</code>, or <code>-L</code>) are specified, then a new column named <font SIZE="-1">JSTAT</font> is added to the output table. The positive values in this column indicate the center position row number (starting from 1) in the list file that this data row successful matched in a cone search. A value of -1 means that the data row did not match any center position. A value of -2 means that the center position was not matched by any data row. </p>
<p> Given a center position and radius, the cone search algorithm calculates limit parameters for a box enclosing the specified cone, and only tests rows whose positions values lie within those limits. For small files, the overhead associated with this cone limit filtering can cause the program to run more slowly than if all events were tested. You can turn off cone limit filtering using the <code>-n</code> switch to see if this speeds up the processing (especially useful when processing a large list of positions). </p>
<p> For example, the default cone search uses columns &#8220;<font SIZE="-1">RA</font>&#8221; and &#8220;Dec&#8221; in hours and degrees (respectively) and <font SIZE="-1">RA</font> position in hours, Dec and radius in degrees: </p>
<pre>
  funone in.fits out.fits 23.45 34.56 0.01
</pre>
<p> To specify the <font SIZE="-1">RA</font> position in degrees: </p>
<pre>
  funcone in.fits out.fits 23.45d 34.56 0.01
</pre>
<p> To get <font SIZE="-1">RA</font> and Dec from a list but use a static value for radius (and also write identifying info for each row in the list): </p>
<pre>
  funcone -x -l list.txt in.fits out.fits MYRA MYDec 0.01
</pre>
<p> User specified columns in degrees, <font SIZE="-1">RA</font> position in hours (sexagesimal notation), Dec position in degrees (sexagesimal notation) and radius in arc minutes: </p>
<pre>
  funcone -r myRa:d -d myDec in.fits out.fits 12:30:15.5 30:12 15'
</pre>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
