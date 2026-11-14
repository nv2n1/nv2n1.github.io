---
title: "ppl-config(1)"
name: "ppl-config"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppl-config/"
description: "ppl-config – obtain information about an installation of the Parma Polyhedra Library"
---

<h2>NAME</h2>
<p> ppl-config &#8211; obtain information about an installation of the Parma Polyhedra Library</p>
<h2>SYNOPSIS</h2>
<p> <code>ppl-config</code> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Displays information, in various formats, about an installation of the Parma Polyhedra Library.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> prints this help text to stdout</p>
<dt><code>-FFMT</code>, <code>&#8211;format</code>=<i>FMT</i></p>
<dd> sets the output format to FMT (one of `plain&#8217;, `makefile&#8217;, `sh&#8217; or `csh&#8217;)</p>
<dt><code>-IINT</code>, <code>&#8211;interface</code>=<i>INT</i></p>
<dd> selects a library interface (one of `C++&#8217;, `C&#8217;, `Ciao-Prolog&#8217;, `GNU-Prolog&#8217;, `SICStus-Prolog&#8217;, `SWI-Prolog&#8217;, `XSB-Prolog&#8217;, `YAP-Prolog&#8217;, `OCaml&#8217; or `Java&#8217;)</p>
<dt><code>-A</code>, <code>&#8211;application</code></p>
<dd> selects output for building an application</p>
<dt><code>-L</code>, <code>&#8211;library</code></p>
<dd> selects output for building a library</p>
<dt><code>-p[PFX]</code>, <code>&#8211;prefix</code>[=<i>PFX</i>]</p>
<dd> prints or sets library prefix information</p>
<dt><code>-e[PFX]</code>, <code>&#8211;exec-prefix</code>[=<i>PFX</i>]</p>
<dd> prints or sets library exec-prefix information</p>
<dt><code>-O</code>, <code>&#8211;configure-options</code></p>
<dd> prints configuration options</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> prints version information</p>
<dt><code>-M</code>, <code>&#8211;version-major</code></p>
<dd> prints version major number</p>
<dt><code>-N</code>, <code>&#8211;version-minor</code></p>
<dd> prints version minor number</p>
<dt><code>-R</code>, <code>&#8211;version-revision</code></p>
<dd> prints version revision number</p>
<dt><code>-B</code>, <code>&#8211;version-beta</code></p>
<dd> prints version beta number</p>
<dt><code>-E</code>, <code>&#8211;banner</code></p>
<dd> prints library banner</p>
<dt><code>-n</code>, <code>&#8211;coefficients</code></p>
<dd> prints type of library coefficients</p>
<dt><code>-i</code>, <code>&#8211;includedir</code></p>
<dd> prints include files directory</p>
<dt><code>-b</code>, <code>&#8211;bindir</code></p>
<dd> prints binary executables directory</p>
<dt><code>-l</code>, <code>&#8211;libdir</code></p>
<dd> prints library files directory</p>
<dt><code>-P</code>, <code>&#8211;cppflags</code></p>
<dd> prints preprocessor flags</p>
<dt><code>-C</code>, <code>&#8211;cflags</code></p>
<dd> prints C compiler flags</p>
<dt><code>-X</code>, <code>&#8211;cxxflags</code></p>
<dd> prints C++ compiler flags</p>
<dt><code>-D</code>, <code>&#8211;ldflags</code></p>
<dd> prints linker flags</p>
<dt><code>-g</code>, <code>&#8211;license</code></p>
<dd> prints synthetic licensing information</p>
<dt><code>-c</code>, <code>&#8211;copying</code></p>
<dd> prints detailed licensing information</p>
<dt><code>-u</code>, <code>&#8211;bugs</code></p>
<dd> prints bug reporting information</p>
<dt><code>-r</code>, <code>&#8211;credits</code></p>
<dd> prints credits</dl>
<h2>AVAILABILITY</h2>
<p> The latest version of the Parma Polyhedra Library and all the documentation is available at <code><a rel="nofollow" href="http://www.cs.unipr.it/ppl/">http://www.cs.unipr.it/ppl/</a></code>. </p>
<h2>AUTHOR</h2>
<p> See the file <code>CREDITS</code> in the source distribution or use the command <code>ppl-config &#8211;credits</code> for a list of contributors. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ppl-devel [at] cs.unipr.it&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ppl-devel [at] cs.unipr.it&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2001-2010 Roberto Bagnara &lt;bagnara [at] cs.unipr.it&gt; Copyright (C) 2010-2011 BUGSENG srl (<a rel="nofollow" href="http://bugseng.com)">http://bugseng.com)</a><br />
 This is free software; see the file <code>COPYING</code> in the source distribution or use the command <code>ppl-config &#8211;copying</code> to obtain the copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libppl/">libppl</a>(3)</code> </p>
<p> <code><a href="/docs/linux/man/3-libppl_c/">libppl_c</a>(3)</code> </p>
<p> Roberto Bagnara, Patricia M. Hill, and Enea Zaffanella. <i>The Parma Polyhedra Library User&#8217;s Manual (version 0.11.2),</i> available (in several formats) at <code><a rel="nofollow" href="http://www.cs.unipr.it/ppl/">http://www.cs.unipr.it/ppl/</a></code> . </p>
<p> Roberto Bagnara, Patricia M. Hill, and Enea Zaffanella. <i>The Parma Polyhedra Library C Language Interface User&#8217;s Manual (version 0.11.2),</i> available (in several formats) at <code><a rel="nofollow" href="http://www.cs.unipr.it/ppl/">http://www.cs.unipr.it/ppl/</a></code> . </p>
<p> Roberto Bagnara, Patricia M. Hill, and Enea Zaffanella. <i>The Parma Polyhedra Library Java Language Interface User&#8217;s Manual (version 0.11.2),</i> available (in several formats) at <code><a rel="nofollow" href="http://www.cs.unipr.it/ppl/">http://www.cs.unipr.it/ppl/</a></code> . </p>
<p> Roberto Bagnara, Patricia M. Hill, and Enea Zaffanella. <i>The Parma Polyhedra Library OCaml Language Interface User&#8217;s Manual (version 0.11.2),</i> available (in several formats) at <code><a rel="nofollow" href="http://www.cs.unipr.it/ppl/">http://www.cs.unipr.it/ppl/</a></code> . </p>
<p> Roberto Bagnara, Patricia M. Hill, and Enea Zaffanella. <i>The Parma Polyhedra Library Prolog Language Interface User&#8217;s Manual (version 0.11.2),</i> available (in several formats) at <code><a rel="nofollow" href="http://www.cs.unipr.it/ppl/">http://www.cs.unipr.it/ppl/</a></code> . </p>
<h2>Index</h2>
