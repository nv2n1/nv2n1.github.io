---
title: "jura(1)"
name: "jura"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jura/"
description: "jura – Job Usage Reporter of ARC"
---

<h2 class="name">NAME</h2>
<p> jura &#8211; Job Usage Reporter of ARC</p>
<h2>DESCRIPTION</h2>
<p> The <code>jura</code> application is a resource-side accounting (usage logging) client. </p>
<h2>SYNOPSIS</h2>
<p> jura [<code>-E</code> <i>exp_time</i>] [<code>-L</code>] [<code>-u</code> <i>url</i> [<code>-u</code> <i>url</i> <code>-t</code> <i>topic</i> <code>-u</code> <i>url</i> &#8230;] ] [<code>-r</code> <i>time_range</i>] <i>ctrl_dir</i> [<i>ctrl_dir</i> &#8230;] </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-E</code></p>
<dd> expiration time (validity length) of job log files in days</p>
<dt><code>-u</code></p>
<dd> logging destination URL</p>
<dt><code>-t</code></p>
<dd> topic for a destination URL</p>
<dt><code>-o</code></p>
<dd> archived accounting records directory</p>
<dt><code>-L</code></p>
<dd> turns on timestamps and logging level in messages printed during execution</p>
<dt><code>-r</code></p>
<dd> time range of archived messages that will be resend</p>
<dt><code>-v</code></p>
<dd> show version of Jura (ARC)</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>ctrl_dir</code></p>
<dd>
&nbsp;<wbr>The A-REX control directory for a mapped local UNIX user</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> Normally, <code>jura</code> is invoked by A-REX periodically with the appropriate command line arguments, but it can also be executed interactively. </p>
<p> Job log files, i.e. files produced by A-REX for each job and stored under <i>&lt;ctrl_dir&gt;/logs</i> contain various usage data and configuration options for accounting (see NORDUGRID-TECH-24 for details of their content). These files are parsed by <code>jura</code>, converted into UR format, and submitted in batches to reporting destinations. A destination is a resource usage logging service; currently SGAS LUTS and CAR 1.2 message propagation are supported. Job log files older than the expiration time specified with the <code>-E</code> option are deleted without parsing. </p>
<p> If the <code>-u</code> option is absent, URs are submitted to the destination URLs specified in the job log files. If submitting succeeds, the corresponding job log files are deleted. This is the default, automatic mode of operation. </p>
<p> If destination URLs are specified with the <code>-u</code> option, URs are submitted only to these destinations (one UR per job to each destination). In this case, job log files are preserved even if submitting succeeds. </p>
<p> If the <code>-r</code> option is absent, <i>&lt;ctrl_dir&gt;</i> parameter be using as location of archived files, URs from the given directory are submitted to the destination URLs specified with <code>-u</code> option in the CLI.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>X509_USER_CERT</code></p>
<dd> The location of the certificate of the reporting entity, used only if not specified in job log files. The default is the standard host certificate location, <i>/etc/grid-security/hostcert.pem</i>. </p>
<dt><code>X509_USER_KEY</code></p>
<dd> The location of the private key of the reporting entity, used only if not specified in job log files. The default is the standard host key location, <i>/etc/grid-security/hostkey.pem</i>. </p>
<dt><code>X509_CERT_DIR</code></p>
<dd> The path to the certificates of trusted CAs, used only if not specified in job log files. The default is the standard certificates directory, <i>/etc/grid-security/certificates</i>. </p>
<dt><code>ARC_LOCATION</code></p>
<dd> The location where ARC is installed can be specified by this variable. If not specified the install location will be determined from the path to the command being executed, and if this fails a WARNING will be given stating the location which will be used. </p>
<dt><code>ARC_PLUGIN_PATH</code></p>
<dd> The location of ARC plugins can be specified by this variable. Multiple locations can be specified by separating them by : (; in Windows). The default location is <code>$ARC_LOCATION</code>/lib/arc (\ in Windows). </p>
</dl>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>Index</h2>
