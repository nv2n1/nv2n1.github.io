---
title: "actsync(8)"
name: "actsync"
section: "8"
letter: "a"
url: "/docs/linux/man/8-actsync/"
description: "actsync, actsyncd – Synchronize newsgroups"
---

<p>actsync, actsyncd &#8211; Synchronize newsgroups</p>
<h2>Synopsis</h2>
<p><code>actsync</code> [<code>-AkmT</code>] [<code>-b</code> <i>hostid</i>] [<code>-d</code> <i>hostid</i>] [<code>-g</code> <i>max</i>] [<code>-i</code> <i>ignore-file</i>] [<code>-I</code> <i>hostid</i>] [<code>-l</code> <i>hostid</i>] [<code>-n</code> <i>name</i>] [<code>-o</code> <i>format</i>] [<code>-p</code> <i>min-unchanged</i>] [<code>-q</code> <i>hostid</i>] [<code>-s</code> <i>size</i>] [<code>-t</code> <i>hostid</i>] [<code>-v</code> <i>verbosity</i>] [<code>-w</code> <i>seconds</i>] [<code>-z</code> <i>seconds</i>] [<i>host</i>] <i>host</i> </p>
<p> <code>actsyncd</code> <i>config</i> [<i>debug-level</i> [<i>debug-format</i>]]</p>
<h2>Description</h2>
<p><code>actsync</code> permits one to synchronize, compare, or merge two <i>active</i> files. With this utility one may add, change, or remove newsgroups on the local news server to make it similar to the list of the newsgroups found on another system or file. The synchronization need not be exact. Local differences in newsgroup lists may be maintained and preserved. Certain newsgroup errors may be detected and optionally corrected. </p>
<p> There are several reasons to run <code>actsync</code> (or <code>actsyncd</code>) on a periodic basis. Among the reasons are:</p>
<dl>
<dt>&bull;</p>
<dd>A control message to add, change or remove a newsgroup may fail to reach your site.</p>
<dt>&bull;</p>
<dd>Your <i>control.ctl</i> may be out of date or incomplete.</p>
<dt>&bull;</p>
<dd>News articles for a new newsgroup may arrive ahead (sometimes days ahead) of the control message.</p>
<dt>&bull;</p>
<dd>Control messages may be forged, thus bypassing the restrictions found in <i>control.ctl</i> unless you set up <font SIZE="-1">PGP</font> authentication (and even then, not all hierarchies use <font SIZE="-1">PGP</font> authentication).</p>
<dt>&bull;</p>
<dd>Your <i>active</i> file may have been trashed.</dl>
<p> If either <i>host</i> argument begins with <tt>&quot;.&quot;</tt> or <tt>&quot;/&quot;</tt>, it is assumed to be the name of a file containing information in the <i><a href="/docs/linux/man/5-active/">active</a></i>(5) format. The <i><a href="/docs/linux/man/1-getlist/">getlist</a></i>(1) utility may be used to obtain a copy of a remote system&#8217;s <i>active</i> file via its <font SIZE="-1">NNTP</font> server, or an <font SIZE="-1">FTP</font> client program can retrieve such a file from an <font SIZE="-1">FTP</font> archive (such as &lt;<a href="ftp://ftp.isc.org/pub/usenet/CONFIG/active">ftp://ftp.isc.org/pub/usenet/CONFIG/active</a>&gt;; see more about this below). Newsgroup information from a file may be treated as if it was obtained from a host. In this man page, the <i>host</i> arguments on the command line are called hosts, even though they may be file names. </p>
<p> If a host argument does not begin with <tt>&quot;.&quot;</tt> or <tt>&quot;/&quot;</tt>, it is assumed to be a hostname or Internet address. In this case, <code>actsync</code> will attempt to use the <font SIZE="-1">NNTP</font> protocol to obtain a copy of the specified system&#8217;s <i>active</i> file. If the host argument contains <tt>&quot;:&quot;</tt>, the right side will be considered the port to connect to on the remote system. If no port number is specified, <code>actsync</code> will connect to port <tt>119</tt>. </p>
<p> Regardless how the <i>active</i> file information is obtained, the actions of <code>actsync</code> remain the same. </p>
<p> The first host specified is taken to be the local host, the one where any changes would be made. The second host specified is the remote host that is being synchronized with. If only one host is specified, it is assumed to be the remote host to synchronize with, and the local host is assumed to be the default local <font SIZE="-1">NNTP</font> server as specified by the <font SIZE="-1">NNTPSERVER</font> environment variable or by the <i>server</i> value found in <i>inn.conf</i>. </p>
<p> If either host is specified as <tt>&quot;-&quot;</tt>, the default server will be used for that host, determined as described above. </p>
<p> The newsgroup synchronization, by default, involves all newsgroups found on both hosts. One may also synchronize a subset of newsgroups by directing <code>actsync</code> to ignore certain newsgroups from both systems. Only newsgroups with valid names will be synchronized. To be valid, a newsgroup name must consist only of alphanumeric characters, <tt>&quot;.&quot;</tt>, <tt>&quot;+&quot;</tt>, <tt>&quot;-&quot;</tt>, and <tt>&quot;_&quot;</tt>. One may not have two <tt>&quot;.&quot;</tt> characters in a row. The first character must be alphanumeric, as must any character following <tt>&quot;.&quot;</tt>. The name may not end in a <tt>&quot;.&quot;</tt> character. </p>
<p> The <code>actsyncd</code> daemon provides a convenient interface to configure and run <code>actsync</code>. If a host is not initially reachable, the daemon will retry up to 9 additional times, waiting 6 minutes before each retry. This daemon runs in the foreground, sending output to standard output and standard error. It then uses <i><a href="/docs/linux/man/8-mod-active/">mod-active</a></i>(8) to update the <i>active</i> file if there are commands for <code>ctlinnd</code> in its output. </p>
<p> The configuration filename for the daemon is given as a command line argument, usually <i>actsync.cfg</i> in <i>pathetc</i>. The config file can contain the following options: </p>
<pre> host=&lt;host&gt;
 ftppath=&lt;path-to-active&gt;
 ignore_file=&lt;ignore-file&gt;
 flags=&lt;actsync-options&gt;</pre>
