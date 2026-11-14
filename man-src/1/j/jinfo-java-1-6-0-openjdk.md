---
title: "jinfo-java-1-6-0-openjdk(1)"
name: "jinfo-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jinfo-java-1-6-0-openjdk/"
description: "jinfo – Configuration Info"
---

<p>jinfo &#8211; Configuration Info</p>
<h2>Synopsis</h2>
<pre><code>jinfo</code> [ option ] pid
<code>jinfo</code> [ option ] executable core
<code>jinfo</code> [ option ] [server-id@]remote-hostname-or-IP </pre>
<h2>Parameters</h2>
<dl>
<dt>option</p>
<dd>Options are mutually exclusive. Option, if used, should follow immediately after the command name.</p>
<dt>pid</p>
<dd>process id for which the configuration info is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, jps may be used.</p>
<dt>executable</p>
<dd>Java executable from which the core dump was produced.</p>
<dt>core</p>
<dd>core file for which the configuration info is to be printed.</p>
<dt>remote-hostname-or-IP</p>
<dd>remote debug server&#8217;s (see jsadebugd) hostname or IP address.</p>
<dt>server-id</p>
<dd>optional unique id, if multiple debug servers are running on the same remote host.</dl>
<h2>Description</h2>
<p><code>jinfo</code> prints Java configuration information for a given Java process or core file or a remote debug server. Configuration information includes Java System properties and Java virtual machine command line flags. If the given process is running on a 64-bit VM, you may need to specify the <i>-J-d64</i> option, e.g.: </p>
<dl>
<dd>jinfo -J-d64 -sysprops pid</dl>
<p> <code>NOTE &#8211; This utility is unsupported and may or may not be available in future versions of the JDK. On Windows, jinfo only supports the -flag option of a running process.</code> </p>
<h2>Options</h2>
<dl>
<dt>&lt;no option&gt;</p>
<dd>prints both command line flags as well as System properties name, value pairs. </p>
<dt>-flag name</p>
<dd>prints the name and value of the given command line flag. </p>
<dt>-flag [+|-]name</p>
<dd>enables or disables the given boolean command line flag. </p>
<dt>-flag name=value</p>
<dd>sets the given command line flag to the specified value. </p>
<dt>-flags</p>
<dd>prints command line flags passed to the JVM. pairs. </p>
<dt>-sysprops</p>
<dd>prints Java System properties as name, value pairs. </p>
<dt>-h</p>
<dd>prints a help message</p>
<dt>-help</p>
<dd>prints a help message</dl>
<h2>See Also</h2>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>jps</p>
<dt>*</p>
<dd>jsadebugd</dl>
</dl>
<p>&nbsp;<wbr></p>
