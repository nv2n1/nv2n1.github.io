---
title: "funlib(3)"
name: "funlib"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funlib/"
description: "FunLib: the Funtools Programming Interface"
---

<h2>NAME</h2>
<p> <code>FunLib: the Funtools Programming Interface</code></p>
<h2>SYNOPSIS</h2>
<p> A description of the Funtools library.</p>
<h2>DESCRIPTION</h2>
<p> <code>Introduction to the Funtools Programming Interface</code> </p>
<p> To create a Funtools application, you need to include the funtools.h definitions file in your code: </p>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p> You then call Funtools subroutines and functions to access Funtools data. The most important routines are:</p>
<dl>
<dt>*</p>
<dd> FunOpen: open a Funtools file</p>
<dt>*</p>
<dd> FunInfoGet: get info about an image or table</p>
<dt>*</p>
<dd> FunImageGet: retrieve image data</p>
<dt>*</p>
<dd> FunImageRowGet: retrieve image data by row</p>
<dt>*</p>
<dd> FunImagePut: output image data</p>
<dt>*</p>
<dd> FunImageRowPut: output image data by row</p>
<dt>*</p>
<dd> FunColumnSelect: select columns in a table for access</p>
<dt>*</p>
<dd> FunTableRowGet: retrieve rows from a table</p>
<dt>*</p>
<dd> FunTableRowPut: output rows to a table</p>
<dt>*</p>
<dd> FunClose: close a Funtools file</dl>
<p> Your program must be linked against the libfuntools.a library, along with the math library. The following libraries also might be required on your system:</p>
<dl>
<dt>*</p>
<dd> -lsocket -lnsl for socket support</p>
<dt>*</p>
<dd> -ldl for dynamic loading</dl>
<p> For example, on a Solaris system using gcc, use the following link line: </p>
<pre>
  gcc -o foo foo.c -lfuntools -lsocket -lnsl -ldl -lm
</pre>
<p> On a Solaris system using Solaris cc, use the following link line: </p>
<pre>
  gcc -o foo foo.c -lfuntools -lsocket -lnsl -lm
</pre>
<p> On a Linux system using gcc, use the following link line: </p>
<pre>
  gcc -o foo foo.c -lfuntools -ldl -lm
</pre>
<p> Once configure has built a Makefile on your platform, the required &#8220;extra&#8221; libraries (aside from -lm, which always is required) are specified in that file&#8217;s <font SIZE="-1">EXTRA_LIBS</font> variable. For example, under Linux you will find: </p>
<pre>
  grep EXTRA_LIBS Makefile
  EXTRA_LIBS      =  -ldl
  ...
