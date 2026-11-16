---
title: "yadifad-conf(5)"
name: "yadifad-conf"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yadifad-conf/"
description: "yadifad.conf – configuration file for yadifad(8)."
---

<p>yadifad.conf &#8211; configuration file for <i><a href="/docs/linux/man/8-yadifad/">yadifad</a></i>(8). </p>
<h2>Synopsis</h2>
<p>${PREFIX}/etc/yadifad.conf </p>
<h2>Description</h2>
<p>The configuration of yadifad has several containers:</p>
<dl>
<dt><code>&lt;main&gt;</code></dt>
<dd>&nbsp;<wbr>General container&nbsp;<wbr></dd>
<dt>&lt;key&gt;</dt>
<dd>TSIG keys</dd>
<dt>&lt;acl&gt;</dt>
<dd>Access lists</dd>
<dt>&lt;nsid&gt;</dt>
<dd>NameServer IDentifier</dd>
<dt>&lt;rrl&gt;</dt>
<dd>Response Rate Limiting directives</dd>
<dt>&lt;zone&gt;</dt>
<dd>Description of the domain name in specific attributes.</dd>
<dt>&lt;channels&gt;</dt>
<dd>Description of the logger outputs.</dd>
<dt>&lt;dnssec-policy&gt;</dt>
<dd>Description of dnssec policies.</dd>
<dt>&lt;key-suite&gt;</dt>
<dd>Description of the key-suites needed if &#8216;dnssec policies&#8217; are used.</dd>
<dt>&lt;key-roll&gt;</dt>
<dd>Description of the key-rolls needed if &#8216;dnssec policies&#8217; are used.</dd>
<dt>&lt;key-template&gt;</dt>
<dd>Description of the key-templates needed if &#8216;dnssec policies&#8217; are used.</dd>
<dt>&lt;denial&gt;</dt>
<dd>Description of &#8216;denial&#8217;, this can be used in certain &#8216;dnssec policies&#8217;.</dd></dl>
<p> The configuration supports included files.<br />
 example: include /etc/yadifa/conf.d/local.conf The configuration files can be nested. The configuration consists of:</p>
<dl>
<dt><code>*</code></dt>
<dd>Container, which starts with &lt;container name&gt; and ends with &lt;/container name&gt;</dd>
<dt><code>*</code></dt>
<dd>Variable name</dd>
<dt><code>*</code></dt>
<dd>1 or 2 arguments</dd>
<dt><code>*</code></dt>
<dd>Arguments can contain 1 or more comma separated values.</dd></dl>
<p> eg. </p>
<pre>&lt;container&gt;
 # variable argument
 variable value1 
 # variable argument1 argument2
 variable value1 value2
 # variable argument1
 variable value1,value2
