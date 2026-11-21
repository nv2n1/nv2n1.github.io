---

title: "echo(1)"
name: "echo"
section: "1"
letter: "e"
url: "/docs/linux/man/1-echo/"
description: "echo – display a line of text"
---

<p> <code>echo</code> [<i>,SHORT-OPTION/</i>]... [<i>,STRING/</i>]... <br />
 <code>echo</code> <i>,LONG-OPTION/</i>  </p>
<p> Echo the STRING(s) to standard output. </p>
<dl>
<dt><code>-n</code></dt>
<dd> <p> do not output the trailing newline </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> enable interpretation of backslash escapes </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> disable interpretation of backslash escapes (default) </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> display this help and exit </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> output version information and exit </p>
 </dd></dl>
<p> If <code>-e</code> is in effect, the following sequences are recognized: </p>
<dl>
<dt>\\</dt>
<dd> <p> backslash </p>
 </dd>
<dt>\a</dt>
<dd> <p> alert (BEL) </p>
 </dd>
<dt>\b</dt>
<dd> <p> backspace </p>
 </dd>
<dt>\c</dt>
<dd> <p> produce no further output </p>
 </dd>
<dt>\e</dt>
<dd> <p> escape </p>
 </dd>
<dt>\f</dt>
<dd> <p> form feed </p>
 </dd>
<dt>\n</dt>
<dd> <p> new line </p>
 </dd>
<dt>\r</dt>
<dd> <p> carriage return </p>
 </dd>
<dt>\t</dt>
<dd> <p> horizontal tab </p>
 </dd>
<dt>\v</dt>
<dd> <p> vertical tab </p>
 </dd>
<dt>\0NNN</dt>
<dd> <p> byte with octal value NNN (1 to 3 digits) </p>
 </dd>
<dt>\xHH</dt>
<dd> <p> byte with hexadecimal value HH (1 to 2 digits) </p>
 </dd></dl>
<p> NOTE: your shell may have its own version of echo, which usually supersedes the version described here. Please refer to your shell&#8217;s documentation for details about the options it supports.  </p>
<h2>AUTHOR</h2>
<p> Written by Brian Fox and Chet Ramey.  </p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt; <br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;  </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;. <br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.  </p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/echo">https://www.gnu.org/software/coreutils/echo</a>&gt; <br />
 or available locally via: info &#8216;(coreutils) echo invocation&#8217; </p>
