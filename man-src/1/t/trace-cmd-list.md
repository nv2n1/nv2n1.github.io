---

title: "trace-cmd-list(1)"
name: "trace-cmd-list"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-list/"
description: "trace-cmd-list – list available plugins, events or options for Ftrace."
---

<p> trace-cmd-list &#8211; list available plugins, events or options for Ftrace. </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd list</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) list displays the available plugins, events or Ftrace options that are configured on the current machine. If no option is given, then it lists all plugins, events and Ftrace options to standard output.</p>
<h2>OPTIONS</h2>
<p> <code>-e</code> [<i>regex</i>]</p>
<dl>
<dt>
</dt><dd> This option will list the available events that are enabled on the local system. </dd>
<dl>
<dt>
</dt><dd>
<pre>
It takes an optional argument that uses '<a href="//www.systutorials.com/docs/linux/man/3-regcomp/">regcomp</a>(3)' expressions to seach.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
trace-cmd list -e '^sys.*'
</pre>
</dd></dl>
</dl>
<p> <code>-F</code></p>
<dl>
<dt>
</dt><dd> Used with <code>-e</code><i>regex</i> to show those events formats.</dd></dl>
<p> <code>-l</code></p>
<dl>
<dt>
</dt><dd> Used with <code>-e</code><i>regex</i> to show those events filters.</dd></dl>
<p> <code>-R</code></p>
<dl>
<dt>
</dt><dd> Used with <code>-e</code><i>regex</i> to show those events triggers.</dd></dl>
<p> <code>-t</code></p>
<dl>
<dt>
</dt><dd> This option will list the available tracers that are enabled on the local system.</dd></dl>
<p> <code>-p</code></p>
<dl>
<dt>
</dt><dd> Same as <code>-t</code> and only for legacy purposes.</dd></dl>
<p> <code>-o</code></p>
<dl>
<dt>
</dt><dd> This option will list the available Ftrace options that are configured on the local system.</dd></dl>
<p> <code>-f</code> [<i>regex</i>]</p>
<dl>
<dt>
</dt><dd> This option will list the available filter functions. These are the list of functions on the system that you can trace, or filter on. It takes an optional argument that uses <i><a href="/docs/linux/man/3-regcomp/">regcomp</a>(3)</i> expressions to seach. </dd>
<dl>
<dt>
</dt><dd>
<pre>
trace-cmd list -f '^sched.*'
</pre>
</dd></dl>
</dl>
<p> <code>-P</code></p>
<dl>
<dt>
</dt><dd> List the plugin files that get loaded on trace-cmd report.</dd></dl>
<p> <code>-O</code></p>
<dl>
<dt>
</dt><dd> List plugin options that can be used by trace-cmd report <code>-O</code> option.</dd></dl>
<p> <code>-B</code></p>
<dl>
<dt>
</dt><dd> List defined buffer instances (sub buffers).</dd></dl>
<p> <code>-C</code></p>
<dl>
<dt>
</dt><dd> List defined clocks that can be used with trace-cmd record -C. The one in brackets ([]) is the active clock.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
<h2>AUTHOR</h2>
<p> Written by Steven Rostedt, &lt;m[blue]<code>rostedt [at] goodmis.org</code>m[][1]&gt;</p>
<h2>RESOURCES</h2>
<p> <a href="git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git">git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git</a></p>
<h2>COPYING</h2>
<p> Copyright (C) 2010 Red Hat, Inc. Free use of this software is granted under the terms of the GNU Public License (GPL).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> rostedt [at] goodmis.org</dd>
<dl>
<dt>
</dt><dd> mailto:rostedt [at] goodmis.org</dd></dl>
</dl>
