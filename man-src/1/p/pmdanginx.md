---
title: "pmdanginx(1)"
name: "pmdanginx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdanginx/"
description: "pmdanginx – nginx performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdanginx</code> &#8211; nginx performance metrics domain agent (PMDA)</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdanginx</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports performance metrics from <code><a href="/docs/linux/man/8-nginx/">nginx</a></code>(8) &#8211; an HTTP and reverse proxy server, a mail proxy server, and a generic TCP proxy server.</p>
<h2>INSTALLATION</h2>
<p> This <font SIZE="-1">PMDA</font> requires that the <code>nginx</code> stub_status module is active and available at <a rel="nofollow" href="http://localhost/nginx_status">http://localhost/nginx_status</a> </p>
<p> In order to enable this module, the &quot;server&quot; section of the <i>nginx.conf</i> configuration file should contain the following. </p>
<pre><code>
location / nginx_status
{
    stub_status on;
    access_log off;
    allow 127.0.0.1;
    allow ::1;
    deny all;
}
</code></pre>
<p> Instrumentation availability can be verified using these commands (compile-time then run-time checks): </p>
<p>#&nbsp;<wbr>nginx -V 2&gt;&amp;1 | grep -o with-http_stub_status_module<br />
#&nbsp;<wbr>curl&nbsp;<wbr><a rel="nofollow" href="http://localhost/nginx_status">http://localhost/nginx_status</a> </p>
<p> Install the nginx <font SIZE="-1">PMDA</font> by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/nginx </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/nginx </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdanginx</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/nginx/nginx.conf</code></p>
<dd> optional configuration file for <code>pmdanginx</code></p>
<dt><code>$PCP_PMDAS_DIR/nginx/Install</code></p>
<dd> installation script for the <code>pmdanginx</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/nginx/Remove</code></p>
<dd> undo installation script for the <code>pmdanginx</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/nginx.log</code></p>
<dd> default log file for error messages from <code>pmdanginx</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/8-nginx/">nginx</a></code>(8). </p>
<h2>Index</h2>
