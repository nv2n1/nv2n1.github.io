---
title: "lexgrog(1)"
name: "lexgrog"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lexgrog/"
description: "lexgrog – parse header information in man pages"
---

<h2 class="name">NAME</h2>
<p> lexgrog &#8211; parse header information in man pages </p>
<h2>SYNOPSIS</h2>
<p> <code>lexgrog</code> [<code>-m</code>|<code>-c</code>] [<code>-dfw?V</code>] [<code>-E</code> <i>encoding</i>] <i>file</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>lexgrog</code> is an implementation of the traditional &#8220;groff guess&#8221; utility in <code>lex</code>. It reads the list of files on its command line as either man page source files or preformatted &#8220;cat&#8221; pages, and displays their name and description as used by <code>apropos</code> and <code>whatis</code>, the list of preprocessing filters required by the man page before it is passed to <code>nroff</code> or <code>troff</code>, or both. </p>
<p> If its input is badly formatted, <code>lexgrog</code> will print &#8220;parse failed&#8221;; this may be useful for external programs that need to check man pages for correctness. If one of <code>lexgrog</code>&#8216;s input files is &#8220;-&#8220;, it will read from standard input; if any input file is compressed, a decompressed version will be read automatically.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debugging information.</p>
<dt><code>-m</code>, <code>&#8211;man</code></p>
<dd> Parse input as man page source files. This is the default if neither <code>&#8211;man</code> nor <code>&#8211;cat</code> is given.</p>
<dt><code>-c</code>, <code>&#8211;cat</code></p>
<dd> Parse input as preformatted man pages (&#8220;cat pages&#8221;). <code>&#8211;man</code> and <code>&#8211;cat</code> may not be given simultaneously.</p>
<dt><code>-w</code>, <code>&#8211;whatis</code></p>
<dd> Display the name and description from the man page&#8217;s header, as used by <code>apropos</code> and <code>whatis</code>. This is the default if neither <code>&#8211;whatis</code> nor <code>&#8211;filters</code> is given.</p>
<dt><code>-f</code>, <code>&#8211;filters</code></p>
<dd> Display the list of filters needed to preprocess the man page before formatting with <code>nroff</code> or <code>troff</code>.</p>
<dt><code>-E</code> <i>encoding</i>, <code>&#8211;encoding</code> <i>encoding</i></p>
<dd> Override the guessed character set for the page to <i>encoding</i>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Successful program execution.</p>
<dt><code>1</code></p>
<dd> Usage error.</p>
<dt><code>2</code></p>
<dd> <code>lexgrog</code> failed to parse one or more of its input files.</dl>
<h2>EXAMPLES</h2>
<pre>
  $ lexgrog man.1
  man.1: &quot;man - an interface to the system reference manuals&quot;
  $ lexgrog -fw man.1
  man.1 (t): &quot;man - an interface to the system reference manuals&quot;
  $ lexgrog -c whatis.cat1
  whatis.cat1: &quot;whatis - display manual page descriptions&quot;
  $ lexgrog broken.1
  broken.1: parse failed
</pre>
<h2>WHATIS PARSING</h2>
<p> <code>mandb</code> (which uses the same code as <code>lexgrog</code>) parses the <code>NAME</code> section at the top of each manual page looking for names and descriptions of the features documented in each. While the parser is quite tolerant, as it has to cope with a number of different forms that have historically been used, it may sometimes fail to extract the required information. </p>
<p> When using the traditional <i>man</i> macro set, a correct <code>NAME</code> section looks something like this: </p>
<dl>
<dt>
<dd>
<pre>
.SH NAME
foo \- program to do something
</pre>
</dl>
<p> Some manual pagers require the &#8216;\-&#8216; to be exactly as shown; <code>mandb</code> is more tolerant, but for compatibility with other systems it is nevertheless a good idea to retain the backslash. </p>
<p> On the left-hand side, there may be several names, separated by commas. Names containing whitespace will be ignored to avoid pathological behaviour on certain ill-formed <code>NAME</code> sections. The text on the right-hand side is free-form, and may be spread over multiple lines. If several features with different descriptions are being documented in the same manual page, the following form is therefore used: </p>
<dl>
<dt>
<dd>
<pre>
.SH NAME
foo, bar \- programs to do something
.br
baz \- program to do nothing
</pre>
</dl>
<p> (A macro which starts a new paragraph, like <tt>.PP</tt>, may be used instead of the break macro <tt>.br</tt>.) </p>
<p> When using the BSD-derived <i>mdoc</i> macro set, a correct <code>NAME</code> section looks something like this: </p>
<dl>
<dt>
<dd>
<pre>
.Sh NAME
.Nm foo
.Nd program to do something
</pre>
</dl>
<p> There are several common reasons why whatis parsing fails. Sometimes authors of manual pages replace &#8216;.SH NAME&#8217; with &#8216;.SH MYPROGRAM&#8217;, and then <code>mandb</code> cannot find the section from which to extract the information it needs. Sometimes authors include a NAME section, but place free-form text there rather than &#8216;name \- description&#8217;. However, any syntax resembling the above should be accepted.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-apropos/">apropos</a></i>(1), <i><a href="/docs/linux/man/1-man/">man</a></i>(1), <i><a href="/docs/linux/man/1-whatis/">whatis</a></i>(1), <i><a href="/docs/linux/man/8-mandb/">mandb</a></i>(8)</p>
<h2>NOTES</h2>
<p> <code>lexgrog</code> attempts to parse files containing .so requests, but will only be able to do so correctly if the files are properly installed in a manual page hierarchy.</p>
<h2>AUTHOR</h2>
<p> The code used by <code>lexgrog</code> to scan man pages was written by: </p>
<pre><code>
Wilf.(G.Wilford[at] ee.surrey.ac.uk).Fabrizio Polacco(fpolacco[at] debian.org).Colin Watson(cjwatson[at] debian.org).
</code></pre>
<p> Colin Watson wrote the current incarnation of the command-line front-end, as well as this man page.</p>
<h2>BUGS</h2>
<p> <a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
<h2>Index</h2>
