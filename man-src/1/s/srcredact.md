---
title: "srcredact(1)"
name: "srcredact"
section: "1"
letter: "s"
url: "/docs/linux/man/1-srcredact/"
description: "srcredact – a program for redaction of text files"
---

<h2 class="name">NAME</h2>
<p> srcredact &#8211; a program for redaction of text files </p>
<h2>SYNOPSIS</h2>
<p> srcredact [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <code>-e</code> <i>audience</i> [<i>full_file</i>] </p>
<p> srcredact [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <code>-u</code> <i>audience</i> <i>full_file</i> [<i>redacted_file</i>] </p>
<p> srcredact <code>-l</code> [<i>full_file</i>] </p>
<p> srcredact <code>-h|-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>srcredact</code> is the program to extract &#8220;redacted versions&#8221; of the master file (option <code>-e</code>) or to incorporate the changes in the redacted versions into the master file (&#8220;unredact&#8221;, option <code>-u</code>). </p>
<p> The master file consists of <i>chunks</i> intended for different audiences. Each audience has a <i>name</i>, e.g. <tt>&quot;classified&quot;</tt>, <tt>&quot;unclssified&quot;</tt>, <tt>&quot;expert&quot;</tt> etc. Chunks are started and stopped by <i>guard lines</i>. Each guard line has the format (for the default TeX syntax) </p>
<pre>
  %&lt;*name1|name2|...&gt;
</pre>
<p> or </p>
<pre>
  %&lt;/name1|name2|...&gt;
</pre>
<p> In the first cases the text following the guard is <i>included</i> for the audiences <tt>&quot;name1&quot;</tt>, <tt>&quot;name2&quot;</tt>, &#8230;. In the second case it is <i>excluded</i> for these audiences. </p>
<p> THere is a special audience <tt>&quot;ALL&quot;</tt>: a wild card for all audiences. Thus the idiom </p>
<pre>
  %&lt;/ALL&gt;
  %&lt;*classified&gt;
</pre>
<p> means that the chunk is excluded for all audiences but <tt>&quot;classified&quot;</tt> </p>
<p> Exactly one of the options <code>-e</code> (extract) or <code>-u</code> (unextract) must be present. In the extract mode the non-option argument is the name of the full file. If it is absent, or is <tt>&quot;-&quot;</tt>, standard input is used. In the unextract mode the first non-option argument</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>list of comment patterns</i></p>
<dd> Use the given pattern for comment lines to search for guards instead of the default <tt>&quot;TeX&quot;</tt> pattern. The recognized patterns are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c</code></p>
<dd>
<pre>
  /*&lt;guard&gt;*/
</pre>
<dt><code>cpp</code></p>
<dd>
<pre>
  //&lt;guard&gt;
</pre>
<dt><code>fortran</code></p>
<dd>
<pre>
  C&lt;guard&gt;
</pre>
<dt><code>shell</code></p>
<dd>
<pre>
  #&lt;guard&gt;
</pre>
<dt><code>TeX</code></p>
<dd>
<pre>
  %&lt;guard&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd>
<p> The pattern names should be separated by commas, and the list may be enclosed in quotes to prevent shell expansion, e.g </p>
<pre>
  -c &quot;TeX, c, shell&quot;
</pre>
</dl>
<dt><code>-d</code></p>
<dd> Debug mode on.</p>
<dt><code>-e</code> <i>audience</i></p>
<dd> Extract the contents for the current audience into the file <i>file</i>. The cuurent audience is guessed from the <i>file</i> name, if the latter has the structure <i>base</i>&#8211;<i>audience</i>.<i>extension</i>, e.g. <tt>&quot;report-unclassified.tex&quot;</tt>. The key <code>-a</code> overrides this guess and should be used if the file name does not follow this pattern. The file name <tt>&quot;-&quot;</tt> means the standard output.</p>
<dt><code>-h</code></p>
<dd> Print help information and exit.</p>
<dt><code>-l</code></p>
<dd> List all audiences set in the file (one per line) and exit.</p>
<dt><code>-u</code> <i>audience</i></p>
<dd> Take a edited file intended for the <i>audience</i> (the second non-option argument) and incorporate the changes in it into the full file (the first non-option argument). If the second argument is missing, standard input is used instead. As usual, <tt>&quot;-&quot;</tt> also means standard input. Note that only one of the two file arguments in this case can be standard input.</p>
<dt><code>-v</code></p>
<dd> Print version information and exit.</p>
<dt><code>-w</code> <i>on|off|1|0|true|false</i></p>
<dd> If <tt>&quot;on&quot;</tt>, <tt>1</tt> or <tt>&quot;true&quot;</tt> (the deafult), implicitly wrap the full document into the guards </p>
<pre>
 %&lt;*ALL&gt;
 ...
 %&lt;/ALL&gt;
</pre>
</dl>
<h2>RETURN VALUE</h2>
<p> The program returns 0 if successful, 1 if conflicts were found in the <tt>&quot;unextract&quot;</tt> mode and 2 in case of problems.</p>
<h2>CONFLICTS IN UNEXTRACT MODE</h2>
<p> Like the standard <i><a href="/docs/linux/man/1-diff3/">diff3</a></i>(1) tool, the program may find conflicts between the full version and the edited one in the <code>-u</code> mode. Then the resulting file brackets the conflicts in the usual manner, e.g. </p>
<pre><code>
  &lt;&lt;&lt;&lt;&lt;&lt;&lt; /tmp/BrjXo0hMOB/full
  %&lt;/nobonds&gt;
  Forty-five tons best old dry government bonds, suitable for furnace, gold
  7 per cents., 1864, preferred.
  %&lt;*nobonds&gt;
  ||||||| /tmp/BrjXo0hMOB/extracted
  Forty-five tons best old dry government bonds, suitable for furnace, gold
  7 per cents., 1864, preferred.
  =======
  &gt;&gt;&gt;&gt;&gt;&gt;&gt; /tmp/BrjXo0hMOB/new
</code></pre>
<p> Here <tt>&quot;full&quot;</tt> is the full document, <tt>&quot;extracted&quot;</tt> is the extracted file for the given audience, <tt>&quot;new&quot;</tt> is the edited file.</p>
<h2>AUTHOR</h2>
<p> Boris Veytsman, borisv [at] lk.net </p>
<p> This work was commissioned by Consumer Financial Protection Bureau, United States Treasury.</p>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright (C) 2015 Boris Veytsman. Version 1.0 </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA</font> 02110-1301, <font SIZE="-1">USA</font> </p>
<h2>Index</h2>
