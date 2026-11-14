---
title: "postfix(1)"
name: "postfix"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postfix/"
description: "postfix – Postfix control program"
---

<h2 class="name">NAME</h2>
<p> postfix &#8211; Postfix control program </p>
<h2>SYNOPSIS</h2>
<p> <code>postfix</code> [<code>-Dv</code>] [<code>-c </code><i>config_dir</i>] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> This command is reserved for the superuser. To submit mail, use the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command. </p>
<p> The <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) command controls the operation of the Postfix mail system: start or stop the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) daemon, do a health check, and other maintenance. </p>
<p> By default, the <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) command sets up a standardized environment and runs the <code>postfix-script</code> shell script to do the actual work. </p>
<p> However, when support for multiple Postfix instances is configured, <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) executes the command specified with the <code>multi_instance_wrapper</code> configuration parameter. This command will execute the <i>command</i> for each applicable Postfix instance. </p>
<p> The following commands are implemented:</p>
<dl>
<dt><code>check</code></p>
<dd> Warn about bad directory/file ownership or permissions, and create missing directories.</p>
<dt><code>start</code></p>
<dd> Start the Postfix mail system. This also runs the configuration check described above.</p>
<dt><code>start-fg</code></p>
<dd> Like <code>start</code>, but keep the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) daemon running in the foreground, and enable <code><a href="/docs/linux/man/8-master/">master</a></code>(8) &quot;init&quot; mode when running as PID 1. This command requires that multi-instance support is disabled (i.e. the multi_instance_directories parameter value must be empty). When running Postfix inside a container, mount the container host&#8217;s /dev/log socket inside the container (example: &quot;docker run -v /dev/log:/dev/log &#8230;&quot;) and specify a distinct Postfix &quot;syslog_name&quot; prefix that identifies logging from the Postfix instance.</p>
<dt><code>stop</code></p>
<dd> Stop the Postfix mail system in an orderly fashion. If possible, running processes are allowed to terminate at their earliest convenience. </p>
<p> Note: in order to refresh the Postfix mail system after a configuration change, do not use the <code>start</code> and <code>stop</code> commands in succession. Use the <code>reload</code> command instead.</p>
<dt><code>abort</code></p>
<dd> Stop the Postfix mail system abruptly. Running processes are signaled to stop immediately.</p>
<dt><code>flush</code></p>
<dd> Force delivery: attempt to deliver every message in the deferred mail queue. Normally, attempts to deliver delayed mail happen at regular intervals, the interval doubling after each failed attempt. </p>
<p> Warning: flushing undeliverable mail frequently will result in poor delivery performance of all other mail.</p>
<dt><code>reload</code></p>
<dd> Re-read configuration files. Running processes terminate at their earliest convenience.</p>
<dt><code>status</code></p>
<dd> Indicate if the Postfix mail system is currently running.</p>
<dt><code>set-permissions</code> [<i>name</i>=<i>value &#8230;</i>]</p>
<dd> Set the ownership and permissions of Postfix related files and directories, as specified in the <code>postfix-files</code> file. </p>
<p> Specify <i>name</i>=<i>value</i> to override and update specific main.cf configuration parameters. Use this, for example, to change the <code>mail_owner</code> or <code>setgid_group</code> setting for an already installed Postfix system. </p>
<p> This feature is available in Postfix 2.1 and later. With Postfix 2.0 and earlier, use &quot;<code>$config_directory/post-install set-permissions</code>&quot;.</p>
<dt><code>logrotate</code></p>
<dd> Rotate the logfile specified with $maillog_file, by appending a time-stamp suffix that is formatted according to $maillog_file_rotate_suffix, and by compressing the file with the command specified with $maillog_file_compressor. This will not rotate /dev/* files. </p>
<p> This feature is available in Postfix 3.4 and later.</p>
<dt><code>tls</code> <i>subcommand</i></p>
<dd> Enable opportunistic TLS in the Postfix SMTP client or server, and manage Postfix SMTP server TLS private keys and certificates. See <a href="/docs/linux/man/1-postfix-tls/">postfix-tls</a>(1) for documentation. </p>
<p> This feature is available in Postfix 3.1 and later.</p>
<dt><code>upgrade-configuration</code> [<i>name</i>=<i>value &#8230;</i>]</p>
<dd> Update the <code>main.cf</code> and <code>master.cf</code> files with information that Postfix needs in order to run: add or update services, and add or update configuration parameter settings. </p>
<p> Specify <i>name</i>=<i>value</i> to override and update specific main.cf configuration parameters. </p>
<p> This feature is available in Postfix 2.1 and later. With Postfix 2.0 and earlier, use &quot;<code>$config_directory/post-install upgrade-configuration</code>&quot;.</dl>
<p> The following options are implemented:</p>
<dl>
<dt><code>-c </code><i>config_dir</i></p>
<dd> Read the <code>main.cf</code> and <code>master.cf</code> configuration files in the named directory instead of the default configuration directory. Use this to distinguish between multiple Postfix instances on the same host. </p>
<p> With Postfix 2.6 and later, this option forces the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command to operate on the specified Postfix instance only. This behavior is inherited by <a href="/docs/linux/man/1-postfix/">postfix</a>(1) commands that run as a descendant of the current process.</p>
<dt><code>-D</code> (with <code>postfix start</code> only)</p>
<dd> Run each Postfix daemon under control of a debugger as specified via the <code>debugger_command</code> configuration parameter.</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</dl>
<h2>ENVIRONMENT</h2>
<p> The <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) command exports the following environment variables before executing the <code>postfix-script</code> file:</p>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd> This is set when the -c command-line option is present. </p>
<p> With Postfix 2.6 and later, this environment variable forces the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command to operate on the specified Postfix instance only. This behavior is inherited by <a href="/docs/linux/man/1-postfix/">postfix</a>(1) commands that run as a descendant of the current process.</p>
<dt><code>MAIL_VERBOSE</code></p>
<dd> This is set when the -v command-line option is present.</p>
<dt><code>MAIL_DEBUG</code></p>
<dd> This is set when the -D command-line option is present.</dl>
<p> When the internal logging service is enabled (by setting a non-empty maillog_file parameter value) the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command exports settings that are used by child processes before they have processed main.cf or command-line settings.</p>
<dl>
<dt><code>POSTLOG_SERVICE</p>
<dd> The name of the public postlog service endpoint.</p>
<dt>POSTLOG_HOSTNAME</p>
<dd> The hostname to prepend to internal logging.</dl>
<p> </code></p>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> configuration parameters are exported as environment variables with the same names:</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>command_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of all postfix administrative commands.</p>
<dt><code>daemon_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The directory with Postfix support programs and daemon programs.</p>
<dt><code>html_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of Postfix HTML files that describe how to build, configure or operate a specific Postfix subsystem or feature.</p>
<dt><code>mail_owner (postfix)</code></p>
<dd> The UNIX system account that owns the Postfix queue and most Postfix daemon processes.</p>
<dt><code>mailq_path (see &#8216;postconf -d&#8217; output)</code></p>
<dd> Sendmail compatibility feature that specifies where the Postfix <code><a href="/docs/linux/man/1-mailq/">mailq</a></code>(1) command is installed.</p>
<dt><code>manpage_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> Where the Postfix manual pages are installed.</p>
<dt><code>newaliases_path (see &#8216;postconf -d&#8217; output)</code></p>
<dd> Sendmail compatibility feature that specifies the location of the <code><a href="/docs/linux/man/1-newaliases/">newaliases</a></code>(1) command.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of the Postfix top-level queue directory.</p>
<dt><code>readme_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of Postfix README files that describe how to build, configure or operate a specific Postfix subsystem or feature.</p>
<dt><code>sendmail_path (see &#8216;postconf -d&#8217; output)</code></p>
<dd> A Sendmail compatibility feature that specifies the location of the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command.</p>
<dt><code>setgid_group (postdrop)</code></p>
<dd> The group ownership of set-gid Postfix commands and of group-writable Postfix directories.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>data_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The directory with Postfix-writable data files (for example: caches, pseudo-random numbers).</dl>
<p> Available in Postfix version 3.0 and later:</p>
<dl>
<dt><code>meta_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of non-executable files that are shared among multiple Postfix instances, such as postfix-files, dynamicmaps.cf, and the multi-instance template files main.cf.proto and master.cf.proto.</p>
<dt><code>shlib_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of Postfix dynamically-linked libraries (libpostfix-*.so), and the default location of Postfix database plugins (postfix-*.so) that have a relative pathname in the dynamicmaps.cf file.</dl>
<p> Available in Postfix version 3.1 and later:</p>
<dl>
<dt><code>openssl_path (openssl)</code></p>
<dd> The location of the OpenSSL command line program <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1).</dl>
<p> Other configuration parameters:</p>
<dl>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd> The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd> A prefix that is prepended to the process name in syslog records, so that, for example, &quot;smtpd&quot; becomes &quot;prefix/smtpd&quot;.</dl>
<p> Available in Postfix version 2.6 and later:</p>
<dl>
<dt><code>multi_instance_directories (empty)</code></p>
<dd> An optional list of non-default Postfix configuration directories; these directories belong to additional Postfix instances that share the Postfix executable files and documentation with the default Postfix instance, and that are started, stopped, etc., together with the default Postfix instance.</p>
<dt><code>multi_instance_wrapper (empty)</code></p>
<dd> The pathname of a multi-instance manager command that the <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) command invokes when the multi_instance_directories parameter value is non-empty.</p>
<dt><code>multi_instance_group (empty)</code></p>
<dd> The optional instance group name of this Postfix instance.</p>
<dt><code>multi_instance_name (empty)</code></p>
<dd> The optional instance name of this Postfix instance.</p>
<dt><code>multi_instance_enable (no)</code></p>
<dd> Allow this Postfix instance to be started, stopped, etc., by a multi-instance manager.</dl>
<p> Available in Postfix version 3.4 and later:</p>
<dl>
<dt><code>maillog_file (empty)</code></p>
<dd> The name of an optional logfile that is written by the Postfix <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8) service.</p>
<dt><code>maillog_file_compressor (gzip)</code></p>
<dd> The program to run after rotating $maillog_file with &quot;postfix logrotate&quot;.</p>
<dt><code>maillog_file_prefixes (/var, /dev/stdout)</code></p>
<dd> A list of allowed prefixes for a maillog_file value.</p>
<dt><code>maillog_file_rotate_suffix (%Y%M%d-%H%M%S)</code></p>
<dd> The format of the suffix to append to $maillog_file while rotating the file with &quot;postfix logrotate&quot;.</p>
<dt><code>postlog_service_name (postlog)</code></p>
<dd> The name of the <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8) service entry in master.cf.</dl>
<h2>FILES</h2>
<p> Prior to Postfix version 2.6, all of the following files were in <code>$config_directory</code>. Some files are now in <code>$daemon_directory</code> so that they can be shared among multiple instances that run the same Postfix version. </p>
<p> Use the command &quot;<code>postconf config_directory</code>&quot; or &quot;<code>postconf daemon_directory</code>&quot; to expand the names into their actual values. </p>
<pre>
$config_directory/main.cf, Postfix configuration parameters
$config_directory/master.cf, Postfix daemon processes
$daemon_directory/postfix-files, file/directory permissions
$daemon_directory/postfix-script, administrative commands
$daemon_directory/post-install, post-installation configuration
$daemon_directory/dynamicmaps.cf, plug-in database clients
</pre>
<h2>SEE ALSO</h2>
<pre>
Commands:
<a href="//www.systutorials.com/docs/linux/man/1-postalias/">postalias</a>(1), create/update/query alias database
<a href="//www.systutorials.com/docs/linux/man/1-postcat/">postcat</a>(1), examine Postfix queue file
<a href="//www.systutorials.com/docs/linux/man/1-postconf/">postconf</a>(1), Postfix configuration utility
<a href="//www.systutorials.com/docs/linux/man/1-postfix/">postfix</a>(1), Postfix control program
<a href="//www.systutorials.com/docs/linux/man/1-postfix-tls/">postfix-tls</a>(1), Postfix TLS management
<a href="//www.systutorials.com/docs/linux/man/1-postkick/">postkick</a>(1), trigger Postfix daemon
<a href="//www.systutorials.com/docs/linux/man/1-postlock/">postlock</a>(1), Postfix-compatible locking
<a href="//www.systutorials.com/docs/linux/man/1-postlog/">postlog</a>(1), Postfix-compatible logging
<a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/1-postmulti/">postmulti</a>(1), Postfix multi-instance manager
<a href="//www.systutorials.com/docs/linux/man/1-postqueue/">postqueue</a>(1), Postfix mail queue control
<a href="//www.systutorials.com/docs/linux/man/1-postsuper/">postsuper</a>(1), Postfix housekeeping
<a href="//www.systutorials.com/docs/linux/man/1-mailq/">mailq</a>(1), Sendmail compatibility interface
<a href="//www.systutorials.com/docs/linux/man/1-newaliases/">newaliases</a>(1), Sendmail compatibility interface
<a href="//www.systutorials.com/docs/linux/man/1-sendmail/">sendmail</a>(1), Sendmail compatibility interface
Postfix configuration:
<a href="//www.systutorials.com/docs/linux/man/5-bounce/">bounce</a>(5), Postfix bounce message templates
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), Postfix master.cf file syntax
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), Postfix main.cf file syntax
<a href="//www.systutorials.com/docs/linux/man/5-postfix-wrapper/">postfix-wrapper</a>(5), Postfix multi-instance API
Table-driven mechanisms:
<a href="//www.systutorials.com/docs/linux/man/5-access/">access</a>(5), Postfix SMTP access control table
<a href="//www.systutorials.com/docs/linux/man/5-aliases/">aliases</a>(5), Postfix alias database
<a href="//www.systutorials.com/docs/linux/man/5-canonical/">canonical</a>(5), Postfix input address rewriting
<a href="//www.systutorials.com/docs/linux/man/5-generic/">generic</a>(5), Postfix output address rewriting
<a href="//www.systutorials.com/docs/linux/man/5-header_checks/">header_checks</a>(5), <a href="//www.systutorials.com/docs/linux/man/5-body_checks/">body_checks</a>(5), Postfix content inspection
<a href="//www.systutorials.com/docs/linux/man/5-relocated/">relocated</a>(5), Users that have moved
<a href="//www.systutorials.com/docs/linux/man/5-transport/">transport</a>(5), Postfix routing table
<a href="//www.systutorials.com/docs/linux/man/5-virtual/">virtual</a>(5), Postfix virtual aliasing
Table lookup mechanisms:
<a href="//www.systutorials.com/docs/linux/man/5-cidr_table/">cidr_table</a>(5), Associate CIDR pattern with value
<a href="//www.systutorials.com/docs/linux/man/5-ldap_table/">ldap_table</a>(5), Postfix LDAP client
<a href="//www.systutorials.com/docs/linux/man/5-lmdb_table/">lmdb_table</a>(5), Postfix LMDB database driver
<a href="//www.systutorials.com/docs/linux/man/5-memcache_table/">memcache_table</a>(5), Postfix memcache client
<a href="//www.systutorials.com/docs/linux/man/5-mysql_table/">mysql_table</a>(5), Postfix MYSQL client
<a href="//www.systutorials.com/docs/linux/man/5-nisplus_table/">nisplus_table</a>(5), Postfix NIS+ client
<a href="//www.systutorials.com/docs/linux/man/5-pcre_table/">pcre_table</a>(5), Associate PCRE pattern with value
<a href="//www.systutorials.com/docs/linux/man/5-pgsql_table/">pgsql_table</a>(5), Postfix PostgreSQL client
<a href="//www.systutorials.com/docs/linux/man/5-regexp_table/">regexp_table</a>(5), Associate POSIX regexp pattern with value
<a href="//www.systutorials.com/docs/linux/man/5-socketmap_table/">socketmap_table</a>(5), Postfix socketmap client
<a href="//www.systutorials.com/docs/linux/man/5-sqlite_table/">sqlite_table</a>(5), Postfix SQLite database driver
<a href="//www.systutorials.com/docs/linux/man/5-tcp_table/">tcp_table</a>(5), Postfix client-server table lookup
Daemon processes:
<a href="//www.systutorials.com/docs/linux/man/8-anvil/">anvil</a>(8), Postfix connection/rate limiting
<a href="//www.systutorials.com/docs/linux/man/8-bounce/">bounce</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-defer/">defer</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-trace/">trace</a>(8), Delivery status reports
<a href="//www.systutorials.com/docs/linux/man/8-cleanup/">cleanup</a>(8), canonicalize and enqueue message
<a href="//www.systutorials.com/docs/linux/man/8-discard/">discard</a>(8), Postfix discard delivery agent
<a href="//www.systutorials.com/docs/linux/man/8-dnsblog/">dnsblog</a>(8), DNS black/whitelist logger
<a href="//www.systutorials.com/docs/linux/man/8-error/">error</a>(8), Postfix error delivery agent
<a href="//www.systutorials.com/docs/linux/man/8-flush/">flush</a>(8), Postfix fast ETRN service
<a href="//www.systutorials.com/docs/linux/man/8-local/">local</a>(8), Postfix local delivery agent
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), Postfix master daemon
<a href="//www.systutorials.com/docs/linux/man/8-oqmgr/">oqmgr</a>(8), old Postfix queue manager
<a href="//www.systutorials.com/docs/linux/man/8-pickup/">pickup</a>(8), Postfix local mail pickup
<a href="//www.systutorials.com/docs/linux/man/8-pipe/">pipe</a>(8), deliver mail to non-Postfix command
<a href="//www.systutorials.com/docs/linux/man/8-postlogd/">postlogd</a>(8), Postfix internal logging service
<a href="//www.systutorials.com/docs/linux/man/8-postscreen/">postscreen</a>(8), Postfix zombie blocker
<a href="//www.systutorials.com/docs/linux/man/8-proxymap/">proxymap</a>(8), Postfix lookup table proxy server
<a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), Postfix queue manager
<a href="//www.systutorials.com/docs/linux/man/8-qmqpd/">qmqpd</a>(8), Postfix QMQP server
<a href="//www.systutorials.com/docs/linux/man/8-scache/">scache</a>(8), Postfix connection cache manager
<a href="//www.systutorials.com/docs/linux/man/8-showq/">showq</a>(8), list Postfix mail queue
<a href="//www.systutorials.com/docs/linux/man/8-smtp/">smtp</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-lmtp/">lmtp</a>(8), Postfix SMTP+LMTP client
<a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), Postfix SMTP server
<a href="//www.systutorials.com/docs/linux/man/8-spawn/">spawn</a>(8), run non-Postfix server
<a href="//www.systutorials.com/docs/linux/man/8-tlsmgr/">tlsmgr</a>(8), Postfix TLS cache and randomness manager
<a href="//www.systutorials.com/docs/linux/man/8-tlsproxy/">tlsproxy</a>(8), Postfix TLS proxy server
<a href="//www.systutorials.com/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a>(8), Postfix address rewriting
<a href="//www.systutorials.com/docs/linux/man/8-verify/">verify</a>(8), Postfix address verification
<a href="//www.systutorials.com/docs/linux/man/8-virtual/">virtual</a>(8), Postfix virtual delivery agent
Other:
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging
</pre>
<h2>README FILES</h2>
<p> Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>
OVERVIEW, overview of Postfix commands and processes
BASIC_CONFIGURATION_README, Postfix basic configuration
ADDRESS_REWRITING_README, Postfix address rewriting
SMTPD_ACCESS_README, SMTP relay/access control
CONTENT_INSPECTION_README, Postfix content inspection
QSHAPE_README, Postfix queue analysis
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
TLS support by:
Lutz Jaenicke
Brandenburg University of Technology
Cottbus, Germany
Victor Duchovni
Morgan Stanley
SASL support originally by:
Till Franke
SuSE Rhein/Main AG
65760 Eschborn, Germany
LMTP support originally by:
Philip A. Prindeville
Mirapoint, Inc.
USA.
Amos Gouaux
University of Texas at Dallas
P.O. Box 830688, MC34
Richardson, TX 75083, USA
IPv6 support originally by:
Mark Huizer, Eindhoven University, The Netherlands
Jun-ichiro 'itojun' Hagino, KAME project, Japan
The Linux PLD project
Dean Strik, Eindhoven University, The Netherlands
</pre>
<h2>Index</h2>
