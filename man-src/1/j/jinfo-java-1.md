---
title: "jinfo-java-1(1)"
name: "jinfo-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jinfo-java-1/"
description: "jinfo – Configuration Info"
---

<h2>Name</h2>
<p> jinfo &#8211; Configuration Info </p>
<h2>SYNOPSIS</h2>
<pre><code>
jinfo[option] pid
            jinfo[option] executable core
                jinfo[option][server - id @] remote -
        hostname -
    or -IP
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>option</p>
<dd> Options are mutually exclusive. Option, if used, should follow immediately after the command name.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>pid</p>
<dd> process id for which the configuration info is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, <a href="/docs/linux/man/1-jps/">jps</a>(1) may be used.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>executable</p>
<dd> Java executable from which the core dump was produced.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>core</p>
<dd> core file for which the configuration info is to be printed.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>remote-hostname-or-IP</p>
<dd> remote debug server&#8217;s (see <a href="/docs/linux/man/1-jsadebugd/">jsadebugd</a>(1)) hostname or IP address.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>server-id</p>
<dd> optional unique id, if multiple debug servers are running on the same remote host.</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>jinfo</code> prints Java configuration information for a given Java process or core file or a remote debug server. Configuration information includes Java System properties and Java virtual machine command line flags. If the given process is running on a 64-bit VM, you may need to specify the <i>-J-d64</i> option, e.g.:<br />
 jinfo -J-d64 -sysprops pid </p>
<p> <code>NOTE &#8211; This utility is unsupported and may or may not be available in future versions of the JDK. In Windows Systems where dbgeng.dll is not present, &#8216;Debugging Tools For Windows&#8217; need to be installed to have these tools working. Also, </code><tt>PATH</tt><code> environment variable should contain the location of </code><tt>jvm.dll</tt><code> used by the target process or the location from which the Crash Dump file was produced.</code> </p>
<p> <code>For example, </code><tt>set PATH=&lt;jdk&gt;\jrein