&lt;/container&gt;</pre>
<h2>Examples</h2>
<p>Examples of containers defined for a configuration file.</p>
<dl>
<dt><code>*</code></dt>
<dd>Main</dd>
<dl>
<dd>
</dd><dl>
<dt>1.</dt>
<dd>Config with includes</dd>
<dl>
<dd>
<pre># start yadifad.conf &lt;main&gt; container
include /etc/yadifa/conf.d/local.conf
# end yadifad.conf &lt;main&gt; container</pre>
</dd></dl>
<dt>2.</dt>
<dd>Main without includes</dd>
<dl>
<dd>
<pre>&lt;main&gt;
 # Detach from the console (alias: daemonize)
 daemon off
 # Jail the application
 chroot off
 # The path of the log files (alias: chroot-path)
 chrootpath &quot;/chroot/yadifad&quot;
 # The path of the log files (alias: log-path)
 logpath &quot;/var/log/yadifa&quot;
 # The location of the pid file (alias: pid-file)
 pidfile &quot;/var/run/yadifa/yadifad.pid&quot;
 # The path of the zone files (alias: data-path)
 datapath &quot;/var/lib/yadifa&quot;
 # The path of the DNSSEC keys (alias: keys-path)
 keyspath &quot;/var/lib/yadifa/keys&quot;
 # The path of the transfer and journaling files (AXFR &amp; IXFR) (alias: xfr-path)
 xfrpath &quot;/var/lib/yadifa/xfr&quot;
 # A string returned by a query of hostname. CH TXT 
 # note: if you leave this out, the real hostname will be given back (alias: hostname-chaos)
 hostname &quot;server-yadifad&quot;
 # An ID returned by a query to id.server. CH TXT (alias: serverid-chaos)
 serverid &quot;yadifad-01&quot;
 # The version returned by a query to version.yadifa. CH TXT (alias: version-chaos)
 version &quot;2.2.2&quot;
 # Set the maximum UDP packet size. 
 # note: the packetsize cannot be less than 512 or more than 65535.
 # Typical choice is 4096.
 edns0-max-size 4096
 # The maximum number of parallel TCP queries (max-tcp-connections)
 max-tcp-queries 100
 # The minimum data rate for a TCP query (in bytes per second)
 tcp-query-min-rate 512
 # The user id to use (alias: user)
 uid yadifa
 # The group id to use (alias: group)
 gid yadifa
 # The DNS port - any DNS query will use that port unless a specific value is used (alias: server-port)
 port 53
 # The interfaces to listen to.
 # listen 0.0.0.0
 listen 127.0.0.1, 192.0.2.2, 192.0.2.130 port 8053, 2001:db8::2
 # Type of querylog to use
 # 0: none
 # 1: yadifa
 # 2: bind
 # 3: both yadifa and bind
 queries-log-type 1
 # Enable the collection and logging of statistics
 statistics on
 # Maximum number of seconds between two statistics lines
 statistics-max-period 60
 # Drop queries with erroneous content
 #
 # answer-formerr-packets on
 answer-formerr-packets off
 # Maximum number of records in an AXFR packet. Set to 1 for compatibility
 # with very old name servers (alias: axfr-max-record-by-packet)
 axfr-maxrecordbypacket 0
 # Global Access Control rules
 #
 # Rules can be defined on network ranges, TSIG signatures, and ACL rules
 # simple queries:
 #
 # allow-query any
 allow-query !192.0.2.251,any
 # dynamic update of a zone
 #
 # allow-update none
 allow-update admins
 # dynamic update of a slave (forwarded to the master)
 #
 # allow-update-forwarding none
 allow-update-forwarding admins,key abroad-admin-key
 # transfer of a zone (AXFR or IXFR)
 #
 # allow-transfer any
 allow-transfer transferer
 # notify of a change in the master
 #
 # allow-notify any
 allow-notify master,admins
 # If YADIFA has the controller enabled, allow control only for these
 # clients (none by default)
 allow-control localhost
 # overwrite the amount of CPUs detected by yadifad
 cpu-count-override 3
 # set the number of threads to serve queries
 thread-count-by-address 2
&lt;/main&gt;</pre>
</dd></dl>
</dl>
</dl>
</dl>
<dl>
<dt><code>*</code></dt>
<dd>Key<br />
 TSIG-key configuration
</dd></dl>
<dl>
<dd>
</dd><dl>
<dt>1.</dt>
<dd>Admin-key key definition (the name is arbitrary)</dd>
<dl>
<dd>
<pre>&lt;key&gt;
 name abroad-admin-key
 algorithm hmac-md5
 secret WorthlessKeyForExample==
&lt;/key&gt;</pre>
</dd></dl>
<dt>2.</dt>
<dd>Master-slave key definition</dd>
<dl>
<dd>
<pre>&lt;key&gt;
 name master-slave
 algorithm hmac-md5
 secret MasterAndSlavesTSIGKey==
&lt;/key&gt;</pre>
</dd></dl>
</dl>
</dl>
<dl>
<dt><code>*</code></dt>
<dd>ACL<br />
 Access Control List definitions
</dd></dl>
<dl>
<dd>
</dd><dl>
<dt>1.</dt>
<dd>Master-slave key use</dd>
<dl>
<dd>
<pre>&lt;acl&gt;
 transferer key master-slave
 admins 192.0.2.0/24, 2001:db8::74
 master 192.0.2.53
 localhost 127.0.0.0/8, ::1
&lt;/acl&gt;</pre>
</dd><dl>
<dt><code>*</code></dt>
<dd>NSID<br />
 DNS NameServer IDentifier
</dd></dl>
<dl>
<dd>
</dd><dl>
<dt>1.</dt>
<dd>Example with ascii</dd>
<dl>
<dd>
<pre>&lt;nsid&gt;
 ascii belgium-brussels-01
&lt;/nsid&gt;</pre>
</dd></dl>
<dt>2.</dt>
<dd>Example with hex</dd>
<dl>
<dd>
<pre>&lt;nsid&gt;
 hex 00320201
&lt;/nsid&gt;</pre>
</dd></dl>
</dl>
</dl>
<dl>
<dt><code>*</code></dt>
<dd>RRL<br />
 Response Rate Limiting</dd></dl>