<p>The host=, ignore_file=, and flags= lines are mandatory. Each keyword must start at the beginning of the line, and there may be no whitespace before the <tt>&quot;=&quot;</tt> character. Blank lines are ignored, as are comment lines that start with <tt>&quot;#&quot;</tt>. Any other lines may produce undefined results. </p>
<p> The &lt;host&gt; setting refers to the second (remote) <i>host</i> parameter to <code>actsync</code>. If &lt;path-to-active&gt; is provided, &lt;host&gt; is accessed as an <font SIZE="-1">FTP</font> server, retrieving the file named. If the filename ends in <tt>&quot;.gz&quot;</tt> or <tt>&quot;.Z&quot;</tt>, it will be automatically uncompressed after retrieval. &lt;ignore-file&gt; names the ignore file used by <code>actsync</code> (the <code>-i</code> option). &lt;actsync-options&gt; contains any other flags that you wish to pass to <code>actsync</code>. </p>
<p> Note that one should not include <code>-i</code> or <code>-o</code> options in the flags= line; they are automatically taken care of by <code>actsyncd</code>. </p>
<p> One may produce a trial <code>actsyncd</code> run without changing anything on the server by supplying the <i>debug-level</i> argument: </p>
<pre> actsyncd &lt;pathetc&gt;/actsync.cfg 2</pre>
<p>The <i>debug-level</i> causes <code>actsyncd</code> to run <code>actsync</code> with a <code>-v</code> <i>debug-level</i> flag (overriding any <code>-v</code> flag on the flags= line), not make any changes to the <i>active</i> file, write a new <i>active</i> file to standard output, and write debug messages to standard error. </p>
<p> If the <i>debug-format</i> argument is also given to <code>actsyncd</code>, the data written to standard output will be in <code>-o </code>debug-format instead of in <tt>&quot;-o a1&quot;</tt> format. </p>
<p> <font SIZE="-1">INN</font> comes with default values of <tt>&quot;<a href="ftp://ftp.isc.org">ftp.isc.org</a>&quot;</tt> for &lt;host&gt; and <tt>&quot;/pub/usenet/CONFIG/active.gz&quot;</tt> for &lt;path-to-active&gt;. You can read about the policies used for maintaining that <i>active</i> file at &lt;<a href="ftp://ftp.isc.org/pub/usenet/CONFIG/README">ftp://ftp.isc.org/pub/usenet/CONFIG/README</a>&gt;. Consider synchronizing from this file on a daily basis by using <code>cron</code>.</p>
<h2>Options</h2>
<p><code>actsync</code> takes the following options. </p>
<p> In all of the following options, the <i>hostid</i> parameter takes one of the following values: </p>
<pre> 0 neither server
 1 local default server
 2 remote server
 12 both servers
 21 both servers</pre>
