---
title: "glite-lb-bkserverd(8)"
name: "glite-lb-bkserverd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glite-lb-bkserverd/"
description: "glite-lb-bkserverd – bookkeeping server daemon"
---

<p>glite-lb-bkserverd &#8211; bookkeeping server daemon</p>
<h2>Synopsis</h2>
<p><code>glite-lb-bkserverd</code> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>glite-lb-bkserverd </code> accepts L&amp;B events from interlogger, manages the data storage, and serves user queries (L&amp;B consumer clients). Currently, the data are stored in MySQL database. The main process spawns several <i>slave</i> processes. Then it listens on <i>port</i> (default value is 9000) for consumer queries and <i>port+1</i> for interlogger daemon requests to store events to database. Requests are redirected to the slaves (and picked up by the first free slave process). All the connection handling and data processing (including SSL handshake) is performed by the slaves. The slaves voluntarily die and are resurrected periodically to workaround potential resource leakage. </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code><i> HOST:PORT</i>, &#8211;address <i>HOST:PORT</i></p>
<dd>Make the server pretend (wrt. data handling) it listens on <i>HOST:PORT </i> instead of the real listening address. This is used for debugging and various administrative purposes (e.g. computing usage statistics on data dumped from another server). </p>
<dt><code>-c</code><i> FILE</i>, &#8211;cert <i>FILE</i></p>
<dd>Get certificate from <i>FILE</i>. This option overrides the $X509_USER_CERT environment variable. </p>
<dt><code>-b</code><i> SWITCH</i>, &#8211;transactions <i>SWITCH</i></p>
<dd>Set transaction on/off. <i>SWITCH</i> is true where its value is not 0. </p>
<dt><code>-C</code><i> DIR</i>, &#8211;CAdir <i>DIR</i></p>
<dd>Trusted CA&#8217;s certificates directory. <i>DIR</i>. This option overrides the $X509_CERT_DIR environment variable. </p>
<dt><code>-V</code><i> DIR</i>, &#8211;VOMSdir <i>DIR</i></p>
<dd>Trusted VOMS server&#8217;s certificates directory. <i>DIR</i>. This option overrides the $X509_VOMS_DIR environment variable. </p>
<dt><code>-d</code>, &#8211;debug</p>
<dd>Don&#8217;t run as daemon. Additional diagnostics are not enabled, they can be configured through log4c instead. </p>
<dt><code>-r</code>, &#8211;rgmaexport</p>
<dd>Write state info to RGMA interface. </p>
<dt><code>-i</code><i> FILE</i>, &#8211;pidfile <i>FILE</i></p>
<dd>Store master pid into <i>FILE</i> instead of the default pidfile location. Unless unavoidable it is not recommended to change the pidfile location as it is also used for locking to prevent starting up multiple server instances and to generate the semaphore set unique key (see option -l). </p>
<dt><code>-k</code><i> FILE</i>, &#8211;key <i>FILE</i></p>
<dd>Get private key from <i>FILE</i>. This option overrides the $X509_USER_KEY environment variable. </p>
<dt><code>-l</code><i> NUM</i>, &#8211;semaphores <i>NUM</i></p>
<dd>Use <i>NUM</i> semaphores (job locks). </p>
<p> To prevent race conditions on simultaneous event storage and job-state updates <code>glite-lb-bkserverd</code> uses a set of semaphores to lock jobs. Jobids are hashed to the semaphores and only one of the set of jobs that map to a particular semaphore may be updated at any given time. Therefore <i>NUM</i> is a limit on potential processing parallelism. </p>
<p> <i>NUM</i> defaults to the number of slaves (see -s). </p>
<dt><code>-L</code><i> NUM:NUM:NUM</i>, &#8211;limits <i>NUM:NUM:NUM</i></p>
<dd>Limit the maximum number of returned jobs/events that match user query to <i>NUM:NUM:NUM</i> in format events_limit:jobs_limit:size_limit.</p>
<dt><code>-N</code><i> NUM</i>, &#8211;notif-dur <i>NUM</i></p>
<dd>Maximal duration of notification registrations in hours <i>NUM</i>. </p>
<dt><code>-S</code><i> PREFIX</i>, &#8211;purge-prefix <i>PREFIX</i></p>
<dd>Purge files full-path prefix <i>PREFIX</i>. </p>
<dt><code>-D</code><i> PREFIX</i>, &#8211;dump-prefix <i>PREFIX</i></p>
<dd>Dump files full-path prefix <i>PREFIX</i>. </p>
<dt><code>-J</code><i> DIR</i>, &#8211;jpreg-dir <i>DIR</i></p>
<dd>JP registration temporary files prefix (implies &#8216;-j&#8217;). <i>DIR</i>. </p>
<dt><code>-j </code>, &#8211;enable-jpreg-export</p>
<dd>Enable JP registration export (disabled by default). </p>
<dt><code>-m</code><i> STRING</i>, &#8211;mysql <i>STRING</i></p>
<dd><i>STRING</i> is a database connect string in the form<br />
&nbsp;<wbr> USER_NAME/PASSWORD [at] DB_HOSTNAME:DB_NAME </p>
<p> It defaults to lbserver/@localhost:lbserver20. </p>
<dt><code>-n, &#8211;noauth</code></p>
<dd>Turn off any authorization. </p>
<dt><code>-p</code><i> NUM</i>, &#8211;port <i>NUM</i></p>
<dd>Listen on the port <i>NUM</i>. </p>
<dt><code>-w</code><i> NUM</i>, &#8211;wsport <i>NUM</i></p>
<dd>Set port to serve the web services requests to <i>NUM</i>. </p>
<dt><code>-r</code>, &#8211;rgmaexport</p>
<dd>Write state info into the RGMA interface. Experimental. </p>
<dt><code>-s</code><i> NUM</i>, &#8211;slaves <i>NUM</i></p>
<dd>Fork <i>NUM</i> slaves. </p>
<dt><code>&#8211;super-user</code><i> USER</i>, &#8211;super-user-file <i>FILE</i></p>
<dd>Bypass query authorization (i.e. return results anyway) when USER (or users listed in FILE) connect. </p>
<dt><code>&#8211;no-index</code><i> NUM</i></p>
<dd>Disable checking the indices for superusers (NUM=1) or entirely (NUM=2). </p>
<dt><code>&#8211;strict-locking</code></p>
<dd><i>(not recommended).</i> Use a more strict locking strategy &#8212; lock jobs sooner, when events are stored, not just for status update. This prevents a non-probable but still possible race condition with parallel purge but may slow down processing on heavy loaded servers. Anyway, the only consequence of the race condition is a little garbage left in the database which is cleaned form time to time anyway. </p>
<dt><code>&#8211;notif-il-sock</code><i> SOCK</i></p>
<dd>Socket <i>SOCK</i> to send notifications. </p>
<dt><code>&#8211;notif-il-sock</code><i> PREFIX</i></p>
<dd>File <i>PREFIX</i> for notifications. </p>
<dt><code>&#8211;count-statistics</code><i> NUM</i></p>
<dd>Count certain statistics on jobs for superusers (NUM=1) or for all (NUM=2). </p>
<dt><code>-t</code><i> NUM</i>, &#8211;request-timeout <i>NUM</i></p>
<dd>Request timeout <i>NUM</i> for one client. </p>
<dt><code>&#8211;silent</code></p>
<dd>Do not print diagnostic, even if -d is on. </p>
<dt><code>-g</code><i></i><code>&#8211;greyjobs</code></p>
<dd>Allow delayed registration (grey jobs), implies &#8211;strict-locking. </p>
<dt><code>-A</code>,<i>&#8211;enable-lcas</i></p>
<dd>Activate LCAS-based authorization. </p>
<dt><code>-I</code>,<i>&#8211;rss-time</i><code> NUM</code></p>
<dd>Set the maximal age (in seconds) of states published via RSS. </p>
<dt><code>-P</code>,<i>&#8211;proxyonly</i></p>
<dd>Run only proxy service. </p>
<dt><code>-B</code>,<i>&#8211;withproxy</i></p>
<dd>Run both server and proxy service. </p>
<dt><code>-o</code>,<i>&#8211;sock</i></p>
<dd>Path-name to the local socket for communication with LB proxy. </p>
<dt><code>-q</code>,<i>&#8211;con-queue</i></p>
<dd>Size of the connection queue (accept). </p>
<dt><code>-W</code>,<i>&#8211;proxy-il-sock</i></p>
<dd>Socket to send events to. </p>
<dt><code>-Z</code>,<i>&#8211;proxy-il-fprefix</i></p>
<dd>File prefix for events. </p>
<dt><code>-G</code>,<i>&#8211;proxy-purge</i></p>
<dd>Enable automatic purging of the jobs in terminal state for proxy service (disabled by default, purging cron job installed by YAIM). </p>
<dt><code>-E</code>,<i>&#8211;exclusive-zombies-off</i></p>
<dd>Disable checking of purged jobs when registering jobs with the EDG_WLL_LOGLFLAG_EXCL flag set. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/run/edg-bkserverd.pid</i></p>
<dd>if running as root (not recommended). </p>
<dt><i>$HOME/edg-bkserverd.pid</i></p>
<dd>otherwise. </p>
<dt>File to store pid and to generate semaphores key.</p>
<dd>
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
<dt><code>EDG_WL_RGMA_FILE</code></p>
<dd>If $EDG_WL_RGMA_FILE is set, it is used as name of file for sharing data with RGMA services. </p>
<dt><code>EDG_WL_RGMA_SOCK</code></p>
<dd>If $EDG_WL_RGMA_SOCK is set, it is used as name of socket for communication with RGMA. </p>
</dl>
<h2>Bugs</h2>
<p>In a case of a sudden crash, alive slave processes may survive or some resources (IPC locks, open ports) may stay allocated. Please, deal with such problems via standard commands <code>kill</code> and ipcrm. Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-glite-lb-bkindex/">glite-lb-bkindex</a></code>(8), <a href="/docs/linux/man/1-glite-lb-purge/">glite-lb-purge</a>(1), <a href="/docs/linux/man/8-glite-lb-interlogd/">glite-lb-interlogd</a>(8), <a href="/docs/linux/man/8-glite-lb-logd/">glite-lb-logd</a>(8), <a href="/docs/linux/man/1-glite-lb-logevent/">glite-lb-logevent</a>(1), </p>
<h2>Author</h2>
<p>EU EGEE, JRA1.</p>
