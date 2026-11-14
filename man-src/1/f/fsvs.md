---
title: "fsvs(1)"
name: "fsvs"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fsvs/"
description: "FSVS – fast versioning tool"
---

<h2 class="name">NAME</h2>
<p> FSVS &#8211; fast versioning tool </p>
<h2>SYNOPSIS</h2>
<p> fsvs command [options] [args] </p>
<p> The following commands are understood by fsvs:</p>
<h2>Local configuration and information:</h2>
<dl>
<dt><code>urls</code></p>
<dd> Define working copy base directories by their URL(s)</p>
<dt><code>status</code></p>
<dd> Get a list of changed entries</p>
<dt><code>info</code></p>
<dd> Display detailed information about single entries</p>
<dt><code>log</code></p>
<dd> Fetch the log messages from the repository</p>
<dt><code>diff</code></p>
<dd> Get differences between files (local and remote)</p>
<dt><code>copyfrom-detect</code></p>
<dd> Ask fsvs about probably copied/moved/renamed entries; see <code>cp</code></dl>
<h2>Defining which entries to take:</h2>
<dl>
<dt><code>ignore</code> and <code>rign</code></p>
<dd> Define ignore patterns</p>
<dt><code>unversion</code></p>
<dd> Remove entries from versioning</p>
<dt><code>add</code></p>
<dd> Add entries that would be ignored</p>
<dt><code>cp</code>, <code>mv</code></p>
<dd> Tell fsvs that entries were copied</dl>
<h2>Commands working with the repository:</h2>
<dl>
<dt><code>commit</code></p>
<dd> Send changed data to the repository</p>
<dt><code>update</code></p>
<dd> Get updates from the repository</p>
<dt><code>checkout</code></p>
<dd> Fetch some part of the repository, and register it as working copy</p>
<dt><code>cat</code></p>
<dd> Get a file from the directory</p>
<dt>revert and uncp</p>
<dd> Undo local changes and entry markings</p>
<dt>remote-status</p>
<dd> Ask what an <code>update</code> would bring</dl>
<h2>Property handling:</h2>
<dl>
<dt><code>prop-set</code></p>
<dd> Set user-defined properties</p>
<dt><code>prop-get</code></p>
<dd> Ask value of user-defined properties</p>
<dt><code>prop-list</code></p>
<dd> Get a list of user-defined properties</dl>
<h2>Additional commands used for recovery and debugging:</h2>
<dl>
<dt><code>export</code></p>
<dd> Fetch some part of the repository</p>
<dt><code>sync-repos</code></p>
<dd> Drop local information about the entries, and fetch the current list from the repository.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Multi-url-operations are relatively new; there might be rough edges.</dl>
<p> The <code>return code</code> is 0 for success, or 2 for an error. 1 is returned if the option <code>Stopping status reports as soon as changes are found</code> is used, and changes are found; see also <code>Filtering entries</code>. </p>
<h2>Universal options</h2>
<h3>-V &#8212; show version</h3>
<p> -V makes fsvs print the version and a copyright notice, and exit. </p>
<h3>-d and -D &#8212; debugging</h3>
<p> If fsvs was compiled using &#8211;enable-debug you can enable printing of debug messages (to STDOUT) with -d. Per default all messages are printed; if you&#8217;re only interested in a subset, you can use -D <i>start-of-function-name</i>. </p>
<pre>
      fsvs -d -D waa_ status
</pre>
<p>&nbsp;<wbr>would call the&nbsp;<wbr><i>status</i>&nbsp;<wbr>action, printing all debug messages of all WAA functions &#8211; waa__init, waa__open, etc. </p>
<p> Furthermore you can specify the debug output destination with the option debug_output. This can be a simple filename (which gets truncated), or, if it starts with a |, a command that the output gets piped into. </p>
<p> If the destination cannot be opened (or none is given), debug output goes to STDOUT. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> That string is taken only once &#8211; at the first debug output line. So you have to use the correct order of parameters: -o debug_output=&#8230; -d.</dl>
<p> An example: writing the last 200 lines of debug output into a file. </p>
<pre>
   fsvs -o debug_output='| tail -200 &gt; /tmp/debug.log' -d ....
