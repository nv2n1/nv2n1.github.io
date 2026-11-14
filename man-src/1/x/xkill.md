---
title: "xkill(1)"
name: "xkill"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xkill/"
description: "xkill – kill a client by its X resource"
---

<h2 class="name">NAME</h2>
<p> xkill &#8211; kill a client by its X resource </p>
<h2>SYNOPSIS</h2>
<p> <code>xkill</code> [-display <i>displayname</i>] [-id <i>resource</i>] [-button number] [-frame] [-all] [-version]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xkill</i> is a utility for forcing the X server to close connections to clients. This program is very dangerous, but is useful for aborting programs that have displayed undesired windows on a user&#8217;s screen. If no resource identifier is given with <i>-id</i>, <i>xkill</i> will display a special cursor as a prompt for the user to select a window to be killed. If a pointer button is pressed over a non-root window, the server will close its connection to the client that created the window.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>displayname</i></p>
<dd> This option specifies the name of the X server to contact.</p>
<dt><code>-id </code><i>resource</i></p>
<dd> This option specifies the X identifier for the resource whose creator is to be aborted. If no resource is specified, <i>xkill</i> will display a special cursor with which you should select a window to be kill.</p>
<dt><code>-button </code><i>number</i></p>
<dd> This option specifies the number of pointer button that should be used in selecting a window to kill. If the word &quot;any&quot; is specified, any button on the pointer may be used. By default, the first button in the pointer map (which is usually the leftmost button) is used.</p>
<dt><code>-all</code></p>
<dd> This option indicates that all clients with top-level windows on the screen should be killed. <i>Xkill</i> will ask you to select the root window with each of the currently defined buttons to give you several chances to abort. Use of this option is highly discouraged.</p>
<dt><code>-frame</code></p>
<dd> This option indicates that xkill should ignore the standard conventions for finding top-level client windows (which are typically nested inside a window manager window), and simply believe that you want to kill direct children of the root.</p>
<dt><code>-version</code></p>
<dd> This option makes xkill print its version and exit without killing anything.</dl>
<h2>CAVEATS</h2>
<p> This command does not provide any warranty that the application whose connection to the X server is closed will abort nicely, or even abort at all. All this command does is to close the connection to the X server. Many existing applications do indeed abort when their connection to the X server is closed, but some can choose to continue.</p>
<h2>XDEFAULTS</h2>
<dl>
<dt><code>Button</code></p>
<dd> Specifies a specific pointer button number or the word &quot;any&quot; to use when selecting windows.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xwininfo/">xwininfo</a>(1), <a href="/docs/linux/man/3-xkillclient/">XKillClient</a>(3), <a href="/docs/linux/man/3-xgetpointermapping/">XGetPointerMapping</a>(3), KillClient in the X Protocol Specification</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium<br />
 Dana Chee, Bellcore </p>
<h2>Index</h2>
