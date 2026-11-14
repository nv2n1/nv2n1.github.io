---
title: "vboxwebsrv(1)"
name: "vboxwebsrv"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxwebsrv/"
description: "vboxwebsrv – x86 virtualization solution"
---

<h2 class="name">NAME</h2>
<p> vboxwebsrv &#8211; x86 virtualization solution </p>
<h2>SYNOPSIS</h2>
<p> <code>vboxwebsrv</code> [<i>,options/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Oracle VM VirtualBox web service (C) 2007-2019 Oracle Corporation All rights reserved. </p>
<p> Supported options (default values in brackets): <code>&#8211;help</code>, <code>-h</code>: Print this help message and exit. <code>&#8211;background</code>, <code>-b</code>: Run in background (daemon mode). <code>&#8211;host</code>, <code>-H</code>: The host to bind to (localhost). <code>&#8211;port</code>, <code>-p</code>: The port to bind to (18083). <code>&#8211;ssl</code>, <code>-s</code>: Enable SSL/TLS encryption. <code>&#8211;keyfile</code>, <code>-K</code>: Server key and certificate file, PEM format (&quot;&quot;). <code>&#8211;passwordfile</code>, <code>-a</code>: File name for password to server key (&quot;&quot;). <code>&#8211;cacert</code>, <code>-c</code>: CA certificate file, PEM format (&quot;&quot;). <code>&#8211;capath</code>, <code>-C</code>: CA certificate path (&quot;&quot;). <code>&#8211;dhfile</code>, <code>-D</code>: DH file name or DH key length in bits (&quot;&quot;). <code>&#8211;randfile</code>, <code>-r</code>: File containing seed for random number generator (&quot;&quot;). <code>&#8211;timeout</code>, <code>-t</code>: Session timeout in seconds; 0 = disable timeouts (300). <code>&#8211;check-interval</code>, <code>-i</code>: Frequency of timeout checks in seconds (5). <code>&#8211;threads</code>, <code>-T</code>: Maximum number of worker threads to run in parallel (100). <code>&#8211;keepalive</code>, <code>-k</code>: Maximum number of requests before a socket will be closed (100). <code>&#8211;authentication</code>, <code>-A</code>: Authentication method for the webservice (&quot;&quot;). <code>&#8211;verbose</code>, <code>-v</code>: Be verbose. <code>&#8211;pidfile</code>, <code>-P</code>: Name of the PID file which is created when the daemon was started. <code>&#8211;logfile</code>, <code>-F</code>: Name of file to write log to (no file). <code>&#8211;logrotate</code>, <code>-R</code>: Number of log files (0 disables log rotation). <code>&#8211;logsize</code>, <code>-S</code>: Maximum size of a log file to trigger rotation (bytes). <code>&#8211;loginterval</code>, <code>-I</code>: Maximum time interval to trigger log rotation (seconds). </p>
<h2>Index</h2>
