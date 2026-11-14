---
title: "javaws-itweb(1)"
name: "javaws-itweb"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javaws-itweb/"
description: "javaws – a Java Web Start client"
---

<h2 class="name">NAME</h2>
<p> javaws &#8211; a Java Web Start client </p>
<h2>SYNOPSIS</h2>
<p> <code>javaws </code> [-run-options] jnlp file<br />
 <code>javaws </code> [-control-options]</p>
<h2>DESCRIPTION</h2>
<p> <code>javaws </code> is an implementation of a JNLP client. It uses a JNLP (Java Network Launch Protocol) file to securely run a remote Java application or a Java applet. This implementation of <code>javaws </code> is from the IcedTea project and is based on the NetX project. </p>
<p> A JNLP file is an xml file that describes how to securely run a remote Java application or a Java applet. </p>
<h2>OPTIONS</h2>
<p> When specifying options, the name of the jnlp file can be after the command, the -jnlp option, an option with no arguments, or after an argument with an option that takes one argument. A html file that launches a jnlp can be specified after the -html option.<br />
 The jnlp-file can either be a url or a local path.<br />
 The JNLP file should only be specified once, whether as a main argument, after -jnlp or through an html file. </p>
<p> <code>Control options:</code> </p>
<dl>
<dt>-about</p>
<dd> Shows a sample application.(No argument expected)</p>
<dt>-help</p>
<dd> Prints out information about supported command and basic usage.(No argument expected)</p>
<dt>-license</p>
<dd> Display the GPL license and exit.(No argument expected)</p>
<dt>-viewer</p>
<dd> Shows the trusted certificate viewer.(No argument expected)</p>
<dt>-Xclearcache</p>
<dd> Clean the JNLP application cache.(No argument expected) </p>
</dl>
<p> <code>Run options:</code> </p>
<dl>
<dt>-allowredirect</p>
<dd> Follows HTTP redirects.(No argument expected)</p>
<dt>-arg arg</p>
<dd> Adds an application argument before launching.(Expected one or more arguments)</p>
<dt>-headless</p>
<dd> Disables download window, other UIs.(No argument expected)</p>
<dt>-html</p>
<dd> Location of HTML file to launch (url or file). You can use parameter ALL or numbers (like 1 2 5) to select applets on page. However experimental, this switch should keep you still in safety.(Expected one or more arguments)</p>
<dt>-jnlp</p>
<dd> Location of JNLP file to launch (url or file).(Exactly one argument expected)</p>
<dt>-nosecurity</p>
<dd> Disables the secure runtime environment.(No argument expected)</p>
<dt>-noupdate</p>
<dd> Disables checking for updates.(No argument expected)</p>
<dt>-param name=value</p>
<dd> Adds an applet parameter before launching.(Expected one or more arguments)</p>
<dt>-property name=value</p>
<dd> Sets a system property before launching.(Expected one or more arguments)</p>
<dt>-strict</p>
<dd> Enables strict checking of JNLP file format.(No argument expected)</p>
<dt>-update seconds</p>
<dd> Check for updates.(Exactly one argument expected)</p>
<dt>-verbose</p>
<dd> Enable verbose output.(No argument expected)</p>
<dt>-version</p>
<dd> Print the IcedTea-Web version and exit.(No argument expected)</p>
<dt>-Xignoreheaders</p>
<dd> Skip jar header verification.(No argument expected)</p>
<dt>-xml</p>
<dd> Uses a strict XML parser to parse the JNLP file.(No argument expected)</p>
<dt>-Xnofork</p>
<dd> Do not create another JVM.(No argument expected)</p>
<dt>-Xoffline</p>
<dd> Prevent ITW network connection. Only cache will be used. Application can still connect.(No argument expected)</p>
<dt>-Xtrustnone</p>
<dd> Instead of asking user, will foretold all answers as no.(No argument expected) </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>javaws -about</p>
<dd> Shows basic help and about informations.</p>
<dt>javaws -about -headless</p>
<dd> Shows basic help and about informations in terminal only.</p>
<dt>javaws -Xnofork -Xignoreheaders -allowredirect -Xoffline <a rel="nofollow" href="http://mypage.web/dangerous.jnlp">http://mypage.web/dangerous.jnlp</a></p>
<dd> Will start dangerous.jnlp application, originally from mypage.web, without downloading it, without headers check and in forced single VM. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>$JAVA_HOME/lib/deployment.config</p>
<dd> java-global deployment properties file. May be affected by deployment.jre.dir.</p>
<dt>$JAVA_HOME/lib/security/cacerts</p>
<dd> Contains various system java-wide stored certificates. Controlled by <code>deployment.system.security.cacerts</code> </p>
<dt>$JAVA_HOME/lib/security/jssecacerts</p>
<dd> Contains various system java-wide stored certificates. Controlled by <code>deployment.system.security.jssecacerts</code> </p>
<dt>$JAVA_HOME/lib/security/trusted.certs</p>
<dd> Contains various system java-wide stored certificates. Controlled by <code>deployment.system.security.trusted.certs</code> </p>
<dt>$JAVA_HOME/lib/security/trusted.clientcerts</p>
<dd> Contains various system java-wide stored certificates. Controlled by <code>deployment.system.security.trusted.clientautcerts</code> </p>
<dt>$JAVA_HOME/lib/security/trusted.jssecerts</p>
<dd> Contains various system java-wide stored certificates. Controlled by <code>deployment.system.security.trusted.jssecerts</code> </p>
<dt>$TMP/$USER/netx/locks</p>
<dd> Location of netx locks. Controlled by <code>deployment.user.locksdir</code> </p>
<dt>$TMP/$USER/netx/locks/netx_running</p>
<dd> Location of netx main lock. Controlled by <code>deployment.user.runningfile</code> </p>
<dt>$XDG_CACHE_HOME/icedtea-web/cache</p>
<dd> Contains cached runtime entries. Controlled by <code>deployment.user.cachedir</code> </p>
<dt>$XDG_CACHE_HOME/icedtea-web/cache/recently_used</p>
<dd> Additional information about items in cache</p>
<dt>$XDG_CACHE_HOME/icedtea-web/pcache</p>
<dd> Contains saved application data. Controlled by <code>deployment.user.pcachedir</code> </p>
<dt>$XDG_CACHE_HOME/icedtea-web/tmp</p>
<dd> Contains temporary runtime files. Controlled by <code>deployment.user.tmp</code> </p>
<dt>$XDG_CONFIG_HOME/icedtea-web/.appletTrustSettings</p>
<dd> File responsible for various actions on applets and apps based on their codebase based on users actions.</p>
<dt>$XDG_CONFIG_HOME/icedtea-web/deployment.properties</p>
<dd> Users main deployment properties file.</p>
<dt>$XDG_CONFIG_HOME/icedtea-web/icons</p>
<dd> Location where icons of javaws applications desktop/menu launchers icons are stored</p>
<dt>$XDG_CONFIG_HOME/icedtea-web/log</p>
<dd> contains file-log files (if enabled), itw-cplugin-date_time.log for native part of plugin, itw-javantx-date_time.log for everything else. Controlled by <code>deployment.user.logdir</code> </p>
<dt>$XDG_CONFIG_HOME/icedtea-web/security/java.policy</p>
<dd> Contains granted permissions for selected unsigned apps. Controlled by <code>deployment.user.security.policy</code> </p>
<dt>$XDG_CONFIG_HOME/icedtea-web/security/trusted.cacerts</p>
<dd> Contains various users stored certificates. Controlled by <code>deployment.user.security.trusted.cacerts</code> </p>
<dt>$XDG_CONFIG_HOME/icedtea-web/security/trusted.certs</p>
<dd> Contains various users stored certificates. Controlled by <code>deployment.user.security.trusted.certs</code> </p>
<dt>$XDG_CONFIG_HOME/icedtea-web/security/trusted.clientcerts</p>
<dd> Contains various users stored certificates. Controlled by <code>deployment.user.security.trusted.clientauthcerts</code> </p>
<dt>$XDG_CONFIG_HOME/icedtea-web/security/trusted.jssecacerts</p>
<dd> Contains various users stored certificates. Controlled by <code>deployment.user.security.trusted.jssecacerts</code> </p>
<dt>$XDG_CONFIG_HOME/icedtea-web/security/trusted.jssecerts</p>
<dd> Contains various users stored certificates. Controlled by <code>deployment.user.security.trusted.jssecerts</code> </p>
<dt>$XDG_DATA_HOME/applications/javaws</p>
<dd> Subdirectory in users menus space, for placing custom menu shortcuts.</p>
<dt>/etc/.java/deployment/.appletTrustSettings</p>
<dd> File responsible for various actions on applets and apps based on their codebase based on admins actions.</p>
<dt>/etc/.java/deployment/deployment.config</p>
<dd> Global deployment config file. </p>
</dl>
<p> Where $XDG_CONFIG_DIR, $XDG_CACHE_DIR and $XDG_RUNTIME_DIR are set as ~/.config, ~/.cache and /tmp or /var/tmp if not set.</p>
<h2>BUGS</h2>
<p> There aren&#8217;t any known bugs. If you come across one, please file it at:<br />
 <a rel="nofollow" href="http://icedtea.classpath.org/wiki/IcedTea-Web#Filing_bugs">http://icedtea.classpath.org/wiki/IcedTea-Web#Filing_bugs</a><br />
 <a rel="nofollow" href="http://icedtea.classpath.org/bugzilla">http://icedtea.classpath.org/bugzilla</a> </p>
