---
title: "pki-logging(5)"
name: "pki-logging"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pki-logging/"
description: "pki-logging – PKI Common Logging Configuration"
---

<p>pki-logging &#8211; PKI Common Logging Configuration</p>
<h2>Location</h2>
<p>/usr/share/pki/etc/logging.properties, /etc/pki/logging.properties</p>
<h2>Description</h2>
<p>PKI clients and tools use java.util.logging (JUL) as the logging framework (see <a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/logging/package-summary.html">https://docs.oracle.com/javase/8/docs/api/java/util/logging/package-summary.html</a>). The default logging configuration is located at /usr/share/pki/etc/logging.properties. By default only log messages with level WARNING or higher will be logged on the console.</p>
<dl>
<dd>
<pre>java.util.logging.ConsoleHandler.level = ALL
java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter
java.util.logging.SimpleFormatter.format = %4$s: %5$s%6$s%n
46level = WARNING
46handlers = java.util.logging.ConsoleHandler</pre>
</dl>
<p> For more information see the following documents: </p>
<pre>- <a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/logging/ConsoleHandler.html">https://docs.oracle.com/javase/8/docs/api/java/util/logging/ConsoleHandler.html</a>
- <a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html">https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html</a>
- <a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/logging/SimpleFormatter.html">https://docs.oracle.com/javase/8/docs/api/java/util/logging/SimpleFormatter.html</a>
- <a rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html">https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html</a></pre>
<h2>Customization</h2>
<p>To customize the logging configuration, copy the default logging configuration into a new location: </p>
<p> $ cp /usr/share/pki/etc/logging.properties /etc/pki/logging.properties </p>
<p> Then edit the file as needed. For example, to troubleshoot issues with PKI library add the following lines: </p>
<dl>
<dd>
<pre>netscape.level = ALL
com.netscape.level = ALL
org.dogtagpki.level = ALL</pre>
</dl>
<p> To troubleshoot issues with RESTEasy add the following line: </p>
<dl>
<dd>
<pre>org.jboss.resteasy.level = ALL</pre>
</dl>
<p> Then specify the location of the custom logging configuration in the following parameter in /etc/pki/pki.conf: </p>
<dl>
<dd>
<pre>LOGGING_CONFIG=/etc/pki/logging.properties</pre>
</dl>
<p> Then restart the application.</p>
<h2>Authors</h2>
<p>Dogtag Team &lt;pki-devel [at] redhat.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2016 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pki-server-logging/">pki-server-logging</a>(5)</code> </p>
