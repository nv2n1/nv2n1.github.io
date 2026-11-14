---
title: "glite-lb-notify(1)"
name: "glite-lb-notify"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-notify/"
description: "glite-lb-notify – Register and receive notification from L&B"
---

<h2 class="name">NAME</h2>
<p> glite-lb-notify &#8211; Register and receive notification from L&amp;B</p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-notify </code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>new</code> [ { <code>-s</code><i> socket_fd</i> | <code>-a </code><i>fake_addr</i> } <code>-t </code><i>requested_validity</i> <code>-j </code><i>jobid </i>| { <code>-o </code><i>owner </i> | <code>-O </code> } <code>-n </code><i>network_server </i> <code>-v</code><i> virtual_organization</i> <code>-c</code> <code>-J</code> <code>-B</code> <code>-T</code> <code>-E</code> <code>-f</code><i> flags</i> ] </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>bind </code> [ { <code>-s</code><i> socket_fd</i> | <code>-a </code><i>fake_addr</i> } <code>-t </code><i>requested_validity</i> ] <i>notifid</i></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>change </code> <i>notifid</i> <i>jobid</i></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>refresh</code> [ <code>-t </code><i>requested_validity </i> ] notifid</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>receive</code> [ { <code>-s</code><i> socket_fd</i> | <code>-a </code><i>fake_addr</i> } <code>-t </code><i>requested_validity</i> ] [ <code>-i </code><i>timeout </i>] [ <code>-r</code>] [ <code>-f</code><i> field1,field2</i>,&#8230; <i>notifid</i></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>drop</code> <i>notifid</i></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-notify </code> is a fairly simple wrapper on the L&amp;B notification API. It allows to create a notification (with a restricted richness of specifying conditions), bind to it for receiving notifications, and drop it finally. </p>
<p> L&amp;B notification is a user-initiated trigger at the server. Whenever a job enters a state matching conditions specified with the notification, the current state of the job is sent to the notification client. On the other hand, the notification client is a network listener which receives server-initiated connections to get the notifications. Unless <code>-s</code> is specified, the notification library creates the listener socket. </p>
<p> Within the notification validity, clients can disappear and even migrate. However, only a single active client for a notification is allowed. </p>
<p> This command is intended to be used in user scripts, graphical tools etc. where direct access to the API is difficult. </p>
<p> L&amp;B server and port to contact is specified with GLITE_WMS_NOTIF_SERVER environment variable. </p>
<h2>USAGE</h2>
<p> Common options (mostly)</p>
<dl>
<dt><code>-t</code></p>
<dd> specifies a requested validity of the notification (in seconds of UNIX Epoch), the server can truncate the value according to its policy.</p>
<dt><code>-a</code></p>
<dd> allows to specify a fake listener address to register with the notification, i.e. to overcome firewalls etc. When notifications are delivered, the server tries to connect to this address rather than the true address of the listening socket. Requires re-binding therefore it can&#8217;t be used in conjunction with <code>-s</code></p>
<dt><code>-s</code></p>
<dd> allows to pass a opened listening socket (filedescriptor number), see EXAMPLE bellow. In this case there is no need to re-bind the notification (it is assumed the socket is recycled) This is critical for a real usage, as the re-bind operation is rather expensive. </p>
</dl>
<h2>&nbsp;<wbr></h2>
<p> Subcommands:</p>
<dl>
<dt><code>new</code></p>
<dd> Create a new notification. Conditions on matching jobs are specified with exacltly one of <code>-j</code>, <code>-o</code>, <code>-n,</code> <code>-v</code> options. If the option <code>-O</code> is used, credentials are retrieved from environment. The <code>-c</code> set matching only on state change. Prints ID of the created notification. </p>
<dt><code>bind</code></p>
<dd>
<p> Binds to an existing notification, changing its listener eventually. Useful for debugging purposes mostly. </p>
<dt><code>change</code></p>
<dd>
<p> Connect notification with another job. </p>
<dt><code>refresh</code></p>
<dd>
<p> Extend validity of an existing notification. </p>
<dt><code>receive</code></p>
<dd>
<p> Bind to an existing notification, and start waiting for an incoming event, at most the time specified with <code>-i</code> (seconds). <code>-r</code> attempts to refresh the notification handle in 1/2 of current validity. <code>-f</code> allows to specify a custom list of fields of the job status to display. Run <code>glite-lb-notify</code> to get list of available fields. </p>
<dt><code>drop</code></p>
<dd>
<p> Drop the notification from the server, removing all messages on the way eventually. </p>
</dl>
<h2>&nbsp;<wbr></h2>
<p> Options for the <code>new</code> subcommand:</p>
<dl>
<dt><code>-o</code></p>
<dd> match on events for jobs belonging to the given <i>DN</i>.</p>
<dt><code>-O</code></p>
<dd> match on events for jobs belonging to the current user.</p>
<dt><code>-v</code></p>
<dd> match on events for jobs belonging to users from the given <i>VO</i>.</p>
<dt><code>-c</code></p>
<dd> match only if job state has actually changed. Notification messages won&#8217;t be sent for events that do not trigger job state change.</p>
<dt><code>-S</code></p>
<dd> match only on jobs in certain <i>states</i> listed in a comma-separated list.</p>
<dt><code>-J</code></p>
<dd> pack JDL with the job status structure.</p>
<dt><code>-B</code></p>
<dd> bootstrap &#8212; send past events matching conditions.</p>
<dt><code>-T</code></p>
<dd> match only on reaching a terminal state.</p>
<dt><code>-H</code></p>
<dd> match only on reaching a terminal state and pack all events for that job.</p>
<dt><code>-N</code></p>
<dd> anonymize all owner data in all messages under this registration. </p>
</dl>
<h2>EXAMPLE</h2>
<p> Installed with the package as share/examples/glite-lb-notify.pl. Demontstrates using the non-trivial <code>-s</code> option. </p>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a></code>(8), <a href="/docs/linux/man/8-glite-lb-interlogd/">glite-lb-interlogd</a>(8), <a href="/docs/linux/man/8-glite-lb-logd/">glite-lb-logd</a>(8) </p>
<p> L&amp;B Users Guide, <a rel="nofollow" href="http://www.glite.org">http://www.glite.org</a> </p>
<h2>AUTHOR</h2>
<p> EU EGEE, JRA1. </p>
<h2>Index</h2>
