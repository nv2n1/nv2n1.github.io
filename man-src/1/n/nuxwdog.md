---
title: "nuxwdog(1)"
name: "nuxwdog"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nuxwdog/"
description: "nuxwdog – Provides a simple watchdog process that can be used to start, stop, monitor, or reconfigure a server process."
---

<h2 class="name">NAME</h2>
<p> nuxwdog &#8211; Provides a simple watchdog process that can be used to start, stop, monitor, or reconfigure a server process. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nuxwdog</code> -f&nbsp;<wbr><i>configuration_file</i> [-i]</dl>
<h2>DESCRIPTION</h2>
<p> <code>nuxwdog</code></p>
<dd>is a watchdog daemon that builds on the <code>uxwdog</code> service that is part of the Netscape Enterprise Server (NES). <code>nuxwdog</code> can start, stop, monitor, and reconfigure server programs, depending on the parameters passed to it in its configuration file. <code>nuxwdog</code> opens a Unix domain socket to accept requests from any server process it is managing. Optionally, <code>nuxwdog</code> can be configured to communicate only with clients that are descendants of the <code>nuxwdog</code> process, limiting an avenue of potential access to any servers managed by the watchdog. </p>
<p> Some servers require a high-level of security to protect their data or operations, which means (for example) that they cannot store plaintext passwords in a password file to allow the server to be started automatically. <code>nuxwdog</code> can be configured to prompt for server passwords when a server first starts and then caches those passwords so that <code>nuxwdog</code> can restart the server without intervention if the server crashes. </p>
<p> To make it easy for clients to communicate with <code>nuxwdog</code>, a C/C++ shared library is provided with the <code>nuxwdog</code> source code (libnuxwdog.so). Additionally, <code>nuxwdog</code> provides JNI interfaces and Perl bindings to the libnuxwdog.so library, so that calls can be made from Java and Perl programs. For more information on this library and the client interfaces, see m[blue]<code><a rel="nofollow" href="https://fedorahosted.org/nuxwdog/wiki/HOWTO">https://fedorahosted.org/nuxwdog/wiki/HOWTO</a></code>m[]. </p>
<p> <code>nuxwdog</code> is used by Dogtag PKI to monitor and manage the subsystem server processes for Java, Tomcat, and Apache servers.</p>
<h2>OPTIONS</h2>
<p> -f <i>configuration_file</i></p>
<dl>
<dt>
<dd> Passes the configuration file for the service which runs the subsystem. <i>With Dogtag PKI.</i> For the CA, OCSP, TKS, and DRM, this is for the Java process. For the TPS, this is for the Apache process.</dl>
<p> -i</p>
<dl>
<dt>
<dd> Runs the nuxwdog process in interactive mode and keeps nuxwdog open in the foreground instead of running it as a daemon in the background.</dl>
<h2>CONFIGURATION FILE PARAMETERS AND EXAMPLES</h2>
<p> ExeFile</p>
<dl>
<dt>
<dd> Gives the full path to the executable to be started.</dl>
<p> ExeArgs</p>
<dl>
<dt>
<dd> Passes any arguments to the executable. The first argument must be the full path to the executable (the same as the value in <code>ExeFile</code>).</dl>
<p> TmpDir</p>
<dl>
<dt>
<dd> Gives the full path to the executable to be started.</dl>
<p> ChildSecurity</p>
<dl>
<dt>
<dd> Sets whether the child server process should only allow requests from a parent (where <code>nuxwdog</code> is the parent). <code>nuxwdog</code> checks the process ID for any client which sends a request to the Unix domain socket and drops any message where the client is not a descendant of the <code>nuxwdog</code> process. To allow any request, set this to <code>0</code>; to allow only parent or ancestor requests, sets this to <code>1</code>.</dl>
<p> ExeOut</p>
<dl>
<dt>
<dd> Gives the file to write stdout for the server to be started.</dl>
<p> ExeErr</p>
<dl>
<dt>
<dd> Gives the file to write stderr for the server to be started.</dl>
<p> ExeBackground</p>
<dl>
<dt>
<dd> Sets whether to run the server and the <code>nuxwdog</code> processes in the background in daemon mode after the watchdog is initialized. Setting this to <code>1</code> enables daemon mode, while <code>0</code> keeps this in the foreground.</dl>
<p> PidFile</p>
<dl>
<dt>
<dd> Gives the PID file to use to store the <code>nuxwdog</code> PID.</dl>
<p> ChildPidFile</p>
<dl>
<dt>
<dd> Gives the PID file to use to store the PID of the server process managed by <code>nuxwdog</code>.</dl>
<p> ExeContext</p>
<dl>
<dt>
<dd> Sets the SELinux context in which to start the server process.</dl>
<p> <code>nuxwdog</code> can be used to manage many types of server processes. For Dogtag PKI, it manages Java, Tomcat, and Apache servers. For the Dogtag PKI Certificate Authority, a Java-based subsystem with a Tomcat web service, the configuration file identifies the appropriate JRE and class paths, along with setting the output, error, and PID files. (The <i>ExeArgs</i> argument should be all on one line.) </p>
<dl>
<dt>
<dd>
<pre>
ExeFile /usr/lib/jvm/jre/bin/java
ExeArgs /usr/lib/jvm/jre/bin/java  
        -Djava.endorsed.dirs=/usr/share/tomcat5/common/endorsed
        -classpath :/usr/lib/jvm/jre/lib/rt.jar
           :/usr/share/java/commons-collections.jar
           :/usr/share/tomcat5/bin/bootstrap.jar
           :/usr/share/tomcat5/bin/commons-logging-api.jar
           :/usr/share/java/mx4j/mx4j-impl.jar
           :/usr/share/java/mx4j/mx4j-jmx.jar
           :/usr/share/tomcat5/common/lib/nuxwdog.jar
        -Dcatalina.base=/var/lib/pki-ca2
        -Dcatalina.home=/usr/share/tomcat5
        -Djava.io.tmpdir=/usr/share/tomcat5/temp org.apache.catalina.startup.Bootstrap
        start
