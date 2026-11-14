---
title: "pptpctrl(8)"
name: "pptpctrl"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pptpctrl/"
description: "pptpctrl – PPTP control connection manager"
---

<p>pptpctrl &#8211; PPTP control connection manager</p>
<h2>Synopsis</h2>
<p><code>pptpctrl</code> <i>pptp-debug-flag</i> <i>no-ipparam-flag</i> <i>ppp-options-value</i> <i>ppp-speed-value</i> <i>ppp-local-ip-value</i> <i>ppp-remote-ip-value</i> [ <i>pptp-call-id</i> ] [ <i>ppp-binary</i> ] [ <i>pptp-logwtmp</i> ]</p>
<h2>Description</h2>
<p><code>pptpctrl</code> is usually run by <code><a href="/docs/linux/man/8-pptpd/">pptpd</a></code>(8), but can also be run from <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) if some of the features of <code><a href="/docs/linux/man/8-pptpd/">pptpd</a></code>(8), such as IP pool management, and inbuilt TCP wrappers, are not required.</p>
<h2>Options</h2>
<p><code>pptpctrl </code> options are unconventional, as they are designed for use by <code><a href="/docs/linux/man/8-pptpd/">pptpd</a></code>(8) rather than users. The option order is critical. Flag options consist of a 0 or 1, and must be present. Value options consist of a 0, or a 1 followed by the value. Either the 0 or both the 1 and the value must be present. The remaining options are optional, but must be present in the defined order. The options are as follows:</p>
<dl>
<dt>pptp-debug-flag</p>
<dd>if set (1), enables debug messages to syslog from pptpctrl. This has no effect on the setting of the PPP debug option.</p>
<dt>no-ipparam-flag</p>
<dd>if set, <code>pptpctrl </code> will not pass the client&#8217;s IP address to <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) using the <i>ipparam</i> option. See the <i>noipparam</i> option in <code><a href="/docs/linux/man/5-pptpd-conf/">pptpd.conf</a></code>(5).</p>
<dt>ppp-options-value</p>
<dd>file to use for PPP options. See the <i>file</i> option in <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8).</p>
<dt>ppp-speed-value</p>
<dd>value for the <i>speed</i> option given to <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8). Note that on Linux, this parameter is ineffective.</p>
<dt>ppp-local-ip-value</p>
<dd>if set, specifies the IP address that <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) is to use for the network interface on the server. If not set, <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) will determine it based on options; usually it will be the ethernet address of the server.</p>
<dt>ppp-remote-ip-value</p>
<dd>if set, specifies the IP address that <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) is to use for the network interface on the client. If not set, <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) will determine it based on options; usually it will be the ethernet address of the client, or an address given in <i>chap-secrets.</i> Must be set if <i>ppp-local-ip-value</i> is set.</p>
<dt>pptp-call-id</p>
<dd>if present, specifies the call identification for the PPTP session. If omitted, the call identification is zero. Normally the ID is allocated by <code><a href="/docs/linux/man/8-pptpd/">pptpd</a></code>(8) and passed to pptpctrl.</p>
<dt>ppp-binary</p>
<dd>if present, path to the PPP binary to use. If omitted, the default value is used.</p>
<dt>pptp-logwtmp</p>
<dd>if present, specifies whether <code><a href="/docs/linux/man/5-wtmp/">wtmp</a></code>(5) should be updated as users connect and disconnect.</dl>
<h2>Files</h2>
<p>none.</p>
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
<p><code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/5-inetd-conf/">inetd.conf</a></code>(5), <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8), <code><a href="/docs/linux/man/8-pptpd/">pptpd</a></code>(8), <code><a href="/docs/linux/man/5-pptpd-conf/">pptpd.conf</a></code>(5), <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8). </p>
