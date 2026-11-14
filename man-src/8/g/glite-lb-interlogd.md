---
title: "glite-lb-interlogd(8)"
name: "glite-lb-interlogd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glite-lb-interlogd/"
description: "glite-lb-interlogd – interlogger daemon"
---

<p>glite-lb-interlogd &#8211; interlogger daemon</p>
<h2>Synopsis</h2>
<p><code>glite-lb-interlogd</code> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>glite-lb-interlogd </code> takes over L&amp;B events from glite-lb-logd and it is responsible for reliable transfer to their target storage &#8211; bookkeeping and logging servers. Interlogger maintains message queues for each target server and implements reliable handling in environment with possible communication failures. On startup (and then periodically during operation) interlogger checks the event files (created by glite-lb-logd, see also the -f option), spawns a thread for each target server, and populates the queues with events read from the files. Then it starts listening for further incoming events on the UNIX socket (see the -s option). The queue threads periodically attempt to contact the destination servers and to deliver the pending events. Eventually, when all events from a file are delivered the file is removed after a certain timeout by a clean-up thread. Possible race conditions wrt. glite-lb-logd are prevented by locking the files appropriately. </p>
<h2>Options</h2>
<dl>
<dt><code>-b</code>, &#8211;book</p>
<dd>Send events only to bookkeeping server. This option has effect only if the logging server address is specified through the -l option. There is no implementation of logging server currently.<br />
&nbsp;<wbr></p>
<dt><code>-c</code><i> FILE</i>, &#8211;cert <i>FILE</i></p>
<dd>Get certificate from <i>FILE</i>. This option overrides the $X509_USER_CERT environment variable. </p>
<dt><code>-k</code><i> FILE</i>, &#8211;key <i>FILE</i></p>
<dd>Get server private key from <i>FILE</i>. This option overrides the $X509_USER_KEY environment variable. </p>
<dt><code>-C</code><i> DIR</i>, &#8211;CAdir <i>DIR</i></p>
<dd>Look for trusted CA&#8217;s certificates in <i>DIR</i>. This option overrides the $X509_CERT_DIR environment variable. </p>
<dt><code>-d</code>, &#8211;debug</p>
<dd>Don&#8217;t run as daemon (do not fork and put itself into background). Additional diagnostics are not enabled, they can be configured through log4c instead. </p>
<dt><code>-i</code><i> FILE</i>, &#8211;pidfile <i>FILE</i></p>
<dd>Store process id into this file rather than default /var/run/glite/glite-lb-[notif|proxy]-interlogd.pid </p>
<dt><code>-f</code><i> PREFIX</i>, &#8211;file-prefix <i>PREFIX</i></p>
<dd><i>PREFIX </i> is path prefix of the event files. </p>
<p> For each job (jobid) a specific file is created that stores all events associated with this job. The job filename is constructed by stripping the protocol+server prefix from the jobid and appending the rest to this <i>PREFIX.</i> </p>
<p> <i>PREFIX</i> defaults to /var/spool/glite/lb-locallogger/dglogd.log, /var/spool/glite/lb-proxy/dglogd.log, or /var/spool/glite/lb-notif/dglogd.log. </p>
<p> On startup, interlogger checks all files matching the pattern <i>PREFIX*.</i> </p>
<p> The value has to be same as used in the cooperating glite-lb-logd (or glite-lb-bkserverd for proxy). </p>
<dt><code>-k</code><i> FILE</i>, &#8211;key <i>FILE</i></p>
<dd>Get private key from <i>FILE</i>. This option overrides the $X509_USER_KEY environment variable. </p>
<dt><code>-l</code><i> HOST</i>, &#8211;log-server <i>HOST</i></p>
<dd>Use <i>HOST</i> as address of logging server. As the logging is not implemented yet this option should not be used. </p>
<dt><code>-s</code><i> PATH</i>, &#8211;socket <i>PATH</i></p>
<dd>Listen for events sent by glite-lb-logd at the UNIX socket <i>PATH.</i> </p>
<dt><code>-V</code>, &#8211;version</p>
<dd>Print version and exit. </p>
<dt><code>-L</code><i> TIMEOUT</i>, &#8211;lazy <i>TIMEOUT</i></p>
<dd>Be lazy when closing connections to servers (default, <i>TIMEOUT</i> ==0 means turn lazy off). </p>
<dt><code>-h</code>, &#8211;help</p>
<dd>Print help and exit. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/run/glite-lb-*.sock</i></p>
<dd>Default name of local socket for logger, notification logger and proxy logger.</p>
<dt><i>/var/spool/glite/lb-*/dglogd.log*</i></p>
<dd>Default locations of event files.</p>
<dt><i>/var/spool/glite/lb-*/dglogd.log*.ctl</i></p>
<dd>Interlogger&#8217;s control files keeping the information on status of the corresponding event file wrt. delivery to the target server. </p>
<dt>No configuration files needed.</p>
<dd></dl>
<h2>Environment</h2>
<dl>
<dt><code>X509_USER_KEY</code></p>
<dd>If $X509_USER_KEY is set, it is used to locate private key file. </p>
<dt><code>X509_USER_CERT</code></p>
<dd>If $X509_USER_CERT is set, it is used to locate certificate file. </p>
<dt><code>X509_CERT_DIR</code></p>
<dd>If $X509_CERT_DIR is set, it is used to locate the trusted CA&#8217;s certificates and ca-signing-policy files. </p>
<dt><code>X509_USER_PROXY</code></p>
<dd>If $X509USER_PROXY is set, it is used to locate proxy certificate file. </p>
</dl>
<h2>Bugs</h2>
<p>Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a></code>(8), <a href="/docs/linux/man/8-glite-lb-logd/">glite-lb-logd</a>(8), <a href="/docs/linux/man/1-glite-lb-logevent/">glite-lb-logevent</a>(1), </p>
<h2>Author</h2>
<p>EU EGEE, JRA1.</p>
