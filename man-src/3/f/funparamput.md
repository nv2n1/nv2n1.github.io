---
title: "funparamput(3)"
name: "funparamput"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funparamput/"
description: "FunParamPut – put a Funtools param value"
---

<h2>NAME</h2>
<p> <code>FunParamPut &#8211; put a Funtools param value</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p>int FunParamPutb(Fun fun, char *name, int n, int value, char *comm,<br />
                 int append)</p>
<p>int FunParamPuti(Fun fun, char *name, int n, int value, char *comm,<br />
                 int append)</p>
<p>int FunParamPutd(Fun fun, char *name, int n, double value, int prec,<br />
                 char *comm, int append)</p>
<p>int FunParamPuts(Fun fun, char *name, int n, char *value, char *comm,<br />
                 int append)</p>
<h2>DESCRIPTION</h2>
<p> The four routines FunParamPutb(), FunParamPuti(), FunParamPutd(), and FunParamPuts(), will set the value of a <font SIZE="-1">FITS</font> header parameter as a boolean, int, double, and string, respectively. </p>
<p> The first argument is the Fun handle associated with the <font SIZE="-1">FITS</font> header being accessed. Normally, the header is associated with the <font SIZE="-1">FITS</font> extension that you opened with FunOpen(). However, you can use <i>FunInfoPut()</i> to specify that use of the primary header. In particular, if you set the <font SIZE="-1">FUN_PRIMARYHEADER</font> parameter to 1, then the primary header is used for all parameter access until the value is reset to 0. For example: </p>
<p>int val;<br />
FunParamPuti(fun, &#8220;NAXIS1&#8221;, 0, 10, NULL, 1);<br />
#current header<br />
    val = 1;<br />
FunInfoPut(fun, FUN_PRIMARYHEADER, &amp;val, 0);<br />
#switch to&#8230; FunParamPuti(fun, &#8220;NAXIS1&#8221;, 0, 10, NULL, 1);<br />
#primary header</p>
<p> (You also can use the deprecated <font SIZE="-1">FUN_PRIMARY</font> macro, to access parameters from the primary header.) </p>
<p> The second argument is the <code>name</code> of the parameter. ( In accordance with <font SIZE="-1">FITS</font> standards, the special names <font SIZE="-1"><code>COMMENT</code></font> and <font SIZE="-1"><code>HISTORY</code></font>, as well as blank names, are output without the &#8220;= &#8221; value indicator in columns 9 and 10. </p>
<p> The third <code>n</code> argument, if non-zero, is an integer that will be added as a suffix to the parameter name. This makes it easy to use a simple loop to process parameters having the same root name. For example, to set the values of <font SIZE="-1">TLMIN</font> and <font SIZE="-1">TLMAX</font> for each column in a binary table, you can use: </p>
<p>for (i = 0; i &lt; got; i++) {<br />
    FunParamPutd(fun, &#8220;TLMIN&#8221;, i + 1, tlmin[i], 7, &#8220;min column val&#8221;, 1);<br />
    FunParamPutd(fun, &#8220;TLMAX&#8221;, i + 1, tlmax[i], 7, &#8220;max column val&#8221;, 1);<br />
}</p>
<p> The fourth <code>defval</code> argument is the value to set. Note that the data type of this argument is different for each specific <i>FunParamPut()</i> call. The <code>comm</code> argument is the comment string to add to this header parameter. Its value can be <font SIZE="-1">NULL</font>. The final <code>append</code> argument determines whether the parameter is added to the header if it does not exist. If set to a non-zero value, the header parameter will be appended to the header if it does not exist. If set to 0, the value will only be used to change an existing parameter. </p>
<p> Note that the double precision routine <i>FunParamPutd()</i> supports an extra <code>prec</code> argument after the <code>value</code> argument, in order to specify the precision when converting the double value to <font SIZE="-1">ASCII</font>. In general a 20.[prec] format is used (since 20 characters are alloted to a floating point number in <font SIZE="-1">FITS</font>) as follows: if the double value being put to the header is less than 0.1 or greater than or equal to 10**(20-2-[prec]), then <tt>%20</tt>.[prec]e format is used (i.e., scientific notation); otherwise <tt>%20</tt>.[prec]f format is used (i.e., numeric notation). </p>
<p> As a rule, parameters should be set before writing the table or image. It is, however, possible to update the value of an <code>existing</code> parameter after writing an image or table (but not to add a new one). Such updating only works if the parameter already exists and if the output file is seekable, i.e. if it is a disk file or is stdout being redirected to a disk file. </p>
<p> It is possible to add a new parameter to a header after the data has been written, but only if space has previously been reserved. To reserve space, add a blank parameter whose value is the name of the parameter you eventually will update. Then, when writing the new parameter, specify a value of 2 for the append flag. The parameter writing routine will first look to update an existing parameter, as usual. If an existing parameter is not found, an appropriately-valued blank parameter will be searched for and replaced. For example: </p>
<pre><code>
/* add blank card to be used as a place holder for IPAR1 update */
FunParamPuts(fun, NULL, 0, "IPAR1", "INTEGER Param", 0);
...
    /* write header and data */
    FunTableRowPut(fun, events, got, 0, NULL);
...
    /* update param in file after writing data -- note append = 2 here */
    FunParamPuti(fun, "IPAR", 1, 400, "INTEGER Param", 2);
</code></pre>
<p> The parameter routines return a 1 if the routine was successful and a 0 on failure. In general, the major reason for failure is that you did not set the append argument to a non-zero value and the parameter did not already exist in the file.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
