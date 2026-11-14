---
title: "pmmgr(1)"
name: "pmmgr"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmmgr/"
description: "pmmgr – pcp daemon manager"
---

<h2>NAME</h2>
<p> <code>pmmgr</code> &#8211; pcp daemon manager</p>
<h2>SYNOPSIS</h2>
<p> <code>pmmgr</code> [<code>-v</code>] [<code>-c</code> <i>config-directory</i>] [<code>-p</code> <i>polling-interval</i>] [<code>-l</code> <i>log-file</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pmmgr</code> manages a collection of PCP daemons for a set of discovered local and remote hosts running the Performance Metrics Collection Daemon (PMCD), according to zero or more configuration directories. It keeps a matching set of <code>pmlogger</code>, <code>pmie</code>, and other clients/daemons running, and their archives/logs merged/rotated. It supplants the older <code>pmlogger_*</code> and <code>pmie_*</code> check/daily management shell scripts. </p>
<p> pmmgr is largely self-configuring and perseveres despite most run-time errors. pmmgr runs in the foreground until interrupted. When signaled, it will stop its running daemons before exiting. </p>
<p> A description of the command line options specific to <code>pmmgr</code> follows:</p>
<dl>
<dt><code>-c</code></p>
<dd> <i>directory</i> adds a given configuration directory to pmmgr. pmmgr can supervise multiple different configurations at the same time, so this option may be repeated. Errors in the configuration may be noted to standard error, but pmmgr will fill in missing information with built-in defaults. The default directory is <i>$PCP_SYSCONF_DIR/pmmgr</i></p>
<dt><code>-p</code></p>
<dd> <i>polling-interval</i> sets the host-discovery polling interval to the given number of seconds. The default is 60. Daemons for a particular target host will be restarted no more frequently than this interval. There may be a short-lived thread inside pmmgr for startup &amp; shutdown of each daemon for each target host.</p>
<dt><code>-l</code></p>
<dd> <i>log-file</i> redirects standard output &amp; error to the given log file, which is created anew</p>
<dt><code>-v</code></p>
<dd> adds more verbose tracing to standard output. </p>
</dl>
<h2>CONFIGURATION</h2>
<p> A <code>pmmgr</code> configuration identifies which hosts should be monitored, which daemons should be maintained for them, and what options those daemons should be run with. pmmgr uses a small number of files in a configuration directory, instead of lines in a text file. The individual files carry zero or more lines of 100% pure configuration text, and no comments. (If desired, a configuration may be commented upon with any other file, such as a free-form README.) </p>
<h3>TARGET SELECTION</h3>
<p> This set of configuration files identifies where pmmgr should search for pmcd instances, how to uniquely identify them, and where state such as log files should be kept for each. Ideally, a persistent &amp; unique host-id string is computed for each potential target pmcd from specified metric values. This host-id is also used as a subdirectory name for locating daemon data. </p>
<dl>
<dt>hostid-metrics</p>
<dd> This file contains one or more lines of metric specifications in the format accepted by <i>pmParseMetricSpec</i>. Metrics without instance specifiers mean all instances of that metric. These are used to generate the <i>unique</i> host-id string for each pmcd server that pmmgr discovers. Upon discovery, all the metrics/instances named are queried, string values fetched, and normalized/concatenated into a single hyphenated printable string. The default is the single metric <code>pmcd.hostname</code>, which is sufficient if all the hosts discovered have unique <a href="/docs/linux/man/2-hostname/">hostname</a>(2). If they don&#8217;t, you should add other pcp metric specifications to set them apart at your site. The more you add, the longer the host-id string, but the more likely that accidental duplication is prevented. </p>
<p> However, it may be desirable for a host-id to also be <i>persistent</i>, so that if the target host goes offline and later returns, the new host-id matches the previous one, because then old and new histories can be joined. This argues against using metrics whose values vary from boot to boot. </p>
<p> Some candidate metrics to consider: <i>network.interface.hw_addr</i>, <i>network.interface.inet_addr[eth0]</i>, <i>network.interface.ipv6_addr</i>, <i>kernel.uname.nodename</i> </p>
<dt>log-directory</p>
<dd> This file contains the path of a directory beneath which the per-host-id subdirectories are to be created by pmmgr. If it is not a full path, it is implicitly relative to the configuration directory itself. The default is <code>$PCP_LOG_DIR/pmmgr/</code>. </p>
<dt>target-host</p>
<dd> This file contains one or more lines containing pmcd host specifications, as described on the <i><a href="/docs/linux/man/1-pcpintro/">PCPintro</a></i>(1) man page. Each poll interval, pmmgr will attempt to make a brief <i>pmNewContext</i> connection to the host to check liveness. It is not a problem if more than one specification for the same host is listed, because the host-id processing eliminates duplicates, and chooses an arbitrary specification among them. The default is to target pmcd at <code>local:</code>. </p>
<dt>target-discovery</p>
<dd> This file contains one or more lines containing specifications for the <i>pmDiscoverServices</i> PMAPI call, each of which may map onto a fluctuating set of local or remote pmcd servers. Each poll interval, pmmgr will attempt to rerun discovery with all of the given specifications. Again, it is not a problem if more than one specification matches the same actual pmcd: one confirmed access path is arbitrarily selected. The default is to do <code>no discovery</code>. Consider including <i>avahi,timeout=5</i> to rely in pmcd self-announcements on the local network (searching for up to five seconds each time). Consider including <i>probe=192.168.1.0/24</i> to quickly scan the given IP address range. </p>
<dt>subtarget-containers</p>
<dd> If this file exists, pmmgr will scan each host that is found for running containers. For each running container, it will create independent subtargets for running requested daemons. The host-id string for these subtargets is the host&#8217;s host-id string, followed by a double-hyphen, then the full unique container instance-name string. </p>
<dt>target-threads</p>
<dd> This file contains a limit on the number of concurrent threads that analyze potential target pmcds for their hostids and/or containers. The default is <code>a few dozen threads per CPU core</code>, if known. Set this to zero if remote pmcds should be analyzed sequentially. A small number of threads is not a good idea if any potential target pmcds are unreachable, since $PMCD_CONNECT_TIMEOUT may be several seconds long each. </p>
<dt>log-subdirectory-gc</p>
<dd> This file may contain a time interval specification as per the <i>PCPintro</i> man page. All subdirectories of the log-directory are presumed to contain data for pmmgr-monitored servers. Those that have not been touched (in the <code>stat/mtime</code> sense) in at least that long, and not associated with a currently monitored target, are deleted entirely. This value should be longer than the longest interval that pmmgr normally recreates archives (such as due to pmmgr restarts, and <code>pmlogmerge</code> intervals). The default value is <code>90days</code>. </p>
</dl>
<h3>PMLOGGER CONFIGURATION</h3>
<p> This group of configuration options controls a <code>pmlogger</code> daemon for each host. This may include generating its configuration, and managing its archives. </p>
<dl>
<dt>pmlogger</p>
<dd> If and only if this file exists, pmmgr will maintain a <code>pmlogger</code> daemon for each targeted host. This file contains one line of additional space-separated options for the pmie daemon. (pmmgr already adds -h, -f, -r, -l, and perhaps -c.) The default is to maintain <code>no pmlogger</code> (and no other configuration in this section is processed). </p>
<dt>pmlogconf</p>
<dd> If and only if this file exists, pmmgr will run <code>pmlogconf</code> to generate a configuration file for each target pmcd. The file contains one line of space-separated additional options for the pmlogconf program. pmlogconf&#8217;s generated output file will be stored under the log-directory/hostid subdirectory. (pmmgr already adds -c, -r, and -h.) The default is <code>no pmlogconf</code>, so instead, the pmlogger file above should probably contain a -c option, to specify a fixed pmlogger configuration. </p>
</dl>
<h3>ARCHIVE LOG MANAGEMENT</h3>
<p> Default pmlogger configurations can collect tens of megabytes of data per day (possibly split into multiple archives), per target host. If your disk space is less than infinite, or archive-splitting unwieldy, this should be managed. In the default, unmanaged case, the system administrator is responsible for managing the individual <i>archive-*</i> files from the per-host logging subdirectories. pmmgr offers several other options, each representing different performance / usability tradeoffs. </p>
<h3>ARCHIVE LOG MANAGEMENT &#8211; pmlogmerge</h3>
<p> This style of archive log management regularly creates a single merged archive from prior archives for each target host, in effect lopping off old data and appending the new. A single merged archive can be relatively large (defaults to approximately 100-400 MB per host), and puts a corresponding I/O load on storage, but is most convenient for a detailed long-timeframe analysis. Once pmlogger is restarted, it always creates a new archive, so in the steady state, there will be one merged archive of recent history, and one current archive being written-to by pmlogger. </p>
<dl>
<dt>pmlogmerge</p>
<dd> If this file exists, pmmgr will run <code>pmlogextract</code> to periodically merge together preexisting log archives for each target pmcd into a single large one. Then, the preexisting log archives are deleted (including any prior merged ones). This configuration file may contain a time interval specification as per the <i>PCPintro</i> man page, representing the period after which pmlogger should be temporarily stopped, and archives merged. It represents the maximum amount of time that the merged archive <i>lags</i> the present time. The default is <code>24hours</code>. </p>
<dt>pmlogmerge-granular</p>
<dd> If this file exists, pmmgr will merge only a subset of preexisting log archives into the new one, instead of all of them, so as to approximate a granular, aligned set of merged archives. The subset chosen corresponds to the previous time interval specified by the <i>pmlogmerge</i> control file. The default is <code>no granularity</code>. </p>
<dt>pmlogmerge-rewrite</p>
<dd> If this file exists, pmmgr will run <code>pmlogrewrite -i</code> (plus any other options listed in this file) on each input archive before merging it. This will naturally require more disk I/O. The default is <code>no rewriting</code>. </p>
<dt>pmlogmerge-retain</p>
<dd> pmmgr reduces/deletes any original-resolution archives after a time period specified by this file, as measured by the file mtime. The period will also be passed to pmlogextract as a negative parameter to -S. The default is <code>14days</code>. To store archives indefinitely, set this to a large quantity like &quot;99999weeks&quot;. </p>
<dt>pmlogreduce</p>
<dd> If this file exists, then prior to removing archives that expire past the <i>pmlogmerge-retain</i> period, they are processed with <i>pmlogreduce</i> to create reduced archives (named <code>reduced-*</code>). If the file contains space-separated options, they are passed onto pmlogreduce. (By default, pmlogreduce downsamples to a 600-second interval.) </p>
<dt>pmlogreduce-retain</p>
<dd> If this file exists, then reduced archives (identified by the <code>reduced-*</code> pattern) are deleted after a time period specified by this file, as measured from the file mtime. Since this time is likely that of the pmlogreduce run, the total retention time will be approximately the pmlogmerge-retain time <code>plus</code> the pmlogreduce-retain time. The default is <code>90days</code>. To store reduced archives indefinitely, set this to a large quantity like &quot;99999weeks&quot;. </p>
</dl>
<h3>PMIE CONFIGURATION</h3>
<p> This group of configuration options controls a <code>pmie</code> daemon for each host. This may include generating a custom configuration. </p>
<dl>
<dt>pmie</p>
<dd> If and only if this file exists, pmmgr will maintain a <code>pmie</code> daemon for each targeted pmcd. This file contains one line of additional space-separated options for the pmie daemon. (pmmgr already adds -h, -f, -l, and perhaps -c.) The default is to maintain <code>no pmie</code> (and no other configuration in this section is processed). </p>
<dt>pmieconf</p>
<dd> If and only if this file exists, pmmgr will run <code>pmieconf</code> to generate a configuration file for each target pmcd. The file contains one line of space-separated additional options for the pmieconf program. pmieconf&#8217;s generated output file will be stored under the log-directory/hostid subdirectory. (pmmgr already adds -F, -c, and -f.) The default is <code>no pmieconf</code>, so instead, the pmie file above should probably contain a -c option, to specify a fixed pmie configuration. </p>
</dl>
<h3>MONITOR DAEMON MANAGEMENT</h3>
<p> In addition to pmlogger and pmie, pmmgr may be used to invoke arbitrary pcp client programs for each target pmcd. This can enable automated invocation of reporting or relaying tools, such as <code>pmrep</code> or <code>pcp2graphite</code>, without needing a specialized system service. </p>
<dl>
<dt>monitor</p>
<dd> If this file exists, then for each line in this file, a new background process will be invoked. (It is restarted if it exits.) The line specifies the beginning of the command line (including the program name); pmmgr appends a -h HOSTSPEC, and arranges to collect the standard output and standard error into separate <code>monitor-NN.out</code> and <code>monitor-NN.err</code> files under the log directory. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_SYSCONFIG_DIR/pmmgr/</code></p>
<dd> default configuration directory</p>
<dt><code>$PCP_LOG_DIR/pmmgr/</code></p>
<dd> default logging directory </p>
</dl>
<h2>BUGS</h2>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parametrize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmlogconf/">pmlogconf</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmieconf/">pmieconf</a></code>(1), <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/1-pmlogreduce/">pmlogreduce</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
