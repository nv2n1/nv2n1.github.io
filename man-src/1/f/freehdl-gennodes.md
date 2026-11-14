---
title: "freehdl-gennodes(1)"
name: "freehdl-gennodes"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freehdl-gennodes/"
description: "FreeHDL-GENNODES – Abstract syntax tree generator used by the VHDL compiler/simulator FreeHDL."
---

<h2>NAME</h2>
<p> FreeHDL-GENNODES &#8211; Abstract syntax tree generator used by the VHDL compiler/simulator FreeHDL.</p>
<h2>SYNOPSIS</h2>
<p> <code>freehdl-gennodes</code> CMD CHUNK IN-FILE OUT-FILE</p>
<h2>DESCRIPTION</h2>
<p> <code>FreeHDL-GENNODES</code> is an extensible framework for representing an abstract syntax tree. The program reads the IN-FILE and generates output for CHUNK in OUT-FILE, according to CMD. </p>
<p> When CMD is `header&#8217;, FreeHDL-GENNODES writes a header file to OUT-FILE that should be included by the users of the CHUNK. When it is `impl&#8217;, it writes the implementation of CHUNK.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-freehdl-v2cc/">freehdl-v2cc</a>(1), <a href="/docs/linux/man/1-freehdl-config/">freehdl-config</a>(1), <a href="/docs/linux/man/5-v2cc-libs/">v2cc.libs</a>(5)</p>
<h2>AVAILABILITY</h2>
<p> The latest version of FreeHDL can always be obtained from <code><a rel="nofollow" href="http://www.freehdl.seul.org">www.freehdl.seul.org</a></code></p>
<h2>REPORTING BUGS</h2>
<p> Known bugs are documented within the BUGS file. If your report addresses a parser related topic then contact Marius Vollmer &lt;mvo [at] zagadka.ping.de&gt;. If it is related to the code generator or compiler then send an email to Edwin Naroska &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt;. If your are not sure send it to Edwin. He will take care of forwarding your report to the appropriate recipient.</p>
<h2>COPYRIGHT</h2>
<p> Marius Vollmer &#169; 1998, 1999, 2000, 2001 &lt;mvo [at] zagadka.ping.de&gt; </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>AUTHORS</h2>
<p> Written by Marius Vollmer &lt;mvo [at] zagadka.ping.de&gt; and Edwin Naroska &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt;. </p>
<h2>Index</h2>
