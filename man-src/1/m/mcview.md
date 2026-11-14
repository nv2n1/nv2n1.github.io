---
title: "mcview(1)"
name: "mcview"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcview/"
description: "mcview – Internal file viewer of GNU Midnight Commander."
---

<h2>NAME</h2>
<p> mcview &#8211; Internal file viewer of GNU Midnight Commander.</p>
<h2>USAGE</h2>
<p> <code>mcview</code> [-bcCdfhstVx?] file</p>
<h2>DESCRIPTION</h2>
<p> mcview is a link to <code>mc</code>, the main GNU Midnight Commander executable. Executing GNU Midnight Commander under this name requests staring the internal viewer and opening the <i>file</i> specified on the command line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-b</i></p>
<dd> Force black and white display.</p>
<dt><i>-c</i></p>
<dd> Force color mode on terminals where <code>mcview</code> defaults to black and white.</p>
<dt><i>-C &lt;keyword&gt;=&lt;fgcolor&gt;,&lt;bgcolor&gt;,&lt;attributes&gt;:&lt;keyword&gt;= &#8230;</i></p>
<dd> Specify a different color set. See the <code>Colors</code> section in <a href="/docs/linux/man/1-mc/">mc</a>(1) for more information.</p>
<dt><i>-d</i></p>
<dd> Disable mouse support.</p>
<dt><i>-f</i></p>
<dd> Display the compiled-in search paths for Midnight Commander files.</p>
<dt><i>-t</i></p>
<dd> Used only if the code was compiled with S-Lang and terminfo: it makes the Midnight Commander use the value of the <code>TERMCAP</code> variable for the terminal information instead of the information on the system wide terminal database</p>
<dt><i>-V</i></p>
<dd> Displays the version of the program.</p>
<dt><i>-x</i></p>
<dd> Forces xterm mode. Used when running on xterm-capable terminals (two screen modes, and able to send mouse escape sequences).</dl>
<h2>COLORS</h2>
<p> The default colors may be changed by appending to the <code>MC_COLOR_TABLE</code> environment variable. Foreground and background colors pairs may be specified for example with: </p>
<pre>
MC_COLOR_TABLE=&quot;$MC_COLOR_TABLE:\
normal=lightgray,black:\
selected=black,green&quot;
</pre>
<h2>FILES</h2>
<p> <i>/usr/share/mc/mc.hlp</i></p>
<dl>
<dt>
<dd> The help file for the program.</dl>
<p> <i>/usr/share/mc/mc.ini</i></p>
<dl>
<dt>
<dd> The default system-wide setup for GNU Midnight Commander, used only if the user&#8217;s own ~/.config/mc/ini file is missing.</dl>
<p> <i>/usr/share/mc/mc.lib</i></p>
<dl>
<dt>
<dd> Global settings for the Midnight Commander. Settings in this file affect all users, whether they have ~/.config/mc/ini or not.</dl>
<p> <i>~/.config/mc/ini</i></p>
<dl>
<dt>
<dd> User&#8217;s own setup. If this file is present, the setup is loaded from here instead of the system-wide startup file.</dl>
<h2>LICENSE</h2>
<p> This program is distributed under the terms of the GNU General Public License as published by the Free Software Foundation. See the built-in help of the Midnight Commander for details on the License and the lack of warranty.</p>
<h2>AVAILABILITY</h2>
<p> The latest version of this program can be found at <a href="ftp://ftp.gnu.org/gnu/mc/.">ftp://ftp.gnu.org/gnu/mc/.</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mc/">mc</a>(1), <a href="/docs/linux/man/1-mcedit/">mcedit</a>(1) </p>
<h2>BUGS</h2>
<p> Bugs should be reported to mc-devel [at] gnome.org </p>
<h2>Index</h2>
