---
title: "yadifad(8)"
name: "yadifad"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yadifad/"
description: "yadifad – an authoritative Internet domain name server."
---

<p>yadifad &#8211; an authoritative Internet domain name server. </p>
<h2>Synopsis</h2>
<p>yadifad [<code>&#8211;config|-c</code><i> configfile</i>] [<code>&#8211;daemon|-d</code>] [<code>-u</code><i> uid</i>] [<code>-g</code><i> gid</i>] [<code>-V</code>] [<code>-h</code>] </p>
<h2>Description</h2>
<p>yadifad is a Domain Name System (DNS) server, part of the YADIFA distribution from EURid vzw/asbl. The latest version of YADIFA can be found on:<br />
 <center> <code><a rel="nofollow" href="http://www.yadifa.eu/download">http://www.yadifa.eu/download</a></code></p>
<p> yadifad<br />
 reads the zone files from yadifad.conf, and starts up an authoritative name server.<br />
 It listens to UDP and TCP DNS queries and returns answers from its own database. </p>
<p> yadifad<br />
 knows the main DNS protocols: </p>
<dl>
<dt><code>*</code></p>
<dd>AXFR </p>
<dt><code>*</code></p>
<dd>IXFR </p>
<dt><code>*</code></p>
<dd>DNSSEC </p>
<dt><code>*</code></p>
<dd>DNS Update </p>
<dt><code>*</code></p>
<dd>NOTIFY
</dl>
<p> yadifad<br />
 works only with 1 CLASS:</p>
<pre><br>
<br>
Class Value Definition<br>
IN 1 (Internet class)<br>
<br>
yadifad supports following TYPES:<br>
<br>
Type Value Defining RFC<br>
<br>
A 1 1035<br>
AAAA 28 3596<br>
CNAME 5 1035<br>
DNSKEY 48 4034<br>
DS 43 4034<br>
HINFO 12 1035<br>
MX 15 1035<br>
NAPTR 35 3403<br>
NS 2 1035<br>
NSEC 47 4034<br>
NSEC3 50 5155<br>
NSEC3PARAM 51 5155<br>
PTR 12 1035<br>
RRSIG 46 4034<br>
SOA 6 1035<br>
SRV 33 2782<br>
SSHFP 44 4255<br>
TLSA 52 6698<br>
TXT 16 1035<br>
<br>
Other tyes and pseudo resource records: <br>
<br>
* 255 1035<br>
AXFR 252 1035<br>
IXFR 251 1035<br>
OPT 41 6891<br>
<br>
<br></pre>
<h2>Options</h2>
<dl>
<dt>[<code>&#8211;config|-c</code><i> configfile</i>]</p>
<dd>
<dt>[<code>&#8211;daemon|-d</code>]</p>
<dd>
<dt>[<code>&#8211;uid|-u</code><i> uid</i>]</p>
<dd>
<dt>[<code>&#8211;gid|-g</code><i> gid</i>]</p>
<dd></dl>
<dl>
<dt>[<code>-V</code>]</p>
<dd>
<dt>[<code>&#8211;help|-h</code>]</p>
<dd></dl>
<h2>Signals</h2>
<dl>
<dt>SIGHUP</p>
<dd>reloads the zone and key sections in the configuration file and reloads the zone file(s) with incremented serial number, and close all log files and reopens them. </p>
<dt>SIGINT</p>
<dd>shuts down the server </p>
<dt>SIGTERM</p>
<dd>(see SIGINT)
</dl>
<h2>Files</h2>
<dl>
<dt>yadifad.conf</p>
<dd>configuration file. </p>
<dt>yadifad</p>
<dd>
<dt>yadifad.8</p>
<dd>
<dt>yadifad.conf.5</p>
<dd></dl>
<h2>See Also</h2>
<p> <i><a href="/docs/linux/man/5-yadifad-conf/">yadifad.conf</a></i>(5)</p>
<h2>Requirements</h2>
<dl>
<dt>OpenSSL</p>
<dd></center> yadifad requires OpenSSL version 0.9.8 or later.</dl>
<h2>Changes</h2>
<p>Please check the README file from the source code.</p>
<h2>Version</h2>
<p>Version: 2.2.3 of 2016-12-15.</p>
<h2>Mailing Lists</h2>
<p>There is a mailinglist for questions relating to any program in the yadifa package: </p>
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
<p> (this is a read-only list).</p>
<h2>License And Copyright</h2>
<dl>
<dt>Copyright</p>
<dd>(C) 2011-2016, EURid vzw/asbl<br />
 B-1831 Diegem, Belgium<br />
 <code>info [at] yadifa.eu</code></dl>
<h2>Authors</h2>
<p>Gery Van Emelen<br />
 Email: <code>Gery.VanEmelen [at] EURid.eu</code><br />
 Eric Diaz Fernandez<br />
 Email: <code>Eric.DiazFernandez [at] EURid.eu</code> </p>
<p> WWW: <code><a rel="nofollow" href="http://www.EURid.eu">http://www.EURid.eu</a></code></p>
