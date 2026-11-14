---
title: "ypxfr(8)"
name: "ypxfr"
section: "8"
letter: "y"
url: "/docs/linux/man/8-ypxfr/"
description: "ypxfr – transfer NIS database from remote server to local host"
---

<p>ypxfr &#8211; transfer NIS database from remote server to local host</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/lib/yp/ypxfr</code> [-f] [-c] [-d&nbsp;<wbr><i>target</i>&nbsp;<wbr><i>domain</i>] [-h&nbsp;<wbr><i>source</i>&nbsp;<wbr><i>host</i>] [-s&nbsp;<wbr><i>source</i>&nbsp;<wbr><i>domain</i>] [-C&nbsp;<wbr><i>taskid</i>&nbsp;<wbr><i>program-number</i>&nbsp;<wbr><i>ipaddr</i>&nbsp;<wbr><i>port</i>] [-p&nbsp;<wbr><i>yp_path</i>] <i>mapname</i>&#8230;</p>
<dd>
<h2>Description</h2>
<p><code>ypxfr</code></p>
<dd>copies an NIS database from one NIS server to the local host by using the NIS service. <code>ypxfr</code> is generally invoked by <code>ypinit</code> or by <code>ypserv,</code> when <code>ypserv</code> receives a map transfer request from <code>yppush.</code> It creates a temporary map in the directory FC/var/yp/domainF[] (this directory must already exist; <i>domain</i> is the default domainname for the local host), fills it by getting the map&#8217;s entries and fetches the map parameters (master and order number). If the transfer was successful, the old version of the map will be deleted and the temporary copy will be moved into its place. Then, <code>ypxfr</code> will attempt to send a &quot;clear current map&quot; request to the local <code>ypserv.</code> </p>
<p> If run interactively, <code>ypxfr</code> writes its output to stderr. However, if it is invoked without a controlling terminal, it will log the output to syslog. </p>
<p> <code>ypxfr</code> is used primarily in environments where several NIS servers are in use. For all maps, you have a NIS master server, which maintains a canonical copy of the NIS map, and all the other servers, the NIS slaves, copy the new version of the map from the master whenever a update was made. Normally, you have one NIS master for all maps. </p>
<p> In order to maintain consistency across all NIS servers, <code>ypxfr</code> can be run periodically in a <code>cron</code> job. Maps which change infrequently need only be updated once a day (preferably late at night when system usage is lowest), where those with frequent changes (such as <i>passwd.byname</i> and <i>passwd.byuid )</i> should be updated perhaps once every hour. Examples are in FC/usr/lib/yp: ypxfr_1perday, ypxfr_2perday,F[] and <code>ypxfr_1perhour.</code> They can serve as reasonable first cuts. </p>
<p> Normally all updates should be propagated by <code>yppush</code> when FC/var/yp/MakefileF[] is run on the NIS master server, however it is a good practice on large networks where possible outages could cause NIS slaves to fall out of sync with the master.</p>
<h2>Options</h2>
<p>The following options are supported: </p>
<p> <code>-f</code></p>
<dl>
<dd>Force a map transfer. Normally, <code>ypxfr</code> will not transfer a map if it determines that the NIS master&#8217;s copy is not newer than the existing copy already on the local host. This flag forces a transfer regardless of which server&#8217;s version is more recent.</dl>
<p> <code>-c</code></p>
<dl>
<dd>Do not send a &quot;clear current map&quot; request to the <code>ypserv</code> process running on the local host. This flag is normally used when invoking <code>ypxfr</code> by <code>ypinit</code> or if <code>ypserv</code> is not running locally at the time you are running <code>ypxfr.</code> Otherwise, <code>ypxfr</code> will complain that it cannot talk to the local <code>ypserv,</code> and the transfer will fail.</dl>
<p> <code>-d</code><i> domain</i></p>
<dl>
<dd>Specify a domain other than the default NIS domain.</dl>
<p> <code>-h</code><i> source host</i></p>
<dl>
<dd>Get the map from <i>host</i>, regardless of what the map says the master is. If <i>host</i> is not specified, <code>ypxfr</code> asks the NIS service for the name of the master, and tries to get the map from there. This option is used to insure that ypxfr only copies maps from the NIS master server.</dl>
<p> <code>-s</code><i> source domain</i></p>
<dl>
<dd>Specify a source domain from which to transfer a map that should be the same across domains.</dl>
<p> <code>-C</code><i> taskid progam-number ipaddr port</i></p>
<dl>
<dd>This option is <code>only</code> for use by <code>ypserv .</code> When <code>ypserv</code> invokes <code>ypxfr</code>, it specifies that <code>ypxfr</code> should call back a <code>yppush</code> process at the host with IP address <i>ipaddr</i>, registered as program number <i>progam-number</i>, listening on port <i>port</i>, and waiting for a response to transaction <i>taskid</i>.</dl>
<p> <code>-p</code><i> yp_path</i></p>
<dl>
<dd>Change the directory for the maps to <i>yp_path/[domainname]/</i>, the default is FC/var/yp/[domainname]F[].</dl>
<p> <i>mapname</i></p>
<dl>
<dd>One or more names of the map to transfer.</dl>
<h2>Files</h2>
<p>/var/yp/[domainname]/[maps]</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-yppush/">yppush</a></code>(8), <code><a href="/docs/linux/man/8-ypinit/">ypinit</a></code>(8), <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8), <code><a href="/docs/linux/man/5-crontab/">crontab</a></code>(5)</p>
<h2>Author</h2>
<p>Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;</p>
