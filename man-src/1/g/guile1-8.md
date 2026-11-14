---
title: "guile1-8(1)"
name: "guile1-8"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guile1-8/"
description: "guile – a Scheme interpreter"
---

<p>guile &#8211; a Scheme interpreter</p>
<h2>Synopsis</h2>
<p><code>guile [-q] [-ds] [&#8211;help] [&#8211;version] [&#8211;emacs] [&#8211;debug]</code> <code>[-l FILE] [-e FUNCTION] []</code> <code>[-c EXPR] [-s SCRIPT] [&#8211;]</code></p>
<h2>Description</h2>
<p>GNU Guile is an interpreter for the Scheme programming language. It implements R5RS, providing additional features necessary for real-world use. It is extremely simple to embed guile into a C program, calling C from Scheme and Scheme from C. Guile&#8217;s design makes it very suitable for use as an &quot;extension&quot; or &quot;glue&quot; language, but it also works well as a stand-alone scheme development environment. </p>
<p> The <code>guile</code> executable itself provides a stand-alone interpreter for scheme programs, for either interactive use or executing scripts. </p>
<p> This manpage provides only brief instruction in invoking <code>guile</code> from the command line. Please consult the guile info documentation (type <code>info guile</code> at a command prompt) for more information. There is also a tutorial <code>(info guile-tut) </code> available. </p>
<h2>Options</h2>
<dl>
<dt>-l</p>
<dd>Load scheme source code from file.</p>
<dt>-e</p>
<dd>After reading script, apply FUNCTION to command-line arguments</p>
<dt>-ds</p>
<dd>do -s SCRIPT at this point (note that this argument must be used in conjuction with -s)</p>
<dt>&#8211;help</p>
<dd>Describe command line options and exit</p>
<dt>&#8211;debug</p>
<dd>Start guile with debugging evaluator and backtraces enabled (useful for debugging guile scripts)</p>
<dt>&#8211;version</p>
<dd>Display guile version and exit.</p>
<dt>&#8211;emacs</p>
<dd>Enable emacs protocol for use from within emacs (experimental)</p>
<dt>&#8212;</p>
<dd>Stop argument processing, start guile in interactive mode.</p>
<dt>-c</p>
<dd>Stop argument processing, evaluate EXPR as a scheme expression.</p>
<dt>-s</p>
<dd>Load Scheme source from SCRIPT-FILE and execute as a script. </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>GUILE_LOAD_PATH</code></p>
<dd>If $<code>GUILE_LOAD_PATH</code> is set, its value is used to agument the path to search for scheme files when loading. It should be a colon separated list of directories which will be prepended to the default %load-path. </p>
</dl>
<h2>Files</h2>
<p><i>~/.guile</i> is a guile script that is executed before any other processing occurs. For example, the following .guile activates guile&#8217;s readline interface: </p>
<dl>
<dd>(use-modules (ice-9 readline))</p>
<dl>
<dd>(activate-readline) </p>
</dl>
</dl>
<h2>See Also</h2>
<p>The full documentation for guile is maintained as a Texinfo manual. If the info and guile programs are properly installed at your site, the command</p>
<dl>
<dd><code>info guile</code></dl>
<p> should give you access to the complete manual. </p>
<p> <a rel="nofollow" href="http://www.schemers.org">http://www.schemers.org</a> provides a general introduction to the Scheme language. </p>
<h2>Authors</h2>
<p>Robert Merkel &lt;rgmerk [at] mira.net&gt; wrote this manpage. Rob Browning &lt;rlb [at] cs.utexas.edu&gt; has added to it. </p>
<p> <code>guile </code> is GNU software. Guile is originally based on Aubrey Jaffer&#8217;s SCM interpreter, and is the work of many individuals.</p>