</pre>
<h3>-N, -R &#8212; recursion</h3>
<p> The -N and -R switches in effect just decrement/increment a counter; the behavious is chosen depending on that. So -N -N -N -R -R is equivalent to -N. </p>
<h3>-q, -v &#8212; verbose/quiet</h3>
<p> Like the options for recursive behaviour (-R and -N) -v and -q just inc/decrement a counter. The higher the value, the more verbose. </p>
<p>&nbsp;<wbr>Currently only the values -1&nbsp;<wbr>(quiet), 0&nbsp;<wbr>(normal), and&nbsp;<wbr>+1&nbsp;<wbr>(verbose)&nbsp;<wbr>are used. </p>
<h3>-C &#8212; checksum</h3>
<p> -C chooses to use more change detection checks; please see <code>the change_check option</code> for more details. </p>
<h3>-f &#8212; filter entries</h3>
<p> This parameter allows to do a bit of filtering of entries, or, for some operations, modification of the work done on given entries. </p>
<p> It requires a specification at the end, which can be any combination of any, text, new, deleted (or removed), meta, mtime, group, mode, changed or owner. </p>
<p> By giving eg. the value text, with a <code>status</code> action only entries that are new or changed are shown; with mtime,group only entries whose group or modification time has changed are printed. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Please see <code>Change detection</code> for some more information. </p>
<p> If an entry gets replaced with an entry of a different type (eg. a directory gets replaced by a file), that counts as deleted <code>and</code> new.</dl>
<p> If you use -v, it&#8217;s used as a any internally. </p>
<p> If you use the string none, it resets the bitmask to <code>no</code> entries shown; then you can built a new mask. So owner,none,any,none,delete would show deleted entries. If the value after all commandline parsing is none, it is reset to the default. </p>
<h3>-W warning=action &#8212; set warnings</h3>
<p> Here you can define the behaviour for certain situations that should not normally happen, but which you might encounter. </p>
<p> The general format here is <i>specification</i> = <i>action</i>, where <i>specification</i> is a string matching the start of at least one of the defined situations, and <i>action</i> is one of these:</p>
<dl>
<dt>*</p>
<dd> <i>once</i> to print only a single warning,</p>
<dt>*</p>
<dd> <i>always</i> to print a warning message <code>every</code> time,</p>
<dt>*</p>
<dd> <i>stop</i> to abort the program,</p>
<dt>*</p>
<dd> <i>ignore</i> to simply ignore this situation, or</p>
<dt>*</p>
<dd> <i>count</i> to just count the number of occurrences.</dl>
<p> If <i>specification</i> matches more than one situation, all of them are set; eg. for <i>meta=ignore</i> all of <i>meta-mtime</i>, <i>meta-user</i> etc. are ignored. </p>
<p> If at least a single warning that is <code>not</code> ignored is encountered during the program run, a list of warnings along with the number of messages it would have printed with the setting <i>always</i> is displayed, to inform the user of possible problems. </p>
<p> The following situations can be handled with this: <i>meta-mtime</i>, <i>meta-user</i>, <i>meta-group</i>, <i>meta-umask</i> These warnings are issued if a meta-data property that was fetched from the repository couldn&#8217;t be parsed. This can only happen if some other program or a user changes properties on entries. </p>
<p>&nbsp;<wbr>In this case you can use -Wmeta=always or -Wmeta=count, until the repository is clean again. </p>
<p> <i>no-urllist</i> This warning is issued if a <code>info</code> action is executed, but no URLs have been defined yet. </p>
<p> <i>charset-invalid</i> If the function <a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a>(3) couldn&#8217;t return the name of the current character encoding, a default of UTF-8 is used. You might need that for a minimal system installation, eg. on recovery. </p>
<p> <i>chmod-eperm</i>, <i>chown-eperm</i> If you update a working copy as normal user, and get to update a file which has another owner but you may modify, you&#8217;ll get errors because neither the user, group, nor mode can be set. </p>
<p> <i>chmod-other</i>, <i>chown-other</i> If you get another error than EPERM in the situation above, you might find these useful. </p>
<p> <i>overlayed-entries</i> This is not yet used. </p>
<p> <i>mixed-rev-wc</i> If you specify some revision number on a <code>revert</code>, it will complain that mixed-revision working copies are not allowed. By using this specification you cannot enable mixed-revision working copies, of course, but you can avoid getting told every time. </p>
<p> <i>propname-reserved</i> It is normally not allowed to set a property with the <code>prop-set</code> action with a name matching some reserved prefixes. </p>
<p>&nbsp;<wbr><i>ignpat-wcbase</i>&nbsp;<wbr>This warning is issued if an&nbsp;<wbr><code>absolute ignore&nbsp;<wbr></code>&nbsp;<wbr>pattern&#8217;&nbsp;<wbr>does not match the working copy base directory. </p>
<p> <i>diff-status</i> GNU diff has defined that it returns an exit code 2 in case of an error; sadly it returns that also for binary files, so that a simply fsvs diff some-binary-file text-file would abort without printing the diff for the second file. So the exit status of diff is per default ignored, but can be used by setting this option to eg. <i>stop</i>. </p>
<p> Also an environment variable FSVS_WARNINGS is used and parsed; it is simply a whitespace-separated list of option specifications. </p>
<h3>-u URLname[@revision[:revision]] &#8212; select URLs</h3>
<p> Some commands can be reduced to a subset of defined URLs; the <code>update</code> command is a example. </p>
<p> If you have more than a single URL in use for your working copy, update normally updates <code>all</code> entries from <code>all</code> URLs. By using this parameter you can tell FSVS to update only the specified URLs. </p>
<p> The parameter can be used repeatedly; the value can have multiple URLs, separated by whitespace or one of &#8216;,;&#8217;. </p>
<pre>
   fsvs up -u base_install,boot@32 -u gcc
