---
title: "xkbevd(1)"
name: "xkbevd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xkbevd/"
description: "xkbevd – XKB event daemon"
---

<h2 class="name">NAME</h2>
<p> xkbevd &#8211; XKB event daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>xkbevd</code> [ options ]</p>
<h2>DESCRIPTION</h2>
<p> This command is very raw and is therefore only partially implemented; we present it here as a rough prototype for developers, not as a general purpose tool for end users. Something like this might make a suitable replacement for xev; I&#8217;m not signing up, mind you, but it&#8217;s an interesting idea. </p>
<p> The <i>xkbevd</i> event daemon listens for specified XKB events and executes requested commands if they occur. The configuration file consists of a list of event specification/action pairs and/or variable definitions. </p>
<p> An event specification consists of a short XKB event name followed by a string or identifier which serves as a qualifier in parentheses; empty parenthesis indicate no qualification and serve to specify the default command which is applied to events which do not match any of the other specifications. The interpretation of the qualifier depends on the type of the event: Bell events match using the name of the bell, message events match on the contents of the message string and slow key events accept any of <i>press</i>, <i>release</i>, <i>accept</i>, or <i>reject</i>. No other events are currently recognized. </p>
<p> An action consists of an optional keyword followed by an optional string argument. Currently, <i>xkbev</i> recognizes the actions: <i>none</i>, <i>ignore</i>, <i>echo</i>, <i>printEvent</i>, <i>sound</i>, and <i>shell</i>. If the action is not specified, the string is taken as the name of a sound file to be played unless it begins with an exclamation point, in which case it is taken as a shell command. </p>
<p> Variable definitions in the argument string are expanded with fields from the event in question before the argument string is passed to the action processor. The general syntax for a variable is either $<i>c</i> or $(<i>str</i>), where <i>c</i> is a single character and <i>str</i> is a string of arbitrary length. All parameters have both single-character and long names. </p>
<p> The list of recognized parameters varies from event to event and is too long to list here right now. This is a developer release anyway, so you can be expected to look at the source code (evargs.c is of particular interest). </p>
<p> The <i>ignore</i>, <i>echo</i>, <i>printEvent</i>, <i>sound</i>,and <i>shell</i> actions do what you would expect commands named <i>ignore</i>, <i>echo</i>, <i>printEvent</i>, <i>sound</i>, and <i>shell</i> to do, except that the sound command has only been implemented and tested for SGI machines. It launches an external program right now, so it should be pretty easy to adapt, especially if you like audio cues that arrive about a half-second after you expect them. </p>
<p> The only currently recognized variables are <i>soundDirectory</i> and <i>soundCmd</i>. I&#8217;m sure you can figure out what they do.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Prints a usage message that is far more up-to-date than anything in this man page.</p>
<dt><code>-cfg </code><i>file</i></p>
<dd> Specifies the configuration file to read. If no configuration file is specified, <i>xkbevd</i> looks for ~/.xkb/xkbevd.cf and $(LIBDIR)/xkb/xkbevd.cf in that order.</p>
<dt><code>-sc&nbsp;</code><i>cmd</i></p>
<dd> Specifies the command used to play sounds.</p>
<dt><code>-sd&nbsp;</code><i>directory</i></p>
<dd> Specifies a top-level directory for sound files.</p>
<dt><code>-display&nbsp;</code><i>display</i></p>
<dd> Specifies the display to use. If not present, <i>xkbevd</i> uses $DISPLAY.</p>
<dt><code>-bg</code></p>
<dd> Tells <i>xkbevd</i> to fork itself (and run in the background).</p>
<dt><code>-synch</code></p>
<dd> Forces synchronization of all X requests. Slow.</p>
<dt><code>-v</code></p>
<dd> Print more information, including debugging messages. Multiple specifications of <i>-v</i> cause more output, to a point.</p>
<dt><code>-version</code></p>
<dd> Prints the program version and exits.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xev/">xev</a></code>(1), <code><a href="/docs/linux/man/1-xkbwatch/">xkbwatch</a></code>(1), <code><a href="/docs/linux/man/7-x/">X</a></code>(7).</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1995, Silicon Graphics Computer Systems<br />
 Copyright 1995, 1998 The Open Group<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Erik Fortune, Silicon Graphics </p>
<h2>Index</h2>
