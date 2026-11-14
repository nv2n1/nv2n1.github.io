---
title: "pmwebd(1)"
name: "pmwebd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmwebd/"
description: "pmwebd – web access to PCP"
---

<h2>NAME</h2>
<p> <code>pmwebd</code> &#8211; web access to PCP</p>
<h2>SYNOPSIS</h2>
<p> <code>pmwebd</code> [<code>-p</code> <i>port</i>] [<code>-4</code>] [<code>-6</code>] [<code>-t</code> <i>timeout</i>] [<code>-R</code> <i>resdir</i>] [<code>-c</code> <i>number</i>] [<code>-h</code> <i>hostname</i>] [<code>-a</code> <i>archive</i>] [<code>-P</code>] [<code>-L</code>] [<code>-N</code>] [<code>-G</code>] [<code>-X</code>] [<code>-i</code> <i>min-interval</i>] [<code>-I</code> [<code>-K</code> <i>spec</i>] [<code>-A</code> <i>archivesdir</i>] [<code>-S</code>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>] [<code>-x</code> <i>file</i>] [<code>-v</code>] [<code>-?</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmwebd</code> is a network daemon that binds a subset of the Performance Co-Pilot (PCP) client API (<code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3)) to RESTful web applications using the HTTP (<code><a href="/docs/linux/man/3-pmwebapi/">PMWEBAPI</a></code>(3)) protocol. Web clients request a URI with the prefix <code>/pmapi</code> to access the bindings. <code>pmwebd</code> creates PCP contexts as requested by a dynamic pool of remote clients, and maintains them as long as the clients regularly reconnect to request PMAPI operations. Otherwise, PCP contexts are closed after a timeout. Permanent contexts may be requested on the command line. </p>
<p> In addition to the API binding, <code>pmwebd</code> may be optionally configured as a simple HTTP file server, in order to feed the web application itself to a web browser. URIs not matching the <code>/pmapi</code> prefix are mapped to files under the configured resource directory, if the <code>-R</code> option was given. </p>
<p> In addition, <code>pmwebd</code> may be optionally configured as a server of a subset of the graphite 0.9.12 web API, for URLs with the <code>/graphite</code> prefix, in order to expose PCP archives to interactive data-graphing web applications. </p>
<p> The options to <code>pmwebd</code> are as follows.</p>
<dl>
<dt><code>-p</code> <i>port</i></p>
<dd> Set the TCP port number on which <code>pmwebd</code> will listen for HTTP requests. The default is 44323.</p>
<dt><code>-4</code> or <code>-6</code></p>
<dd> Listen only on IPv4 or IPv6. By default, <code>pmwebd</code> will listen on both protocols, if possible.</p>
<dt><code>-A</code> <i>archdir</i></p>
<dd> Limit remote access to archives to only those beneath the given directory. By default, only files beneath the initial <code>pmwebd</code> working directory may be accessed.</p>
<dt><code>-R</code> <i>resdir</i></p>
<dd> Activate file serving beneath the given resource directory. All regular files there may be read and transcribed to remote clients. By default, file serving is disabled.</p>
<dt><code>-G</code></p>
<dd> Activate servicing of a subset of the graphite webapi. This exposes all PCP archives under the <code>-A</code> directory to remote clients. By default, graphite webapi serving is disabled. To use the graphite and/or grafana web applications included with <code>pmwebd</code>, use both <code>-G</code> and <code>-R</code>, and connect your web browser to <code><a rel="nofollow" href="http://127.0.0.1:43323/">http://127.0.0.1:43323/</a></code></p>
<dt><code>-X</code></p>
<dd> Disable encoding of common characters for metric names, which allows shorter graphite metric names.</p>
<dt><code>-i</code> <i>min-interval</i></p>
<dd> Set the minimum sampling interval for graphite time series in seconds. The default is 60. Smaller values give higher precision (but not necessarily accuracy) data, but may cost extra processing time at <code>pmwebd</code> or the web browser; and vice versa.</p>
<dt><code>-I</code></p>
<dd> Attempt to open an entire directory as an archive when traversing the <code>-A</code> DIR paths to serve graphite-api metrics. If successful, it can make the metric names much shorter (omitting individual encoded file names) and span across time. If the attempt fails, <code>pmwebd</code> will recurse to each individual archive file, just as though <code>-I</code> were not given. The difference is that if the <code>-I</code> attempt succeeds, a subdirectory is not recursed further, so if any other archives or subdirectories are present, they won&#8217;t be exposed to graphite-api clients.</p>
<dt><code>-t</code> <i>timeout</i></p>
<dd> Set the maximum timeout (in seconds) after the last operation on a pmapi web context, before it is closed by <code>pmwebd</code>. A smaller timeout may be requested by the web client.</p>
<dt><code>-c</code> <i>number</i></p>
<dd> Reset the next PMWEBAPI permanent context identifier as given. The default is 1.</p>
<dt><code>-h</code> <i>hostname</i> or <code>-a</code> <i>archive</i> or <code>-L</code></p>
<dd> Assign the next permanent PMWEBAPI context identifier to a PMAPI connection to the given host (with an extended syntax as given in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)), or archive file, or the PM_CONTEXT_LOCAL.</p>
<dt><code>-P</code></p>
<dd> Run in permissive mode, allowing Unix domain socket connections and/or local PMDA contexts. By default these are not allowed due to the automatic authentication that is performed on the server in these modes. Only enable this option if you understand the risks involved, and are sure that all remote <code>pmwebd</code> accesses will be from benevolent users. If enabled, unauthenticated remote <code><a href="/docs/linux/man/3-pmwebapi/">PMWEBAPI</a></code>(3) clients will be able to access potentially sensitive performance metric values which an unauthenticated <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) client usually would not be able to.</p>
<dt><code>-N</code></p>
<dd> Disable creation of new PMWEBAPI contexts via HTTP requests, leaving only permanent ones accessible.</p>
<dt><code>-K</code> <i>spec</i></p>
<dd> When fetching metrics from a local context, the <code>-K</code> option may be used to control the DSO PMDAs that should be made accessible. The <i>spec</i> argument conforms to the syntax described in <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3). More than one <code>-K</code> option may be used.</p>
<dt><code>-l</code> <i>logfile</i></p>
<dd> By default, logging goes to standard output/error file handles. The verbosity flag <code>-v</code> affects the amount of traffic. The <code>-l</code> option causes the log file to be written to <i>logfile</i> instead. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-U</code> <i>username</i></p>
<dd> If invoked as root, assume the identity of <i>username</i> before starting to accept incoming requests from web clients.</p>
<dt><code>-S</code></p>
<dd> Disable service advertisement. By default, <code>pmwebd</code> will advertise its presence on the network using any available mechanisms (such as Avahi/DNS-SD), assisting remote monitoring tools with finding it. These mechanisms are disabled with this option.</p>
<dt><code>-x</code> <i>file</i></p>
<dd> Before the <code>pmwebd</code> <i>logfile</i> can be opened, <code>pmwebd</code> may encounter a fatal error which prevents it from starting. By default, the output describing this error is sent to <code>/dev/tty</code> but it may redirected to <i>file</i>.</p>
<dt><code>-v</code></p>
<dd> Increase the verbosity of the <code>pmwebd</code> program as it logs to its standard output/error.</p>
<dt><code>-?</code></p>
<dd> Show <code>pmwebd</code> invocation help and exit.</dl>
<h2>SECURITY</h2>
<p> The current release of <code>pmwebd</code> is suitable for direct exposure to trusted networks only, due to several security limitations. Most or all of these limitations may be worked around by use of a web application firewall (for example, an Apache HTTPD proxy), which would add the constraints and capabilities absent within <code>pmwebd</code>. Such configuration is beyond the scope of this document.</p>
<dl>
<dt>encryption/confidentiality</p>
<dd> The <code>pmwebd</code> program is does not currently support HTTPS (SSL/TLS), so the HTTP traffic is not protected against network-level attacks.</p>
<dt>authentication</p>
<dd> The PMAPI layer does not possess a mandatory authentication mechanism, so any remote connection can access any metric exposed by suchly connected PMAPI contexts. However, a new host-context string may use authentication clauses of the longer host URLs, for example <i><a href="pcps://hostname?method=plain">pcps://hostname?method=plain</a>&amp;user=userid&amp;pass=password</i>. Use of resulting pmwebapi contexts later requires matching HTTP PLAIN authentication; see below.</p>
<dt>inbound admission control</p>
<dd> The <code>pmwebd</code> program does not impose access control on the origin or rate of its incoming requests. It may be possible for some clients to starve others.</p>
<dt>outbound admission control</p>
<dd> The <code>pmwebd</code> program does not impose access control on outbound connections when a new PMAPI context is created for a PMCD. (Without the <code>-P</code> option, connections to UNIX-domain / local PMCDs are blocked.) This enables hypothetical use of a <code>pmwebd</code> instance to be used as a network proxy/scanner. For an archive type context, the files must be located under the <code>pmwebd</code> current directory, or another directory specified by <code>-A</code>. One may entirely disable remotely specified PMAPI context creation using the <code>-N</code> option; in this case, specify a static set of contexts using the <code>-h</code>, <code>-a</code>, and/or <code>-L</code> options. You may assign them arbitrary context numbers with the <code>-c</code> option.</p>
<dt>context ownership</p>
<dd> Authenticated PCP contexts are protected by requiring the same HTTP PLAIN/simple userid/password credentials for related /pmapi requests. However, unauthenticated contexts for different web clients are kept distinct only by the assignment of large pseudorandom identifiers. It may be possible to find these by brute-force search or other techniques, thereby letting a web client impersonate another. For more privacy of the permanent contexts, use the <code>-c</code> option to reset their starting web context identifiers to a number much different from 1. On the other hand, context ownership is not that precious, since there exist no state-destructive operations for them, except perhaps metric store or instance profile settings.</dl>
<h2>STARTING AND STOPPING PMWEBD</h2>
<p> The <code>pmwebd</code> server may be started automatically at boot time and stopped when the system is being brought down. Users may also run customized <code>pmwebd</code> instances (under separate <code>-p</code> PORT numbers), for example for their own archive farms. <code>For management fo the system</code> <code>pmwebd</code>, become superuser and type </p>
<p> # $PCP_RC_DIR/pmwebd start </p>
<p> to start <code>pmwebd</code>, or </p>
<p> # $PCP_RC_DIR/pmwebd stop </p>
<p> to stop <code>pmwebd</code>. Starting <code>pmwebd</code> when it is already running is the same as stopping it and then starting it again.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMWEBDOPTIONS_PATH</code></p>
<dd> command line options and environment variable settings for <code>pmwebd</code> when launched from <code>$PCP_RC_DIR/pmwebd</code> This file is interpreted as a Bourne Shell script, expecting variable settings of the form &quot;OPTIONS=value&quot; and possibly others.</p>
<dt><code>$PCP_LOG_DIR/pmwebd/pmwebd.log</code></p>
<dd> Log file for system <code>pmwebd</code> service.</p>
<dt><code>$PCP_LOG_DIR</code></p>
<dd> Default directory for <code>-A</code> option: a base directory containing PCP archives.</p>
<dt><code>$PCP_SHARE_DIR/webapps</code></p>
<dd> Default directory for <code>-R</code> option: a base directory containing web applications.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmwebapi/">PMWEBAPI</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) <code><a rel="nofollow" href="http://graphite.readthedocs.org/">http://graphite.readthedocs.org/</a></code> and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