</pre>
<p> This would get HEAD of base_install and gcc, and set the target revision of the boot URL at 32. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The second revision specification will be used for eg. the <code>diff</code> command; but this is not yet implemented.</dl>
<h3>-o [name[=value]] &#8212; other options</h3>
<p> This is used for setting some seldom used option, for which default can be set in a configuration file (to be implemented, currently only command-line). </p>
<p> For a list of these please see <code>Further options for FSVS.</code>. </p>
<h2>add</h2>
<pre>
 fsvs add PATH [PATH...]
</pre>
<p> With this command you can explicitly define entries to be versioned, even if they have a matching ignore pattern. They will be sent to the repository on the next commit, just like other new entries, and will therefore be reported as <i>New</i> . </p>
<h3>Example</h3>
<p> Say, you&#8217;re versioning your home directory, and gave an ignore pattern of ./.* to ignore all .* entries in your home-directory. Now you want .bashrc, .ssh/config, and your complete .kde3-tree saved, just like other data. </p>
<p> So you tell fsvs to not ignore these entries: </p>
<pre>
    fsvs add .bashrc .ssh/config .kde3
</pre>
<p>&nbsp;<wbr>Now the entries below .kde3 would match your earlier ./.*&nbsp;<wbr>pattern&nbsp;<wbr>(as a match at the beginning is sufficient), so you have to insert a negative ignore pattern&nbsp;<wbr>(a&nbsp;<wbr><i>take</i>&nbsp;<wbr>pattern):&nbsp;<wbr> </p>
<pre>
    fsvs ignore --insert t./.kde3
</pre>
<p>&nbsp;<wbr>Now a fsvs st would show your entries as&nbsp;<wbr><i>New</i>&nbsp;<wbr>, and the next commit will send them to the repository. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This loads the wc data, writes the given paths with some flags to it, and saves the wc data again.</dl>
<h2>unversion</h2>
<pre>
 fsvs unversion PATH [PATH...]
</pre>
<p> This command flags the given paths locally as removed. On the next commit they will be deleted in the repository, and the local information of them will be removed, but not the entries themselves. So they will show up as <i>New</i> again, and you get another chance at ignoring them. </p>
<h3>Example</h3>
<p> Say, you&#8217;re versioning your home directory, and found that you no longer want .bash_history and .sh_history versioned. So you do </p>
<pre>
    fsvs unversion .bash_history .sh_history
</pre>
<p>&nbsp;<wbr>and these files will be reported as d&nbsp;<wbr>(will be deleted, but only in the repository). </p>
<p> Then you do a </p>
<pre>
    fsvs commit
</pre>
<p> Now fsvs would report these files as New , as it does no longer know anything about them; but that can be cured by </p>
<pre>
    fsvs ignore './.*sh_history'
