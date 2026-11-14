---
title: "gcl(1)"
name: "gcl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcl/"
description: "gcl – GCL Common Lisp interpreter/compiler"
---

<h2>NAME</h2>
<p> gcl &#8211; GCL Common Lisp interpreter/compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>gcl</code> [ <code>options</code> ] </p>
<h2>DESCRIPTION</h2>
<p> The program <i>gcl</i> is an implementation of a subset of the Common Lisp Ansi standard. It is written in C and in Common Lisp, and is highly portable. It includes those features in the original definition of Common Lisp, (Guy Steele version 1.), as well as some features from the proposed new standard. </p>
<p> The best documentation is available in <i>texinfo/info</i> form, with there being three groups of information. <i>gcl-si</i> for basic common lisp descriptions, and features unique to <i>gcl</i> The <i>gcl-tk</i> info refers to the connection with <i>tk</i> window system, allowing all the power of the <i>tcl/tk</i> interaction system to be used from lisp. The third info file <i>gcl</i> details the Ansi standard for common lisp, to which this subset tries to adhere. It is highly recommended to write programs, which will be in the intersection of gcl and ansi common lisp. Unfortunately the Ansi standard is huge, and will require a substantial effort, and increase in the size of gcl, to include all of it. </p>
<p> When <i>gcl</i> is invoked from the shell, the variable <i>si::*command-args*</i> is set to the list of command line arguments. Various <i>options</i> are understood:</p>
<dl>
<dt><code>-eval command</code></p>
<dd> Call<code>read</code>and<code>then</code>eval<code>on</code>the <i>command passed in.</i></p>
<dt><code>-load pathname</code></p>
<dd> Load<code>the</code>file<code>whose</code> <i>pathname</i> is specified after <code>-load</code>.</p>
<dt><code>-f</code></p>
<dd> Replace si::*command-args* by the the list starting after <code>-f</code>. Open the file following <code>-f</code>for<code>input,</code>skip<code>the</code>first<code>line,</code>and then read and eval the rest of the forms in the file. This can be used as with the shells to write small shell programs: </p>
</dl>
<p> #!/usr/local/bin/gcl.exe -f<br />
 (format t &quot;hello world ~a~%&quot; (nth 1 si::*command-args*)) </p>
<p> <code>The</code>value <i>si::*command-args*</i> will have the appropriate value. Thus if the above 2 line file is made executable and called <i>foo</i> then </p>
<p> tutorial% foo billy<br />
 hello world billy </p>
<p> <code>NOTE:</code>On<code>many</code>systems<code>(eg</code>SunOs)<code>the</code>first<code>line</code>of<code>an</code>executable script file such as: <code>#!/usr/local/bin/gcl.exe</code>-f only reads the first 32 characters! So if your pathname where the executable together with the &#8216;-f&#8217; amount to more than 32 characters the file will not be recognized. Also the executable must be the actual large binary file, [or a link to it], and not just a <i>/bin/sh</i> script. In latter case the <i>/bin/sh</i> interpreter would get invoked on the file. </p>
<p> Alternately one could invoke the file <i>foo</i> without making it executable: </p>
<p> tutorial% gcl -f foo &quot;from bill&quot;<br />
 hello world from bill </p>
<dl>
<dt><code>-batch</code></p>
<dd> Do<code>not</code>enter<code>the</code>command<code>print</code>loop.<code>Useful</code>if<code>the</code>other<code>command</code> line arguments do something. Do not print the License and acknowledgement information. Note if your program does print any License information, it must print the GCL header information also. </p>
<dt><code>-dir</code></p>
<dd> Directory<code>where</code>the<code>executable</code>binary<code>that</code>is<code>running</code>is<code>located.</code> Needed by save and friends. This gets set as si::*system-directory* </p>
<dt><code>-libdir</code></p>
<dd> .BR<code>-libdir</code> <i>/d/wfs/gcl-2.0/</i> would mean that the files like gcl-tk/tk.o would be found by concatting the path to the libdir path, ie in /d/wfs/gcl-2.0/gcl-tk/tk.o </p>
<dt><code>-compile</code></p>
<dd> Invoke<code>the</code>compiler<code>on</code>the<code>filename</code>following <code>-compile</code> flags affect compilation. </p>
<dt><code>-o-file</code></p>
<dd> If<code>nil</code>follows <code>-o-file</code> then do not produce an <i>.o</i> file. </p>
<dt><code>-c-file</code></p>
<dd> If <code>-c-file</code> is specified, leave the intermediate <i>.c</i> file there. </p>
<dt><code>-h-file</code></p>
<dd> If <code>-h-file</code> is specified, leave the intermediate <i>.h</i> file there. </p>
<dt><code>-data-file</code></p>
<dd> If <code>-data-file</code> is specified, leave the intermediate <i>.data</i> file there. </p>
<dt><code>-system-p</code></p>
<dd> If <code>-system-p</code> is specified then invoke <i>compile-file</i> with the <i>:system-p t</i> keyword argument, meaning that the C init function will bear a name based on the name of the file, so that it may be invoked by name by C code. </p>
<p> This GNU package should not be confused with the proprietary program distributed by FRANZ, Inc. Nor should it be confused with the public domain or the proprietary . For anything other than program development, use of the lisp compiler <i><a href="//www.systutorials.com/docs/linux/man/1L-glc/">glc</a></i>(1L) is strongly recommended in preference to use of the interpreter, due to much higher speed.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/site/subsys/gcl/bin/gcl</p>
<dd> executable file</p>
<dt>/site/subsys/gcl/bin/gclc</p>
<dd> compiler</p>
<dt>/usr/include/cmpinclude.h</p>
<dd> C library file</dl>
<p> </i></p>
<h2>SEE ALSO</h2>
<p> <i>Common LISP: The Language</i>, Guy L. Steele, Jr., Digital Press, Bedford, MA, 1984. </p>
<p> <i>Common LISPcraft</i>, Robert Wilensky, W. W. Norton &amp; Co., New York, 1984.</p>
<h2>AUTHORS</h2>
<p> The GCL system contains C and Lisp source files to build a Common Lisp sytem. CGL is derived from Kyoto Common LISP (<i>kcl</i>), which was written in 1984 by T. Yuasa and M. Hagiya (working under Professor R. Nakajima at the Research Institute for Mathematical Sciences, Kyoto University). The AKCL system work was begun in 1987 by William Schelter at the University of Texas, Austin, and continued through 1994. In 1994 AKCL was released as GCL (GNU Common Lisp) under the GNU public library license. </p>
<h2>Index</h2>
