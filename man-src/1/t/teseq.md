---

title: "teseq(1)"
name: "teseq"
section: "1"
letter: "t"
url: "/docs/linux/man/1-teseq/"
description: "teseq – manual page for teseq 1.0.0"
---

<p> teseq &#8211; manual page for teseq 1.0.0</p>
<h2>SYNOPSIS</h2>
<p> <code>teseq</code> [<i>-CLDEx</i>] [<i>in</i>] [<i>out</i>]<br />
 <code>teseq</code> <i>-h | &#8211;help</i><br />
 <code>teseq</code> <i>-V | &#8211;version</i></p>
<h2>DESCRIPTION</h2>
<p> Format text with terminal escapes and control sequences for human consumption.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display usage information (this message).</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Display version and warrantee.</dd>
<dt><code>-C</code></dt>
<dd> Don&#8217;t print ^X for C0 controls.</dd>
<dt><code>-D</code></dt>
<dd> Don&#8217;t print descriptions.</dd>
<dt><code>-E</code></dt>
<dd> Don&#8217;t print escape sequences.</dd>
<dt><code>-L</code></dt>
<dd> Don&#8217;t print labels.</dd>
<dt> <code>-I</code>, <code>&#8211;no-interactive</code></dt>
<dd>Don&#8217;t put the terminal into non-canonical or no-echo mode, and don&#8217;t try to ensure output lines are finished when a signal is received.</dd>
<dt><code>-b</code>, <code>&#8211;buffered</code></dt>
<dd> Force teseq to buffer I/O.</dd>
<dt> <code>-t</code>, <code>&#8211;timings</code>=<i>TIMINGS</i></dt>
<dd>Read timing info from TIMINGS and emit delay lines.</dd>
<dt><code>-x</code></dt>
<dd> Identify control sequences from VT100/Xterm</dd></dl>
<p> The GNU Teseq home page is at <a rel="nofollow" href="http://www.gnu.org/software/teseq/.">http://www.gnu.org/software/teseq/.</a> Report all bugs to bug-teseq [at] gnu.org</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Micah Cowan &lt;micah [at] cowan.name&gt;. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>teseq</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>teseq</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info teseq</code></dd></dl>
<p> should give you access to the complete manual. </p>
