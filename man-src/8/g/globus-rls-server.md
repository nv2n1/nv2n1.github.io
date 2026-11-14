---
title: "globus-rls-server(8)"
name: "globus-rls-server"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-rls-server/"
description: "globus-rls-server – Replica Location Server"
---

<p>globus-rls-server &#8211; Replica Location Server</p>
<h2>Synopsis</h2>
<p><code>globus-rls-server</code> [ <i>-B update_bf_int</i> ] [ <i>-b maxbackoff</i> ] [ <i>-C rlscertfile</i> ] [ <i>-c conffile</i> ] [ <i>-d</i> ] [ <i>-e rli_expire_int</i> ] [ <i>-F update_factor</i> ] [ <i>-f maxfreethreads</i> ] [ <i>-I true|false</i> [ <i>-i idletimeout</i> ] [ <i>-K rlskeyfile</i> ] [ <i>-L loglevel</i> ] [ <i>-l true|false</i> ] [ <i>-M maxconnections</i> ] [ <i>-m maxthreads</i> ] [ <i>-N</i> ] [ <i>-o update_buftime</i> ] [ <i>-p pidfiledir</i> ] [ <i>-r true|false</i> ] [ <i>-S rli_expire_stale</i> ] [ <i>-s startthreads</i> ] [ <i>-t timeout</i> ] [ <i>-U myurl</i> ] [ <i>-u update_ll_int</i> ] [ <i>-v</i> ]</p>
<h2>Description</h2>
<p>The RLS server <code>globus-rls-server</code> supports both a Location Replica Catalog (LRC) server, which manages Logical FileName (LFN) to Physical FileName (PFN) mappings in a database, and a Replica Location Index (RLI) server, which manages mappings of LFNs to LRC servers. <code>globus-rls-server</code> may be configured as either an LRC or RLI server, or both. Both LRCs and RLIs may be configured to send updates to other RLIs (using <a href="/docs/linux/man/8-globus-rls-admin/">globus-rls-admin</a>(8)). </p>
<p> Clients wishing to locate 1 or more physical filenames associated with a logical filename may first contact an RLI server, which will return a list of LRCs that may know about the LFN. The LRC servers are then contacted in turn to find the physical filenames. Note that RLI information may be out of date, so clients should be prepared to get a negative response when contacting an LRC (or no response at all if the LRC server is unavailable). </p>
<p> <code>globus-rls-server</code> uses <a href="/docs/linux/man/3-syslog/">syslog</a>(3) to log errors and other information (facility LOG_DAEMON) when it&#8217;s running in normal (daemon) mode. If the -d option (debug) is specified then log messages are written to stdout.</p>
<h2>LRC to RLI Updates</h2>
<p>Two methods exist for LRC or RLI servers to inform RLI servers of their LFNs. By default the list of LFNs are sent from the source to the RLI. This can be time consuming if the number of LFNs is large, but does give the RLI an exact list of the LFNs known to the LRC. This allows wildcard searching of the RLI. Alternatively Bloom filters may be sent, which are highly compressed summaries of the LFNs, however they do not allow wildcard searching, and they will generate more &quot;false positives&quot; when querying an RLI. Please see below for more on Bloom filters. The program <i><a href="/docs/linux/man/8-globus-rls-admin/">globus-rls-admin</a>(8)</i> can be used to manage the list of RLIs that an LRC or RLI server sends updates to, this includes partitioning LFNs amongst multiple RLI servers. </p>
<p> A softstate algorithm is used for updates, periodically the source server sends its state (LFN information) to the RLI servers it updates. The RLI servers add these LFNs to their index, or update a timestamp if the LFNs were already known. RLI servers expire information about LFN,LRC mappings if they haven&#8217;t been updated for a period longer than the softstate update interval. </p>
<p> Options that can be configured to control the softstate algorithm when a source server updates an RLI by sending LFNs are include:</p>
<dl>
<dt><code>rli_expire_int (seconds)</code></p>
<dd>How often an RLI server will check for stale entries in its database.</p>
<dt><code>rli_expire_stale (seconds)</code></p>
<dd>How old an entry must be in an RLI database before it&#8217;s considered stale. This value should be no smaller than <code>update_ll_int.</code> Note if the LRC server is responding this value is not used, instead the value of <code>update_ll_int</code> or <code>update_bf_int</code> is retrieved from the LRC server, multiplied by 1.2, and used as the value for <code>rli_expire_stale.</code></p>
<dt><code>update_bf_int seconds</code></p>
<dd>Interval between RLI updates when using Bloom filters.</p>
<dt><code>update_ll_int (seconds)</code></p>
<dd>Interval between RLI updates when using LFN lists for softstate updates.</dl>
<p> Updates to an LRC (new LFNs or deleted LFNs) normally don&#8217;t propagate to RLI servers until the next softstate update (controlled by <code>update_ll_int</code> and <code>update_bf_int).</code> However by enabling &quot;immediate update&quot; mode an LRC will send updates to an RLI within <code>update_buftime</code> seconds. Immedate updates are enabled by setting <code>update_immediate</code> to true. If updates are done with LFN lists then only the LFNs that have been added or deleted to the source server are sent, if Bloom filters are used then the entire Bloom filter is sent. </p>
<p> When immediate updates are enabled the interval between softstate updates is multiplied by <code>update_factor</code> as long as no updates have failed (source and RLI are considered to be in sync). This can greatly reduce the number of softstate updates a source needs to send to an RLI. Incremental updates are buffered by the source server until either 100 udpates have accumulated (when LFN lists are used), or <code>update_buftime</code> seconds have passed since the last update. </p>
<p> A Bloom filter is an array of bits. Each LFN is hashed multiple times and the corresponding bits in the Bloom filter are set. Querying an RLI to verify if an LFN exists is done by performing the same hashes, and checking if the bits in the filter are on. If not then the LFN is known not to exist, however if they&#8217;re all on then all that&#8217;s known is that the LFN probably exists. The size of the Bloom filter (as a multiple of the number of LFNs) and the number of hash functions, control the false positive rate. The default values of 10 and 3 give a false positive rate of approximately 1%. The advantage of Bloom filters is their efficiency. For example, if the LRC has 1,000,000 LFNs in its database, of average length 20 bytes, then 20,000,000 bytes must be sent to an RLI during a softstate update (assuming no partitioning). The RLI server must perform 1,000,000 updates to its database to create new LFN,LRC mappings, or update timestamps on existing entries. With Bloom filters only 1,250,000 bytes are sent (10 x 1,000,000 bits / 8), and there are no database operations on the RLI (Bloom filters are maintained entirely in memory). A comparison of the time to perform a 1,000,000 LFN update took 20 minutes sending all the LFNs, and less than 1 second using a Bloom filter. However as noted before wild card searches of an RLI are not supported with Bloom filters. </p>
<p> The options that control Bloom filter updates are:</p>
<dl>
<dt><code>rli_bloomfilter true|false</code></p>
<dd>RLI servers must have this set to accept Bloom filter updates.</p>
<dt><code>rli_bloomfilter_dir none|default|pathname</code></p>
<dd>Bloom filters saved in this directory and read at start time if not &quot;none&quot;. See CONFIGURATION for details.</p>
<dt><code>lrc_bloomfilter_numhash N</code></p>
<dd>Number of hash functions, an integer from 1 to 8. The default is 3.</p>
<dt><code>lrc_bloomfilter_ratio N</code></p>
<dd>Size of the Bloom filter as a multiple of the number of LFNs in the LRC database. Too small a value will generate too many false positives, too large wastes memory and network bandwidth.</dl>
<p> Note an LRC server can update some RLIs with Bloom filters, and others with LFNs. However an RLI server can only be updated using one method, and an RLI acting as a source for updates can only send the type of updates that it receives.</p>
<h2>Options</h2>
<dl>
<dt><code>-b maxbackoff</code></p>
<dd>Maximum time, in seconds, that <code>globus-rls-server</code> will attempt to reopen the socket it listens on after an I/O error.</p>
<dt><code>-C rlscertfile</code></p>
<dd>Name of X.509 certificate file that identifies the server, sets environment variable X509_USER_CERT.</p>
<dt><code>-c conffile</code></p>
<dd>Name of configuration file for server. The default is <i>$GLOBUS_LOCATION/etc/globus-rls-server.conf</i> if the environment variable GLOBUS_LOCATION is set, else <i>/etc/globus-rls-server.conf.</i></p>
<dt><code>-d</code></p>
<dd>Enable debugging. Server will not detach from controlling terminal and log messages will be written to stdout rather than syslog. For additional logging verbosity set loglevel (see -L option) to higher values.</p>
<dt><code>-e rli_expire_int</code></p>
<dd>Interval (seconds) at which an RLI server should expire stale entries.</p>
<dt><code>-F update_factor</code></p>
<dd>If <i>update_immediate</i> mode is on, and the source server is in sync with an RLI server (an LRC and RLI are synced if there have been no failed updates since the last full softstate update), then the interval between RLI updates for this server ( <i>update_ll_int</i> ) is multipled by <i>update_factor.</i></p>
<dt><code>-f maxfreethreads</code></p>
<dd>Maximum number of idle threads server will leave running. Excess threads are terminated.</p>
<dt><code>-I true|false</code></p>
<dd>Turns LRC to RLI immediate update mode on or off. Default is false.</p>
<dt><code>-i idletimeout</code></p>
<dd>Seconds after which idle client connections are timed out.</p>
<dt><code>-K rlskeyfile</code></p>
<dd>Name of X.509 key file. Sets environment variable X509_USER_KEY.</p>
<dt><code>-L loglevel</code></p>
<dd>Sets log level. By default this is 0, which means only errors will be logged. Higher values mean more verbose logging. Level 1 causes logging of major events (eg start of full softstate update), 2 includes medium level events (eg writing pending updates to an RLI), 3 enables all tracing. Level 4 includes all the SQL commands executed by the server.</p>
<dt><code>-l true|false</code></p>
<dd>Configure whether server is an LRC server. Default is false.</p>
<dt><code>-M maxconnections</code></p>
<dd>Maximum number of active connections. Should be small enough to prevent server from running out of open file descriptors. Default is 100.</p>
<dt><code>-m maxthreads</code></p>
<dd>Maximum number of threads server will start up to support simultaneous requests.</p>
<dt><code>-N</code></p>
<dd>Disable authentication checking. Intended for debugging. Clients should use the URL <code>RLSN://host</code> to disable authentication on the client side.</p>
<dt><code>-o update_buftime</code></p>
<dd>Softstate updates are buffered until either the buffer is full or this much time has elapsed since the last update. Default is 30 seconds.</p>
<dt><code>-p pidfiledir</code></p>
<dd>Directory where pid file should be written.</p>
<dt><code>-r</code></p>
<dd>Configure whether server is an RLI server. Default is false.</p>
<dt><code>-S rli_expire_stale</code></p>
<dd>Interval after which entries in the RLI database are considered stale (presumably because they were deleted in the LRC). Stale entries are not returned in queries.</p>
<dt><code>-s startthreads</code></p>
<dd>Number of threads to start up initially.</p>
<dt><code>-t timeout</code></p>
<dd>Timeout (in seconds) for calls to other RLS servers (eg for LRC calls to send an update to an RLI). A value of 0 disables timeouts. The default is 30 seconds.</p>
<dt><code>-U myurl</code></p>
<dd>URL for this server.</p>
<dt><code>-u update_ll_int</code></p>
<dd>Interval (in seconds) between lfn-list LRC to RLI updates.</p>
<dt><code>-v</code></p>
<dd>Show version and exit.</dl>
<h2>Signals</h2>
<p>The server will reread its configuration file if it receives a HUP signal. It will wait for all current requests to complete and shut down cleanly if sent a INT, QUIT or TERM signal.</p>
<h2>Configuration</h2>
<p>If the configuration file is not specified on the command line (see the -c option) then it&#8217;s looked for in <i>$GLOBUS_LOCATION/etc/globus-rls-server.conf,</i> or <i>/etc/globus-rls-server.conf</i> if GLOBUS_LOCATION is not set. </p>
<p> Most command line options may also be set in the configuration file, however command line options always override items found in the configuration file. The configuration file is a sequence of lines consisting of a keyword, whitespace, and a value. Comments begin with a # and end with a newline.</p>
<dl>
<dt><code>acl user: permission [permission]</code></p>
<dd><i>user</i> is a regular expression matching distinguished names (or local usernames if a gridmap file is used) of users allowed to make calls to the server. Permission is one or more of <i>lrc_read,</i> <i>lrc_update,</i> <i>rli_read,</i> <i>rli_update,</i> <i>admin,</i> <i>stats,</i> and <i>all.</i> There may be multiple <i>acl</i> entries, the first match found is used to determine a user&#8217;s privileges. The <i>admin</i> privilege is necessary to update an LRC&#8217;s list of RLIs to send updates to. The <i>stats</i> privilege allows a client to read performance statistics.</p>
<dd>A gridmap file may also be used to map DNs to local usernames, which in turn are matched against the regular expressions in the <i>acl</i> list to determine the user&#8217;s permissions.</p>
<dd><i>acl</i> entries may be a combination of DNs and local usernames. If a DN is not found in the gridmap file then it is used to search the <i>acl</i> list.</p>
<dt><code>authentication true|false</code></p>
<dd>Enable or disable GSI authentication. The default is true. If authentication is enabled clients should use the URL schema &quot;rls:&quot; to connect to the server, if disabled &quot;rlsn:&quot;.</p>
<dt><code>db_pwd password</code></p>
<dd>Password to use to connect to MYSQL server, default is <i>changethis.</i></p>
<dt><code>db_user databaseuser</code></p>
<dd>Username to use to connect to MYSQL server, default is <i>dbperson.</i></p>
<dt><code>idletimeout seconds</code></p>
<dd>Seconds after which idle connections closed, default is <i>900.</i></p>
<dt><code>loglevel N</code></p>
<dd>Sets loglevel to N (default is 0). Higher levels mean more verbosity.</p>
<dt><code>lrc_bloomfilter_numhash N</code></p>
<dd>Number of hash functions to use in Bloom filters. The default is 3. Possible values are 1 to 8. This value, in conjunction with <code>lrc_bloomfilter_ratio,</code> will determine the number of false positives that may be expected when querying an RLI that is updated via Bloom filters. The default values of 3 and 10 give a false positive rate of approximately 1%.</p>
<dt><code>lrc_bloomfilter_ratio N</code></p>
<dd>Sets ratio of bloom filter size (in bits) to number of LFNs in the LRC catalog. Only meaningful if Bloom filters are used to update an RLI. The default is 10.</p>
<dt><code>lrc_dbname</code></p>
<dd>Name of LRC database, default is <i>lrcdb.</i></p>
<dt><code>lrc_server true|false</code></p>
<dd>True if LRC server, default is <i>false.</i></p>
<dt><code>maxbackoff seconds</code></p>
<dd>Max seconds to wait before retrying listen in the event of an I/O error, default is <i>300.</i></p>
<dt><code>maxfreethreads N</code></p>
<dd>Maximum number of idle threads, excess threads are killed. Default is <i>5.</i></p>
<dt><code>maxconnections N</code></p>
<dd>Maximum number of simultaneous connections. Default is 100.</p>
<dt><code>maxthreads N</code></p>
<dd>Maximum number of threads running at one time, default is 30.</p>
<dt><code>myurl URL</code></p>
<dd>URL of server. Default is <i>rls://&lt;hostname&gt;:port</i></p>
<dt><code>odbcini filename</code></p>
<dd>Sets environment variable ODBCINI. If not specified, and ODBCINI is not already set, then defaults to <i>$GLOBUS_LOCATION/var/odbc.ini.</i></p>
<dt><code>pidfiledir directory</code></p>
<dd>Directory where pid file should be written, default is /var/run.</p>
<dt><code>port N</code></p>
<dd>Port server listens on, default is <i>39281.</i></p>
<dt><code>result_limit limit</code></p>
<dd>Sets the maximum number of results returned by a query. If a query request includes a limit greater than this value an error (GLOBUS_RLS_BADARG) is returned. If the query request has no limit specified then at most <code>result_limit</code> records are returned by a query. A value of zero means no limit, this is the default.</p>
<dt><code>rli_bloomfilter true|false</code></p>
<dd>If true then only Bloom filter updates are accepted from source servers, otherwise full LFN lists are accepted. Note if Bloom filters are enabled then the RLI does not support wildcarded queries.</p>
<dt><code>rli_bloomfilter_dir none|default|pathname</code></p>
<dd>If an RLI is configured to accept bloom filters (rli_bloomfilter true) then bloom filters may be saved to this directory after updates. This directory is scanned when an RLI server starts up and is used to initialize Bloom filters for each LRC that updated the RLI. This option is useful when it is desired that the RLI recover its data immediately after a restart rather than wait for LRCs to send another update. If the LRCs are updating frequently this option is unnecessary, and may be wasteful in that each Bloom filter is written to disk after each update.</p>
<dd>If <i>rli_bloomfilter_dir</i> is set to the string &quot;none&quot; then Bloom filters are not saved to disk, this is the default. If &quot;default&quot; then the default directory is used, which is $GLOBUS_LOCATION/var/rls-bloomfilters if GLOBUS_LOCATION is set, else /tmp/rls-bloomfilters. Any other string is used as the directory name unchanged. The Bloom filter files in this directory have the name of the URL of the LRC that sent the Bloom filter, with slashes (/) changed to percent signs (%), and &quot;.bf&quot; appended.</p>
<dt><code>rli_dbname database</code></p>
<dd>Name of RLI database, default is <i>rlidb.</i></p>
<dt><code>rli_expire_int seconds</code></p>
<dd>Interval between RLI expirations of stale entries. Default is <i>28800</i> seconds.</p>
<dt><code>rli_expire_stale seconds</code></p>
<dd>Interval after which entries in the RLI database are considered stale (presumably because they were deleted in the LRC). Default is <i>86400</i> seconds. Stale RLI entries are not returned in queries.</p>
<dt><code>rli_server true|false</code></p>
<dd>True if RLI server, default is <i>false.</i></p>
<dt><code>rlscertfile filename</code></p>
<dd>Name of X.509 certificate file identifying server, set by setting environment variable X509_USER_CERT.</p>
<dt><code>rlskeyfile</code></p>
<dd>Name of X.509 key file for server, set by setting environment variable X509_USER_KEY.</p>
<dt><code>startthreads N</code></p>
<dd>Number of threads to start initially, default is <i>3.</i></p>
<dt><code>timeout seconds</code></p>
<dd>Timeout (in seconds) for calls to other RLS servers (eg for LRC calls to send an update to an RLI).</p>
<dt><code>update_bf_int seconds</code></p>
<dd>Interval between RLI updates when the RLI is updated by Bloom filters. The default is 900 seconds.</p>
<dt><code>update_buftime N</code></p>
<dd>RLI updates are buffered until either the buffer is full or this much time has elapsed since the last update. Default is 30 seconds.</p>
<dt><code>update_factor N</code></p>
<dd>If <i>update_immediate</i> mode is on, and the source server is in sync with an RLI server (a source and RLI are synced if there have been no failed updates since the last full softstate update), then the interval between RLI updates for this server ( <i>update_ll_int</i> ) is multipled by <i>update_factor.</i></p>
<dt><code>update_immediate true|false</code></p>
<dd>Turn LRC to RLI immediate mode updates on or off. Default is false.</p>
<dt><code>update_ll_int seconds</code></p>
<dd>Seconds between lfn-list softstate updates, default is <i>86400</i> seconds.</p>
<dt><code>update_retry seconds</code></p>
<dd>Seconds to wait before a source server will retry to connect to an RLI server that it needs to update. Default is 300.</dl>
<h2>Files</h2>
<dl>
<dt><code>$GLOBUS_LOCATION/etc/globus-rls-server.conf</code></p>
<dd>Default configuration file. </p>
</dl>
