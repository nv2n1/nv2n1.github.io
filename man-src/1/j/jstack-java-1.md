---
title: "jstack-java-1(1)"
name: "jstack-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jstack-java-1/"
description: "jstack – Stack Trace"
---

<h2>Name</h2>
<p> jstack &#8211; Stack Trace </p>
<h2>SYNOPSIS</h2>
<pre><code>
jstack[option] pid
            jstack[option] executable core
                jstack[option][server - id @] remote -
        hostname -
    or -IP
</code></pre>
<h2>PARAMETERS</h2>
<p> Options are mutually exclusive. Option, if used, should follow immediately after the command name. See OPTIONS. </p>
<dl>
<dt>
<dd>
<dl>
<dt>pid</p>
<dd> process id for which the stack trace is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, <a href="/docs/linux/man/1-jps/">jps</a>(1) may be used.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>executable</p>
<dd> Java executable from which the core dump was produced. </p>
<dt>core</p>
<dd> core file for which the stack trace is to be printed. </p>
<dt>remote-hostname-or-IP</p>
<dd> remote debug server&#8217;s (see <a href="/docs/linux/man/1-jsadebugd/">jsadebugd</a>(1)) hostname or IP address. </p>
<dt>server-id</p>
<dd> optional unique id, if multiple debug servers are running on the same remote host.</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>jstack</code> prints Java stack traces of Java threads for a given Java process or core file or a remote debug server. For each Java frame, the full class name, method name, &#8216;bci&#8217; (byte code index) and line number, if available, are printed. With the -m option, jstack prints both Java and native frames of all threads along with the &#8216;pc&#8217; (program counter). For each native frame, the closest native symbol to &#8216;pc&#8217;, if available, is printed. C++ mangled names are not demangled. To demangle C++ names, the output of this command may be piped to <code>c++filt</code>. If the given process is running on a 64-bit VM, you may need to specify the <i>-J-d64</i> option, e.g.: </p>
<pre>
<code>jstack -J-d64 -m pid</code>
</pre>
<p> <code>NOTE</code> &#8211; This utility is unsupported and may or may not be available in future versions of the JDK. In Windows Systems where dbgeng.dll is not present, &#8216;Debugging Tools For Windows&#8217; needs to be installed to have these tools working. Also, <i>PATH</i> environment variable should contain the location of <i>jvm.dll</i> used by the target process or the location from which the Crash Dump file was produced. </p>
<p> For example, <i>set PATH=&lt;jdk&gt;\jrein
