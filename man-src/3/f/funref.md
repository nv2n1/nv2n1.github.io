---
title: "funref(3)"
name: "funref"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funref/"
description: "FunRef: the Funtools Reference Handle"
---

<h2>NAME</h2>
<p> <code>FunRef: the Funtools Reference Handle</code></p>
<h2>SYNOPSIS</h2>
<p> A description of how to use a Funtools reference handle to connect a Funtools input file to an output file.</p>
<h2>DESCRIPTION</h2>
<p> The Funtools reference handle connects a Funtools input file to a Funtools output file so that parameters (or even whole extensions) can be copied from the one to the other. To make the connection, the Funtools handle of the input file is passed to the final argument of the <i>FunOpen()</i> call for the output file: </p>
<pre><code>
if (!(ifun = FunOpen(argv[1], "r", NULL)))
    gerror(stderr, "could not FunOpen input file: %s
", argv[1]);
if (!(ofun = FunOpen(argv[2], "w", ifun)))
    gerror(stderr, "could not FunOpen output file: %s
", argv[2]);
</code></pre>
<p> It does not matter what type of input or output file (or extension) is opened, or whether they are the same type. When the output image or binary table is written using <i>FunImagePut()</i> or <i>FunTableRowPut()</i> an appropriate header will be written first, with parameters copied from the input extension. Of course, invalid parameters will be removed first, e.g., if the input is a binary table and the output is an image, then binary table parameters such as <font SIZE="-1">TFORM</font>, <font SIZE="-1">TUNIT</font>, etc. parameters will not be copied to the output. </p>
<p> Use of a reference handle also allows default values to be passed to <i>FunImagePut()</i> in order to write out an output image with the same dimensions and data type as the input image. To use the defaults from the input, a value of 0 is entered for dim1, dim2, and bitpix. For example: </p>
<p>fun = FunOpen(argv[1], &#8220;r&#8221;, NULL);<br />
fun2 = FunOpen(argv[2], &#8220;w&#8221;, fun);<br />
buf = FunImageGet(fun, NULL, NULL);<br />
&#8230; process image data&#8230; FunImagePut(fun2, buf, 0, 0, 0, NULL);</p>
<p> Of course, you often want to get information about the data type and dimensions of the image for processing. The above code is equivalent to the following: </p>
<p>fun = FunOpen(argv[1], &#8220;r&#8221;, NULL);<br />
fun2 = FunOpen(argv[2], &#8220;w&#8221;, fun);<br />
buf = FunImageGet(fun, NULL, NULL);<br />
FunInfoGet(fun, FUN_SECT_DIM1, &amp;dim1, FUN_SECT_DIM2, &amp;dim2,<br />
           FUN_SECT_BITPIX, &amp;bitpix, 0);<br />
&#8230; process image data&#8230; FunImagePut(fun2, buf, dim1, dim2, bitpix, NULL);</p>
<p> It is possible to change the reference handle for a given output Funtools handle using the <i>FunInfoPut()</i> routine: </p>
<p>/* make the new extension the reference handle for the output file */<br />
FunInfoPut(fun2, FUN_IFUN, &amp;fun, 0);</p>
<p> When this is done, Funtools specially resets the output file to start a new output extension, which is connected to the new input reference handle. You can use this mechanism to process multiple input extensions into a single output file, by successively opening the former and setting the reference handle for the latter. For example: </p>
<p>/* open a new output FITS file */<br />
if (!(fun2 = FunOpen(argv[2], &#8220;w&#8221;, NULL)))<br />
    gerror(stderr, &#8220;could not FunOpen output file: %s
&#8221;, argv[2]);<br />
/* process each input extension in turn */<br />
for (ext = 0;; ext++) {<br />
    /* get new extension name */<br />
    sprintf(tbuf, &#8220;%s[%d]&#8221;, argv[1], ext);<br />
    /* open it &#8212; if we cannot open it, we are done */<br />
    if (!(fun = FunOpen(tbuf, &#8220;r&#8221;, NULL)))<br />
        break;<br />
    /* make the new extension the reference handle for the output file */<br />
    FunInfoPut(fun2, FUN_IFUN, &amp;fun, 0);<br />
    &#8230; process&#8230;<br />
        /* flush output extension (write padding, etc.) */<br />
        FunFlush(fun2, NULL);<br />
    /* close the input extension */<br />
    FunClose(fun);<br />
}</p>
<p> In this example, the output file is opened first. Then each successive input extension is opened, and the output reference handle is set to the newly opened input handle. After data processing is performed, the output extension is flushed and the input extension is closed, in preparation for the next input extension. </p>
<p> Finally, a reference handle can be used to copy other extensions from the input file to the output file. Copy of other extensions is controlled by adding a &#8220;C&#8221; or &#8220;c&#8221; to the mode string of the <i>FunOpen()</i> call <code>of the input reference file</code>. If &#8220;C&#8221; is specified, then other extensions are <code>always</code> copied (i.e., copy is forced by the application). If &#8220;c&#8221; is used, then other extensions are copied if the user requests copying by adding a plus sign &#8220;+&#8221; to the extension name in the bracket specification. For example, the <code>funtable</code> program utilizes user-specified &#8220;c&#8221; mode so that the second example below will copy all extensions: </p>
<p>#copy only the EVENTS extension<br />
csh &gt; funtable &#8220;test.ev[EVENTS,circle(512,512,10)]&#8221; foo.ev<br />
#copy ALL extensions<br />
          csh &gt; funtable &#8220;test.ev[EVENTS+,circle(512,512,10)]&#8221; foo.ev</p>
<p> When extension copy is specified in the input file, the call to <i>FunOpen()</i> on the input file delays the actual file open until the output file also is opened (or until I/O is performed on the input file, which ever happens first). Then, when the output file is opened, the input file is also opened and input extensions are copied to the output file, up to the specific extension being opened. Processing of input and output extensions then proceed. </p>
<p> When extension processing is complete, the remaining extensions need to be copied from input to output. This can be done explicitly, using the <i>FunFlush()</i> call with the &#8220;copy=remaining&#8221; plist: </p>
<pre>
  FunFlush(fun, &quot;copy=remaining&quot;);
</pre>
<p> Alternatively, this will happen automatically, if the output file is closed <code>before</code> the input file: </p>
<pre><code>
/* we could explicitly flush remaining extensions that need copying */
/* FunFlush(fun2, "copy=remaining"); */
/* but if we close output before input, end flush is done automatically  */
FunClose(fun2);
FunClose(fun);
</code></pre>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
