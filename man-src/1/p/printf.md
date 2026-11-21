---
title: "printf(1)"
name: "printf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-printf/"
description: "printf – format and print data"
---
<h2 class="name">NAME</h2>
<p> printf - format and print data </p>
<h2>SYNOPSIS</h2>
<p> <code>printf</code> <i>,FORMAT /</i>[<i>,ARGUMENT/</i>]... <br />
 <code>printf</code> <i>,OPTION/</i>  </p>
<h2>DESCRIPTION</h2>
<p> Print ARGUMENT(s) according to FORMAT, or execute according to OPTION: </p>
<dl>
<dt><code>--help</code></dt>
<dd> <p> display this help and exit </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> output version information and exit </p>
 </dd></dl>
<p> FORMAT controls the output as in C printf. Interpreted sequences are: </p>
<dl>
<dt>\&quot;</dt>
<dd> <p> double quote </p>
 </dd>
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
<dt>\NNN</dt>
<dd> <p> byte with octal value NNN (1 to 3 digits) </p>
 </dd>
<dt>\xHH</dt>
<dd> <p> byte with hexadecimal value HH (1 to 2 digits) </p>
 </dd>
<dt>\uHHHH</dt>
<dd> <p> Unicode (ISO/IEC 10646) character with hex value HHHH (4 digits) </p>
 </dd>
<dt>\UHHHHHHHH</dt>
<dd> <p> Unicode character with hex value HHHHHHHH (8 digits) </p>
 </dd>
<dt>%%</dt>
<dd> <p> a single % </p>
 </dd>
<dt>%b</dt>
<dd> <p> ARGUMENT as a string with &#8216;\&#8216; escapes interpreted, except that octal escapes are of the form \0 or \0NNN </p>
 </dd>
<dt>%q</dt>
<dd> <p> ARGUMENT is printed in a format that can be reused as shell input, escaping non-printable characters with the proposed POSIX $&#8216;&#8216; syntax. </p>
 </dd></dl>
<p> and all C format specifications ending with one of diouxXfeEgGcs, with ARGUMENTs converted to proper type first. Variable widths are handled. </p>
<p> NOTE: your shell may have its own version of printf, which usually supersedes the version described here. Please refer to your shell&#8217;s documentation for details about the options it supports.  </p>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.  </p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt; <br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;  </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;. <br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-printf/">printf</a>(3) </p>
<p> <br />
 Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/printf">https://www.gnu.org/software/coreutils/printf</a>&gt; <br />
 or available locally via: info &#8216;(coreutils) printf invocation&#8217; </p>
