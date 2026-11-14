---
title: "expr(1)"
name: "expr"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expr/"
description: "expr – evaluate expressions"
---

<h2 class="name">NAME</h2>
<p> expr &#8211; evaluate expressions </p>
<h2>SYNOPSIS</h2>
<p> <code>expr</code> <i>,EXPRESSION/</i><br />
 <code>expr</code> <i>,OPTION/</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Print the value of EXPRESSION to standard output. A blank line below separates increasing precedence groups. EXPRESSION may be:</p>
<dl>
<dt>ARG1 | ARG2</p>
<dd> ARG1 if it is neither null nor 0, otherwise ARG2</p>
<dt>ARG1 &amp; ARG2</p>
<dd> ARG1 if neither argument is null or 0, otherwise 0</p>
<dt>ARG1 &lt; ARG2</p>
<dd> ARG1 is less than ARG2</p>
<dt>ARG1 &lt;= ARG2</p>
<dd> ARG1 is less than or equal to ARG2</p>
<dt>ARG1 = ARG2</p>
<dd> ARG1 is equal to ARG2</p>
<dt>ARG1 != ARG2</p>
<dd> ARG1 is unequal to ARG2</p>
<dt>ARG1 &gt;= ARG2</p>
<dd> ARG1 is greater than or equal to ARG2</p>
<dt>ARG1 &gt; ARG2</p>
<dd> ARG1 is greater than ARG2</p>
<dt>ARG1 + ARG2</p>
<dd> arithmetic sum of ARG1 and ARG2</p>
<dt>ARG1 &#8211; ARG2</p>
<dd> arithmetic difference of ARG1 and ARG2</p>
<dt>ARG1 * ARG2</p>
<dd> arithmetic product of ARG1 and ARG2</p>
<dt>ARG1 / ARG2</p>
<dd> arithmetic quotient of ARG1 divided by ARG2</p>
<dt>ARG1 % ARG2</p>
<dd> arithmetic remainder of ARG1 divided by ARG2</p>
<dt>STRING : REGEXP</p>
<dd> anchored pattern match of REGEXP in STRING</p>
<dt>match STRING REGEXP</p>
<dd> same as STRING : REGEXP</p>
<dt>substr STRING POS LENGTH</p>
<dd> substring of STRING, POS counted from 1</p>
<dt>index STRING CHARS</p>
<dd> index in STRING where any CHARS is found, or 0</p>
<dt>length STRING</p>
<dd> length of STRING</p>
<dt>+ TOKEN</p>
<dd> interpret TOKEN as a string, even if it is a</p>
<dt>
<dd> keyword like &#8216;match&#8217; or an operator like &#8216;/&#8217;</p>
<dt>( EXPRESSION )</p>
<dd> value of EXPRESSION</dl>
<p> Beware that many operators need to be escaped or quoted for shells. Comparisons are arithmetic if both ARGs are numbers, else lexicographical. Pattern matches return the string matched between \( and \) or null; if \( and \) are not used, they return the number of characters matched or 0. </p>
<p> Exit status is 0 if EXPRESSION is neither null nor 0, 1 if EXPRESSION is null or 0, 2 if EXPRESSION is syntactically invalid, and 3 if an error occurred.</p>
<h2>AUTHOR</h2>
<p> Written by Mike Parker, James Youngman, and Paul Eggert.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/expr">https://www.gnu.org/software/coreutils/expr</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) expr invocation&#8217; </p>
<h2>Index</h2>
