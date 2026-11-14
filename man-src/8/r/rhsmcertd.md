---
title: "rhsmcertd(8)"
name: "rhsmcertd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhsmcertd/"
description: "rhsmcertd – Periodically scans and updates the entitlement certificates on a registered system."
---

<p>rhsmcertd &#8211; Periodically scans and updates the entitlement certificates on a registered system. </p>
<h2>Synopsis</h2>
<p>rhsmcertd [&#8211;cert-check-interval=MINUTES] [&#8211;auto-attach-interval=MINUTES] [&#8211;now] [&#8211;debug] [&#8211;help] <i>Deprecated usage</i> rhsmcertd [<i>certInterval autoattachInterval</i>] </p>
<h2>Description</h2>
<p>Red Hat provides content updates and support by issuing <i>subscriptions</i> for its products. These subscriptions are applied to systems (machines). Red Hat Subscription Manager is a tool which allows administrators to manage those subscriptions by registering systems and people, applying subscriptions, and viewing subscriptions. When subscriptions are applied to a system or when new subscriptions are available, the subscription management system issues that machine an X.509 certificate which contains all of the details of that subscription. The <code>rhsmcertd</code> process runs periodically to check for changes in the subscriptions available to a machine by updating the entitlement certificates installed on the machine and by installing new entitlement certificates as they&#8217;re available. At a defined interval, the process checks with the subscription management service to see if any new subscriptions are available to the system. If there are, it pulls in the associated subscription certificates. If any subscriptions have expired and new subscriptions are available, then the <code>rhsmcertd</code> process will automatically request those subscriptions. This <code>rhsmcertd</code> process invokes the <code>rhsmcertd-worker.py</code> script to perform the certificate add and update operations. Both the certificate interval and the auto-attach interval are configurable and can be reset through the <code>rhsmcertd</code> daemon itself or by editing the Subscription Manager <code>/etc/rhsm/rhsm.conf</code> file. <code>rhsmcertd</code> is started with the machine, by default, and is always running in the background. </p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Prints the specific help information for the given command. </p>
<dt><code>-d, &#8211;debug</code></p>
<dd>Records more verbose output to the <code>/var/log/rhsm/rhsmcertd.log</code> log file. </p>
<dt><code>-n, &#8211;now</code></p>
<dd>Runs the <code>rhsmcertd</code> scan immediately, rather than waiting for the next scheduled interval. </p>
<dt><code>-c, &#8211;cert-check-interval=MINUTES</code></p>
<dd>Resets the interval for checking for new subscription certificates. This value is in minutes. The default is 240, or four hours. This interval is in effect until the daemon restarts, and then the values in the <code>/etc/rhsm/rhsm.conf</code> file are used (unless the argument is passed again). </p>
<dt><code>-i, &#8211;auto-attach-interval=MINUTES</code></p>
<dd>Resets the interval for checking for and replacing expired subscriptions. This value is in minutes. The default is 1440, or 24 hours. This interval is in effect until the daemon restarts, and then the values in the <code>/etc/rhsm/rhsm.conf</code> file are used (unless the argument is passed again). </p>
</dl>
<h2>Usage Examples</h2>
<dl>
<dt><code>NOTE</code></p>
<dd>Be sure to stop the running <code>rhsmcertd</code> daemon before making any configuration changes, or the new configuration is not applied. </p>
</dl>
<h3>Resetting The Certificate Scan Interval</h3>
<pre>service rhsmcertd stop
rhsmcertd --cert-check-interval=240</pre>
<h3>Running Certificate And Healing Scans Immediately</h3>
<p>Normally, the certificate and auto-attach scans are run periodically, on a schedule defined in the <code>rhsmcertd</code> configuration. The scans can be run immediately &#8212; which is useful if an administrator knows that there are new subscriptions available &#8212; and then the scans resume their schedules. </p>
<pre>service rhsmcertd stop
rhsmcertd -n</pre>
<h3>Deprecated Usage</h3>
<p><code>rhsmcertd</code> used to allow the certificate and auto-attach intervals to be reset simply by passing two integers as arguments. </p>
<p> <code>rhsmcertd</code> <i>certInterval autoAttachInterval</i> </p>
<p> For example: </p>
<pre>service rhsmcertd stop
rhsmcertd 180 480</pre>
<p>This usage is still allowed, but it is deprecated and not recommended.</p>
<h2>Associated Files</h2>
<dl>
<dd>* /usr/share/rhsm/certmgr.py</p>
<dd>* /etc/rhsm/rhsm.conf</p>
<dd>* /var/log/rhsm/rhsmcertd.log </p>
</dl>
<h2>Bugs</h2>
<p>This daemon is part of Red Hat Subscription Manager. To file bugs against this daemon, go to <a rel="nofollow" href="https://bugzilla.redhat.com,">https://bugzilla.redhat.com,</a> and select Red Hat &gt; Red Hat Enterprise Linux &gt; subscription-manager. </p>
<h2>Authors</h2>
<p>Deon Lackey, &lt;dlackey [at] redhat.com&gt; and Jeff Ortel, &lt;jortel [at] redhat.com&gt;. rhsmcertd was written by Jeff Ortel.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2010-2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
