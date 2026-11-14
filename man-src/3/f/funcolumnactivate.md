---
title: "funcolumnactivate(3)"
name: "funcolumnactivate"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funcolumnactivate/"
description: "FunColumnActivate – activate Funtools columns"
---

<h2>NAME</h2>
<p> <code>FunColumnActivate &#8211; activate Funtools columns</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<pre>
  void FunColumnActivate(Fun fun, char *s, char *plist)
</pre>
<h2>DESCRIPTION</h2>
<p> The FunColumnActivate() routine determines which columns (set up by <i>FunColumnSelect()</i>) ultimately will be read and/or written. By default, all columns that are selected using <i>FunColumnSelect()</i> are activated. The <i>FunColumnActivate()</i> routine can be used to turn off/off activation of specific columns. </p>
<p> The first argument is the Fun handle associated with this set of columns. The second argument is a space-delimited list of columns to activate or de-activate. Columns preceded by &#8220;+&#8221; are activated and columns preceded by a &#8220;-&#8221; are de-activated. If a column is named without &#8220;+&#8221; or &#8220;-&#8221;, it is activated. The reserved strings &#8220;$region&#8221; and &#8216;$n&#8217; are used to activate a special columns containing the filter region value and row value, respectively, associated with this row. For example, if a filter containing two circular regions is specified as part of the Funtools file name, this column will contain a value of 1 or 2, depending on which region that row was in. The reserved strings &#8220;$x&#8221; and &#8220;$y&#8221; are used to activate the current binning columns. Thus, if the columns <font SIZE="-1">DX</font> and <font SIZE="-1">DY</font> are specified as binning columns: </p>
<p>[sh $] fundisp foo.fits[bincols = (DX, DY)]</p>
<p> then &#8220;$x&#8221; and &#8220;$y&#8221; will refer to these columns in a call to <i>FunColumnActivate()</i>. </p>
<p> In addition, if the activation string contains only columns to be activated, then the routine will de-activate all other columns. Similarly, if the activation string contains only columns to de-activate, then the routine will activate all other columns before activating the list. This makes it simple to change the activation state of all columns without having to know all of the column names. For example:</p>
<dl>
<dt>*</p>
<dd> <code>&#8220;pi pha time&#8221;</code> # only these three columns will be active</p>
<dt>*</p>
<dd> <code>&#8220;-pi -pha -time&#8221;</code> # all but these columns will be active</p>
<dt>*</p>
<dd> <code>&#8220;pi -pha&#8221;</code> # only pi is active, pha is not, others are not</p>
<dt>*</p>
<dd> <code>&#8220;+pi -pha&#8221;</code> # same as above</p>
<dt>*</p>
<dd> <code>&#8220;pi -pha -time&#8221;</code> # only pi is active, all others are not</p>
<dt>*</p>
<dd> <code>&#8220;pi pha&#8221;</code> # pha and pi are active, all others are not</p>
<dt>*</p>
<dd> <code>&#8220;pi pha -x -y&#8221;</code> # pha and pi are active, all others are not</dl>
<p> You can use the column activation list to reorder columns, since columns are output in the order specified. For example: </p>
<p>#default output order<br />
fundisp snr.ev &#8216;[cir 512 512 .1]&#8217; X Y PHA PI TIME DX DY&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;512 512 6 7 79493997.45854475 578 574 512 512 8 9 79494575.58943175 579 573 512 512 5 6 79493631.03866175 578 575 512 512 5 5 79493290.86521725 578 575 512 512 8 9 79493432.00990875 579 573</p>
<p>#re &#8211; order the output by specifying explicit order<br />
fundisp snr.ev &#8216;[cir 512 512 .1]&#8217; &#8220;time x y dy dx pi pha&#8221; TIME X Y DY DX PI PHA&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;79493997.45854475 512 512 574 578 7 6 79494575.58943175 512 512 573 579 9 8 79493631.03866175 512 512 575 578 6 5 79493290.86521725 512 512 575 578 5 5 79493432.00990875 512 512 573 579 9 8</p>
<p> A &#8220;+&#8221; sign by itself means to activate all columns, so that you can reorder just a few columns without specifying all of them: </p>
<p>#reorder 3 columns and then output the rest<br />
fundisp snr.ev &#8216;[cir 512 512 .1]&#8217; &#8220;time pi pha +&#8221; TIME PI PHA Y X DX DY&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;79493997.45854475 7 6 512 512 578 574 79494575.58943175 9 8 512 512 579 573 79493631.03866175 6 5 512 512 578 575 79493290.86521725 5 5 512 512 578 575 79493432.00990875 9 8 512 512 579 573</p>
<p> The column activation/deactivation is performed in the order of the specified column arguments. This means you can mix &#8220;+&#8221;, &#8220;-&#8221; (which de-activates all columns) and specific column names to reorder and select columns in one command. For example, consider the following: </p>
<p>#reorder and de &#8211; activate<br />
fundisp snr.ev &#8216;[cir 512 512 .1]&#8217; &#8220;time pi pha + -x -y&#8221; TIME PI PHA DX DY&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;79493997.45854475 7 6 578 574 79494575.58943175 9 8 579 573 79493631.03866175 6 5 578 575 79493290.86521725 5 5 578 575 79493432.00990875 9 8 579 573</p>
<p> We first activate &#8220;time&#8221;, &#8220;pi&#8221;, and &#8220;pha&#8221; so that they are output first. We then activate all of the other columns, and then de-activate &#8220;x&#8221; and &#8220;y&#8221;. Note that this is different from: </p>
<p>#probably not what you want&#8230;<br />
fundisp snr.ev &#8216;[cir 512 512 .1]&#8217; &#8220;time pi pha -x -y +&#8221; TIME PI PHA Y X DX DY&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;79493997.45854475 7 6 512 512 578 574 79494575.58943175 9 8 512 512 579 573 79493631.03866175 6 5 512 512 578 575 79493290.86521725 5 5 512 512 578 575 79493432.00990875 9 8 512 512 579 573</p>
<p> Here, &#8220;x&#8221; and &#8220;y&#8221; are de-activated, but then all columns including &#8220;x&#8221; and &#8220;y&#8221; are again re-activated. </p>
<p> Typically, <i>FunColumnActivate()</i> uses a list of columns that are passed into the program from the command line. For example, the code for funtable contains the following: </p>
<pre>
  char *cols=NULL;
