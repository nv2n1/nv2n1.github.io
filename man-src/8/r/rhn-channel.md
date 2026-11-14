---
title: "rhn-channel(8)"
name: "rhn-channel"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhn-channel/"
description: "spacewalk-channel – Subscribe to or unsubscribe system from channel."
---

<p>spacewalk-channel &#8211; Subscribe to or unsubscribe system from channel.</p>
<h2>Synopsis</h2>
<p>spacewalk-channel [<i>options</i>] </p>
<h2>Description</h2>
<p>spacewalk-channel allows you to subscribe to and unsubscribe from specified channels via the command line. A visit to the &quot;<code>Red Hat Satellite</code>&quot; website isn&#8217;t required. </p>
<h2>Options</h2>
<dl>
<dt><code>-l, &#8211;list</code></p>
<dd>Print a list of channel(s) that you are currently subscribed to. </p>
<dt><code>-b, &#8211;base</code></p>
<dd>Print a base channel that you are currently subscribed to. </p>
<dt><code>-L, &#8211;available-channels</code></p>
<dd>Print a list of all available child channels. </p>
<dt><code>-a, &#8211;add</code></p>
<dd>You are subscribing system to given channel(s). You have to specify &#8211;user and &#8211;password. </p>
<dt><code>-r, &#8211;remove</code></p>
<dd>You are unsubscribing system to given channel(s). You have to specify &#8211;user and &#8211;password. </p>
<dt><code>-u, &#8211;user</code></p>
<dd>Your username used to register the system with and for Red Hat Satellite. If you do not enter this option and it is required, you will be prompted. </p>
<dt><code>-p, &#8211;password</code></p>
<dd>The password associated with the username specified with the <code>&#8211;user</code> option. This is an unencrypted password. If you do not enter this option and it is required, you will be prompted. </p>
<dt><code>-c, &#8211;channel</code></p>
<dd>Label of channel you want to subscribe to or unsubscribe from. Can be specified multiple times. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Print out successfull action. </p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show a help message and exit. </p>
</dl>
<h2>Note</h2>
<p>The addition and removal of channels is mutually exclusive, please use the command twice.</p>
<h2>Examples</h2>
<p>Subscribe to two channels:</p>
<dl>
<dd>
<pre>spacewalk-channel --add -c rhn-tools-rhel-i386-server-5 -c rhel-i386-server-vt-5 --user username --password password</pre>
</dl>
<p> Unsubscribe from channel:</p>
<dl>
<dd>
<pre>spacewalk-channel --remove -c rhn-tools-rhel-i386-server-5 -c rhel-i386-server-vt-5 --user username --password password</pre>
</dl>
<p> List subscribed channels:</p>
<dl>
<dd>
<pre>spacewalk-channel --list</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rhnplugin/">rhnplugin</a></code>(8), <code><a href="/docs/linux/man/8-rhn_register/">rhn_register</a></code>(8), <code><a href="/docs/linux/man/5-up2date/">up2date</a></code>(5). </p>
<h2>Authors</h2>
<p>Miroslav Suchý &lt;msuchy [at] redhat.com&gt;</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;. </p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2010 Red Hat, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
