---
title: "eutp(1)"
name: "eutp"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eutp/"
description: "eutp – EuroBraille file transferring"
---

<h2 class="name">NAME</h2>
<p> eutp &#8211; EuroBraille file transferring </p>
<h2>SYNOPSIS</h2>
<p> eutp</p>
<h2>DESCRIPTION</h2>
<p> <i>eutp</i> lets you exchange files with a Clio terminal from EuroBraile. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> None so far </p>
<h2>RETURNED VALUE</h2>
<table>
<tr VALIGN=top>
<td><code>1</code></td>
<td>error
</td>
</tr>
</table>
<h2>SHELL EXPANSIONS</h2>
<p> Beware of special chars: * and . are often expanded by your shell, hence <i>sending files *</i> will probably do what you want, putting every file existing in the current directory onto the terminal, but <i> receiving files *</i> may not do what you want: it will only get every file which already exist in the current directory, skipping those you just created on your terminal ! If you want to get every file which exist in the terminal, you should use <i>&#8216;*&#8217;</i> or something similar (please read your shell manual). </p>
<p> The same warning applies to other special chars, such as $, ~, &amp;,&#8230; which should be protected by surrounding arguments by quotes (&#8216;) or by using single backslashes (\) just before them (please read your shell manual). </p>
<h2>AUTHOR</h2>
<p> Olivier Bert &lt;olivier.bert [at] laposte.net&gt; </p>
<h2>Index</h2>
