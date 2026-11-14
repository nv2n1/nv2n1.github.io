---
title: "text2html(1)"
name: "text2html"
section: "1"
letter: "t"
url: "/docs/linux/man/1-text2html/"
description: "text2html – convert plain text to HTML"
---

<h2 class="name">NAME</h2>
<p> text2html &#8211; convert plain text to HTML </p>
<h2>VERSION</h2>
<p> version 2.07</p>
<h2>SYNOPSIS</h2>
<p> <code>text2html [options&#8230;]</code> [file &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <tt>&quot;text2html&quot;</tt> utility converts text to <font SIZE="-1">HTML.</font> Text can come from standard input or files listed on the command line. </p>
<p> The available options are outlined in HTML::FromText. The option syntax is slightly different. Options are prefixed with two dashes (<tt>&quot;--&quot;</tt>) and may have an option value following an equals sign (<tt>&quot;=&quot;</tt>). The default value is on (&lt;1&gt;).</p>
<h2>EXAMPLES</h2>
<p> Convert the <tt>&quot;README&quot;</tt> file using <tt>&quot;paras&quot;</tt> and <tt>&quot;blockcode&quot;</tt>. </p>
<pre>
  text2html --paras --blockcode README
</pre>
<p> Convert a file called <tt>&quot;--stupid-name&quot;</tt>. </p>
<pre>
  text2html --paras -- --stupid-name
</pre>
<p> Convert text on standard input. </p>
<pre><code>
text2html-- paras-- urls-- email-- bold-- underline
</code></pre>
<p> Convert text on standard input but turn off <tt>&quot;metachars&quot;</tt>. </p>
<pre>
  text2html --metachars=0 --lines
</pre>
<h2>DIAGNOSTICS</h2>
<p> The <tt>&quot;text2html&quot;</tt> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i><a href="/docs/linux/man/3-html--fromtext/">HTML::FromText</a></i>(3).</p>
<h2>AUTHORS</h2>
<dl>
<dt>&bull;</p>
<dd> Ricardo <font SIZE="-1">SIGNES</font> &lt;rjbs [at] cpan.org&gt;</p>
<dt>&bull;</p>
<dd> Casey West &lt;casey [at] geeknest.com&gt;</p>
<dt>&bull;</p>
<dd> Gareth Rees &lt;garethr [at] cre.canon.co.uk&gt;</dl>
<h2>COPYRIGHT AND LICENSE</h2>
<p> This software is copyright (c) 2003 by Casey West. </p>
<p> This is free software; you can redistribute it and/or modify it under the same terms as the Perl 5 programming language system itself. </p>
<h2>Index</h2>
