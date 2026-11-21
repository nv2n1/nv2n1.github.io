---

title: "gendesc(1)"
name: "gendesc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gendesc/"
description: "gendesc – Generate a test case description file"
---

<h2>NAME</h2>
<p> gendesc &#8211; Generate a test case description file</p>
<p> <code>gendesc</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>|<code>&#8211;version</code>]</p>
<dl>
<dt>
</dt><dd>
 [<code>-o</code>|<code>&#8211;output-filename</code> <i>filename</i>]<br />
 <i>inputfile</i></dd></dl>
<p> Convert plain text test case descriptions into a format as understood by <code>genhtml</code>. <i>inputfile</i> needs to observe the following format: </p>
<p> For each test case:</p>
<dl>
<dt> &#8211;</dt>
<dd> one line containing the test case name beginning at the start of the line</dd>
<dt> &#8211;</dt>
<dd> one or more lines containing the test case description indented with at least one whitespace character (tab or space) </dd>
<p> <code>Example input file:</code> </p>
<p> test01</p>
<dl>
<dt>
</dt><dd> An example test case description.<br />
 Description continued</dd></dl>
<p> test42</p>
<dl>
<dt>
</dt><dd> Supposedly the answer to most of your questions</dd></dl>
<p> Note: valid test names can consist of letters, decimal digits and the underscore character (&#8216;_&#8217;).</dl>
<h2>OPTIONS</h2>
<p> <code>-h</code><br />
 <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Print a short help text, then exit.</dd></dl>
<p> <code>-v</code><br />
 <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print version number, then exit.</dd></dl>
<p> <code>-o </code><i>filename</i><br />
 <code>&#8211;output-filename </code><i>filename</i></p>
<dl>
<dt>
</dt><dd> Write description data to <i>filename</i>. </dd>
<p> By default, output is written to STDOUT.</dl>
<h2>AUTHOR</h2>
<p> Peter Oberparleiter &lt;Peter.Oberparleiter [at] de.ibm.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lcov/">lcov</a></code>(1), <code><a href="/docs/linux/man/1-genhtml/">genhtml</a></code>(1), <code><a href="/docs/linux/man/1-geninfo/">geninfo</a></code>(1), <code><a href="/docs/linux/man/1-genpng/">genpng</a></code>(1), <code><a href="/docs/linux/man/1-gcov/">gcov</a></code>(1) </p>
