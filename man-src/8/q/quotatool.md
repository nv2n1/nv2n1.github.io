---
title: "quotatool(8)"
name: "quotatool"
section: "8"
letter: "q"
url: "/docs/linux/man/8-quotatool/"
description: "quotatool – manipulate filesystem quotas"
---

<p>quotatool &#8211; manipulate filesystem quotas</p>
<h2>Synopsis</h2>
<p><code>quotatool</code> [-u [:]uid | -g [:]gid] [-b | -i] [-r | -l NUM | -q NUM] [-nvR] [-d] <i>filesystem</i><br />
 <code>quotatool</code> (-u | -g) (-b | -i) -t TIME [-nv] <i>filesystem</i><br />
 <code>quotatool</code> [-hV]</p>
<h2>Description</h2>
<p><code>quotatool</code> is a tool for manipulating filesystem quotas. Depending on the commandline options given, it can set hard or soft limits on block and inode usage, set and reset grace periods, for both users and (if your system supports this) groups. The filesystem to set the quota on is given as the first (and only) non-option element, and it is either the block special file (i.e /dev/sda3) or the mount point (i.e. /home) for the filesystem.</p>
<h2>Options</h2>
<dl>
<dt>-u [[:]uid]</p>
<dd>Set user quotas</p>
<dt>-g [[:]gid]</p>
<dd>Set group quotas</dl>
<p> <i>uid</i> and <i>gid</i> are either the numerical ID of the user or group, or its name in the <code>/etc/passwd</code> and <code>/etc/group</code> files. Prefix <i>:</i> allows using numerical uid/gid not present in /etc/passwd or /etc/group.</p>
<dl>
<dt>-b</p>
<dd>Set block quotas [default]</p>
<dt>-i</p>
<dd>Set inode quotas</dl>
<p> The -b and -i options are persistent &#8212; they stay in effect until they are overridden.</p>
<dl>
<dt>-R</p>
<dd>Only raise quotas, never lower. Makes sure you don&#8217;t accidentally lower quotas for a user/group.</p>
<dt>-t TIME</p>
<dd>Set the system-wide grace period to TIME. TIME consists of an optional &#8216;-&#8216; or &#8216;+&#8217; character, a number, and optionally one of the following modifiers: &quot;seconds&quot;, &quot;minutes&quot;, &quot;hours&quot;, &quot;days&quot;, &quot;weeks&quot;, or &quot;months&quot;. Unique abbreviations (e.g. &quot;s&quot;, &quot;mo&quot;) are also accepted. The default is &quot;seconds&quot;. The argument should be preceded by -u|-g and -b|-i</p>
<dt>-r</p>
<dd>Reset the grace period</p>
<dt>-l NUM</p>
<dd>Set hard limit to NUM</p>
<dt>-q NUM</p>
<dd>Set soft limit (quota) to NUM</dl>
<p> NUM consists of an optional &#8216;-&#8216; or &#8216;+&#8217; character, a number (integer or floating point), and optionally one of the following modifiers: &quot;Kb&quot;, &quot;Mb&quot;, &quot;Gb&quot;, &quot;Tb&quot;, &quot;bytes&quot;, or &quot;blocks&quot;. Unique abbreviations are also accepted. The default is &quot;blocks&quot;. Modifiers are base 2 for block quotas (1k = 1024), and base 10 for inode quotas (1k = 1000) </p>
<p> If +/- is supplied, the existing quota is increased or reduced by the specified amount.</p>
<dl>
<dt><i>-d</i></p>
<dd>Dump quota info for user/group in a machine readable format:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&#8212;&#8212;- BLOCKS &#8212;&#8212;&#8211;| |&#8212;&#8212;&#8211; FILES &#8212;&#8212;&#8211;|<br />
 <code>uid/gid mountpoint current quota limit grace current quota limit grace</code></p>
