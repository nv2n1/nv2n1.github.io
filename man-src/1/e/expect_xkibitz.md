---
title: "expect_xkibitz(1)"
name: "expect_xkibitz"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expect_xkibitz/"
description: "xkibitz – allow multiple people to interact in an xterm"
---

<h2 class="name">NAME</h2>
<p> xkibitz &#8211; allow multiple people to interact in an xterm </p>
<h2>SYNOPSIS</h2>
<p> <code>xkibitz</code> [ <i>xkibitz-args</i> ] [ <i>program program-args&#8230;</i> ] </p>
<h2>INTRODUCTION</h2>
<p> <code>xkibitz</code> allows users in separate xterms to share one shell (or any program that runs in an xterm). Uses include:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A novice user can ask an expert user for help. Using <code>xkibitz</code>, the expert can see what the user is doing, and offer advice or show how to do it right.</p>
<dt>&bull;</p>
<dd> By running <code>xkibitz</code> and then starting a full-screen editor, people may carry out a conversation, retaining the ability to scroll backwards, save the entire conversation, or even edit it while in progress.</p>
<dt>&bull;</p>
<dd> People can team up on games, document editing, or other cooperative tasks where each person has strengths and weaknesses that complement one another.</p>
<dt>&bull;</p>
<dd> If you want to have a large number of people do an on-line code walk-through, you can sit two in front of each workstation, and then connect them all together while you everyone looks at code together in the editor.</dl>
</dl>
<h2>USAGE</h2>
<p> To start <code>xkibitz</code>, one user (the master) runs xkibitz with no arguments. </p>
<p> <code>xkibitz</code> starts a new shell (or another program, if given on the command line). The user can interact normally with the shell, or upon entering an escape (described when xkibitz starts) can add users to the interaction. </p>
<p> To add users, enter &quot;+ display&quot; where display is the X display name. If there is no &quot;:X.Y&quot; in the display name, &quot;:0.0&quot; is assumed. The master user must have permission to access each display. Each display is assigned a tag &#8211; a small integer which can be used to reference the display. </p>
<p> To show the current tags and displays, enter &quot;=&quot;. </p>
<p> To drop a display, enter &quot;- tag&quot; where tag is the display&#8217;s tag according to the &quot;=&quot; command. </p>
<p> To return to the shared shell, enter &quot;return&quot;. Then the keystrokes of all users become the input of the shell. Similarly, all users receive the output from the shell. </p>
<p> To terminate <code>xkibitz</code> it suffices to terminate the shell itself. For example, if any user types ^D (and the shell accepts this to be EOF), the shell terminates followed by <code>xkibitz</code>. </p>
<p> Normally, all characters are passed uninterpreted. However, in the escape dialogue the user talks directly to the <code>xkibitz</code> interpreter. Any <code><a href="/docs/linux/man/1-expect/">Expect</a></code>(1) or <code><a href="/docs/linux/man/3-tcl/">Tcl</a></code>(3) commands may also be given. Also, job control may be used while in the interpreter, to, for example, suspend or restart <code>xkibitz</code>. </p>
<p> Various processes can produce various effects. For example, you can emulate a multi-way <a href="/docs/linux/man/1-write/">write</a>(1) session with the command: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>xkibitz sleep 1000000</p>
<h2>ARGUMENTS</h2>
<p> <code>xkibitz</code> understands a few special arguments which should appear before the <i>program</i> name (if given). Each argument should be separated by whitespace. If the arguments themselves takes arguments, these should also be separated by whitespace. </p>
<p> <code>-escape</code> sets the escape character. The default escape character is ^]. </p>
<p> <code>-display</code> adds a display much like the &quot;+&quot; command. Multiple -display flags can be given. For example, to start up xkibitz with three additional displays: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>xkibitz -display mercury -display fox -display dragon:1.0</p>
<h2>CAVEATS</h2>
<p> Due to limitations in both X and UNIX, resize propagation is weak. </p>
<p> When the master user resizes the xterm, all the other xterms are logically resized. Unfortunately, xkibitz cannot force the physical xterm size to correspond with the logical xterm sizes. </p>
<p> The other users are free to resize their xterm but their sizes are not propagated. The master can check the logical sizes with the &quot;=&quot; command. </p>
<p> Deducing the window size is a non-portable operation. The code is known to work for recent versions of SunOS, AIX, Unicos, and HPUX. Send back mods if you add support for anything else.</p>
<h2>ENVIRONMENT</h2>
<p> The environment variable SHELL is used to determine and start a shell, if no other program is given on the command line. </p>
<p> If the environment variable DISPLAY is defined, its value is used for the display name of the <code>xkibitz</code> master (the display with tag number 0). Otherwise this name remains empty. </p>
<p> Additional arguments may be passed to new xterms through the environment variable XKIBITZ_XTERM_ARGS. For example, to create xterms with a scrollbar and a green pointer cursor: </p>
<pre>
        XKIBITZ_XTERM_ARGS=&quot;-sb -ms green&quot;
        export XKIBITZ_XTERM_ARGS
</pre>
<p> (this is for the Bourne shell &#8211; use whatever syntax is appropriate for your favorite shell). Any option can be given that is valid for the <code>xterm</code> command, with the exception of <code>-display</code>, <code>-geometry</code> and <code>-S</code> as those are set by <code>xkibitz</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-tcl/">Tcl</a></code>(3), <code><a href="/docs/linux/man/3-libexpect/">libexpect</a></code>(3) <code><a href="/docs/linux/man/1-kibitz/">kibitz</a></code>(1)<br />
 <i>&quot;Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs&quot;</i> by Don Libes, O&#8217;Reilly and Associates, January 1995.<br />
 <i>&quot;kibitz &#8211; Connecting Multiple Interactive Programs Together&quot;, </i>by Don Libes, Software &#8211; Practice &amp; Experience, John Wiley &amp; Sons, West Sussex, England, Vol. 23, No. 5, May, 1993.</p>
<h2>AUTHOR</h2>
<p> Don Libes, National Institute of Standards and Technology </p>
<h2>Index</h2>
