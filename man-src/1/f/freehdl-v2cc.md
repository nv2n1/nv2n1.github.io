---

title: "freehdl-v2cc(1)"
name: "freehdl-v2cc"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freehdl-v2cc/"
description: "FreeHDL-V2CC – A VHDL to C++ converter."
---

<h2>NAME</h2>
<p> FreeHDL-V2CC &#8211; A VHDL to C++ converter.</p>
<p> <code>freehdl-v2cc</code> [<i>OPTION</i>] &#8230; [<i>FILE</i>] &#8230;</p>
<p> <code>FreeHDL</code> is a parser/compiler/simulator suite for the hardware description language VHDL. VHDL&#8217;93 as well as VHDL&#8217;87 files are supported. </p>
<p> <code>FreeHDL-V2CC</code> translates the original VHDL source FILEs into C++. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> FILE</dt>
<dd> Write C++ generated code to FILE.</dd>
<dt><code>-n</code></dt>
<dd> Dry run.</dd>
<dt><code>-R</code></dt>
<dd> Emit register code.</dd>
<dt><code>-v</code></dt>
<dd> Enable verbosity.</dd>
<dt><code>-g</code></dt>
<dd> Emit debugging code.</dd>
<dt><code>-D</code></dt>
<dd> Emit CDFG code.</dd>
<dt><code>-l</code> LIBNAME</dt>
<dd> Use LIBNAME as the WORK library, default is the &quot;.&quot; library directory.</dd>
<dt><code>&#8211;relaxed-component-visibility</code></dt>
<dd> Allows invisible default bindings from <i>WORK</i>.</dd>
<dt><code>&#8211;depend</code> FILE</dt>
<dd> Write dependency information to FILE.</dd>
<dt><code>-m</code> FILE</dt>
<dd> Emit the main() file C++ code to FILE.</dd>
<dt><code>-L</code> VHDLLIB</dt>
<dd> Path to VHDL library root directory. Within this directory the compiler search for a file named <i>v2cc.libs</i>. The mapping file <i>v2cc.libs</i> translates library unit names to directories. Note that more than one VHDLLIB may be provided.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>V2CC_LIBRARY_PATH</dt>
<dd> The variable V2CC_LIBRARY_PATH consists of &quot;:&quot; separated filenames. In addition to the environment variable, you can use the &quot;-L libdir&quot; command line option with v2cc. The directories specified with &quot;-L&quot; are added in front of the ones specified by V2CC_LIBRARY_PATH. In the final library path, they appear in the same order as on the command line.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gvhdl/">gvhdl</a>(1), <a href="/docs/linux/man/1-freehdl-config/">freehdl-config</a>(1), v2cc.libs(5)</p>
<h2>AVAILABILITY</h2>
<p> The latest version of FreeHDL can always be obtained from <code><a rel="nofollow" href="http://www.freehdl.seul.org">www.freehdl.seul.org</a></code></p>
<h2>REPORTING BUGS</h2>
<p> Known bugs are documented within the BUGS file. If your report addresses a parser related topic then contact Marius Vollmer &lt;mvo [at] zagadka.ping.de&gt;. If it is related to the code generator or compiler then send an email to Edwin Naroska &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt;. If your are not sure send it to Edwin. He will take care of forwarding your report to the appropriate recipient.</p>
<h2>COPYRIGHT</h2>
<p> Edwin Naroska &#169; 1999, 2000, 2001, 2002, 2003, 2004, 2005 &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt; </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>AUTHORS</h2>
<p> Written by Marius Vollmer &lt;mvo [at] zagadka.ping.de&gt; and Edwin Naroska &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt;. </p>
