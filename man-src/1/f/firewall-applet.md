---
title: "firewall-applet(1)"
name: "firewall-applet"
section: "1"
letter: "f"
url: "/docs/linux/man/1-firewall-applet/"
description: "firewall-applet – firewalld applet"
---

<h2 class="name">NAME</h2>
<p> firewall-applet &#8211; firewalld applet </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>firewall-applet</code> [OPTIONS&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>firewall-applet is a tray applet for firewalld.</p>
<h2>OPTIONS</h2>
<p> <code>firewall-applet</code> does not support any special options. </p>
<p> The following options are supported: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints a short help text and exists.</dl>
<h2>QSETTINGS</h2>
<p> <code>firewall-applet</code> has additional settings to adapt the look and feel. QSettings is used and stores them in <i>~/.config/firewall/applet.conf</i>. The file is automatically reloaded if it has been changed and the new settings will immediately be effective. </p>
<p> There is also the global config file <i>/etc/firewall/applet.conf</i>, which contains the default values. The settings in this file will be overloaded by settings in the user settings file. </p>
<p> Here is an example <i>applet.conf</i> file: </p>
<dl>
<dt>
<dd>
<pre>
[General]
notifications=true
show-inactive=true
      
</pre>
</dl>
<p> The following settings are supported: </p>
<p> <code>notifications</code></p>
<dl>
<dt>
<dd> The applet shows notifications if enabled. This setting can be enabled also in the applet with the &quot;Enable Notifications&quot; checkbox in the right mouse menu. </p>
<p> This setting defaults to <code>false</code>. </p>
<p> If notifications are shown for these actions if enabled: </p>
<dl>
<dt>
<dd> &bull; Connection to firewalld established</dl>
<dl>
<dt>
<dd> &bull; Connection to firewalld lost</dl>
<dl>
<dt>
<dd> &bull; Firewall has been reloaded</dl>
<dl>
<dt>
<dd> &bull; Default zone has been changed</dl>
<dl>
<dt>
<dd> &bull; Panic mode has been enabled or disabled</dl>
<dl>
<dt>
<dd> &bull; Activation, deactivation or change of zones bound to interfaces</dl>
<dl>
<dt>
<dd> &bull; Activation, deactivation or change of zones bound to sources addresses</dl>
</dl>
<p> <code>show-inactive</code></p>
<dl>
<dt>
<dd> Show applet also if firewalld is not running. If firewalld has been stopped or is not running the applet will be hidden and not visible in the applet tray. Enable this setting to see the applet all the time for example to be sure that the firewall is active. </p>
<p> This setting defaults to <code>false</code>.</dl>
<p> <code>shields-up</code></p>
<dl>
<dt>
<dd> The shields-up zone name to be used if shields-up is enabled. </p>
<p> This setting defaults to &#8216;<code>block</code>&#8216;.</dl>
<p> <code>shields-down</code></p>
<dl>
<dt>
<dd> The shields-down zone name to be used if shields-up has been deactivated again. </p>
<p> This setting defaults to &#8216;<code>public</code>&#8216;.</dl>
<p> <code>blink</code></p>
<dl>
<dt>
<dd> If enabled, the applet icon blinks in these cases: </p>
<dl>
<dt>
<dd> &bull; Connection to firewalld lost</dl>
<dl>
<dt>
<dd> &bull; Panic mode has been enabled or disabled</dl>
<p> This setting defaults to <code>false</code>.</dl>
<p> <code>blink-count</code></p>
<dl>
<dt>
<dd> The number of blinks if <code>blink</code> is enabled. </p>
<p> This setting defaults to <code>5</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-firewall-applet/">firewall-applet</a></code>(1), <code><a href="/docs/linux/man/1-firewalld/">firewalld</a></code>(1), <code><a href="/docs/linux/man/1-firewall-cmd/">firewall-cmd</a></code>(1), <code><a href="/docs/linux/man/1-firewall-config/">firewall-config</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-conf/">firewalld.conf</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-dbus/">firewalld.dbus</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5), <code><a href="/docs/linux/man/1-firewall-offline-cmd/">firewall-offline-cmd</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zones/">firewalld.zones</a></code>(5)</p>
<h2>NOTES</h2>
<p> firewalld home page:</p>
<dl>
<dt>
<dd> m[blue]<code><a rel="nofollow" href="http://www.firewalld.org">http://www.firewalld.org</a></code>m[]</dl>
<p> More documentation with examples:</p>
<dl>
<dt>
<dd> m[blue]<code><a rel="nofollow" href="http://fedoraproject.org/wiki/FirewallD">http://fedoraproject.org/wiki/FirewallD</a></code>m[]</dl>
<h2>AUTHORS</h2>
<p> <code>Thomas Woerner</code> &lt;twoerner [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<p> <code>Jiri Popelka</code> &lt;jpopelka [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<h2>Index</h2>
