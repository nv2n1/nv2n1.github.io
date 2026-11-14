---
title: "glite-lb-logd(8)"
name: "glite-lb-logd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glite-lb-logd/"
description: "glite-lb-logd – local logger daemon"
---

<p>glite-lb-logd &#8211; local logger daemon</p>
<h2>Synopsis</h2>
<p><code>glite-lb-logd</code> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>glite-lb-logd </code> accepts the L&amp;B events from their sources (via the producer L&amp;B API). It is responsible for fast acceptance of the events and their reliable storage in local files. Under normal conditions, the events are forwared to the <code>glite-lb-interlogd</code> immediately. The file storage allows the interlogger crash recovery. </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> FILE</i>, &#8211;cert <i>FILE</i></p>
<dd>Get certificate from <i>FILE</i>. This option overrides the $X509_USER_CERT environment variable. </p>
<dt><code>-C</code><i> DIR</i>, &#8211;CAdir <i>DIR</i></p>
<dd>Look for trusted CA&#8217;s certificates in <i>DIR</i>. This option overrides the $X509_CERT_DIR environment variable. </p>
<dt><code>-d</code>, &#8211;debug</p>
<dd>Don&#8217;t run as daemon. Additional diagnostics are not enabled, they can be configured through log4c instead. </p>
<dt><code>-p</code><i> NUM</i>, &#8211;port <i>NUM</i></p>
<dd>Listen on the port <i>NUM</i>. </p>
<dt><code>-f</code><i> PREFIX</i>, &#8211;file-prefix <i>PREFIX</i></p>
<dd><i>PREFIX </i> is a path prefix of the event files. </p>
<p> For each job (jobid) a specific file is created that stores all events associated with this job. The job filename is constructed by stripping the protocol+server prefix from the jobid and appending the rest to this <i>PREFIX. </i> </p>
<p> <i>PREFIX </i> defaults to /var/spool/glite/lb-locallogger/dglogd.log. </p>
<p> The value has to be same as used in the cooperating glite-lb-logd. </p>
<dt><code>-k</code><i> FILE</i>, &#8211;key <i>FILE</i></p>
<dd>Get private key from <i>FILE</i>. This option overrides the $X509_USER_KEY environment variable. </p>
<dt><code>-s</code><i> PATH</i>, &#8211;socket <i>PATH</i></p>
<dd>Send the messages to interlogger through the UNIX socket <i>PATH</i>. </p>
<p> The value has to be same as used in the cooperating glite-lb-interlogd. </p>
<dt><code>-i</code><i> FILE</i>, &#8211;pidfile <i>FILE</i></p>
<dd>Store pid into <i>FILE</i>. Defaults to /var/run/glite/glite-lb-logd.pid. </p>
<dt><code>-V</code>, &#8211;version</p>
<dd>Print version and exit. </p>
<dt><code>-h</code>, &#8211;help</p>
<dd>Print help and exit. </p>
<dt><code>&#8211;noAuth</code></p>
<dd>Don&#8217;t require valid X509 credentials to run the daemon. Used for debugging only. </p>
<dt><code>&#8211;noIPC</code></p>
<dd>Don&#8217;t send messages to interlogger. </p>
<dt><code>&#8211;noParse</code></p>
<dd>Don&#8217;t parse messages for correctness. Dangerous, for debugging only! Don&#8217;t use at all. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/tmp/interlogger.sock</i></p>
<dd>Default name of local socket. </p>
<dt><i>/var/spool/glite/lb-locallogger/dglogd.log*</i></p>
<dd>Default location of the event storage files.</p>
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
<h2>Signals</h2>
<dl>
<dt><code>USR1</code></p>
<dd>Increase verbosity of the program. </p>
<dt><code>USR2</code></p>
<dd>Decrease verbosity of the program. </p>
</dl>
<h2>Bugs</h2>
<p>Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a></code>(8), <a href="/docs/linux/man/8-glite-lb-interlogd/">glite-lb-interlogd</a>(8), <a href="/docs/linux/man/1-glite-lb-logevent/">glite-lb-logevent</a>(1), </p>
<h2>Author</h2>
<p>EU EGEE, JRA1.</p>
