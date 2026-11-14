---
title: "ghex(1)"
name: "ghex"
section: "1"
letter: "g"
url: "/docs/linux/man/1-ghex/"
description: "ghex – A GNOME Hex Editor"
---

<h2 class="name">NAME</h2>
<p> ghex &#8211; A GNOME Hex Editor </p>
<h2>SYNOPSIS</h2>
<p> <code>ghex</code> [<i>options</i>]<i> files</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>ghex</code> command. This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page. Instead, it has documentation in the GNOME help system. </p>
<p> <code>ghex</code> allows the user to load data from any file, view and edit it in either hex or ascii. A must for anyone playing games that use non-ascii format for saving.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> Usage: ghex [OPTION&#8230;] </p>
<p> GNOME options<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;disable-sound&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Disable sound server usage<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;enable-sound&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Enable sound server usage<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;espeaker=HOSTNAME:PORT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Host:port on which the sound server to use is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>running<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;version </p>
<p> Help options<br />
&nbsp;<wbr>&nbsp;<wbr>-?, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show this help message<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display brief usage message </p>
<p> GTK options<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;gdk-debug=FLAGS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Gdk debugging flags to set<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;gdk-no-debug=FLAGS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Gdk debugging flags to unset<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;display=DISPLAY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X display to use<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;sync&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Make X calls synchronous<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-xshm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t use X shared memory extension<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;name=NAME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Program name as used by the window manager<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;class=CLASS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Program class as used by the window manager<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;gxid_host=HOST<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;gxid_port=PORT<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;xim-preedit=STYLE<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;xim-status=STYLE<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;gtk-debug=FLAGS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Gtk+&nbsp;<wbr>debugging flags to set<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;gtk-no-debug=FLAGS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Gtk+&nbsp;<wbr>debugging flags to unset<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;g-fatal-warnings&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Make all warnings fatal<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;gtk-module=MODULE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Load an additional Gtk module </p>
<p> GNOME GUI options<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;disable-crash-dialog </p>
<p> Session management options<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;sm-client-id=ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specify session management ID<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;sm-config-prefix=PREFIX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specify prefix of saved configuration<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;sm-disable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Disable connection to session manager </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Eric Gillespie, Jr. &lt;epg [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
