---
title: "rpcinfo(8)"
name: "rpcinfo"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpcinfo/"
description: "rpcinfo – report RPC information"
---

<p><code>rpcinfo</code> &#8211; report RPC information</p>
<h2>Synopsis</h2>
<p><code>rpcinfo</code> [-<code>m | -s</code> ] [<i>host</i> ]<br />
<code>rpcinfo</code> &#8211;<code>p </code>[<i>host</i> ]<br />
<code>rpcinfo</code> &#8211;<code>T </code><i>transport</i> <i>host prognum</i> [<i>versnum</i> ]<br />
<code>rpcinfo</code> &#8211;<code>l</code> [-<code>T </code><i>transport</i> ] <i>host prognum versnum</i><br />
<code>rpcinfo</code> [-<code>n </code><i>portnum</i> ] &#8211;<code>u</code> <i>host prognum</i> [<i>versnum</i> ]<br />
<code>rpcinfo</code> [-<code>n </code><i>portnum</i> ] [-<code>t</code> ] <i>host prognum</i> [<i>versnum</i> ]<br />
<code>rpcinfo</code> &#8211;<code>a </code><i>serv_address</i> &#8211;<code>T </code><i>transport</i> <i>prognum</i> [<i>versnum</i> ]<br />
<code>rpcinfo</code> &#8211;<code>b</code> [-<code>T </code><i>transport</i> ] <i>prognum versnum</i><br />
<code>rpcinfo</code> &#8211;<code>d</code> [-<code>T </code><i>transport</i> ] <i>prognum versnum</i></p>
<h2>Description</h2>
<p><code>rpcinfo</code> makes an RPC call to an RPC server and reports what it finds. </p>
<p> In the first synopsis, <code>rpcinfo</code> lists all the registered RPC services with <code>rpcbind</code> on <i>host</i> If <i>host</i> is not specified, the local host is the default. If &#8211;<code>s</code> is used, the information is displayed in a concise format. </p>
<p> In the second synopsis, <code>rpcinfo</code> lists all the RPC services registered with <code>rpcbind</code> version 2. Also note that the format of the information is different in the first and the second synopsis. This is because the second synopsis is an older protocol used to collect the information displayed (version 2 of the <code>rpcbind</code> protocol). </p>
<p> The third synopsis makes an RPC call to procedure 0 of <i>prognum</i> and <i>versnum</i> on the specified <i>host</i> and reports whether a response was received. <i>transport</i> is the transport which has to be used for contacting the given service. The remote address of the service is obtained by making a call to the remote <code>rpcbind</code> </p>
<p> The <i>prognum</i> argument is a number that represents an RPC program number. If a <i>versnum</i> is specified, <code>rpcinfo</code> attempts to call that version of the specified <i>prognum</i> Otherwise, <code>rpcinfo</code> attempts to find all the registered version numbers for the specified <i>prognum</i> by calling version 0, which is presumed not to exist; if it does exist, <code>rpcinfo</code> attempts to obtain this information by calling an extremely high version number instead, and attempts to call each registered version. Note: the version number is required for &#8211;<code>b</code> and &#8211;<code>d</code> options.</p>
<h2>Options</h2>
<dl>
<dt><code>-T </code><i>transport</i></p>
<dd>Specify the transport on which the service is required. If this option is not specified, <code>rpcinfo</code> uses the transport specified in the <code>NETPATH</code> environment variable, or if that is unset or null, the transport in the <a href="/docs/linux/man/5-netconfig/">netconfig</a>(5) database is used. This is a generic option, and can be used in conjunction with other options as shown in the SYNOPSIS. </p>
<dt><code>-a </code><i>serv_address</i></p>
<dd>Use <i>serv_address</i> as the (universal) address for the service on <i>transport</i> to ping procedure 0 of the specified <i>prognum</i> and report whether a response was received. The &#8211;<code>T</code> option is required with the &#8211;<code>a</code> option. </p>
<p> If <i>versnum</i> is not specified, <code>rpcinfo</code> tries to ping all available version numbers for that program number. This option avoids calls to remote <code>rpcbind</code> to find the address of the service. The <i>serv_address</i> is specified in universal address format of the given transport. </p>
<dt><code>-b</code></p>
<dd>Make an RPC broadcast to procedure 0 of the specified <i>prognum</i> and <i>versnum</i> and report all hosts that respond. If <i>transport</i> is specified, it broadcasts its request only on the specified transport. If broadcasting is not supported by any transport, an error message is printed. Use of broadcasting should be limited because of the potential for adverse effect on other systems. </p>
<dt><code>-d</code></p>
<dd>Delete registration for the RPC service of the specified <i>prognum</i> and <i>versnum</i> If <i>transport</i> is specified, unregister the service on only that transport, otherwise unregister the service on all the transports on which it was registered. Only the owner of a service can delete a registration, except the super-user who can delete any service. </p>
<dt><code>-l</code></p>
<dd>Display a list of entries with a given <i>prognum</i> and <i>versnum</i> on the specified <i>host</i> Entries are returned for all transports in the same protocol family as that used to contact the remote <code>rpcbind</code> </p>
<dt><code>-m</code></p>
<dd>Display a table of statistics of <code>rpcbind</code> operations on the given <i>host</i> The table shows statistics for each version of <code>rpcbind</code> (versions 2, 3 and 4), giving the number of times each procedure was requested and successfully serviced, the number and type of remote call requests that were made, and information about RPC address lookups that were handled. This is useful for monitoring RPC activities on <i>host</i> </p>
<dt><code>-n </code><i>portnum</i></p>
<dd>Use <i>portnum</i> as the port number for the &#8211;<code>t</code> and &#8211;<code>u</code> options instead of the port number given by <code>rpcbind</code> Use of this option avoids a call to the remote <code>rpcbind</code> to find out the address of the service. This option is made obsolete by the &#8211;<code>a</code> option. </p>
<dt><code>-p</code></p>
<dd>Probe <code>rpcbind</code> on <i>host</i> using version 2 of the <code>rpcbind</code> protocol, and display a list of all registered RPC programs. If <i>host</i> is not specified, it defaults to the local host. Note: Version 2 of the <code>rpcbind</code> protocol was previously known as the portmapper protocol. </p>
<dt><code>-s</code></p>
<dd>Display a concise list of all registered RPC programs on <i>host</i> If <i>host</i> is not specified, it defaults to the local host. </p>
<dt><code>-t</code></p>
<dd>Make an RPC call to procedure 0 of <i>prognum</i> on the specified <i>host</i> using TCP, and report whether a response was received. This option is made obsolete by the &#8211;<code>T</code> option as shown in the third synopsis. </p>
<dt><code>-u</code></p>
<dd>Make an RPC call to procedure 0 of <i>prognum</i> on the specified <i>host</i> using UDP, and report whether a response was received. This option is made obsolete by the &#8211;<code>T</code> option as shown in the third synopsis.</dl>
<h2>Examples</h2>
<p>To show all of the RPC services registered on the local machine use: </p>
<pre> example% rpcinfo</pre>
<p>To show all of the RPC services registered with <code>rpcbind</code> on the machine named <code>klaxon</code> use: </p>
<pre> example% rpcinfo klaxon</pre>
<p>The information displayed by the above commands can be quite lengthy. Use the &#8211;<code>s</code> option to display a more concise list: </p>
<pre> example$ rpcinfo -s klaxon</pre>
<dl>
<dt><code>program Ta </code>version(s) Ta netid(s) Ta service Ta owner</p>
<dd>
<dt><code>100000 Ta </code>2,3,4 Ta local,tcp,udp,tcp6,udp6 Ta rpcbind Ta super-user</p>
<dd>
<dt><code>100008 Ta </code>1 Ta udp,tcp,udp6,tcp6 Ta walld Ta super-user</p>
<dd>
<dt><code>100002 Ta </code>2,1 Ta udp,udp6 Ta rusersd Ta super-user</p>
<dd>
<dt><code>100001 Ta </code>2,3,4 Ta udp,udp6 Ta rstatd Ta super-user</p>
<dd>
<dt><code>100012 Ta </code>1 Ta udp,tcp Ta sprayd Ta super-user</p>
<dd>
<dt><code>100007 Ta </code>3 Ta udp,tcp Ta ypbind Ta super-user</p>
<dd></dl>
<p> To show whether the RPC service with program number <i>prognum</i> and version <i>versnum</i> is registered on the machine named <code>klaxon</code> for the transport TCP use: </p>
<pre> example% rpcinfo -T tcp klaxon prognum versnum</pre>
<p>To show all RPC services registered with version 2 of the <code>rpcbind</code> protocol on the local machine use: </p>
<pre> example% rpcinfo -p</pre>
<p>To delete the registration for version 1 of the <code>walld</code> (program number 100008 ) service for all transports use: </p>
<pre> example# rpcinfo -d 100008 1</pre>
<p>or </p>
<pre> example# rpcinfo -d walld 1</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-rpc/">rpc</a>(3), <a href="/docs/linux/man/5-netconfig/">netconfig</a>(5), <a href="/docs/linux/man/5-rpc/">rpc</a>(5), <a href="/docs/linux/man/8-rpcbind/">rpcbind</a>(8) </p>
