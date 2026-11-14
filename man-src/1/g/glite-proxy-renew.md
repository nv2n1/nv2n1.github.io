---
title: "glite-proxy-renew(1)"
name: "glite-proxy-renew"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-proxy-renew/"
description: "glite-proxy-renew – simple client for the proxy renewal daemon."
---

<h2 class="name">NAME</h2>
<p> glite-proxy-renew &#8211; simple client for the proxy renewal daemon.</p>
<h2>SYNOPSIS</h2>
<p> <code>glite-proxy-renew</code> -j<i> &lt;jobid&gt; </i>[<i>options</i>]<i> command</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-proxy-renew</code> communicates with the proxy renewal daemon and allows administrators to check it functions correctly. It is not meant to be used regularly or by regular users. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>start </code></p>
<dd> Register a proxy with the renewal daemon to keep it renewed. The name of the file from the repository is returned as the result. The <code>-f</code><i> FILE</i>, &#8211;file <i>FILE</i> option must be given. </p>
<dt><code>stop </code></p>
<dd> Unregisters a proxy from the renewal repository. The proxy file will be removed. </p>
<dt><code>get</code></p>
<dd> Lookup the renewal repository to find whether a proxy for the jobid is registered. If found, the command returns the filename from the repository. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> FILE</i>, &#8211;file <i>FILE</i></p>
<dd> Specifies the filename containing the proxy certificate that should be renewed. </p>
<dt><code>-h</code><i></i>, &#8211;help</p>
<dd> Display a list of valid options. </p>
<dt><code>-j</code><i> JOBID</i>, &#8211;jobid <i>JOBID</i></p>
<dd> Specifies the job id that is uniquely tied with the proxy. This option is obligatory and is required for all commands. </p>
<dt><code>-p</code><i> PORT</i>, &#8211;port <i>PORT</i></p>
<dd> Specifies port of the MyProxy server, which should be used to renew the proxy. </p>
<dt><code>-s</code><i> SERVER</i>, &#8211;server <i>SERVER</i></p>
<dd> Specifies the name of the MyProxy server, which should be used to renew the proxy. </p>
<dt><code>-v</code><i></i>, &#8211;version</p>
<dd> Display the version of the proxy renewal daemon. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/tmp/dgpr_renew_&lt;uid&gt;</i></p>
<dd> A unix socket used to talk to the daemon. It is created the daemon upon its start </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GLITE_PR_TIMEOUT</code></p>
<dd> Sets the maximum number of seconds that the daemon is given to answer a request done over the unix socket. The default value is 120 seconds. </p>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite Proxyrenewal issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/proxyrenewal/issues">https://github.com/CESNET/proxyrenewal/issues</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-glite-proxy-renewd/">glite-proxy-renewd</a></code>(8) </p>
<h2>AUTHOR</h2>
<p> EU EGEE, EU EMI </p>
<h2>Index</h2>
