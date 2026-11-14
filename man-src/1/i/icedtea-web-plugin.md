---
title: "icedtea-web-plugin(1)"
name: "icedtea-web-plugin"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icedtea-web-plugin/"
description: "icedtea-web-plugin – allow to run java applets in your favorite browser"
---

<h2 class="name">NAME</h2>
<p> icedtea-web-plugin &#8211; allow to run <code>java applets </code> in your favorite <code>browser</code></p>
<h2>SYNOPSIS</h2>
<p> <code>icedtea-web-plugin </code> is working in your browser, once your browser knows about this files. </p>
<p> The IcedTeaPlugin.so must be placed, or linked inside specific directories. See <a rel="nofollow" href="http://icedtea.classpath.org/wiki/IcedTea-Web#Plugin">http://icedtea.classpath.org/wiki/IcedTea-Web#Plugin</a> </p>
<p> <code>Mozilla compatible browsers </code> like Firefox, Midori, Epiphany, Chrome or Chromium use: </p>
<dl>
<dt>$HOME/.mozilla/plugins</p>
<dd> Location of plugin library for user&#8217;s purposes on Mozilla compliant browser.</p>
<dt>/usr/lib64/mozilla/plugins</p>
<dd> Location of plugin library for global purposes on Mozilla compliant browser, 64-bit systems.</p>
<dt>/usr/lib/mozilla/plugins</p>
<dd> Location of plugin library for global purposes on Mozilla compliant browser, 32-bit systems. </p>
</dl>
<p> <code>Opera family browsers </code> like Opera use: </p>
<dl>
<dt>/usr/lib64/opera/plugins</p>
<dd> Location of plugin library for global purposes on opera compliant browser, 64-bit systems.</p>
<dt>/usr/lib/opera/plugins</p>
<dd> Location of plugin library for global purposes on opera compliant browser, 32-bit systems. </p>
</dl>
<p> All third-party trademarks are the property of their respective owners </p>
<h2>FILES</h2>
<dl>
<dt>$HOME/.mozilla/plugins/IcedTeaPlugin.so</p>
<dd> Location of plugin library for user&#8217;s purposes on Mozilla compliant browser.</p>
<dt>$XDG_CACHE_HOME/icedtea-web/cache/recently_used</p>
<dd> Additional information about items in cache</p>
<dt>$XDG_CONFIG_HOME/icedtea-web/generated_jnlps</p>
<dd> Location where jnlp files generated from html pages for javaws applications desktop/menu launchers icons are stored</p>
<dt>$XDG_RUNTIME_DIR/tmp/icedteaplugin-user-*</p>
<dd> Contains in and out pipe for native2java communication and (if enabled) debugging pipe.</p>
<dt>/usr/lib/mozilla/plugins/IcedTeaPlugin.so</p>
<dd> Location of plugin library for global purposes on Mozilla compliant browser, 32-bit systems.</p>
<dt>/usr/lib/opera/plugins/IcedTeaPlugin.so</p>
<dd> Location of plugin library for global purposes on opera compliant browser, 32-bit systems.</p>
<dt>/usr/lib64/mozilla/plugins/IcedTeaPlugin.so</p>
<dd> Location of plugin library for global purposes on Mozilla compliant browser, 64-bit systems.</p>
<dt>/usr/lib64/opera/plugins/IcedTeaPlugin.so</p>
<dd> Location of plugin library for global purposes on opera compliant browser, 64-bit systems. </p>
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
