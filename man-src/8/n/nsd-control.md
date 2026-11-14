---
title: "nsd-control(8)"
name: "nsd-control"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsd-control/"
description: "nsd-control, nsd-control-setup – NSD remote server control utility."
---

<p><code>nsd-control,</code> <code>nsd-control-setup</code> &#8211; NSD remote server control utility.</p>
<h2>Synopsis</h2>
<p><code>nsd-control</code> [<code>-c</code> <i>cfgfile</i>] [<code>-s</code> <i>server</i>] <i>command</i></p>
<h2>Description</h2>
<p><code>nsd-control</code> performs remote administration on the <i><a href="/docs/linux/man/8-nsd/">nsd</a></i>(8) DNS server. It reads the configuration file, contacts the nsd server over SSL, sends the command and displays the result. </p>
<p> The available options are:</p>
<dl>
<dt><code>-h</code></p>
<dd>Show the version and commandline option help.</p>
<dt><code>-c </code><i>cfgfile</i></p>
<dd>The config file to read with settings. If not given the default config file /etc/nsd/nsd.conf is used.</p>
<dt><code>-s </code><i>server[@port]</i></p>
<dd>IPv4 or IPv6 address of the server to contact. If not given, the address is read from the config file.</dl>
<h2>Commands</h2>
<p>There are several commands that the server understands.</p>
<dl>
<dt><code>start</code></p>
<dd>Start the server. Simply execs <i><a href="/docs/linux/man/8-nsd/">nsd</a></i>(8). The nsd executable is searched for in the <code>PATH</code> set in the environment. It is started with the config file specified using <i>-c</i> or the default config file.</p>
<dt><code>stop</code></p>
<dd>Stop the server. The server daemon exits.</p>
<dt><code>reload [&lt;zone&gt;]</code></p>
<dd>Reload zonefiles and reopen logfile. Without argument reads changed zonefiles. With argument reads the zonefile for the given zone and loads it.</p>
<dt><code>reconfig</code></p>
<dd>Reload nsd.conf and apply changes to TSIG keys and configuration patterns, and apply the changes to add and remove zones that are mentioned in the config. Other changes are not applied, such as listening ip address and port and chroot. The pattern updates means that the configuration options for zones (request-xfr, zonefile, notify, &#8230;) are updated. Also new patterns are available for use with the addzone command.</p>
<dt><code>repattern</code></p>
<dd>Same as the reconfig option.</p>
<dt><code>log_reopen</code></p>
<dd>Reopen the logfile, for log rotate that wants to move the logfile away and create a new logfile. The log can also be reopened with kill -HUP (which also reloads all zonefiles).</p>
<dt><code>status</code></p>
<dd>Display server status. Exit code 3 if not running (the connection to the port is refused), 1 on error, 0 if running.</p>
<dt><code>stats</code></p>
<dd>Output a sequence of name=value lines with statistics information, requires NSD to be compiled with this option enabled.</p>
<dt><code>stats_noreset</code></p>
<dd>Same as stats, but does not zero the counters.</p>
<dt><code>addzone &lt;zone name&gt; &lt;pattern name&gt;</code></p>
<dd>Add a new zone to the running server. The zone is added to the zonelist file on disk, so it stays after a restart. The pattern name determines the options for the new zone. For slave zones a zone transfer is immediately attempted. For zones with a zonefile, the zone file is attempted to be read in.</p>
<dt><code>delzone &lt;zone name&gt;</code></p>
<dd>Remove the zone from the running server. The zone is removed from the zonelist file on disk, from the nsd.db file and from the memory. If it had a zonefile, this remains (but may be outdated). Zones configured inside nsd.conf itself cannot be removed this way because the daemon does not write to the nsd.conf file, you need to add such zones to the zonelist file to be able to delete them with the delzone command.</p>
<dt><code>addzones</code></p>
<dd>Add zones read from stdin of nsd-control. Input is read per line, with name space patternname on a line. For bulk additions.</p>
<dt><code>delzones</code></p>
<dd>Remove zones read from stdin of nsd-control. Input is one name per line. For bulk removals.</p>
<dt><code>write [&lt;zone&gt;]</code></p>
<dd>Write zonefiles to disk, or the given zonefile to disk. Zones that have changed (via AXFR or IXFR) are written, or if the zonefile has not been created yet then it is created. Directory components of the zonefile path are created if necessary.</p>
<dt><code>notify [&lt;zone&gt;]</code></p>
<dd>Send NOTIFY messages to slave servers. Sends to the IP addresses configured in the &#8216;notify:&#8217; lists for the master zones hosted on this server. Usually NSD sends NOTIFY messages right away when a master zone serial is updated. If a zone is given, notifies are sent for that zone. These slave servers are supposed to initiate a zone transfer request later (to this server or another master), this can be allowed via the &#8216;provide-xfr:&#8217; acl list configuration.</p>
<dt><code>transfer [&lt;zone&gt;]</code></p>
<dd>Attempt to update slave zones that are hosted on this server by contacting the masters. The masters are configured via &#8216;request-xfr:&#8217; lists. If a zone is given, that zone is updated. Usually NSD receives a NOTIFY from the masters (configured via &#8216;allow-notify:&#8217; acl list) that a new zone serial has to be transferred. For zones with no content, NSD may have backed off from asking often because the masters did not respond, but this command will reset the backoff to its initial timeout, for frequent retries.</p>
<dt><code>force_transfer [&lt;zone&gt;]</code></p>
<dd>Force update slave zones that are hosted on this server. Even if the master hosts the same serial number of the zone, a full AXFR is performed to fetch it. If you want to use IXFR and check that the serial number increases, use the &#8216;transfer&#8217; command.</p>
<dt><code>zonestatus [&lt;zone&gt;]</code></p>
<dd>Print state of the zone, the serial numbers and since when they have been acquired. Also prints the notify action (to which server), and zone transfer (and from which master) if there is activity right now. The state of the zone is printed as: &#8216;master&#8217; (master zones), &#8216;ok&#8217; (slave zone is up-to-date), &#8216;expired&#8217; (slave zone has expired), &#8216;refreshing&#8217; (slave zone has transfers active). The serial numbers printed are the &#8216;served-serial&#8217; (currently active), the &#8216;commit-serial&#8217; (is in reload), the &#8216;notified-serial&#8217; (got notify, busy fetching the data). The serial numbers are only printed if such a serial number is available.</p>
<dt><code>serverpid</code></p>
<dd>Prints the PID of the server process. This is used for statistics (and only works when NSD is compiled with statistics enabled). This pid is not for sending unix signals, use the pid from nsd.pid for that, that pid is also stable.</p>
<dt><code>verbosity &lt;number&gt;</code></p>
<dd>Change logging verbosity.</dl>
<h2>Exit Code</h2>
<p>The nsd-control program exits with status code 1 on error, 0 on success.</p>
<h2>Set Up</h2>
<p>The setup requires a self-signed certificate and private keys for both the server and client. The script <i>nsd-control-setup</i> generates these in the default run directory, or with -d in another directory. If you change the access control permissions on the key files you can decide who can use nsd-control, by default owner and group but not all users. The script preserves private keys present in the directory. After running the script as root, turn on <code>control-enable</code> in <i>nsd.conf</i>.</p>
<h2>Statistic Counters</h2>
<p>The <i>stats</i> command shows a number of statistic counters.</p>
<dl>
<dt><i>num.queries</i></p>
<dd>number of queries received (the tcp and udp queries added up).</p>
<dt><i>serverX.queries</i></p>
<dd>number of queries handled by the server process. The number of server processes is set with the config statement <code>server-count</code>.</p>
<dt><i>time.boot</i></p>
<dd>uptime in seconds since the server was started. With fractional seconds.</p>
<dt><i>time.elapsed</i></p>
<dd>time since the last stats report, in seconds. With fractional seconds. Can be zero if polled quickly and the previous stats command resets the counters, so that the next gets a fully zero, and zero elapsed time, report.</p>
<dt><i>size.db.disk</i></p>
<dd>size of nsd.db on disk, in bytes.</p>
<dt><i>size.db.mem</i></p>
<dd>size of the DNS database in memory, in bytes.</p>
<dt><i>size.xfrd.mem</i></p>
<dd>size of memory for zone transfers and notifies in xfrd process, excludes TSIG data, in bytes.</p>
<dt><i>size.config.disk</i></p>
<dd>size of zonelist file on disk, excludes the nsd.conf size, in bytes.</p>
<dt><i>size.config.mem</i></p>
<dd>size of config data in memory, kept twice in server and xfrd process, in bytes.</p>
<dt><i>num.type.X</i></p>
<dd>number of queries with this query type.</p>
<dt><i>num.opcode.X</i></p>
<dd>number of queries with this opcode.</p>
<dt><i>num.class.X</i></p>
<dd>number of queries with this query class.</p>
<dt><i>num.rcode.X</i></p>
<dd>number of answers that carried this return code.</p>
<dt><i>num.edns</i></p>
<dd>number of queries with EDNS OPT.</p>
<dt><i>num.ednserr</i></p>
<dd>number of queries which failed EDNS parse.</p>
<dt><i>num.udp</i></p>
<dd>number of queries over UDP ip4.</p>
<dt><i>num.udp6</i></p>
<dd>number of queries over UDP ip6.</p>
<dt><i>num.tcp</i></p>
<dd>number of connections over TCP ip4.</p>
<dt><i>num.tcp6</i></p>
<dd>number of connections over TCP ip6.</p>
<dt><i>num.answer_wo_aa</i></p>
<dd>number of answers with NOERROR rcode and without AA flag, this includes the referrals.</p>
<dt><i>num.rxerr</i></p>
<dd>number of queries for which the receive failed.</p>
<dt><i>num.txerr</i></p>
<dd>number of answers for which the transmit failed.</p>
<dt><i>num.raxfr</i></p>
<dd>number of AXFR requests from clients (that got served with reply).</p>
<dt><i>num.truncated</i></p>
<dd>number of answers with TC flag set.</p>
<dt><i>num.dropped</i></p>
<dd>number of queries that were dropped because they failed sanity check.</p>
<dt><i>zone.master</i></p>
<dd>number of master zones served. These are zones with no &#8216;request-xfr:&#8217; entries.</p>
<dt><i>zone.slave</i></p>
<dd>number of slave zones served. These are zones with &#8216;request-xfr&#8217; entries.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/nsd/nsd.conf</i></p>
<dd>nsd configuration file.</p>
<dt><i>/etc/nsd</i></p>
<dd>directory with private keys (nsd_server.key and nsd_control.key) and self-signed certificates (nsd_server.pem and nsd_control.pem).</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a></i>(5), <i><a href="/docs/linux/man/8-nsd/">nsd</a></i>(8), <i><a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a></i>(8) </p>
