---
title: "pki-server-logging(5)"
name: "pki-server-logging"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pki-server-logging/"
description: "pki-server-logging – PKI Server Logging Configuration"
---

<p>pki-server-logging &#8211; PKI Server Logging Configuration</p>
<h2>Location</h2>
<p>/etc/pki/&lt;instance&gt;/logging.properties, /var/lib/pki/&lt;instance&gt;/lib/log4j.properties, /etc/pki/&lt;instance&gt;/&lt;subsystem&gt;/CS.cfg</p>
<h2>Description</h2>
<p>PKI server logging can be configured using the following logging frameworks: </p>
<pre>- java.util.logging (JUL) (<a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/logging/package-summary.html)">https://docs.oracle.com/javase/8/docs/api/java/util/logging/package-summary.html)</a>
- Log4j (<a rel="nofollow" href="http://logging.apache.org/log4j/1.2/)">http://logging.apache.org/log4j/1.2/)</a>
- Internal Logging</pre>
<h3>java.util.logging (JUL)</h3>
<p>Tomcat uses JUL as the default logging framework. The configuration is described in <a rel="nofollow" href="http://tomcat.apache.org/tomcat-7.0-doc/logging.html">http://tomcat.apache.org/tomcat-7.0-doc/logging.html</a> and <a href="http://tomcat.apache.org/tomcat-8.0-doc/logging.html.">http://tomcat.apache.org/tomcat-8.0-doc/logging.html.</a> The default configuration is located at /usr/share/pki/server/conf/logging.properties. During server deployment a link will be created at /etc/pki/&lt;instance&gt;/logging.properties. By default only log messages with level WARNING or higher will be logged on the console (i.e. systemd journal).</p>
<dl>
<dd>
<pre>java.util.logging.ConsoleHandler.level = ALL
java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter
java.util.logging.SimpleFormatter.format = %4$s: %5$s%6$s%n
46level = WARNING
46handlers = java.util.logging.ConsoleHandler</pre>
</dl>
<p> The systemd journal can be viewed with the following command: </p>
<pre>$ journalctl -u pki-tomcatd@&lt;instance&gt;.service</pre>
<p>For more information see the following documents: </p>
<pre>- <a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/logging/ConsoleHandler.html">https://docs.oracle.com/javase/8/docs/api/java/util/logging/ConsoleHandler.html</a>
- <a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html">https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html</a>
- <a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/logging/SimpleFormatter.html">https://docs.oracle.com/javase/8/docs/api/java/util/logging/SimpleFormatter.html</a>
- <a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html">https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html</a></pre>
<h3>Log4j</h3>
<p>The default Tomcat 7 classpath does include Log4j, but the server itself is not configured to use Log4j for logging by default. However, since the Log4j is in the classpath the RESTEasy will use Log4j for logging automatically (see <a rel="nofollow" href="https://docs.jboss.org/resteasy/docs/3.0.6.Final/userguide/html/Installation_Configuration.html#RESTEasyLogging">https://docs.jboss.org/resteasy/docs/3.0.6.Final/userguide/html/Installation_Configuration.html#RESTEasyLogging</a>). The default Log4j configuration is located at /usr/share/pki/server/conf/log4j.properties. During server deployment a link will be created at /var/lib/pki/&lt;instance&gt;/lib/log4j.properties. By default only log messages with level WARN or higher will be logged on the console (i.e. systemd journal).</p>
<dl>
<dd>
<pre>log4j.appender.console = org.apache.log4j.ConsoleAppender
log4j.appender.console.Target = System.err
log4j.appender.console.layout = org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern = %p: %m%n
log4j.rootLogger = WARN, console</pre>
</dl>
<p> The default Tomcat 8 classpath does not include Log4j, so RESTEasy will use JUL instead. For more information see the following documents: </p>
<pre>- <a rel="nofollow" href="http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/ConsoleAppender.html">http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/ConsoleAppender.html</a>
- <a rel="nofollow" href="http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/Level.html">http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/Level.html</a>
- <a rel="nofollow" href="http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/PatternLayout.html">http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/PatternLayout.html</a></pre>
<h3>Internal Logging</h3>
<p>Each PKI subsystem uses an internal logging framework for debugging purposes. The logging configuration is stored in /etc/pki/&lt;instance&gt;/&lt;subsystem&gt;/CS.cfg.</p>
<dl>
<dd>
<pre>debug.enabled=true
debug.level=0
debug.filename=/var/lib/pki/&lt;instance&gt;/logs/&lt;subsystem&gt;/debug
debug.hashkeytypes=
debug.showcaller=false</pre>
</dl>
<p> The <code>debug.enabled</code> determines whether the debug log is enabled. By default it is enabled. The <code>debug.level</code> determines the amount of details to be logged. The value ranges from 0 (most details) to 10 (least details). The default is 0. The <code>debug.filename</code> determines the debug log file location. By default it is located at /var/lib/pki/&lt;instance&gt;/logs/&lt;subsystem&gt;/debug. The <code>debug.hashkeytypes</code> is a comma-separated list of additional components to log. By default it&#8217;s empty. The <code>debug.showcaller</code> determines whether to include the caller information in the log message. By default it&#8217;s disabled. </p>
<h2>Customization</h2>
<h3>java.util.logging (JUL)</h3>
<p>To customize JUL configuration, replace the link with a copy of the default configuration: </p>
<pre>$ rm -f /etc/pki/&lt;instance&gt;/logging.properties
$ cp /usr/share/pki/server/conf/logging.properties /etc/pki/&lt;instance&gt;
$ chown pkiuser.pkiuser /etc/pki/&lt;instance&gt;/logging.properties</pre>
<p>Then edit the file as needed. For example, to troubleshoot issues with PKI library add the following lines: </p>
<dl>
<dd>
<pre>netscape.level = ALL
com.netscape.level = ALL
org.dogtagpki.level = ALL</pre>
</dl>
<p> To troubleshoot issues with RESTEasy add the following line (unless Log4j is installed in Tomcat classpath): </p>
<dl>
<dd>
<pre>org.jboss.resteasy.level = ALL</pre>
</dl>
<p> Then restart the server.</p>
<h3>Log4j</h3>
<p>To customize Log4j configuration, replace the link with a copy of the default configuration: </p>
<pre>$ rm -f /var/lib/pki/&lt;instance&gt;/lib/log4j.properties
$ cp /usr/share/pki/server/conf/log4j.properties /var/lib/pki/&lt;instance&gt;/lib
$ chown pkiuser.pkiuser /var/lib/pki/&lt;instance&gt;/lib/log4j.properties</pre>
<p>Then edit the file as needed. For example, to troubleshoot issues with RESTEasy add the following line (unless Log4j is not installed in Tomcat classpath): </p>
<dl>
<dd>
<pre>log4j.logger.org.jboss.resteasy = ALL</pre>
</dl>
<p> Then restart the server.</p>
<h3>Internal Logging</h3>
<p>To customize the internal logging configuration, edit the CS.cfg as needed, then restart the server.</p>
<h2>Authors</h2>
<p>Dogtag Team &lt;pki-devel [at] redhat.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2016 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pki-logging/">pki-logging</a>(5)</code> </p>
