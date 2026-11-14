---
title: "jstack-java-1-6-0-openjdk(1)"
name: "jstack-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jstack-java-1-6-0-openjdk/"
description: "jstack – Stack Trace"
---

<p>jstack &#8211; Stack Trace </p>
<h2>Synopsis</h2>
<pre><code>jstack</code> [ option ] pid
<code>jstack</code> [ option ] executable core
<code>jstack</code> [ option ] [server-id@]remote-hostname-or-IP</pre>
<h2>Parameters</h2>
<p>Options are mutually exclusive. Option, if used, should follow immediately after the command name. See OPTIONS. </p>
<dl>
<dd>
<dl>
<dt>pid</p>
<dd>process id for which the stack trace is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, jps may be used.</dl>
</dl>
<dl>
<dd>
<dl>
<dt>executable</p>
<dd>Java executable from which the core dump was produced. </p>
<dt>core</p>
<dd>core file for which the stack trace is to be printed. </p>
<dt>remote-hostname-or-IP</p>
<dd>remote debug server&#8217;s (see jsadebugd) hostname or IP address. </p>
<dt>server-id</p>
<dd>optional unique id, if multiple debug servers are running on the same remote host.</dl>
</dl>
<h2>Description</h2>
<p><code>jstack</code> prints Java stack traces of Java threads for a given Java process or core file or a remote debug server. For each Java frame, the full class name, method name, &#8216;bci&#8217; (byte code index) and line number, if available, are printed. With the -m option, jstack prints both Java and native frames of all threads along with the &#8216;pc&#8217; (program counter). For each native frame, the closest native symbol to &#8216;pc&#8217;, if available, is printed. C++ mangled names are not demangled. To demangle C++ names, the output of this command may be piped to <code>c++filt</code>. If the given process is running on a 64-bit VM, you may need to specify the <i>-J-d64</i> option, e.g.: </p>
<dl>
<dd>
<pre><code>jstack -J-d64 -m pid</code></pre>
</dl>
<p> <code>NOTE &#8211; This utility is unsupported and may or may not be available in future versions of the JDK. The only form of jstack that is available on Windows platforms is</code> </p>
<pre><code> jstack pid </code></pre>
<h2>Options</h2>
<dl>
<dd>
<dl>
<dt>-F</p>
<dd>Forces a stack dump when &#8216;jstack pid&#8217; does not respond.</p>
<dt>-m</p>
<dd>prints mixed mode (both Java and native C/C++ frames) stack trace.</p>
<dt>-h</p>
<dd>prints a help message. </p>
<dt>-help</p>
<dd>prints a help message
</dl>
</dl>
<h2>See Also</h2>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><a href="/docs/linux/man/1-pstack/">pstack</a>(1)</p>
<dt>o</p>
<dd>c++<a href="/docs/linux/man/1-filt/">filt</a>(1)</p>
<dt>o</p>
<dd>jps</p>
<dt>o</p>
<dd>jsadebugd</dl>
</dl>
<h2>Known Bugs</h2>
<p>Mixed mode stack trace, the -m option, does not work with the remote debug server. </p>
<p>&nbsp;<wbr></p>