</pre>
<p>&nbsp;<wbr>Now these two files won&#8217;t be shown as&nbsp;<wbr><i>New</i>&nbsp;<wbr>, either. </p>
<p> The example also shows why the given paths are not just entered as separate ignore patterns &#8211; they are just single cases of a (probably) much broader pattern. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> If you didn&#8217;t use some kind of escaping for the pattern, the shell would expand it to the actual filenames, which is (normally) not what you want.</dl>
<h2>_build_new_list</h2>
<p> This is used mainly for debugging. It traverses the filesystem and build a new entries file. In production it should not be used &#8211; as the revision of the entries is unknown, we can only use 0 &#8211; and loose information this way! </p>
<h2>delay</h2>
<p> This command delays execution until the time has passed at least to the next second after writing the <code>dir</code> and <code>urls</code> files. So, where previously the <code>delay</code> option was used, this can be substituted by the given command followed by the delay command. </p>
<p> The advantage is over the <code>Waiting for a time change after working copy operations</code> option is, that read-only commands can be used in the meantime. </p>
<p> An example: </p>
<pre>
   fsvs commit /etc/X11 -m 'Backup of X11'
   ... read-only commands, like 'status'
   fsvs delay /etc/X11
   ... read-write commands, like 'commit'
</pre>
<p> In the testing framework it is used to save a bit of time; in normal operation, where fsvs commands are not so tightly packed, it is normally preferable to use the <code>delay</code> option. </p>
<h2>cat</h2>
<pre>
 fsvs cat [-r rev] path
</pre>
<p> Fetches a file with the specified revision or, if not given, BASE, from the repository, and outputs it to STDOUT. </p>
<h2>checkout</h2>
<pre><code>
fsvs checkout[path] URL[URLs...]
</code></pre>
<p> Sets one or more URLs for the current working directory (or the directory path), and does an <code>checkout</code> of these URLs. </p>
<p> Example: </p>
<pre>
 fsvs checkout . <a rel="nofollow" href="http://svn/repos/installation/machine-1/trunk">http://svn/repos/installation/machine-1/trunk</a>
