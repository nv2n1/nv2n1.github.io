---
title: "fvwmgtkdebug(1)"
name: "fvwmgtkdebug"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmgtkdebug/"
description: "FvwmGtkDebug – graphical interactive fvwm module debugger"
---

<p>FvwmGtkDebug &#8211; graphical interactive fvwm module debugger </p>
<h2>Synopsis</h2>
<p>FvwmGtkDebug should be spawned by <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1). </p>
<p> To run this module, place this command somewhere in the configuration: </p>
<pre> Module FvwmGtkDebug</pre>
<p>To stop this module, just close the <font SIZE="-1">GUI</font> window, the usual KillModule works too. </p>
<p> You may also run this application as a regular program from the command line shell.&nbsp;<wbr> But the communication with <i>fvwm</i> is not established in this dummy mode, so commands are not really sent and there are no real events received.&nbsp;<wbr> However certain activity is emulated using dummy events.</p>
<h2>Description</h2>
<p>This module monitors all fvwm event information and shows it nicely in the interactive gtk+ application. Good for debugging and educational purposes. </p>
<p> Among the features: command console with history and auto command help, requesting to send back ConfigInfo (configuration of <i>fvwm</i> and all modules), WindowList (information about all windows) or custom Reply. </p>
<p> The fvwm commands may be executed within the context of some window. The context window may be optionally set on invocation, like: &#8220;Next (Navigator) FvwmGtkDebug&#8221;, and be set/unset interactively at any time.</p>
<h2>Invocation</h2>
<p>There are several command line switches: </p>
<p> <code>FvwmGtkDebug</code> [ <code>&#8211;mask</code> <i>mask</i> ] [ <code>&#8211;xmask</code> <i>mask</i> ] [ <code>&#8211;debug</code> <i>level</i> ] </p>
<p> Long switches may be abbreviated to shorter switches. </p>
<p> <code>-m</code>|<code>&#8211;mask</code> <i>mask</i> &#8211; set the initial module mask, 31 bit integer. This mask may be changed interactively at any time. By default almost all events are monitored (except for some flood events like <i></i><font SIZE="-1"><i>CONFIGURE_WINDOW</i></font><i></i> or <i></i><font SIZE="-1"><i>FOCUS_WINDOW</i></font><i></i>. The special value of <i>-1</i> sets the maximal mask. </p>
<p> <code>-x</code>|<code>&#8211;xmask</code> <i>mask</i> &#8211; set the initial module extended mask, 31 bit integer. This mask may be changed interactively at any time. By default almost all events are monitored (except for some flood events like <i></i><font SIZE="-1"><i>ENTER_WINDOW</i></font><i></i> or <i></i><font SIZE="-1"><i>LEAVE_WINDOW</i></font><i></i>. The special value of <i>-1</i> sets the maximal extended mask. </p>
<p> <code>-d</code>|<code>&#8211;debug</code> <i>level</i> &#8211; use the Perl library debugging mechanism. The useful <i>level</i>s are 2 to 4.</p>
<h2>See Also</h2>
<p>See also FvwmDebug, &#8220;fvwm-perllib man events&#8221;.</p>
<h2>Author</h2>
<p>Mikhael Goikhman &lt;migo [at] homemail.com&gt;.</p>