<p>In other words, <tt>1</tt> refers to the local host (the first <i>host</i> argument on the <code>actsync</code> command line) and <tt>2</tt> refers to the remote host (the second <i>host</i> argument, or the only one if only one is given).</p>
<dl>
<dt><code>-A</code></p>
<dd><code>actsync</code> tries to authenticate before issuing the <font SIZE="-1">LIST</font> command.</p>
<dt><code>-b</code> <i>hostid</i></p>
<dd>This flag causes <code>actsync</code> to ignore for synchronization purposes newsgroups with <tt>&quot;bork.bork.bork&quot;</tt>-style names (newsgroups whose last 3 components are identical). For example, the following newsgroups have bork-style names: </p>
<pre> alt.helms.dork.dork.dork
 alt.auto.accident.sue.sue.sue
 alt.election.vote.vote.vote</pre>
<p>The default is <tt>&quot;-b 0&quot;</tt>; no newsgroups are ignored because of bork-style names.</p>
<dt><code>-d</code> <i>hostid</i></p>
<dd>This flag causes <code>actsync</code> to ignore newsgroups that have all numeric path components. For example, the following newsgroups have numeric path components: </p>
<pre> alt.prime.chongo.23209
 391581.times.2.to_the.216193.power.-1
 99.bottles.of.treacle.on.the.wall
 linfield.class.envio_bio.101.d</pre>
<p>The newsgroups directory of a newsgroup with a all numeric component could conflict with an article from another group if stored using the tradspool storage method; see <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5). For example, the directory for the first newsgroup listed above is the same path as article number 23209 from the newsgroup: </p>
<pre> alt.prime.chongo</pre>
<p>The default is <tt>&quot;-d 0&quot;</tt>; all numeric newsgroups from both hosts will be processed.</p>
<dt><code>-g</code> <i>max</i></p>
<dd>Ignore any newsgroup with more than <i>max</i> levels. For example, <tt>&quot;-g 6&quot;</tt> would ignore: </p>
<pre> alt.feinstien.votes.to.trash.freedom.of.speech
 alt.senator.exon.enemy.of.the.internet
 alt.crypto.export.laws.dumb.dumb.dumb</pre>
<p>but would not ignore: </p>
<pre> alt.feinstien.acts.like.a.republican
 alt.exon.amendment
 alt.crypto.export.laws</pre>
<p>If <i>max</i> is <tt>0</tt>, then the max level feature is disabled. </p>
<p> By default, the max level feature is disabled.</p>
<dt><code>-i</code> <i>ignore-file</i></p>
<dd>The <i>ignore-file</i>, usually <i>actsync.ign</i> in <i>pathetc</i>, allows one to have a fine degree of control over which newsgroups are ignored. It contains a set of rules that specifies which newsgroups will be checked and which will be ignored. </p>
<p> By default, these rules apply to both hosts. This can be modified by using the <code>-I</code> flag. </p>
<p> Blank lines and text after a <tt>&quot;#&quot;</tt> are considered comments and are ignored. </p>
<p> Rule lines consist of tokens separated by whitespace. Rule lines may be one of two forms: </p>
<pre> c &lt;newsgroup&gt; [&lt;type&gt; ...]
 i &lt;newsgroup&gt; [&lt;type&gt; ...]</pre>
