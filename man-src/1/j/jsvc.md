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
<dt> <code>jsvc</code> [-jvm&nbsp;<wbr><i>JVM name</i>] [-client&nbsp;<wbr><i>client JVM</i>] [-server&nbsp;<wbr><i>server JVM</i>] [-classpath&nbsp;<wbr><i>path</i>] [-cp&nbsp;<wbr><i>path</i>] [-java-home&nbsp;<wbr><i>directory</i>] [-version] [-help] [-?] [-nodetach] [-debug] [-check] [-user&nbsp;<wbr><i>user</i>] [-wait&nbsp;<wbr><i>waittime</i>] [-umask&nbsp;<wbr><i>mask</i>] [-stop] [-verbose<i>:class|gc|jni</i>] [-outfile&nbsp;<wbr><i>/full/path/to/file</i>] [-errfile&nbsp;<wbr><i>/full/path/to/file</i>] [-pidfile&nbsp;<wbr><i>/full/path/to/file</i>] [-Dproperty=<i>value</i>] [-X<i>option</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>jsvc</code></p>
<dd>executes <i>classfile</i> that implements a Daemon interface.</p>
<h2>OPTIONS</h2>
<p> <code>-jvm</code> JVM name</p>
<dl>
<dt>
<dd> use a specific Java Virtual Machine.</dl>
<p> <code>-client</code> client JVM</p>
<dl>
<dt>
<dd> use a client Java Virtual Machine.</dl>
<p> <code>-server</code> server JVM</p>
<dl>
<dt>
<dd> use a server Java Virtual Machine.</dl>
<p> <code>-cp/ -classpath</code> directory and zip/jar files</p>
<dl>
<dt>
<dd> set search path for service classes and resouces</dl>
<p> <code>-java-home</code> directory</p>
<dl>
<dt>
<dd> set the path of your JDK or JRE installation (or set the JAVA_HOME environment variable)</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> show the current Java environment version (to check correctness of -home and -jvm. Implies -nodetach)</dl>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> show this help page (implies -nodetach)</dl>
<p> <code>-nodetach</code></p>
<dl>
<dt>
<dd> don&#8217;t detach from parent process and become a daemon</dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> verbosely print debugging information</dl>
<p> <code>-check</code></p>
<dl>
<dt>
<dd> only check service (implies -nodetach)</dl>
<p> <code>-stop</code></p>
<dl>
<dt>
<dd> stop the service using the file given in the -pidfile option</dl>
<p> <code>-wait</code> waittime</p>
<dl>
<dt>
<dd> wait up to waittime seconds for the service to start waittime should multiple of 10 (min=10)</dl>
<p> <code>-umask</code> mask</p>
<dl>
<dt>
<dd> sets the file mode creation mask</dl>
<p> <code>-user</code> user</p>
<dl>
<dt>
<dd> user used to run the daemon (defaults to current user)</dl>
<p> <code>-verbose[:class|gc|jni]</code></p>
<dl>
<dt>
<dd> enable verbose output</dl>
<p> <code>-outfile</code> /full/path/to/file</p>
<dl>
<dt>
<dd> Location for output from stdout (defaults to /dev/null). Use the value &#8216;&amp;2&#8217; to simulate &#8216;1&gt;&amp;2&#8217;, or &#8216;SYSLOG&#8217; to send output to the system log.</dl>
<p> <code>-errfile</code> /full/path/to/file</p>
<dl>
<dt>
<dd> Location for output from stderr (defaults to /dev/null). Use the value &#8216;&amp;1&#8217; to simulate &#8216;2&gt;&amp;1&#8217;, or &#8216;SYSLOG&#8217; to send output to the system log.</dl>
<p> <code>-pidfile</code> /full/path/to/file</p>
<dl>
<dt>
<dd> Location for output from the file containing the pid of jsvc (defaults to /var/run/jsvc.pid)</dl>
<p> <code>-D</code>&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> set a Java system property</dl>
<p> <code>-X</code>&lt;option&gt;</p>
<dl>
<dt>
<dd> set Virtual Machine specific option</dl>
<h2>AUTHOR</h2>
<p> JSVC is part of the Apache Commons Daemon project. Authors are Jean-Frederic Clere, Remy Maucherat, Yoav Shapira, Bill Barker, Mladen Turk. JSVC is released under the Apache License Version 2.0. </p>
<h2>Index</h2>
