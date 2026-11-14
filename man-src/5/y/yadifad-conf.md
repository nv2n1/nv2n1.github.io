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
<dt><code>&lt;main&gt;</code></p>
<dd>&nbsp;<wbr>General container&nbsp;<wbr></p>
<dt>&lt;key&gt;</p>
<dd>TSIG keys</p>
<dt>&lt;acl&gt;</p>
<dd>Access lists</p>
<dt>&lt;nsid&gt;</p>
<dd>NameServer IDentifier</p>
<dt>&lt;rrl&gt;</p>
<dd>Response Rate Limiting directives</p>
<dt>&lt;zone&gt;</p>
<dd>Description of the domain name in specific attributes.</p>
<dt>&lt;channels&gt;</p>
<dd>Description of the logger outputs.</p>
<dt>&lt;dnssec-policy&gt;</p>
<dd>Description of dnssec policies.</p>
<dt>&lt;key-suite&gt;</p>
<dd>Description of the key-suites needed if &#8216;dnssec policies&#8217; are used.</p>
<dt>&lt;key-roll&gt;</p>
<dd>Description of the key-rolls needed if &#8216;dnssec policies&#8217; are used.</p>
<dt>&lt;key-template&gt;</p>
<dd>Description of the key-templates needed if &#8216;dnssec policies&#8217; are used.</p>
<dt>&lt;denial&gt;</p>
<dd>Description of &#8216;denial&#8217;, this can be used in certain &#8216;dnssec policies&#8217;.</dl>
<p> The configuration supports included files.<br />
 example: include /etc/yadifa/conf.d/local.conf The configuration files can be nested. The configuration consists of:</p>
<dl>
<dt><code>*</code></p>
<dd>Container, which starts with &lt;container name&gt; and ends with &lt;/container name&gt;</p>
<dt><code>*</code></p>
<dd>Variable name</p>
<dt><code>*</code></p>
<dd>1 or 2 arguments</p>
<dt><code>*</code></p>
<dd>Arguments can contain 1 or more comma separated values.</dl>
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
<dt><code>*</code></p>
<dd>Main</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Config with includes</p>
<dl>
<dd>
<pre># start yadifad.conf &lt;main&gt; container
include /etc/yadifa/conf.d/local.conf
# end yadifad.conf &lt;main&gt; container</pre>
</dl>
<dt>2.</p>
<dd>Main without includes</p>
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
</dl>
</dl>
</dl>
</dl>
<dl>
<dt><code>*</code></p>
<dd>Key<br />
 TSIG-key configuration
</dl>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Admin-key key definition (the name is arbitrary)</p>
<dl>
<dd>
<pre>&lt;key&gt;
 name abroad-admin-key
 algorithm hmac-md5
 secret WorthlessKeyForExample==
&lt;/key&gt;</pre>
</dl>
<dt>2.</p>
<dd>Master-slave key definition</p>
<dl>
<dd>
<pre>&lt;key&gt;
 name master-slave
 algorithm hmac-md5
 secret MasterAndSlavesTSIGKey==
&lt;/key&gt;</pre>
</dl>
</dl>
</dl>
<dl>
<dt><code>*</code></p>
<dd>ACL<br />
 Access Control List definitions
</dl>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Master-slave key use</p>
<dl>
<dd>
<pre>&lt;acl&gt;
 transferer key master-slave
 admins 192.0.2.0/24, 2001:db8::74
 master 192.0.2.53
 localhost 127.0.0.0/8, ::1
&lt;/acl&gt;</pre>
<dl>
<dt><code>*</code></p>
<dd>NSID<br />
 DNS NameServer IDentifier
</dl>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Example with ascii</p>
<dl>
<dd>
<pre>&lt;nsid&gt;
 ascii belgium-brussels-01
&lt;/nsid&gt;</pre>
</dl>
<dt>2.</p>
<dd>Example with hex</p>
<dl>
<dd>
<pre>&lt;nsid&gt;
 hex 00320201
&lt;/nsid&gt;</pre>
</dl>
</dl>
</dl>
<dl>
<dt><code>*</code></p>
<dd>RRL<br />
 Response Rate Limiting</dl>
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
<dt><code>*</code></p>
<dd>Zone</dl>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Master domain zone config</p>
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
</dl>
<dt>2.</p>
<dd>Slave domain zone config</p>
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
<dl>
<dt><code>*</code></p>
<dd>DNSSEC-Policy</dl>
<p> DNSSEC-Policy needs some extra sections: key-suite, key-roll, key-template (and denial if NSEC3 is configured)</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>dnssec-policy example with all the needed sections</p>
<dl>
<dd>example with NSEC3 </p>
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
<dt>2.</p>
<dd>key-suite </p>
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
<dt>3.</p>
<dd>key-roll </p>
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
<dt>4.</p>
<dd>key-template </p>
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
<dt>5.</p>
<dd>denial </p>
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
<dl>
<dt><code>*</code></p>
<dd>Channels</dl>
<p> Logging output-channel configurations: The &quot;name&quot; is arbitrary and is used in the &lt;loggers&gt;.<br />
 The &quot;stream-name&quot; defines the output type (ie: a file name or syslog).<br />
 The &quot;arguments&quot; are specific to the output type (ie: unix file access rights or syslog options and facilities).
 </dl>
