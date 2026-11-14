---
title: "flumotion-admin(1)"
name: "flumotion-admin"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flumotion-admin/"
description: "flumotion-admin – streaming media server administration GUI"
---

<h2 class="name">NAME</h2>
<p> flumotion-admin &#8211; streaming media server administration GUI</p>
<h2>SYNOPSIS</h2>
<p> <code>flumotion-admin</code> [ <code>-h</code> ] [ <code>&#8211;debug</code> <i>debug configuration</i> ] [ <code>-m</code> <i>manager</i> ] [ <code>&#8211;no-ssl</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>flumotion-admin</code> is a GUI application that provides administration capabilities for the flumotion streaming server. Using it, you can configure and monitor the streams flumotion serves. <code>flumotion-admin</code> connects to a running <i>flumotion-manager</i> to control the manager, start and stop components, and display logging and monitoring information about the running components. </p>
<p> You must start <i>flumotion-manager</i> before you can use <code>flumotion-admin</code> , but once you&#8217;ve done so you can just run <code>flumotion-admin</code> with no arguments to start the GUI. </p>
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
<dt>-mMANAGER, &#8211;manager=MANAGER</p>
<dd> Set the manager connection string in the form [username[:password]@]host:port</p>
<dt>&#8211;no-ssl</p>
<dd> Disable encryption when connecting to the manager. </p>
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
<h2>BUGS</h2>
<p> Hopefully none. If you find any bugs, please report them at <a rel="nofollow" href="https://core.fluendo.com/trac/cgi-bin/trac.cgi">https://core.fluendo.com/trac/cgi-bin/trac.cgi</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flumotion/">flumotion</a>(1),<a href="/docs/linux/man/1-flumotion-worker/">flumotion-worker</a>(1),<a href="/docs/linux/man/1-flumotion-manager/">flumotion-manager</a>(1)</code> </p>
<h2>Index</h2>
