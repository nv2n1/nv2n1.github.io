---
title: "rec_control(1)"
name: "rec_control"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rec_control/"
description: "rec_control – control pdns_recursor"
---

<h2>NAME</h2>
<p> rec_control &#8211; control pdns_recursor</p>
<h2>SYNOPSIS</h2>
<p> rec_control [OPTION]&#8230; COMMAND [COMMAND-OPTION]&#8230;</p>
<h3>DESCRIPTION</h3>
<p> <a href="/docs/linux/man/1-rec_control/">rec_control</a>(1) allows the operator to control a running instance of the pdns_recursor. </p>
<p> The commands that can be passed to the recursor are described on <a rel="nofollow" href="http://doc.powerdns.com/md/recursor/running/#rec_control-commands">http://doc.powerdns.com/md/recursor/running/#rec_control-commands</a></p>
<h2>EXAMPLES</h2>
<p> To stop the recursor by hand, run: </p>
<p> #&nbsp;<wbr>rec_control quit </p>
<p> To dump the cache to disk, execute: </p>
<p> #&nbsp;<wbr>rec_control dump-cache&nbsp;<wbr>/tmp/the-cache</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> provide this helpful message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;socket-dir=</code>PATH</p>
<dd> Where the controlsocket will live.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;socket-pid=</code>PID</p>
<dd> When running in SMP mode, pid of pdns_recursor to control.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;timeout=</code>NUM</p>
<dd> Number of seconds to wait for the remote PowerDNS Recursor to respond. Set to 0 for infinite.</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>current-queries</code></p>
<dd> Shows the currently active queries.</p>
<dl>
<dt>
<dd></dl>
<dt><code>dump-cache </code>FILENAME</p>
<dd> Dumps the entire cache to FILENAME. This file should not exist already, PowerDNS will refuse to overwrite it. While dumping, the recursor will not answer questions.</p>
<dl>
<dt>
<dd></dl>
<dt><code>dump-edns </code>FILENAME</p>
<dd> Dumps the EDNS status to the filename mentioned. This file should not exist already, PowerDNS will refuse to overwrite it. While dumping, the recursor will not answer questions.</p>
<dl>
<dt>
<dd></dl>
<dt><code>dump-nsspeeds </code>FILENAME</p>
<dd> Dumps the nameserver speed statistics to the FILENAME mentioned. This file should not exist already, PowerDNS will refuse to overwrite it. While dumping, the recursor will not answer questions.</p>
<dl>
<dt>
<dd></dl>
<dt><code>get </code>STATISTIC [STATISTIC]&#8230;</p>
<dd> Retrieve a statistic. For items that can be queried, see <a rel="nofollow" href="http://doc.powerdns.com/md/recursor/stats/">http://doc.powerdns.com/md/recursor/stats/</a></p>
<dl>
<dt>
<dd></dl>
<dt><code>get-all</code></p>
<dd> Retrieve all known statistics.</p>
<dl>
<dt>
<dd></dl>
<dt><code>get-parameter </code>KEY [KEY]&#8230;</p>
<dd> Retrieves the specified configuration parameter(s).</p>
<dl>
<dt>
<dd></dl>
<dt><code>get-qtypelist</code></p>
<dd> Retrieves QType statistics. Queries from cache aren&#8217;t being counted yet.</p>
<dl>
<dt>
<dd></dl>
<dt><code>help</code></p>
<dd> Shows a list of supported commands.</p>
<dl>
<dt>
<dd></dl>
<dt><code>ping</code></p>
<dd> Check if server is alive.</p>
<dl>
<dt>
<dd></dl>
<dt><code>quit</code></p>
<dd> Request shutdown of the recursor.</p>
<dl>
<dt>
<dd></dl>
<dt><code>quit-nicely</code></p>
<dd> Request nice shutdown of the recursor.</p>
<dl>
<dt>
<dd></dl>
<dt><code>reload-acls</code></p>
<dd> Reloads ACLs.</p>
<dl>
<dt>
<dd></dl>
<dt><code>reload-lua-script </code>FILENAME</p>
<dd> (Re)loads Lua script FILENAME.</p>
<dl>
<dt>
<dd></dl>
<dt><code>reload-zones</code></p>
<dd> Reload authoritative and forward zones. Retains current configuration in case of errors.</p>
<dl>
<dt>
<dd></dl>
<dt><code>set-minimum-ttl </code>NUM</p>
<dd> Set minimum-ttl-override to NUM.</p>
<dl>
<dt>
<dd></dl>
<dt><code>top-remotes</code></p>
<dd> Shows the top-20 most active remote hosts. Statistics are over the last &#8216;remotes-ringbuffer-entries&#8217; queries, which defaults to 0.</p>
<dl>
<dt>
<dd></dl>
<dt><code>trace-regex </code>REGEX</p>
<dd> Emit resolution trace for matching queries. Empty regex to disable trace.</p>
<dl>
<dt>
<dd></dl>
<dt><code>unload-lua-script</code></p>
<dd> Unloads Lua script.</p>
<dl>
<dt>
<dd></dl>
<dt><code>version</code></p>
<dd> Report running version.</p>
<dl>
<dt>
<dd></dl>
<dt><code>wipe-cache </code>DOMAIN [DOMAIN] [&#8230;]</p>
<dd> Wipe entries for DOMAIN from the cache. This is useful if, for example, an important server has a new IP address, but the TTL has not yet expired. Multiple domain names can be passed. Note that you must terminate a domain with a .! So to wipe powerdns.org, issue &#8216;rec_control wipe-cache powerdns.org.&#8217;. Versions beyond 3.1 don&#8217;t need the trailing dot. Consider not only wiping &#8216;<a rel="nofollow" href="http://www.domain.com">www.domain.com</a>.&#8217; but also &#8216;domain.com.&#8217;, as the cached nameservers or target of CNAME may continue to be undesired.</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>BUGS</h2>
<p> None known. File new ones at <a rel="nofollow" href="https://github.com/PowerDNS/pdns/issues.">https://github.com/PowerDNS/pdns/issues.</a></p>
<h2>RESOURCES</h2>
<p> Website: <a rel="nofollow" href="http://wiki.powerdns.com,">http://wiki.powerdns.com,</a> <a href="http://www.powerdns.com">http://www.powerdns.com</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pdns_recursor/">pdns_recursor</a>(1)</p>
<h2>AUTHORS</h2>
<p> PowerDNS.COM BV. </p>
<h2>Index</h2>