<p>If the rule begins with a <tt>&quot;c&quot;</tt>, the rule requests certain newsgroups to be checked. If the rule begins with an <tt>&quot;i&quot;</tt>, the rule requests certain newsgroups to be ignored. The &lt;newsgroup&gt; field may be a specific newsgroup, or a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) pattern. </p>
<p> If one or more &lt;type&gt;s are specified, then the rule applies to the newsgroup only if it is of the specified type. Types refer to the 4th field of the <i>active</i> file; that is, a type may be one of: </p>
<pre> y
 n
 m
 j
 x
 =group.name</pre>
<p>Unlike <i>active</i> files, the <tt>&quot;group.name&quot;</tt> in an alias type may be a newsgroup name or a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) pattern. Also, <tt>&quot;=&quot;</tt> is equivalent to <tt>&quot;=*&quot;</tt>. </p>
<p> On each rule line, no pattern type may be repeated. For example, one may not have more than one type that begins with <tt>&quot;=&quot;</tt>, per line. However, one may achieve an effect equivalent to using multiple <tt>&quot;=&quot;</tt> types by using multiple rule lines affecting the same newsgroup. </p>
<p> By default, all newsgroups are candidates to be checked. If no <i>ignore-file</i> is specified, or if the ignore file contains no rule lines, all newsgroups will be checked. If an ignore file is used, each newsgroup in turn is checked against the ignore file. If multiple lines match a given newsgroup, the last line in the ignore file is used. </p>
<p> For example, consider the following ignore file lines: </p>
<pre> i *.general
 c *.general m
 i nsa.general</pre>
