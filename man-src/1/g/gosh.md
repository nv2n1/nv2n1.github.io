---
title: "gosh(1)"
name: "gosh"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gosh/"
description: "gosh – a Scheme script interpreter"
---

<h2 class="name">NAME</h2>
<p> gosh &#8211; a Scheme script interpreter </p>
<h2>SYNOPSIS</h2>
<p> <code>gosh</code> [-biqV] [-I <i>path</i> ] [-A <i>path</i> ] [-u <i>module</i> ] [-l <i>file</i> ] [-e <i>expr</i> ] [-E <i>expr</i> ] [-f <i>flag</i> ] [&#8211;] [ <i>script argument &#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <i>Gosh</i> is a stand-alone Scheme interpreter built on top of the <i>Gauche</i> Scheme implementation. </p>
<p> When <i>script</i> is given, gosh loads the script, evaluating Scheme code in it. Then, if the <i>script</i> defines a procedure named <i>main,</i> gosh calls it with a single argument which is a list of the script name and subsequent arguments. When <i>main</i> returns an integer value, gosh exits with it as an exit code. If <i>main</i> returns non-integer value, or an error is signaled during evaluation, gosh exits with exit code 70 (EX_SOFTWARE). See SRFI-22 (<a rel="nofollow" href="http://srfi.schemers.org/srfi-22/srfi-22.html)">http://srfi.schemers.org/srfi-22/srfi-22.html)</a> for details. If there&#8217;s no <i>main</i> procedure defined in the script, gosh exits with code 0 after loading the script file. </p>
<p> If no script file is given, gosh goes into an interactive mode. By default, gosh prompts the user to enter a Scheme expression, read and evaluates it, then prints the result, until EOF is read. If the standard input is not a terminal, however, gosh doesn&#8217;t print a prompt; it allows a user to use gosh as a filter program. This behavior can be controlled by -i or -b option; see below. </p>
<h2>OPTIONS</h2>
<p> Command line options are processed before loading the script file or entering the interactive mode. </p>
<p> The options -I, -A, -u, -l, -e and -E are processed in the order of appearance. For example, adding a load path by -I option affects the -l options after it, but not the ones before it. </p>
<dl>
<dt><code>-V</code></p>
<dd> Prints gosh version and exits.</p>
<dt><code>-b</code></p>
<dd> Batch mode. Doesn&#8217;t print prompt even the standard input is a terminal. Supersedes -i.</p>
<dt><code>-i</code></p>
<dd> Interactive mode. Forces to print prompt, even the standard input is not a terminal.</p>
<dt><code>-q</code></p>
<dd> Prevents reading the default initialization file.</p>
<dt><code>-I</code><i>path</i></p>
<dd> Adds <i>path</i> in front of the load path list.</p>
<dt><code>-A</code><i>path</i></p>
<dd> Appends <i>path</i> to the tail of the load path list.</p>
<dt><code>-u</code><i>module</i></p>
<dd> Loads and imports <i>module,</i> as if &quot;(use <i>module</i> )&quot; is specified in the code.</p>
<dt><code>-l</code><i>file</i></p>
<dd> Loads a Scheme file <i>file.</i></p>
<dt><code>-e</code><i>expr</i></p>
<dd> Evaluates a Scheme expression <i>expr.</i></p>
<dt><code>-E</code><i>expr</i></p>
<dd> Same as -e, except that the <i>expr</i> is read as if it is surrounded by parenthesis.</p>
<dt><code>-f</code><i>flag</i></p>
<dd> Sets various flags.<br />
&nbsp;<wbr>&nbsp;<wbr>no-inline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>don&#8217;t inline primitive procedures<br />
&nbsp;<wbr>&nbsp;<wbr>no-source-info&nbsp;<wbr>&nbsp;<wbr>don&#8217;t preserve source information for debug<br />
&nbsp;<wbr>&nbsp;<wbr>load-verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>report while loading files<br />
&nbsp;<wbr>&nbsp;<wbr>case-fold&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>uses case-insensitive reader&nbsp;<wbr>(as in R5RS)</p>
<dt><code>&#8212;</code></p>
<dd> Specifies that there are no more options. If there are more arguments after this, they are taken as script file name and its arguments. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GAUCHE_LOAD_PATH</code></p>
<dd> A colon separated list of the load paths. The paths are appended before the system default load paths.</p>
<dt><code>GAUCHE_DYNLOAD_PATH</code></p>
<dd> A colon separated list of the load paths for dynamically loaded objects. The paths are appended before the system default load paths. </p>
</dl>
<h2>AUTHORS</h2>
<p> Shiro Kawai (shiro @ acm . org) </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gauche-config/">gauche-config</a>(1) </p>
<p> Gauche Scheme interpreter:<br />
 <a rel="nofollow" href="http://practical-scheme.net/gauche/">http://practical-scheme.net/gauche/</a> </p>
<p> For the information about Scheme language, see<br />
 <a rel="nofollow" href="http://www.schemers.org/">http://www.schemers.org/</a> </p>
<h2>Index</h2>
