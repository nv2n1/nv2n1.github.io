---
title: "jinfo-java-1(1)"
name: "jinfo-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jinfo-java-1/"
description: "jinfo – Configuration Info"
---
<h2>Name</h2>
<p> jinfo - Configuration Info </p>
<h2>SYNOPSIS</h2>
<pre><code>
 jinfo  [ option ] pid
 jinfo  [ option ] executable core
 jinfo  [ option ] [server-id@]remote-hostname-or-IP
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dd>  </dd>
<dl>
<dt>option </dt>
<dd> <p> Options are mutually exclusive. Option, if used, should follow immediately after the command name. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd>
<dl>
<dt>pid </dt>
<dd> <p> process id for which the configuration info is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, <a href="/docs/linux/man/1-jps/">jps</a>(1) may be used. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd>
<dl>
<dt>executable </dt>
<dd> <p> Java executable from which the core dump was produced. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd>
<dl>
<dt>core </dt>
<dd> <p> core file for which the configuration info is to be printed. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd>
<dl>
<dt>remote-hostname-or-IP </dt>
<dd> <p> remote debug server&#8217;s (see jsadebugd(1)) hostname or IP address. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd>
<dl>
<dt>server-id </dt>
<dd> <p> optional unique id, if multiple debug servers are running on the same remote host. </p>
 </dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>jinfo</code> prints Java configuration information for a given Java process or core file or a remote debug server. Configuration information includes Java System properties and Java virtual machine command line flags. If the given process is running on a 64-bit VM, you may need to specify the <i>-J-d64</i> option, e.g.: <br />
 jinfo -J-d64 -sysprops pid </p>
<p> <code>NOTE - This utility is unsupported and may or may not be available in future versions of the JDK. In Windows Systems where dbgeng.dll is not present, &#8216;Debugging Tools For Windows&#8217; need to be installed to have these tools working. Also, </code><code>PATH</code><code> environment variable should contain the location of </code><code>jvm.dll</code><code> used by the target process or the location from which the Crash Dump file was produced.</code> </p>
<p> <code>For example, </code><code>set PATH=&lt;jdk&gt;\jre\bin\client;%PATH%</code> </p>
<h2>OPTIONS</h2>
<dl>
<dd>  </dd>
<dl>
<dt>&lt;no option&gt; </dt>
<dd> <p> prints both command line flags as well as System properties name, value pairs. <br />
 </p>
 </dd>
<dt>-flag name </dt>
<dd> <p> prints the name and value of the given command line flag. <br />
 </p>
 </dd>
<dt>-flag [+|-]name </dt>
<dd> <p> enables or disables the given boolean command line flag. <br />
 </p>
 </dd>
<dt>-flag name=value </dt>
<dd> <p> sets the given command line flag to the specified value. <br />
 </p>
 </dd>
<dt>-flags </dt>
<dd> <p> prints command line flags passed to the JVM. pairs. <br />
 </p>
 </dd>
<dt>-sysprops </dt>
<dd> <p> prints Java System properties as name, value pairs. <br />
 </p>
 </dd>
<dt>-h </dt>
<dd> <p> prints a help message </p>
 </dd>
<dt>-help </dt>
<dd> <p> prints a help message </p>
 </dd></dl>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> <a href="/docs/linux/man/1-jps/">jps</a>(1) </p>
 </dd>
<dt>o</dt>
<dd> <p> jsadebugd(1) </p>
 </dd></dl>
</dl>
<p> <br />
&nbsp;<wbr> </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">Name</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">PARAMETERS</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">SEE ALSO</a></dt>
<dd>  </dd></dl>
