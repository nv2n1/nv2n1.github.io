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
<dt>option</dt>
<dd>Options are mutually exclusive. Option, if used, should follow immediately after the command name.</dd>
<dt>pid</dt>
<dd>process id for which the configuration info is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, jps may be used.</dd>
<dt>executable</dt>
<dd>Java executable from which the core dump was produced.</dd>
<dt>core</dt>
<dd>core file for which the configuration info is to be printed.</dd>
<dt>remote-hostname-or-IP</dt>
<dd>remote debug server&#8217;s (see jsadebugd) hostname or IP address.</dd>
<dt>server-id</dt>
<dd>optional unique id, if multiple debug servers are running on the same remote host.</dd></dl>
<h2>Description</h2>
<p><code>jinfo</code> prints Java configuration information for a given Java process or core file or a remote debug server. Configuration information includes Java System properties and Java virtual machine command line flags. If the given process is running on a 64-bit VM, you may need to specify the <i>-J-d64</i> option, e.g.: </p>
<dl>
<dd>jinfo -J-d64 -sysprops pid</dd></dl>
<p> <code>NOTE &#8211; This utility is unsupported and may or may not be available in future versions of the JDK. On Windows, jinfo only supports the -flag option of a running process.</code> </p>
<h2>Options</h2>
<dl>
<dt>&lt;no option&gt;</dt>
<dd>prints both command line flags as well as System properties name, value pairs. </dd>
<dt>-flag name</dt>
<dd>prints the name and value of the given command line flag. </dd>
<dt>-flag [+|-]name</dt>
<dd>enables or disables the given boolean command line flag. </dd>
<dt>-flag name=value</dt>
<dd>sets the given command line flag to the specified value. </dd>
<dt>-flags</dt>
<dd>prints command line flags passed to the JVM. pairs. </dd>
<dt>-sysprops</dt>
<dd>prints Java System properties as name, value pairs. </dd>
<dt>-h</dt>
<dd>prints a help message</dd>
<dt>-help</dt>
<dd>prints a help message</dd></dl>
<h2>See Also</h2>
<dl>
<dd>
</dd><dl>
<dt>*</dt>
<dd>jps</dd>
<dt>*</dt>
<dd>jsadebugd</dd></dl>
</dl>
<p>&nbsp;<wbr></p>
