---
title: "fsvs-options(5)"
name: "fsvs-options"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fsvs-options/"
description: "Further options for FSVS. – FSVS understands some other options, that modify its behaviour."
---

<p>Further options for FSVS. &#8211; FSVS understands some other options, that modify its behaviour.</p>
<h2>Short list of options</h2>
<p>FSVS currently knows: </p>
<dl>
<dt>*</p>
<dd>all_removed &#8211; <code>Trimming the list of deleted entries</code></p>
<dt>*</p>
<dd>author &#8211; <code>Author</code></p>
<dt>*</p>
<dd>change_check &#8211; <code>Change detection</code></p>
<dt>*</p>
<dd>colordiff &#8211; <code>Using colordiff</code></p>
<dt>*</p>
<dd>commit_to &#8211; <code>Destination URL for commit</code></p>
<dt>*</p>
<dd>conflict &#8211; <code>How to resolve conflicts on update</code></p>
<dt>*</p>
<dd>conf &#8211; <code>Path definitions for the config and WAA area</code>.</p>
<dt>*</p>
<dd>config_dir &#8211; <code>Configuration directory for the subversion libraries</code>.</p>
<dt>*</p>
<dd>copyfrom_exp &#8211; <code>Avoiding expensive compares on copyfrom-detect</code></p>
<dt>*</p>
<dd>debug_output &#8211; <code>Destination for debug output</code></p>
<dt>*</p>
<dd>delay &#8211; <code>Waiting for a time change after working copy operations</code></p>
<dt>*</p>
<dd>diff_prg, diff_opt, diff_extra &#8211; <code>Options relating to the &#8216;diff&#8217; action</code></p>
<dt>*</p>
<dd>dir_sort &#8211; <code>Directory sorting</code></p>
<dt>*</p>
<dd>empty_commit &#8211; <code>Doing empty commits</code></p>
<dt>*</p>
<dd>filter &#8211; <code>Filtering entries</code>, but see <code>-f</code>.</p>
<dt>*</p>
<dd>limit &#8211; <code>&#8216;fsvs log&#8217; revision limit</code></p>
<dt>*</p>
<dd>log_output &#8211; <code>&#8216;fsvs log&#8217; output format</code></p>
<dt>*</p>
<dd>merge_prg, merge_opt &#8211; <code>Options regarding the &#8216;merge&#8217; programm</code></p>
<dt>*</p>
<dd>path &#8211; <code>Displaying paths</code></p>
<dt>*</p>
<dd>softroot &#8211; <code>Using an alternate root directory</code></p>
<dt>*</p>
<dd>stat_color &#8211; <code>Status output coloring</code></p>
<dt>*</p>
<dd>stop_on_change &#8211; <code>Stopping status reports as soon as changes are found</code></p>
<dt>*</p>
<dd>warning &#8211; <code>Setting warning behaviour</code>, but see <code>-W</code>.</p>
<dt>*</p>
<dd>waa &#8211; <code>o_waa</code>.</dl>
<h2>Priorities for option setting</h2>
<p>The priorities are </p>
<dl>
<dt>*</p>
<dd>Command line <i></i>(highest)</p>
<dt>*</p>
<dd>Environment variables. These are named as FSVS_<i>{upper-case option name}</i>.</p>
<dt>*</p>
<dd>$HOME/.fsvs/wc-dir/config</p>
<dt>*</p>
<dd>$FSVS_CONF/wc-dir/config</p>
<dt>*</p>
<dd>$HOME/.fsvs/config</p>
<dt>*</p>
<dd>$FSVS_CONF/config</p>
<dt>*</p>
<dd>Default value, compiled in <i></i>(lowest)</dl>
<p> <code>Note:</code></p>
<dl>
<dd>The $HOME-dependent configuration files are not implemented currently. Volunteers?</dl>
<p> Furthermore there are &#8216;intelligent&#8217; run-time dependent settings, like turning off colour output when the output is redirected. Their priority is just below the command line &#8211; so they can always be overridden if necessary.</p>
<h2>Examples</h2>
<p>Using the commandline: </p>
<pre> fsvs -o path=environment
 fsvs -opath=environment</pre>
