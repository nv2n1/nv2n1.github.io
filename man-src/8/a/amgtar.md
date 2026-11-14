---
title: "amgtar(8)"
name: "amgtar"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amgtar/"
description: "amgtar – Amanda Application to interface with GNU Tar"
---

<p>amgtar &#8211; Amanda Application to interface with GNU Tar</p>
<h2>Description</h2>
<p>Amgtar is an Amanda Application API script. It should not be run by users directly. It uses GNU Tar to backup and restore data. </p>
<p> The <code>diskdevice</code> in the disklist (DLE) must be the directory to backup.</p>
<h2>Properties</h2>
<p>This section lists the properties that control amgtar&#8217;s functionality. See <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) for information on application properties and how they are configured. </p>
<p> ATIME-PRESERVE</p>
<dl>
<dd>If &quot;YES&quot; (the default), amgtar use the <i>&#8211;atime-preserve=system</i> option of gnutar to not update the atime of all files accessed; if &quot;NO&quot;, gnutar will updates the atime for all files accessed. This property works only if you have gnutar 1.15.90 or newer, if not, you must set ATIME_PRESERVE to &quot;NO&quot;.</dl>
<p> CHECK-DEVICE</p>
<dl>
<dd>If &quot;YES&quot; (the default), amgtar checks that the device number doesn&#8217;t change for each file. If &quot;NO&quot;, changes in device number are ignored. To ignore device numbers, tar must support the <i>&#8211;no-check-device</i> option (gnutar 1.19.90 and newer). This option is needed for some filesystems and devices on which device numbers change frequently, such as LVM or FiberChannel.</dl>
<p> COMMAND-OPTIONS</p>
<dl>
<dd>If set, theses options are passed asis to gtar. Each option must be a different value of the property. Some option can break how amanda do backup, use it with care. </p>
<p> Use: </p>
<pre> property &quot;COMMAND-OPTIONS&quot; &quot;--foo&quot; &quot;bar&quot;</pre>
<p>Do not use: </p>
<pre> property &quot;COMMAND-OPTIONS&quot; &quot;--foo bar&quot;</pre>
</dl>
<p> DIRECTORY</p>
<dl>
<dd>If set, gnutar will backup from that directory instead of the <i>diskdevice</i> set by the DLE. On restore, the data is restore in that directory instead of the current working directory.</dl>
<p> GNUTAR-LISTDIR</p>
<dl>
<dd>The directory where gnutar stores the database it uses to generate incremental dumps. The default is set when Amanda is built.</dl>
<p> GNUTAR-PATH</p>
<dl>
<dd>The path to the gnutar binary. The default is set when Amanda is built.</dl>
<p> IGNORE-ZEROS</p>
<dl>
<dd>If &quot;YES&quot; (the default), use the <i>&#8211;ignore-zeros</i> argument of gtar on recovery, set it to &quot;NO&quot; if you do not want that argument.</dl>
<p> INCLUDE-LIST-GLOB</p>
<dl>
<dd>A filename containing include glob expression for the restore command.</dl>
<p> EXCLUDE-LIST-GLOB</p>
<dl>
<dd>A filename containing exclude glob expression for the restore command.</dl>
<p> ONE-FILE-SYSTEM</p>
<dl>
<dd>If &quot;YES&quot; (the default), do not allow gnutar to cross filesystem boundaries. If &quot;NO&quot;, gnutar will cross filesystem boundaries. This corresponds to the <i>&#8211;one-filesystem</i> option of gnutar.</dl>
<p> TAR-BLOCKSIZE</p>
<dl>
<dd>Block size of Nx512 bytes (default N=20). This corresponds to the <i>&#8211;blocking-factor</i> option of gnutar.</dl>
<p> SPARSE</p>
<dl>
<dd>If &quot;YES&quot; (the default), gnutar will store sparse files efficiently. If &quot;NO&quot;, then the <i>&#8211;sparse</i> option is not given to gnutar, and it will not try to detect sparse files.</dl>
<p> NO-UNQUOTE</p>
<dl>
<dd>If &quot;NO&quot; (the default), gnutar doesn&#8217;t get the <i>&#8211;no-unquote</i> option and the diskname can&#8217;t have some characters, eg. &#8216;\&#8217;. If &quot;YES&quot;, then the <i>&#8211;no-unquote</i> option is given to gnutar and the diskname can have any characters. This option is available only if you are using tar-1.16 or newer.</dl>
<p> ACLS</p>
<dl>
<dd>Default &quot;NO&quot;. If &quot;YES&quot;, gnutar will preserve ACL extended attributes. This corresponds to the <i>&#8211;acls</i> gnutar option. Requires a GNU Tar with nonstandard extended attribute patches from the Fedora Project.</dl>
<p> SELINUX</p>
<dl>
<dd>Default &quot;NO&quot;. If &quot;YES&quot;, gnutar will preserve SELinux extended attributes on Linux. This corresponds to the <i>&#8211;selinux</i> gnutar option. Requires a GNU Tar with nonstandard extended attribute patches from the Fedora Project.</dl>
<p> XATTRS</p>
<dl>
<dd>Default &quot;NO&quot;. If &quot;YES&quot;, gnutar will preserve all extended attributes. This corresponds to the <i>&#8211;xattrs</i> gnutar option. If enabled, this option also implies the ACLS and SELINUX properties, regardless of their settings, as they are implemented as extended attributes. Requires a GNU Tar with nonstandard extended attribute patches from the Fedora Project.</dl>
<p> EXIT-HANDLING</p>
<dl>
<dd>List which exit status of gtar are good or bad. eg. &quot;1=GOOD 2=BAD&quot;, exit status of 1 will produce a good backup, exit status of 2 will give an error.</dl>
<p> NORMAL</p>
<dl>
<dd>List all regex (POSIX Extended Regular Expression syntax) that are normal output from gtar. These output are in the &quot;FAILED DUMP DETAILS&quot; section of the email report if the dump result is STRANGE or FAILED. Default values: </p>
<pre> &quot;^could not open conf file&quot;
 &quot;^Elapsed time:&quot;
 &quot;^Throughput&quot;
 &quot;: socket ignored$&quot;
 &quot;: File .* shrunk by [0-9][0-9]* bytes, padding with zeros&quot;
 &quot;: Cannot add file .*: No such file or directory$&quot;
 &quot;: Error exit delayed from previous errors&quot;</pre>
