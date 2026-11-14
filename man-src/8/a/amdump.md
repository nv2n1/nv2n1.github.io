---
title: "amdump(8)"
name: "amdump"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amdump/"
description: "amdump – back up all disks in an Amanda configuration"
---

<p>amdump &#8211; back up all disks in an Amanda configuration</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amdump</code> [&#8211;no-taper] [&#8211;exact-match] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>config</i> [<i>host</i>&nbsp;<wbr>[<i>disk</i>&#8230;]&#8230;]</dl>
<h2>Description</h2>
<p><code>Amdump</code></p>
<dd>is the main interface to the Amanda backup process. It loads the specified configuration and attempts to back up every disk specified by the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5). <code>Amdump</code> is normally run by <code>cron</code>. </p>
<p> The command optionally takes a set of DLE specifications (see <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7)) to narrow the DLEs that will be dumped. All disks are dumped if no expressions are given. </p>
<p> If a file named hold exists in the configuration directory, <code>amdump</code> will wait until it is removed before starting the backups. This allows scheduled backups to be delayed when circumstances warrant, for example, if the tape device is being used for some other purpose. While waiting, <code>amdump</code> checks for the hold file every minute. </p>
<p> In some cases it is desirable to dump all Amanda clients to holding disk without writing anything to storage media. The <code>&#8211;no-taper</code> option instructs Amanda to not start the taper, and thus enter degraded mode immediately. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><i>host</i> [<i>disk</i>]*</p>
<dl>
<dd>Specify the host and disk on which the command will work &#8212; see the description of DLE specifications in <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7).</dl>
<p> <code>&#8211;exact-match</code></p>
<dl>
<dd>The host and disk are parsed as exact values</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>Example</h2>
<p>Here is a typical crontab entry. It runs <code>amdump</code> every weeknight at 1 a.m. as user <code>bin</code>: </p>
<pre>0 1 * * 1-5 bin /usr/local/sbin/amdump daily</pre>
<p>Please see the <code><a href="/docs/linux/man/5-crontab/">crontab</a></code>(5) or <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1) manual page for the correct crontab format for your system.</p>
<h2>Messages</h2>
<p>amdump: waiting for hold file to be removed</p>
<dl>
<dd>The &quot;hold&quot; file exists and <code>amdump</code> is waiting for it to be removed before starting backups.</dl>
<p> amdump: amdump or amflush is already running, or you must run amcleanup</p>
<dl>
<dd>Amdump detected another <code>amdump</code> or <code>amflush</code> running, or the remains of a previous incomplete <code>amdump</code> or <code>amflush</code> run. This run is terminated. If the problem is caused by the remains of a previous run, you must execute <code><a href="/docs/linux/man/8-amcleanup/">amcleanup</a></code>(8) and then rerun <code>amdump</code>.</dl>
<h2>Exit Code</h2>
<p>The exit code of <code>amdump</code> is the ORed value of: </p>
<pre> 0 = success
 1 = error
 2 = a dle give strange message
 4 = a dle failed
 8 = Don't know the status of a dle (RESULT_MISSING in the report)
 16 = tape error or no more tape</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amcheck/">amcheck</a></code>(8), <code><a href="/docs/linux/man/8-amcleanup/">amcleanup</a></code>(8), <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8), <code><a href="/docs/linux/man/8-amflush/">amflush</a></code>(8), <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8), <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
