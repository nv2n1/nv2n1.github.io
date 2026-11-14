---
title: "bitlbee(8)"
name: "bitlbee"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bitlbee/"
description: "BitlBee – IRC gateway to IM chat networks"
---

<p>BitlBee &#8211; IRC gateway to IM chat networks</p>
<h2>Synopsis</h2>
<p><code>bitlbee</code> [-I] [-c <i>configuration file</i>] [-d <i>configuration directory</i>] </p>
<p> <code>bitlbee</code> -D [-i <i>address</i>] [-p <i>port number</i>] [-n] [-v] [-c <i>configuration file</i>] [-d <i>configuration directory</i>] </p>
<p> <code>bitlbee</code> -h</p>
<h2>Description</h2>
<p>BitlBee is an IRC daemon that can talk to instant messaging networks and acts as a gateway. Users can connect to the server with any normal IRC client and see their &#8216;buddy list&#8217; in &amp;bitlbee. <code>bitlbee</code> should be called by <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), or you can run it as a stand-alone daemon. </p>
<h2>Options</h2>
<dl>
<dt>-I</p>
<dd>Run in <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) mode. This is the default setting, you usually don&#8217;t have to specify this option.</p>
<dt>-D</p>
<dd>Run in daemon mode. In this mode, BitlBee forks to the background and waits for new connections. All clients will be served from one process.</p>
<dt>-F</p>
<dd>Run in ForkDaemon mode. This is similar to ordinary daemon mode, but every client gets its own process. Easier to set up than inetd mode, and without the possible stability issues.</p>
<dt>-i <i>address</i></p>
<dd>Only useful when running in daemon mode, to specify the network interface (identified by IP address) to which the daemon should attach. Use this if you don&#8217;t want BitlBee to listen on every interface (which is the default behaviour).</p>
<dt>-p <i>port number</i></p>
<dd>Only useful when running in daemon mode, to specify the port number on which BitlBee should listen for connections. 6667 is the default value.</p>
<dt>-n</p>
<dd>Only useful when running in daemon mode. This option prevents BitlBee from forking into the background.</p>
<dt>-v</p>
<dd>Be more verbose. This only works together with the <code>-n</code> flag.</p>
<dt>-c <i>path to other configuration file</i></p>
<dd>Use a different configuration file.</p>
<dt>-d <i>path to user settings directory</i></p>
<dd>BitlBee normally saves every user&#8217;s settings in <code>/var/lib/bitlbee/</code>. If you want the settings to be stored somewhere else (for example, if you don&#8217;t have write permissions in the default location), use this option.</p>
<dt>-h</p>
<dd>Show help information.</dl>
<h2>Commands</h2>
<p>To get a complete list of commands, please use the <code>help commands</code> command in the &amp;bitlbee channel.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ircd/">ircd</a></code>(8), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/5-inetd-conf/">inetd.conf</a></code>(5), <code><a href="/docs/linux/man/1-gaim/">gaim</a></code>(1). </p>
<p> <code><a rel="nofollow" href="http://www.bitlbee.org/">http://www.bitlbee.org/</a></code> </p>
<p> For more information on using BitlBee, once connected, you should use the on-line help system.</p>
<h2>Bugs</h2>
<p>Of course there are bugs. If you find some, please report them at <code><a rel="nofollow" href="http://bugs.bitlbee.org/">http://bugs.bitlbee.org/</a></code>.</p>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <code>WITHOUT ANY WARRANTY</code>; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple PLace, Suite 330, Boston, MA 02111-1307 USA</p>
<h2>Authors</h2>
<p>&nbsp;<wbr>Wilmer van der Gaast&nbsp;<wbr>&lt;wilmer [at] gaast.net&gt;</p>
