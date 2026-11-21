---
title: "jinfo(1)"
name: "jinfo"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jinfo/"
description: "jinfo – Generates configuration information. This command is experimental and unsupported."
---
<h2>NAME</h2>
<p> jinfo - Generates configuration information. This command is experimental and unsupported.  </p>
<h2>SYNOPSIS</h2>
<pre><code>
 jinfo  [ option  ] pid 
</code></pre>
<pre><code>
 jinfo  [ option ] executable core 
</code></pre>
<pre><code>
 jinfo  [ option ] [ servier-id ] remote-hostname-or-IP 
</code></pre>
<dl>
<dt><i>option</i></dt>
<dd> <p> The command-line options. See Options. </p>
 </dd>
<dt><i>pid</i></dt>
<dd> <p> The process ID for which the configuration information is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, use the <a href="/docs/linux/man/1-jps/">jps</a>(1) command. </p>
 </dd>
<dt><i>executable</i></dt>
<dd> <p> The Java executable from which the core dump was produced. </p>
 </dd>
<dt><i>core</i></dt>
<dd> <p> The core file for which the configuration information is to be printed. </p>
 </dd>
<dt><i>remote-hostname-or-IP</i></dt>
<dd> <p> The remote debug server <code>hostname</code> or <code>IP</code> address. See jsadebugd(1). </p>
 </dd>
<dt><i>server-id</i></dt>
<dd> <p> An optional unique ID to use when multiple debug servers are running on the same remote host. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code>jinfo</code> command prints Java configuration information for a specified Java process or core file or a remote debug server. The configuration information includes Java system properties and Java Virtual Machine (JVM) command-line flags. If the specified process is running on a 64-bit JVM, then you might need to specify the <code>-J-d64</code> option, for example: <code>jinfo</code><code>-J-d64 -sysprops pid</code>. </p>
<p> This utility is unsupported and might not be available in future releases of the JDK. In Windows Systems where <code>dbgeng.dll</code> is not present, Debugging Tools For Windows must be installed to have these tools working. The <code>PATH</code> environment variable should contain the location of the jvm.dll that is used by the target process or the location from which the crash dump file was produced. For example, <code>set PATH=%JDK_HOME%\jre\bin\client;%PATH%</code> .  </p>
<h2>OPTIONS</h2>
<dl>
<dt>no-option</dt>
<dd> <p> Prints both command-line flags and system property name-value pairs. </p>
 </dd>
<dt>-flag <i>name</i></dt>
<dd> <p> <br />
 Prints the name and value of the specified command-line flag. </p>
 </dd>
<dt>-flag <i>[+|-]name</i></dt>
<dd> <p> <br />
 enables or disables the specified Boolean command-line flag. </p>
 </dd>
<dt>-flag <i>name=value</i></dt>
<dd> <p> <br />
 Sets the specified command-line flag to the specified value. </p>
 </dd>
<dt>-flags</dt>
<dd> <p> <br />
 Prints command-line flags passed to the JVM. </p>
 </dd>
<dt>-sysprops</dt>
<dd> <p> <br />
 Prints Java system properties as name-value pairs. </p>
 </dd>
<dt>-h</dt>
<dd> <p> <br />
 Prints a help message. </p>
 </dd>
<dt>-help</dt>
<dd> <p> <br />
 Prints a help message. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <a href="/docs/linux/man/1-jps/">jps</a>(1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> jsadebugd(1) <br />
 </p>
 </dd></dl>