</pre>
<p> The distinction whether a directory is given or not is done based on the result of URL-parsing &#8212; if it looks like an URL, it is used as an URL. </p>
<p>&nbsp;<wbr>Please mind that at most a single path is allowed;&nbsp;<wbr>as soon as two non-URLs are found an error message is printed. </p>
<p> If no directory is given, . is used; this differs from the usual subversion usage, but might be better suited for usage as a recovery tool (where versioning / is common). Opinions welcome. </p>
<p> The given path must exist, and <code>should</code> be empty &#8212; fsvs will abort on conflicts, ie. if files that should be created already exist. </p>
<p>&nbsp;<wbr>If there&#8217;s a need to create that directory, please say so;&nbsp;<wbr>patches for some parameter like -p are welcome. </p>
<p> For a format definition of the URLs please see the chapter <code>Format of URLs</code> and the <code>urls</code> and <code>update</code> commands. </p>
<p> Furthermore you might be interested in <code>Using an alternate root directory</code> and <code>Recovery for a non-booting system</code>. </p>
<h2>commit</h2>
<p>fsvs commit[-m &#8216;message&#8217; | -F filename][-v][-C[-C]][PATH[PATH&#8230;]]</p>
<p> Commits the current state into the repository. It is possible to commit only parts of a working copy into the repository. </p>
<p> Your working copy is /etc , and you&#8217;ve set it up and committed already. Now you&#8217;ve changed /etc/hosts , and /etc/inittab . Since these are non-related changes, you&#8217;d like them to be in separate commits. </p>
<p> So you simply run these commands: </p>
<pre>
 fsvs commit -m 'Added some host' /etc/hosts
 fsvs commit -m 'Tweaked default runlevel' /etc/inittab
</pre>
<p> If you&#8217;re currently in /etc , you can even drop the /etc/ in front, and just use the filenames. </p>
<p> Please see <code>status</code> for explanations on -v and -C . For advanced backup usage see also <code>FSVS_PROP_COMMIT_PIPE</code>. </p>
<h2>cp</h2>
<pre>
 fsvs cp [-r rev] SRC DEST
 fsvs cp dump
 fsvs cp load
</pre>
<p> The copy command marks DEST as a copy of SRC at revision rev, so that on the next commit of DEST the corresponding source path is sent as copy source. </p>
<p> The default value for rev is BASE, ie. the revision the SRC (locally) is at. </p>
<p> Please note that this command works <code>always</code> on a directory <code>structure</code> &#8211; if you say to copy a directory, the <code>whole</code> structure is marked as copy. That means that if some entries below the copy are missing, they are reported as removed from the copy on the next commit. </p>
<p>&nbsp;<wbr>(Of course it is possible to mark files as copied, too;&nbsp;<wbr>non-recursive copies are not possible.) </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Or TODO: There will be differences in the exact usage &#8211; copy will try to run the cp command, whereas copied will just remember the relation.</dl>
<p> If this command are used without parameters, the currently defined relations are printed; please keep in mind that the <code>key</code> is the destination name, ie. the 2nd line of each pair! </p>
<p> The input format for load is newline-separated &#8211; first a SRC line, followed by a DEST line, then an line with just a dot (&#8216;.&#8217;) as delimiter. If you&#8217;ve got filenames with newlines or other special characters, you have to give the paths as arguments. </p>
<p> Internally the paths are stored relative to the working copy base directory, and they&#8217;re printed that way, too. </p>
<p> Later definitions are <code>appended</code> to the internal database; to undo mistakes, use the <code>revert</code> action. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> <code>Important:</code> User-defined properties like <code>fsvs:commit-pipe</code> are <code>not</code> copied to the destinations, because of space/time issues (traversing through entire subtrees, copying a lot of property-files) and because it&#8217;s not sure that this is really wanted. <code>TODO:</code> option for copying properties? </p>
<p> As subversion currently treats a rename as copy+delete, the <code>mv</code> command is an alias to <code>cp</code>.</dl>
<p> If you have a need to give the filenames dump or load as first parameter for copyfrom relations, give some path, too, as in ./dump. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The source is internally stored as URL with revision number, because else an operation like </p>
<pre>
   $ fsvs cp a b
   $ rm a/1
   $ fsvs ci a
   $ fsvs ci b
</pre>
<p>&nbsp;<wbr>would fail &#8211; FSVS would send the wrong&nbsp;<wbr>(too recent!)&nbsp;<wbr>revision number as source, and so the local filelist would get inconsistent with the repository.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>But it is not implementd to give an URL as copyfrom source directly &#8211; we&#8217;d have to fetch a list&nbsp;<wbr>(and possibly the data!)&nbsp;<wbr>from the repository.</dl>
<h2>copyfrom-detect</h2>
<pre>
 fsvs copyfrom-detect [paths...]
</pre>
<p> This command tells fsvs to look through the new entries, and see whether it can find some that seem to be copied from others already known. </p>
<p>&nbsp;<wbr>It will output a list with source and destination path and why it could match. </p>
<p> This is just for information purposes and doesn&#8217;t change any FSVS state, <i>unless some option/parameter is set. (TODO)</i> </p>
<p> The list format is <code>on purpose</code> incompatible with the load syntax, as the best match normally has to be taken manually. </p>
<p> If <code>verbose</code> is used, an additional value giving the percentage of matching blocks, and the count of possibly copied entries is printed. </p>
<p> Example: </p>
<pre>
   $ fsvs copyfrom-list -v
   newfile1
     md5:oldfileA
   newfile2
     md5:oldfileB
     md5:oldfileC
     md5:oldfileD
   newfile3
     inode:oldfileI
     manber=82.6:oldfileF
     manber=74.2:oldfileG
     manber=53.3:oldfileH
     ...
   3 copyfrom relations found.
</pre>
<p> The abbreviations are: <i>md5</i> The <code>MD5</code> of the new file is identical to that of one or more already committed files; there is no percentage. </p>
<p> <i>inode</i> The <code>device/inode</code> number is identical to the given known entry; this could mean that the old entry has been renamed or hardlinked. <code>Note:</code> Not all filesystems have persistent inode numbers (eg. NFS) &#8211; so depending on your filesystems this might not be a good indicator! </p>
<p> <i>name</i> The entry has the same name as another entry. </p>
<p> <i>manber</i> Analysing files of similar size shows some percentage of (variable-sized) <code>common blocks</code> (ignoring the order of the blocks). </p>
<p> <i>dirlist</i> The new directory has similar files to the old directory. </p>
<p>&nbsp;<wbr>The percentage is&nbsp;<wbr>(number_of_common_entries)/(files_in_dir1&nbsp;<wbr>+&nbsp;<wbr>files_in_dir2 &#8211; number_of_common_entries). </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Only <code>md5</code>, <code>name</code> and <code>inode</code> matching currently done. </p>
<p> If too many possible matches are found, not all may be printed; only the indicator &#8230; is shown at the end.</dl>
<h2>uncp</h2>
<pre>
 fsvs uncopy DEST [DEST ...]
</pre>
<p> The uncopy command removes a copyfrom mark from the destination entry. This will make the entry unknown again, and reported as New on the next invocations. </p>
<p> Only the base of a copy can be un-copied; if a directory structure was copied, and the given entry is just implicitly copied, this command will give you an error. </p>
<p> This is not folded in <code>revert</code>, because it&#8217;s not clear whether revert should restore the original copyfrom data or remove the copy attribute; by using a special command this is no longer ambiguous. </p>
<p> Example: </p>
<pre>
   $ fsvs copy SourceFile DestFile
   # Whoops, was wrong!
   $ fsvs uncopy DestFile
</pre>
<h2>diff</h2>
<p>fsvs diff[-v][-r rev[:rev2]][-R] PATH[PATH&#8230;]</p>
<p> This command gives you diffs between local and repository files. </p>
<p> With -v the meta-data is additionally printed, and changes shown. </p>
<p> If you don&#8217;t give the revision arguments, you get a diff of the base revision in the repository (the last commit) against your current local file. With one revision, you diff this repository version against you local file. With both revisions given, the difference between these repository versions is calculated. </p>
<p> You&#8217;ll need the diff program, as the files are simply passed as parameters to it. </p>
<p> The default is to do non-recursive diffs; so fsvs diff . will output the changes in all files <code>in the current directory</code>. </p>
<p> The output for non-files is not defined. </p>
<p> For entries marked as copy the diff against the (clean) source entry is printed. </p>
<p> Please see also <code>Options relating to the &#8216;diff&#8217; action</code> and <code>Using colordiff</code>. </p>
<h2>export</h2>
<pre>
 fsvs export REPOS_URL [-r rev]
</pre>
<p> If you want to export a directory from your repository <code>without</code> having to have an WAA-area, you can use this command. This restores all meta-data &#8211; owner, group, access mask and modification time. Its primary use is for data recovery. </p>
<p> The data gets written (in the correct directory structure) below the current working directory; if entries already exist, the export will stop, so this should be an empty directory. </p>
<h2>help</h2>
<pre>
 help [command]
</pre>
<p> This command shows general or specific <code>help</code> (for the given command). A similar function is available by using -h or -? after a command. </p>
<h2>ignore</h2>
<p>fsvs ignore dump | load<br />
                       fsvs ignore[prepend | append | at = n] pattern[pattern&#8230;]</p>
<p> This command adds patterns to the end of the ignore list, or, with <i>prepend</i> , puts them at the beginning of the list. With at=x the patterns are inserted at the position x , counting from 0. </p>
<p> fsvs dump prints the patterns to STDOUT . If there are special characters like CR or LF embedded in the pattern <code>without encoding</code> (like  or 
), the output will be garbled. </p>
<p> The patterns may include * and ? as wildcards in one directory level, or ** for arbitrary strings. </p>
<p> These patterns are only matched against new files; entries that are already versioned are not invalidated. If the given path matches a new directory, entries below aren&#8217;t found, either; but if this directory or entries below are already versioned, the pattern doesn&#8217;t work, as the match is restricted to the directory. </p>
<p> So: </p>
<pre>
     fsvs ignore ./tmp
</pre>
<p>&nbsp;<wbr>ignores the directory tmp;&nbsp;<wbr>but if it has already been committed, existing entries would have to be unmarked with&nbsp;<wbr><code>fsvs unversion</code>. Normally it&#8217;s better to use&nbsp;<wbr> </p>
<pre>
     fsvs ignore ./tmp/**
</pre>
<p>&nbsp;<wbr>as that takes the directory itself&nbsp;<wbr>(which might be needed after restore as a mount point), but ignore&nbsp;<wbr><code>all</code>&nbsp;<wbr>entries below. </p>
<p> Other special variants are available, see the documentation <code>Using ignore patterns</code> . </p>
<p> Examples: </p>
<pre>
     fsvs ignore ./proc
     fsvs ignore ./dev/pts
     fsvs ignore './var/log/*-*'
     fsvs ignore './**~'
     fsvs ignore './**/*.bak'
     fsvs ignore prepend 't./**.txt'
     fsvs ignore append 't./**.svg'
     fsvs ignore at=1 './**.tmp'
     fsvs ignore dump
     fsvs ignore dump -v
     echo './**.doc' | fsvs ignore load
</pre>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Please take care that your wildcard patterns are not expanded by the shell!</dl>
<h2>rign</h2>
<p>fsvs rel &#8211; ignore[prepend | append | at = n] path &#8211; spec[path &#8211; spec&#8230;] fsvs ri[prepend | append | at = n] path &#8211; spec[path &#8211; spec&#8230;]</p>
<p> If you use more than a single working copy for the same data, it will be stored in different paths &#8211; and that makes absolute ignore patterns infeasible. But relative ignore patterns are anchored at the beginning of the WC root &#8211; which is a bit tiring if you&#8217;re deep in your WC hierarchy and want to ignore some files. </p>
<p> To make that easier you can use the rel-ignore (abbreviated as ri) command; this converts all given path-specifications (that may include wildcards as per the shell pattern specification above) to WC-relative values before storing them. </p>
<p> Example for /etc as working copy root: </p>
<pre>
        fsvs rel-ignore '/etc/X11/xorg.conf.*'
 
        cd /etc/X11
        fsvs rel-ignore 'xorg.conf.*'
</pre>
<p>&nbsp;<wbr>Both commands would store the pattern&nbsp;<wbr>&#8216;./X11/xorg.conf.*&#8217;. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This works only for <code>shell patterns</code>.</dl>
<p> For more details about ignoring files please see the <code>ignore</code> command and <code>Using ignore patterns</code>. </p>
<h2>info</h2>
<p>fsvs info[-R[-R]][PATH&#8230;]</p>
<p> Use this command to show information regarding one or more entries in your working copy. Currently you must be at the working copy root; but that will change. You can use -v to obtain slightly more information. </p>
<p> This may sometimes be helpful for locating bugs, or to obtain the URL and revision a working copy is currently at. </p>
<p> Example: </p>
<pre>
     $ fsvs info
     URL: file:
     ....       200  .
             Type:           directory
             Status:         0x0
             Flags:          0x100000
             Dev:            0
             Inode:          24521
             Mode:           040755
             UID/GID:        1000/1000
             MTime:          Thu Aug 17 16:34:24 2006
             CTime:          Thu Aug 17 16:34:24 2006
             Revision:       4
             Size:           200
</pre>
<p> The default is to print information about the given entry only. With a single -R you&#8217;ll get this data about <code>all</code> entries of a given directory; with a second -R you&#8217;ll get the whole (sub-)tree. </p>
<h2>log</h2>
<p>fsvs log[-v][-r rev1[:rev2]][path]</p>
<p> This command views the log information associated with the given <i>path</i>, or, if none, the highest priority URL. </p>
<p> The optional <i>rev1</i> and <i>rev2</i> can be used to restrict the revisions that are shown; if no values are given, the logs are given starting from HEAD downwards, and then a limit on the number of revisions is applied (but see the <code>limit</code> option). </p>
<p> If you use the <code>-v</code> -option, you get the files changed in each revision printed, too. </p>
<p> There is an option controlling the output format; see <code>&#8216;fsvs log&#8217; output format</code>. </p>
<p> TODOs:</p>
<dl>
<dt>*</p>
<dd> &#8211;stop-on-copy</p>
<dt>*</p>
<dd> Show revision for <code>all</code> URLs associated with a working copy? In which order?</p>
<dt>*</p>
<dd> A URL-parameter, to specify the log URL. (Name)</dl>
<h2>prop-get</h2>
<pre>
 fsvs prop-get PROPERTY-NAME PATH...
</pre>
<p> You get the data of the property printed to STDOUT. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Be careful! This command will dump the property <code>as it is</code>, ie. with any special characters! If there are escape sequences or binary data in the property, your terminal might get messed up! </p>
<p>&nbsp;<wbr>If you want a safe way to look at the properties, use prop-list with the -v parameter.</dl>
<h2>prop-set</h2>
<pre>
 fsvs prop-set PROPERTY-NAME VALUE PATH...
</pre>
<p> This command sets an arbitrary property value for the given path(s). </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Some property prefixes are reserved; currently everything starting with svn: throws a (fatal) warning, and fsvs: is already used, too. See <code>Special property names</code>.</dl>
<h2>prop-del</h2>
<pre>
 fsvs prop-del PROPERTY-NAME PATH...
</pre>
<p> This command removes property value for the given path(s). </p>
<p> See also <code>prop-set</code>. </p>
<h2>prop-list</h2>
<pre>
 fsvs prop-list [-v] PATH...
</pre>
<p> Lists the names of all properties for the given entry. With -v, the value is printed as well; special characters will be translated, to not mess with your terminal. </p>
<p> If you need raw output, post a patch for &#8211;raw, or loop with <code>prop-get</code>. </p>
<h2>remote-status</h2>
<pre>
 fsvs remote-status PATH [-r rev]
</pre>
<p> This command looks into the repository and tells you which files would get changed on an <code>update</code> &#8211; it&#8217;s a dry-run for <code>update</code> . </p>
<p> Per default it compares to HEAD, but you can choose another revision with the -r parameter. </p>
<h2>resolve</h2>
<pre>
 fsvs resolve PATH [PATH...]
</pre>
<p> When FSVS tries to update local files which have been changed, a conflict might occur. (For various ways of handling these please see the <code>conflict</code> option.) </p>
<p> This command lets you mark such conflicts as resolved. </p>
<h2>revert</h2>
<p>fsvs revert[-rRev][-R] PATH[PATH&#8230;]</p>
<p> This command undoes local modifications:</p>
<dl>
<dt>*</p>
<dd> An entry that is marked to be unversioned gets this flag removed.</p>
<dt>*</p>
<dd> For a already versioned entry (existing in the repository), the local entry is replaced with its repository version, and its status and flags are cleared.</p>
<dt>*</p>
<dd> An entry that is a copy destination, but modified, gets reverted to the copy source data.</p>
<dt>*</p>
<dd> An unmodified direct copy destination entry, and other uncommitted entries with special flags (manually added, or defined as copied), are changed back to <i>&#8216;N&#8217;</i>ew &#8212; the copy definition and the special status is removed. </p>
<p>&nbsp;<wbr>Please note that on implicitly copied entries&nbsp;<wbr>(entries that are marked as copied because some parent directory is the base of a copy)&nbsp;<wbr><code>cannot</code>&nbsp;<wbr>be un-copied;&nbsp;<wbr>they can only be reverted to their original&nbsp;<wbr>(copied-from)&nbsp;<wbr>data, or removed.</dl>
<p> See also <code>HOWTO: Understand the entries&#8217; statii</code>. </p>
<p> If a directory is given on the command line <code>all known entries in this directory</code> are reverted to the old state; this behaviour can be modified with <code>-R/-N</code>, or see below. </p>
<p> The reverted entries are printed, along with the status they had <code>before</code> the revert (because the new status is per definition <i>unchanged</i>). </p>
<p> If a revision is given, the entries&#8217; data is taken from this revision; furthermore, the <code>new</code> status of that entry is shown. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Please note that mixed revision working copies are not possible; the <i>BASE</i> revision is not changed, and a simple revert without a revision arguments gives you that.</dl>
<h3>Difference to update</h3>
<p> If you find that something doesn&#8217;t work as it should, you can revert entries until you are satisfied, and directly <code>commit</code> the new state. </p>
<p> In contrast, if you <code>update</code> to an older version, you</p>
<dl>
<dt>*</p>
<dd> cannot choose single entries (no mixed revision working copies),</p>
<dt>*</p>
<dd> and you cannot commit the old version with changes, as later changes will create conflicts in the repository.</dl>
<h3>Currently only known entries are handled.</h3>
<p> If you need a switch (like &#8211;delete in <a href="/docs/linux/man/1-rsync/">rsync</a>(1) ) to remove unknown (new, not yet versioned) entries, to get the directory in the exact state it is in the repository, say so. </p>
<h3>If a path is specified whose parent is missing, 
