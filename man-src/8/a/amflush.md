---
title: "amflush(8)"
name: "amflush"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amflush/"
description: "amflush – flush Amanda backup files from holding disk to tape"
---

<p>amflush &#8211; flush Amanda backup files from holding disk to tape</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amflush</code> [-b] [-f] [&#8211;exact-match] [-s] [-D&nbsp;<wbr><i>datestamp</i>] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>config</i> [<i>host</i>&nbsp;<wbr>[<i>disk</i>&#8230;]&#8230;]</dl>
<h2>Description</h2>
<p><code>Amflush</code></p>
<dd>writes Amanda backups from the holding disks to tape, and updates the Amanda info database and <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5) accordingly. It is similar to amdump, but does not perform any backup operations on Amanda clients. Backups may stay in a holding disk when something is wrong with the tape at the time <code>amdump</code> is run. When this happens, the problem must be corrected and <code>amflush</code> run by hand. </p>
<p> The command optionally takes a set of DLE specifications (see <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7)) to narrow the DLEs for which dumps will be flushed. All dumps in holding are flushed if no expressions are given.</p>
<h2>Options</h2>
<p><code>-b</code></p>
<dl>
<dd>Run <code>amflush</code> in batch mode. All datestamps are selected unless specified. The flush is started without confirmation.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Run <code>amflush</code> in foreground. <code>Amflush</code> normally detaches itself from the tty and runs as a background process. With the <code>-f</code> option, <code>amflush</code> stays in the foreground. This is useful if <code>amflush</code> is run as part of another script that, for example, advances the tape after the flush is completed.</dl>
<p> <code>-s</code></p>
<dl>
<dd>Write log to stdout/stderr instead of the amflush log file. Requires the <code>-f</code> option.</dl>
<p> <code>-D datestamp</code></p>
<dl>
<dd>specify a datestamp expression you want to flush; see <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7) for details on the format of this expression. <code>-D 20001225-7</code> will flush all dumps from 25 december 2000 to 27 december 2000.</dl>
<p> <code>&#8211;exact-match</code></p>
<dl>
<dd>The host and disk are parsed as exact values</dl>
<p> <i>host</i> [<i>disk</i>]*</p>
<dl>
<dd>Specify the host and disk on which the command will work &#8212; see the description of DLE specifications in <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7).</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<p> You can specify many host/disk expressions, only disks that match an expression will be flushed. All disks are flushed if no expressions are given. see the &quot;HOST &amp; DISK EXPRESSION&quot; section of <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) for a description. </p>
<p> <code>Amflush</code> will look in the holding disks specified by the <i>amanda.conf</i> file in /usr/local/etc/amanda/<i>config</i> for any non-empty Amanda work directories. It then prompts you to select a directory or to process all of the directories. The work directories in the holding disks are named by the date at the time <code>amdump</code> was run, e.g. 19910215. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Example</h2>
<p><code>Amflush</code> will search for holding areas associated with the <i>daily</i> configuration. After you select which holding area to flush, <code>amflush</code> writes the data to tape, updates the databases and sends a mail report similar to <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8). </p>
<pre>% amflush MyConfig
Scanning /amanda-hold...
 20001113: found Amanda directory.
 20001114: found Amanda directory.
Multiple Amanda directories, please pick one by letter:
 A. 20001113
 B. 20001114
Select directories to flush [A..B]: [ALL] all
Flushing dumps in 20001113, 20001114,
today: 20001117
to tape drive /dev/rmt/0mn.
Expecting tape DMP014 or a new tape. (The last dumps were to tape DMP013)
Are you sure you want to do this? yes
Running in background, you can log off now.
You'll get mail when amflush is finished.</pre>
<p>The following example causes amflush to flush everything to tape, then ejects tape, using &#8216;at&#8217; to run the task in the background. </p>
<pre>% echo 'amflush -b -f MyConfig &amp;&amp; mt offline' | at now</pre>
<h2>Exit Code</h2>
<p>The exit code of <code>amflush</code> is the ORed value of: </p>
<pre> 0 = success
 1 = error
 4 = a dle failed
 8 = Don't know the status of a dle (RESULT_MISSING in the report)
 16 = tape error or no more tape</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8), <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
