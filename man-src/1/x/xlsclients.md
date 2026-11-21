---
title: "xlsclients(1)"
name: "xlsclients"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xlsclients/"
description: "xlsclients – list client applications running on a display"
---

<h2>SYNOPSIS</h2>
<p> <code>xlsclients</code> [-display <i>displayname</i>] [-a] [-l] [-m maxcmdlen] [-version]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xlsclients</i> is a utility for listing information about the client applications running on a display. It may be used to generate scripts representing a snapshot of the user&#8217;s current session.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>displayname</i></dt>
<dd> This option specifies the X server to contact.</dd>
<dt><code>-a</code></dt>
<dd> This option indicates that clients on all screens should be listed. By default, only those clients on the default screen are listed.</dd>
<dt><code>-l</code></dt>
<dd> List in long format, giving the window name, icon name, and class hints in addition to the machine name and command string shown in the default format.</dd>
<dt><code>-m </code><i>maxcmdlen</i></dt>
<dd> This option specifies the maximum number of characters in a command to print out. The default is 10000.</dd>
<dt><code>-version</code></dt>
<dd> Print the program version and exit.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></dt>
<dd> To get the default host, display number, and screen.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xwininfo/">xwininfo</a>(1), <a href="/docs/linux/man/1-xprop/">xprop</a>(1)</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium </p>
