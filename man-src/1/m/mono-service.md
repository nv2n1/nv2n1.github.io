---
title: "mono-service(1)"
name: "mono-service"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mono-service/"
description: "mono-service, mono-service2 – Mono ServiceProcess host"
---

<h2>NAME</h2>
<p> mono-service, mono-service2 &#8211; Mono ServiceProcess host</p>
<h2>SYNOPSIS</h2>
<p> <code>mono-service [options] program.exe</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>mono-service</i> is a host to run services built with the ServiceProcess assembly. </p>
<p> Use <i>mono-service</i> to run services that use the 1.0 assemblies and use <i>mono-service2</i> to run services that use the 2.0 assemblies. </p>
<p> Services can be paused by sending the SIGUSR1 signal to the process, and execution can be resumed by sending the SIGUSR2 signal. The service can be cleanly shutdown by sending the SIGTERM signal to the process. </p>
<p> Mono programs started with mono-service run with the <code>MONO_DISABLE_SHM</code> variable set. This means that certain Mono features that depend on it are not available to services. </p>
<p> The following options can be used to control the service:</p>
<dl>
<dt><i>-d:DIRECTORY</i></p>
<dd> Use this option to specify the working directory for the service. The default is the current directory.</p>
<dt><i>-l:LOCKFILE</i></p>
<dd> Specifies the file to use for locking, the default is a filename constructed in /tmp based on the name of the program that hosts the service.</p>
<dt><i>-m:MESSAGE</i></p>
<dd> Name to show in the syslog.</p>
<dt><i>-n:NAME</i></p>
<dd> Use this to specify the service to be launched (if the program contains more than one service). The default is to run the first defined service.</p>
<dt><i>&#8211;debug</i></p>
<dd> Use this option to prevent mono-service from redirecting stdin and stdout and prevent the program to be sent to the background. Equivalent to &#8211;no-daemon</p>
<dt><i>&#8211;no-daemon</i></p>
<dd> Use this option to prevent mono-service from redirecting stdin and stdout and prevent the program to be sent to the background. Equivalent to &#8211;debug.</dl>
<h2>CONTROL</h2>
<p> You can control the service by sending signals to the process, you can use the following commands:</p>
<dl>
<dt>Pausing service:</p>
<dd>
<pre>
        kill -USR1 `cat &lt;lock file&gt;`
</pre>
<dt>Resuming service:</p>
<dd>
<pre>
        kill -USR2 `cat &lt;lock file&gt;`
</pre>
<dt>Stopping the service:</p>
<dd>
<pre>
        kill `cat &lt;lock file&gt;`
</pre>
</dl>
<h2>EXAMPLES</h2>
<p> Start the MyService.exe assembly, with a lock in /root/service-lock: </p>
<pre>
        mono-service -l:/root/service-lock MyService.exe
</pre>
<h2>DEBUGGING</h2>
<p> Messages produced by the service are logged on syslog.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-list">http://lists.ximian.com/mailman/listinfo/mono-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit: <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a>(1)</code> </p>
<p> <code>N:System.ServiceProcess</code> </p>
<h2>Index</h2>
