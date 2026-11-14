---
title: "nload(1)"
name: "nload"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nload/"
description: "nload – displays the current network usage"
---

<h2>NAME</h2>
<p> nload &#8211; displays the current network usage </p>
<h2>SYNOPSIS</h2>
<p> <code>nload</code> [<code>-a</code> <i>period</i>] [<code>-i</code> <i>max_scaling</i>] [<code>-m</code>] [<code>-o</code> <i>max_scaling</i>] [<code>-t</code> <i>interval</i>] [<code>-u</code> <i>h|H|b|B|k|K|m|M|g|G</i>] [<code>-U</code> <i>h|H|b|B|k|K|m|M|g|G</i>] [<i>devices</i>] </p>
<p> <code>nload &#8211;help|-h</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>nload</code> is a console application which monitors network traffic and bandwidth usage in real time. It visualizes the in- and outgoing traffic using two graphs and provides additional info like the total amount of transfered data and min/max network usage. </p>
<h2>USAGE</h2>
<p> When running <code>nload,</code> you can switch between the devices (which you gave <code>nload</code> either on the command line or which were auto-detected) by pressing the left and right arrow keys. If the <code>-m</code> command line parameter is given, the arrow keys switch as many devices back and forth as there are shown on the screen. If you want to quit, do so by pressing &#8216;q&#8217; or &#8216;Ctrl+C&#8217;. </p>
<p> For further key shortcuts, have a look at the sections <code>MAIN WINDOW</code> and <code>OPTION WINDOW</code> below. </p>
<h2>OPTIONS</h2>
<p> A summary of the options supported by <code>nload</code> is included below. </p>
<dl>
<dt><code>-a period</code></p>
<dd> Sets the length in seconds of the time window for average calculation. The default is 300.</p>
<dt><code>-i max_scaling</code></p>
<dd> Specifies the 100% mark in kBit/s of the graph indicating the incoming bandwidth usage. Ignored if max_scaling is 0 or the switch -m is given. The default value for max_scaling is 10240.</p>
<dt><code>-m</code></p>
<dd> Show multiple devices at a time; do not show the traffic graphs.</p>
<dt><code>-o max_scaling</code></p>
<dd> Same as -i but for the graph indicating the outgoing bandwidth usage.</p>
<dt><code>-t interval</code></p>
<dd> Determines the refresh interval of the display in milliseconds. The default value of interval is 500. </p>
<p> PLEASE NOTE: Specifying refresh intervals shorter than about 100 milliseconds makes traffic calculation very unprecise. Also the display may flicker using such short refresh intervals. <code>nload</code> tries to balance this out by doing extra time measurements, but this may not always succeed.</p>
<dt><code>-u h|H|b|B|k|K|m|M|g|G</code></p>
<dd> Sets the type of unit used for the display of traffic numbers. h means human readable (auto), b Bit/s, k kBit/s, m MBit/s and g GBit/s. The upper case letters mean the corresponding units in Bytes (instead of Bits). The default is k.</p>
<dt><code>-U h|H|b|B|k|K|m|M|g|G</code></p>
<dd> Same as -u, but for an amount of data, e.g. Bit, kByte, GBit etc. (without &quot;/s&quot;). The default is M.</p>
<dt><code>devices</code></p>
<dd> Network devices to use. The default is &quot;all&quot;, which means to display all auto-detected devices.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a short summary of these command line options. </p>
</dl>
<h2>MAIN WINDOW</h2>
<p> After starting, <code>nload</code> begins to monitor the network devices given on the command line, or, if none where specified, the default device. In this mode, the following key shortcuts are available. </p>
<dl>
<dt><code>&#8216;ArrowRight&#8217;, &#8216;ArrowDown&#8217;, &#8216;PageDown&#8217;, &#8216;Enter&#8217;, &#8216;Tab&#8217;</code></p>
<dd> Switch the display to the next network device, or, when started with the <code>-m</code> flag, to the next page of devices. </p>
<dt><code>&#8216;ArrowLeft&#8217;, &#8216;ArrowUp&#8217;, &#8216;PageUp&#8217;</code></p>
<dd> Switch the display to the previous network device, or, when started with the <code>-m</code> flag, to the previous page of devices. </p>
<dt><code>&#8216;F2&#8217;</code></p>
<dd> Show the option window (see section <code>OPTION WINDOW</code> below). </p>
<dt><code>&#8216;F5&#8217;</code></p>
<dd> Save current settings to the user&#8217;s config file. </p>
<dt><code>&#8216;F6&#8217;</code></p>
<dd> Reload settings from the config files. </p>
<dt><code>&#8216;q&#8217;, &#8216;Ctrl+C&#8217;</code></p>
<dd> Quit <code>nload</code>. </p>
</dl>
<h2>OPTION WINDOW</h2>
<p> The parameters given to <code>nload</code> on the command line can be adjusted during run time by pressing the &#8216;F2&#8217; key. A small window appears on the top of the screen, listing the available settings. </p>
<dl>
<dt><code>&#8216;F2&#8217;</code></p>
<dd> Show/hide the option window. </p>
<dt><code>&#8216;ArrowLeft&#8217;, &#8216;ArrowRight&#8217;, &#8216;Home&#8217;, &#8216;End&#8217;</code></p>
<dd> Navigate within the edit fields. </p>
<dt><code>&#8216;ArrowUp&#8217;, &#8216;ArrowDown&#8217;, &#8216;Enter&#8217;</code></p>
<dd> Navigate between the settings. </p>
<dt><code>&#8216;PageUp&#8217;, &#8216;PageDown&#8217;, &#8216;Tab&#8217;</code></p>
<dd> Toggle between the different values possible for the current field. </p>
<dt><code>&#8216;+&#8217; / &#8216;-&#8216;</code></p>
<dd> Switch to the next / previous page of settings. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/nload.conf</i></p>
<dd> System-wide configuration file. </p>
<dt><i>$(HOME)/.nload</i></p>
<dd> User-specific configuration file (overrides system-wide settings). </p>
<dt><i>/sys/class/net/*/* /proc/net/dev</i></p>
<dd> are read by <code>nload</code> when running on Linux to get the network traffic data. </p>
</dl>
<h2>VERSION</h2>
<p> This manual page describes version 0.7.4 of <code>nload</code>. </p>
<p> For updates, look at the nload homepage:<br />
 <code><a rel="nofollow" href="http://www.roland-riegel.de/nload/">http://www.roland-riegel.de/nload/</a></code> </p>
<h2>HELP</h2>
<p> If you need help, either contact me directly (see below) or write to the nload-user mailing list at<br />
 <code>nload-user [at] lists.sourceforge.net</code><br />
 after having subscribed at<br />
 <code><a rel="nofollow" href="https://lists.sourceforge.net/lists/listinfo/nload-user">https://lists.sourceforge.net/lists/listinfo/nload-user</a></code>. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2001 &#8211; 2012 Roland Riegel &lt;feedback [at] roland-riegel.de&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place &#8211; Suite 330, Boston, MA 02111-1307, USA. </p>
<h2>Index</h2>