</pre>
<p> The Funtools library contains both the zlib library (<a rel="nofollow" href="http://www.gzip.org/zlib/)">http://www.gzip.org/zlib/)</a> and Doug Mink&#8217;s <font SIZE="-1">WCS</font> library (<a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/">http://tdc-www.harvard.edu/software/wcstools/</a>). It is not necessary to put these libraries on a Funtools link line. Include files necessary for using these libraries are installed in the Funtools include directory. </p>
<p> <code>Funtools Programming Tutorial</code> </p>
<p> The <i>FunOpen()</i> function is used to open a <font SIZE="-1">FITS</font> file, an array, or a raw event file: </p>
<p>/* open the input FITS file for reading */<br />
ifun = FunOpen(iname, &#8220;r&#8221;, NULL);<br />
/* open the output FITS file for writing, and connect it to the input file */<br />
ofun = FunOpen(iname, &#8220;w&#8221;, ifun);</p>
<p> A new output file can inherit header parameters automatically from existing input file by passing the input Funtools handle as the last argument to the new file&#8217;s <i>FunOpen()</i> call as shown above. </p>
<p> For image data, you then can call <i>FunImageGet()</i> to read an image into memory. </p>
<p>float buf = NULL;<br />
/* extract and bin the data section into an image buffer */<br />
buf = FunImageGet(fun, NULL, &#8220;bitpix=-32&#8221;);</p>
<p> If the (second) buf argument to this call is <font SIZE="-1">NULL</font>, buffer space is allocated automatically. The (third) plist argument can be used to specify the return data type of the array. If <font SIZE="-1">NULL</font> is specified, the data type of the input file is used. </p>
<p> To process an image buffer, you would generally make a call to <i>FunInfoGet()</i> to determine the dimensions of the image (which may have been changed from the original file dimensions due to Funtools image sectioning on the command line). In a <font SIZE="-1">FITS</font> image, the index along the dim1 axis varies most rapidly, followed by the dim2 axis, etc. Thus, to access each pixel in an 2D image, use a double loop such as: </p>
<p>buf = FunImageGet(fun, NULL, &#8220;bitpix=-32&#8221;);<br />
FunInfoGet(fun, FUN_SECT_DIM1, &amp;dim1, FUN_SECT_DIM2, &amp;dim2, 0);<br />
for (i = 1; i &lt;= dim2; i++) {<br />
    for (j = 1; j &lt;= dim1; j++) {<br />
        &#8230; process buf[((i &#8211; 1) * dim1) + (j &#8211; 1)]&#8230;<br />
    }<br />
}</p>
<p> or: </p>
<p>buf = FunImageGet(fun, NULL, &#8220;bitpix=-32&#8221;);<br />
FunInfoGet(fun, FUN_SECT_DIM1, &amp;dim1, FUN_SECT_DIM2, &amp;dim2, 0);<br />
for (i = 0; i &lt; (dim1 * dim2); i++) {<br />
    &#8230; process buf[i]&#8230;<br />
}</p>
<p> Finally, you can write the resulting image to disk using <i>FunImagePut()</i>: </p>
<p>FunImagePut(fun2, buf, dim1, dim2, -32, NULL);</p>
<p> Note that Funtools automatically takes care of book-keeping tasks such as reading and writing <font SIZE="-1">FITS</font> headers (although you can, of course, write your own header or add your own parameters to a header). </p>
<p> For binary tables and raw event files, a call to <i>FunOpen()</i> will be followed by a call to the <i>FunColumnSelect()</i> routine to select columns to be read from the input file and/or written to the output file: </p>
<p>typedef struct evstruct {<br />
    double time;<br />
    int time2;<br />
} * Ev, EvRec;<br />
FunColumnSelect(fun, sizeof(EvRec), NULL,<br />
                &#8220;time&#8221;, &#8220;D&#8221;, &#8220;rw&#8221;, FUN_OFFSET(Ev, time),<br />
                &#8220;time2&#8221;, &#8220;J&#8221;, &#8220;w&#8221;, FUN_OFFSET(Ev, time2),<br />
                NULL);</p>
<p> Columns whose (third) mode argument contains an &#8220;r&#8221; are &#8220;readable&#8221;, i.e., columns will be read from the input file and converted into the data type specified in the call&#8217;s second argument. These columns values then are stored in the specified offset of the user record structure. Columns whose mode argument contains a &#8220;w&#8221; are &#8220;writable&#8221;, i.e., these values will be written to the output file. The <i>FunColumnSelect()</i> routine also offers the option of automatically merging user columns with the original input columns when writing the output rows. </p>
<p> Once a set of columns has been specified, you can retrieve rows using <i>FunTableRowGet()</i>, and write the rows using <i>FunTableRowPut()</i>: </p>
<p>Ev ebuf, ev;<br />
/* get rows &#8212; let routine allocate the array */<br />
while ((ebuf = (Ev)FunTableRowGet(fun, NULL, MAXROW, NULL, &amp;got))) {<br />
    /* process all rows */<br />
    for (i = 0; i &lt; got; i++) {<br />
        /* point to the i&#8217;th row */<br />
        ev = ebuf + i;<br />
        /* time2 is generated here */<br />
        ev-&gt;time2 = (int)(ev-&gt;time + .5);<br />
        /* change the input time as well */<br />
        ev-&gt;time = -(ev-&gt;time / 10.0);<br />
    }<br />
    /* write out this batch of rows with the new column */<br />
    FunTableRowPut(fun2, (char *)ebuf, got, 0, NULL);<br />
    /* free row data */<br />
    if (ebuf)<br />
        free(ebuf);<br />
}</p>
<p> The input rows are retrieved into an array of user structs, which can be accessed serially as shown above. Once again, Funtools automatically takes care of book-keeping tasks such as reading and writing <font SIZE="-1">FITS</font> headers (although you can, of course, write your own header or add your own parameters to a header). </p>
<p> When all processing is done, you can call <i>FunClose()</i> to close the file(s): </p>
<p>FunClose(fun2);<br />
FunClose(fun);</p>
<p> These are the basics of processing <font SIZE="-1">FITS</font> files (and arrays or raw event data) using Funtools. The routines in these examples are described in more detail below, along with a few other routines that support parameter access, data flushing, etc. </p>
<p> <code>Compiling and Linking</code> </p>
<p> To create a Funtools application, a software developer will include the funtools.h definitions file in Funtools code: </p>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p> The program is linked against the libfuntools.a library, along with the math library (and the dynamic load library, if the latter is available on your system): </p>
<pre>
  gcc -o foo foo.c -lfuntools -ldl -lm
</pre>
<p> If gcc is used, Funtools filtering can be performed using dynamically loaded shared objects that are built at run-time. Otherwise, filtering is performed using a slave process. </p>
<p> Funtools has been built on the following systems:</p>
<dl>
<dt>*</p>
<dd> Sun/Solaris 5.X</p>
<dt>*</p>
<dd> Linux/RedHat Linux 5.X,6.X,7.X</p>
<dt>*</p>
<dd> Dec Alpha/OSF1 V4.X</p>
<dt>*</p>
<dd> WindowsNT/Cygwin 1.0</p>
<dt>*</p>
<dd> <font SIZE="-1">SGI/IRIX64</font> 6.5</dl>
<p> <code>A Short Digression on Subroutine Order</code> </p>
<p> There is a natural order for all I/O access libraries. You would not think of reading a file without first opening it, or writing a file after closing it. A large part of the experiment in funtools is to use the idea of &#8220;natural order&#8221; as a means of making programming easier. We do this by maintaining the state of processing for a given funtools file, so that we can do things like write headers and flush extension padding at the right time, without you having to do it. </p>
<p> For example, if you open a new funtools file for writing using <i>FunOpen()</i>, then generate an array of image data and call <i>FunImagePut()</i>, funtools knows to write the image header automatically. There is no need to think about writing a standard header. Of course, you can add parameters to the file first by calling one of the <i>FunParamPut()</i> routines, and these parameters will automatically be added to the header when it is written out. There still is no need to write the header explicitly. </p>
<p> Maintaining state in this way means that there are certain rules of order which should be maintained in any funtools program. In particular, we strongly recommend the following ordering rules be adhered to:</p>
<dl>
<dt>*</p>
<dd> When specifying that input extensions be copied to an output file via a reference handle, open the output file <code>before</code> reading the input file. (Otherwise the initial copy will not occur).</p>
<dt>*</p>
<dd> Always write parameters to an output file using one of the <i>FunParamPut()</i> calls <code>before</code> writing any data. (This is a good idea for all <font SIZE="-1">FITS</font> libraries, to avoid having to recopy data is the <font SIZE="-1">FITS</font> header needs to be extended by adding a single parameter.)</p>
<dt>*</p>
<dd> If you retrieve an image, and need to know the data type, use the <font SIZE="-1">FUN_SECT_BITPIX</font> option of <i>FunInfoGet()</i>, <code>after</code> calling <i>FunImageGet()</i>, since it is possible to change the value of <font SIZE="-1">BITPIX</font> from the latter.</p>
<dt>*</p>
<dd> When specifying that input extensions be copied to an output file via a reference handle, close the output file <code>before</code> closing input file, or else use <i>FunFlush()</i> explicitly on the output file <code>before</code> closing the input file. (Otherwise the final copy will not occur).</dl>
<p> We believe that these are the natural rules that are implied in most <font SIZE="-1">FITS</font> programming tasks. However, we recognize that making explicit use of &#8220;natural order&#8221; to decide what automatic action to take on behalf of the programmer is experimental. Therefore, if you find that your needs are not compatible with our preferred order, please let us know &#8212; it will be most illuminating for us as we evaluate this experiment. </p>
<p> <code>Funtools Programming Examples</code> </p>
<p> The following complete coding examples are provided to illustrate the simplicity of Funtools applications. They can be found in the funtest subdirectory of the Funtools distribution. In many cases, you should be able to modify one of these programs to generate your own Funtools program:</p>
<dl>
<dt>*</p>
<dd> evread.c: read and write binary tables</p>
<dt>*</p>
<dd> evcols.c: add column and rows to binary tables</p>
<dt>*</p>
<dd> evmerge.c: merge new columns with existing columns</p>
<dt>*</p>
<dd> evnext.c: manipulate raw data pointers</p>
<dt>*</p>
<dd> imblank.c: blank out image values below a threshold</p>
<dt>*</p>
<dd> asc2fits.c: convert a specific <font SIZE="-1">ASCII</font> table to <font SIZE="-1">FITS</font> binary table</dl>
<p> <code>The Funtools Programming Reference Manual</code> </p>
<p> #include &lt;<a href="file:/usr/include/funtools.h">funtools.h</a>&gt; </p>
<p> Fun FunOpen(char *name, char *mode, Fun ref) </p>
<p> void *FunImageGet(Fun fun, void *buf, char *plist) </p>
<p> int FunImagePut(Fun fun, void *buf, int dim1, int dim2, int bitpix, char *plist) </p>
<p> void * FunImageRowGet(Fun fun, void *buf, int rstart, int rstop, char *plist) </p>
<p> void * FunImageRowPut(Fun fun, void *buf, int rstart, int rstop, int dim1, int dim2, int bitpix, char *plist) </p>
<p> int FunColumnSelect(Fun fun, int size, char *plist, &#8230;) </p>
<p> void FunColumnActivate(Fun fun, char *s, char *plist) </p>
<p> int FunColumnLookup(Fun fun, char *s, int which, char **name, int *type, int *mode, int *offset, int *n, int *width) </p>
<p> void *FunTableRowGet(Fun fun, void *rows, int maxrow, char *plist, int *nrow) </p>
<p> int FunTableRowPut(Fun fun, void *rows, int nev, int idx, char *plist) </p>
<p> int FunParamGetb(Fun fun, char *name, int n, int defval, int *got) </p>
<p> int FunParamGeti(Fun fun, char *name, int n, int defval, int *got) </p>
<p> double FunParamGetd(Fun fun, char *name, int n, double defval, int *got) </p>
<p> char *FunParamGets(Fun fun, char *name, int n, char *defval, int *got) </p>
<p> int FunParamPutb(Fun fun, char *name, int n, int value, char *comm, int append) </p>
<p> int FunParamPuti(Fun fun, char *name, int n, int value, char *comm, int append) </p>
<p> int FunParamPutd(Fun fun, char *name, int n, double value, int prec, char *comm, int append) </p>
<p> int FunParamPuts(Fun fun, char *name, int n, char *value, char *comm, int append) </p>
<p> int FunInfoGet(Fun fun, int type, &#8230;) </p>
<p> int FunInfoPut(Fun fun, int type, &#8230;) </p>
<p> void FunFlush(Fun fun, char *plist) </p>
<p> void FunClose(Fun fun)</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
