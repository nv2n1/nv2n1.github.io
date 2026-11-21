---
title: "jsvc(1)"
name: "jsvc"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jsvc/"
description: "jsvc – application to launch java daemon"
---

<h2 class="name">NAME</h2>
<p> jsvc &#8211; application to launch java daemon </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>jsvc</code> [-jvm&nbsp;<wbr><i>JVM name</i>] [-client&nbsp;<wbr><i>client JVM</i>] [-server&nbsp;<wbr><i>server JVM</i>] [-classpath&nbsp;<wbr><i>path</i>] [-cp&nbsp;<wbr><i>path</i>] [-java-home&nbsp;<wbr><i>directory</i>] [-version] [-help] [-?] [-nodetach] [-debug] [-check] [-user&nbsp;<wbr><i>user</i>] [-wait&nbsp;<wbr><i>waittime</i>] [-umask&nbsp;<wbr><i>mask</i>] [-stop] [-verbose<i>:class|gc|jni</i>] [-outfile&nbsp;<wbr><i>/full/path/to/file</i>] [-errfile&nbsp;<wbr><i>/full/path/to/file</i>] [-pidfile&nbsp;<wbr><i>/full/path/to/file</i>] [-Dproperty=<i>value</i>] [-X<i>option</i>]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>jsvc</code></p>
<dd>executes <i>classfile</i> that implements a Daemon interface.</dd>
<h2>OPTIONS</h2>
<p> <code>-jvm</code> JVM name</p>
<dl>
<dt>
</dt><dd> use a specific Java Virtual Machine.</dd></dl>
<p> <code>-client</code> client JVM</p>
<dl>
<dt>
</dt><dd> use a client Java Virtual Machine.</dd></dl>
<p> <code>-server</code> server JVM</p>
<dl>
<dt>
</dt><dd> use a server Java Virtual Machine.</dd></dl>
<p> <code>-cp/ -classpath</code> directory and zip/jar files</p>
<dl>
<dt>
</dt><dd> set search path for service classes and resouces</dd></dl>
<p> <code>-java-home</code> directory</p>
<dl>
<dt>
</dt><dd> set the path of your JDK or JRE installation (or set the JAVA_HOME environment variable)</dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
</dt><dd> show the current Java environment version (to check correctness of -home and -jvm. Implies -nodetach)</dd></dl>
<p> <code>-help</code></p>
<dl>
<dt>
</dt><dd> show this help page (implies -nodetach)</dd></dl>
<p> <code>-nodetach</code></p>
<dl>
<dt>
</dt><dd> don&#8217;t detach from parent process and become a daemon</dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
</dt><dd> verbosely print debugging information</dd></dl>
<p> <code>-check</code></p>
<dl>
<dt>
</dt><dd> only check service (implies -nodetach)</dd></dl>
<p> <code>-stop</code></p>
<dl>
<dt>
</dt><dd> stop the service using the file given in the -pidfile option</dd></dl>
<p> <code>-wait</code> waittime</p>
<dl>
<dt>
</dt><dd> wait up to waittime seconds for the service to start waittime should multiple of 10 (min=10)</dd></dl>
<p> <code>-umask</code> mask</p>
<dl>
<dt>
</dt><dd> sets the file mode creation mask</dd></dl>
<p> <code>-user</code> user</p>
<dl>
<dt>
</dt><dd> user used to run the daemon (defaults to current user)</dd></dl>
<p> <code>-verbose[:class|gc|jni]</code></p>
<dl>
<dt>
</dt><dd> enable verbose output</dd></dl>
<p> <code>-outfile</code> /full/path/to/file</p>
<dl>
<dt>
</dt><dd> Location for output from stdout (defaults to /dev/null). Use the value &#8216;&amp;2&#8217; to simulate &#8216;1&gt;&amp;2&#8217;, or &#8216;SYSLOG&#8217; to send output to the system log.</dd></dl>
<p> <code>-errfile</code> /full/path/to/file</p>
<dl>
<dt>
</dt><dd> Location for output from stderr (defaults to /dev/null). Use the value &#8216;&amp;1&#8217; to simulate &#8216;2&gt;&amp;1&#8217;, or &#8216;SYSLOG&#8217; to send output to the system log.</dd></dl>
<p> <code>-pidfile</code> /full/path/to/file</p>
<dl>
<dt>
</dt><dd> Location for output from the file containing the pid of jsvc (defaults to /var/run/jsvc.pid)</dd></dl>
<p> <code>-D</code>&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
</dt><dd> set a Java system property</dd></dl>
<p> <code>-X</code>&lt;option&gt;</p>
<dl>
<dt>
</dt><dd> set Virtual Machine specific option</dd></dl>
<h2>AUTHOR</h2>
<p> JSVC is part of the Apache Commons Daemon project. Authors are Jean-Frederic Clere, Remy Maucherat, Yoav Shapira, Bill Barker, Mladen Turk. JSVC is released under the Apache License Version 2.0. </p>
