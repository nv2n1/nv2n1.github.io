---
title: "gearmand(1)"
name: "gearmand"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gearmand/"
---

<h2 class="name">NAME</h2>
 

 gearmand - Gearman client/worker connector. 

<h2>SYNOPSIS</h2>

 <pre>
 gearmand --daemon
</pre>

<h2>DESCRIPTION</h2>

 This is the main executable for Gearman::Server. It provides command-line configuration of port numbers, pidfiles, and daemonization.

<h2>OPTIONS</h2>

<dl>
<dt>--daemonize / -d
<dd> Make the daemon run in the background (good for init.d scripts, bad for running under daemontools/supervise).
<dt>--port=7003 / -p 7003
<dd> Set the port number, defaults to 7003.
<dt>--pidfile=/some/dir/gearmand.pid
<dd> Write a pidfile when starting up
<dt>--debug=1
<dd> Enable debugging (currently the only debug output is when a client or worker connects).</dl>

<h2>COPYRIGHT</h2>

 Copyright 2005-2007, Danga Interactive 

 You are granted a license to use it under the same terms as Perl itself.

<h2>WARRANTY</h2>

 This is free software. <font SIZE="-1">IT</font> <font SIZE="-1">COMES</font> <font SIZE="-1">WITHOUT</font> <font SIZE="-1">WARRANTY</font> <font SIZE="-1">OF</font> <font SIZE="-1">ANY</font> <font SIZE="-1">KIND</font>.

<h2>AUTHORS</h2>

 Brad Fitzpatrick &lt;brad [at] danga.com&gt; 

 Brad Whitaker &lt;whitaker [at] danga.com&gt;

<h2>SEE ALSO</h2>

 Gearman::Server 

 Gearman::Client 

 Gearman::Worker 

 Gearman::Client::Async 

<h2>Index</h2>


