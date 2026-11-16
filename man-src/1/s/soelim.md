---
title: "soelim(1)"
name: "soelim"
section: "1"
letter: "s"
url: "/docs/linux/man/1-soelim/"
description: "soelim – interpret .so requests in groff input"
---

<h2 class="name">NAME</h2>
<p> soelim &#8211; interpret .so requests in groff input </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-Crtv</code> ] [ <code>-I </code><i>dir</i> ] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>soelim</code> reads <i>files</i> and replaces lines of the form</p>
<dl>
<dt>
</dt><dd> <code>.so~</code><i>file</i></dd></dl>
<p> by the contents of <i>file</i>. It is useful if files included with <code>.so</code> need to be preprocessed. Normally, <code>soelim</code> should be invoked with the <code>-s</code> option of <code>groff</code>. </p>
<p> To embed &#8216;\&#8217; in the file name, write &#8216;\&#8217; or &#8216;&#8217;. To embed a space, write &#8216;\&nbsp;&#8216;. Any other escape sequence in <i>file</i> makes <code>soelim</code> ignore the whole line. </p>
<p> Note that there must be no whitespace between the leading dot and the two characters &#8216;s&#8217; and &#8216;o&#8217;. Otherwise, only <code>groff</code> interprets the <code>.so</code> request (and <code>soelim</code> ignores it).</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-C</code></dt>
<dd> Recognize <code>.so</code> even when followed by a character other than space or newline.</dd>
<dt><code>-I</code><i>dir</i></dt>
<dd> This option may be used to add a directory to the search path for files (both those on the command line and those named in <code>.so</code> requests). The search path is initialized with the current directory. This option may be specified more than once; the directories are then searched in the order specified (but before the current directory). If you want to make the current directory be read before other directories, add <code>-I.</code> at the appropriate place.</dd>
<dt>
</dt><dd> No directory search is performed for files with an absolute file name.</dd>
<dt><code>-r</code></dt>
<dd> Do not add <code>.lf</code> requests (for general use, with non-groff files).</dd>
<dt><code>-t</code></dt>
<dd> Don&#8217;t emit <code>.lf</code> requests but TeX comment lines (starting with &#8216;%&#8217;) giving the current file and line number.</dd>
<dt><code>-v</code></dt>
<dd> Print the version number.</dd></dl>
<h2>USAGE</h2>
<p> The normal processing sequence of groff is this: </p>
<pre>
          input        sourced
          file          file
            |             |
            v             v
        preprocessor -&gt; troff -&gt; postprocessor
                                      |
                                      v
                                   output
                                    file
</pre>
<p> That is, files sourced with <code>.so</code> are normally read <i>only</i> by <code>troff</code> (the actual formatter). <code>soelim</code> is <i>not</i> required for <code>troff</code> to source files. </p>
<p> If a file to be sourced should also be preprocessed, it must already be read <i>before</i> the input file passes through the preprocessor. This is handled by <code>soelim</code>: </p>
<pre>
          input
          file
            |
            v
          soelim -&gt; preprocessor -&gt; troff -&gt; postprocessor
            ^                                     |
            |                                     v
         sourced                               output
          file                                  file
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) </p>
<h2>Index</h2>
