---
title: "itweb-settings(1)"
name: "itweb-settings"
section: "1"
letter: "i"
url: "/docs/linux/man/1-itweb-settings/"
description: "itweb-settings – view and modify settings for javaws and the browser plugin"
---

<h2 class="name">NAME</h2>
<p> itweb-settings &#8211; view and modify settings for <code>javaws </code> and the <code>browser plugin</code></p>
<h2>SYNOPSIS</h2>
<p> <code>itweb-settings </code><br />
 <code>itweb-settings </code> command arguments</p>
<h2>DESCRIPTION</h2>
<p> <code>itweb-settings </code> is a command line and a GUI program to modify and edit settings used by the IcedTea-Web implementation of <code>javaws </code> and the <code>browser plugin</code> </p>
<p> If executed without any arguments, it starts up a GUI. Otherwise, it tries to do what is specified in the argument. </p>
<p> The command-line allows quickly searching, making a copy of and modifying specific settings without having to hunt through a UI.</p>
<h2>DESCRIPTION</h2>
<dl>
<dt>-check name</p>
<dd> Checks that all the current settings have valid values.(No argument expected)</p>
<dt>-get name</p>
<dd> Shows the value of the specified settings.(Expected one or more arguments)</p>
<dt>-headless</p>
<dd> Disables download window, other UIs.(No argument expected)</p>
<dt>-help</p>
<dd> Prints out information about supported command and basic usage. Can also take an parameter, and then it prints detailed help for this command.(No argument expected)</p>
<dt>-info name</p>
<dd> Shows additional information about the named settings. Includes a description, the current value, the possible values, and the source of the setting.(Expected one or more arguments)</p>
<dt>-list</p>
<dd> Shows a list of all the IcedTea-Web settings and their current values.(No argument expected)</p>
<dt>-reset name</p>
<dd> Resets the specified settings to their original value.(Expected one or more arguments)</p>
<dt>-reset all</p>
<dd> Resets all settings to their original values.(No argument expected)</p>
<dt>-set name value</p>
<dd> Sets the settings to the new value specified, if it is an appropriate value.(Expected even number of arguments with param=value as valid argument)</p>
<dt>-verbose</p>
<dd> Enable verbose output.(No argument expected) </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>itweb-settings</p>
<dd> Show the GUI editor</p>
<dt>itweb-settings -reset deployment.proxy.type</p>
<dd>
&nbsp;<wbr>Resets the value of&nbsp;<wbr>`deployment.proxy.type`&nbsp;<wbr>setting. </p>
</dl>
<p> <code>Known properties (key and default value):</code> </p>
<dl>
<dt>deployment.browser.path</p>
<dd> null (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.cache.jarcompression</p>
<dd> 0 (Possible: are in range 0 to 10 (inclusive))</p>
<dt>deployment.cache.max.size</p>
<dd> -1 (Possible: are in range -1 to 2,147,483,647 (inclusive))</p>
<dt>deployment.console.startup.mode</p>
<dd> HIDE (Possible: [DISABLE, HIDE, SHOW, SHOW_PLUGIN_ONLY, SHOW_JAVAWS_ONLY])</p>
<dt>deployment.javapi.cache.enabled</p>
<dd> false (Possible: are true or false)</p>
<dt>deployment.javaws.associations</p>
<dd> 2 (Possible: are in range 0 to 3 (inclusive))</p>
<dt>deployment.javaws.autodownload</p>
<dd> false (Possible: are true or false)</p>
<dt>deployment.javaws.installURL</p>
<dd> null (Possible: include any valid url (eg. <a rel="nofollow" href="http://icedtea.classpath.org/hg/))">http://icedtea.classpath.org/hg/))</a></p>
<dt>deployment.javaws.shortcut</p>
<dd> ASK_IF_HINTED (Possible: [ALWAYS, ALWAYS_IF_HINTED, ASK_USER, ASK_IF_HINTED, NEVER])</p>
<dt>deployment.javaws.update.timeout</p>
<dd> 500 (Possible: are in range 0 to 10,000 (inclusive))</p>
<dt>deployment.jnlpclassloader.strict</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.jre.dir</p>
<dd> null</p>
<dt>deployment.log</p>
<dd> false (Possible: are true or false)</p>
<dt>deployment.log.file</p>
<dd> false (Possible: are true or false)</p>
<dt>deployment.log.file.clientapp</p>
<dd> false (Possible: are true or false)</p>
<dt>deployment.log.file.legacylog</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.log.headers</p>
<dd> false (Possible: are true or false)</p>
<dt>deployment.log.stdstreams</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.log.system</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.manifest.attributes.check</p>
<dd> ALL (Possible: (Values that can be used alone only): [ALL, NONE] (Values that can be used in combination separated by the delimiter &quot;,&quot; with no space expected ): [ALAC, CODEBASE, ENTRYPOINT, PERMISSIONS, TRUSTED])</p>
<dt>deployment.plugin.jvm.arguments</p>
<dd> null</p>
<dt>deployment.proxy.auto.config.url</p>
<dd> null (Possible: include any valid url (eg. <a rel="nofollow" href="http://icedtea.classpath.org/hg/))">http://icedtea.classpath.org/hg/))</a></p>
<dt>deployment.proxy.bypass.list</p>
<dd> null</p>
<dt>deployment.proxy.bypass.local</p>
<dd> null</p>
<dt>deployment.proxy.<a href="ftp://ftp.host">ftp.host</a></p>
<dd> null</p>
<dt>deployment.proxy.<a href="ftp://ftp.port">ftp.port</a></p>
<dd> null</p>
<dt>deployment.proxy.http.host</p>
<dd> null</p>
<dt>deployment.proxy.http.port</p>
<dd> null</p>
<dt>deployment.proxy.https.host</p>
<dd> null</p>
<dt>deployment.proxy.https.port</p>
<dd> null</p>
<dt>deployment.proxy.override.hosts</p>
<dd> null</p>
<dt>deployment.proxy.same</p>
<dd> false (Possible: are true or false)</p>
<dt>deployment.proxy.socks.host</p>
<dd> null</p>
<dt>deployment.proxy.socks.port</p>
<dd> null</p>
<dt>deployment.proxy.type</p>
<dd> 3 (Possible: are in range -1 to 3 (inclusive))</p>
<dt>deployment.security.askgrantdialog.notinca</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.security.askgrantdialog.show</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.security.expired.warning</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.security.jsse.hostmismatch.warning</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.security.level</p>
<dd> null (Possible: DENY_ALL DENY_UNSIGNED ASK_UNSIGNED ALLOW_UNSIGNED)</p>
<dt>deployment.security.notinca.warning</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.security.sandbox.awtwarningwindow</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.security.sandbox.jnlp.enhanced</p>
<dd> true (Possible: are true or false)</p>
<dt>deployment.security.trusted.policy</p>
<dd> null (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.system.cachedir</p>
<dd> null (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.system.security.cacerts</p>
<dd> $JAVA_HOME/lib/security/cacerts (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.system.security.jssecacerts</p>
<dd> $JAVA_HOME/lib/security/jssecacerts (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.system.security.policy</p>
<dd> null (Possible: include any valid url (eg. <a rel="nofollow" href="http://icedtea.classpath.org/hg/))">http://icedtea.classpath.org/hg/))</a></p>
<dt>deployment.system.security.trusted.certs</p>
<dd> $JAVA_HOME/lib/security/trusted.certs (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.system.security.trusted.clientautcerts</p>
<dd> $JAVA_HOME/lib/security/trusted.clientcerts (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.system.security.trusted.jssecerts</p>
<dd> $JAVA_HOME/lib/security/trusted.jssecerts (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.cachedir</p>
<dd> $XDG_CACHE_HOME/icedtea-web/cache (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.locksdir</p>
<dd> $TMP/$USER/netx/locks (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.logdir</p>
<dd> $XDG_CONFIG_HOME/icedtea-web/log (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.pcachedir</p>
<dd> $XDG_CACHE_HOME/icedtea-web/pcache (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.runningfile</p>
<dd> $TMP/$USER/netx/locks/netx_running (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.security.policy</p>
<dd> $XDG_CONFIG_HOME/icedtea-web/security/java.policy (Possible: include any valid url (eg. <a rel="nofollow" href="http://icedtea.classpath.org/hg/))">http://icedtea.classpath.org/hg/))</a></p>
<dt>deployment.user.security.trusted.cacerts</p>
<dd> $XDG_CONFIG_HOME/icedtea-web/security/trusted.cacerts (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.security.trusted.certs</p>
<dd> $XDG_CONFIG_HOME/icedtea-web/security/trusted.certs (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.security.trusted.clientauthcerts</p>
<dd> $XDG_CONFIG_HOME/icedtea-web/security/trusted.clientcerts (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.security.trusted.jssecacerts</p>
<dd> $XDG_CONFIG_HOME/icedtea-web/security/trusted.jssecacerts (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.security.trusted.jssecerts</p>
<dd> $XDG_CONFIG_HOME/icedtea-web/security/trusted.jssecerts (Possible: include an absolute path to a file or directory)</p>
<dt>deployment.user.tmp</p>
<dd> $XDG_CACHE_HOME/icedtea-web/tmp (Possible: include an absolute path to a file or directory) </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>$JAVA_HOME/lib/deployment.config</p>
<dd> java-global deployment properties file. May be affected by deployment.jre.dir.</p>
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
<dt>$XDG_CONFIG_HOME/icedtea-web/generated_jnlps</p>
<dd> Location where jnlp files generated from html pages for javaws applications desktop/menu launchers icons are stored</p>
<dt>$XDG_CONFIG_HOME/icedtea-web/icons</p>
<dd> Location where icons of javaws applications desktop/menu launchers icons are stored</p>
<dt>$XDG_CONFIG_HOME/icedtea-web/log</p>
<dd> contains file-log files (if enabled), itw-cplugin-date_time.log for native part of plugin, itw-javantx-date_time.log for everything else. Controlled by <code>deployment.user.logdir</code> </p>
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
