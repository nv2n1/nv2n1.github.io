---
title: "conmand(8)"
name: "conmand"
section: "8"
letter: "c"
url: "/docs/linux/man/8-conmand/"
description: "conmand – ConMan daemon"
---

<p>conmand &#8211; ConMan daemon</p>
<h2>Synopsis</h2>
<p><code>conmand</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p><code>conmand</code> is the daemon responsible for managing consoles defined by its configuration file as well as listening for connections from clients. </p>
<h2>Options</h2>
<dl>
<dt><code>-c </code><i>file</i></p>
<dd>Specify a configuration file, overriding the default location [/etc/conman.conf].</p>
<dt><code>-F</code></p>
<dd>Run the daemon in the foreground.</p>
<dt><code>-h</code></p>
<dd>Display a summary of the command-line options.</p>
<dt><code>-k</code></p>
<dd>Send a SIGTERM to the <code>conmand</code> process associated with the specified configuration, thereby killing the daemon. Returns 0 if the daemon was successfully signaled; otherwise, returns 1.</p>
<dt><code>-L</code></p>
<dd>Display license information.</p>
<dt><code>-p </code><i>port</i></p>
<dd>Specify the port on which <code>conmand</code> will listen for clients, overriding both the default port [7890] and the port specified in the configuration file.</p>
<dt><code>-q</code></p>
<dd>Displays the PID of the <code>conmand</code> process associated with the specified configuration if it appears active. Returns 0 if the configuration appears active; otherwise, returns 1.</p>
<dt><code>-r</code></p>
<dd>Send a SIGHUP to the <code>conmand</code> process associated with the specified configuration, thereby re-opening both that daemon&#8217;s log file and individual console log files. Returns 0 if the daemon was successfully signaled; otherwise, returns 1.</p>
<dt><code>-v</code></p>
<dd>Enable verbose mode.</p>
<dt><code>-V</code></p>
<dd>Display version information.</p>
<dt><code>-z</code></p>
<dd>Truncate both the daemon&#8217;s log file and individual console log files at start-up. </p>
</dl>
<h2>Signals</h2>
<dl>
<dt><code>SIGHUP</code></p>
<dd>Close and re-open both the daemon&#8217;s log file and the individual console log files. Conversion specifiers within filenames will be re-evaluated. This is useful for <code>logrotate</code> configurations.</p>
<dt><code>SIGTERM</code></p>
<dd>Terminate the daemon. </p>
</dl>
<h2>Security</h2>
<p>Connections to the server are not authenticated, and communications between client and server are not encrypted. When time allows, this will be addressed in a future release. Until then, the recommendation is to bind the server&#8217;s listen socket to the loopback address (by specifying &quot;<code>server loopback=on</code>&quot; in conman.conf) and restrict access to the server host.</p>
<h2>Notes</h2>
<p>Log messages are sent to standard-error until after the configuration file has been read, at which time future messages are discarded unless either the <code>logfile</code> or <code>syslog</code> keyword has been specified (cf., <code><a href="/docs/linux/man/5-conman-conf/">conman.conf</a>(5)</code>). If the configuration file is modified while the daemon is running and a <code>pidfile</code> was not originally specified, the &#8216;<code>-k</code>&#8216; and &#8216;<code>-r</code>&#8216; options may be unable to identify the daemon process; consequently, the appropriate signal may need to be sent to the daemon manually. The number of consoles that can be simultaneously managed is limited by the maximum number of file descriptors a process can have open. The daemon sets its &quot;nofile&quot; soft limit to the maximum/hard limit. If you are encountering &quot;too many open files&quot; errors, you may need to increase the &quot;nofile&quot; hard limit. </p>
<h2>Author</h2>
<p>Chris Dunlap &lt;cdunlap [at] llnl.gov&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2011 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2001-2007 The Regents of the University of California. </p>
<p> ConMan is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-conman/">conman</a></code>(1), <code><a href="/docs/linux/man/5-conman-conf/">conman.conf</a></code>(5). <code><a rel="nofollow" href="http://conman.googlecode.com/">http://conman.googlecode.com/</a></code> </p>
