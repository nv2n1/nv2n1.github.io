---
title: "tinyproxy(8)"
name: "tinyproxy"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tinyproxy/"
description: "tinyproxy – A light-weight HTTP proxy daemon"
---

<p>tinyproxy &#8211; A light-weight HTTP proxy daemon</p>
<h2>Synopsis</h2>
<p><code>tinyproxy</code> [-vldch]</p>
<h2>Description</h2>
<p><code>tinyproxy</code> is a light-weight HTTP proxy daemon designed to consume a minimum amount of system resources. It listens on a given TCP port and handles HTTP proxy requests. Designed from the ground up to be fast and yet small, it is an ideal solution for use cases such as embedded deployments where a full featured HTTP proxy is required, but the system resources for a larger proxy are unavailable.</p>
<h2>Options</h2>
<p><code>tinyproxy</code> accepts the following options: </p>
<p> <code>-c &lt;config-file&gt;</code></p>
<dl>
<dd>Use an alternate configuration file.</dl>
<p> <code>-d</code></p>
<dl>
<dd>Don&#8217;t daemonize and stay in the foreground. Useful for debugging purposes.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Display a short help screen of command line arguments and exit.</dl>
<p> <code>-l</code></p>
<dl>
<dd>Display the licensing agreement.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Display version information and exit.</dl>
<h2>Signals</h2>
<p>In addition to command-line options, there are also several signals that can be sent to <code>tinyproxy</code> while it is running to generate debugging information and to force certain events. </p>
<p> <code>SIGHUP</code></p>
<dl>
<dd>Force Tinyproxy to do a garbage collection on the current connections linked list. This is usually done automatically after a certain number of connections have been handled.</dl>
<h2>Template Files</h2>
<p>There are two occasions when Tinyproxy delivers HTML pages to the client on it&#8217;s own right: </p>
<dl>
<dd>1. When an error occurred, a corresponding error page is returned.</dl>
<dl>
<dd>2. When a request for the stathost is made, a page summarizing the connection statistics is returned. (See STATHOST below.)</dl>
<p> The layout of both error pages and the statistics page can be controlled via configurable HTML template files that are plain HTML files that additionally understand a few template variables.</p>
<h2>Template Variables</h2>
<p>There are several standard HTML variables that are available in every template file: </p>
<p> <code>request</code></p>
<dl>
<dd>The full HTTP request line.</dl>
<p> <code>cause</code></p>
<dl>
<dd>The abbreviated cause of the error condition.</dl>
<p> <code>clientip</code></p>
<dl>
<dd>The IP address of the client making the request.</dl>
<p> <code>clienthost</code></p>
<dl>
<dd>The hostname of the client making the request.</dl>
<p> <code>version</code></p>
<dl>
<dd>The version of Tinyproxy.</dl>
<p> <code>package</code></p>
<dl>
<dd>The package name. Presently, resolves to <i>tinyproxy</i>.</dl>
<p> <code>date</code></p>
<dl>
<dd>The current date/time in HTTP format.</dl>
<p> In addition, almost all templates support: </p>
<p> <code>detail</code></p>
<dl>
<dd>A detailed, plain English explanation of the error and possible causes.</dl>
<p> When Tinyproxy finds a variable name enclosed in braces, e.g. &quot;{request}&quot;, then this is replaced by the value of the corresponding variable before delivery of the page.</p>
<h2>Stathost</h2>
<p>Tinyproxy returns a HTML page with connection statistics when it receives a HTTP request for a certain host &#8212; the stathost. The stathost name defaults to tinyproxy.stats and can be changed at runtime to any name or IP address with the configuration variable StatHost. </p>
<p> The stat file template can be changed at runtime through the configuration variable StatFile.</p>
<h2>Files</h2>
<p>/etc/tinyproxy/tinyproxy.conf, /var/run/tinyproxy/tinyproxy.pid, /var/log/tinyproxy/tinyproxy.log</p>
<h2>Bugs</h2>
<p>To report bugs in Tinyproxy, please visit &lt;<a rel="nofollow" href="https://www.banu.com/tinyproxy/">https://www.banu.com/tinyproxy/</a>&gt;.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-tinyproxy-conf/">tinyproxy.conf</a>(5)</p>
<h2>Author</h2>
<p>Written by the Tinyproxy project team.</p>
<h2>Copyright</h2>
<p>Copyright (c) 1998-2000 Steven Young; Copyright (c) 2000-2001 Robert James Kaes; Copyright (c) 2009-2010 Mukund Sivaraman; Copyright (c) 2009-2010 Michael Adam. </p>
<p> This program is distributed under the terms of the GNU General Public License version 2 or above. See the COPYING file for additional information.</p>
