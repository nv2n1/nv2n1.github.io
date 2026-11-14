---
title: "jmap-java-1(1)"
name: "jmap-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jmap-java-1/"
description: "jmap – Memory Map"
---

<h2>Name</h2>
<p> jmap &#8211; Memory Map </p>
<h2>SYNOPSIS</h2>
<pre><code>
jmap[option] pid
            jmap[option] executable core
                jmap[option][server - id @] remote -
        hostname -
    or -IP
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>option</p>
<dd> Options are mutually exclusive. Option, if used, should follow immediately after the command name.</p>
<dt>pid</p>
<dd> process id for which the memory map is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, <a href="/docs/linux/man/1-jps/">jps</a>(1) may be used. </p>
<dt>executable</p>
<dd> Java executable from which the core dump was produced. </p>
<dt>core</p>
<dd> core file for which the memory map is to be printed. </p>
<dt>remote-hostname-or-IP</p>
<dd> remote debug server&#8217;s (see <a href="/docs/linux/man/1-jsadebugd/">jsadebugd</a>(1)) hostname or IP address. </p>
<dt>server-id</p>
<dd> optional unique id, if multiple debug servers are running on the same remote host.
</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>jmap</code> prints shared object memory maps or heap memory details of a given process or core file or a remote debug server. If the given process is running on a 64-bit VM, you may need to specify the <i>-J-d64</i> option, e.g.: </p>
<pre>
<code>jmap -J-d64 -heap pid</code>
</pre>
<p> <code>NOTE: This utility is unsupported and may or may not be available in future versions of the JDK. In Windows Systems where dbgeng.dll is not present, &#8216;Debugging Tools For Windows&#8217; needs to be installed to have these tools working. Also, </code><tt>PATH</tt><code> environment variable should contain the location of </code><tt>jvm.dll</tt><code> used by the target process or the location from which the Crash Dump file was produced.</code> </p>
<p> <code>For example, </code><tt>set PATH=&lt;jdk&gt;\jrein