TmpDir /var/lib/pki-ca2/logs/pids 
ChildSecurity 1
ExeOut /var/lib/pki-ca2/logs/catalina.out
ExeErr /var/lib/pki-ca2/logs/catalina.out
ExeBackground 1
PidFile /var/lib/pki-ca2/logs/wd-pki-ca2.pid
ChildPidFile /var/run/pki-ca2.pid
</pre>
</dl>
<p> For Dogtag PKI, the Token (smart card) Processing System uses an Apache-based server. This example also sets the SELinux context, <code>pki_tps_t</code>, used by the TPS subsystem processes. </p>
<dl>
<dt>
<dd>
<pre>
ExeFile /usr/sbin/httpd.worker
ExeArgs /usr/sbin/httpd.worker -f /etc/pki-tps1/httpd.conf
TmpDir /var/lib/pki-tps1/logs/pids
PidFile /var/lib/pki-tps1/logs/wd-pki-tps1.pid
ExeContext pki_tps_t
</pre>
</dl>
<h2>ADDITIONAL RESOURCES</h2>
<p> There is a more detailed how-to article, including information on available client calls for <code>nuxwdog</code>, at m[blue]<code><a rel="nofollow" href="https://fedorahosted.org/nuxwdog/wiki/HOWTO">https://fedorahosted.org/nuxwdog/wiki/HOWTO</a></code>m[]. </p>
<p> The <code>nuxwdog</code> server works in conjunction with the Dogtag PKI subsystems. The Dogtag PKI project wiki is at m[blue]<code><a rel="nofollow" href="http://pki.fedoraproject.org/wiki/">http://pki.fedoraproject.org/wiki/</a></code>m[]. </p>
<p> For information specifically about <code>nuxwdog</code>, the <code>nuxwdog</code> project wiki is located at m[blue]<code><a rel="nofollow" href="https://fedorahosted.org/nuxwdog/wiki/">https://fedorahosted.org/nuxwdog/wiki/</a></code>m[]<font SIZE="-2">[1]</font>. The <code>nuxwdog</code> relates directly to <code>nuxwdog</code> code changes and releases, rather than all PKI-related updates. </p>
<p> Mailing lists: pki-devel [at] redhat.com and pki-users [at] redhat.com </p>
<p> IRC: Freenode at #dogtag-pki</p>
<h2>AUTHORS</h2>
<p> The PKI tools were written and maintained by developers with Netscape and now with Red Hat. </p>
<p> Authors: Ade Lee &lt;alee [at] redhat.com&gt;, Deon Lackey &lt;dlackey [at] redhat.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> (c) 2010, Red Hat, Inc. Licensed under the GNU Public License version 2.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> <a rel="nofollow" href="https://fedorahosted.org/nuxwdog/wiki/">https://fedorahosted.org/nuxwdog/wiki/</a></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://fedorahosted.org/nuxwdog/wiki">https://fedorahosted.org/nuxwdog/wiki</a></dl>
</dl>
<h2>Index</h2>