<dd><code>grace</code> is the number of seconds from now until the grace time ends. May be negative = time already passed. When quota is not passed, grace is zero.</p>
<dt>-n</p>
<dd>dry-run: show what would have been done but don&#8217;t change anything. Use together with -v</p>
<dt>-v</p>
<dd>Verbose output. Use twice or thrice for even more output (debugging)</p>
<dt><i>-h</i></p>
<dd>Print a usage message to stdout and exit successfully</p>
<dt><i>-V</i></p>
<dd>Print version information to stdout and exit successfully</dl>
<h2>Filesystems / Formats</h2>
<p>On Linux, <code>quotatool</code> works with both &quot;old&quot;, &quot;vfsv0&quot; and &quot;vfsv1&quot; + &quot;generic&quot; kernel-quota formats. Supported filesystems: ext2, ext3, ext4, ReiserFS and XFS. </p>
<p> Mac OS X: hfs </p>
<p> FreeBSD / OpenBSD / NetBSD: filesystems ufs and ffs</p>
<h2>Examples</h2>
<p>Set soft block limit to 800Mb, hard block limit to 1.2 Gb for user mpg4 on /home:<br />
quotatool -u mpg4 -b -q 800M -l 1.2G&nbsp;<wbr>/home Raise soft block limit by 100M for non-existent gid 12345 on /dev/loop3:<br />
quotatool -g :12345 -b -q&nbsp;<wbr>+100M&nbsp;<wbr>/dev/loop3 Set soft inode limit to 1.8k (1800), hard inode limit to 2000 for user johan on /var:<br />
quotatool -u johan -i -q 1.8K -l 2000&nbsp;<wbr>/var Set the global block grace period to one week on /home:<br />
quotatool -u&nbsp;<wbr>&nbsp;<wbr>-b -t&nbsp;<wbr>&quot;1 week&quot;&nbsp;<wbr>/home Restart inode grace period for user johan on root filesystem:<br />
quotatool -u johan -i -r&nbsp;<wbr>/ </p>
<h2>Notes</h2>
<p>Grace periods are set on a &quot;global per quotatype and filesystem&quot; basis only. Each quotatype (usrquota / grpquota) on each filesystem has two grace periods &#8211; one for block limits and one for inode limits. It is not possible to set different grace periods for users on the same filesystem. According to &#8216;man quotactl&#8217;, global grace periods should be supported on BSD. quotatool on BSD does the right thing, which can be confirmed with &#8216;edquota -t&#8217;. However, the value doesn&#8217;t seem to be used by the system when usage passes a soft limit. So far, I haven&#8217;t been able to make global grace periods work on Mac OS X, either with &#8216;edquota -t&#8217; or quotatool. Using non-existent uids/gids like &quot;:12345&quot; can be useful when configuring quotas on a mounted filesystem which is a separate system in it self, like when preparing an install image or repairing a filesystem from another installation. Limit arguments can be specified in several ways, these are all equivalent:<br />
&nbsp;<wbr>&nbsp;<wbr>1M<br />
&nbsp;<wbr>&nbsp;<wbr>1m<br />
&nbsp;<wbr>&nbsp;<wbr>1Mb<br />
&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&quot;Mb&quot; Use +/- to raise/lower quotas relative to current limits Use -v (or -v -v) to see verbose/debug info when running commands </p>
<h2>Files</h2>
<p><code>quota.user</code> , <code>quota.group</code> (linux, *BSD, aix)<br />
 <code>.quota.user</code> , <code>.quota.group</code> (Mac OS X)<br />
 <code>quotas</code> (solaris, &#8230;)</p>
<h2>Bugs</h2>
<p>Please check <a rel="nofollow" href="https://github.com/ekenberg/quotatool">https://github.com/ekenberg/quotatool</a> for any open issues. Feel free to add a new issue if you find an unresolved bug! </p>
<p> Calling <code>quotatool</code> with more than one -v option will cause a segfault on some systems. This will happen if vprintf (3) fails to check for NULL arguments. GNU libc doesn&#8217;t have this problem, solaris libc does.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8), <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8), <code><a href="/docs/linux/man/8-quotaon/">quotaon</a></code>(8), <code><a href="/docs/linux/man/8-repquota/">repquota</a></code>(8) </p>
