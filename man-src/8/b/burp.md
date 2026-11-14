---
title: "burp(8)"
name: "burp"
section: "8"
letter: "b"
url: "/docs/linux/man/8-burp/"
description: "Burp – BackUp and Restore Program"
---

<p>Burp &#8211; BackUp and Restore Program</p>
<h2>Synopsis</h2>
<p><code>burp [OPTIONS]</code></p>
<h2>Description</h2>
<p>BackUp and Restore Program. </p>
<h2>Server Options</h2>
<dl>
<dt><code>-c</code> <code>[path]</code></p>
<dd>Short for &#8216;config file&#8217;. The argument is a path to the config file. The default is /etc/burp/burp.conf.</p>
<dt><code>-n</code></p>
<dd>No forking mode. The program will accept a single query, deal with it, and then exit. This is useful for debugging. Implies &#8216;-F&#8217;.</p>
<dt><code>-F</code></p>
<dd>Foreground mode. The server will fork into the background and run as a daemon if you do not give this option.</p>
<dt><code>-g</code></p>
<dd>Generate initial CA keys and certificates, and then exit.</p>
<dt><code>-t</code></p>
<dd>Dry-run mode to test config file syntax.</p>
<dt><code>-i</code></p>
<dd>Print an index table of symbols that humans may see burp produce, and exit.</p>
<dt><code>-a s</code></p>
<dd>Run this to connect to a running server to get a live monitor of the status of all your backup clients. If your server config file is not in the default location, you will also need to specify the path with the &#8216;-c&#8217; option. The live monitor requires ncurses support at compile time.</p>
<dt><code>-a S</code></p>
<dd>Similar to &#8216;-a s&#8217;, but it prints the main status monitor summary screen to stdout. The intention is that a script can run this and email an administrator the output on a cron job. This doesn&#8217;t require ncurses support. There are additional options that can be given with &#8216;-a S&#8217;, listed below. These enable logs and contents of backups to be listed whilst logged in on the server machine.</p>
<dt>ADDITIONAL SERVER OPTIONS TO USE WITH &#8216;-a S&#8217;</p>
<dd>
<dt><code>-C</code> <code>[client]</code></p>
<dd>Limit the output to a single client.</p>
<dt><code>-b</code> <code>[number]</code></p>
<dd>Show listable files in a particular backup (requires -C).</p>
<dt><code>-z</code> <code>[file]</code></p>
<dd>Dump a particular log file in a backup (requires -C and -b).</p>
<dt><code>-d</code> <code>[path]</code></p>
<dd>Show a particular path in a backup (requires -C and -b). </p>
</dl>
<h2>Client Options</h2>
<dl>
<dt><code>-a</code> <code>[b|t|r|l|L|v|delete|e|T]</code></p>
<dd>Short for &#8216;action&#8217;. The arguments mean backup, timed backup, restore, list, long list, verify, delete, estimate, or timer check respectively.</p>
<dt><code>-b</code> <code>[number|a]</code></p>
<dd>Short for &#8216;backup number&#8217;. The argument is a number, or &#8216;a&#8217; to select all backups.</p>
<dt><code>-c</code> <code>[path]</code></p>
<dd>Short for &#8216;config file&#8217;. The argument is a path to the config file. The default is /etc/burp/burp.conf, or %PROGRAMFILES%\Burpurp.conf on Windows.</p>
<dt><code>-C</code> <code>[client]</code></p>
<dd>Allows you to specify an alternative client to list or restore from. Requires that the server configuration of the alternative client permits your client to do this. See the &#8216;restore_client&#8217; option.</p>
<dt><code>-d</code> <code>[path]</code></p>
<dd>Short for &#8216;directory&#8217;. When restoring, the argument is a path to an alternative directory to restore to. When listing, the argument is the directory to list.</p>
<dt><code>-f</code> <code>[path]</code></p>
<dd>Short for &#8216;force overwrite&#8217;. Without this option set, a restore will not overwrite existing files.</p>
<dt><code>-i</code></p>
<dd>Print an index table of symbols that humans may see burp produce, and exit.</p>
<dt><code>-r</code> <code>[regex]</code></p>
<dd>Short for &#8216;regular expression&#8217;. The argument is a regular expression with which to match backup files. Use it for lists and restores.</p>
<dt><code>-s</code> <code>[number]</code></p>
<dd>For use with restores &#8211; strip a number of leading path components.</p>
<dt><code>-j</code></p>
<dd>Format list output as JSON.</p>
<dt><code>-t</code></p>
<dd>Dry-run mode to test config file syntax.</p>
<dt><code>-x</code></p>
<dd>For Windows clients only &#8211; do not use the Windows VSS API on restore. Give this option when you are restoring a backup that contains no VSS information. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>burp -a b</code></p>
<dd>Runs a backup.</p>
<dt><code>burp -a l</code></p>
<dd>Lists the available backups and dates.</p>
<dt><code>burp -a l -b 1</code></p>
<dd>Lists all the files in backup number 1.</p>
<dt><code>burp -a l -b a</code></p>
<dd>Lists all the files in all the backups.</p>
<dt><code>burp -a l -b 1 -r myregex</code></p>
<dd>Lists all the files in backup number 1 that match the regular expression &#8216;myregex&#8217;.</p>
<dt><code>burp -a L -b 1 -r myregex</code></p>
<dd>Long lists all the files in backup number 1 that match the regular expression &#8216;myregex&#8217;. This is like doing an &#8216;ls -l&#8217;.</p>
<dt><code>burp -a r -b 1 -r myregex</code></p>
<dd>Restores all the files in backup number 1 that match the regular expression &#8216;myregex&#8217; back to their original location.</p>
<dt><code>burp -a r -b 1 -r myregex -d /tmp/restoredir</code></p>
<dd>Restores all the files in backup number 1 that match the regular expression &#8216;myregex&#8217; into the directory /tmp/restoredir.</p>
<dt><code>burp -a r -b 1 -r myregex -d /tmp/restoredir -s 2</code></p>
<dd>Restores all the files in backup number 1 that match the regular expression &#8216;myregex&#8217; into the directory /tmp/restoredir and strip 2 leading path components.</p>
<dt><code>burp -a r</code></p>
<dd>Restores all the files in the most recent backup to their original location.</p>
<dt><code>burp -a v</code></p>
<dd>Verifies the most recent backup.</p>
<dt><code>burp -a v -b 1 -r myregex</code></p>
<dd>Verifies everything in backup number 1 that matches the regular expression &#8216;myregex&#8217;.</p>
<dt><code>burp -a delete -b 1</code></p>
<dd>Deletes backup number 1. Note that burp will not delete backup directories that other backup directories depend upon.</p>
<dt><code>burp -a t</code></p>
<dd>Timed backup. The same as &#8216;burp -a b&#8217;, except that a script is run on the server before deciding to go ahead. The intention is that this command will be run on a repeating cron job with a short interval, and that the server will decide when it is time for a new backup.</p>
<dt><code>burp -a T</code></p>
<dd>Check whether it is time to do backup, but don&#8217;t actually do a backup. The client will return 0 to mean that it is time, or 3 to mean that it is not time. Any other return code indicates an error.</p>
<dt><code>burp -a L -b 1 -d &#8221;</code></p>
<dd>Long list the top level directory of backup 1.</p>
<dt><code>burp -a L -b 1 -d &#8216;/home/graham&#8217;</code></p>
<dd>Long list the /home/graham directory of backup 1. These &#8216;-d&#8217; versions of the list function provide the ability to &#8216;browse&#8217; backups.</p>
<dt><code>burp -C altclient -a L</code></p>
<dd>Long list the top level directory of backup 1 on client &#8216;altclient&#8217;.</p>
<dt><code>burp -C altclient -a r -b 1 -r myregex -d /tmp/restoredir</code></p>
<dd>Restores all the files in backup number 1 from client &#8216;altclient&#8217; that match the regular expression &#8216;myregex&#8217; into the directory /tmp/restoredir. </p>
<h2>Server Configuration File Options</h2>
<dl>
<dt><code>. [path]</code></p>
<dd>Read an additional configuration file.</p>
<dt><code>mode=server</code></p>
<dd>Required to run in server mode.</p>
<dt><code>port=[port number]</code></p>
<dd>Defines the main TCP port that the server listens on.</p>
<dt><code>status_port=[port number]</code></p>
<dd>Defines the TCP port that the server listens on for status requests.</p>
<dt><code>daemon=[0|1]</code></p>
<dd>Whether to daemonise. The default is 1.</p>
<dt><code>fork=[0|1]</code></p>
<dd>Whether to fork children. The default is 1.</p>
<dt><code>directory=[path]</code></p>
<dd>Path to the directory in which to store backups.</p>
<dt><code>directory_tree=[0|1]</code></p>
<dd>When turned on (which is the default) and the client is on version 1.3.6 or greater, the structure of the storage directory will mimic that of the original filesystem on the client.</p>
<dt><code>timestamp_format=[strftime format]</code></p>
<dd>This allows you to tweak the format of the timestamps of individual backups. See &#8216;man strftime&#8217; to see available substitutions. If this option is unset, burp uses &quot;%Y-%m-%d %H:%M:%S&quot;.</p>
<dt><code>password_check=[0|1]</code></p>
<dd>Allows you to turn client password checking on or off. The default is on. SSL certificates will still be checked if you turn passwords off. This option can be overridden by the client configuration files in clientconfdir on the server.</p>
<dt><code>manual_delete=[path]</code></p>
<dd>If a path is given, the server will move directories to be deleted into the directory specified by the path, but will not actually delete them. The path must be on the same file system as the backup storage. The idea is that a busy server may be configured to run the deletions outside of the backup timebands, when the server is less busy, via a cron job. The default is unset, which means that the server will automatically delete the directories at the end of a backup. This option can be overridden by the client configuration files in clientconfdir on the server.</p>
<dt><code>clientconfdir=[path]</code></p>
<dd>Path to the directory that contains client configuration files.</p>
<dt><code>lockfile=[path]</code></p>
<dd>Path to the lockfile that ensures that two server processes cannot run simultaneously.</p>
<dt><code>pidfile=[path]</code></p>
<dd>Synonym for lockfile.</p>
<dt><code>syslog=[0|1]</code></p>
<dd>Log to syslog. Defaults to off.</p>
<dt><code>stdout=[0|1]</code></p>
<dd>Log to stdout. Defaults to on.</p>
<dt><code>keep=[number]</code></p>
<dd>Number of backups to keep. This can be overridden by the client configuration files in clientconfdir on the server. Specify multiple &#8216;keep&#8217; entries on separate lines in order to keep multiple periods of backups. For example, assuming that you are doing a backup a day, keep=7 keep=4 keep=6 (on separate lines) will keep 7 daily backups, 4 weekly backups (7&#215;4=28), and 6 multiples of 4 weeks (7x4x6=168) &#8211; roughly 6 monthly backups. Effectively, you will be guaranteed to be able to restore up to 168 days ago, with the number of available backups exponentially decreasing as you go back in time to that point. In this example, every 7th backup will be hardlinked to allow burp to safely delete intermediate backups when necessary. You can have as many &#8216;keep&#8217; lines as you like, as long as they don&#8217;t exceed 52560000 when multiplied together. That is, a backup every minute for 100 years.</p>
<dt><code>hardlinked_archive=[0|1]</code></p>
<dd>On the server, defines whether to keep hardlinked files in the backups, or whether to generate reverse deltas and delete the original files. Can be set to either 0 (off) or 1 (on). Disadvantage: More disk space will be used Advantage: Restores will be faster, and since no reverse deltas need to be generated, the time and effort the server needs at the end of a backup is reduced.</p>
<dt><code>max_hardlinks=[number]</code></p>
<dd>On the server, the number of times that a single file can be hardlinked. The bedup program also obeys this setting. The default is 10000.</p>
<dt><code>librsync=[0|1]</code></p>
<dd>When set to 0, delta differencing will not take place. That is, when a file changes, the server will request the whole new file. The default is 1. This option can be overridden by the client configuration files in clientconfdir on the server.</p>
<dt><code>compression=gzip[0-9]</code></p>
<dd>Choose the level of gzip compression for files stored in backups. Setting 0 or gzip0 turns compression off. The default is gzip9. This option can be overridden by the client configuration files in clientconfdir on the server.</p>
<dt><code>hard_quota=[b/Kb/Mb/Gb]</code></p>
<dd>Do not back up the client if the estimated size of all files is greater than the specified size. Example: &#8216;hard_quota = 100Gb&#8217;. Set to 0 (the default) to have no limit.</p>
<dt><code>soft_quota=[b/Kb/Mb/Gb]</code></p>
<dd>A warning will be issued when the estimated size of all files is greater than the specified size and smaller than hard_quota. Example: &#8216;soft_quota = 95Gb&#8217;. Set to 0 (the default) to have no warning.</p>
<dt><code>version_warn=[0|1]</code></p>
<dd>When this is on, which is the default, a warning will be issued when the client version does not match the server version. This option can be overridden by the client configuration files in clientconfdir on the server.</p>
<dt><code>client_lockdir=[path]</code></p>
<dd>Path to the directory in which to keep per-client lock files. By default, this is set to the path given by the &#8216;directory&#8217; option.</p>
<dt><code>user=[username]</code></p>
<dd>Run as a particular user. This can be overridden by the client configuration files in clientconfdir on the server.</p>
<dt><code>group=[groupname]</code></p>
<dd>Run as a particular group. This can be overridden by the client configuration files in clientconfdir on the server.</p>
<dt><code>umask=[umask]</code></p>
<dd>Set the file creation umask. Default is 0022.</p>
<dt><code>ratelimit=[Mb/s]</code></p>
<dd>Set the network send rate limit, in Mb/s. If this option is not given, burp will send data as fast as it can.</p>
<dt><code>network_timeout=[s]</code></p>
<dd>Set the network timeout in seconds. If no data is sent or received over a period of this length, burp will give up. The default is 7200 seconds (2 hours).</p>
<dt><code>working_dir_recovery_method=[resume|use|delete]</code></p>
<dd>This option tells the server what to do when it finds the working directory of an interrupted backup (perhaps somebody pulled the plug on the server, or something). This can be overridden by the client configurations files in clientconfdir on the server. Options are&#8230;</p>
<dt><code>delete:</code> Just delete the old working directory.</p>
<dd>
<dt><code>use:</code> Convert the working directory into a complete backup.</p>
<dd>
<dt><code>resume:</code> Simply continue the previous backup from the point at which it left off, at file granularity. NOTE: If the client has changed its include/exclude configuration since the backup was interrupted, the recovery method will automatically switch to &#8216;use&#8217;.</p>
<dd>
<dt><code>resume_partial=[0|1]</code></p>
<dd>Turn this on to enable &#8216;resume partial&#8217; code. Requires &#8216;working_dir_recovery_method=resume&#8217;. When resuming an interrupted transfer of a single file, it attempts to use previously transferred blocks of that file in order to be more efficient. However, situations have been reported where the file on the server side just gets bigger forever, so this feature now defaults to being turned off.</p>
<dt><code>client_can_delete=[0|1]</code></p>
<dd>Turn this off to prevent clients from deleting backups with the &#8216;-a D&#8217; option. The default is that clients can delete backups. Restore clients can override this setting.</p>
<dt><code>client_can_force_backup=[0|1]</code></p>
<dd>Turn this off to prevent clients from forcing backups with the &#8216;-a b&#8217; option. Timed backups will still work. The default is that clients can force backups.</p>
<dt><code>client_can_list=[0|1]</code></p>
<dd>Turn this off to prevent clients from listing backups with the &#8216;-a l&#8217; option. The default is that clients can list backups. Restore clients can override this setting.</p>
<dt><code>client_can_restore=[0|1]</code></p>
<dd>Turn this off to prevent clients from initiating restores with the &#8216;-a r&#8217; option. The default is that clients can initiate restores. Restore clients can override this setting.</p>
<dt><code>client_can_verify=[0|1]</code></p>
<dd>Turn this off to prevent clients from initiating a verify job with the &#8216;-a v&#8217; option. The default is that clients can initiate a verify job. Restore clients can override this setting.</p>
<dt><code>restore_client=[client]</code></p>
<dd>A client that is permitted to list, verify, restore and delete files belonging to any other client. You may specify multiple restore_clients. If this is too permissive, you may set a restore_client for individual original clients in the individual clientconfdir files. Note that restoring a backup from a Windows computer onto a Linux computer will currently leave the VSS headers in place at the beginning of each file. This will be addressed in a future version of burp.</p>
<dt><code>ssl_cert_ca=[path]</code></p>
<dd>The path to the SSL CA certificate. This file will probably be the same on both the server and the client. The file should contain just the certificate in PEM format. For more information on this, and the other ssl_* options, please see docs/burp_ca.txt.</p>
<dt><code>ssl_cert=[path]</code></p>
<dd>The path to the server SSL certificate. It works for me when the file contains the concatenation of the certificate and private key in PEM format.</p>
<dt><code>ssl_key=[path]</code></p>
<dd>The path to the server SSL private key in PEM format.</p>
<dt><code>ssl_key_password=[password]</code></p>
<dd>The SSL key password.</p>
<dt><code>ssl_cert_password=[password]</code></p>
<dd>Synonym for ssl_key_password.</p>
<dt><code>ssl_ciphers=[cipher list]</code></p>
<dd>Allowed SSL ciphers. See openssl ciphers for details.</p>
<dt><code>ssl_dhfile=[path]</code></p>
<dd>Path to Diffie-Hellman parameter file. To generate one with openssl, use a command like this: openssl dhparam -out dhfile.pem -5 1024</p>
<dt><code>max_children=[number]</code></p>
<dd>Defines the number of child processes to fork (the number of clients that can simultaneously connect. The default is 5.</p>
<dt><code>max_status_children=[number]</code></p>
<dd>Defines the number of status child processes to fork (the number of status clients that can simultaneously connect. The default is 5.</p>
<dt><code>max_storage_subdirs=[number]</code></p>
<dd>Defines the number of subdirectories in the data storage areas. The maximum number of subdirectories that ext3 allows is 32000. If you do not set this option, it defaults to 30000.</p>
<dt><code>timer_script=[path]</code></p>
<dd>Path to the script to run when a client connects with the timed backup option. If the script exits with code 0, a backup will run. The first two arguments are the client name and the path to the &#8216;current&#8217; storage directory. The next three arguments are reserved, and user arguments are appended after that. An example timer script is provided. The timer_script option can be overridden by the client configuration files in clientconfdir on the server.</p>
<dt><code>timer_arg=[string]</code></p>
<dd>A user-definable argument to the timer script. You can have many of these. The timer_arg options can be overridden by the client configuration files in clientconfdir on the server.</p>
<dt><code>notify_success_script=[path]</code></p>
<dd>Path to the script to run when a backup succeeds. User arguments are appended after the first five reserved arguments. An example notify script is provided. The notify_success_script option can be overriddden by the client configuration files in clientconfdir on the server.</p>
<dt><code>notify_success_arg=[string]</code></p>
<dd>A user-definable argument to the notify success script. You can have many of these. The notify_success_arg options can be overriddden by the client configuration files in clientconfdir on the server.</p>
<dt><code>notify_success_warnings_only=[0|1]</code></p>
<dd>Set to 1 to send success notifications when there were warnings. If this and notify_success_changes_only are not turned on, success notifications are always sent.</p>
<dt><code>notify_success_changes_only=[0|1]</code></p>
<dd>Set to 1 to send success notifications when there were new or changed files. If this and notify_success_warnings_only are not turned on, success notifications are always sent.</p>
<dt><code>notify_failure_script=[path]</code></p>
<dd>The same as notify_success_script, but for backups that failed.</p>
<dt><code>notify_failure_arg=[string]</code></p>
<dd>The same as notify_success_arg, but for backups that failed.</p>
<dt><code>dedup_group=[string]</code></p>
<dd>Enables you to group clients together for file deduplication purposes. For example, you might want to set &#8216;dedup_group=xp&#8217; for each Windows XP client, and then run the bedup program on a cron job every other day with the option &#8216;-g xp&#8217;.</p>
<dt><code>server_script_pre=[path]</code></p>
<dd>Path to a script to run on the server after each successfully authenticated connection but before any work is carried out. The arguments to it are &#8216;pre&#8217;, &#8216;(client command)&#8217;, &#8216;reserved3&#8217; to &#8216;reserved5&#8217;, and then arguments defined by server_script_pre_arg. If the script returns non-zero, the task asked for by the client will not be run. This command and related options can be overriddden by the client configuration files in clientconfdir on the server.</p>
<dt><code>server_script_pre_arg=[string]</code></p>
<dd>A user-definable argument to the server pre script. You can have many of these.</p>
<dt><code>server_script_pre_notify=[0|1]</code></p>
<dd>Turn on to send a notification email when the server pre script returns non-zero. The output of the script will be included in the email. The default is off. Most people will not want this turned on because clients usually contact the server at 20 minute intervals and this could cause a lot of emails to be generated. Requires the notify_failure options to be set.</p>
<dt><code>server_script_post=[path]</code></p>
<dd>Path to a script to run on the server before the client disconnects. The arguments to it are &#8216;post&#8217;, &#8216;(client command)&#8217;, &#8216;reserved3&#8217; to &#8216;reserved5&#8217;, and then arguments defined by server_script_post_arg. This command and related options can be overriddden by the client configuration files in clientconfdir on the server.</p>
<dt><code>server_script_post_arg=[string]</code></p>
<dd>A user-definable argument to the server post script. You can have many of these.</p>
<dt><code>server_script_post_notify=[0|1]</code></p>
<dd>Turn on to send a notification email when the server post script returns non-zero. The output of the script will be included in the email. The default is off. Requires the notify_failure options to be set.</p>
<dt><code>server_script=[path]</code></p>
<dd>You can use this to save space in your config file when you want to run the same server script twice. It overrides server_script_pre and server_script_post. This command and related options can be overriddden by the client configuration files in clientconfdir on the server.</p>
<dt><code>server_script_arg=[path]</code></p>
<dd>Goes with server_script and overrides server_script_pre_arg and server_script_post_arg.</p>
<dt><code>server_script_notify=[0|1]</code></p>
<dd>Turn on to send a notification emails when the server pre and post scripts return non-zero. The output of the script will be included it the email. The default is off. Requires the notify_failure options to be set.</p>
<dt><code>server_script_post_run_on_fail=[0|1]</code></p>
<dd>If this is set to 1, server_script_post will always be run. The default is 0, which means that if the task asked for by the client fails, server_script_post will not be run.</p>
<dt><code>autoupgrade_dir=[path]</code></p>
<dd>Path to autoupgrade directory from which upgrades are downloaded. The option can be left unset in order not to autoupgrade clients. Please see docs/autoupgrade.txt in the source package for more help with this option.</p>
<dt><code>ca_conf=[path]</code></p>
<dd>Path to certificate authority configuration file. The CA configuration file will usually be /etc/burp/CA.cnf. The CA directory indicated by CA.cnf will usually be /etc/burp/CA. If ca_conf is set and the CA directory does not exist, the server will create, populate it, and the paths indicated by ssl_cert_ca, ssl_cert, ssl_key and ssl_dhfile will be overwritten. For more detailed information on this and the other ca_* options, please see docs/burp_ca.txt.</p>
<dt><code>ca_name=[name]</code></p>
<dd>Name of the CA that the server will generate when using the ca_conf option.</p>
<dt><code>ca_server_name=[name]</code></p>
<dd>The name that the server will put into its own SSL certficates when using the ca_conf option.</p>
<dt><code>ca_burp_ca=[path]</code></p>
<dd>Path to the burp_ca script when using the ca_conf option. </p>
</dl>
<h2>Client Configuration File Options</h2>
<dl>
<dt><code>. [path]</code></p>
<dd>Read an additional configuration file.</p>
<dt><code>mode=client</code></p>
<dd>Required to run in client mode.</p>
<dt><code>server=[IP address or hostname]</code></p>
<dd>Defines the server to connect to.</p>
<dt><code>port=[port number]</code></p>
<dd>Defines the TCP port that the server is listening on.</p>
<dt><code>cname=[password]</code></p>
<dd>Defines the client name to identify as to the server.</p>
<dt><code>password=[password]</code></p>
<dd>Defines the password to send to the server.</p>
<dt><code>lockfile=[path]</code></p>
<dd>Path to the lockfile that ensures that two client processes cannot run simultaneously (this currently doesn&#8217;t work on Windows).</p>
<dt><code>pidfile=[path]</code></p>
<dd>Synonym for lockfile.</p>
<dt><code>syslog=[0|1]</code></p>
<dd>Log to syslog. Defaults to off.</p>
<dt><code>stdout=[0|1]</code></p>
<dd>Log to stdout. Defaults to on.</p>
<dt><code>progress_counter=[0|1]</code></p>
<dd>Print progress counters on stdout. Defaults to on.</p>
<dt><code>user=[username]</code></p>
<dd>Run as a particular user (not supported on Windows).</p>
<dt><code>group=[groupname]</code></p>
<dd>Run as a particular group (not supported on Windows).</p>
<dt><code>ratelimit=[Mb/s]</code></p>
<dd>Set the network send rate limit, in Mb/s. If this option is not given, burp will send data as fast as it can.</p>
<dt><code>network_timeout=[s]</code></p>
<dd>Set the network timeout in seconds. If no data is sent or received over a period of this length, burp will give up. The default is 7200 seconds (2 hours).</p>
<dt><code>ca_burp_ca=[path]</code></p>
<dd>Path to the burp_ca script (burp_ca.bat on Windows). For more information on this, please see docs/burp_ca.txt.</p>
<dt><code>ca_csr_dir=[path]</code></p>
<dd>Directory where certificate signing requests are generated. For more information on this, please see docs/burp_ca.txt.</p>
<dt><code>ssl_cert_ca=[path]</code></p>
<dd>The path to the SSL CA certificate. This file will probably be the same on both the server and the client. The file should contain just the certificate in PEM format. For more information on this and the other ssl_* options, please see docs/burp_ca.txt.</p>
<dt><code>ssl_cert=[path]</code></p>
<dd>The path to the client SSL certificate. It works for me when the file contains the concatenation of the certificate and private key in PEM format.</p>
<dt><code>ssl_key=[path]</code></p>
<dd>The path to the client SSL private key in PEM format.</p>
<dt><code>ssl_key_password=[password]</code></p>
<dd>The SSL key password.</p>
<dt><code>ssl_cert_password=[password]</code></p>
<dd>Synonym for ssl_key_password.</p>
<dt><code>ssl_peer_cn=[string]</code></p>
<dd>Must match the common name in the SSL certificate that the server gives when it connects. If ssl_peer_cn is not set, the server name will be used instead.</p>
<dt><code>ssl_ciphers=[cipher list]</code></p>
<dd>Allowed SSL ciphers. See openssl ciphers for details.</p>
<dt><code>server_can_restore=[0|1]</code></p>
<dd>To prevent the server from initiating restores, set this to 0. The default is 1.</p>
<dt><code>encryption_password=[password]</code></p>
<dd>Set this to enable client side file Blowfish encryption. If you do not want encryption, leave this field out of your config file. <code>IMPORTANT:</code> Configuring this renders delta differencing pointless, since the smallest real change to a file will make the whole file look different. Therefore, activating this option turns off delta differencing so that whenever a client file changes, the whole new file will be uploaded on the next backup. <code>ALSO IMPORTANT:</code> If you manage to lose your encryption password, you will not be able to unencrypt your files. You should therefore think about having a copy of the encryption password somewhere off-box, in case of your client hard disk failing. <code>FINALLY:</code> If you change your encryption password, you will end up with a mixture of files on the server with different encryption and it may become tricky to restore more than one file at a time. For this reason, if you change your encryption password, you may want to start a fresh chain of backups (by moving the original set aside, for example). Burp will cope fine with turning the same encryption password on and off between backups, and will restore a backup of mixed encrypted and unencrypted files without a problem.</p>
<dt><code>backup_script_pre=[path]</code></p>
<dd>Path to a script to run before a backup. The arguments to it are &#8216;pre&#8217;, &#8216;reserved2&#8217; to &#8216;reserved5&#8217;, and then arguments defined by backup_script_pre_arg.</p>
<dt><code>backup_script_pre_arg=[string]</code></p>
<dd>A user-definable argument to the backup pre script. You can have many of these.</p>
<dt><code>backup_script_post=[path]</code></p>
<dd>Path to a script to run after a backup. The arguments to it are &#8216;post&#8217;, [0|1] if the backup failed or succeeded, &#8216;reserved3&#8217; to &#8216;reserved5&#8217;, and then arguments defined by backup_script_post_arg.</p>
<dt><code>backup_script_post_arg=[string]</code></p>
<dd>A user-definable argument to the backup post script. You can have many of these.</p>
<dt><code>backup_script_post_run_on_fail=[0|1]</code></p>
<dd>If this is set to 1, backup_script_post will be run whether the backup succeeds or not. The default is 0, which means that backup_script_post will only be run if the backup succeeds.</p>
<dt><code>restore_script_pre=[path]</code></p>
<dd>Path to a script to run before a restore. The arguments to it are &#8216;pre&#8217;, &#8216;reserved2&#8217; to &#8216;reserved5&#8217;, and then arguments defined by restore_script_pre_arg.</p>
<dt><code>restore_script_pre_arg=[string]</code></p>
<dd>A user-definable argument to the restore pre script. You can have many of these.</p>
<dt><code>restore_script_post=[path]</code></p>
<dd>Path to a script to run after a restore. The arguments to it are &#8216;post&#8217;, [0|1] if the restore failed or succeeded, &#8216;reserved3&#8217; to &#8216;reserved5&#8217;, and then arguments defined by restore_script_post_arg.</p>
<dt><code>restore_script_post_arg=[string]</code></p>
<dd>A user-definable argument to the restore post script. You can have many of these.</p>
<dt><code>restore_script_post_run_on_fail=[0|1]</code></p>
<dd>If this is set to 1, restore_script_post will be run whether the restore succeeds or not. The default is 0, which means that restore_script_post will only be run if the restore succeeds.</p>
<dt><code>backup_script=[path]</code></p>
<dd>You can use this to save space in your config file when you want to run the same script before and after a backup. It overrides backup_script_pre and backup_script_post.</p>
<dt><code>backup_script_arg=[path]</code></p>
<dd>Goes with backup_script and overrides backup_script_pre_arg and backup_script_post_arg.</p>
<dt><code>restore_script=[path]</code></p>
<dd>You can use this to save space in your config file when you want to run the same script before and after a restore. It overrides restore_script_pre and restore_script_post.</p>
<dt><code>restore_script_arg=[path]</code></p>
<dd>Goes with restore_script and overrides restore_script_pre_arg and restore_script_post_arg.</p>
<dt><code>autoupgrade_dir=[path]</code></p>
<dd>Path to autoupgrade directory into which upgrades are downloaded. Please see docs/autoupgrade.txt in the source package for more help with this option. If you do not want your client to autoupgrade, do not set this option.</p>
<dt><code>autoupgrade_os=[string]</code></p>
<dd>Name of the client operating system. Should match a directory name in the server&#8217;s autoupgrade_dir. If you do not want your client to autoupgrade, do not set this option. </p>
</dl>
<h2>Includes / Excludes</h2>
<dl>
<dt>The following options specify exactly what is backed up. The client can specify these options, or if you have at least one &#8216;include=&#8217; or &#8216;include_glob=&#8217; in the client configuration files on the server, the server will override them all.</p>
<dd>
<dt><code>include=[path]</code></p>
<dd>Path to include in the backup. You can have multiple include lines. Use forward slashes &#8216;/&#8217;, not backslashes &#8216;\&#8217; as path delimiters.</p>
<dt><code>exclude=[path]</code></p>
<dd>Path to exclude from the backup. You can have multiple exclude lines. Use forward slashes &#8216;/&#8217;, not backslashes &#8216;\&#8217; as path delimiters.</p>
<dt><code>include_regex=[regular expression]</code></p>
<dd>Not implemented.</p>
<dt><code>include_glob=[glob expression]</code></p>
<dd>Include paths that match the glob expression. For example, &#8216;/home/*/Documents&#8217; will include &#8216;/home/user1/Documents&#8217; and &#8216;/home/user2/Documents&#8217; if user1 and user2 exist. On Unix systems, <a href="/docs/linux/man/3-glob/">glob</a>(3) is used. For Windows systems, the functionality is limited to one &#8216;*&#8217;.</p>
<dt><code>exclude_regex=[regular expression]</code></p>
<dd>Exclude paths that match the regular expression.</p>
<dt><code>include_ext=[extension]</code></p>
<dd>Extensions to include in the backup. Case insensitive. Nothing else will be included in the backup. You can have multiple include extension lines. For example, set &#8216;txt&#8217; to include files that end in &#8216;.txt&#8217;. You need to specify an &#8216;include&#8217; line so that burp knows where to start looking.</p>
<dt><code>exclude_ext=[extension]</code></p>
<dd>Extensions to exclude from the backup. Case insensitive. You can have multiple exclude extension lines. For example, set &#8216;vdi&#8217; to exclude VirtualBox disk images.</p>
<dt><code>exclude_comp=[extension]</code></p>
<dd>Extensions to exclude from compression. Case insensitive. You can have multiple exclude compression lines. For example, set &#8216;gz&#8217; to exclude gzipped files from compression.</p>
<dt><code>exclude_fs=[fstype]</code></p>
<dd>File systems to exclude from the backup. Case insensitive. You can have multiple exclude file system lines. For example, set &#8216;tmpfs&#8217; to exclude tmpfs. Burp has an internal mapping of file system names to file system IDs. If you know the file system ID, you can use that instead. For example, &#8216;exclude_fs = 0x01021994&#8217; will also exclude tmpfs.</p>
<dt><code>min_file_size=[b/Kb/Mb/Gb]</code></p>
<dd>Do not back up files that are less than the specified size. Example: &#8216;min_file_size = 10Mb&#8217;. Set to 0 (the default) to have no limit.</p>
<dt><code>max_file_size=[b/Kb/Mb/Gb]</code></p>
<dd>Do not back up files that are greater than the specified size. Example: &#8216;max_file_size = 10Mb&#8217;. Set to 0 (the default) to have no limit.</p>
<dt><code>cross_filesystem=[path]</code></p>
<dd>Allow backups to cross a particular filesystem mountpoint.</p>
<dt><code>cross_all_filesystems=[0|1]</code></p>
<dd>Allow backups to cross all filesystem mountpoints.</p>
<dt><code>nobackup=[file name]</code></p>
<dd>If this file system entry exists, the directory containing it will not be backed up.</p>
<dt><code>read_fifo=[path]</code></p>
<dd>Do not back up the given fifo itself, but open it for reading and back up the contents as if it were a regular file.</p>
<dt><code>read_all_fifos=[0|1]</code></p>
<dd>Open all fifos for reading and back up the contents as if they were regular files.</p>
<dt><code>read_blockdev=[path]</code></p>
<dd>Do not back up the given block device itself, but open it for reading and back up the contents as if it were a regular file.</p>
<dt><code>read_all_blockdevs=[0|1]</code></p>
<dd>Open all block devices for reading and back up the contents as if they were regular files.</p>
<dt><code>split_vss=[0|1]</code></p>
<dd>When backing up Windows computers, this option allows you to save the VSS header data separate from the file data. The default is off, which means that the VSS header data is saved prepended to the file data.</p>
<dt><code>strip_vss=[0|1]</code></p>
<dd>When backing up Windows computers, this option allows you to prevent the VSS header data being backed up. The default is off. To restore a backup that has no VSS information on Windows, you need to give the client the &#8216;-x&#8217; command line option.</p>
<dt><code>vss_drives=[list of drive letters]</code></p>
<dd>When backing up Windows computers, this option allows you to specify which drives have VSS snapshots taken of them. If you omit this option, burp will automatically decide based on the &#8216;include&#8217; options. If you want no drives to have snapshots taken of them, you can specify &#8216;0&#8217;.</p>
<dt><code>atime=[0|1]</code></p>
<dd>This allows you to control whether the client uses O_NOATIME when opening files and directories. The default is 0, which enables O_NOATIME. This means that the client can read files and directories without updating the access times. However, this is only possible if you are running as root, or are the owner of the file or directory. If this is not the case (perhaps you only have group or world access to the files), you will get errors until you set atime=1. With atime=1, the access times will be updated on the files and directories that get backed up. As an alternative, you may consider setting capability &#8216;CAP_FOWNER&#8217; on the client burp binary &#8211; see &#8216;man capabilities&#8217;. </p>
</dl>
<h2>Server Clientconfdir File</h2>
<dl>
<dt>For the server to know about clients that can contact it, you need to place a file named after the client in clientconfdir. Files beginning with &#8216;.&#8217; or ending with &#8216;~&#8217; are ignored. Directories are also ignored.</p>
<dd>
<dt>The file name must match the name in the &#8216;cname&#8217; field on the client.</p>
<dd>
<dt><code>ssl_peer_cn=[string]</code> must match the common name in the SSL certificate that the client gives when it connects. If ssl_peer_cn is not set, the client name will be used instead (the clientconfdir file name).</p>
<dd>
<dt>The file needs to contain a line like <code>password=[password]</code> that matches the same field on the client, or <code>passwd=[encrypted password]</code> &#8211; where the plain text password on the client will be tested against an encrypted password of the kind you might find in /etc/passwd.</p>
<dd>
<dt>Additionally, the following options can be overridden here for each client:</p>
<dd><code>directory</code> <code>directory_tree</code> <code>timestamp_format</code> <code>password_check</code> <code>keep</code> <code>working_dir_recovery_method</code> <code>resume_partial</code> <code>librsync</code> <code>manual_delete</code> <code>version_warn</code> <code>syslog</code> <code>client_can_delete</code> <code>client_can_force_backup</code> <code>client_can_list</code> <code>client_can_restore</code> <code>client_can_verify</code> <code>restore_client</code> <code>compression</code> <code>hard_quota</code> <code>soft_quota</code> <code>timer_script</code> <code>timer_arg</code> <code>notify_success_script</code> <code>notify_success_arg</code> <code>notify_success_warnings_only</code> <code>notify_failure_script</code> <code>notify_failure_arg</code> <code>dedup_group</code> <code>server_script_pre</code> <code>server_script_pre_arg</code> <code>server_script_pre_notify</code> <code>server_script_post</code> <code>server_script_post_arg</code> <code>server_script_post_notify</code> <code>server_script</code> <code>server_script_arg</code> <code>server_script_notify</code> <code>server_script_post_run_on_fail</code></p>
<dt>Additionally, the includes and excludes can be overridden here, as described in the section above.</p>
<dd>
<dt>As with the other configuration files, extra configuration can be included with the &#8216;. path/to/config/file&#8217; syntax.</p>
<dd></dl>
<h2>Some notes on SSL certificates</h2>
<dl>
<dt>The burp example configs come with example SSL certificates and keys. You can use these and burp will work. But if you are worried about network security, you should generate your own certificates and keys and point your config files to them. To create the example files, I used a handy interface to openssl, called &#8216;tinyca&#8217; (<a rel="nofollow" href="http://tinyca.sm-zone.net/">http://tinyca.sm-zone.net/</a>). If you are using Debian, you can run &#8216;apt-get install tinyca&#8217; to get it. There is also the option of using burp_ca, which you can find in the source distribution, courtesy of Patrick Koppen.</p>
<dd></dl>
<h2>Examining backups</h2>
<dl>
<dt>As well as using the client list options described above, you can go directly to the storage directory on the server. The backups for a client are in the directory named after the client. Inside each backup directory is a file called manifest.gz.</p>
<dd>
<dt>This contains a list of all the files in the backup, and where they originally came from on the client.</p>
<dd>
<dt>There is also a &#8216;log.gz&#8217; file in the backup directory, which contains the output generated by the server during the backup.</p>
<dd>
<dt>The &#8216;data&#8217; directory contains complete backup files.</p>
<dd>
<dt>The &#8216;deltas.reverse&#8217; directory contains reverse deltas that can be applied to the data from the next backup in the sequence (indicated by the contents of the &#8216;forward&#8217; file).</p>
<dd>
<dt>Anything with a .gz suffix is compressed in gzip format. You can use standard tools, such as zcat, zless or cp, to view them or copy them elsewhere. Files from Windows backups will probably contain VSS headers and/or footers. For help stripping these, see the vss_strip man page.</p>
<dd></dl>
<h2>Server initiated backups</h2>
<dl>
<dt>You can queue a backup on the server, to be performed when the client next makes contact. To do this, you put a file called &#8216;backup&#8217; into the top level of the client storage directory. The contents of the file are ignored.</p>
<dd></dl>
<h2>Server initiated restores</h2>
<dl>
<dt>You can queue a restore on the server, to be performed when the client next makes contact. To do this, you put a file called &#8216;restore&#8217; into the top level of the client storage directory. The client can deny server initiated restores by setting &quot;server_can_restore=0&quot; in its burp.conf. Valid fields to include in the restore file are:</p>
<dd>
<dt><code>orig_client=[client]</code></p>
<dd>The original client to restore from. Equivalent to &#8216;-C&#8217; when initiating a restore from a client. Do not include this line when restoring to the original client. See also the &#8216;restore_client&#8217; server option.</p>
<dt><code>backup=[number|a]</code></p>
<dd>The number of the backup to restore from. Equivalent to &#8216;-b&#8217; when initiating a restore from the client.</p>
<dt><code>overwrite=[0|1]</code></p>
<dd>Whether to overwrite existing files. Equivalent to &#8216;-f&#8217; when initiating a restore from the client.</p>
<dt><code>strip=[number]</code></p>
<dd>Number of leading path components to strip. Equivalent to &#8216;-s&#8217; when initiating a restore from the client.</p>
<dt><code>restoreprefix=[path]</code></p>
<dd>Prefix to the restore path. Equivalent to &#8216;-d&#8217; when initiating a restore from the client.</p>
<dt><code>regex=[regular expression]</code></p>
<dd>Only restore files matching the regular expression. Equivalent to &#8216;-r&#8217; when initiating a restore from the client.</p>
<dt><code>include=[path]</code></p>
<dd>Restore directories and files that match the path. If it is a directory, the contents of the directory will be restored. You can have multiple &#8216;include&#8217; lines. There is no equivalent when initiating a restore from the client.</p>
<dt>As a minimum, the &#8216;restore&#8217; file needs to contain a &#8216;backup&#8217; option.</p>
<dd></dl>
<h2>Signals</h2>
<p>Sending signal 1 (HUP) to the main server process will cause it to reload. For the vast majority of configuration changes, a reload is unnecessary as the server will pick up changes &quot;on-the-fly&quot;. Sending signal 12 (USR2) to the main server process will cause it to wait until there are no longer any child processes, and then exit. The intention is to help with upgrades without interrupting current backups. if you are running upstart, a new burp server process will start up when the old one exits.</p>
<h2>Bugs</h2>
<p>If you find bugs, please report them to the email list. See the website &lt;<a rel="nofollow" href="http://burp.grke.net/">http://burp.grke.net/</a>&gt; for details. </p>
<h2>Author</h2>
<p>The main author of Burp is Graham Keeling.</p>
<h2>Copyright</h2>
<p>See the LICENCE file included with the source distribution.</p>