</pre>
<p>/* open the input FITS file */<br />
if (!(fun = FunOpen(argv[1], &#8220;rc&#8221;, NULL)))<br />
    gerror(stderr, &#8220;could not FunOpen input file: %s
&#8221;, argv[1]);</p>
<p>/* set active flag for specified columns */<br />
if (argc &gt;= 4)<br />
    cols = argv[3];<br />
FunColumnActivate(fun, cols, NULL);</p>
<p> The <i>FunOpen()</i> call sets the default columns to be all columns in the input file. The <i>FunColumnActivate()</i> call then allows the user to control which columns ultimately will be activated (i.e., in this case, written to the new file). For example: </p>
<pre>
  funtable test.ev foo.ev &quot;pi pha time&quot;
</pre>
<p> will process only the three columns mentioned, while: </p>
<pre>
  funtable test.ev foo.ev &quot;-time&quot;
</pre>
<p> will process all columns except &#8220;time&#8221;. </p>
<p> If <i>FunColumnActivate()</i> is called with a null string, then the environment variable <font SIZE="-1"><code>FUN_COLUMNS</code></font> will be used to provide a global value, if present. This is the reason why we call the routine even if no columns are specified on the command line (see example above), instead of calling it this way: </p>
<pre><code>
/* set active flag for specified columns */
if (argc &gt;= 4) {
    FunColumnActivate(fun, argv[3], NULL);
}
</code></pre>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
