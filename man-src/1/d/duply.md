---
title: "duply(1)"
name: "duply"
section: "1"
letter: "d"
url: "/docs/linux/man/1-duply/"
---

<h2>VERSION</h2>
<p> duply version 1.11.3 (<a rel="nofollow" href="http://duply.net)">http://duply.net)</a></p>
<h2>DESCRIPTION</h2>
<p> Duply deals as a wrapper for the mighty duplicity magic. It simplifies running duplicity with cron or on command line by:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> keeping recurring settings in profiles per backup job</p>
<dt>&bull;</p>
<dd> enabling batch operations eg. backup_verify+purge</p>
<dt>&bull;</p>
<dd> executing pre/post scripts (different actions possible depending on previous or next command or it&#8217;s exit status)</p>
<dt>&bull;</p>
<dd> precondition checking for flawless duplicity operation</dl>
</dl>
<p> For each backup job one configuration profile must be created. The profile folder will be stored under &#8216;~/.duply/&lt;profile&gt;&#8217; (where ~ is the current users home directory).</p>
<dl>
<dt><code>Hint:</code></p>
<dd> If the folder &#8216;/etc/duply&#8217; exists, the profiles for the super user root will be searched &amp; created there.</dl>
<h2>USAGE</h2>
<dl>
<dt><code>first time usage (profile creation):</code></p>
<dd> duply &lt;profile&gt; create</p>
<dt><code>general usage in single or batch mode (see EXAMPLES):</code></p>
<dd> duply &lt;profile&gt; &lt;command&gt;[[_|+|-]&lt;command&gt;[_|+|-]&#8230;] [&lt;options&gt; &#8230;]</dl>
<p> For batches the conditional separators can also be written as pseudo commands <code>and</code>(+), <code>or</code>(-). See SEPARATORS for details. </p>
<p> Non duply options are passed on to duplicity (see OPTIONS). All conf parameters can also be defined in the environment instead.</p>
<h2>PROFILE</h2>
<p> Indicated by a path or a profile name (&lt;profile&gt;), which is resolved to &#8216;~/.duply/&lt;profile&gt;&#8217; (~ expands to environment variable $HOME). </p>
<p> Superuser root can place profiles under &#8216;/etc/duply&#8217;. Simply create the folder manually before running duply as superuser.</p>
<dl>
<dt><code>Note:</code></p>
<dd> Already existing profiles in root&#8217;s home folder will cease to work unless they are moved to the new location manually.</p>
<dt><code>example 1:</code></p>
<dd> duply humbug backup</dl>
<p> Alternatively a _path_ might be used e.g. useful for quick testing, restoring or exotic locations. Shell expansion should work as usual.</p>
<dl>
<dt><code>Hint:</code></p>
<dd> The path must contain at least one path separator &#8216;/&#8217;, e.g. &#8216;./test&#8217; instead of only &#8216;test&#8217;.</p>
<dt><code>example 2:</code></p>
<dd> duply ~/.duply/humbug backup</dl>
<h2>SEPARATORS</h2>
<dl>
<dt><code>_ (underscore)</code></p>
<dd> neutral separator</p>
<dt><code>+ (plus sign), _and_</code></p>
<dd> conditional AND the next command will only be executed if the previous succeeded</p>
<dt><code>&#8211; (minus sign), _or_</code></p>
<dd> conditional OR the next command will only be executed if the previous failed</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>example:</code></p>
<dd> &#8216;pre+bkp-verify_post&#8217; translates to &#8216;pre_and_bkp_or_verify_post&#8217;</dl>
</dl>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>usage</code></p>
<dd> get usage help text</p>
<dt><code>and/or</code></p>
<dd> pseudo commands for better batch cmd readability (see SEPARATORS)</p>
<dt><code>create</code></p>
<dd> creates a configuration profile</p>
<dt><code>backup</code></p>
<dd> backup with pre/post script execution (batch: pre_bkp_post), full (if full_if_older matches or no earlier backup is found) incremental (in all other cases)</p>
<dt><code>pre/post</code></p>
<dd> execute &#8216;&lt;profile&gt;/pre&#8217;, &#8216;&lt;profile&gt;/post&#8217; scripts</p>
<dt><code>bkp</code></p>
<dd> as above but without executing pre/post scripts</p>
<dt><code>full</code></p>
<dd> force full backup</p>
<dt><code>incr</code></p>
<dd> force incremental backup</p>
<dt><code>list [&lt;age&gt;]</code></p>
<dd> list all files in backup (as it was at &lt;age&gt;, default: now)</p>
<dt><code>status</code></p>
<dd> prints backup sets and chains currently in repository</p>
<dt><code>verify [&lt;age&gt;] [&#8211;compare-data</code>]</p>
<dd> list files changed, since age if given</p>
<dt><code>verifyPath &lt;rel_path_in_bkp&gt; &lt;local_path&gt; [&lt;age&gt;] [&#8211;compare-data</code>]</p>
<dd> list changes of a file or folder path in backup compared to a local path, since age if given</p>
<dt><code>restore &lt;target_path&gt; [&lt;age&gt;]</code></p>
<dd> restore the complete backup to &lt;target_path&gt; [as it was at &lt;age&gt;]</p>
<dt><code>fetch &lt;src_path&gt; &lt;target_path&gt; [&lt;age&gt;]</code></p>
<dd> fetch single file/folder from backup [as it was at &lt;age&gt;]</p>
<dt><code>purge [&lt;max_age&gt;] [&#8211;force</code>]</p>
<dd> list outdated backup files (older than $MAX_AGE) [use <code>&#8211;force</code> to actually delete these files]</p>
<dt><code>purgeFull [&lt;max_full_backups&gt;] [&#8211;force</code>]</p>
<dd> list outdated backup files ($MAX_FULL_BACKUPS being the number of full backups and associated incrementals to keep, counting in reverse chronological order) [use <code>&#8211;force</code> to actually delete these files]</p>
<dt><code>purgeIncr [&lt;max_fulls_with_incrs&gt;] [&#8211;force</code>]</p>
<dd> list outdated incremental backups ($MAX_FULLS_WITH_INCRS being the number of full backups which associated incrementals will be kept, counting in reverse chronological order) [use <code>&#8211;force</code> to actually delete these files]</p>
<dt><code>cleanup [&#8211;force</code>]</p>
<dd> list broken backup chain files archives (e.g. after unfinished run) [use <code>&#8211;force</code> to actually delete these files]</p>
<dt><code>changelog</code></p>
<dd> print changelog / todo list</p>
<dt><code>txt2man</code></p>
<dd> feature for package maintainers &#8211; create a manpage based on the usage output. download txt2man from <a rel="nofollow" href="http://mvertes.free.fr/,">http://mvertes.free.fr/,</a> put it in the PATH and run &#8216;duply txt2man&#8217; to create a man page.</p>
<dt><code>version</code></p>
<dd> show version information of duply and needed programs</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;force</code></p>
<dd> passed to duplicity (see commands: purge, purge-full, cleanup)</p>
<dt><code>&#8211;preview</code></p>
<dd> do nothing but print out generated duplicity command lines</p>
<dt><code>&#8211;disable-encryption</code></p>
<dd> disable encryption, overrides profile settings</dl>
<h2>TIME FORMATS</h2>
<p> For all time related parameters like age, max_age etc. Refer to the duplicity manpage for all available formats. Here some examples: 2002-01-25T07:00:00+02:00 (full date time format string) 2002/3/5 (date string YYYY/MM/DD) 12D (interval, 12 days ago) 1h78m (interval, 1 hour 78 minutes ago)</p>
<h2>PRE POST SCRIPTS</h2>
<p> Useful internal duply variables will be readable in the scripts. Some of interest may be </p>
<pre>
    CONFDIR, SOURCE, TARGET_URL_&lt;PROT|HOSTPATH|USER|PASS&gt;, 
    GPG_&lt;KEYS_ENC|KEY_SIGN|PW&gt;, CMD_&lt;PREV|NEXT&gt;, CMD_ERR
</pre>
<p> The CMD_* variables were introduced to allow different actions according to the command the scripts were attached to e.g. &#8216;pre_bkp_post_pre_verify_post&#8217; will call the pre script two times, with CMD_NEXT variable set to &#8216;bkp&#8217; on the first and to &#8216;verify&#8217; on the second run. CMD_ERR holds the exit code of the CMD_PREV .</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>create profile &#8216;humbug&#8217;:</code></p>
<dd> duply humbug create (don&#8217;t forget to edit this new conf file)</p>
<dt><code>backup &#8216;humbug&#8217; now:</code></p>
<dd> duply humbug backup</p>
<dt><code>list available backup sets of profile &#8216;humbug&#8217;:</code></p>
<dd> duply humbug status</p>
<dt><code>list and delete outdated backups of &#8216;humbug&#8217;:</code></p>
<dd> duply humbug purge <code>&#8211;force</code></p>
<dt><code>restore latest backup of &#8216;humbug&#8217; to /mnt/restore:</code></p>
<dd> duply humbug restore /mnt/restore</p>
<dt><code>restore /etc/passwd of &#8216;humbug&#8217; from 4 days ago to /root/pw:</code></p>
<dd> duply humbug fetch etc/passwd /root/pw 4D (see &quot;duplicity manpage&quot;, section TIME FORMATS)</p>
<dt><code>a one line batch job on &#8216;humbug&#8217; for cron execution:</code></p>
<dd> duply humbug backup_verify_purge <code>&#8211;force</code></p>
<dt><code>batch job to run a full backup with pre/post scripts:</code></p>
<dd> duply humbug pre_full_post</dl>
<h2>FILES</h2>
<p> in profile folder &#8216;~/.duply/&lt;profile&gt;&#8217; or &#8216;/etc/duply&#8217;</p>
<dl>
<dt><code>conf</code></p>
<dd> profile configuration file</p>
<dt><code>pre,post</code></p>
<dd> pre/post scripts (see above for details)</p>
<dt><code>gpgkey.*.asc</code></p>
<dd> exported GPG key files</p>
<dt><code>exclude</code></p>
<dd> a globbing list of included or excluded files/folders (see &quot;duplicity manpage&quot;, section FILE SELECTION)</dl>
<h2>IMPORTANT</h2>
<p> Copy the _whole_ profile folder after the first backup to a safe place. It contains everything needed to restore your backups. You will need it if you have to restore the backup from another system (e.g. after a system crash). Keep access to these files restricted as they contain _all_ informations (gpg data, ftp data) to access and modify your backups. </p>
<p> Repeat this step after _all_ configuration changes. Some configuration options are crucial for restoration.</p>
<h2>SEE ALSO</h2>
<p> duplicity man page: <code><a href="/docs/linux/man/1-duplicity/">duplicity</a></code>(1) or <a rel="nofollow" href="http://duplicity.nongnu.org/duplicity.1.html">http://duplicity.nongnu.org/duplicity.1.html</a> </p>
<h2>Index</h2>
