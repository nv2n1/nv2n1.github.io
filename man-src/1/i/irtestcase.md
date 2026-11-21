---

title: "irtestcase(1)"
name: "irtestcase"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irtestcase/"
description: "irtestcase – create or check decoding testcases."
---

<p> irtestcase &#8211; create or check decoding testcases.</p>
<h2>SYNOPSIS</h2>
<p> <code>irtestcase [-l lircrc-file -p prog] &lt;socket&gt;</code><br />
 <code>irtestcase [-l lircrc-file -p prog] -t testdata &lt;socket&gt;</code><br />
 <code>irtestcase [-v|-h|</code> </p>
<h2>DESCRIPTION</h2>
<p> irtestcase is a tool which can record keypresses from a remote together with the decoded values. Given output from another session, it can also verify that the decoding still works as expected. </p>
<p> In the first form irtestcase will wait for input and create log files for it. Doing so, it also echoes received buttons on stdout. There is no way to stop the program in a clean way, just use ctrl-C when completed. </p>
<p> In the second form it will feed the data from the testdata file to lircd and log the the decoded data as usually. Thus, this makes it possible to test the output from the remote which generated the testdata. In this form lircd must be running with the &quot;file&quot; driver. </p>
<p> The optional socket is the lircd output socket (lircd must be running). It defaults to LIRC_SOCKET_PATH in environment, falling back to a hardcoded default value (usually /var/run/lirc/lircd). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l, &#8211;lircrc &lt;lircrc config file&gt;</code></dt>
<dd> Log also applications strings (as <a href="/docs/linux/man/1-ircat/">ircat</a>(1)) using lircrc type config file. </dd>
<dt><code>-p, &#8211;prog &lt;program id&gt;</code></dt>
<dd> When using -l/&#8211;lircrc, the program name matching the PROG = entries in lircrc </dd>
<dt><code>-t, &#8211;testdata</code></dt>
<dd> Use data i file instead of &quot;live&quot; input from the remote. This can be the durations.log file from a previous run, see FILES. It can also be logged output from <a href="/docs/linux/man/1-mode2/">mode2</a>(1). </dd>
<dt><code>-v , &#8211;version</code></dt>
<dd> Print version and exit. </dd>
<dt><code>-h , &#8211;help</code></dt>
<dd> Print help message. </dd>
</dl>
<h2>FILES</h2>
<p> irtestcase creates files in /tmp/irtestcase (hardcoded, sorry). After a successful run here is:</p>
<dl>
<dt><code>durations.log</code></dt>
<dd> Printable space/pulse durations in the same format as <a href="/docs/linux/man/1-mode2/">mode2</a>(1). This file is usable as -t/&#8211;testdata input.</dd>
<dt><code>codes.log</code></dt>
<dd> The decoded buttons, in same format as irw(1).</dd>
<dt><code>app_strings.log</code></dt>
<dd> The application strings, as presented by <a href="/docs/linux/man/1-ircat/">ircat</a>(1). </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.cache/irtestcase.log</code></dt>
<dd> Debug output. Setting the XDG_CACHE_HOME environment variable relocates this file to $XDG_CACHE_HOME/irtestcase.log </dd>
</dl>
<h2>SEE ALSO</h2>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
