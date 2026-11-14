---
title: "xclip(1)"
name: "xclip"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xclip/"
description: "xclip – command line interface to X selections (clipboard)"
---

<h2 class="name">NAME</h2>
<p> xclip &#8211; command line interface to X selections (clipboard) </p>
<h2>SYNOPSIS</h2>
<p> <code>xclip</code> [OPTION] [FILE]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Reads from standard in, or from one or more files, and makes the data available as an X selection for pasting into X applications. Prints current X selection to standard out.</p>
<dl>
<dt><code>-i</code>, <code>-in</code></p>
<dd> read text into X selection from standard input or files (default)</p>
<dt><code>-o</code>, <code>-out</code></p>
<dd> print the selection to standard out (generally for piping to a file or program)</p>
<dt><code>-f</code>, <code>-filter</code></p>
<dd> when xclip is invoked in the in mode with output level set to silent (the defaults), the filter option will cause xclip to print the text piped to standard in back to standard out unmodified</p>
<dt><code>-r</code>, <code>-rmlastnl</code></p>
<dd> when the last character of the selection is a newline character, remove it. Newline characters that are not the last character in the selection are not affected. If the selection does not end with a newline character, this option has no effect. This option is useful for copying one-line output of programs like <code>pwd</code> to the clipboard to paste it again into the command prompt without executing the line immediately due to the newline character <code>pwd</code> appends.</p>
<dt><code>-l</code>, <code>-loops</code></p>
<dd> number of X selection requests (pastes into X applications) to wait for before exiting, with a value of 0 (default) causing xclip to wait for an unlimited number of requests until another application (possibly another invocation of xclip) takes ownership of the selection</p>
<dt><code>-t</code>, <code>-target</code></p>
<dd> specify a particular data format using the given target atom. With <code>-o</code> the special target atom name &quot;TARGETS&quot; can be used to get a list of valid target atoms for this selection. For more information about target atoms refer to ICCCM section 2.6.2</p>
<dt><code>-d</code>, <code>-display</code></p>
<dd> X display to use (e.g. &quot;localhost:0&quot;), xclip defaults to the value in $<code>DISPLAY</code> if this option is omitted</p>
<dt><code>-h</code>, <code>-help</code></p>
<dd> show quick summary of options</p>
<dt><code>-selection</code></p>
<dd> specify which X selection to use, options are &quot;primary&quot; to use XA_PRIMARY (default), &quot;secondary&quot; for XA_SECONDARY or &quot;clipboard&quot; for XA_CLIPBOARD</p>
<dt><code>-version</code></p>
<dd> show version information</p>
<dt><code>-silent</code></p>
<dd> fork into the background to wait for requests, no informational output, errors only (default)</p>
<dt><code>-quiet</code></p>
<dd> show informational messages on the terminal and run in the foreground</p>
<dt><code>-verbose</code></p>
<dd> provide a running commentary of what xclip is doing</p>
<dt><code>-noutf8</code></p>
<dd> operate in legacy (i.e. non UTF-8) mode for backwards compatibility (Use this option only when really necessary, as the old behavior was broken) </p>
</dl>
<p> xclip reads text from standard in or files and makes it available to other X applications for pasting as an X selection (traditionally with the middle mouse button). It reads from all files specified, or from standard in if no files are specified. xclip can also print the contents of a selection to standard out with the <code>-o</code> option. </p>
<p> xclip was designed to allow tighter integration of X applications and command line programs. The default action is to silently wait in the background for X selection requests (pastes) until another X application places data in the clipboard, at which point xclip exits silently. You can use the <code>-verbose</code> option to see if and when xclip actually receives selection requests from other X applications. </p>
<p> Options can be abbreviated as long as they remain unambiguous. For example, it is possible to use <code>-d</code> or <code>-disp</code> instead of <code>-display</code>. However, <code>-v</code> couldn&#8217;t be used because it is ambiguous (it could be short for <code>-verbose</code> or <code>-version</code>), so it would be interpreted as a filename. </p>
<p> Note that only the first character of the selection specified with the <code>-selection</code> option is important. This means that &quot;p&quot;, &quot;sec&quot; and &quot;clip&quot; would have the same effect as using &quot;primary&quot;, &quot;secondary&quot; or &quot;clipboard&quot; respectively. </p>
<h2>EXAMPLES</h2>
<p> I hate man pages without examples! </p>
<p> <code>uptime | xclip</code> </p>
<p> Put your uptime in the X selection. Then middle click in an X application to paste. </p>
<p> <code>xclip -loops 10 -verbose /etc/motd</code> </p>
<p> Exit after /etc/motd (message of the day) has been pasted 10 times. Show how many selection requests (pastes) have been processed. </p>
<p> <code>xclip -o &gt; helloworld.c</code> </p>
<p> Put the contents of the selection into a file. </p>
<p> <code>xclip -t text/html index.html</code> </p>
<p> Middle click in an X application supporting HTML to paste the contents of the given file as HTML. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DISPLAY</code></font></p>
<dd> X display to use if none is specified with the <code>-display</code> option. </p>
</dl>
<h2>REPORTING BUGS</h2>
<p> Please report any bugs, problems, queries, experiences, etc. directly to the author. </p>
<h2>AUTHORS</h2>
<p> Kim Saunders &lt;kims [at] debian.org&gt; Peter Åstrand &lt;astrand [at] lysator.liu.se&gt; </p>
<h2>Index</h2>