<p>The newsgroups ba.general and mod.general would be synchronized if moderated and ignored if not moderated. The newsgroup nsa.general would be ignored regardless of moderation status. All newsgroups not matching *.general would be synchronized by default.</p>
<dt><code>-I</code> <i>hostid</i></p>
<dd>This flag restricts which hosts are affected by the ignore file. This flag may be useful in conjunction with the <code>-m</code> flag. For example: </p>
<pre> actsync -i actsync.ign -I 2 -m host1 host2</pre>
<p>will keep all newsgroups currently on host1. It will also only compare host1 groups with non-ignored newsgroups from host2. </p>
<p> The default is <tt>&quot;-I 12&quot;</tt>; newsgroups from both hosts are ignored per the file specified with <code>-i</code>.</p>
<dt><code>-k</code></p>
<dd>By default, any newsgroup on the local host that has an invalid name will be considered for removal. This causes <code>actsync</code> simply ignore such newsgroups. This flag, used in combination with <code>-m</code>, will prevent any newsgroup from being scheduled for removal.</p>
<dt><code>-l</code> <i>hostid</i></p>
<dd>This flag causes problem newsgroups of type <tt>&quot;=&quot;</tt> to be considered as errors. Newsgroups of type <tt>&quot;=&quot;</tt> are newsgroups <i>active</i> entries that have a fourth field that begins with <tt>&quot;=&quot;</tt>; i.e., newsgroups that are aliased to other newsgroups. A problem newsgroup is one for which one of the following is true:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Aliased to itself.</p>
<dt>&bull;</p>
<dd>In an alias chain that loops around to itself.</p>
<dt>&bull;</p>
<dd>In an alias chain longer than 16 groups.</p>
<dt>&bull;</p>
<dd>Aliased to a non-existant newsgroup.</p>
<dt>&bull;</p>
<dd>Aliased to a newsgroup that has an error of some kind.</dl>
</dl>
<dl>
<dd>However, a newsgroup that is equivalent to an ignored newsgroup is not a problem. </p>
<p> The default is <tt>&quot;-l 12&quot;</tt>: problem newsgroups from both hosts are marked as errors.</dl>
<dt><code>-m</code></p>
<dd>Merge newsgroups instead of sync. By default, if a newsgroup exists on the local host but not the remote, it will be scheduled to be removed. This flag disables this process, permitting newsgroups unique to the local host to be kept.</p>
<dt><code>-n</code> <i>name</i></p>
<dd>Depending on <code>-o</code>, the <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8) command may be used to create newsgroups as necessary. When this is done, the default creator name used is <tt>&quot;actsync&quot;</tt>. This flag changes the creator name to <i>name</i>.</p>
<dt><code>-o</code> <i>format</i></p>
<dd>Determine the output or action format of this utility. <i>format</i> may be one of:</p>
<dl>
<dd>
<dl>
<dt>a</p>
<dd>Output in <i><a href="/docs/linux/man/5-active/">active</a></i>(5) format.</p>
<dt>a1</p>
<dd>Output in <i><a href="/docs/linux/man/5-active/">active</a></i>(5) format and output non-error ignored groups from the local host.</p>
<dt>ak</p>
<dd>Output in <i><a href="/docs/linux/man/5-active/">active</a></i>(5) format, but use the high and low (2nd and 3rd active fields) values from the remote host for any newsgroup being created.</p>
<dt>aK</p>
<dd>Output in <i><a href="/docs/linux/man/5-active/">active</a></i>(5) format, but use the high and low (2nd and 3rd active fields) values from the remote host for all newsgroups found on that host.</p>
<dt>a1k</p>
<dd>Output in <i><a href="/docs/linux/man/5-active/">active</a></i>(5) format, but use the high and low (2nd and 3rd active fields) values from the remote host for any newsgroup being created and output non-error ignored groups from the local host.</p>
<dt>a1K</p>
<dd>Output in <i><a href="/docs/linux/man/5-active/">active</a></i>(5) format, but use the high and low (2nd and 3rd active fields) values from the remote host for all newsgroups found on that host and output non-error ignored groups from the local host.</p>
<dt>ak1</p>
<dd>Same as <tt>&quot;a1k&quot;</tt>.</p>
<dt>aK1</p>
<dd>Same as <tt>&quot;a1K&quot;</tt>.</p>
<dt>c</p>
<dd>Output as commands to <code>ctlinnd</code>.</p>
<dt>x</p>
<dd>No output. Instead, directly run <code>ctlinnd</code> commands.</p>
<dt>xi</p>
<dd>No output. Instead, directly run <code>ctlinnd</code> commands in an interactive mode.</dl>
</dl>
<dl>
<dd>The <tt>&quot;a&quot;</tt>, <tt>&quot;a1&quot;</tt>, <tt>&quot;ak&quot;</tt>, <tt>&quot;aK&quot;</tt>, <tt>&quot;a1k&quot;</tt>, <tt>&quot;a1K&quot;</tt>, <tt>&quot;ak1&quot;</tt>, and <tt>&quot;aK1&quot;</tt> style formats allow one to format new <i>active</i> file instead of producing <code>ctlinnd</code> commands. They use high and low values of <tt>0000000000</tt> and <tt>0000000001</tt> respectively for newsgroups that are created unless otherwise specified. The <tt>&quot;ak&quot;</tt> and <tt>&quot;aK&quot;</tt> variants change the high and low values (2nd and 3rd <i>active</i> fields). In the case of <tt>&quot;ak&quot;</tt>, newsgroups created take their high and low values from the remote host. In the case of <tt>&quot;aK&quot;</tt>, all newsgroups found on the remote host take their high and low values from it. </p>
<p> The <tt>&quot;c&quot;</tt> format produces <code>ctlinnd</code> commands. No actions are taken because <code>actsync</code> simply prints <code>ctlinnd</code> commands on standard output. This output format is useful to let you see how the local host will be affected by the sync (or merge) with the remote host. </p>
<p> The sync (or merge) may be accomplished directly by use of the <tt>&quot;x&quot;</tt> or <tt>&quot;xi&quot;</tt> format. With this format, <code>actsync</code> uses the <i><a href="/docs/linux/man/2-execl/">execl</a></i>(2) system call to directly execute <code>ctlinnd</code> commands. The output of such exec calls may be seen if the verbosity level is at least <tt>2</tt>. </p>
<p> The <code>actsync</code> utility will pause for 4 seconds before each command is executed if <tt>&quot;-o x&quot;</tt> is selected. See the <code>-z</code> flag below for discussion of this delay and how to customize it. </p>
<p> The <tt>&quot;xi&quot;</tt> format interactively prompts on standard output and reads directives on standard input. One may pick and choose changes using this format. </p>
<p> Care should be taken when producing <i><a href="/docs/linux/man/5-active/">active</a></i>(5) formatted output. One should check to be sure that <code>actsync</code> exited with a zero status prior to using such output. Also one should realize that such output will not contain lines ignored due to <code>-i</code> even if <tt>&quot;-p 100&quot;</tt> is used. </p>
<p> By default, <tt>&quot;-o c&quot;</tt> is assumed.</dl>
<dt><code>-p</code> <i>min-unchanged</i></p>
<dd>By default, the <code>actsync</code> utility has safeguards against performing massive changes. If fewer than <i>min-unchanged</i> percent of the non-ignored lines from the local host remain unchanged, no actions (output, execution, etc.) are performed and <code>actsync</code> exits with a non-zero exit status. The <i>min-unchanged</i> value may be a floating point value such as <tt>66.667</tt>. </p>
<p> A change is a local newsgroup line that was removed, added, changed, or found to be in error. Changing the 2nd or 3rd <i>active</i> fields via <tt>&quot;-o ak&quot;</tt> or <tt>&quot;-o aK&quot;</tt> are not considered changes by <code>-p</code>. </p>
<p> To force <code>actsync</code> to accept any amount of change, use the <tt>&quot;-p 0&quot;</tt> option. To force <code>actsync</code> to reject any changes, use the <tt>&quot;-p 100&quot;</tt> option. </p>
<p> Care should be taken when producing <i><a href="/docs/linux/man/5-active/">active</a></i>(5) formatted output. One should check to be sure that <code>actsync</code> exited with a zero status prior to using such output. Also one should realize that such output will not contain lines ignored due to <code>-i</code> even if <tt>&quot;-p 100&quot;</tt> is used. </p>
<p> By default, 96% of the lines not ignored in the first <i>host</i> argument on the <code>actsync</code> command line must be unchanged. That is, by default, <tt>&quot;-p 96&quot;</tt> is assumed.</p>
<dt><code>-q</code> <i>hostid</i></p>
<dd>By default, all newsgroup errors are reported on standard error. This flag quiets errors from the specified <i>hostid</i>.</p>
<dt><code>-s</code> <i>size</i></p>
<dd>If <i>size</i> is greater than 0, then ignore newsgroups with names longer than <i>size</i> and ignore newsgroups aliased (by following <tt>&quot;=&quot;</tt> chains) to names longer than <i>size</i>. Length checking is performed on both the local and remote hosts. </p>
<p> By default, <i>size</i> is <tt>0</tt> and thus no length checking is performed.</p>
<dt><code>-t</code> <i>hostid</i></p>
<dd>Ignore improper newsgroups consisting of only a top component from the specified <i>hostid</i>. The following newsgroups are considered proper newsgroups despite top only names and therefore are exempt from this flag: </p>
<pre> control
 general
 junk
 test
 to</pre>
