---
title: "inadyn(8)"
name: "inadyn"
section: "8"
letter: "i"
url: "/docs/linux/man/8-inadyn/"
description: "inadyn – a client for open DNS servers."
---

<p>inadyn &#8211; a client for open DNS servers.</p>
<h2>Synopsis</h2>
<p><code>inadyn</code> [-h | &#8211;help] [-u | &#8211;username <i>username</i> ] [-p | &#8212; password <i>password</i> ] [-a | &#8211;alias[,hash] <i>alias,hash</i> [-a | &#8211;alias[,hash] <i>another_alias,the_other_hash </i> &nbsp;<wbr>&#8230; ]] [&#8211;input_file <i>path/name</i> ] [&#8211;ip_server_name <i>server[:port] url</i> ] [&#8211;dyndns_server_name[:port] <i>server[:port]</i> ] [&#8211;dyndns_system <i>service</i> ] [&#8211;proxy_server[:port] <i>proxy[:port]</i> ] [&#8211;update_period <i>ms</i> ] [&#8211;update_period_sec <i>sec</i> ] [&#8211;forced_update_period <i>sec</i> ] [&#8211;log_file <i>path/name</i> ] [&#8211;background] [&#8211;verbose <i>level</i> ] [&#8211;iterations <i>iterations</i> ] [&#8211;syslog] ] [&#8211;change_persona <i>uid[:gid]</i> ]</p>
<h2>Description</h2>
<p><code>inadyn</code> is a client for `open&#8217; name servers. That is, it let the user have an Internet recognized name for his machine by transferring to him some control over a name server that he does not manage. Some of the services that are offered by those open name servers are free of charge, and work even when the client machine does not have a static IP. The name servers that are supported by <code>inayn</code> are: <a rel="nofollow" href="http://www.dyndns.org">http://www.dyndns.org</a> and <a rel="nofollow" href="http://freedns.afraid.org">http://freedns.afraid.org</a> Its basic operation is to periodically check whether the actual IP of the client machine is the same one that is recorded in the name server, and update the name server records when there is a mismatch.</p>
<h3>Options</h3>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>Print a summary of the options to <code>inadyn</code> and exit.</p>
<dt><i>-u, &#8211;username</i></p>
<dd>The username, if applicable. This might be referred to as hash.</p>
<dt><i>-p, &#8211;password</i></p>
<dd>The password, if applicable.</p>
<dt><i>-a, &#8211;alias[,hash]</i></p>
<dd>A host name alias. This option can appear multiple times, for each domain that has the same IP.</p>
<dt><i>&#8211;input_file</i></p>
<dd>The file name that contains inadyn command options exactly as specified in the command line syntax (adds to those already present in the cmd line). The default configuration file name is &#8216;/etc/inadyn.conf&#8217;. It is looked at automatically if <code>inadyn</code> is called without any command line options. The format is as expected for a **NIX config the hash character is used to comment entire lines. Spaces are ingored. The long options may be specified without &#8212; if placed at the beginning of the line.</p>
<dt><i>&#8211;ip_server_name[:port] url</i></p>
<dd>The client IP is detected by calling &#8216;url&#8217; from this &#8216;ip_server_name:port&#8217;. Defaults to checkip.dyndns.org:80 /.</p>
<dt><i>&#8211;dyndns_server_name[:port]</i></p>
<dd>The server that receives the update DNS requests. When no proxy is specified it is sufficient to set the dyndns_system so that the default servers will be taken. The option is useful for generic DynDNS services that support HTTP update.</p>
<dt><i>&#8211;dyndns_server_url name</i></p>
<dd>The update path inside the DynDNS server.</p>
<dt><i>&#8211;dyndns_system</i></p>
<dd>An optional DNS service. For <a rel="nofollow" href="http://www.dyndns.org">http://www.dyndns.org</a> the acceptable services are one of dyndns [at] dyndns.org, statdns [at] dyndns.org or custom [at] dyndns.org. There is only one acceptable service for <a rel="nofollow" href="http://freedns.afraid.org">http://freedns.afraid.org</a> , which is default [at] freedns.afraid.org. Other services are: default [at] zoneedit.com, custom [at] http_svr_basic_auth. The default service is dyndns [at] dyndns.org, which is believed to be used by most users, at least initially.</p>
<dt><i>&#8211;proxy_server[:port]</i></p>
<dd>An http proxy server name and port. The default is none.</p>
<dt><i>&#8211;update_period</i></p>
<dd>How often the IP is checked. This value denotes millisecond (There are 1000 milliseconds in one second). The default is about 1 minute. The maximum is 10 days.</p>
<dt><i>&#8211;update_period_sec</i></p>
<dd>How often the IP is checked. Here the value denotes seconds. The default is about 1 minute. The maximum value is 10 days.</p>
<dt><i>&#8211;forced_update_period</i></p>
<dd>How often the IP should be updated even if it is not changed. The time should be given in seconds.</p>
<dt><i>&#8211;log_file</i></p>
<dd>The name, including the full path, of a log file.</p>
<dt><i>&#8211;background</i></p>
<dd>run in background. Output is sent to the UNIX syslog facilities or to a log file, if one was specified.</p>
<dt><i>&#8211;verbose</i></p>
<dd>Set the debug level, which is an integer between 0 to 5.</p>
<dt><i>&#8211;iterations</i></p>
<dd>Set the number of DNS updates. The default is 0, which means infinity.</p>
<dt><i>&#8211;syslog</i></p>
<dd>Explicitly sending the output to a syslog like file, such as /var/log/messages.</p>
<dt><i>&#8211;change_persona uid[:gid]</i></p>
<dd>After init changes user ID and group ID to the provided ones. This allows dropping unneeded [root] privileges after startup. </p>
<h2>Typical Usage</h2>
<h3></h3>
<p><a rel="nofollow" href="http://www.dyndns.org">http://www.dyndns.org</a></p>
<dl>
<dt><code>inadyn</code></p>
<dd>&nbsp;<wbr>-u username -p password -a my.registered.name</p>
<dt><code>inadyn</code></p>
<dd>&#8211;username test &#8211;password test &#8211;update_period 60000 &#8211;alias test.homeip.net &#8211;alias my.second.domain</p>
<dt><code>inadyn</code></p>
<dd>&#8211;background -u test -p test &#8211;update_period 60000 &#8211;alias inarcis.homeip.net &#8211;alias my.second.domain &#8211;log_file inadyn_srv.log</dl>
<h3></h3>
<p><a rel="nofollow" href="http://freedns.afraid.org">http://freedns.afraid.org</a></p>
<dl>
<dt><code>inadyn</code></p>
<dd>&#8211;dyndns_service default [at] freedns.afraid.org -a my.registrated.name,hash_from_freedns</p>
<dt><code>inadyn</code></p>
<dd>&#8211;update_period 60000 &#8211;alias test.homeip.net,hash_for_host1 -a my.second.domain,hash2 &#8211;dyndns_system default [at] freedns.afraid.org</dl>
<p> The &#8216;hash&#8217; should be extracted from the grab url batch file that can be downloaded from the site. A single hashed (base64 encoded) string is preferred upon a username and password pair, apparently to reduce the computational resources that is required on their side. Unfortunately the hash can not be computed by inadyn because it requires the index to the username record in the freedns database, which is not known. The simplest solution seems to be a copy&amp;paste action from the grab url batch file offered on their website. When the batch file looks is like </p>
<p> graburl <a rel="nofollow" href="http://freedns.afraid.org/dynamic/update.php?YUGIUGSEIUFGOUIHEOIFEOIHJFEIO=">http://freedns.afraid.org/dynamic/update.php?YUGIUGSEIUFGOUIHEOIFEOIHJFEIO=</a> </p>
<p> the hash string, which is what the user should copy and paste, is the string that begins right after the &#8216;?&#8217; character and ends with the end of line. This string shell be used as the username in inadyn command. When the user has several names then each name should be followed with that name hash string.</p>
<h2>Output</h2>
<p><code>inadyn</code> prints a message when the IP is updated. If no update is needed then by default it prints a single &#8216;.&#8217; character, unless &#8211;verbose is set to 0. Therefore, unless &#8211;verbose is set to 0, the log file will contains lot of dots. When the connection goes down it could be that <code>inadyn</code> will print some error messages. Those are harmless and should be followed by &#8216;OK&#8217; messages after the connection is back up.</p>
<h2>Signals</h2>
<p>Any of the SIG_HUP, SIG_INT, SIG_QUIT will cause inadyn to terminate gracefully.</p>
<h2>See Also</h2>
<h3>Other manual pages</h3>
<p>The syntax of the optional configuration file is given by <code><a href="/docs/linux/man/5-inadyn-conf/">inadyn.conf</a>(5).</code></p>
<h3>Internet resources</h3>
<p><code>Inadyn</code> &#8216;s home page is <a rel="nofollow" href="http://inadyn.ina-tech.net.">http://inadyn.ina-tech.net.</a></p>
<h2>Author</h2>
<p><code>inadyn</code> was written by Narcis Ilisei, &lt;inarcis2002 [at] hotpop.com&gt;. </p>
<p> This manual page was written by Shaul Karl, &lt;shaul [at] debian.org&gt;, for the <code>Debian GNU/Linux</code> system, based on the readme.html file that is found in the source.</p>
