---
title: "xev(1)"
name: "xev"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xev/"
description: "xev – print contents of X events"
---

<h2 class="name">NAME</h2>
<p> xev &#8211; print contents of X events </p>
<h2>SYNOPSIS</h2>
<p> <code>xev</code> [-display <i>displayname</i>] [-geometry <i>geom</i>] [-bw <i>pixels</i>] [-bs <i>{NotUseful,WhenMapped,Always}</i>] [-id <i>windowid</i>] [-root] [-s] [-name <i>string</i>] [-rv] [-version] [-event <i>event_mask</i> [-event <i>event_mask</i> &#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xev</i> creates a window and then asks the X server to send it <i>events</i> whenever anything happens to the window (such as it being moved, resized, typed in, clicked in, etc.). You can also attach it to an existing window. It is useful for seeing what causes events to occur and to display the information that they contain; it is essentially a debugging and development tool, and should not be needed in normal usage.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This option specifies the X server to contact.</p>
<dt><code>-geometry </code><i>geom</i></p>
<dd> This option specifies the size and/or location of the window, if a window is to be created.</p>
<dt><code>-bw </code><i>pixels</i></p>
<dd> This option specifies the border width for the window.</p>
<dt><code>-bs </code><i>{NotUseful,WhenMapped,Always}</i></p>
<dd> This option specifies what kind of backing store to give the window. The default is NotUseful. Backing store refers to the the pixels saved off-screen when the X server maintains the contents of a window; NotUseful means that the xev process will redraw its contents itself, as necessary.</p>
<dt><code>-id </code><i>windowid</i></p>
<dd> This option specifies that the window with the given id should be monitored, instead of creating a new window.</p>
<dt><code>-root</code></p>
<dd> This option specifies that the root window should be monitored, instead of creating a new window.</p>
<dt><code>-s</code></p>
<dd> This option specifies that save-unders should be enabled on the window. Save unders are similar to backing store, but they refer rather to the saving of pixels off-screen when the current window obscures other windows. Save unders are only advisory, and are normally set for popup dialogs and other transient windows.</p>
<dt><code>-name </code><i>string</i></p>
<dd> This option specifies the name to assign to the created window.</p>
<dt><code>-rv</code></p>
<dd> This option specifies that the window should be in reverse video.</p>
<dt><code>-event </code><i>event_mask</i></p>
<dd> Select which events to display. The <code>-event</code> option can be specified multiple times to select multiple types of events. When not specified, all events are selected. Available event masks: keyboard mouse expose visibility structure substructure focus property colormap owner_grab_button randr button</p>
<dt><code>-version</code></p>
<dd> This option prints the program version and exits.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xwininfo/">xwininfo</a>(1), <a href="/docs/linux/man/1-xdpyinfo/">xdpyinfo</a>(1), Xlib Programmers Manual, X Protocol Specification<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium </p>
<h2>Index</h2>