<pre>&lt;rrl&gt;
 # Number of identical responses per second before responses are being limited
 responses-per-second 5
 # Number of errors per second before responses are being limited
 errors-per-second 5
 # Random slip parameter
 slip 10
 # If enabled, the rate limits are only logged and not enforced
 log-only off
 # Mask applied to group the IPv4 clients
 ipv4-prefix-length 24
 # Mask applied to group the IPv6 clients
 ipv6-prefix-length 56
 # Rate limits are not subject to the following clients (aka whitelist)
 exempt-clients none
 # Enable or disable the rate limit capabilities
 enabled yes
&lt;/rrl&gt;</pre>
<dl>
<dt><code>*</code></dt>
<dd>Zone</dd></dl>
<dl>
<dd>
</dd><dl>
<dt>1.</dt>
<dd>Master domain zone config</dd>
<dl>
<dd>
<pre>&lt;zone&gt;
 # This server is master for the zone (mandatory)
 type master
 # The domain name (mandatory)
 domain mydomain.eu
 # The zone file, relative to 'datapath' (mandatory for a master) (alias: file-name)
 file master/mydomain.eu
 # List of servers also notified of a change (beside the ones in the zone file) (alias: notifies, notify)
 also-notify 192.0.2.84, 192.0.2.149
 # Set the size of the journal file in KB (alias: journal-size-kb)
 journal-size 8192 
 # Allow dynupdate for these ACL entries
 allow-update admins
 # Allow AXFR/IXFR for these ACL entries
 allow-transfer transferer
 # Use DNSSEC policies otherwise remove or put in remark line below
 dnssec-policy 1
&lt;/zone&gt;</pre>
</dd></dl>
<dt>2.</dt>
<dd>Slave domain zone config</dd>
<dl>
<dd>
<pre>&lt;zone&gt;
 # This server is slave for that zone (mandatory)
 type slave
 # The domain name (mandatory)
 domain myotherdomain.eu
 # The address of the master (mandatory for a slave, forbidden for a master) (alias: master)
 masters 191.0.2.53 port 4053 key master-slave
 # The zone file, relative to 'datapath'.
 file slaves/myotherdomain.eu
 # Accept notifes from these ACL entries
 allow-notify master
&lt;/zone&gt;</pre>
</dd><dl>
<dt><code>*</code></dt>
<dd>DNSSEC-Policy</dd></dl>
<p> DNSSEC-Policy needs some extra sections: key-suite, key-roll, key-template (and denial if NSEC3 is configured)</p>
<dl>
<dd>
</dd><dl>
<dt>1.</dt>
<dd>dnssec-policy example with all the needed sections</dd>
<dl>
<dd>example with NSEC3 </dd>
<pre>&lt;dnssec-policy&gt;
 id &quot;1&quot;
 description &quot;Example of ZSK and KSK&quot;
 denial &quot;nsec3-with-salt-on&quot;
 key-suite &quot;zsk-1024&quot;
 key-suite &quot;ksk-2048&quot;
&lt;/dnssec-policy&gt;</pre>
<p>example with NSEC </p>
<pre>&lt;dnssec-policy&gt;
 id &quot;2&quot;
 description &quot;Example of ZSK and KSK&quot;
 denial nsec
 key-suite &quot;zsk-1024&quot;
 key-suite &quot;ksk-2048&quot;
&lt;/dnssec-policy&gt;</pre>
</dl>
<dt>2.</dt>
<dd>key-suite </dd>
<pre>&lt;key-suite&gt; 
 id &quot;ksk-2048&quot;
 key-template &quot;ksk-2048&quot;
 key-roll &quot;key-roll-ksk-2048-short-times&quot;
&lt;/key-suite&gt; 
&lt;key-suite&gt; 
 id &quot;zsk-1024&quot;
 key-template &quot;zsk-1024&quot;
 key-roll &quot;key-roll-zsk-1024-short-times&quot;
&lt;/key-suite&gt; </pre>
<dt>3.</dt>
<dd>key-roll </dd>
<pre>&lt;key-roll&gt; 
 id &quot;key-roll-ksk-2048-short-times&quot;
# command minutes hours day month day-week week
 generate 5,35 * * * * *
 publish 6,36 * * * * *
 activate 7,37 * * * * *
 inactive 8,38 * * * * * 
 remove 12,42 * * * * *
