---
title: "nsdc(8)"
name: "nsdc"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsdc/"
description: "nsdc – Name Server Daemon (NSD) control script."
---

<p><code>nsdc</code> &#8211; Name Server Daemon (NSD) control script.</p>
<h2>Synopsis</h2>
<p><code>nsdc</code> [<code>-c</code> <i>configfile</i>] <i>start</i> | <i>stop</i> | <i>reload</i> | <i>rebuild</i> | <i>restart</i> | <i>running</i> | <i>update</i> | <i>notify</i> | <i>patch</i></p>
<h2>Description</h2>
<p><code>Nsdc</code> is the shell script that used to control <a href="/docs/linux/man/8-nsd/">nsd</a>(8) and <a href="/docs/linux/man/8-zonec/">zonec</a>(8) from <code>NSD</code> distribution. <code>Nsdc</code> is also suitable to be linked into <i>/etc/rc.d</i> directory on <i>BSD</i> like systems for automatic startup of <a href="/docs/linux/man/8-nsd/">nsd</a>(8) at boot time. At every invokation, <code>nsdc</code> will try to read the <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5) configuration file. An example of such configuration file is distributed with the <code>NSD</code> package as <i>nsd.conf.sample</i>. The config file is checked for errors before it is used, see <a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a>(8). Possible <code>nsdc</code> applications are:</p>
<dl>
<dt><i>start</i></p>
<dd>Start <a href="/docs/linux/man/8-nsd/">nsd</a>(8).</p>
<dt><i>stop</i></p>
<dd>Shut down <a href="/docs/linux/man/8-nsd/">nsd</a>(8) by sending <i>SIGTERM </i> to it.</p>
<dt><i>reload</i></p>
<dd>Initiate <a href="/docs/linux/man/8-nsd/">nsd</a>(8) name space database reload by sending <i>SIGHUP.</i></p>
<dt><i>rebuild</i></p>
<dd>Rebuild the <a href="/docs/linux/man/8-nsd/">nsd</a>(8) database by invoking <a href="/docs/linux/man/8-zonec/">zonec</a>(8) with appropriate arguments.</p>
<dt><i>restart</i></p>
<dd>Restart <a href="/docs/linux/man/8-nsdc/">nsdc</a>(8). This equals to nsdc stop &amp;&amp; nsdc start.</p>
<dt><i>running</i></p>
<dd>Check whether <a href="/docs/linux/man/8-nsd/">nsd</a>(8) is running. Returns error message and error code if it is not running, and no message and zero error code otherwise.</p>
<dt><i>update</i></p>
<dd>Updates all the slave zones which have <i>allow-notify:</i> from localhost (127.0.0.1 or ::1) allowed. If a TSIG key is specified for the allow-notify statement in the config file, it will be used to secure the notify. Note that NSD keeps track of zone timeouts automatically, this is only needed if you want to manually force updates by sending notify messages to the localhost.</p>
<dl>
<dd>Another method you can use is to stop nsd, delete the xfrd.state file and then start nsd again. It will try to update all zones. This method does not require allow-notify: statements.</dl>
<dt><i>notify</i></p>
<dd>Sends notify messages to all the slaves for all the zones that have the <i>notify:</i> keyword in the <i>nsd.conf</i> file. If a TSIG key is specified for a notify statement, it will be used to secure the notification message to that slave server.</p>
<dt><i>patch</i></p>
<dd>Merge zone transfer changes back to zone files. It reads in the nsd database (nsd.db) and difffile (ixfr.db), and overwrites the zone text files if they have been updated. Running this regularly ensures that the difffile does not grow infinitely.</dl>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> configfile</i></p>
<dd>Specify configfile to use instead of the default <i>/etc/nsd/nsd.conf</i>.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/nsd/nsd.conf</p>
<dd>Configuration file for nsd to change default pathnames and <code>NSD </code> flags. The zone names, pathnames to zone files and access control lists are also in <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5).</p>
<dt>/var/db/nsd/nsd.db</p>
<dd>default <code>NSD</code> database</p>
<dt>/var/db/nsd/nsd.db.lock</p>
<dd>Lockfile for the <code>NSD</code> database access by operator tools.</p>
<dt>/var/db/nsd/ixfr.db</p>
<dd>Journal of zone transfers, the diff file containing the new zone contents transferred.</p>
<dt>/var/db/nsd/xfrd.state</p>
<dd>State for the zone transfer process of <code>NSD.</code> Contains timeouts for the zones and whether zones are expired.</p>
<dt>/var/run/nsd.pid</p>
<dd>the process id of the name server.</dl>
<h2>Diagnostics</h2>
<p><code>Nsdc</code> will return zero return code if operation was successful and an error message to standard output plus a non-zero return code otherwise.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nsd/">nsd</a>(8), <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5), <a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a>(8), <a href="/docs/linux/man/8-nsd-notify/">nsd-notify</a>(8), <a href="/docs/linux/man/8-nsd-patch/">nsd-patch</a>(8), <a href="/docs/linux/man/8-nsd-xfer/">nsd-xfer</a>(8), <a href="/docs/linux/man/8-zonec/">zonec</a>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
<h2>Bugs</h2>
<p>Syntax checking of the config file is rudimentary and error messages may be wrong. If you do a nsdc patch, whilst a (long) zone transfer is busy, the zone transfer contents will be partially lost. After a reload, this will be detected and the zone transfer should be restarted. The reload that happens at the end of nsdc patch also frees up memory churn in <code>NSD </code> caused by zone transfers. </p>
