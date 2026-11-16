---
title: "svnserve(8)"
name: "svnserve"
section: "8"
letter: "s"
url: "/docs/linux/man/8-svnserve/"
description: "svnserve – Server for the ‘svn’ repository access method"
---

<p>svnserve &#8211; Server for the &#8216;svn&#8217; repository access method</p>
<h2>Synopsis</h2>
<dl>
<dt><code>svnserve</code> [<i>options</i>]</dt>
<dd></dd></dl>
<h2>Description</h2>
<p><code>svnserve</code> allows access to Subversion repositories using the svn network protocol. It can both run as a standalone server process, or it can run out of inetd. You must choose a mode of operation when you start <code>svnserve</code>. The following options are recognized: </p>
<dl>
<dt><code>-d</code>, <code>&#8211;daemon</code></dt>
<dd>Causes <code>svnserve</code> to run in daemon mode. <code>svnserve</code> backgrounds itself and accepts and serves TCP/IP connections on the svn port (3690, by default).</dd></dl>
<dl>
<dt><code>&#8211;listen-port</code>=<i>port</i></dt>
<dd>Causes <code>svnserve</code> to listen on <i>port</i> when run in daemon mode.</dd></dl>
<dl>
<dt><code>&#8211;listen-host</code>=<i>host</i></dt>
<dd>Causes <code>svnserve</code> to listen on the interface specified by <i>host</i>, which may be either a hostname or an IP address.</dd></dl>
<dl>
<dt><code>&#8211;foreground</code></dt>
<dd>When used together with <code>-d</code>, this option causes <code>svnserve</code> to stay in the foreground. This option is mainly useful for debugging.</dd></dl>
<dl>
<dt><code>-i</code>, <code>&#8211;inetd</code></dt>
<dd>Causes <code>svnserve</code> to use the stdin/stdout file descriptors, as is appropriate for a daemon running out of inetd.</dd></dl>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Displays a usage summary and exits.</dd></dl>
<dl>
<dt><code>&#8211;version</code></dt>
<dd>Print <code>svnserve</code>&#8216;s version and the repository filesystem back-end(s) a particular <code>svnserve</code> supports.</dd></dl>
<dl>
<dt><code>-r</code> <i>root</i>, <code>&#8211;root</code>=<i>root</i></dt>
<dd>Sets the virtual root for repositories served by <code>svnserve</code>. The pathname in URLs provided by the client will be interpreted relative to this root, and will not be allowed to escape this root.</dd></dl>
<dl>
<dt><code>-R</code> <code>&#8211;read-only</code></dt>
<dd>Force all write operations through this <code>svnserve</code> instance to be forbidden, overriding all other access policy configuration. Do not use this option to set general repository access policy &#8211; that is what the <code>conf/svnserve.conf</code> repository configuration file is for. This option should be used only to restrict access via a certain method of invoking <code>svnserve</code> &#8211; for example, to allow write access via SSH, but not via a <code>svnserve</code> daemon, or to create a restricted SSH key which is only capable of read access.</dd></dl>
<dl>
<dt><code>-t</code>, <code>&#8211;tunnel</code></dt>
<dd>Causes <code>svnserve</code> to run in tunnel mode, which is just like the inetd mode of operation (serve one connection over stdin/stdout) except that the connection is considered to be pre-authenticated with the username of the current uid. This flag is selected by the client when running over a tunnel agent.</dd></dl>
<dl>
<dt><code>&#8211;tunnel-user</code>=<i>username</i></dt>
<dd>When combined with <code>&#8211;tunnel</code>, overrides the pre-authenticated username with the supplied <i>username</i>. This is useful in combination with the ssh authorized_key file&#8217;s &quot;command&quot; directive to allow a single system account to be used by multiple committers, each having a distinct ssh identity.</dd></dl>
<dl>
<dt><code>-T</code>, <code>&#8211;threads</code></dt>
<dd>When running in daemon mode, causes <code>svnserve</code> to spawn a thread instead of a process for each connection. The <code>svnserve</code> process still backgrounds itself at startup time.</dd></dl>
<dl>
<dt><code>&#8211;config-file</code>=<i>filename</i></dt>
<dd>When specified, <code>svnserve</code> reads <i>filename</i> once at program startup and caches the <code>svnserve</code> configuration and any passwords and authorization configuration referenced from <i>filename</i>. <code>svnserve</code> will not read any per-repository <code>conf/svnserve.conf</code> files when this option is used. See the <code><a href="/docs/linux/man/5-svnserve-conf/">svnserve.conf</a></code>(5) man page for details of the file format for this option.</dd></dl>
<dl>
<dt><code>&#8211;pid-file</code>=<i>filename</i></dt>
<dd>When specified, <code>svnserve</code> will write its process ID to <i>filename</i>.</dd></dl>
<dl>
<dt><code>-X</code>, <code>&#8211;listen-once</code></dt>
<dd>Causes <code>svnserve</code> to accept one connection on the svn port, serve it, and exit. This option is mainly useful for debugging.</dd></dl>
<p> Unless the <code>&#8211;config-file</code> option was specified on the command line, once the client has selected a repository by transmitting its URL, <code>svnserve</code> reads a file named <code>conf/svnserve.conf</code> in the repository directory to determine repository-specific settings such as what authentication database to use and what authorization policies to apply. See the <code><a href="/docs/linux/man/5-svnserve-conf/">svnserve.conf</a></code>(5) man page for details of that file format.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-svnserve-conf/">svnserve.conf</a></code>(5) </p>
