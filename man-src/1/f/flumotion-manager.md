---
title: "flumotion-manager(1)"
name: "flumotion-manager"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flumotion-manager/"
description: "flumotion-manager – streaming media server central management"
---

<h2 class="name">NAME</h2>
<p> flumotion-manager &#8211; streaming media server central management</p>
<h2>SYNOPSIS</h2>
<p> <code>flumotion-manager</code> [ <code>&#8211;</code> ] [ <code>&#8211;debug</code> <i>debug configuration</i> ] [ <code>-L</code> <i>logdir</i> ] [ <code>-R</code> <i>rundir</i> ] [ <code>-H</code> <i>host</i> ] [ <code>-P</code> <i>port</i> ] [ <code>-T</code> <i>protocol</i> ] [ <code>-C</code> <i>certificate</i> ] [ <code>-n</code> <i>name</i> ] [ <code>-s</code> <i>servicename</i> ] [ <code>-D</code> ] [ <code>&#8211;daemonize-to=directory</code> ] <i>manager.xml [flow1.xml flow2.xml &#8230;]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>flumotion-manager</code> is the central management component of the flumotion streaming server. <code>flumotion-manager</code> does not actually perform any streaming or encoding itself, it simply acts as a central point for <i>flumotion-worker</i> instances and <i>flumotion-admin</i> administration consoles to connect to. You need to start it before any other flumotion component. When starting flumotion-manager, you need only specify a <i>planet configuration file</i> , but it is frequently helpful to set other options from the command line. </p>
<p> <code>flumotion-manager</code> can load other configuration files as well, if more than one is specified. These additional configuration files define <i>flows</i> that the manager will run on the workers. This allows you to define your manager configuration in the first configuration file, and your streaming configuration or configurations in one or more additional configurations files. </p>
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
<dd> Specify the directory for logging output from the manager.</p>
<dt>-R RUNDIR, &#8211;rundir=RUNDIR</p>
<dd> Specify the directory for runtime files created by the manager.</p>
<dt>-HHOST, &#8211;hostname=HOST</p>
<dd> Specify the interface to bind to, either as a hostname or a numeric address. Usually, unless you have multiple network connections, you won&#8217;t want to set this at all. Defaults to binding to all interfaces.</p>
<dt>-PPORT, &#8211;port=PORT</p>
<dd> Set the port the manager should listen on. Default is 7531 if SSL is being used, or 8642 otherwise.</p>
<dt>-TTRANSPORT, &#8211;transport=TRANSPORT</p>
<dd> Set the transport protocol to use, either &#8216;tcp&#8217; or &#8216;ssl&#8217;. Default is &#8216;ssl&#8217;.</p>
<dt>-CCERTIFICATE, &#8211;certificate=CERTIFICATE</p>
<dd> Specify the PEM certificate file to use. This is required if you use SSL.</p>
<dt>-nNAME, &#8211;name=NAME</p>
<dd> Set the manager name.</p>
<dt>-sSERVICENAME, &#8211;service-name=SERVICENAME</p>
<dd> Set the name used for naming log and pid files when running as a daemon.</p>
<dt>-D, &#8211;daemonize</p>
<dd> Run in the background as a daemon.</p>
<dt>&#8211;daemonize-to=DAEMONIZETO</p>
<dd> Specify what directory to run from when daemonizing. </p>
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
<p> Simple example, starting flumotion-manager using TCP, in verbose mode: </p>
<dl>
<dt>
<dd> flumotion-manager -v -T tcp conf/managers/default/planet.xml</dl>
<p> A slightly more complex example, using two different configuration files and running in the background: </p>
<dl>
<dt>
<dd> flumotion-manager -T tcp -D conf/managers/default/planet.xml conf/managers/mystream.xml </p>
</dl>
<h2>BUGS</h2>
<p> Hopefully none. If you find any bugs, please report them at <a rel="nofollow" href="https://core.fluendo.com/trac/cgi-bin/trac.cgi">https://core.fluendo.com/trac/cgi-bin/trac.cgi</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flumotion/">flumotion</a>(1),<a href="/docs/linux/man/1-flumotion-worker/">flumotion-worker</a>(1),<a href="/docs/linux/man/1-flumotion-admin/">flumotion-admin</a>(1)</code> </p>
<h2>Index</h2>
