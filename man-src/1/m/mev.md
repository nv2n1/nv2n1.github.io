---
title: "mev(1)"
name: "mev"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mev/"
description: "mev – a program to report mouse events"
---

<h2 class="name">NAME</h2>
<p> mev &#8211; a program to report mouse events </p>
<h2>SYNOPSIS</h2>
<p> <code>mev</code> [ <i>options</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The `mev&#8217; program is part of the gpm package. The information below is extracted from the texinfo file, which is the preferred source of information. </p>
<p> The mev program is modeled after xev. It prints to stdout the mouse console events it gets. </p>
<p> mev&#8217;s default behaviour is to get anything, but command line switches can be used to set the various fields in the Gpm_Connect structure, in order to customize the program&#8217;s behaviour. I&#8217;m using mev to handle mouse events to Emacs. </p>
<p> Command line switches for mev are the following:</p>
<dl>
<dt>-C <code>number</code></p>
<dd> Select a virtual console to get events from. This is intended to be used for debugging.</p>
<dt>-d <code>number</code></p>
<dd> Choose a default mask. By default the server gets any events not belonging to the event mask. The mask can be provided either as a decimal number, or as a symbolic string.</p>
<dt>-e <code>number</code></p>
<dd> Choose the event mask. By default any event is received. The mask can be provided either as a decimal number, or as a symbolic string.</p>
<dt>-E</p>
<dd> Enter emacs mode. In emacs mode events are reported as lisp forms rather than numbers. This is the format used by the t-mouse package within emacs.</p>
<dt>-f</p>
<dd> Fit events inside the screen before reporting them. This options re-fits drag events, which are allowed to exit the screen border, </p>
<dt>-i</p>
<dd> Interactive. Accepts input from stdin to change connection parameters.</p>
<dt>-m <code>number</code></p>
<dd> Choose the minimum modifier mask. Any event with fewer modifiers will not be reported to mev. It defaults to 0. The mask must be provided either as a decimal number, or as a symbolic string.</p>
<dt>-M <code>number</code></p>
<dd> Choose the maximum modifier mask. Any event with more modifier than specified will not be reported to mev. It defaults to ~~0, i.e. all events are received. The mask must be provided either as a decimal number, or as a symbolic string.</p>
<dt>-p</p>
<dd> Requests to draw the pointer during drags. This option is used by emacs to avoid invoking ioctl() from lisp code. </p>
</dl>
<p> When the arguments are not decimal integers, they are considered lists of alphanumeric characters, separated by a single non-alphanumeric character. I use the comma (,), but any will do. </p>
<p> Allowed names for events are move, drag, down or press, up or release, motion (which is both move and drag), and hard. </p>
<p> Allowed names for modifiers are shift, leftAlt, rightAlt, anyAlt (one or the other), control. </p>
<p> When the -i switch is specified, mev looks at its standard input as command lines rather than events. The input lines are parsed, and the commands push and pop are recognized. </p>
<p> The push command, then, accepts the options -d, -e, -m and -M, with the same meaning described above. Unspecified options retain the previous value and the resulting masks are used to reopen the connection with the server. pop is used to pop the connection stack. If an empty stack is popped the program exits. </p>
<p> Other commands recognized are info, used to return the stack depth; quit to prematurely terminate the program; and snapshot to get some configuration information from the server. </p>
<h2>BUGS</h2>
<p> Beginning with release 1.16, <code>mev</code> no longer works under xterm. Please use the <code>rmev</code> program (provided in the <code>sample</code> directory) to watch gpm events under xterm or rxvt. <code>rmev</code> also displays keyboard events besides mouse events. </p>
<h2>AUTHOR</h2>
<p> Alessandro Rubini &lt;rubini [at] linux.it&gt;<br />
 Ian Zimmerman &lt;itz [at] speakeasy.org&gt; </p>
<h2>FILES</h2>
<pre>
/dev/gpmctl The socket used to connect to gpm.
</pre>
<h2>SEE ALSO</h2>
<pre>
<code> <a href="//www.systutorials.com/docs/linux/man/8-gpm/">gpm</a>(8) </code>      The mouse server
<code> <a href="//www.systutorials.com/docs/linux/man/1-gpm-root/">gpm-root</a>(1) </code> An handler for Control-Mouse events.
</pre>
<p> The info file about `gpm&#8217;, which gives more complete information and explains how to write a gpm client. </p>
<h2>Index</h2>
