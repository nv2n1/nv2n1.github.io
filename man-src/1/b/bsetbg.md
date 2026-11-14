---
title: "bsetbg(1)"
name: "bsetbg"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsetbg/"
description: "bsetbg – utility to manipulate the appearance of the X11 desktop’s root window."
---

<h2>NAME</h2>
<p> bsetbg &#8211; utility to manipulate the appearance of the X11 desktop&#8217;s root window.</p>
<h2>SYNOPSIS</h2>
<p> <code>bsetbg</code> [options] <i>image</i></p>
<h2>DESCRIPTION</h2>
<p> <code>bsetbg</code> is intended to provide a standard method for the <i>Blackbox</i> window manager to alter the background of the root window (although it will work with any other window manager as well). <code>bsetbg</code> acts as a wrapper both to <i>bsetroot</i> and to a flexible variety of third-party applications that it uses when handling images files. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code>, <code>-full</code> <i>image</i></p>
<dd> <i>image</i> is stretched to fill the entire desktop.</p>
<dt><code>-t</code>, <code>-tile</code> <i>image</i></p>
<dd> <i>image</i> is tiled on the desktop.</p>
<dt><code>-c</code>, <code>-center</code> <i>image</i></p>
<dd> <i>image</i> is centered on the desktop.</p>
<dt><code>-e</code>, <code>-exec</code> <i>program</i> <i>options</i> <i>fallback-arg</i> <i>image</i></p>
<dd> This option tells <code>bsetbg</code> to run a separate command by executing <i>program</i> with <i>options</i>, where <i>options</i> are arguments to <i>program</i>. </p>
<p> If a <i>fallback-arg</i> is supplied (<code>-full</code>, <code>-tile</code>, or <code>-center</code> as described above), <code>bsetbg</code> will assume that the last argument is a filename. In the case that <i>program</i> exits non-zero or isn&#8217;t available on the target system, <code>bsetbg</code> will try to handle the file with the fallback argument. </p>
<p> See the <code>EXAMPLES</code> section for more information on <code>-exec</code>.</p>
<dt><code>-p</code>, <code>-post</code> <i>list</i></p>
<dd> Specifies a list of arguments to pass to the $POST_COMMAND.</p>
<dt><code>-d</code>, <code>-debug</code></p>
<dd> Debugging mode. <code>bsetbg</code> will print commands without executing them.</p>
<dt><code>-g</code>, <code>-generate</code> <i>list</i></p>
<dd> Output a list of default configuration values, suitable for redirecting into <i>~/.bsetbgrc</i>. Any arguments that are supplied will be considered applications to search for in the system path, overriding <code>bsetbg</code>&#8216;s internal defaults.</p>
<dt><code>-app</code> <i>imageApp</i></p>
<dd> Use this flag to specify which image application to use. This application may be one of the pre-defined list or any application capable of displaying an image on the root window. This flag may be used in conjunction with passing application specific parameters to the application, in which case they should be enclosed in double quotes.</p>
<dt><code>-v</code>, <code>-version</code></p>
<dd> Output version number.</p>
<dt><code>-h</code>, <code>-help</code></p>
<dd> Output a brief usage message. </p>
</dl>
<h2>OTHER OPTIONS</h2>
<p> <code>bsetbg</code> will also accept all of the arguments for <i>bsetroot</i>. Consult the <i><a href="/docs/linux/man/1-bsetroot/">bsetroot</a></i>(1) man page for further information. </p>
<h2>CONFIGURATION</h2>
<p> <code>bsetbg</code> will read its configuration values from the file <i>~/.bsetbgrc</i> if it exists. Otherwise, it will scan the system path for a pre-defined list of image applications to use (currently this list consists of qiv, xli, xv, wmsetbg, Esetroot, display, and xsetbg). <i>~/.bsetbgrc</i> should contain the following variables:</p>
<dl>
<dt><code> CENTER=</code><i>&quot;string&quot;</i></p>
<dd> Application and arguments to be used to center an image on the root window when the <code>-center</code> argument is specified. </p>
<dt><code> FULL=</code><i>&quot;string&quot;</i></p>
<dd> Application and arguments to be used to stretch an image to fill the root window when the <code>-full</code> argument is specified. </p>
<dt><code> TILE=</code><i>&quot;string&quot;</i></p>
<dd> Application and arguments to be used to tile an image on the root window when the <code>-tile</code> argument is specified. </p>
<dt><code> DEFAULT=</code><i>&quot;string&quot;</i></p>
<dd> Action to take place by default if none of the above have been specified. </p>
<dt>The following variables are optional:</p>
<dd>
<dt><code> NO_EXEC=</code><i>&quot;boolean&quot;</i></p>
<dd> If this variable is set, bsetbg will never modify the root window. </p>
<dt><code> POST_COMMAND=</code><i>&quot;string&quot;</i></p>
<dd> This variable specifies a command that <code>bsetbg</code> will run after every successful modification of the root window. </p>
<dt><code> LOG_LAST_CMD=</code><i>&quot;boolean&quot;</i></p>
<dd> If this variable is set, <code>bsetbg</code> will keep a logfile of the last two successful commands. </p>
<dt><code> LOGFILE=</code><i>&quot;string&quot;</i></p>
<dd> This variable can specify the logfile to be used when $LOG_LAST_CMD is defined. The default is ~/.bsetbg_last_cmd . </p>
<dt>As mentioned above, <code>bsetbg</code> will function perfectly for the majority of users without having a configuration file. Power users who want more control over <code>bsetbg</code>&#8216;s behavior should run <code>bsetbg -g</code> and use the output to create a <i>~/.bsetbgrc</i> which may then be tweaked by hand.</p>
<dd>
</dl>
<h2>EXAMPLES</h2>
<p> In this example, bsetbg will set the image in centered mode: </p>
<p>&nbsp;<wbr>bsetbg -center foo.png </p>
<p> An example of the <code>-exec</code> argument: </p>
<p>&nbsp;<wbr>bsetbg -exec xv -root -quit -rmode 5 -rbg rgb:2/2/2&nbsp;<wbr>\ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-center foo.png</p>
<p> An example in which bsetbg creates a configuration file using xv and qiv: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bsetbg -g xv qiv &gt; ~/.bsetbgrc</p>
<p> An example of the use of the <code>-app</code> argument: </p>
<p>&nbsp;<wbr>bsetbg&nbsp;<wbr>&nbsp;<wbr>-app qiv&nbsp;<wbr>&quot;-o rgb:d6/c5/a2 -x&quot;&nbsp;<wbr>-c foo.png </p>
<h2>AUTHOR</h2>
<p> The author of <code>bsetbg</code> may be reached at <i>tmk [at] lordzork.com</i>. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-blackbox/">blackbox</a></i>(1), <i><a href="/docs/linux/man/1-bsetroot/">bsetroot</a></i>(1), <i><a href="/docs/linux/man/1-qiv/">qiv</a></i>(1), <i><a href="/docs/linux/man/1-xli/">xli</a></i>(1), <i><a href="/docs/linux/man/1-xv/">xv</a></i>(1), <i><a href="/docs/linux/man/1-display/">display</a></i>(1), <i><a href="/docs/linux/man/1-wmsetbg/">wmsetbg</a></i>(1) </p>
<h2>Index</h2>