<p>To treat one of these default patterns differently, specify it explicitly in a different property.</dl>
<p> IGNORE</p>
<dl>
<dd>List all regex (POSIX Extended Regular Expression syntax) that amanda ignore. These output are never in the email report. Default values: </p>
<pre> &quot;: Directory is new$&quot;
 &quot;: Directory has been renamed&quot;</pre>
<p>To treat one of these default patterns differently, specify it explicitly in a different property.</dl>
<p> STRANGE</p>
<dl>
<dd>List all regex (POSIX Extended Regular Expression syntax) that are strange output from gtar. All gtar output that doesn&#8217;t match a normal or ignore regex are strange by default. The result of the dump is STRANGE if gtar produce a strange output. These output are in the &quot;FAILED DUMP DETAILS&quot; section of the email report.</dl>
<p> VERBOSE</p>
<dl>
<dd>Default: &quot;NO&quot;. If &quot;YES&quot;, amgtar print more verbose debugging message and can leave temporary files in AMANDA_TMPDIR.</dl>
<h2>Include And Exclude Lists</h2>
<p>This application supplies exclude lists via the <code>GNU-tar</code> <code>&#8211;exclude-from</code> option. This option accepts normal shell-style wildcard expressions, using <code>*</code> to match any number of characters and <code>?</code> to match a single character. Character classes are represented with <code>[..]</code>, which will match any of the characters in the brackets. Expressions can be &quot;anchored&quot; to the base directory of the DLE by prefixing them with &quot;./&quot;. Without this prefix, they will match at any directory level. Expressions that begin or end with a &quot;/&quot; will not match anything: to completely exclude a directory, do not include the trailing slash. Example expressions: </p>
<pre> ./temp-files # exclude top-level directory entirely
 ./temp-files/ # BAD: does nothing
 /temp-files # BAD: does nothing
 ./temp-files/* # exclude directory contents; include directory
 temp-files # exclude anything named &quot;temp-files&quot;
 generated-* # exclude anything beginning with &quot;generated-&quot;
 *.iso # exclude ISO files
 proxy/local/cache # exclude &quot;cache&quot; in dir &quot;local&quot; in &quot;proxy&quot;</pre>
<p>Similarly, include expressions are supplied to <code>GNU-tar</code>&#8216;s <code>&#8211;files-from</code> option. This option ordinarily does not accept any sort of wildcards, but amgtar &quot;manually&quot; applies glob pattern matching to include expressions with only one slash. The expressions must still begin with &quot;./&quot;, so this effectively only allows expressions like &quot;./[abc]*&quot; or &quot;./*.txt&quot;.</p>
<h2>Example</h2>
<pre> define application-tool app_amgtar {
 plugin &quot;amgtar&quot;
 property &quot;ATIME-PRESERVE&quot; &quot;NO&quot;
 property &quot;CHECK-DEVICE&quot; &quot;YES&quot;
 property &quot;GNUTAR-LISTDIR&quot; &quot;/path/to/listdir&quot;
 property &quot;GNUTAR-PATH&quot; &quot;/bin/tar&quot;
 property &quot;ONE-FILE-SYSTEM&quot; &quot;YES&quot;
 property &quot;TAR-BLOCKSIZE&quot; &quot;20&quot;
 property &quot;SPARSE&quot; &quot;YES&quot;
 property &quot;ACLS&quot; &quot;NO&quot;
 property &quot;SELINUX&quot; &quot;NO&quot;
 property &quot;XATTRS&quot; &quot;NO&quot;
 property &quot;EXIT-HANDLING&quot; &quot;1=GOOD 2=BAD&quot;
 # change a default NORMAL regex to a STRANGE regex.
 property &quot;STRANGE&quot; &quot;: socket ignored$&quot;
 # add three new IGNORE regex
 property &quot;IGNORE&quot; &quot;: Directory is new$&quot;
 property append &quot;IGNORE&quot; &quot;: Directory has been renamed&quot;
 property append &quot;IGNORE&quot; &quot;file changed as we read it$&quot;
 }</pre>
<p>A dumptype using this application might look like: </p>
<pre> define dumptype amgtar_app_dtyp {
 global
 program &quot;APPLICATION&quot;
 application &quot;app_amgtar&quot;
 }</pre>
<p>Note that the <i>program</i> parameter must be set to <i>&quot;APPLICATION&quot;</i> to use the <i>application</i> parameter.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