<p> Please run in debug (-verbose switch or itw-settings setting or ICEDTEAPLUGIN_DEBUG variable set to true) mode and include that output (best is from java console) with URL to jnlp or html file (or the jnlp/html file or application itself) when filing out the bug report. </p>
<h2>AUTHOR</h2>
<p> Please run in debug (-verbose switch or itw-settings setting or ICEDTEAPLUGIN_DEBUG variable set to true) mode and include that output (best is from java console) with URL to jnlp or html file (or the jnlp/html file or application itself) when filing out the bug report. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-icedtea-web/">icedtea-web</a></code>(1) <code><a href="/docs/linux/man/1-javaws/">javaws</a></code>(1) <code><a href="/docs/linux/man/1-icedtea-web-plugin/">icedtea-web-plugin</a></code>(1) <code><a href="/docs/linux/man/1-itweb-settings/">itweb-settings</a></code>(1) <code><a href="/docs/linux/man/1-policyeditor/">policyeditor</a></code>(1) <code><a href="/docs/linux/man/1-policytool/">policytool</a></code>(1) <code><a href="/docs/linux/man/1-java/">java</a></code>(1) </p>
<p> <a rel="nofollow" href="http://icedtea.classpath.org/wiki/IcedTea-Web">http://icedtea.classpath.org/wiki/IcedTea-Web</a><br />
 <a rel="nofollow" href="http://icedtea.classpath.org/hg/icedtea-web">http://icedtea.classpath.org/hg/icedtea-web</a> </p>
<h2>Index</h2>
