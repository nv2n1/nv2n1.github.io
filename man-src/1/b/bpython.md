---
title: "bpython(1)"
name: "bpython"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bpython/"
description: "bpython – a fancy {curses, GTK+, urwid} interface to the Python interactive interpreter"
---

<h2>NAME</h2>
<p> bpython &#8211; a fancy {curses, GTK+, urwid} interface to the Python interactive interpreter</p>
<h2>SYNOPSIS</h2>
<p> <code>bpython</code> [<i>options</i>] [<i>file</i> [<i>args</i>]] </p>
<p> <code>bpython-gtk</code> [<i>options</i>] [<i>file</i> [<i>args</i>]] </p>
<p> <code>bpython-urwid</code> [<i>options</i>] [<i>file</i> [<i>args</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The idea is to provide the user with all the features in-line, much like modern IDEs, but in a simple, lightweight package that can be run in a terminal window.</p>
<dl>
<dt><code>In-line syntax highlighting.</code></dt>
<dd> Hilights commands as you type!</dd>
<dt><code>Readline-like autocomplete with suggestions displayed as you type.</code></dt>
<dd> Press tab to complete expressions when there&#8217;s only one suggestion.</dd>
<dt><code>Expected parameter list.</code></dt>
<dd> This displays a list of parameters for any function you call. It uses the inspect module, then tries pydoc.</dd>
<dt><code>Rewind.</code></dt>
<dd> This is a bit misleading, but it code that has been entered is remembered, and when you Rewind, it pops the last line and re-evaluates the entire code. This is error-prone, and mostly useful for defining classes and functions.</dd>
<dt><code>Pastebin code/write to file.</code></dt>
<dd> This posts the current buffer to a pastebin (paste.pocoo.org) or writes it to a file.</dd>
<dt><code>Flush curses screen to stdout.</code></dt>
<dd> Unlike other curses apps, bpython dumps the screen data to stdout when you quit, so you see what you&#8217;ve done in the buffer of your terminal.</dd></dl>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent. If <code>bpython</code> sees an argument it does not know, execution falls back to the regular Python interpreter.</p>
<dl>
<dt><code>&#8211;config=</code><i>&lt;config&gt;</i></dt>
<dd> Use &lt;config&gt; instead of default config file.</dd>
<dt><code>-h</code>,<code> &#8211;help</code></dt>
<dd> Show the help message and exit.</dd>
<dt><code>-i</code>,<code> &#8211;interactive</code></dt>
<dd> Drop to bpython shell after running file instead of exiting. The PYTHONSTARTUP file is not read.</dd>
<dt><code>-q</code>,<code> &#8211;quiet</code></dt>
<dd> Do not flush the output to stdout.</dd>
<dt><code>-V</code>,<code> &#8211;version</code></dt>
<dd> Print <code>bpython</code>&#8216;s version and exit. </dd>
<p> In addition to the above options, <code>bpython-urwid</code> also supports the following options if Twisted is available:</p>
<dt><code>-r</code><i>&nbsp;<wbr>&lt;reactor&gt;</i>,<code>&nbsp;<wbr>&#8211;reactor=</code><i>&lt;reactor&gt;</i></dt>
<dd> Use Twisted&#8217;s &lt;reactor&gt; instead of urwid&#8217;s event loop.</dd>
<dt><code>&#8211;help-reactors</code></dt>
<dd> Display a list of available Twisted reactors.</dd>
<dt><code>-p</code><i>&nbsp;<wbr>&lt;plugin&gt;</i>,<code>&nbsp;<wbr>&#8211;plugin=</code><i>&lt;plugin&gt;</i></dt>
<dd> Execute a <code>twistd</code> plugin. Use <code>twistd</code> to get a list of available plugins. Use &#8212; to pass options to the plugin.</dd>
<dt><code>-s</code><i>&nbsp;<wbr>&lt;port&gt;</i>,<code>&nbsp;<wbr>&#8211;server=</code><i>&lt;port&gt;</i></dt>
<dd> Run an eval server on port &lt;port&gt;. This options forces the use of a Twisted reactor. </dd>
<p> <code>bpython-gtk</code> also supports the following options:</p>
<dt><code>&#8211;socket-id=</code><i>&lt;socket-id&gt;</i></dt>
<dd> Embed bpython.</dd></dl>
<h2>KEYS</h2>
<p> <code>bpython</code>&#8216;s keys are fully configurable. See <i><a rel="nofollow" href="http://docs.bpython-interpreter.org/configuration.html#keyboard">http://docs.bpython-interpreter.org/configuration.html#keyboard</a></i></p>
<h2>FILES</h2>
<p> <code>$XDG_CONFIG_HOME/bpython/config</code> </p>
<p> Your bpython config. See sample-config (in /usr/share/doc/bpython/examples on Debian) for various options you can use, or read <i>python-config(5)</i>.</p>
<h2>KNOWN BUGS</h2>
<p> See <i><a rel="nofollow" href="http://bitbucket.org/bobf/bpython/issues/">http://bitbucket.org/bobf/bpython/issues/</a></i> for a list of known issues.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-bpython-config/">bpython-config</a>(5)</i>, <i><a href="/docs/linux/man/1-python/">python</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> <code>bpython</code> was written by Robert Anthony Farrell &lt;<i>robertanthonyfarrel [at] gmail.com</i>&gt; and his bunch of loyal followers. </p>
<p> This manual page was written by Jørgen Pedersen Tjernø &lt;<i>jorgen [at] devsoft.no</i>&gt;, for the Debian project (but may be used by others).</p>
<h2>COPYRIGHT</h2>
<p> 2008-2012 Bob Farrell, Andreas Stuehrk et al. </p>
