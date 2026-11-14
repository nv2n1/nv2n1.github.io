---
title: "boothd(8)"
name: "boothd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-boothd/"
description: "boothd – The Booth Cluster Ticket Manager."
---

<p>boothd &#8211; The Booth Cluster Ticket Manager.</p>
<h2>Synopsis</h2>
<p><code>boothd</code> <i>daemon</i> [-SD] [-c <i>config</i>] [-l <i>lockfile</i>] </p>
<p> <code>booth</code> <i>list</i> [-s <i>site</i>] [-c <i>config</i>] </p>
<p> <code>booth</code> <i>grant</i> [-s <i>site</i>] [-c <i>config</i>] [-FCw] <i>ticket</i> </p>
<p> <code>booth</code> <i>revoke</i> [-s <i>site</i>] [-c <i>config</i>] [-w] <i>ticket</i> </p>
<p> <code>booth</code> <i>peers</i> [-s <i>site</i>] [-c <i>config</i>] </p>
<p> <code>booth</code> <i>status</i> [-D] [-c <i>config</i>]</p>
<h2>Description</h2>
<p>Booth manages tickets which authorizes one of the cluster sites located in geographically dispersed distances to run certain resources. It is designed to be extend Pacemaker to support geographically distributed clustering. </p>
<p> It is based on the RAFT protocol, see eg. <a rel="nofollow" href="https://ramcloud.stanford.edu/wiki/download/attachments/11370504/raft.pdf">https://ramcloud.stanford.edu/wiki/download/attachments/11370504/raft.pdf</a> for details.</p>
<h2>Short Examples</h2>
<dl>
<dd>
<pre># boothd daemon -D
# booth list
# booth grant ticket-nfs
# booth revoke ticket-nfs</pre>
</dl>
<h2>Options</h2>
<p><code>-c</code> <i>configfile</i></p>
<dl>
<dd>Configuration to use. </p>
<p> Can be a full path to a configuration file, or a short name; in the latter case, the directory <i>/etc/booth</i> and suffix <i>.conf</i> are added. Per default <i>booth</i> is used, which results in the path <i>/etc/booth/booth.conf</i>. </p>
<p> The configuration name also determines the name of the PID file &#8211; for the defaults, <i>/var/run/booth/booth.pid</i>.</dl>
<p> <code>-s</code></p>
<dl>
<dd>Site address or name. </p>
<dl>
<dd>
<pre>The special value 'other' can be used to specify the other
site. Obviously, in that case, the booth configuration must
have exactly two sites defined.</pre>
</dl>
</dl>
<p> <code>-F</code></p>
<dl>
<dd><i>immediate grant</i>: Don&#8217;t wait for unreachable sites to relinquish the ticket. See the <i>Booth ticket management</i> section below for more details. </p>
<dl>
<dd>
<pre>This option may be DANGEROUS. It makes booth grant the ticket
even though it cannot ascertain that unreachable sites don't
hold the same ticket. It is up to the user to make sure that
unreachable sites don't have this ticket as granted.</pre>
</dl>
</dl>
<p> <code>-w</code></p>
<dl>
<dd><i>wait for the request outcome</i>: The client waits for the final outcome of grant or revoke request.</dl>
<p> <code>-C</code></p>
<dl>
<dd><i>wait for ticket commit to CIB</i>: The client waits for the ticket commit to CIB (only for grant requests). If one or more sites are unreachable, this takes the ticket expire time (plus, if defined, the <i>acquire-after</i> time).</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Give a short usage output.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Report version information.</dl>
<p> <code>-S</code></p>
<dl>
<dd><i>systemd</i> mode: don&#8217;t fork. This is like <i>-D</i> but without the debug output.</dl>
<p> <code>-D</code></p>
<dl>
<dd>Debug output/don&#8217;t daemonize. Increases the debug output level; booth daemon remains in the foreground.</dl>
<p> <code>-l</code> <i>lockfile</i></p>
<dl>
<dd>Use another lock file. By default, the lock file name is inferred from the configuration file name. Normally not needed.</dl>
<h2>Commands</h2>
<p>Whether the binary is called as <i>boothd</i> or <i>booth</i> doesn&#8217;t matter; the first argument determines the mode of operation. </p>
<p> <i>daemon</i></p>
<dl>
<dd>Tells <i>boothd</i> to serve a site. The locally configured interfaces are searched for an IP address that is defined in the configuration. booth then runs in either /arbitrator/ or /site/ mode.</dl>
<p> <i>client</i></p>
<dl>
<dd>Booth clients can list the ticket information (see also <i>crm_ticket -L</i>), and revoke or grant tickets to a site. </p>
<p> The grant and, under certain circumstances, revoke operations may take a while to return a definite operation&#8217;s outcome. The client will wait up to the network timeout value (by default 5 seconds) for the result. Unless the <i>-w</i> option was set, in which case the client waits indefinitely. </p>
<p> In this mode the configuration file is searched for an IP address that is locally reachable, ie. matches a configured subnet. This allows to run the client commands on another node in the same cluster, as long as the config file and the service IP is locally reachable. </p>
<p> For instance, if the booth service IP is 192.168.55.200, and the local node has 192.168.55.15 configured on one of its network interfaces, it knows which site it belongs to. </p>
<p> Use <i>-s</i> to direct client to connect to a different site.</dl>
<p> <i>status</i></p>
<dl>
<dd><i>boothd</i> looks for the (locked) PID file and the UDP socket, prints some output to stdout (for use in shell scripts) and returns an OCF-compatible return code. With <i>-D</i>, a human-readable message is printed to STDERR as well.</dl>
<p> <i>peers</i></p>
<dl>
<dd>List the other <i>boothd</i> servers we know about. </p>
<p> In addition to the type, name (IP address), and the last time the server was heard from, network statistics are also printed. The statistics are split into two rows, the first one consists of counters for the sent packets and the second one for the received packets. The first counter is the total number of packets and descriptions of the other counters follows:</dl>
<p> <i>resends</i></p>
<dl>
<dd>Packets which had to be resent because the recipient didn&#8217;t acknowledge a message. This usually means that either the message or the acknowledgement got lost. The number of resends usually reflect the network reliability.</dl>
<p> <i>error</i></p>
<dl>
<dd>Packets which either couldn&#8217;t be sent, got truncated, or were badly formed. Should be zero.</dl>
<p> <i>invalid</i></p>
<dl>
<dd>These packets contain either invalid or non-existing ticket name or refer to a non-existing ticket leader. Should be zero.</dl>
<p> <i>authfail</i></p>
<dl>
<dd>Packets which couldn&#8217;t be authenticated. Should be zero.</dl>
<h2>Configuration File</h2>
<p>The configuration file must be identical on all sites and arbitrators. </p>
<p> A minimal file may look like this: </p>
<dl>
<dd>
<pre>site=&quot;192.168.201.100&quot;
site=&quot;192.168.202.100&quot;
arbitrator=&quot;192.168.203.100&quot;
ticket=&quot;ticket-db8&quot;</pre>
</dl>
<p> Comments start with a hash-sign (<i>&#8216;#</i>&#8216;). Whitespace at the start and end of the line, and around the <i>&#8216;=</i>&#8216;, are ignored. </p>
<p> The following key/value pairs are defined: </p>
<p> <i>port</i></p>
<dl>
<dd>The UDP/TCP port to use. Default is <i>9929</i>.</dl>
<p> <i>transport</i></p>
<dl>
<dd>The transport protocol to use for Raft exchanges. Currently only UDP is supported. </p>
<p> Clients use TCP to communicate with a daemon; Booth will always bind and listen to both UDP and TCP ports.</dl>
<p> <i>authfile</i></p>
<dl>
<dd>File containing the authentication key. The key can be either binary or text. If the latter, then both leading and trailing white space, including new lines, is ignored. This key is a shared secret and used to authenticate both clients and servers. The key must be between 8 and 64 characters long and be readable only by the file owner.</dl>
<p> <i>maxtimeskew</i></p>
<dl>
<dd>As protection against replay attacks, packets contain generation timestamps. Such a timestamp is not allowed to be too old. Just how old can be specified with this parameter. The value is in seconds and the default is 600 (10 minutes). If clocks vary more than this default between sites and nodes (which is definitely something you should fix) then set this parameter to a higher value. The time skew test is performed only in concert with authentication.</dl>
<p> <i>site</i></p>
<dl>
<dd>Defines a site Raft member with the given IP. Sites can acquire tickets. The sites&#8217; IP should be managed by the cluster.</dl>
<p> <i>arbitrator</i></p>
<dl>
<dd>Defines an arbitrator Raft member with the given IP. Arbitrators help reach consensus in elections and cannot hold tickets.</dl>
<p> Booth needs at least three members for normal operation. Odd number of members provides more redundancy. </p>
<p> <i>site-user</i>, <i>site-group</i>, <i>arbitrator-user</i>, <i>arbitrator-group</i></p>
<dl>
<dd>These define the credentials <i>boothd</i> will be running with. </p>
<p> On a (Pacemaker) site the booth process will have to call <i>crm_ticket</i>, so the default is to use <i>hacluster</i>:&#8217;haclient&#8217;; for an arbitrator this user and group might not exists, so there we default to <i>nobody</i>:&#8217;nobody&#8217;.</dl>
<p> <i>ticket</i></p>
<dl>
<dd>Registers a ticket. Multiple tickets can be handled by single Booth instance. </p>
<p> Use the special ticket name <i>defaults</i> to modify the defaults. The <i>defaults</i> stanza must precede all the other ticket specifications.</dl>
<p> All times are in seconds. </p>
<p> <i>expire</i></p>
<dl>
<dd>The lease time for a ticket. After that time the ticket can be acquired by another site if the ticket holder is not reachable. </p>
<p> The default is <i>600</i>.</dl>
<p> <i>acquire-after</i></p>
<dl>
<dd>Once a ticket is lost, wait this time in addition before acquiring the ticket. </p>
<p> This is to allow for the site that lost the ticket to relinquish the resources, by either stopping them or fencing a node. </p>
<p> A typical delay might be 60 seconds, but ultimately it depends on the protected resources and the fencing configuration. </p>
<p> The default is <i>0</i>.</dl>
<p> <i>renewal-freq</i></p>
<dl>
<dd>Set the ticket renewal frequency period. </p>
<p> If the network reliability is often reduced over prolonged periods, it is advisable to try to renew more often. </p>
<p> Before every renewal, if defined, the command or commands specified in <i>before-acquire-handler</i> is run. In that case the <i>renewal-freq</i> parameter is effectively also the local cluster monitoring interval.</dl>
<p> <i>timeout</i></p>
<dl>
<dd>After that time <i>booth</i> will re-send packets if there was an insufficient number of replies. This should be long enough to allow packets to reach other members. </p>
<p> The default is <i>5</i>.</dl>
<p> <i>retries</i></p>
<dl>
<dd>Defines how many times to retry sending packets before giving up waiting for acks from other members. </p>
<p> Default is <i>10</i>. Values lower than 3 are illegal. </p>
<p> Ticket renewals should allow for this number of retries. Hence, the total retry time must be shorter than the renewal time (either half the expire time or <i>renewal-freq</i>): </p>
<dl>
<dd>
<pre>timeout*(retries+1) &lt; renewal</pre>
</dl>
</dl>
<p> <i>weights</i></p>
<dl>
<dd>A comma-separated list of integers that define the weight of individual Raft members, in the same order as the <i>site</i> and <i>arbitrator</i> lines. </p>
<p> Default is <i>0</i> for all; this means that the order in the configuration file defines priority for conflicting requests.</dl>
<p> <i>before-acquire-handler</i></p>
<dl>
<dd>If set, this parameter specifies either a file containing a program to be run or a directory where a number of programs can reside. They are invoked before <i>boothd</i> tries to acquire or renew a ticket. If any of them exits with a code other than 0, <i>boothd</i> relinquishes the ticket. </p>
<p> Thus it is possible to ensure whether the services and its dependencies protected by the ticket are in good shape at this site. For instance, if a service in the dependency-chain has a failcount of <i>INFINITY</i> on all available nodes, the service will be unable to run. In that case, it is of no use to claim the ticket. </p>
<p> One or more arguments may follow the program or directory location. Typically, there is at least the name of one of the resources which depend on this ticket. </p>
<p> See below for details about booth specific environment variables. The distributed <i>service-runnable</i> script is an example which may be used to test whether a pacemaker resource can be started.</dl>
<p> <i>attr-prereq</i></p>
<dl>
<dd>Sites can have GEO attributes managed with the <i><a href="/docs/linux/man/8-geostore/">geostore</a>(8)</i> program. Attributes are within ticket&#8217;s scope and may be tested by <i>boothd</i> for additional control of ticket failover (automatic) or ticket acquire (manual). </p>
<p> Attributes are typically used to convey extra information about resources, for instance database replication status. The attributes are commonly updated by resource agents. </p>
<p> Attribute values are referenced in expressions and may be tested for equality with the <i>eq</i> binary operator or inequality with the <i>ne</i> operator. The usage is as follows: </p>
<dl>
<dd>
<pre>attr-prereq = &lt;grant_type&gt; &lt;name&gt; &lt;op&gt; &lt;value&gt;</pre>
</dl>
<dl>
<dd>
<pre>&lt;grant_type&gt;: &quot;auto&quot; | &quot;manual&quot;
&lt;name&gt;: attribute name
&lt;op&gt;: &quot;eq&quot; | &quot;ne&quot;
&lt;value&gt;: attribute value</pre>
</dl>
<p> The two grant types are <i>auto</i> for ticket failover and <i>manual</i> for grants using the booth client. Only in case the expression evaluates to true can the ticket be granted. </p>
<p> It is not clear whether the <i>manual</i> grant type has any practical use because, obviously, this operation is anyway controlled by a human. </p>
<p> Note that there can be no guarantee on whether an attribute value is up to date, i.e. if it actually reflects the current state.</dl>
<p> One example of a booth configuration file: </p>
<dl>
<dd>
<pre>transport = udp
port = 9930
# D-85774
site=&quot;192.168.201.100&quot;
# D-90409
site=&quot;::ffff:192.168.202.100&quot;
# A-1120
arbitrator=&quot;192.168.203.100&quot;
ticket=&quot;ticket-db8&quot;
 expire = 600
 acquire-after = 60
 timeout = 10
 retries = 5
 renewal-freq = 60
 before-acquire-handler = /usr/share/booth/service-runnable db8
 attr-prereq = auto repl_state eq ACTIVE</pre>
</dl>
<h2>Booth Ticket Management</h2>
<p>The booth cluster guarantees that every ticket is owned by only one site at the time. </p>
<p> Tickets must be initially granted with the <i>booth client grant</i> command. Once it gets granted, the ticket is managed by the booth cluster. Hence, only granted tickets are managed by <i>booth</i>. </p>
<p> If the ticket gets lost, i.e. that the other members of the booth cluster do not hear from the ticket owner in a sufficiently long time, one of the remaining sites will acquire the ticket. This is what is called <i>ticket failover</i>. </p>
<p> If the remaining members cannot form a majority, then the ticket cannot fail over. </p>
<p> A ticket may be revoked at any time with the <i>booth client revoke</i> command. For revoke to succeed, the site holding the ticket must be reachable. </p>
<p> Once the ticket is administratively revoked, it is not managed by the booth cluster anymore. For the booth cluster to start managing the ticket again, it must be again granted to a site. </p>
<p> The grant operation, in case not all sites are reachable, may get delayed for the ticket expire time (and, if defined, the <i>acquire-after</i> time). The reason is that the other booth members may not know if the ticket is currently granted at the unreachable site. </p>
<p> This delay may be disabled with the <i>-F</i> option. In that case, it is up to the administrator to make sure that the unreachable site is not holding the ticket. </p>
<p> When the ticket is managed by <i>booth</i>, it is dangerous to modify it manually using either crm_ticket command or crm site ticket. Neither of these tools is aware of <i>booth</i> and, consequently, <i>booth</i> itself may not be aware of any ticket status changes. A notable exception is setting the ticket to standby which is typically done before a planned failover.</p>
<h2>Notes</h2>
<p>Tickets are not meant to be moved around quickly, the default <i>expire</i> time is 600 seconds (10 minutes). </p>
<p> <i>booth</i> works with both IPv4 and IPv6 addresses. </p>
<p> <i>booth</i> renews a ticket before it expires, to account for possible transmission delays. The renewal time, unless explicitly set, is set to half the <i>expire</i> time.</p>
<h2>Handlers</h2>
<p>Currently, there&#8217;s only one external handler defined (see the <i>before-acquire-handler</i> configuration item above). </p>
<p> The following environment variables are exported to the handler: </p>
<p> *<i>BOOTH_TICKET</i></p>
<dl>
<dd>The ticket name, as given in the configuration file. (See <i>ticket</i> item above.)</dl>
<p> *<i>BOOTH_LOCAL</i></p>
<dl>
<dd>The local site name, as defined in <i>site</i>.</dl>
<p> *<i>BOOTH_CONF_PATH</i></p>
<dl>
<dd>The path to the active configuration file.</dl>
<p> *<i>BOOTH_CONF_NAME</i></p>
<dl>
<dd>The configuration name, as used by the <i>-c</i> commandline argument.</dl>
<p> *<i>BOOTH_TICKET_EXPIRES</i></p>
<dl>
<dd>When the ticket expires (in seconds since 1.1.1970), or <i>0</i>.</dl>
<p> The handler is invoked with positional arguments specified after it.</p>
<h2>Files</h2>
<p><i>/etc/booth/booth.conf</i></p>
<dl>
<dd>The default configuration file name. See also the <i>-c</i> argument.</dl>
<p> <i>/etc/booth/authkey</i></p>
<dl>
<dd>There is no default, but this is a typical location for the shared secret (authentication key).</dl>
<p> <i>/var/run/booth/</i></p>
<dl>
<dd>Directory that holds PID/lock files. See also the <i>status</i> command.</dl>
<h2>Raft Implementation</h2>
<p>In essence, every ticket corresponds to a separate Raft cluster. </p>
<p> A ticket is granted to the Raft <i>Leader</i> which then owns (or keeps) the ticket.</p>
<h2>Arbitrator Management</h2>
<p>The booth daemon for an arbitrator which typically doesn&#8217;t run the cluster stack, may be started through systemd or with <i>/etc/init.d/booth-arbitrator</i>, depending on which init system the platform supports. </p>
<p> The SysV init script starts a booth arbitrator for every configuration file found in <i>/etc/booth</i>. </p>
<p> Platforms running systemd can enable and start every configuration separately using <i>systemctl</i>: </p>
<dl>
<dd>
<pre># systemctl enable booth@&lt;configurationname&gt;
# systemctl start booth@&lt;configurationname&gt;</pre>
</dl>
<p> <i>systemctl</i> requires the configuration name, even for the default name <i>booth</i>.</p>
<h2>Exit Status</h2>
<p><code>0</code></p>
<dl>
<dd>Success. For the <i>status</i> command: Daemon running.</dl>
<p> <code>1</code> (PCMK_OCF_UNKNOWN_ERROR)</p>
<dl>
<dd>General error code.</dl>
<p> <code>7</code> (PCMK_OCF_NOT_RUNNING)</p>
<dl>
<dd>No daemon process for that configuration active.</dl>
<h2>Bugs</h2>
<p>Booth is tested regularly. See the README-testing file for more information. </p>
<p> Please report any bugs either at GitHub: <a rel="nofollow" href="https://github.com/ClusterLabs/booth/issues">https://github.com/ClusterLabs/booth/issues</a> </p>
<p> Or, if you prefer bugzilla, at openSUSE bugzilla (component &quot;High Availability&quot;): <a rel="nofollow" href="https://bugzilla.opensuse.org/enter_bug.cgi?product=openSUSE%20Factory">https://bugzilla.opensuse.org/enter_bug.cgi?product=openSUSE%20Factory</a></p>
<h2>Author</h2>
<p><i>boothd</i> was originally written (mostly) by Jiaju Zhang. </p>
<p> In 2013 and 2014 Philipp Marek took over maintainership. </p>
<p> Since April 2014 it has been mainly developed by Dejan Muhamedagic. </p>
<p> Many people contributed (see the AUTHORS file).</p>
<h2>Resources</h2>
<p>GitHub: <a rel="nofollow" href="https://github.com/ClusterLabs/booth">https://github.com/ClusterLabs/booth</a> </p>
<p> Documentation: <a rel="nofollow" href="http://doc.opensuse.org/products/draft/SLE-HA/SLE-ha-guide_sd_draft/cha.ha.geo.html">http://doc.opensuse.org/products/draft/SLE-HA/SLE-ha-guide_sd_draft/cha.ha.geo.html</a></p>
<h2>Copying</h2>
<p>Copyright &#169; 2011 Jiaju Zhang &lt;jjzhang [at] suse.de&gt; </p>
<p> Copyright &#169; 2013-2014 Philipp Marek &lt;philipp.marek [at] linbit.com&gt; </p>
<p> Copyright &#169; 2014 Dejan Muhamedagic &lt;dmuhamedagic [at] suse.com&gt; </p>
<p> Free use of this software is granted under the terms of the GNU General Public License (GPL) as of version 2 (see COPYING file) or later.</p>
