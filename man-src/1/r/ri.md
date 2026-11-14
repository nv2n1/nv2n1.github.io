---
title: "ri(1)"
name: "ri"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ri/"
description: "ri – Ruby API reference front end"
---

<p>UNIX</p>
<h2 class="name">NAME</h2>
<p> <code>ri</code> &#8211; Ruby API reference front end </p>
<h2>SYNOPSIS</h2>
<p> <code>ri</code> [-<code>ahilTv </code>[-<code>d </code><i>DIRNAME</i> ] ] [-<code>f </code><i>FORMAT</i> ] [-<code>w </code><i>WIDTH</i> ] [-<code>&#8211; </code>[<code>no- pager</code> ] ] [-<code>-server </code>[= <i>PORT </i>] ] [-<code>&#8211; </code>[<code>no- list-doc-dirs</code> ] ] [-<code>-no-standard-docs</code> ] [-<code>&#8211; </code>[<code>no- Bro system | site | gems | home Brc</code> ] ] [-<code>&#8211; </code>[<code>no- profile</code> ] ] [-<code>-dump = </code><i>CACHE</i> ] [<i>name &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ri</code> is a command-line front end for the Ruby API reference. You can search and read the API reference for classes and methods with <code>ri.</code> </p>
<p> <code>ri</code> is a part of Ruby. </p>
<p> <i>name</i> can be:</p>
<dl>
<dt><code>Class | Module | Module::Class</code></p>
<dd>
<dt><code>Class::method | Class#method | Class.method | method</code></p>
<dd>
<dt><code>gem_name: | gem_name:README | gem_name:History</code></p>
<dd></dl>
<p> All class names may be abbreviated to their minimum unambiguous form. If a name is ambiguous, all valid options will be listed. </p>
<p> A `.&#8217; matches either class or instance methods, while #method matches only instance and ::method matches only class methods. </p>
<p> README and other files may be displayed by prefixing them with the gem name they&#8217;re contained in. If the gem name is followed by a `:&#8217; all files in the gem will be shown. The file name extension may be omitted where it is unambiguous. </p>
<p> For example: </p>
<blockquote>
<pre>
ri Fil
ri File
ri File.new
ri zip
ri rdoc:README
</pre>
</blockquote>
<p> Note that shell quoting or escaping may be required for method names containing punctuation: </p>
<blockquote>
<pre>
ri 'Array.[]'
ri compact\!
</pre>
</blockquote>
<p> To see the default directories <code>ri</code> will search, run: </p>
<blockquote>
<pre>
ri --list-doc-dirs
</pre>
</blockquote>
<p> Specifying the &#8211;<code>-system , &#8211;site , &#8211;home , &#8211;gems</code> or &#8211;<code>-doc-dir</code> options will limit <code>ri</code> to searching only the specified directories. </p>
<p> <code>ri</code> options may be set in the <code>RI</code> environment variable. </p>
<p> The <code>ri</code> pager can be set with the <code>RI_PAGER</code> environment variable or the <code>PAGER</code> environment variable. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8212; </code>[<code>no- interactive</code> ]</p>
<dd> In interactive mode you can repeatedly look up methods with autocomplete. </p>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8212; </code>[<code>no- all</code> ]</p>
<dd> Show all documentation for a class or module. </p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8212; </code>[<code>no- list</code> ]</p>
<dd> List classes <code>ri</code> knows about. </p>
<dt><code>&#8212; </code>[<code>no- pager</code> ]</p>
<dd> Send output to a pager, rather than directly to stdout. </p>
<dt><code>-T</code></p>
<dd> Synonym for &#8211;<code>-no-pager</code> </p>
<dt><code>-w </code><i>WIDTH</i></p>
<dd>
<dt><code>&#8211;width = </code><i>WIDTH</i></p>
<dd> Set the width of the output. </p>
<dt><code>&#8211;server </code>[= <i>PORT </i>]</p>
<dd> Run RDoc server on the given port. The default port is~8214. </p>
<dt><code>-f </code><i>FORMAT</i></p>
<dd>
<dt><code>&#8211;format = </code><i>FORMAT</i></p>
<dd> Use the selected formatter. The default formatter is <code>bs</code> for paged output and <code>ansi</code> otherwise. Valid formatters are: <code>ansi , bs , markdown , rdoc</code> </p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Show help and exit. </p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</dl>
<p> Data source options:</p>
<dl>
<dt><code>&#8212; </code>[<code>no- list-doc-dirs</code> ]</p>
<dd> List the directories from which <code>ri</code> will source documentation on stdout and exit. </p>
<dt><code>-d </code><i>DIRNAME</i></p>
<dd>
<dt><code>&#8211;doc-dir = </code><i>DIRNAME</i></p>
<dd> List of directories from which to source documentation in addition to the standard directories. May be repeated. </p>
<dt><code>&#8211;no-standard-docs</code></p>
<dd> Do not include documentation from the Ruby standard library, site_lib installed gems, or ~/.rdoc Use with &#8211;<code>-doc-dir</code> </p>
<dt><code>&#8212; </code>[<code>no- system</code> ]</p>
<dd> Include documentation from Ruby&#8217;s standard library. Defaults to true. </p>
<dt><code>&#8212; </code>[<code>no- site</code> ]</p>
<dd> Include documentation from libraries installed in site_lib Defaults to true. </p>
<dt><code>&#8212; </code>[<code>no- gems</code> ]</p>
<dd> Include documentation from RubyGems. Defaults to true. </p>
<dt><code>&#8212; </code>[<code>no- home</code> ]</p>
<dd> Include documentation stored in ~/.rdoc Defaults to true.</dl>
<p> Debug options:</p>
<dl>
<dt><code>&#8212; </code>[<code>no- profile</code> ]</p>
<dd> Run with the Ruby profiler. </p>
<dt><code>&#8211;dump = </code><i>CACHE</i></p>
<dd> Dump data from an ri cache or data file.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>RI</code></p>
<dd> Options to prepend to those specified on the command-line. </p>
<dt><code>RI_PAGER</code></p>
<dd>
<dt><code>PAGER</code></p>
<dd> Pager program to use for displaying. </p>
<dt><code>HOME</code></p>
<dd>
<dt><code>USERPROFILE</code></p>
<dd>
<dt><code>HOMEPATH</code></p>
<dd> Path to the user&#8217;s home directory.</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.rdoc </code></p>
<dd> Path for ri data in the user&#8217;s home directory. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ruby/">ruby</a>(1), <a href="/docs/linux/man/1-rdoc/">rdoc</a>(1), <a href="/docs/linux/man/1-gem/">gem</a>(1) </p>
<h2>REPORTING BUGS</h2>
<ul>
<li> Security vulnerabilities should be reported via an email to Mt security [at] ruby-lang.org . Reported problems will be published after being fixed.
<li> Other bugs and feature requests can be reported via the Ruby Issue Tracking System (Lk <a rel="nofollow" href="https://bugs.ruby-lang.org/">https://bugs.ruby-lang.org/</a> ) Do not report security vulnerabilities via this system because it publishes the vulnerabilities immediately. </ul>
<h2>AUTHORS</h2>
<p> Written by An Dave Thomas Aq dave [at] pragmaticprogrammer.com . </p>
<h2>Index</h2>
