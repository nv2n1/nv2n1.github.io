---
title: "iptstate(8)"
name: "iptstate"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iptstate/"
---

<b>iptstate</b> - A top-like display of IP Tables state table entries 

<h2>Synopsis</h2>

<b>iptstate </b> [&lt;<b>options</b>&gt;] 

<h2>Description</h2>

<b>iptstate</b> displays information held in the IP Tables state table in real-time in a top-like format. Output can be sorted by any field, or any field reversed. Users can choose to have the output only print once and exit, rather than the top-like system. Refresh rate is configurable, IPs can be resolved to names, output can be formatted, the display can be filtered, and color coding are among some of the many features. 

<h2>Command-Line Options</h2>

<dl><dt><b>-c, --no-color</b>
<dd>Toggle color-code by protocol
<dt><b>-C, --counters</b>
<dd>Toggle display of bytes/packets counters
<dt><b>-d, --dst-filter </b><i>IP</i>
<dd>Only show states with a destination of <i>IP</i> Note, that this must be an IP, hostname matching is not yet supported.
<dt><b>-D --dstpt-filter </b><i>port</i>
<dd>Only show states with a destination port of <i>port</i>
<dt><b>-h, --help</b>
<dd>Show help message
<dt><b>-l, --lookup</b>
<dd>Show hostnames instead of IP addresses
<dt><b>-m, --mark-truncated</b>
<dd>Mark truncated hostnames with a '+'
<dt><b>-o, --no-dynamic</b>
<dd>Toggle dynamic formatting
<dt><b>-L, --no-dns</b>
<dd>Skip outgoing DNS lookup states
<dt><b>-f, --no-loopback</b>
<dd>Filter states on loopback
<dt><b>-p, --no-scroll</b>
<dd>No scrolling (don't use a &quot;pad&quot;). See <b>SCROLLING AND PADS</b> for more information.
<dt><b>-r, --reverse</b>
<dd>Reverse sort order
<dt><b>-R, --rate </b><i>seconds</i>
<dd>Refresh rate, followed by rate in <i>seconds</i>. Note that this is for statetop mode, and not applicable for single-run mode (--single).
<dt><b>-1, --single</b>
<dd>Single run (no curses)
<dt><b>-b, --sort </b><i>column</i>
<dd>This determines what column to sort by. Options: 
 <b><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>S</b> Source Port
 
 <b><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>d</b> Destination IP (or Name)
 
 <b><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>D</b> Destination Port
 
 <b><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>p</b> Protocol
 
 <b><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>s</b> State
 
 <b><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>t</b> TTL
 
 <b><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>b</b> Bytes
 
 <b><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>P</b> Packets
 
 To sort by Source IP (or Name), don't use -b. Sorting by bytes/packets is only available for kernels that support it, and only when compiled against libnetfilter_conntrack (the default).
<dt><b>-s, --src-filter </b><i>IP</i>
<dd>Only show states with a source of <i>IP</i>. Note, that this must be an IP, hostname matching is not yet supported.
<dt><b>-S, --srcpt-filter </b><i>port</i>
<dd>Only show states with a source port of <i>port</i>
<dt><b>-t, --totals</b>
<dd>Toggle display of totals 

</dl>

<h2>Interactive Options</h2>

As of version 2.0, all command-line options are now available interactively using the same key as the short-option. For example, <b>--sort</b> is also <b>-b</b>, so while <b>iptstate</b> is running, hitting <b>b</b> will change the sorting to the next column. Similarly, <b>t</b> toggles the display of totals, and so on. 

 There are also extra interactive options: <b>B</b> - change sorting to previous column (opposite of <b>b</b>); <b>q</b> - quit; and <b>x</b> - delete the currently highlighted state from the netfilter conntrack table. 

 Additionally, the following keys are used to navigate within <b>iptstate</b>:
<dl><dt><b>Up</b> or <b>j</b> - Move up one line
<dd><dt><b>Down</b> or <b>k</b> - Move down one line
<dd><dt><b>Left</b> or <b>h</b> - Move left one column
<dd><dt><b>Right</b> or <b>l</b> - Move right one column
<dd><dt><b>PageUp</b> or <b>^u</b> - Move up one page
<dd><dt><b>PageDown</b> or <b>^d</b> - Move down one page
<dd><dt><b>Home</b> - Go to the top
<dd><dt><b>End</b> - Go to the end
<dd></dl>
 

 In many cases, <b>iptstate</b> needs to prompt you in order to change something. For example, if you want to set or change the source-ip filter, when you hit <b>s</b>, <b>iptstate</b> will pop up a prompt at the top of the window to ask you what you want to set it to. 

 Note that like many UNIX applications, ctrl-G will tell <b>iptstate</b> &quot;nevermind&quot; - it'll remove the prompt and forget you ever hit <b>s</b>. 

 In most cases, a blank response means &quot;clear&quot; - clear the source IP filter, for example. 

 At anytime while <b>iptstate</b> is running, you can hit <b>h</b> to get to the <b>interactive help</b> which will display all the current settings to you as well give you a list of all interactive commands available. 

 While running, <b>space</b> will immediately update the display. <b>Iptstate</b> should gracefully handle all window resizes, but if it doesn't, you can force it to re-calculate and re-draw the screen with a <b>ctrl-L</b>.

<h2>Scrolling And Pads</h2>

For almost any user, there is no reason to turn off scrolling. The ability to turn this off - and especially the ability to toggle this interactively - is done more for theoretical completeness than anything else.
<dl><dt>But, nonetheless, here are the details. Typically in a curses application you create a &quot;window.&quot; Windows don't scroll, however. They are, at most, the size of your terminal. Windows provide double-buffering to make refreshing as fast and seemless as possible. However, to enable scrolling, one has to use &quot;pads&quot; instead of windows. Pads can be bigger than the current terminal. Then all necessary data is written to the pad, and &quot;scrolling&quot; becomes a function of just showing the right part of that pad on the screen.
<dd><dt>However, pads do not have the double-buffering feature that windows have. Thus, there _might_ be some case where for some user using some very strange machine, having scrolling enabled could cause poor refreshing. Given the nature of the way <b>iptstate</b> uses the screen though, I find this highly unlikely. In addition, the scrolling method uses a little more memory. However, <b>iptstate</b> is not a memory intensive application, so this shouldn't be a problem even on low-memory systems.
<dd><dt>Nonetheless, if this does negatively affect you, the option to turn it off is there.
<dd></dl>

<h2>Exit Status</h2>

Anything other than 0 indicates and error. A list of current exit statuses are below:
<dl><dt><b>0</b>
<dd>Success
<dt><b>1</b>
<dd>Bad command-line arguments
<dt><b>2</b>
<dd>Error communicating with the netfilter subsystem.
<dt><b>3</b>
<dd>Terminal too narrow 

</dl>

<h2>Bugs</h2>

We don't support filtering on resolved names, and we don't support filtering on networks. IPv6 support is new and the dynamic formatting doesn't yet always handle IPv6 addresses as well as it should. 

<h2>Bug Reports</h2>

All bugs should be reported to Phil Dibowitz &lt;phil AT ipom DOT com&gt;. Please see the <b>README</b> and <b>BUGS</b> for more information on bug reports. Please read the <b>WISHLIST</b> before sending in features you hope to see.

<h2>Notes</h2>

<b>iptstate</b> does a lot of work to try to fit everything on the screen in an easy-to-read way. However, in some cases, hostnames may need to be truncated (in lookup mode). Similarly, IPv6 addresses may need to be truncated. The truncation of names happens from the right for source because you most likely know your own domain name, and from the left for destination because knowing your users are connection to &quot;mail.a.&quot; doesn't help much. However, for addresses, this is reversed. <b>iptstate</b> does not automatically handle window-resizes while in the <b>interactive help</b> screen. If you do resize while in this window, you should return to the main window, hit <b>ctrl-L</b> to re-calculate and re-draw the screen, and then, if you choose, return to the <b>interactive help</b>. <b>iptstate</b> currently uses libnetfilter_conntrack to access the netfilter connection state table. However, older versions read out of /proc/net/ip_conntrack, and the current version can still be compiled to do this. This deprecated method can be racy on SMP systems, and can hurt performance on very heavily loaded firewalls. This deprecated method should be avoided - support will be removed in future versions. 

<h2>See Also</h2>

<b><a HREF="/docs/linux/man/8-iptables/">iptables</a></b>(8) 

<h2>Author</h2>

<b>iptstate</b> was written by Phil Dibowitz &lt;phil AT ipom DOT com&gt; 
 <a rel="nofollow" HREF="http://www.phildev.net/iptstate/">http://www.phildev.net/iptstate/</a>