<p>For example, the following newsgroup names are improper because they only contain a top level component: </p>
<pre> dole_for_pres
 dos
 microsoft
 windows95</pre>
<p>The default is <tt>&quot;-t 2&quot;</tt>; that is, all improper top-level-only newsgroups from the remote host are ignored.</p>
<dt><code>-T</code></p>
<dd>This flag causes newsgroups on the remote host in new hierarchies to be ignored. Normally a newsgroup which only exists on the remote host, chongo.was.here for example, is created on the local host. However, if this flag is given and the local host does not have any other newsgroups in the same hierarchy (chongo.* in this case), the newsgroup in question will be ignored and will not be created on the local host.</p>
<dt><code>-v</code> <i>verbosity</i></p>
<dd>By default, <code>actsync</code> is not verbose. This flag controls the verbosity level as follows:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>No debug or status reports (default).</p>
<dt>1</p>
<dd>Print summary, but only if work was needed or done.</p>
<dt>2</p>
<dd>Print actions, exec output, and summary, but only if work was needed or done.</p>
<dt>3</p>
<dd>Print actions, exec output, and summary.</p>
<dt>4</p>
<dd>Full debug output.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-w</code> <i>seconds</i></p>
<dd>If <tt>&quot;-o x&quot;</tt> or <tt>&quot;-o xi&quot;</tt> is selected, <code>ctlinnd</code> will wait <i>seconds</i> seconds before timing out. The default value is <tt>&quot;-w 30&quot;</tt>.</p>
<dt><code>-z</code> <i>seconds</i></p>
<dd>If <tt>&quot;-o x&quot;</tt> is selected, <code>actsync</code> will pause for <i>seconds</i> seconds before each command is executed. This helps prevent <code>innd</code> from being busied-out if a large number of <code>ctlinnd</code> commands are needed. One can entirely disable this sleeping by using <tt>&quot;-z 0&quot;</tt>. </p>
<p> By default, <code>actsync</code> will pause for <tt>4</tt> seconds before each command is executed if <tt>&quot;-o x&quot;</tt> is selected.</dl>
<h2>Examples</h2>
<p>Determine the difference (but don&#8217;t change anything) between your newsgroup set and uunet&#8217;s set: </p>
<pre> actsync news.uu.net</pre>
<p>Same as above, with full debug and progress reports: </p>
<pre> actsync -v 4 news.uu.net</pre>
<p>Force a site to have the same newsgroups as some other site: </p>
<pre> actsync -o x master</pre>
<p>This may be useful to sync a slave site to its master, or to sync internal site to a gateway. </p>
<p> Compare your site with uunet, disregarding local groups and certain local differences with uunet. Produce a report if any differences were encountered: </p>
<pre> actsync -v 2 -i actsync.ign news.uu.net</pre>
<p>where <i>actsync.ign</i> contains: </p>
<pre> # Don't compare to.* groups as they will differ.
 #
 i to.*
 # These are our local groups that nobody else
 # (should) carry. So ignore them for the sake
 # of the compare.
 #
 i nsa.*
 # These groups are local favorites, so keep them
 # even if uunet does not carry them.
 #
 i ca.dump.bob.dorman
 i ca.keep.bob.dorman
 i alt.tv.dinosaurs.barney.die.die.die
 i alt.tv.dinosaurs.barney.love.love.love
 i alt.sounds.* =alt.binaries.sounds.*</pre>
<p>To interactively sync against news.uu.net, using the same ignore file: </p>
<pre> actsync -o xi -v 2 -i actsync.ign news.uu.net</pre>
<p>Based on newsgroups that you decided to keep, one could make changes to the <i>actsync.ign</i> file: </p>
<pre> # Don't compare to.* groups as they will differ.
 #
 i to.*
 # These are our local groups that nobody else
 # (should) carry. So ignore them for the sake
 # of the compare.
 #
 i nsa.*
 # These groups are local favorites, so keep them
 # even if uunet does not carry them.
 #
 i ca.dump.bob.dorman
 i alt.tv.dinosaurs.barney.die.die.die
 i alt.sounds.* =alt.binaries.sounds.*
 # Don't sync test groups, except for ones that are
 # moderated or that are under the gnu hierarchy.
 #
 i *.test
 c *.test m # check moderated test groups
 c gnu.*.test
 c gnu.test # just in case it ever exists</pre>
<p>Automatic processing may be set up by using the following <i>actsync.cfg</i> file: </p>
<pre> # Host to sync off of (host2).
 host=news.uu.net
 # Location of the ignore file.
 ignore_file=&lt;pathetc in inn.conf&gt;/actsync.ign
 # Where news articles are kept.
 spool=&lt;patharticles in inn.conf&gt;
 # <a href="//www.systutorials.com/docs/linux/man/8-actsync/">actsync</a>(8) flags
 #
 # Automatic execs, report if something was done,
 # otherwise don't say anything, don't report
 # uunet active file problems, just ignore
 # the affected entries.
 flags=-o x -v 2 -q 2</pre>
<p>and then by running <code>actsyncd</code> with the path to the config file: </p>
<pre> actsyncd &lt;pathetc&gt;/actsync.cfg</pre>
<p>The command </p>
<pre> actsyncd &lt;pathetc&gt;/actsync.cfg 4 &gt;cmd.log 2&gt;dbg.log</pre>
<p>will operate in debug mode, not change the <i>active</i> file, write <code>ctlinnd</code> style commands to <i>cmd.log</i>, and write debug statements to <i>dbg.log</i>. </p>
<p> To check only the major hierarchies against news.uu,net, use the following <i>actsync.ign</i> file: </p>
<pre> # By default, ignore everything.
 #
 i *
 # Check the major groups.
 #
 c alt.*
 c comp.*
 c gnu.*
 c humanities.*
 c misc.*
 c news.*
 c rec.*
 c sci.*
 c soc.*
 c talk.*</pre>
<p>and the command: </p>
<pre> actsync -i actsync.ign news.uu.net</pre>
<p>To determine the differences between your old <i>active</i> and your current default server: </p>
<pre> actsync &lt;pathetc&gt;/active.old -</pre>
<p>To report but not fix any newsgroup problems with the current <i>active</i> file: </p>
<pre> actsync - -</pre>
<p>To detect any newsgroup errors on your local server, and to remove any *.bork.bork.bork-style silly newsgroup names: </p>
<pre> actsync -b 2 - -</pre>
<p>The <i>active</i> file produced by: </p>
<pre> actsync &lt;flags&gt; -o x erehwon.honey.edu</pre>
<p>is effectively the same as the <i>active</i> file produced by: </p>
<pre> cd &lt;pathdb&gt;
 ctlinnd pause 'running actsync'
 rm -f active.new
 actsync &lt;flags&gt; -o a1 erehwon.honey.edu &gt; active.new
 rm -f active.old
 ln active active.old
 mv active.new active
 ctlinnd reload active 'running actsync'
 ctlinnd go 'running actsync'</pre>
<p>It should be noted that the final method above, pausing the server and simply replacing the <i>active</i> file, may be faster if you are making lots of changes.</p>
<h2>Files</h2>
<dl>
<dt><i>pathbin</i>/actsync</p>
<dd>The C program itself used to synchronize, compare, or merge two <i>active</i> files.</p>
<dt><i>pathbin</i>/actsyncd</p>
<dd>The Shell daemon which provides a convenient interface to configure and run <code>actsync</code>.</p>
<dt><i>pathetc</i>/actsync.cfg</p>
<dd>The configuration file which specifies the settings to use.</p>
<dt><i>pathetc</i>/actsync.ign</p>
<dd>The ignore file which contains a set of synchronization rules that specifies which newsgroups will be checked and which will be ignored.</dl>
<h2>Caution</h2>
<p>Careless use of this tool may result in the unintended addition, change, or removal of newsgroups. You should avoid using the <tt>&quot;x&quot;</tt> output format until you are sure it will do what you want.</p>
<h2>Bugs</h2>
<p>If a newsgroup appears multiple times, <code>actsync</code> will treat all copies as errors. However, if the group is marked for removal, only one rmgroup will be issued.</p>
<h2>History</h2>
<p>Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; for InterNetNews. Updated to support <font SIZE="-1">FTP</font> fetching by David Lawrence &lt;tale [at] isc.org&gt;. Converted to <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> actsync.pod 9768 2014-12-07 21:22:57Z iulius $ </p>
<p> By Landon Curt Noll &lt;chongo [at] toad.com&gt; (chongo was here /\../\). </p>
<p> Copyright (c) Landon Curt Noll, 1993. All rights reserved. </p>
<p> Permission to use and modify is hereby granted so long as this notice remains. Use at your own risk. No warranty is implied.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-getlist/">getlist</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-mod-active/">mod-active</a></i>(8), <i><a href="/docs/linux/man/1-simpleftp/">simpleftp</a></i>(1). </p>
