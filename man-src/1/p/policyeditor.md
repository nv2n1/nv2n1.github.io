---
title: "policyeditor(1)"
name: "policyeditor"
section: "1"
letter: "p"
url: "/docs/linux/man/1-policyeditor/"
description: "policyeditor – view and modify security policy settings for javaws and the browser plugin"
---

<h2 class="name">NAME</h2>
<p> policyeditor &#8211; view and modify security policy settings for <code>javaws </code> and the <code>browser plugin</code></p>
<h2>SYNOPSIS</h2>
<p> <code>policyeditor </code><br />
 <code>policyeditor [-file] </code> policy_file <code>[-codebase] </code> url</p>
<h2>DESCRIPTION</h2>
<p> <code>policyeditor </code> is a GUI application with small command line support to view and edit applet security policy settings used by the IcedTea-Web implementation of <code>javaws </code> and the <code>browser plugin. </code> It is intended as a simpler, easier to use, and more accessible alternative to the standard <code>JDK Policy Tool. </code> Administrators and power users who need fine grained control over policy files should probably use Policy Tool instead of PolicyEditor. </p>
<p> If executed without any arguments, no file is opened, and saving the file will result in a prompt on where to save it. Otherwise, if a file path is given as a command line argument, then that file path will be opened and parsed as policy file. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-codebase url</p>
<dd> Specifies an applet codebase URL. If the specified codebase already exists in the policy file (if any), then it will be selected when the editor opens. If it is a new codebase then it will be added and selected. Multiple URLs may also be given with a single -codebase flag by separating them with spaces. In this case, the last codebase given will be selected, and all will be added. If this flag is given more than once, only the first is used.(Expected one or more arguments)</p>
<dt>-defaultfile</p>
<dd> Specifies that the default user-level policy file should be opened. This is the file which is normally used by IcedTea-Web to make decisions about custom policies and permissions for applets at runtime, unless configured otherwise.(No argument expected)</p>
<dt>-file policy_file</p>
<dd> Specifies a policy file path to open. If exactly one argument is given, and it is not this flag, it is interpreted as a file path to open, as if this flag was given first. This flag exists mostly for compatibility with Policy Tool, but is also needed when opening a policy file and also using the -codebase flag.(Exactly one argument expected)</p>
<dt>-help</p>
<dd> Prints out information about supported command and basic usage.(No argument expected)</p>
<dt>-verbose</p>
<dd> Enable verbose output.(No argument expected) </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>policyeditor</p>
<dd> Show the GUI editor with no file opened.</p>
<dt>policyeditor -file $XDG_CONFIG_HOME/icedtea-web/security/java.policy</p>
<dd> Show GUI and opens the default policy file. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>$XDG_CACHE_HOME/icedtea-web/cache/recently_used</p>
<dd> Additional information about items in cache</p>
<dt>$XDG_CONFIG_HOME/icedtea-web/security/java.policy</p>
<dd> Contains granted permissions for selected unsigned apps. Controlled by <code>deployment.user.security.policy</code> </p>
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
