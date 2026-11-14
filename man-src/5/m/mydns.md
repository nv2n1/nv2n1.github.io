---
title: "mydns(5)"
name: "mydns"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mydns/"
description: "mydns.conf – mydns(8) configuration file."
---

<p>mydns.conf &#8211; <code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8) configuration file.</p>
<h2>Description</h2>
<p><code>mydns.conf</code> is read by <code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8) on startup. The default location of this file is <i>/etc/mydns.conf</i>. </p>
<p> A <code>mydns.conf</code> might look something like this:</p>
<dl>
<dd>
<pre># /etc/mydns.conf
# Configuration file for the MyDNS name daemon
db-host = dbserver.example.com
db-user = mydnsuser
db-password = Gr8DNS!</pre>
</dl>
<p> Each line in the file may contain only one configuration variable. All allowable configuration variables are described in this man page. The syntax for a configuration line is `<i>option</i> [<i>=</i> <i>value</i>]&#8217;. All configuration variables have default values, which are used if the variable is omitted from the <code>mydns.conf</code>. These defaults are listed in parentheses after the variable syntax. </p>
<p> All text following a hash mark (`<code>#</code>&#8216;) and empty lines are ignored. If you need to specify an actual hash mark in a option value, escape it by prefixing it with a backslash (`<code>\</code>&#8216;) character. </p>
<p> The <code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8) program has a convenient command-line option that will output all current configuration variables in <code>mydns.conf</code> format. If you are creating a <code>mydns.conf</code> file for the first time, this is a great way to create a template that you can customize. See <code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8) for details.</p>
<h2>Database Information</h2>
<p>The following configuration variables tell MyDNS about your database server.</p>
<dl>
<dt><code>db-host</code> = <i>hostname</i> (`<i>localhost</i>&#8216;)</p>
<dd>Connect to the database server located at <i>hostname</i>.</p>
<dt><code>db-user</code> = <i>username</i></p>
<dd>Use <i>username</i> when authenticating with the database server.</p>
<dt><code>db-password</code> = <i>password</i></p>
<dd>Use <i>password</i> when authenticating with the database server.</p>
<dt><code>database</code> = <i>name</i> (`<i>mydns</i>&#8216;)</p>
<dd>Read resource record information from the database called <i>name</i>. The specified <code>dbuser</code> must have <code>SELECT</code> privileges on the specified database.</dl>
<h2>General Options</h2>
<p>The following configuration variables control the general behavior of the name daemon.</p>
<dl>
<dt><code>user</code> = <i>username</i> (`<i>nobody</i>&#8216;)</p>
<dd>Run the name daemon with the permissions of user <i>username</i>.</p>
<dt><code>group</code> = <i>groupname</i> (`<i>nogroup</i>&#8216;)</p>
<dd>Run the name daemon with the permissions of group <i>groupname</i>.</p>
<dt><code>listen</code> = <i>address</i> (`<i>*</i>&#8216;)</p>
<dd>The name daemon should listen on <i>address</i>. If <i>address</i> is <code>*</code>, listen on all addresses. This must be an IP address in numbers-and-dots format, or <code>*</code>. Multiple addresses may be specified, either separated by commas, or listed on separate <code>listen</code> lines, or both. If a port number other than port 53 is desired, append `<code>:</code><i>port</i>&#8216; to the address.</p>
<dt><code>no-listen</code> = <i>address</i> (`<i>*</i>&#8216;)</p>
<dd>The name daemon should NOT listen on <i>address</i>, even if it was specified by <code>listen</code>. This must be an IP address in numbers-and-dots format, or <code>*</code>. Multiple addresses may be specified, either separated by commas, or listed on separate <code>listen</code> lines, or both. If a port number other than port 53 is desired, append `<code>:</code><i>port</i>&#8216; to the address.</dl>
<h2>Cache Options</h2>
<p>The following configuration variables affect the cache used internally by the name daemon.</p>
<dl>
<dt><code>zone-cache-size</code> = <i>number</i> (`<i>4096</i>&#8216;)</p>
<dd>The zone data cache will not contain more than <i>number</i> entries. The average entry in the cache is about 128 bytes. If <i>number</i> is <code>0</code>, the zone data cache will not be used.</p>
<dt><code>zone-cache-expire</code> = <i>seconds</i> (`<i>60</i>&#8216;)</p>
<dd>Entries expire from the zone data cache once they are <i>seconds</i> old. If <i>seconds</i> is <code>0</code>, the zone data cache will not be used. If the TTL for any RR in the zone is less than the cache expire time, the TTL will be honored.</p>
<dt><code>reply-cache-size</code> = <i>number</i> (`<i>1024</i>&#8216;)</p>
<dd>The reply cache will not contain more than <i>number</i> entries. The average entry in the cache is about 128 bytes. If <i>number</i> is <code>0</code>, the reply cache will not be used.</p>
<dt><code>reply-cache-expire</code> = <i>seconds</i> (`<i>30</i>&#8216;)</p>
<dd>Entries expire from the reply cache once they are <i>seconds</i> old. If <i>seconds</i> is <code>0</code>, the reply cache will not be used.</dl>
<h2>Esoterica</h2>
<p>The following configuration variables affect the name daemon also, but most users will not need to use them.</p>
<dl>
<dt><code>log</code> = <i>facility</i> (`<i>LOG_DAEMON</i>&#8216;)</p>
<dd>The name daemon should log via syslog facility <i>facility</i>. <i>facility</i> may be <code>LOG_DAEMON</code> or <code>LOG_LOCAL0</code> through <code>LOG_LOCAL7</code>. If <i>facility</i> is <code>stderr</code>, program output will go to stderr only.</p>
<dt><code>pidfile</code> = <i>filename</i> (`<i>/var/run/named.pid</i>&#8216;)</p>
<dd>Create a PID file for the name daemon called <i>filename</i>.</p>
<dt><code>timeout</code> = <i>seconds</i> (`<i>120</i>&#8216;)</p>
<dd>Incoming queries time out if a reply could not be sent after <i>seconds</i> have elapsed.</p>
<dt><code>multicpu</code> = <i>cpucount</i> (`<i>1</i>&#8216;)</p>
<dd>Run with multiple processes to support <i>cpucount</i> number of processors.- deprecated use servers instead</p>
<dt><code>servers</code> = <i>servercount</i> (`<i>1</i>&#8216;)</p>
<dd>Number of server processors to run. Set this to 0 to run just a single process, 1 will run a master and a server process. n runs <i>n</i> servers plus a master. It is recommended that this be set to the number of CPUS times 2 plus 1.</p>
<dt><code>recursive</code> = <i>address</i></p>
<dd>If this option is specified, <i>address</i> is the address of a DNS server that accepts recursive queries. If MyDNS receives a query where recursion is desired, and the zone is not local, MyDNS will forward the query to the server at <i>address</i> and return the result to the client.</p>
<dt><code>recursive-timeout</code> = <i>seconds</i> (`<i>60</i>&#8216;)</p>
<dd>Number of seconds to wait before first retry</p>
<dt><code>recursive-retries</code> = <i>count</i> (`<i>5</i>&#8216;)</p>
<dd>Number of retries before abandoning recursion</p>
<dt><code>recursive-algorithm</code> = <i>algorithm</i> (`<i>linear</i>&#8216;)</p>
<dd>Algorithm to use when applying timeout. Linear &#8211; each timeout is equal to recursive-timeout, Exponential &#8211; double timeout on each retry, Progressive &#8211; increase timeout by number of retries.</p>
<dt><code>allow-axfr</code> = <i>bool</i> (`<i>no</i>&#8216;)</p>
<dd>Should DNS-based zone transfers be allowed?</p>
<dt><code>allow-tcp</code> = <i>bool</i> (`<i>no</i>&#8216;)</p>
<dd>Should TCP requests be allowed? <i>(not recommended)</i></p>
<dt><code>allow-update</code> = <i>bool</i> (`<i>no</i>&#8216;)</p>
<dd>Should DNS-based zone updates (RFC 2136) be allowed?</p>
<dt><code>ignore-minimum</code> = <i>bool</i> (`<i>no</i>&#8216;)</p>
<dd>Should MyDNS ignore the minimum TTL for zones?</p>
<dt><code>soa-table</code> = <i>name</i> (`<i>soa</i>&#8216;)</p>
<dd>The name of the table containing SOA records.</p>
<dt><code>rr-table</code> = <i>name</i> (`<i>rr</i>&#8216;)</p>
<dd>The name of the table containing resource record data.</p>
<dt><code>use-soa-active</code> = <i>boolean</i> (`<i>yes</i>&#8216;)</p>
<dd>Where there is an soa-active column use this to determine which zones to serve.</p>
<dt><code>use-rr-active</code> = <i>boolean</i> (`<i>yes</i>&#8216;)</p>
<dd>Where there is a rr-active column use this to determine which records to serve.</p>
<dt><code>notify-enabled</code> = <i>boolean</i> (`<i>yes</i>&#8216;)</p>
<dd>Support DNS NOTIFY message generation if this is enabled.</p>
<dt><code>notify-source</code> = <i>IPv4 address</i> (`<i>0.0.0.0</i>&#8216;)</p>
<dd>IPv4 address from which NOTIFY messages will be sent &#8211; set to 0.0.0.0 or leave blank for the default of using the outgoing interface address.</p>
<dt><code>notify-source6</code> = <i>IPv6 address</i> (`<i>;;</i>&#8216;)</p>
<dd>IPv6 address from which NOTIFY messages will be sent &#8211; set to :: or leave blank for the default of using the outgoing interface address.</p>
<dt><code>notify-timeout</code> = <i>seconds</i> (`<i>60</i>&#8216;)</p>
<dd>Number of seconds before first retry of NOTIFY message</p>
<dt><code>notify-retries</code> = <i>count</i> (`<i>5</i>&#8216;)</p>
<dd>Number of times to retry the NOTIFY message before giving up.</p>
<dt><code>notify-algorithm</code> = <i>string</i> (`<i>linear</i>&#8216;)</p>
<dd>Select type of notify algorithm to use &#8211; select oneof Linear &#8211; each timeout is equal to notify-timeout, Exponential &#8211; double timeout on each retry, Progressive &#8211; increase timeout by number of retries.</p>
<dt><code>ixfr-enabled</code> = <i>boolean</i> (`<i>yes</i>&#8216;)</p>
<dd>Enable IXFR functionality &#8211; requires DB schema change as well.</p>
<dt><code>ixfr-gc-enabled</code> = <i>boolean</i> (`<i>yes</i>&#8216;)</p>
<dd>Enable real-time IXFR garbage collection facility. With this switched on the server will periodically scan the database for expired records that have been marked deleted and will remove them from the DB.</p>
<dt><code>ixfr-gc-interval</code> = <i>seconds</i> (`<i>86400</i>&#8216;)</p>
<dd>Number of seconds between each GC scan. &#8211; default 86400 seconds = 1 day.</p>
<dt><code>ixfr-gc-delay</code></p>
<dd>Number of seconds before first GC scan. &#8211; default 600 seconds = 10 minutes.</p>
<dt><code>extended-data-support</code> = <i>boolean</i> (`<i>no</i>&#8216;)</p>
<dd>Switch on extended data support, this allow resource records to grow very big as needed for large TXT records.</p>
<dt><code>dbengine</code> = <i>string</i> (`<i>MyISAM</i>&#8216;)</p>
<dd>Select DBengine to use when running under MySQL. Has been tested with MyISAM, InnoDB, NDBCLUSTER.</p>
<dt><code>soa-where</code> = <i>string</i></p>
<dd>An extra WHERE clause to append to queries selecting records from the `soa&#8217; table.</p>
<dt><code>rr-where</code> = <i>string</i></p>
<dd>An extra WHERE clause to append to queries selecting records from the `rr&#8217; table.</p>
<dt><code>wildcard-recursion</code> = <i>number of ancestor levels</i></p>
<dd>Allow the server to look in ancestor zones for wildcard matches. This specifies how many levels to scan up before giving up. Use &#8216;0&#8217; (the default) to switch this off, a positive number to specify how many levels and &#8216;-1&#8217; for infinite. [Caveat: Using this feature in the current release 1.2.8 will affect performance if you have deeply nested zones and search many levels. You have been warned, if you need to do this then increase the number of &#8216;servers&#8217;]</p>
<dt><code>debug-&lt;module&gt;</code> = <i>&lt;debug level&gt;</i></p>
<dd>Switches on module based debug for the module in question. The debug level sets the volume and detail of messages produced. See output of &#8211;dump-config option for modules available.</dl>
<h2>Security</h2>
<p>The <i>mydns.conf</i> file should be readable only by the root user (uid=0) since it typically contains a username and password allowing access to your database.</p>
<h2>Files</h2>
<p><i>/etc/mydns.conf</i></p>
<dl>
<dd>The default location of the configuration file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8) </p>
