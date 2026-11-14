---
title: "rhnsd(8)"
name: "rhnsd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhnsd/"
description: "rhnsd – A program for querying the Spacewalk server for updates and information."
---

<p>rhnsd &#8211; A program for querying the Spacewalk server for updates and information.</p>
<h2>Synopsis</h2>
<p>rhn_check [<i>options</i>] </p>
<h2>Description</h2>
<p><code>rhnsd</code> is a background daemon process that periodically polls the Spacewalk server to see if there are any queued actions available. If any are queued, rhnsd will execute those actions. rhnsd is typically started from the initialization (init) scripts in <i>/etc/init.d/rhnsd</i>. when it&#8217;s time to poll the Spacewalk server for available updates and actions. The default interval is every 240 minutes. The minimum polling interval is 60 minutes. To check for updates, rhnsd runs an external program called <code>rhn_check</code>. This is a small application that actually makes the network connection to Spacewalk. The rhnsd daemon does not listen on any network ports, nor does it ever talk to the network directly. Any network activity is done via the <code>rhn_check</code> utility. rhnsd can be configured by editing the <i>/etc/sysconfig/rhn/rhnsd</i>. configuration file. This is actually the configuration file the rhnsd initialization script <i>/etc/init.d/rhnsd</i>. uses. </p>
<h2>Options</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;interval</code></p>
<dd>Specify the interval that rhnsd should wait between checking the Spacewalk. Default is 240 minutes, the minimum is 60 minutes. This can also be specified in <i>/etc/sysconfig/rhn/rhnsd</i> </p>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd>force the rhnsd process to run in the foreground instead of automatically backgrounding itself, as it does by default. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sysconfig/rhn/rhnsd</i></p>
<dd>Configuration settings for the rhnsd daemon&#8217;s initialization script. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rhn_check/">rhn_check</a></code>(8), <code><a href="/docs/linux/man/8-rhn_register/">rhn_register</a></code>(8), <code><a href="/docs/linux/man/8-rhnsd/">rhnsd</a></code>(8), <code><a href="/docs/linux/man/8-rhn-profile-sync/">rhn-profile-sync</a></code>(8), <code><a href="/docs/linux/man/8-rhnplugin/">rhnplugin</a></code>(8), <code><a href="/docs/linux/man/5-up2date/">up2date</a></code>(5). </p>
<h2>Authors</h2>
<p>Preston Brown &lt;pbrown [at] redhat.com&gt;<br />
 Cristian Gafton &lt;gafton [at] redhat.com&gt;<br />
 Adrian Likins &lt;alikins [at] redhat.com&gt;<br />
 James Bowes &lt;jbowes [at] redhat.com&gt;</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;. </p>
<h2>Copyright</h2>
<p>Copyright &#169; 1999-2006 Red Hat, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