&lt;/key-roll&gt; 
&lt;key-roll&gt; 
 id &quot;key-roll-zsk-1024-short-times&quot;
# command minutes hours day month day-week week
 generate 5,35 * * * * *
 publish 6,36 * * * * *
 activate 7,37 * * * * *
 inactive 8,38 * * * * * 
 remove 12,42 * * * * *
&lt;/key-roll&gt; </pre>
<dt>4.</dt>
<dd>key-template </dd>
<pre>&lt;key-template&gt;
 id &quot;ksk-2048&quot;
 ksk true
 algorithm 8
 size 2048
&lt;/key-template&gt;
&lt;key-template&gt;
 id &quot;zsk-1024&quot;
 ksk false
 algorithm 8
 size 1024
&lt;/key-template&gt;</pre>
<dt>5.</dt>
<dd>denial </dd>
<pre>&lt;denial&gt; 
 id &quot;nsec3-with-salt-on&quot;
 salt &quot;ABCD&quot;
 algorithm 1
 iterations 5
 optout off 
&lt;/denial&gt; </pre>
<dl>
<dd>
<pre>&lt;denial&gt; 
 id &quot;nsec3-with-salt-length-on&quot;
 salt-length 4
 algorithm 1
 iterations 5
 optout off 
&lt;/denial&gt; </pre>
</dd><dl>
<dt><code>*</code></dt>
<dd>Channels</dd></dl>
<p> Logging output-channel configurations: The &quot;name&quot; is arbitrary and is used in the &lt;loggers&gt;.<br />
 The &quot;stream-name&quot; defines the output type (ie: a file name or syslog).<br />
 The &quot;arguments&quot; are specific to the output type (ie: unix file access rights or syslog options and facilities).
 </dl>
<dl>
<dt>1.</dt>
<dd>Example: YADIFA running as daemon channel definition. </dd>
<dl>
<dd>
<pre>&lt;channels&gt;
# name stream-name arguments
 database database.log 0644
 dnssec dnssec.log 0644
 server server.log 0644
 statistics statistics.log 0644
 system system.log 0644
 queries queries.log 0644
 zone zone.log 0644
 all all.log 0644
 syslog syslog user
&lt;/channels&gt;</pre>
</dd></dl>
<dt>2.</dt>
<dd>Example: YADIFA running in debug mode.<br />
 This example shows the &quot;stderr&quot; and &quot;stdout&quot; which can also be used in the first example, but will output to the console.</dd>
<dl>
<dd>
<pre>&lt;channels&gt;
# name stream-name arguments
 syslog syslog user
 stderr STDERR
 stdout STDOUT
&lt;/channels&gt;</pre>
</dd><dl>
<dt><code>*</code></dt>
<dd>Loggers</dd></dl>
<p> Logging input configurations: The &quot;bundle&quot; name is predefined: database, dnssec, server, statistics, system, zone.<br />
 The &quot;debuglevel&quot; uses the same names as syslog or &quot;*&quot; or &quot;all&quot; to filter the input.<br />
 The &quot;channels&quot; are a comma-separated list of channels.</p>
<dl>
<dd>
</dd><dl>
<dt>1.</dt>
<dd>Example without syslog</dd>
<dl>
<dd>
<pre>&lt;loggers&gt;
# bundle debuglevel channels
 database ALL database,all
 dnssec warning dnssec,all
 server INFO,WARNING,ERR,CRIT,ALERT,EMERG server,all
 statistics * statistics
 system * system,all
 queries * queries
 zone * zone,all
&lt;/loggers&gt;</pre>
</dd></dl>
<dt>2.</dt>
<dd>Example with syslog</dd>
<dl>
<dd>
<pre>&lt;loggers&gt;
# bundle debuglevel channels
 database ALL database,syslog
 dnssec warning dnssec,syslog
 server INFO,WARNING,ERR,CRIT,ALERT,EMERG server,syslog
 stats * statistics, syslog
 system * system,syslog
 queries * queries,syslog
 zone * zone,syslog
