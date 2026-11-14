---
title: "flumotion-worker(1)"
name: "flumotion-worker"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flumotion-worker/"
description: "flumotion-worker – streaming media server worker"
---

<h2 class="name">NAME</h2>
<p> flumotion-worker &#8211; streaming media server worker</p>
<h2>SYNOPSIS</h2>
<p> <code>flumotion-worker</code> [ <code>&#8211;</code> ] [ <code>&#8211;debug</code> <i>debug configuration</i> ] [ <code>-L</code> <i>logdir</i> ] [ <code>-R</code> <i>rundir</i> ] [ <code>-H</code> <i>host</i> ] [ <code>-P</code> <i>port</i> ] [ <code>-T</code> <i>protocol</i> ] [ <code>-n</code> <i>name</i> ] [ <code>-D</code> ] [ <code>&#8211;daemonize-to=</code> <i>directory</i> ] [ <code>-F</code> <i>ports</i> | <code>&#8211;random-feederports</code> ] <code>-u username</code> <code>-p password</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>flumotion-worker</code> is the part of flumotion that actually performs all the real work of encoding, streaming, etc. In a flumotion system, there will be a single manager, and could be several workers running on different systems (this is useful to distribute the load of, for instance, video encoding). You need to have a minimum of one worker for flumotion to function correctly. </p>
<p> You should start flumotion-manager first, then connect flumotion-worker to the running manager. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd> Show a brief help message, then exit.</p>
<dt>&#8211;version</p>
<dd> Show the version number.</p>
<dt>-v, &#8211;verbose</p>
<dd> Be verbose in console output. This is equivalent to setting the debug level to 3, and will override any debug specifiers.</p>
<dt>-dDEBUG, &#8211;debug=DEBUG</p>
<dd> Set the debug configuration to the specified <code>debug</code> string. See the <i>Debugging</i> section for details of this.</p>
<dt>-L LOGDIR, &#8211;logdir=LOGDIR</p>
<dd> Specify the directory for logging output from the worker.</p>
<dt>-R RUNDIR, &#8211;rundir=RUNDIR</p>
<dd> Specify the directory for runtime files created by the worker.</p>
<dt>-HHOST, &#8211;host=HOST</p>
<dd> Specify the hostname on which the manager is running.</p>
<dt>-PPORT, &#8211;port=PORT</p>
<dd> Specify the port on which the manager in running (usually 7531 for SSL, or 8642 otherwise)</p>
<dt>-TTRANSPORT, &#8211;transport=TRANSPORT</p>
<dd> Set the transport protocol to use, either &#8216;tcp&#8217; or &#8216;ssl&#8217;. Default is &#8216;ssl&#8217;.</p>
<dt>-nNAME, &#8211;name=NAME</p>
<dd> Set the name for this worker to use in the manager.</p>
<dt>-D, &#8211;daemonize</p>
<dd> Run in the background as a daemon.</p>
<dt>-u, &#8211;username</p>
<dd> Specify the username to use to connect to the manager.</p>
<dt>-p, &#8211;password</p>
<dd> Specify the password to use to connect to the manager.</p>
<dt>-FPORTS, &#8211;feederports=PORT_FROM:PORT_TO</p>
<dd> Specify the range of feeder ports to use in the format &#8216;lower-upper&#8217;. These are the ports used for inter-worker communication. If you have multiple workers on seperate systems (perhaps one doing encoding, behind a firewall, and a second doing the streaming outside the firewall), they must be able to communicate using this port range, so you&#8217;ll have to open these ports in your firewall. It is recommended that you have a range of 20 ports.</p>
<dt>&#8211;random-feederports</p>
<dd> Use random available feeder ports. </p>
</dl>
<h2>DEBUGGING</h2>
<p> In the unlikely event of something in flumotion not working, you might want to debug it. The flumotion tools ( <code>flumotion-worker</code> , <code>flumotion-admin</code> , and <code>flumotion-manager</code> ) all alow you to turn on debugging output in two different ways. </p>
<p> Firstly, you can use an environment variable, FLU_DEBUG. Secondly, you can launch the program with a -d or &#8211;debug switch. Either approach allows you to specify a debug configuration string with the following syntax: </p>
<dl>
<dt>
<dd> <code>name1:n1,name2:n2,name3:n3</code></dl>
<p> In this syntax, the &#8216;name&#8217; variables can be replaced with the name of a particular module within flumotion (such as &#8216;admin&#8217;, &#8216;twisted&#8217;, etc.). You can also use &#8216;*&#8217; to specify all modules. The &#8216;n&#8217; variables are numbers from 1 to 5, larger numbers corresponding to more verbose output (ERROR, WARN, INFO, DEBUG, and LOG). At level 4, full debugging information is emitted. </p>
<p> You can also use an abbreviated form where you just supply a single number, thisuses that debug level for all modules. Thus the simplest way to enable full debug output for all modules is to use &#8216;-d 4&#8217; on the command line. </p>
<p> A more complex example would be &#8216;-d *:3,admin:4&#8217; to set the logging level for the admin module to DEBUG, and for all other modules to INFO. </p>
<h2>EXAMPLES</h2>
<p> Simple example, starting flumotion-worker connecting to a manager using TCP, default host and port, and with the username &#8216;user&#8217; and the password &#8216;test&#8217; </p>
<dl>
<dt>
<dd> flumotion-worker -v -T tcp -u user -p test &#8211;feederports=8060-8080</dl>
<h2>BUGS</h2>
<p> Hopefully none. If you find any bugs, please report them at <a rel="nofollow" href="https://core.fluendo.com/trac/cgi-bin/trac.cgi">https://core.fluendo.com/trac/cgi-bin/trac.cgi</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flumotion/">flumotion</a>(1),<a href="/docs/linux/man/1-flumotion-manager/">flumotion-manager</a>(1),<a href="/docs/linux/man/1-flumotion-admin/">flumotion-admin</a>(1)</code> </p>
<h2>Index</h2>
