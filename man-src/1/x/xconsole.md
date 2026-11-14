---
title: "xconsole(1)"
name: "xconsole"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xconsole/"
description: "xconsole – monitor system console messages with X"
---

<h2 class="name">NAME</h2>
<p> xconsole &#8211; monitor system console messages with X </p>
<h2>SYNOPSIS</h2>
<p> <code>xconsole</code> [-<i>toolkitoption</i> &#8230;] [-file <i>file-name</i>] [-notify] [-stripNonprint] [-daemon] [-verbose] [-exitOnFail]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xconsole</i> program displays messages which are usually sent to /dev/console.</p>
<h2>OPTIONS</h2>
<p> <i>Xconsole</i> accepts all of the standard X Toolkit command line options along with the additional options listed below:</p>
<dl>
<dt><code>-file </code><i>file-name</i></p>
<dd> To monitor some other device, use this option to specify the device name. This does not work on regular files as they are always ready to be read from.</p>
<dt><code>-notify -nonotify</code></p>
<dd> When new data are received from the console and the notify option is set, the icon name of the application has &quot; *&quot; appended, so that it is evident even when the application is iconified. -notify is the default.</p>
<dt><code>-daemon</code></p>
<dd> This option causes <i>xconsole</i> to place itself in the background, using fork/exit.</p>
<dt><code>-verbose</code></p>
<dd> When set, this option directs <i>xconsole</i> to display an informative message in the first line of the text buffer.</p>
<dt><code>-exitOnFail</code></p>
<dd> When set, this option directs <i>xconsole</i> to exit when it is unable to redirect the console output.</p>
<dt><code>-saveLines </code><i>count</i></p>
<dd> When set, <i>xconsole</i> only preserves <i>count</i> lines of message history instead of growing the text buffer without bound (a <i>count</i> of zero &#8211; the default &#8211; is treated as placing no limit on the history).</dl>
<h2>X DEFAULTS</h2>
<p> This program uses the <i>Athena Text</i> widget, look in the <i>Athena Widget Set</i> documentation for controlling it. </p>
<p> <i>Xconsole</i> otherwise accepts resources of the same names as the command-line options (without the leading dash). &quot;file&quot; is a string type, &quot;saveLines&quot; an integer, and the remaining options are booleans.</p>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which compose <i>xconsole</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
XConsole  xconsole
     XConsole  text
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/X11/app-defaults/XConsole</i></p>
<dd> specifies required resources</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), Athena Text widget</p>
<h2>AUTHOR</h2>
<p> Keith Packard (MIT X Consortium) </p>
<h2>Index</h2>