&lt;/loggers&gt;</pre>
</dd></dl>
</dl>
</dl>
<p> The defined loggers are:</p>
<dl>
<dd></dd></dl>
<dl>
<dt>system</dt>
<dd>contains low level messages about the system such as memory allocation, threading, IOs, timers and cryptography, &#8230;</dd>
<dt>database</dt>
<dd>It contains messages about most lower-level operations in the DNS database. ie: journal, updates, zone loading and sanitization, DNS message query resolution, &#8230;)</dd>
<dt>dnssec</dt>
<dd>contains messages about lower-level dnssec operations in the DNS database. ie: status, maintenance, verification, &#8230;</dd>
<dt>server</dt>
<dd>contains messages about operations in the DNS server. ie: start up, shutdown, configuration, transfers, various services status (database management, network management, DNS notification management, dynamic update management, resource rate limiting, &#8230;)</dd>
<dt>zone</dt>
<dd>contains messages about the loading of a zone from a source (file parsing, transferred binary zone reading, &#8230;)</dd>
<dt>stats</dt>
<dd>contains the statistics of the server.</dd>
<dt>queries</dt>
<dd>contains the queries on the server. Queries can be logged with the BIND and/or with the YADIFA format. </dd>
<p> <code>BIND format:</code> </p>
<p> client sender-ip#port: query: fqdn class type +SETDC (listen-ip) </p>
<p> <code>YADIFA format:</code> </p>
<p> query [ id ] {+SETDC} fqdn class type (sender-ip#port) </p>
<p> where:</p>
<dl>
<dd>
</dd><dl>
<dt>id</dt>
<dd>is the query message id</dd>
<dt>+</dt>
<dd>means the message has the Recursion Desired flag set</dd>
<dt>S</dt>
<dd>means the message is signed with a TSIG</dd>
<dt>E</dt>
<dd>means the message is EDNS</dd>
<dt>T</dt>
<dd>means the message was sent using TCP instead of UDP</dd>
<dt>D</dt>
<dd>means the message has the DNSSEC OK flag set</dd>
<dt>C</dt>
<dd>means the message has the Checking Disabled flag set</dd>
<dt>fqdn</dt>
<dd>is the queried FQDN</dd>
<dt>class</dt>
<dd>is the queried class</dd>
<dt>type</dt>
<dd>is the queried type</dd>
<dt>sender-ip</dt>
<dd>is the IP of the client that sent the query</dd>
<dt>port</dt>
<dd>is the port of the client that sent the query</dd>
<dt>listen-ip</dt>
<dd>is the listen network interface that received the message</dd></dl>
</dl>
<dl>
<dd>Note that on YADIFA any unset flag is replaced by a &#8216;-&#8216;, on BIND only the &#8216;+&#8217; follows that rule.</dd></dl>
</dl>
<p> System operators will mostly be interested in the info and above messages of queries and stats, as well as the error and above messages of the other loggers. </p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-yadifad/">yadifad</a></i>(8) </p>
<h2>Notes</h2>
<p>Since unquoted leading whitespace is generally ignored in the yadifad.conf you can indent everything to taste. </p>
<h2>Changes</h2>
<p>Please check the file ChangeLog from the sources.</p>
<h2>Version</h2>
<p>Version: 2.2.3 of 2016-12-15.</p>
<h2>Mailing Lists</h2>
<p>There exists a mailinglist for questions relating to any program in the yadifa package: </p>
<dl>
<dt><code>*</code></dt>
<dd><code>yadifa-users [at] mailinglists.yadifa.eu</code><br />
 for submitting questions/answers.</dd></dl>
<dl>
<dt><code>*</code></dt>
<dd><code><a rel="nofollow" href="http://www.yadifa.eu/mailing-list-users">http://www.yadifa.eu/mailing-list-users</a></code><br />
 for subscription requests.</dd></dl>
<p> If you would like to stay informed about new versions and official patches send a subscription request to via:</p>
<dl>
<dt><code>*</code></dt>
<dd><code><a rel="nofollow" href="http://www.yadifa.eu/mailing-list-announcements">http://www.yadifa.eu/mailing-list-announcements</a></code></dd></dl>
<p> (this is a readonly list).</p>
<h2>License And Copyright</h2>
<dl>
<dt>Copyright</dt>
<dd>(C)2012-2016, EURid<br />
 B-1831 Diegem, Belgium<br />
 <code>info [at] yadifa.eu</code></dd></dl>
<h2>Authors</h2>
<p>Gery Van Emelen<br />
 Email: <code>Gery.VanEmelen [at] EURid.eu</code><br />
 Eric Diaz Fernandez<br />
 Email: <code>Eric.DiazFernandez [at] EURid.eu</code> </p>
<p> WWW: <code><a rel="nofollow" href="http://www.EURid.eu">http://www.EURid.eu</a></code></p>
</dl></dl></dl></dl></dl></dl></dl></dl></dl></dl>