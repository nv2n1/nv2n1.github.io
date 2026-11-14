---
title: "subscription-manager-gui(8)"
name: "subscription-manager-gui"
section: "8"
letter: "s"
url: "/docs/linux/man/8-subscription-manager-gui/"
description: "subscription-manager-gui – Launches the UI client of the Subscription Manager."
---

<p>subscription-manager-gui &#8211; Launches the UI client of the Subscription Manager. </p>
<h2>Synopsis</h2>
<p>subscription-manager-gui [&#8211;register] </p>
<h2>Description</h2>
<p><code>subscription-manager-gui</code> opens the local client tool to manage subscriptions and installed products on Red Hat Enterprise Linux systems. The same tasks that can be performed by invoking <code>subscription-manager</code> can be performed in the GUI, including registering systems with a subscription management service, applying and removing subscriptions, and viewing the subscription status of installed products. The Subscription Manager UI can also be opened by selecting the <code>Red Hat Subscription Manager</code> item from the <code>Applications &gt; System Tools</code> menu in RHEL 5.x and RHEL 7.x, or the <code>System &gt; Administration</code> menu in RHEL 6.x. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;register</code></p>
<dd>If a system has not yet been registered, then the GUI registration page can be opened immediately, as the Subscription Manager GUI comes up. This is only relevant for unregistered systems; if this is used after a system is registered, the option is ignored. </p>
</dl>
<h2>References</h2>
<p>For procedures and tasks that can be performed in the Subscription Manager UI, check the Gnome help files (by pressing &lt;F1&gt;) or refer to the RHEL Subscription Management Guide at &lt;<a rel="nofollow" href="https://access.redhat.com/documentation/en-US/Red_Hat_Subscription_Management/1/html/RHSM/index.html">https://access.redhat.com/documentation/en-US/Red_Hat_Subscription_Management/1/html/RHSM/index.html</a>&gt;.</p>
<h2>Associated Files</h2>
<dl>
<dd>* /usr/sbin/subscription-manager-gui</p>
<dd>* /usr/sbin/subscription-manager</p>
<dd>* /etc/rhsm/rhsm.conf </p>
</dl>
<h2>Bugs</h2>
<p>This client is part of Red Hat Subscription Manager. To file bugs against this client, go to <a rel="nofollow" href="https://bugzilla.redhat.com,">https://bugzilla.redhat.com,</a> and select Red Hat &gt; Red Hat Enterprise Linux &gt; subscription-manager. </p>
<h2>Authors</h2>
<p>Deon Lackey, &lt;dlackey [at] redhat.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2010-2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
