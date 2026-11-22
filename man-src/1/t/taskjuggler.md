---

title: "taskjuggler(1)"
name: "taskjuggler"
section: "1"
letter: "t"
url: "/docs/linux/man/1-taskjuggler/"
description: "_______taskjuggler ____ – translates project descriptions into HTML or XML reports"
---

<p> _______taskjuggler ____ &#8211; translates project descriptions into HTML or XML reports </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code><br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>taskjuggler<br/>
</code>&nbsp;<wbr>[<code>&nbsp;<wbr></code><i>&nbsp;<wbr>options&nbsp;<wbr></i><code>&nbsp;<wbr></code>]&nbsp;<wbr>[<code>&nbsp;<wbr></code><i>&nbsp;<wbr></i><i>&nbsp;<wbr>&lt;filename1&gt;&nbsp;<wbr></i><i>&nbsp;<wbr></i><code>&nbsp;<wbr></code>]&nbsp;<wbr>[<code>&nbsp;<wbr></code><i>&nbsp;<wbr></i><i>&nbsp;<wbr>&lt;filename2&gt;&nbsp;<wbr>&#8230;&nbsp;<wbr></i><i>&nbsp;<wbr></i><code>&nbsp;<wbr></code>]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code> taskjuggler </code></p>
<dd>must be called with at least one file that contains the project description and the report definitions. </dd>
<h2>OPTIONS</h2>
<p> <code> -h </code> <code> &#8211;help </code></p>
<dl>
<dt>
</dt><dd> Show summary of options.</dd></dl>
<p> <code> -v </code> <code> &#8211;version </code></p>
<dl>
<dt>
</dt><dd> Show version and copyright of program</dd></dl>
<p> <code> -s </code></p>
<dl>
<dt>
</dt><dd> stop after syntax check</dd></dl>
<p> <code> -M </code></p>
<dl>
<dt>
</dt><dd> output include dependencies for make utilities</dd></dl>
<p> <code> &#8211;makefile </code><code> &lt;file&gt; </code></p>
<dl>
<dt>
</dt><dd> generate include dependencies for make utilities into the specified file</dd></dl>
<p> <code> &#8211;maxerrors N </code></p>
<dl>
<dt>
</dt><dd> stop after N errors. If N is 0 show all errors</dd></dl>
<p> <code> &#8211;nodepcheck </code></p>
<dl>
<dt>
</dt><dd> don&#8217;t search for dependency loops</dd></dl>
<p> <code> &#8211;debug N </code></p>
<dl>
<dt>
</dt><dd> print debug output, N must be between 0 and 40, the higher N the more output is printed</dd></dl>
<p> <code> &#8211;dbmode N </code></p>
<dl>
<dt>
</dt><dd> activate debug mode only for certain parts of the code</dd></dl>
<h2>SEE ALSO</h2>
<p> /usr/share/doc/taskjuggler/index.html , <a href="/docs/linux/man/1-taskjugglerui/">TaskjugglerUI</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Fathi Boudra &lt; &lt;fboudra [at] free.fr&gt; &gt; based on the output of taskjuggler &#8211;help for the Debian(TM) system (but may be used by others). </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL .</p>
<h2>AUTHOR</h2>
<p> <code>fathi Boudra</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006 Fathi Boudra </p>