<p>&nbsp;<wbr>Using environment variables:&nbsp;<wbr> </p>
<pre> FSVS_PATH=absolute fsvs st</pre>
<p>&nbsp;<wbr>A configuration file:&nbsp;<wbr> </p>
<pre> # FSVS configuration file
 path=wcroot</pre>
<h2>Displaying paths</h2>
<p>You can specify how paths printed by FSVS should look like; this is used for the entry status output of the various actions, and for the diff header lines. </p>
<p> There are several possible settings, of which one can be chosen via the path option. </p>
<dl>
<dt>*</p>
<dd>&nbsp;<wbr>wcroot&nbsp;<wbr> </p>
<p>&nbsp;<wbr>This is the old, traditional FSVS setting, where all paths are printed relative to the working copy root.</dl>
<dl>
<dt>*</p>
<dd>&nbsp;<wbr>parameter&nbsp;<wbr> </p>
<p>&nbsp;<wbr>With this setting FSVS works like most other programs &#8211; it uses the first best-matching parameter given by the user, and appends the rest of the path. </p>
<p>&nbsp;<wbr>This is the new default.&nbsp;<wbr></dl>
<p> <code>Note:</code></p>
<dl>
<dd>Internally FSVS still first parses all arguments, and then does a single run through the entries. So if some entry matches more than one parameter, it is printed using the first.
</dl>
<dl>
<dt>*</p>
<dd>&nbsp;<wbr>absolute&nbsp;<wbr> </p>
<p>&nbsp;<wbr>All paths are printed in absolute form. This is useful if you want to paste them into other consoles without worrying whether the current directory matches.&nbsp;<wbr></dl>
<p> The next two are nearly identical to absolute, but the beginning of paths are substituted by environment variables. This makes sense if you want the advantage of full paths, but have some of them abbreviated. </p>
<dl>
<dt>*</p>
<dd>&nbsp;<wbr>environment&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Match variables to directories after reading the known entries, and use this cached information. This is faster, but might miss the best case if new entries are found&nbsp;<wbr>(which would not be checked against possible longer hits).&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Furthermore, as this works via associating environment variables to entries, the environment variables must at least match the working copy base &#8211; shorter paths won&#8217;t be substituted.&nbsp;<wbr></p>
<dt>*</p>
<dd>full-environment </p>
<p>&nbsp;<wbr>Check for matches just before printing the path.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>This is slower, but find the best fit.&nbsp;<wbr></dl>
<p> <code>Note:</code></p>
<dl>
<dd>The string of the environment variables must match a directory name; the filename is always printed literally, and partial string matches are not allowed. Feedback wanted. </p>
<p> Only environment variables whose names start with WC are used for substitution, to avoid using variables like $PWD, $OLDPWD, $HOME and similar which might differ between sessions. Maybe the allowed prefixes for the environment variables should be settable in the configuration. Opinions to the users mailing list, please.</dl>
<p> Example, with / as working copy base: </p>
<pre>$ cd /etc
$ fsvs -o path=wcroot st
$ fsvs -o path=absolute st
$ fsvs -o path=parameters st
$ fsvs -o path=parameters st .
$ fsvs -o path=parameters st /
$ fsvs -o path=parameters st X11
$ fsvs -o path=parameters st ../dev/..
$ fsvs -o path=parameters st X11 ../etc
$ fsvs -o path=parameters st ../etc X11
$ fsvs -o path=environ st
$ WCBAR=/etc fsvs -o path=wcroot st
$ WCBAR=/etc fsvs -o path=wcroot st /
$ WCBAR=/e fsvs -o path=wcroot st
$ WCBAR=/etc WCFOO=/etc/X11 fsvs -o path=wcroot st
$ touch /etc/X11/xinit/xinitrc
$ fsvs -o path=parameters st
$ fsvs -o path=parameters st X11 /etc/X11/xinit</pre>
<p><code>Note:</code></p>
<dl>
<dd>At least for the command line options the strings can be abbreviated, as long as they&#8217;re still identifiable. Please use the full strings in the configuration file, to avoid having problems in future versions when more options are available.</dl>
<h2>Options relating to the &#8216;diff&#8217; action</h2>
<p>The diff is not done internally in FSVS, but some other program is called, to get the highest flexibility. </p>
<p> There are several option values: </p>
<dl>
<dt>*</p>
<dd>diff_prg: The executable name, default &#8216;diff&#8217;.</p>
<dt>*</p>
<dd>diff_opt: The default options, default &#8216;-pu&#8217;.</p>
<dt>*</p>
<dd>diff_extra: Extra options, no default.</dl>
<p> The call is done as </p>
<pre> $diff_prg $diff_opt $file1 --label '$label1' $file2 --label '$label2' diff_extra</pre>
<p><code>Note:</code></p>
<dl>
<dd>In diff_opt you should use only use command line flags without parameters; in diff_extra you can encode a single flag with parameter (like &#8216;-U5&#8217;). If you need more flexibility, write a shell script and pass its name as diff_prg.</dl>
<p> Very advanced users might be interested in <code>exported environment</code>variables&#8217;, too.</p>
<h2>Using colordiff</h2>
<p>If you have colordiff installed on your system, you might be interested in the colordiff option. </p>
<p> It can take on of these values: </p>
<dl>
<dt>*</p>
<dd>no, off or false: Don&#8217;t use colordiff.</p>
<dt>*</p>
<dd>empty (default value): Try to use colordiff as executable, but don&#8217;t throw an error if it can&#8217;t be started; just pipe the data as-is to STDOUT.</p>
<dt>*</p>
<dd>anything else: Pipe the output of the diff program (see <code>Options relating to the &#8216;diff&#8217; action</code>) to the given executable.</dl>
<p> Please note that if STDOUT is not a tty (eg. is redirected into a file), this option must be given on the command line to take effect.</p>
<h2>Filtering entries</h2>
<p>Please see the command line parameter for <code>-f</code>, which is identical. </p>
<pre> fsvs -o filter=mtime</pre>
<h2>Trimming the list of deleted entries</h2>
<p>If you remove a directory, all entries below are implicitly known to be deleted, too. To make the <code>status</code> output shorter there&#8217;s the all_removed option; which, if set to yes, will cause children of removed entries to be omitted. </p>
<p> Example for the config file: </p>
<pre> all_removed=yes</pre>
<h2>Change detection</h2>
<p>This options allows to specify the trade-off between speed and accuracy. </p>
<p> A file with a changed size can immediately be known as changed; but if only the modification time is changed, this is not so easy. Per default FSVS does a MD5 check on the file in this case; if you don&#8217;t want that, or if you want to do the checksum calculation for <code>every</code> file (in case a file has changed, but its mtime not), you can use this option to change FSVS&#8217; behaviour. </p>
<p> On the command line there&#8217;s a shortcut for that: for every &#8216;-C&#8217; another check in this option is chosen. </p>
<p> The recognized specifications are noneResets the check bitmask to &#8216;no checks&#8217;. file_mtimeCheck files for modifications via MD5 if the mtime is different &#8211; default dirCheck all directories for new entries &#8211; this happens normally if a directory ha allfilesCheck <code>all</code> files with MD5 for changes (tripwire -like operation). fullAll available checks. </p>
<p> You can give multiple options; they&#8217;re accumulated unless overridden by none. </p>
<pre> fsvs -o change_check=allfiles status</pre>
<p><code>Note:</code></p>
<dl>
<dd><i>commit</i> and <i>update</i> set additionally the dir option, to avoid missing new files.</dl>
<h2>Setting warning behaviour</h2>
<p>Please see the command line parameter <code>-W</code>, which is identical. </p>
<pre> fsvs -o warning=diff-status=ignore</pre>
<h2>Using an alternate root directory</h2>
<p>This is a path that is prepended to $FSVS_WAA and $FSVS_CONF (or their default values, see <code>Files used by fsvs</code>), if they do not already start with it, and it is cut off for the directory-name MD5 calculation. </p>
<p> When is that needed? Imagine that you&#8217;ve booted from some Live-CD like Knoppix; if you want to setup or restore a non-working system, you&#8217;d have to transfer all files needed by the fsvs binary to it, and then start in some kind of chroot environment. </p>
<p> With this parameter you can tell fsvs that it should load its libraries from the current filesystem, but use the given path as root directory for its administrative data. </p>
<p> This is used for recovery; see the example in <code>Recovery for a non-booting system</code>. </p>
<p> So how does this work? </p>
<dl>
<dt>*</p>
<dd>The internal data paths derived from $FSVS_WAA and $FSVS_CONF use the value given for softroot as a base directory, if they do not already start with it. </p>
<p>&nbsp;<wbr>(If that creates a conflict for you, eg. in that you want to use&nbsp;<wbr>/var as the softroot, and your&nbsp;<wbr>$FSVS_WAA should be&nbsp;<wbr>/var/fsvs, you can make the string comparison fail by using&nbsp;<wbr>/./var for either path.)</dl>
<dl>
<dt>*</p>
<dd>When a directory name for $FSVS_CONF or $FSVS_WAA is derived from some file path, the part matching softroot is cut off, so that the generated names match the situation after rebooting.</dl>
<p> Previously you&#8217;d have to <code>export</code> your data back to the filesystem and call <code>urls</code> &#8216;fsvs urls&#8217; and fsvs <code>sync-repos</code> again, to get the WAA data back. </p>
<p> <code>Note:</code></p>
<dl>
<dd>A plain chroot() would not work, as some needed programs (eg. the decoder for update, see <code>Special property names</code>) would not be available. </p>
<p> The easy way to understand softroot is: If you want to do a chroot() into the given directory (or boot with it as /), you&#8217;ll want this set. </p>
<p> As this value is used for finding the correct working copy root (by trying to find a <code>conf-path</code>, it cannot be set from a per-wc config file. Only the environment, global configuration or command line parameter make sense.</dl>
<h2>&#8216;fsvs log&#8217; revision limit</h2>
<p>There are some defaults for the number of revisions that are shown on a &#8216;fsvs log&#8217; command: </p>
<dl>
<dt>*</p>
<dd>2 revisions given (-rX:Y): abs(X-Y)+1, ie. all revisions in that range.</p>
<dt>*</p>
<dd>1 revision given: exactly that one.</p>
<dt>*</p>
<dd>no revisions given: from HEAD to 1, with a maximum of 100.</dl>
<p> So this command is mostly useful to get more than the default number of revisions on when running without revision arguments, or to get fewer.</p>
<h2>&#8216;fsvs log&#8217; output format</h2>
<p>You can modify aspects of the <code>fsvs log</code> output format by setting the log_output option to a combination of these flags: </p>
<dl>
<dt>*</p>
<dd>color: This uses color in the output, similar to cg-log (cogito-log); the header and separator lines are highlighted.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>This uses ANSI escape sequences, and tries to restore the default color; if you know how to do that better (and more compatible), please tell the developer mailing list.</dl>
<dl>
<dt>*</p>
<dd>indent: Additionally you can shift the log message itself a space to the right, to make the borders clearer.</dl>
<p> Furthermore the value normal is available; this turns off all special handling. </p>
<p> <code>Note:</code></p>
<dl>
<dd>If you start such an option, the value is reseted; so if you specify log_output=color,indent in the global config file, and use log_output=color on the commandline, only colors are used. This is a difference to the <code>Filtering entries</code> option, which is cumulating.</dl>
<h2>Status output coloring</h2>
<p>FSVS can colorize the output of the status lines; removed entries will be printed in red, new ones in green, and otherwise changed in blue. Unchanged (for -v) will be given in the default color. </p>
<p> For this you can set stat_color=yes; this is turned off per default. </p>
<p> As with the other colorizing options this gets turned off automatically if the output is not on a tty; on the command line you can override this, though.</p>
<h2>Directory sorting</h2>
<p>If you&#8217;d like to have the output of <code>status</code> sorted, you can use the option dir_sort=yes. FSVS will do a run through the tree, to read the status of the entries, and then go through it again, but sorted by name. (See dir_enumerator().) </p>
<p> <code>Note:</code></p>
<dl>
<dd>If FSVS aborts with an error during <code>status</code> output, you might want to turn this option off again, to see where fsvs stops; the easiest way is on the commandline with -odir_sort=no.</dl>
<h2>Author</h2>
<p>You can specify an author to be used on commit. This option has a special behaviour; if the first character of the value is an &#8216;$&#8217;, the value is replaced by the environment variable named. </p>
<p> Empty strings are ignored; that allows an /etc/fsvs/config like this: </p>
<pre> author=unknown
 author=$LOGNAME
 author=$SUDO_USER</pre>
<p>&nbsp;<wbr>where the last non-empty value is taken;&nbsp;<wbr>and if your .authorized_keys has lines like&nbsp;<wbr> </p>
<pre> environment='FSVS_AUTHOR=some_user' ssh-rsa ...</pre>
<p>&nbsp;<wbr>that would override the config values. </p>
<p> <code>Note:</code></p>
<dl>
<dd>Your sshd_config needs the PermitUserEnvironment setting; you can also take a look at the AcceptEnv and SendEnv documentation.</dl>
<h2>Destination URL for commit</h2>
<p>If you defined multiple URLs for your working copy, FSVS needs to know which URL to commit to. </p>
<p> For this you would set commit_to to the <code>name</code> of the URL; see this example: </p>
<pre> fsvs urls N:master,P:10,<a rel="nofollow" href="http://...">http://...</a> N:local,P:20,file:///...
 fsvs ci /etc/passwd -m 'New user defined' -ocommit_to=local</pre>
<h2>Destination for debug output</h2>
<p>See <code>-d</code>. </p>
<p> Example: </p>
<pre> fsvs -o debug_output=/tmp/debug.out -d st /etc</pre>
<h2>Doing empty commits</h2>
<p>In the default settings FSVS will happily create empty commits, ie. revisions without any changed entry. These just have a revision number, an author and a timestamp; this is nice if FSVS is run via CRON, and you want to see when FSVS gets run. </p>
<p> If you would like to avoid such revisions, set this option to no; then such commits will be avoided. </p>
<p> Example: </p>
<pre> fsvs commit -o empty_commit=no -m 'cron' /etc</pre>
<h2>Avoiding expensive compares on ef cpfd &#8216;copyfrom-detect&#8217;</h2>
<p>If you&#8217;ve got big files that are seen as new, doing the MD5 comparison can be time consuming. So there&#8217;s the option copyfrom_exp, which takes the usual yes (default) and no arguments. </p>
<pre> fsvs copyfrom-detect -o copyfrom_exp=no some_directory</pre>
<h2>Waiting for a time change after working copy operations</h2>
<p>If you&#8217;re using fsvs in automated systems, you might see that changes that happen in the same second as a commit are not seen with <code>status</code> later; this is because the timestamp granularity of fsvs is 1 second. </p>
<p> For backward compatibility the default value is no (don&#8217;t delay). You can set it to any combination of </p>
<dl>
<dt>*</p>
<dd>commit,</p>
<dt>*</p>
<dd>update,</p>
<dt>*</p>
<dd>revert and/or</p>
<dt>*</p>
<dd>checkout;</dl>
<p> for yes all of these actions are delayed until the clock seconds change. </p>
<p> Example how to set that option via an environment variable: </p>
<pre> export FSVS_DELAY=commit,revert</pre>
<h2>Stopping status reports as soon as changes are found</h2>
<p>If you want to use FSVS in scripts, you might simply want to know whether anything was changed. </p>
<p> For this use the stop_on_change option, possibly combined with <code>Filtering entries</code> : </p>
<pre> fsvs -o stop_change=yes st /etc
 fsvs -o stop_change=yes -o filter=text status /etc/init.d</pre>
<h2>How to resolve conflicts on update</h2>
<p>If you start an update, but one of the entries that was changed in the repository is changed locally too, you get a conflict. </p>
<p> There are some ways to resolve a conflict: </p>
<dl>
<dt>*</p>
<dd>local &#8211; Just take the local entry, ignore the repository.</dl>
<dl>
<dt>*</p>
<dd>remote &#8211; Overwrite any local change with the remote version.</dl>
<dl>
<dt>*</p>
<dd>both &#8211; Keep the local modifications in the file renamed to <i>filename</i>.mine, and save the repository version as <i>filename</i>.r<i>XXX</i>, ie. put the revision number after the filename.</dl>
<p> These files will be seen as New; the conflict must be solved manually, and the resolution made known to FSVS via <code>resolve</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dd>As there&#8217;s no known <i>good</i> version after this renaming, a zero byte file gets created. </p>
<p>&nbsp;<wbr>Any&nbsp;<wbr><code>resolve</code>&nbsp;<wbr>or&nbsp;<wbr><code>revert</code>&nbsp;<wbr>command would make that current, and the changes that are kept in&nbsp;<wbr><i>filename</i>.mine would be lost!&nbsp;<wbr> </p>
<p>&nbsp;<wbr>You could only&nbsp;<wbr><code>revert</code>&nbsp;<wbr>to the last repository version, ie. the data of&nbsp;<wbr><i>filename</i>.r<i>XXX</i>.</dl>
<dl>
<dt>*</p>
<dd>merge &#8211; Call the program merge with the common ancestor, the local and the remote version.</dl>
<p> If it is a clean merge, no further work is necessary; else you&#8217;ll get the (partly) merged file, and the two other versions just like with the both variant, and have to tell FSVS that the conflict is resolved by <code>resolve</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dd>As in the subversion command line client svn the auxiliary files are seen as new, although that might change in the future (so that they automatically get ignored).</dl>
<h2>Options regarding the &#8216;merge&#8217; programm</h2>
<p>Like with <code>diff</code>, the merge operation is not done internally in FSVS. </p>
<p> To have better control </p>
<dl>
<dt>*</p>
<dd>merge_prg: The executable name, default &#8216;merge&#8217;.</p>
<dt>*</p>
<dd>merge_opt: The default options, default &#8216;-A&#8217;.</dl>
<p> The option &#8216;-p&#8217; is always used: </p>
<pre> $merge_prg $merge_opt -p $file1 $common $file2</pre>
<h2>Path definitions for the config and WAA area</h2>
<p>The paths given here are used to store the persistent configuration data needed by FSVS; please see <code>Files used by fsvs</code> and <code>Priorities for option setting</code> for more details, and the <code>Using an alternate root directory</code> parameter as well as the <code>Recovery for a non-booting system</code> for further discussion. </p>
<pre> FSVS_CONF=/home/user/.fsvs-conf fsvs -o waa=/home/user/.fsvs-waa st</pre>
<p><code>Note:</code></p>
<dl>
<dd>Please note that these paths can be given <code>only</code> as environment variables ($FSVS_CONF resp. $FSVS_WAA) or as command line parameter; settings in config files are ignored.</dl>
<h2>Configuration directory for the subversion libraries</h2>
<p>This path specifies where the subversion libraries should take their configuration data from; the most important aspect of that is authentication data, especially for certificate authentication. </p>
<p> The default value is $FSVS_CONF/auth/. </p>
<p> /etc/fsvs/config could have eg. </p>
<pre> config_dir=/root/.subversion</pre>
<p>&nbsp;<wbr></p>
