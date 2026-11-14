---
title: "funopen(3)"
name: "funopen"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funopen/"
description: "FunOpen – open a Funtools data file"
---

<h2>NAME</h2>
<p> <code>FunOpen &#8211; open a Funtools data file</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p>Fun FunOpen(char *name, char *mode, Fun ref);</p>
<h2>DESCRIPTION</h2>
<p> The FunOpen() routine opens a Funtools data file for reading or appending, or creates a new <font SIZE="-1">FITS</font> file for writing. The <code>name</code> argument specifies the name of the Funtools data file to open. You can use IRAF-style bracket notation to specify Funtools Files, Extensions, and Filters. A separate call should be made each time a different <font SIZE="-1">FITS</font> extension is accessed: </p>
<p>Fun fun;<br />
char *iname;<br />
&#8230; if (!(fun = FunOpen(iname, &#8220;r&#8221;, NULL)))<br />
{<br />
    fprintf(stderr, &#8220;could not FunOpen input file: %s
&#8221;, iname);<br />
    exit(1);<br />
}</p>
<p> If <code>mode</code> is &#8220;r&#8221;, the file is opened for reading, and processing is set up to begin at the specified extension. For reading, <code>name</code> can be <code>stdin</code>, in which case the standard input is read. </p>
<p> If <code>mode</code> is &#8220;w&#8221;, the file is created if it does not exist, or opened and truncated for writing if it does exist. Processing starts at the beginning of the file. The <code>name</code> can be <code>stdout</code>, in which case the standard output is readied for processing. </p>
<p> If <code>mode</code> is &#8220;a&#8221;, the file is created if it does not exist, or opened if it does exist. Processing starts at the end of the file. The <code>name</code> can be <code>stdout</code>, in which case the standard output is readied for processing. </p>
<p> When a Funtools file is opened for writing or appending, a previously opened Funtools reference handle can be specified as the third argument. This handle typically is associated with the input Funtools file that will be used to generate the data for the output data. When a reference file is specified in this way, the output file will inherit the (extension) header parameters from the input file: </p>
<p>Fun fun, fun2;<br />
&#8230;<br />
    /* open input file */<br />
    if (!(fun = FunOpen(argv[1], &#8220;r&#8221;, NULL)))<br />
        gerror(stderr, &#8220;could not FunOpen input file: %s
&#8221;, argv[1]);<br />
/* open the output FITS image, inheriting params from input */<br />
if (!(fun2 = FunOpen(argv[2], &#8220;w&#8221;, fun)))<br />
    gerror(stderr, &#8220;could not FunOpen output file: %s
&#8221;, argv[2]);</p>
<p> Thus, in the above example, the output <font SIZE="-1">FITS</font> binary table file will inherit all of the parameters associated with the input binary table extension. </p>
<p> A file opened for writing with a Funtools reference handle also inherits the selected columns (i.e. those columns chosen for processing using the <i>FunColumnSelect()</i> routine) from the reference file as its default columns. This makes it easy to open an output file in such a way that the columns written to the output file are the same as the columns read in the input file. Of course, column selection can easily be tailored using the <i>FunColumnSelect()</i> routine. In particular, it is easy to merge user-defined columns with the input columns to generate a new file. See the evmerge for a complete example. </p>
<p> In addition, when a Funtools reference handle is supplied in a <i>FunOpen()</i> call, it is possible also to specify that all other extensions from the reference file (other than the input extension being processed) should be copied from the reference file to the output file. This is useful, for example, in a case where you are processing a <font SIZE="-1">FITS</font> binary table or image and you want to copy all of the other extensions to the output file as well. Copy of other extensions is controlled by adding a &#8220;C&#8221; or &#8220;c&#8221; to the mode string of the <i>FunOpen()</i> call of the input reference file. If &#8220;C&#8221; is specified, then other extensions are <code>always</code> copied (i.e., copy is forced by the application). If &#8220;c&#8221; is used, then other extensions are copied if the user requests copying by adding a plus sign &#8220;+&#8221; to the extension name in the bracket specification. For example, the <code>funtable</code> program utilizes &#8220;c&#8221; mode, giving users the option of copying all other extensions: </p>
<p>/* open input file &#8212; allow user copy of other extensions */<br />
if (!(fun = FunOpen(argv[1], &#8220;rc&#8221;, NULL)))<br />
    gerror(stderr, &#8220;could not FunOpen input file: %s
&#8221;, argv[1]);<br />
/* open the output FITS image, inheriting params from input */<br />
if (!(fun2 = FunOpen(argv[2], &#8220;w&#8221;, fun)))<br />
    gerror(stderr, &#8220;could not FunOpen output file: %s
&#8221;, argv[2]);</p>
<p> Thus, <code>funtable</code> supports either of these command lines: </p>
<pre><code>
#copy only the EVENTS extension
csh &gt; funtable "test.ev[EVENTS,circle(512,512,10)]" foo.ev
#copy ALL extensions
          csh &gt; funtable "test.ev[EVENTS+,circle(512,512,10)]" foo.ev
</code></pre>
<p> Use of a Funtools reference handle implies that the input file is opened before the output file. However, it is important to note that if copy mode (&#8220;c&#8221; or &#8220;C&#8221;) is specified for the input file, the actual input file open is delayed until just after the output file is opened, since the copy of prior extensions to the output file takes place while Funtools is seeking to the specified input extension. This implies that the output file should be opened before any I/O is done on the input file or else the copy will fail. Note also that the copy of subsequent extension will be handled automatically by <i>FunClose()</i> if the output file is closed before the input file. Alternatively, it can be done explicitly by <i>FunFlush()</i>, but again, this assumes that the input file still is open. </p>
<p> Upon success <i>FunOpen()</i> returns a Fun handle that is used in subsequent Funtools calls. On error, <font SIZE="-1">NULL</font> is returned.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
