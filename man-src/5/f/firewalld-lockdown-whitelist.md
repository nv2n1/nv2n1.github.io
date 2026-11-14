---
title: "firewalld-lockdown-whitelist(5)"
name: "firewalld-lockdown-whitelist"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-lockdown-whitelist/"
description: "firewalld.lockdown-whitelist – firewalld lockdown whitelist configuration file"
---

<p>firewalld.lockdown-whitelist &#8211; firewalld lockdown whitelist configuration file</p>
<h2>Synopsis</h2>
<pre><i>/etc/firewalld/lockdown-whitelists.xml</i></pre>
<h2>Description</h2>
<p>The firewalld lockdown-whitelist configuration file contains the selinux contexts, commands, users and user ids that are white-listed when firewalld lockdown feature is enabled (see <code><a href="/docs/linux/man/5-firewalld-conf/">firewalld.conf</a></code>(5) and <code><a href="/docs/linux/man/1-firewall-cmd/">firewall-cmd</a></code>(1)). This example configuration file shows the structure of an lockdown-whitelist file:</p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;whitelist&gt;
 &lt;selinux context=&quot;<i>selinuxcontext</i>&quot;/&gt;
 &lt;command name=&quot;<i>commandline</i>[*]&quot;/&gt;
 &lt;user {name=&quot;<i>username</i>|id=&quot;<i>userid</i>&quot;}/&gt;
&lt;/whitelist&gt;</pre>
</dl>
<h2>Options</h2>
<p>The config can contain these tags and attributes. Some of them are mandatory, others optional.</p>
<h3>whitelist</h3>
<p>The mandatory whitelist start and end tag defines the lockdown-whitelist. This tag can only be used once in a lockdown-whitelist configuration file. There are no attributes for this.</p>
<h3>selinux</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one selinux contexts entries. A selinux entry has exactly one attribute: </p>
<p> context=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The context is the security (SELinux) context of a running application or service. </p>
<p> To get the context of a running application use <code>ps -e &#8211;context</code> and search for the application that should be white-listed. </p>
<p> Warning: If the context of an application is unconfined, then this will open access for more than the desired application.</dl>
<h3>command</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one command entry. A command entry has exactly one attribute: </p>
<p> name=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The command <i>string</i> is a complete command line including path and also attributes. </p>
<p> If a command entry ends with an asterisk &#8216;*&#8217;, then all command lines starting with the command will match. If the &#8216;*&#8217; is not there the absolute command inclusive arguments must match. </p>
<p> Commands for user root and others is not always the same, the used path depends on the use of the <code>PATH</code> environment variable.</dl>
<h3>user</h3>
<p>Is an optional empty-element tag and can be used several times to white-list more than one user. A user entry has exactly one attribute of these: </p>
<p> name=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The user with the name <i>string</i> will be white-listed.</dl>
<p> id=&quot;<i>integer</i>&quot;</p>
<dl>
<dd>The user with the id <i>userid</i> will be white-listed.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-firewall-applet/">firewall-applet</a></code>(1), <code><a href="/docs/linux/man/1-firewalld/">firewalld</a></code>(1), <code><a href="/docs/linux/man/1-firewall-cmd/">firewall-cmd</a></code>(1), <code><a href="/docs/linux/man/1-firewall-config/">firewall-config</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-conf/">firewalld.conf</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-dbus/">firewalld.dbus</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5), <code><a href="/docs/linux/man/1-firewall-offline-cmd/">firewall-offline-cmd</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zones/">firewalld.zones</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5)</p>
<h2>Notes</h2>
<p>firewalld home page:</p>
<dl>
<dd>m[blue]<code><a rel="nofollow" href="http://www.firewalld.org">http://www.firewalld.org</a></code>m[]</dl>
<p> More documentation with examples:</p>
<dl>
<dd>m[blue]<code><a rel="nofollow" href="http://fedoraproject.org/wiki/FirewallD">http://fedoraproject.org/wiki/FirewallD</a></code>m[]</dl>
<h2>Authors</h2>
<p><code>Thomas Woerner</code> &lt;twoerner [at] redhat.com&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Jiri Popelka</code> &lt;jpopelka [at] redhat.com&gt;</p>
<dl>
<dd>Developer</dl>
