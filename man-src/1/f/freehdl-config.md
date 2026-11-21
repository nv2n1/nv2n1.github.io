---

title: "freehdl-config(1)"
name: "freehdl-config"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freehdl-config/"
description: "FreeHDL-CONFIG – The FreeHDL configuration script."
---

<p> FreeHDL-CONFIG &#8211; The FreeHDL configuration script.</p>
<h2>SYNOPSIS</h2>
<p> <code>freehdl-config</code> [<i>OPTION</i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>FreeHDL</code> is a parser/compiler/simulator suite for the hardware description language VHDL. VHDL&#8217;93 as well as VHDL&#8217;87 files are supported. </p>
<p> <code>FreeHDL-CONFIG</code> can be used to obtain the installation (path) configuration of the FreeHDL package.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v, &#8211;version</code></dt>
<dd> show installed FreeHDL version</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> show usage info</dd>
<dt><code>-l, &#8211;ldflags</code></dt>
<dd> print libraries to link with</dd>
<dt><code>-libs, &#8211;libtool</code></dt>
<dd> print libtool libraries to link with</dd>
<dt><code>-ieee, &#8211;ieee</code></dt>
<dd> print IEEE libtool libraries to link with</dd>
<dt><code>-c, &#8211;cxxflags</code></dt>
<dd> print C++ compiler flags to compile with</dd>
<dt><code>-cxx, &#8211;cxx</code></dt>
<dd> print C++ compiler <code>-linker, &#8211;linker</code> print libtool linker</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gvhdl/">gvhdl</a>(1), <a href="/docs/linux/man/1-freehdl-v2cc/">freehdl-v2cc</a>(1), v2cc.libs(5)</p>
<h2>AVAILABILITY</h2>
<p> The latest version of FreeHDL can always be obtained from <code><a rel="nofollow" href="http://www.freehdl.seul.org">www.freehdl.seul.org</a></code></p>
<h2>REPORTING BUGS</h2>
<p> Known bugs are documented within the BUGS file. If your report addresses a parser related topic then contact Marius Vollmer &lt;mvo [at] zagadka.ping.de&gt;. If it is related to the code generator or compiler then send an email to Edwin Naroska &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt;. If your are not sure send it to Edwin. He will take care of forwarding your report to the appropriate recipient.</p>
<h2>COPYRIGHT</h2>
<p> Stefan Jahn &#169; 2006 &lt;stefan [at] lkcc.org&gt; </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>AUTHORS</h2>
<p> Written by Stefan Jahn &lt;stefan [at] lkcc.org&gt;. </p>
