---
title: "debconf-set-selections(1)"
name: "debconf-set-selections"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-set-selections/"
description: "debconf-set-selections – insert new values into the debconf database"
---

<h2 class="name">NAME</h2>
<p> debconf-set-selections &#8211; insert new values into the debconf database </p>
<h2>SYNOPSIS</h2>
<pre>
 debconf-set-selections file
 debconf-get-selections | ssh newhost debconf-set-selections
</pre>
<h2>DESCRIPTION</h2>
<p> <code>debconf-set-selections</code> can be used to pre-seed the debconf database with answers, or to change answers in the database. Each question will be marked as seen to prevent debconf from asking the question interactively. </p>
<p> Reads from a file if a filename is given, otherwise from stdin.</p>
<h2>WARNING</h2>
<p> Only use this command to seed debconf values for packages that will be or are installed. Otherwise you can end up with values in the database for uninstalled packages that will not go away, or with worse problems involving shared values. It is recommended that this only be used to seed the database if the originating machine has an identical install.</p>
<h2>DATA FORMAT</h2>
<p> The data is a series of lines. Lines beginning with a # character are comments. Blank lines are ignored. All other lines set the value of one question, and should contain four values, each separated by one character of whitespace. The first value is the name of the package that owns the question. The second is the name of the question, the third value is the type of this question, and the fourth value (through the end of the line) is the value to use for the answer of the question. </p>
<p> Alternatively, the third value can be &#8220;seen&#8221;; then the preseed line only controls whether the question is marked as seen in debconf&#8217;s database. Note that preseeding a question&#8217;s value defaults to marking that question as seen, so to override the default value without marking a question seen, you need two lines. </p>
<p> Lines can be continued to the next line by ending them with a &#8220;\&#8221; character.</p>
<h2>EXAMPLES</h2>
<pre>
 # Force debconf priority to critical.
 debconf debconf/priority select critical
 # Override default frontend to readline, but allow user to select.
 debconf debconf/frontend select readline
 debconf debconf/frontend seen false
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;verbose</code>, <code>-v</code></p>
<dd> verbose output</p>
<dt><code>&#8211;checkonly</code>, <code>-c</code></p>
<dd> only check the input file format, do not save changes to database</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-debconf-get-selections/">debconf-get-selections</a></code>(1) (available in the debconf-utils package)</p>
<h2>AUTHOR</h2>
<p> Petter Reinholdtsen &lt;pere [at] hungry.com&gt; </p>
<h2>Index</h2>
