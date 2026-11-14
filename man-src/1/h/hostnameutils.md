---
title: "hostnameutils(1)"
name: "hostnameutils"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hostnameutils/"
description: "gethostname, gethostbyname, gethostbyaddr, getservbyname – get local host information"
---

<h2 class="name">NAME</h2>
<p> gethostname, gethostbyname, gethostbyaddr, getservbyname &#8211; get local host information</p>
<h2>SYNTAX</h2>
<p> <code>$SGE_ROOT/utilbin/$ARCH/gethostname&nbsp;</code>[<code>-help</code>|<code>-name</code>|<code>-aname</code>|<code>-all</code>] </p>
<p> <code>$SGE_ROOT/utilbin/$ARCH/gethostbyname&nbsp;</code>[<code>-help</code>|<code>-name</code>|<code>-aname</code>|<code>-all</code>] <i>name</i> </p>
<p> <code>$SGE_ROOT/utilbin/$ARCH/gethostbyaddr&nbsp;</code>[<code>-help</code>|<code>-name</code>|<code>-aname</code>|<code>-all</code>] <i>ip</i> </p>
<p> <code>$SGE_ROOT/utilbin/$ARCH/getservbyname&nbsp;</code>[<code>-help</code>|<code>-number</code>] <i>service</i> </p>
<h2>DESCRIPTION</h2>
<p> <i>gethostname</i> and <i>gethostbyname</i> are used to get the local resolved host name. <i>gethostbyaddr</i> is used to get the hostname of a specified IP address (dotted decimal notation). <i>getservbyname</i> can be used to get the configured port number of a service (e.g. from /etc/services). </p>
<p> The hostname utils are primarily used by the xxQS_NAMExx installation scripts. <i>gethostname</i> , <i>gethostbyname</i> and <i>gethostbyaddr</i> called without any option will print out the hostname, all specified aliases, and the IP address of the locally resolved hostname. Calling <i>getservbyname</i> without any option will print out the full service entry. </p>
<h2>OPTIONS</h2>
<h3><code>-help</code></h3>
<p> Prints a list of all options.</p>
<h3><code>-name</code></h3>
<p> This option only reports the primary name of the host.</p>
<h3><code>-aname</code></h3>
<p> If this option is set, the xxQS_NAMExx host alias file is used for host name resolving. It is necessary to set the environment variable xxQS_NAME_Sxx_ROOT and, if more than one cell is defined, also xxQS_NAME_Sxx_CELL. </p>
<p> This option will print out the xxQS_NAMExx host name.</p>
<h3><code>-all</code></h3>
<p> By using the <code>-all</code> option all available host information will be printed. This information includes the host name, the xxQS_NAMExx host name, all host aliases, and the IP address of the host.</p>
<h3><code>-number</code></h3>
<p> This option will print out the port number of the specified service name.</p>
<h3><code>&lt;name&gt;</code></h3>
<p> The host name for which the information is requested.</p>
<h3><code>&lt;ip&gt;</code></h3>
<p> The IP address (dotted decimal notation) for which the information is requested.</p>
<h3><code>&lt;service&gt;</code></h3>
<p> The service name for which the information is requested (e.g. ftp, sge_qmaster or sge_execd).</p>
<h2>EXAMPLES</h2>
<p> The following example shows how to get the port number of the FTP service: </p>
<dl>
<dt>
<dd>
<pre>
&gt;/opt/sge/default/lx-amd64/getservbyname -number ftp
21
</pre>
</dl>
<p> The next example shows the output of <code>gethostname -all</code> when the host alias file contains this line: </p>
<p> gridmaster extern_name extern_name.mydomain </p>
<p> The local host resolving must also provide the alias name &quot;gridmaster&quot;. Each xxQS_NAMExx host that wants to use the cluster must be able to resolve the host name &quot;gridmaster&quot;. </p>
<p> To setup an alias name, edit your /etc/hosts file or modify your NIS setup to provide the alias for the NIS clients. </p>
<p> The host alias file must be readable from each host (use e.g. NFS shared file location). </p>
<dl>
<dt>
<dd>
<pre>
&gt;/opt/sge/default/lx-amd64/gethostname -all
Hostname: extern_name.mydomain
SGE name: gridmaster
Aliases:  loghost gridmaster
Host Address(es): 192.168.143.99
</pre>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell.</dl>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
<dt><a href="#lbAN">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAO">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAP">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAQ">COPYRIGHT</a></p>
<dd></dl>
