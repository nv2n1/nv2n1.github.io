---
title: "rhsm-icon(8)"
name: "rhsm-icon"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhsm-icon/"
description: "rhsm-icon – Periodically checks installed products against active subscriptions to check their status."
---

<p>rhsm-icon &#8211; Periodically checks installed products against active subscriptions to check their status. </p>
<h2>Synopsis</h2>
<p>rhsm-icon [&#8211;check-period] [&#8211;force-icon=warning|expired|partial] [&#8211;check-immediately] </p>
<h2>Description</h2>
<p>Red Hat provides content updates and support by issuing <i>subscriptions</i> for its products. These subscriptions are applied to systems (machines) and apply to the installed software products. On graphical X systems (systems with a GUI interface), a product status daemon runs every 4 hours to check the currently installed software against the applied subscriptions. If software is installed without a valid and applied subscription (such as a subscription expires or no subscription is available for the product), then the daemon triggers an icon and warning message to display in the notification area of the menu. <code>rhsm-icon</code><br />
&nbsp;<wbr>only runs on graphical&nbsp;<wbr>(X-based)&nbsp;<wbr>systems. Servers which do not have a GUI interface do not run or require the <code>rhsm-icon</code> daemon. </p>
<h2>Options</h2>
<dl>
<dt><code>-c, &#8211;check-period</code></p>
<dd>Sets the interval to use between checks for the product subscription status. The value is in seconds and the default is one day. </p>
<dt><code>-f, &#8211;force-icon=TYPE</code></p>
<dd>Manually displays the given type of icon in the start menu. The TYPE can be <i>warning</i>, <i>expired</i>, or <i>partial</i> and uses a different icon for each type of message. </p>
<dt><code>&#8211;i, &#8211;check-immediately</code></p>
<dd>Runs the status check process immediately when the command is invoked. Otherwise, there is a four (4) minute delay before running the initial check. </p>
<dt><code>-d, &#8211;debug</code></p>
<dd>Shows debug messages for the daemon. </p>
</dl>
<h2>Usage</h2>
<p>There are two reasons to invoke <code>rhsm-icon</code> manually: </p>
<dl>
<dd>* To run the daemon on a new schedule (immediately or with a different frequency) </p>
<dd>* To view the status icons or messages regardless of the state of the machine </p>
</dl>
<p> Since X runs the daemon automatically and on schedule, it is not necessary to launch the subscription status daemon manually. The <code>rhsm-icon</code> command can change this schedule. For example: </p>
<pre>rhsm-icon --check-period 120</pre>
<p>Administrators can also run <code>rhsm-icon</code> to view any immediate changes to the subscription status of the system. Using the <code>&#8211;check-immediately</code> option runs the check at the time the command is run; otherwise, running <code>rhsm-icon</code> has a four-minute delay before running the status check. </p>
<pre>rhsm-icon --check-immediately</pre>
<p>If you just want to know what the different subscription status messages look like, then use the <code>&#8211;force-icon</code> option. (Also use the <code>&#8211;check-immediately</code> option, or the scan will take the standard four minutes to run and display the icon.) </p>
<pre>rhsm-icon --force-icon=warning --check-immediately
rhsm-icon --force-icon=expired --check-immediately
rhsm-icon --force-icon=partial --check-immediately</pre>
<h2>Bugs</h2>
<p>This daemon is part of Red Hat Subscription Manager. To file bugs against this daemon, go to <a rel="nofollow" href="https://bugzilla.redhat.com,">https://bugzilla.redhat.com,</a> and select Red Hat &gt; Red Hat Enterprise Linux &gt; subscription-manager. </p>
<h2>Authors</h2>
<p>Deon Lackey, &lt;dlackey [at] redhat.com&gt;, and James Bowes, &lt;jbowes [at] redhat.com&gt;. rhsm-icon was written by James Bowes.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2010-2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
