---
title: "pptpd(8)"
name: "pptpd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pptpd/"
description: "pptpd – PPTP VPN daemon"
---

<p>pptpd &#8211; PPTP VPN daemon</p>
<h2>Synopsis</h2>
<p><code>pptpd</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p><code>pptpd</code> is the Poptop PPTP daemon, which manages tunnelled PPP connections encapsulated in GRE using the PPTP VPN protocol. It may contain features like IP address management and TCP wrappers if compiled in.</p>
<h2>Options</h2>
<p>Here we document the command line options. See <code><a href="/docs/linux/man/5-pptpd-conf/">pptpd.conf</a></code>(5) for configuration directives, IP address allocation, routing, and firewall rules. </p>
<dl>
<dt><code>-b</code>|<code>&#8211;bcrelay </code><i>internal-interface</p>
<dd>specifies that broadcasts received on the server&#8217;s internal network interface should be relayed to the clients. </p>
<dt></i><code>-c</code>|<code>&#8211;conf </code><i>conf-file</p>
<dd>specifies the configuration file for </i><code>pptpd</code> (default <i>/etc/pptpd.conf</i>) </p>
<dt><code>-d</code>|<code>&#8211;debug</code></p>
<dd>turns on debugging mode, causing more debugging messages to be sent to syslog. </p>
<dt><code>-e</code>|<code>&#8211;ppp </code><i>pppd-program</p>
<dd>use pppd-program</i> in place of the default <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8). </p>
<dt><code>-f</code>|<code>&#8211;fg</code></p>
<dd>run in the foreground instead of detaching from terminal </p>
<dt><code>-h</code>|<code>&#8211;help</code></p>
<dd>display program usage. </p>
<dt><code>-i</code>|<code>&#8211;noipparam</code></p>
<dd>do not send the client&#8217;s IP address to ip-up scripts (required if you are using the <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) <i>ipparam</i> option for some other purpose). </p>
<dt><code>-l</code>|<code>&#8211;listen </code><i>x.x.x.x</p>
<dd>specifies the local interface IP address to listen on. </p>
<dt></i><code>-o</code>|<code>&#8211;option </code><i>ppp-conf-file</p>
<dd>specifies that pptpd should specify an alternate configuration file for the ppp daemon (the default is normally /etc/ppp/options</i> but may vary depending on your ppp daemon). </p>
<dt><code>-p</code>|<code>&#8211;pidfile </code><i>pid-file</p>
<dd>specifies an alternate location to store the process ID file (default /var/run/pptpd.pid</i>). </p>
<dt><code>-s</code>|<code>&#8211;speed </code><i>baud</p>
<dd>specifies that the speed baud</i> should be passed to the ppp daemon as the tty speed to use (in some cases this is ignored by the ppp daemon). </p>
<dt><code>-t</code>|<code>&#8211;stimeout </code><i>seconds</p>
<dd>specifies the number of seconds to wait for the first packet before dropping the connection. This is a denial of service protection feature. </p>
<dt></i><code>-w</code>|<code>&#8211;logwtmp</code></p>
<dd>update <code><a href="/docs/linux/man/5-wtmp/">wtmp</a></code>(5) as users connect and disconnect. See <code><a href="/docs/linux/man/1-wtmp/">wtmp</a></code>(1). </p>
<dt><code>-C</code>|<code>&#8211;connections </code><i>n</p>
<dd>limits the number of client connections that may be accepted. Corresponds to the </i><code>connections</code> option in <i>pptpd.conf</i>. If pptpd is allocating IP addresses (e.g. <code>&#8211;delegate</code> is not used) then the number of connections is also limited by the <code>remoteip</code> option in <i>pptpd.conf</i>. </p>
<dt><code>-D</code>|<code>&#8211;delegate</code></p>
<dd>delegates the allocation of client IP addresses to <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8). Without this option, which is the default, pptpd manages the list of IP addresses for clients and passes the next free address to pppd. With this option, pptpd does not pass an address, and so pppd may use radius or chap-secrets to allocate an address. </p>
<dt><code>-V</code>|<code>&#8211;vrf </code><i>vrf-name</p>
<dd>specifies the VRF to be used for listening in. </p>
<dt></i><code>-v</code>|<code>&#8211;version</code></p>
<dd>displays the current version of the pptp daemon. </p>
</dl>
<h2>Files</h2>
<p>/etc/pptpd.conf<br />
 /var/run/pptpd.pid</p>
<h2>Debugging</h2>
<p>To turn on debugging, add &#8216;debug&#8217; to /etc/pptpd.conf and your PPP options file, and restart pptpd. </p>
<p> Typically the PPP options file is options.pptpd in /etc/ppp, though on some distributions it may be pptpd-options. Use your package manager to find it, e.g. &#8216;rpm -ql pptpd | grep options&#8217; or &#8216;dpkg &#8211;listfiles pptpd | grep options&#8217;. </p>
<p> You may need to configure syslogd to catch debug messages. e.g. edit /etc/syslog.conf and add something similar to the example below, then restart syslogd. </p>
<p> # debug logging<br />
 *.debug;mail.none /var/log/debug </p>
<p> This will log all debug information, except mail, to the file /var/log/debug. Note that this is a lot of information and might flood your disks. If performance is an issue, you can try turning off sync during your debugging, by prefixing the destination with &#8216;-&#8216;. </p>
<p> # debug logging<br />
 *.debug;mail.none -/var/log/debug </p>
<p> Disable this line and restart syslog after you are done debugging. See the syslog man pages for more details.</p>
<h2>Authors</h2>
<p>Poptop is written by Matthew Ramsay &lt;matthewr [at] moreton.com.au&gt;, David Luyer &lt;luyer [at] ucs.uwa.edu.au&gt;, Kevin Thayer &lt;tmk [at] netmagic.net&gt;, Peter Galbavy &lt;Peter.Galbavy [at] knowledge.com&gt; and others. Development has been moved to SourceForge and worked on by Richard de Vroede &lt;r.devroede [at] linvision.com&gt; since June 26, 2002.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 1999 Matthew Ramsay and others. </p>
<p> Poptop is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> Poptop is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with Poptop; see the file COPYING. If not, write to the Free Software Foundation, 59 Temple Place &#8211; Suite 330, Boston, MA 02111-1307, USA.</p>
<h2>Availability</h2>
<p>The most recent version of Poptop is available for download from SourceForge at <i><a rel="nofollow" href="http://sourceforge.net/projects/poptop">http://sourceforge.net/projects/poptop</a></i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8), <code><a href="/docs/linux/man/8-pptpd/">pptpd</a></code>(8), <code><a href="/docs/linux/man/5-pptpd-conf/">pptpd.conf</a></code>(5). </p>
