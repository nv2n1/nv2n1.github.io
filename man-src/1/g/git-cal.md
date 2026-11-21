---

title: "git-cal(1)"
name: "git-cal"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cal/"
description: "git-cal – A simple tool to view commits calendar (similar to github contributions calendar) on command line"
---

<p> &#8220;git-cal&#8221; is a tool to visualize the git commit history in github&#8217;s contribution calendar style. The calendar shows how frequently the commits are made over the past year or some choosen period Activity can be displayed using ascii, ansi or unicode characters, default is choosen based on <font SIZE="-1">ENV</font> </p>
<pre><code>
git - cal git - cal-- period = &lt;1..12, -1.. - 11&gt;
                                   git - cal-- author = &lt;author&gt; --&lt;filepath&gt;
                                                            git - cal-- ascii git - cal-- ansi git - cal-- unicode
</code></pre>
<h3><font SIZE="-1">OPTIONS</font></h3>
<dl>
<dt>&#8211;ansi</dt>
<dd> Display activity using <font SIZE="-1">ANSI</font> colors</dd>
<dt>&#8211;ascii</dt>
<dd> Display activity using <font SIZE="-1">ASCII</font> characters instead of <font SIZE="-1">ANSI</font> colors.</dd>
<dt>&#8211;author=&lt;author&gt;</dt>
<dd> View commits of a particular author.</dd>
<dt>&#8211;period|p=&lt;n&gt;</dt>
<dd> Do not show the entire year:</dd>
<dt>&#8211;unicode</dt>
<dd> Display activity using unicode characters</dd>
<dl>
<dl>
<dt>n = 1 to 12</dt>
<dd> Shows only one month (1=Jan .. 12=Dec)</dd>
<dt>n = -1 to -11</dt>
<dd> Shows the last n months (and the current month)</dd>
<dt>&#8211;help|?</dt>
<dd> Print this message.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h3><font SIZE="-1">ADDITIONAL OPTIONS</font></h3>
<pre>
  -- filename to view the logs of a particular file or directory
</pre>
<h2>AUTHOR</h2>
<p> Karthik katooru &lt;karthikkatooru [at] gmail.com&gt;</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the <font SIZE="-1">MIT</font> License</p>
<h2>POD ERRORS</h2>
<p> Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 451:</dt>
<dd> You forgot a &#8216;=back&#8217; before &#8216;=head2&#8217; </dd>
</dl>
