---

title: "peekfd(1)"
name: "peekfd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-peekfd/"
description: "peekfd – peek at file descriptors of running processes"
---

<p> peekfd &#8211; peek at file descriptors of running processes </p>
<h2>SYNOPSIS</h2>
<p> <code>peekfd </code> [<code>-8</code>,<code>&#8211;eight-bit-clean</code>] [<code>-n</code>,<code>&#8211;no-headers</code>] [<code>-f</code>,<code>&#8211;follow</code>] [<code>-d</code>,<code>&#8211;duplicates-removed</code>] [<code>-V</code>,<code>&#8211;version</code>] [<code>-h</code>,<code>&#8211;help</code>] <i>pid</i> [<i>fd</i>] [<i>fd</i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>peekfd</code> attaches to a running process and intercepts all reads and writes to file descriptors. You can specify the desired file descriptor numbers or dump all of them.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-8</dt>
<dd> Do no post-processing on the bytes being read or written.</dd>
<dt>-n</dt>
<dd> Do not display headers indicating the source of the bytes dumped.</dd>
<dt>-c</dt>
<dd> Also dump the requested file descriptor activity in any new child processes that are created.</dd>
<dt>-d</dt>
<dd> Remove duplicate read/writes from the output. If you&#8217;re looking at a tty with echo, you might want this.</dd>
<dt>-v</dt>
<dd> Display a version string.</dd>
<dt>-h</dt>
<dd> Display a help message.</dd></dl>
<h2>FILES</h2>
<p> <code>/proc/</code><i>*</i><code>/fd</code></p>
<dl>
<dt>
</dt><dd> Not used but useful for the user to look at to get good file descriptor numbers.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> None.</p>
<h2>DIAGNOSTICS</h2>
<p> The following diagnostics may be issued on stderr:</p>
<dl>
<dt><code>Error attaching to pid </code><i>&lt;PID&gt;</i></dt>
<dd> An unknown error occurred while attempted to attach to a process, you may need to be root.</dd></dl>
<h2>BUGS</h2>
<p> Probably lots. Don&#8217;t be surprised if the process you are monitoring dies.</p>
<h2>AUTHOR</h2>
<p> Trent Waddington</p>
<h2>SEE ALSO</h2>
<p> <code>ttysnoop</code>(8) </p>
