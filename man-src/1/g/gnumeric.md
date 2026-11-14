---
title: "gnumeric(1)"
name: "gnumeric"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnumeric/"
description: "gnumeric – a GNOME spreadsheet application."
---

<h2 class="name">NAME</h2>
<p> gnumeric &#8211; a GNOME spreadsheet application.</p>
<h2>SYNOPSIS</h2>
<p> <code>gnumeric</code> [<i>OPTIONS</i>] [<i>files</i> <i>&#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>Gnumeric</code> is a powerful spreadsheet program created by the GNOME project. <code>Gnumeric</code> intends to compete with commercial spreadsheets by becoming fully compatible with Microsoft Excel(TM) and through the support of most popular spreadsheet file formats such as Excel(TM), Lotus 1-2-3(TM), Applix(TM), Sylk(TM), XBase(TM), Oleo(TM) and OpenOffice.org formats. </p>
<p> <code>Gnumeric</code> supports advanced calculations using statistical, financial and database access functions. Plotting data is supported through an incomplete but powerful plotting system. A plugin system extends <code>gnumeric</code> , for instance enabling the export of data to the LaTeX \longtable format. Plugins can be used to define custom functionality. A rudimentary scripting API for the Python language exists and will be extended in the near future. Since <code>gnumeric</code> is <code>free</code> software, <code>gnumeric</code> can also be extended directly at the source code level by any competent programmer. </p>
<p> The program can be started from the command line as <code>gnumeric</code> or from one of the menus provided by the underlying platform. When started on the command line, <code>gnumeric</code> may be followed by the options listed below and possibly the names of files in various spreadsheet formats which will then be opened immediately. For instance, the command: </p>
<p>&nbsp;<wbr>gnumeric myfile.gnumeric </p>
<p> will launch <code>gnumeric</code> and open the file called &quot;myfile.gnumeric&quot;. The default <code>gnumeric</code> file format is in extensible markup language (XML) which subsequently has been compressed with <code>gzip</code>. </p>
<h2>USER OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with single letter options starting with a single dash (`-&#8216;) and longer options starting with two dashes (`&#8211;&#8216;). </p>
<h3>Help options</h3>
<p> <code>-?, &#8211;help</code> Show help message.</p>
<dl>
<dt><code>&#8211;usage</code></p>
<dd> Displays a brief usage message. </p>
</dl>
<h3>Gnumeric options</h3>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Displays the version number of the installed instance of <code>gnumeric</code>.</p>
<dt><code>&#8211;no-splash</code></p>
<dd> Start <code>gnumeric</code> without showing the splash screen. The splash screen is normally shown if loading files takes too long.</p>
<dt><code>-L, &#8211;lib-dir=</code><i>STRING</i></p>
<dd> Set the root library directory to STRING which should be a pathname.</p>
<dt><code>-D, &#8211;data-dir=</code><i>STRING</i></p>
<dd> Adjust the root data directory to STRING which should be a pathname. </p>
</dl>
<h3>Options for window placement</h3>
<dl>
<dt><code>-g, &#8211;geometry=WIDTHxHEIGHT+XOFF+YOFF</p>
<dd> Set the size and position of the first window. All units are in pixels. The X offset is from the left hand side of the screen, the Y offset is from the top of the screen. For example, -g=800&#215;600+20+30 will open a gnumeric window 800 pixels wide by 600 pixels high, with the left edge of gnumeric 20 pixels from the left of the screen and the top edge of gnumeric 30 pixels from the top of the screen.</p>
<dt>&#8211;display=</code><i>DISPLAY</i></p>
<dd> X display to use, where DISPLAY has the form machinename:Xdisplay.Screen. Note that the machine displaying gnumeric must have granted the machine running gnumeric the right to display (see xhost). </p>
<dt><code>&#8211;screen=</code><i>SCREEN</i></p>
<dd> X screen to use, a more compact form of the functionality described above. </p>
</dl>
<h2>ADVANCED OPTIONS</h2>
<h3>GNOME options</h3>
<dl>
<dt><code>&#8211;disable-sound</code></p>
<dd> Disable sound server usage.</p>
<dt><code>&#8211;enable-sound</code></p>
<dd> Enable sound server usage.</p>
<dt><code>&#8211;espeaker=</code><i>HOSTNAME:PORT</i></p>
<dd> Host:port on which the sound server to use is running.</p>
<dt><code>&#8211;disable-crash-dialog</code></p>
<dd> Disable the bug submission dialog which appears if Gnumeric crashes. </p>
</dl>
<h3>GTK options</h3>
<dl>
<dt><code>&#8211;gdk-debug=</code><i>FLAGS</i></p>
<dd> Gdk debugging flags to set.</p>
<dt><code>&#8211;gdk-no-debug=</code><i>FLAGS</i></p>
<dd> Gdk debugging flags to unset.</p>
<dt><code>&#8211;sync</code></p>
<dd> Make X calls synchronous.</p>
<dt><code>&#8211;name=</code><i>NAME</i></p>
<dd> Program name as used by the window manager.</p>
<dt><code>&#8211;class=</code><i>CLASS</i></p>
<dd> Program class as used by the window manager.</p>
<dt><code>&#8211;gxid_host=</code><i>HOST</i></p>
<dd> The host on which to contact the gxid daemon. This overrides the GXID_HOST environment variable. This option is only available if GTK+ has been configured with &#8211;gdk-target=x11.</p>
<dt><code>&#8211;gxid_port=</code><i>PORT</i></p>
<dd> The port for the connection to gxid. This overrides the GXID_PORT environment variable. This option is only available if GTK+ has been configured with &#8211;gdk-target=x11.</p>
<dt><code>&#8211;gtk-debug=</code><i>FLAGS</i></p>
<dd> Gtk+ debugging flags to set.</p>
<dt><code>&#8211;gtk-no-debug=</code><i>FLAGS</i></p>
<dd> Gtk+ debugging flags to unset.</p>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd> Make all warnings fatal.</p>
<dt><code>&#8211;gtk-module=</code><i>MODULE</i></p>
<dd> Load an additional Gtk module. </p>
</dl>
<h3>Session management options</h3>
<dl>
<dt><code>&#8211;sm-client-id=</code><i>ID</i></p>
<dd> Specify session management ID.</p>
<dt><code>&#8211;sm-config-prefix=</code><i>PREFIX</i></p>
<dd> Specify prefix of saved configuration.</p>
<dt><code>&#8211;sm-disable</code></p>
<dd> Disable connection to session manager. </p>
</dl>
<h2>VERSION</h2>
<p> This manual page describes <code>gnumeric</code> version 1.8. </p>
<h2>BUGS</h2>
<p> For the list of known <code>gnumeric</code> bugs, or to report new ones please visit <i><a rel="nofollow" href="http://bugzilla.gnome.org">http://bugzilla.gnome.org</a></i>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ssconvert/">ssconvert</a></code>(1), <code><a href="/docs/linux/man/1-ssindex/">ssindex</a></code>(1), <code><a href="/docs/linux/man/1-ssdiff/">ssdiff</a></code>(1) <code><a href="/docs/linux/man/1-ssgrep/">ssgrep</a></code>(1) </p>
<p> <code>The Gnumeric Manual</code> Available through the <code>Help</code> menu or online &lt;URL: <a rel="nofollow" href="http://www.gnome.org/projects/gnumeric/doc/gnumeric.shtml">http://www.gnome.org/projects/gnumeric/doc/gnumeric.shtml</a> &gt;. </p>
<p> The Gnumeric Homepage &lt;URL: <a rel="nofollow" href="http://www.gnome.org/projects/gnumeric/">http://www.gnome.org/projects/gnumeric/</a> &gt;. </p>
<p> The GNOME project page &lt;URL: <a rel="nofollow" href="http://www.gnome.org/">http://www.gnome.org/</a> &gt;. </p>
<h2>LICENSE</h2>
<p> <code>Gnumeric</code> is licensed under the terms of the General Public License (GPL), version 2 or 3. For information on this license look at the source code that came with the software or see the GNU project page &lt;URL: <a rel="nofollow" href="http://www.gnu.org/">http://www.gnu.org/</a> &gt;. </p>
<h2>COPYRIGHT</h2>
<p> The copyright on the <code>gnumeric</code> software and source code is held by the individual authors as is documented in the source code. </p>
<h2>AUTHORS</h2>
<h3>Gnumeric</h3>
<p> Jody Goldberg &lt;jody [at] gnome.org&gt;<br />
 Miguel de Icaza &lt;miguel [at] gnome.org&gt;<br />
 Morten Welinder &lt;terra [at] gnome.org&gt; </p>
<p> &#8212; and many others. For a more complete list, see the About dialog.</p>
<h3>This manual page</h3>
<p> Jan Schaumann &lt;jschauma [at] netmeister.org&gt;<br />
 Adrian Custer &lt;acuster [at] gnome.org&gt; </p>
<h2>Index</h2>