<dl>
<dt>1.</p>
<dd>Example: YADIFA running as daemon channel definition. </p>
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
</dl>
<dt>2.</p>
<dd>Example: YADIFA running in debug mode.<br />
 This example shows the &quot;stderr&quot; and &quot;stdout&quot; which can also be used in the first example, but will output to the console.</p>
<dl>
<dd>
<pre>&lt;channels&gt;
# name stream-name arguments
 syslog syslog user
 stderr STDERR
 stdout STDOUT
&lt;/channels&gt;</pre>
<dl>
<dt><code>*</code></p>
<dd>Loggers</dl>
<p> Logging input configurations: The &quot;bundle&quot; name is predefined: database, dnssec, server, statistics, system, zone.<br />
 The &quot;debuglevel&quot; uses the same names as syslog or &quot;*&quot; or &quot;all&quot; to filter the input.<br />
 The &quot;channels&quot; are a comma-separated list of channels.</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Example without syslog</p>
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
</dl>
<dt>2.</p>
<dd>Example with syslog</p>
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
</dl>
</dl>
</dl>
<p> The defined loggers are:</p>
<dl>
<dd></dl>
<dl>
<dt>system</p>
<dd>contains low level messages about the system such as memory allocation, threading, IOs, timers and cryptography, &#8230;</p>
<dt>database</p>
<dd>It contains messages about most lower-level operations in the DNS database. ie: journal, updates, zone loading and sanitization, DNS message query resolution, &#8230;)</p>
<dt>dnssec</p>
<dd>contains messages about lower-level dnssec operations in the DNS database. ie: status, maintenance, verification, &#8230;</p>
<dt>server</p>
<dd>contains messages about operations in the DNS server. ie: start up, shutdown, configuration, transfers, various services status (database management, network management, DNS notification management, dynamic update management, resource rate limiting, &#8230;)</p>
<dt>zone</p>
<dd>contains messages about the loading of a zone from a source (file parsing, transferred binary zone reading, &#8230;)</p>
<dt>stats</p>
<dd>contains the statistics of the server.</p>
<dt>queries</p>
<dd>contains the queries on the server. Queries can be logged with the BIND and/or with the YADIFA format. </p>
<p> <code>BIND format:</code> </p>
<p> client sender-ip#port: query: fqdn class type +SETDC (listen-ip) </p>
<p> <code>YADIFA format:</code> </p>
<p> query [ id ] {+SETDC} fqdn class type (sender-ip#port) </p>
<p> where:</p>
<dl>
<dd>
<dl>
<dt>id</p>
<dd>is the query message id</p>
<dt>+</p>
<dd>means the message has the Recursion Desired flag set</p>
<dt>S</p>
<dd>means the message is signed with a TSIG</p>
<dt>E</p>
<dd>means the message is EDNS</p>
<dt>T</p>
<dd>means the message was sent using TCP instead of UDP</p>
<dt>D</p>
<dd>means the message has the DNSSEC OK flag set</p>
<dt>C</p>
<dd>means the message has the Checking Disabled flag set</p>
<dt>fqdn</p>
<dd>is the queried FQDN</p>
<dt>class</p>
<dd>is the queried class</p>
<dt>type</p>
<dd>is the queried type</p>
<dt>sender-ip</p>
<dd>is the IP of the client that sent the query</p>
<dt>port</p>
<dd>is the port of the client that sent the query</p>
<dt>listen-ip</p>
<dd>is the listen network interface that received the message</dl>
</dl>
<dl>
<dd>Note that on YADIFA any unset flag is replaced by a &#8216;-&#8216;, on BIND only the &#8216;+&#8217; follows that rule.</dl>
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
<dt><code>*</code></p>
<dd><code>yadifa-users [at] mailinglists.yadifa.eu</code><br />
 for submitting questions/answers.</dl>
<dl>
<dt><code>*</code></p>
<dd><code><a rel="nofollow" href="http://www.yadifa.eu/mailing-list-users">http://www.yadifa.eu/mailing-list-users</a></code><br />
 for subscription requests.</dl>
<p> If you would like to stay informed about new versions and official patches send a subscription request to via:</p>
<dl>
<dt><code>*</code></p>
<dd><code><a rel="nofollow" href="http://www.yadifa.eu/mailing-list-announcements">http://www.yadifa.eu/mailing-list-announcements</a></code></dl>
<p> (this is a readonly list).</p>
<h2>License And Copyright</h2>
<dl>
<dt>Copyright</p>
<dd>(C)2012-2016, EURid<br />
 B-1831 Diegem, Belgium<br />
 <code>info [at] yadifa.eu</code></dl>
<h2>Authors</h2>
<p>Gery Van Emelen<br />
 Email: <code>Gery.VanEmelen [at] EURid.eu</code><br />
 Eric Diaz Fernandez<br />
 Email: <code>Eric.DiazFernandez [at] EURid.eu</code> </p>
<p> WWW: <code><a rel="nofollow" href="http://www.EURid.eu">http://www.EURid.eu</a></code></p>
