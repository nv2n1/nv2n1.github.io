---
title: "fvwmdebug(1)"
name: "fvwmdebug"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmdebug/"
description: "FvwmDebug – the fvwm module debugger"
---

<p>FvwmDebug &#8211; the fvwm module debugger </p>
<h2>Synopsis</h2>
<p>FvwmDebug should be spawned by <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1) for normal functionality. </p>
<p> To run this module, place this command somewhere in the configuration: </p>
<pre> Module FvwmDebug [optional-params]</pre>
<p>To stop this module, execute: </p>
<pre> KillModule FvwmDebug</pre>
<h2>Description</h2>
<p>This module persistently dumps all fvwm event details and optionally some other information into the standard error stream or a file, good for debugging purposes. The output may be optionally redirected to <i>xconsole</i> or similar window.</p>
<h2>Invocation</h2>
<p>There are several command line switches: </p>
<p> <code>FvwmDebug</code> [ <code>&#8211;args</code>|<code>&#8211;noargs</code> ] [ <code>&#8211;events</code>|<code>&#8211;noevents</code> ] [ <code>&#8211;log</code> <i>file</i> ] [ <code>&#8211;xconsole</code> ] [ <code>&#8211;mask</code> <i>mask</i> ] [ <code>&#8211;xmask</code> <i>mask</i> ] [ <code>&#8211;debug</code> <i>level</i> ] [ <code>&#8211;track</code> <i>tracker-name</i> ] [ <code>&#8211;send-configinfo</code> ] [ <code>&#8211;send-windowlist</code> ] </p>
<p> Long switches may be abbreviated to shorter switches. </p>
<p> <code>&#8211;noargs</code> &#8211; do not print all arguments of the event, just its name. <code>&#8211;args</code> is the default. </p>
<p> <code>&#8211;noevents</code> &#8211; do not print even event names, implies <code>&#8211;noargs</code>. It is similar in effect to setting both <code>&#8211;mask</code> and <code>&#8211;xmask</code> to 0, but the events are actually received by the module, they are just not printed. </p>
<p> This option may be useful if <code>&#8211;track</code> or/and <code>&#8211;debug</code> is used. </p>
<p> The default is <code>&#8211;events</code> normally, and <code>&#8211;noevents</code> if one or more <code>&#8211;track</code> options specified. </p>
<p> <code>-l</code>|<code>&#8211;log</code> <i>file</i> &#8211; specify the log file name instead of the standard error stream. If the log file can&#8217;t be open for writing, the default standard error stream is used. </p>
<p> The <i>file</i> may start with a pipe &#8216;|&#8217;, this is similar to the usual meaning of a pipe, the output is piped to the specified command. See also <code>&#8211;xconsole</code> option. </p>
<p> <code>-xc</code>|<code>&#8211;xconsole</code> &#8211; this is a shortcut for: </p>
<pre> FvwmDebug --log '|xconsole -file /dev/stdin -geometry 600x400 -notify'</pre>
<p>That shows the module output in the <i>xconsole</i> window rather than the standard error stream. </p>
<p> <code>-m</code>|<code>&#8211;mask</code> <i>mask</i> &#8211; set the module mask, 31 bit integer. By default almost all events are monitored (except for some flood events like <i></i><font SIZE="-1"><i>CONFIGURE_WINDOW</i></font><i></i> or <i></i><font SIZE="-1"><i>FOCUS_WINDOW</i></font><i></i>. The special value of <i>-1</i> sets the maximal mask. </p>
<p> <code>-x</code>|<code>&#8211;xmask</code> <i>mask</i> &#8211; set the module extended mask, 31 bit integer. By default almost all events are monitored (except for some flood events like <i></i><font SIZE="-1"><i>ENTER_WINDOW</i></font><i></i> or <i></i><font SIZE="-1"><i>LEAVE_WINDOW</i></font><i></i>. The special value of <i>-1</i> sets the maximal extended mask. </p>
<p> <code>-d</code>|<code>&#8211;debug</code> <i>level</i> &#8211; use the Perl library debugging mechanism. The useful <i>level</i>s are 2 to 4. </p>
<p> <code>-t</code>|<code>&#8211;track</code> <i>tracker-name</i> &#8211; create the given Perl library tracker and observe its main observable. This option may be specified multiple times. This options implies <code>&#8211;noevents</code> unless explicitly overwritten. You may optionally try <code>&#8211;debug</code>, for example: </p>
<pre> FvwmDebug -xc --track PageInfo --track GlobalConfig --debug 3</pre>
<p>Run &#8220;fvwm-perllib man&#8221; to get the names of all existing trackers in your installed Perl library. </p>
<p> <code>-sc</code>|<code>&#8211;send-configinfo</code> &#8211; send <code>Send_ConfigInfo</code> command to <i>fvwm</i> on startup, this results in a lot of events received. </p>
<p> <code>-sw</code>|<code>&#8211;send-windowlist</code> &#8211; send <code>Send_WindowList</code> command to <i>fvwm</i> on startup, this results in a lot of events received.</p>
<h2>See Also</h2>
<p>See also FvwmGtkDebug.</p>
<h2>Author</h2>
<p>Mikhael Goikhman &lt;migo [at] homemail.com&gt;.</p>
