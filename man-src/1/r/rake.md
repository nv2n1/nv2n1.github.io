---
title: "rake(1)"
name: "rake"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rake/"
description: "rake – make-like build utility for Ruby"
---

<p>rake 11.2.2</p>
<h2 class="name">NAME</h2>
<p> <code>rake</code> &#8211; make-like build utility for Ruby </p>
<h2>SYNOPSIS</h2>
<p> <code>rake</code> [-<code>f </code><i>rakefile</i> ] [<i>options</i> ] <i>targets &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>rake</code> is a <a href="/docs/linux/man/1-make/">make</a>(1)Ns-like build utility for Ruby. Tasks and dependencies are specified in standard Ruby syntax.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m , &#8211;multitask</code></p>
<dd> Treat all tasks as multitasks.</p>
<dt><code>-B , &#8211;build-all</code></p>
<dd> Build all prerequisites, including those which are up-to-date.</p>
<dt><code>-j , &#8211;jobs </code><i>num_jobs</i></p>
<dd> Specifies the maximum number of tasks to execute in parallel (default is number of CPU cores + 4).</dl>
<h3>Modules</h3>
<dl>
<dt><code>-I , &#8211;libdir </code><i>libdir</i></p>
<dd> Include <i>libdir</i> in the search path for required modules.</p>
<dt><code>-r , &#8211;require </code><i>module</i></p>
<dd> Require <i>module</i> before executing rakefile</dl>
<h3>Rakefile location</h3>
<dl>
<dt><code>-f , &#8211;rakefile </code><i>filename</i></p>
<dd> Use <i>filename</i> as the rakefile to search for.</p>
<dt><code>-N , &#8211;no-search , &#8211;nosearch</code></p>
<dd> Do not search parent directories for the Rakefile.</p>
<dt><code>-G , &#8211;no-system , &#8211;nosystem</code></p>
<dd> Use standard project Rakefile search paths, ignore system wide rakefiles.</p>
<dt><code>-R , &#8211;rakelib </code><i>rakelibdir , &#8211;</i><code>-rakelibdir </code><i>rakelibdir</i></p>
<dd> Auto-import any .rake files in <i>rakelibdir</i> (default is `rakelib&#8217;</p>
<dt><code>-g , &#8211;system</code></p>
<dd> Use system-wide (global) rakefiles (usually ~/.rake/*.rake )</dl>
<h3>Debugging</h3>
<dl>
<dt><code>&#8211;backtrace = </code><i>out</i></p>
<dd> Enable full backtrace. <i>out</i> can be <code>stderr</code> (default) or <code>stdout</code></p>
<dt><code>-t , &#8211;trace = </code><i>out</i></p>
<dd> Turn on invoke/execute tracing, enable full backtrace. <i>out</i> can be <code>stderr</code> (default) or <code>stdout</code></p>
<dt><code>&#8211;suppress-backtrace </code><i>pattern</i></p>
<dd> Suppress backtrace lines matching regexp <i>pattern</i> Ignored if &#8211;<code>-trace</code> is on.</p>
<dt><code>&#8211;rules</code></p>
<dd> Trace the rules resolution.</p>
<dt><code>-n , &#8211;dry-run</code></p>
<dd> Do a dry run without executing actions.</p>
<dt><code>-T , &#8211;tasks </code>[<i>pattern</i> ]</p>
<dd> Display the tasks (matching optional <i>pattern</i> with descriptions, then exit.</p>
<dt><code>-D , &#8211;describe </code>[<i>pattern</i> ]</p>
<dd> Describe the tasks (matching optional <i>pattern )</i> then exit.</p>
<dt><code>-W , &#8211;where </code>[<i>pattern</i> ]</p>
<dd> Describe the tasks (matching optional <i>pattern )</i> then exit.</p>
<dt><code>-P , &#8211;prereqs</code></p>
<dd> Display the tasks and dependencies, then exit.</p>
<dt><code>-e , &#8211;execute </code><i>code</i></p>
<dd> Execute some Ruby code and exit.</p>
<dt><code>-p , &#8211;execute-print </code><i>code</i></p>
<dd> Execute some Ruby code, print the result, then exit.</p>
<dt><code>-E , &#8211;execute-continue </code><i>code</i></p>
<dd> Execute some Ruby code, then continue with normal task processing.</dl>
<h3>Information</h3>
<dl>
<dt><code>-v , &#8211;verbose</code></p>
<dd> Log message to standard output.</p>
<dt><code>-q , &#8211;quiet</code></p>
<dd> Do not log messages to standard output.</p>
<dt><code>-s , &#8211;silent</code></p>
<dd> Like &#8211;<code>-quiet</code> but also suppresses the `in directory&#8217; announcement.</p>
<dt><code>-X , &#8211;no-deprecation-warnings</code></p>
<dd> Disable the deprecation warnings.</p>
<dt><code>&#8211;comments</code></p>
<dd> Show commented tasks only</p>
<dt><code>-A , &#8211;all</code></p>
<dd> Show all tasks, even uncommented ones (in combination with &#8211;<code>T</code> or &#8211;<code>D</code></p>
<dt><code>&#8211;job-stats </code>[<i>level</i> ]</p>
<dd> Display job statistics. If <i>level</i> is `history&#8217; displays a complete job list.</p>
<dt><code>-V , &#8211;version</code></p>
<dd> Display the program version.</p>
<dt><code>-h , -H , &#8211;help</code></p>
<dd> Display a help message.</dl>
<h2>SEE ALSO</h2>
<p> The complete documentation for <code>rake</code> has been installed at /usr/share/doc/rake-doc/html/index.html It is also available online at Lk <a rel="nofollow" href="https://ruby.github.io/rake">https://ruby.github.io/rake</a> .</p>
<h2>AUTHORS</h2>
<p> An -nosplit <code>rake</code> was written by An Jim Weirich Aq Mt jim [at] weirichhouse.org . </p>
<p> This manual was created by An Caitlin Matos Aq Mt caitlin.matos [at] zoho.com for the Debian project (but may be used by others). It was inspired by the manual by An Jani Monoses Aq Mt jani [at] iv.ro for the Ubuntu project. </p>
<h2>Index</h2>
