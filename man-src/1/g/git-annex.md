---
title: "git-annex(1)"
name: "git-annex"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-annex/"
description: "git-annex – manage files with git, without checking their contents in"
---

<h2>NAME</h2>
<p> git-annex &#8211; manage files with git, without checking their contents in </p>
<h2>SYNOPSIS</h2>
<p> git annex command [params &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> git-annex allows managing files with git, without checking the file contents into git. While that may seem paradoxical, it is useful when dealing with files larger than git can currently easily handle, whether due to limitations in memory, checksumming time, or disk space. </p>
<p> Even without file content tracking, being able to manage files with git, move files around and delete files with versioned directory trees, and use branches and distributed clones, are all very handy reasons to use git. And annexed files can co-exist in the same git repository with regularly versioned files, which is convenient for maintaining documents, Makefiles, etc that are associated with annexed files but that benefit from full revision control. </p>
<p> When a file is annexed, its content is moved into a key-value store, and a symlink is made that points to the content. These symlinks are checked into git and versioned like regular files. You can move them around, delete them, and so on. Pushing to another git repository will make git-annex there aware of the annexed file, and it can be used to retrieve its content from the key-value store. </p>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr>#&nbsp;<wbr>git annex get video/hackity_hack_and_kaxxt.mov<br />
&nbsp;<wbr>get video/_why_hackity_hack_and_kaxxt.mov&nbsp;<wbr>(not available)<br />
I was unable to access these remotes: server<br />
Try making some of these repositories available:<br />
<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>5863d8c0-d9a9-11df-adb2-af51e6559a49&nbsp;<wbr>&nbsp;<wbr>&#8212; my home file server</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>58d84e8a-d9ae-11df-a1aa-ab9aa8c00826&nbsp;<wbr>&nbsp;<wbr>&#8212; portable USB drive</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ca20064c-dbb5-11df-b2fe-002170d25c55&nbsp;<wbr>&nbsp;<wbr>&#8212; backup SATA drive</p>
<p>&nbsp;<wbr>failed<br />
&nbsp;<wbr>#&nbsp;<wbr>sudo mount&nbsp;<wbr>/media/usb<br />
&nbsp;<wbr>#&nbsp;<wbr>git remote add usbdrive&nbsp;<wbr>/media/usb<br />
&nbsp;<wbr>#&nbsp;<wbr>git annex get video/hackity_hack_and_kaxxt.mov<br />
&nbsp;<wbr>get video/hackity_hack_and_kaxxt.mov&nbsp;<wbr>(from usbdrive&#8230;)&nbsp;<wbr>ok<br />
&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>git annex add iso<br />
&nbsp;<wbr>add iso/Debian_5.0.iso ok<br />
&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>git annex drop iso/Debian_4.0.iso<br />
&nbsp;<wbr>drop iso/Debian_4.0.iso ok<br />
&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>git annex move iso &#8211;to=usbdrive<br />
&nbsp;<wbr>move iso/Debian_5.0.iso&nbsp;<wbr>(moving to usbdrive&#8230;)&nbsp;<wbr>ok </p>
<h2>COMMONLY USED COMMANDS</h2>
<p> Like many git commands, git-annex can be passed a path that is either a file or a directory. In the latter case it acts on all relevant files in the directory. When no path is specified, most git-annex commands default to acting on all relevant files in the current directory (and subdirectories). </p>
<dl>
<dt><code>add [path &#8230;]</code></p>
<dd> Adds files in the path to the annex. Files that are already checked into git, or that git has been configured to ignore will be silently skipped. (Use <code>&#8211;force</code> to add ignored files.) Dotfiles are skipped unless explicitly listed.</p>
<dt>
<dd>
<dt><code>get [path &#8230;]</code></p>
<dd> Makes the content of annexed files available in this repository. This will involve copying them from another repository, or downloading them, or transferring them from some kind of key-value store.</p>
<dt>
<dd> Normally git-annex will choose which repository to copy the content from, but you can override this using the <code>&#8211;from</code> option.</p>
<dt>
<dd>
<dt><code>drop [path &#8230;]</code></p>
<dd> Drops the content of annexed files from this repository.</p>
<dt>
<dd> git-annex will refuse to drop content if it cannot verify it is safe to do so. This can be overridden with the <code>&#8211;force</code> switch.</p>
<dt>
<dd> To drop content from a remote, specify <code>&#8211;from</code>.</p>
<dt>
<dd>
<dt><code>move [path &#8230;]</code></p>
<dd> When used with the <code>&#8211;from</code> option, moves the content of annexed files from the specified repository to the current one.</p>
<dt>
<dd> When used with the <code>&#8211;to</code> option, moves the content of annexed files from the current repository to the specified one.</p>
<dt>
<dd>
<dt><code>copy [path &#8230;]</code></p>
<dd> When used with the <code>&#8211;from</code> option, copies the content of annexed files from the specified repository to the current one.</p>
<dt>
<dd> When used with the <code>&#8211;to</code> option, copies the content of annexed files from the current repository to the specified one.</p>
<dt>
<dd> To avoid contacting the remote to check if it has every file when copying &#8211;to the repository, specify <code>&#8211;fast</code></p>
<dt>
<dd> To force checking the remote for every file when copying &#8211;from the repository, specify <code>&#8211;force</code>.</p>
<dt>
<dd>
<dt><code>status [path &#8230;]</code></p>
<dd> Similar to <code>git status &#8211;short</code>, displays the status of the files in the working tree. Shows files that are not checked into git, files that have been deleted, and files that have been modified. Particularly useful in direct mode.</p>
<dt>
<dd>
<dt><code>unlock [path &#8230;]</code></p>
<dd> Normally, the content of annexed files is protected from being changed. Unlocking an annexed file allows it to be modified. This replaces the symlink for each specified file with a copy of the file&#8217;s content. You can then modify it and <code>git annex add</code> (or <code>git commit</code>) to inject it back into the annex.</p>
<dt>
<dd>
<dt><code>edit [path &#8230;]</code></p>
<dd> This is an alias for the unlock command. May be easier to remember, if you think of this as allowing you to edit an annexed file.</p>
<dt>
<dd>
<dt><code>lock [path &#8230;]</code></p>
<dd> Use this to undo an unlock command if you don&#8217;t want to modify the files, or have made modifications you want to discard.</p>
<dt>
<dd>
<dt><code>sync [remote &#8230;]</code></p>
<dd> Use this command when you want to synchronize the local repository with one or more of its remotes. You can specify the remotes to sync with; the default is to sync with all remotes. Or specify <code>&#8211;fast</code> to sync with the remotes with the lowest annex-cost value.</p>
<dt>
<dd> The sync process involves first committing all local changes, then fetching and merging the <code>synced/master</code> and the <code>git-annex</code> branch from the remote repositories, and finally pushing the changes back to those branches on the remote repositories. You can use standard git commands to do each of those steps by hand, or if you don&#8217;t want to worry about the details, you can use sync.</p>
<dt>
<dd> Merge conflicts are automatically handled by sync. When two conflicting versions of a file have been committed, both will be added to the tree, under different filenames. For example, file &quot;foo&quot; would be replaced with &quot;foo.somekey&quot; and &quot;foo.otherkey&quot;.</p>
<dt>
<dd> Note that syncing with a remote will not update the remote&#8217;s working tree with changes made to the local repository. However, those changes are pushed to the remote, so they can be merged into its working tree by running &quot;git annex sync&quot; on the remote.</p>
<dt>
<dd> With the <code>&#8211;content</code> option, the contents of annexed files in the work tree will also be uploaded and downloaded from remotes. By default, this tries to get each annexed file that the local repository does not yet have, and then copies each file to every remote that it is syncing with. This behavior can be overridden by configuring the preferred content of a repository. See see PREFERRED CONTENT below.</p>
<dt>
<dd>
<dt><code>merge</code></p>
<dd> This performs the same merging that is done by the sync command, but without pushing or pulling any data.</p>
<dt>
<dd> One way to use this is to put <code>git annex merge</code> into a repository&#8217;s post-receive hook. Then any syncs to the repository will update its working copy automatically.</p>
<dt>
<dd>
<dt><code>mirror [path &#8230;]</code></p>
<dd> This causes a destination repository to mirror a source repository.</p>
<dt>
<dd> To use the local repository as the source repository, specify mirror <code>&#8211;to</code> remote.</p>
<dt>
<dd> To use a remote as the source repository, specify mirror <code>&#8211;from</code> remote.</p>
<dt>
<dd> Each specified file in the source repository is mirrored to the destination repository. If a file&#8217;s content is present in the source repository, it is copied to the destination repository. If a file&#8217;s content is not present in the source repository, it will be dropped from the destination repository when the numcopies setting allows.</p>
<dt>
<dd> Note that mirror does not sync the git repository, but only the file contents.</p>
<dt>
<dd> Also, &#8211;all may be specified to mirror all objects stored in the git annex, not only objects used by currently existing files. However, this bypasses checking the .gitattributes annex.numcopies setting when dropping files.</p>
<dt>
<dd>
<dt><code>addurl [url &#8230;]</code></p>
<dd> Downloads each url to its own file, which is added to the annex.</p>
<dt>
<dd> To avoid immediately downloading the url, specify <code>&#8211;fast</code>.</p>
<dt>
<dd> To avoid storing the size of the url&#8217;s content, and accept whatever is there at a future point, specify <code>&#8211;relaxed</code>. (Implies <code>&#8211;fast</code>.)</p>
<dt>
<dd> Normally the filename is based on the full url, so will look like &quot;<a rel="nofollow" href="http://www.example.com_dir_subdir_bigfile">www.example.com_dir_subdir_bigfile</a>&quot;. For a shorter filename, specify <code>&#8211;pathdepth=N</code>. For example, <code>&#8211;pathdepth=1</code> will use &quot;dir/subdir/bigfile&quot;, while <code>&#8211;pathdepth=3</code> will use &quot;bigfile&quot;. It can also be negative; <code>&#8211;pathdepth=-2</code> will use the last two parts of the url.</p>
<dt>
<dd> Or, to directly specify what file the url is added to, specify <code>&#8211;file</code>. This changes the behavior; now all the specified urls are recorded as alternate locations from which the file can be downloaded. In this mode, addurl can be used both to add new files, or to add urls to existing files.</p>
<dt>
<dd> When quvi is installed, urls are automatically tested to see if they point to a video hosting site, and the video is downloaded instead.</p>
<dt>
<dd>
<dt><code>rmurl file url</code></p>
<dd> Record that the file is no longer available at the url.</p>
<dt>
<dd>
<dt><code>import [path &#8230;]</code></p>
<dd> Moves files from somewhere outside the git working copy, and adds them to the annex. Individual files to import can be specified. If a directory is specified, the entire directory is imported.</p>
<dt>
<dd>
&nbsp;<wbr>git annex import&nbsp;<wbr>/media/camera/DCIM/*</p>
<dt>
<dd> By default, importing two files with the same contents from two different locations will result in both files being added to the repository. (With all checksumming backends, including the default SHA256E, only one copy of the data will be stored.)</p>
<dt>
<dd> To not delete files from the import location, use the <code>&#8211;duplicate</code> option. This could allow importing the same files repeatedly to different locations in a repository. More likely, it could be used to import the same files to a number of different branches or separate git repositories.</p>
<dt>
<dd> To only import files whose content has not been seen before by git-annex, use the <code>&#8211;deduplicate</code> option. Duplicate files will be deleted from the import location.</p>
<dt>
<dd> To only import files whose content has not been seen before by git-annex, but avoid deleting duplicate files, use the <code>&#8211;skip-duplicates</code> option.</p>
<dt>
<dd> The <code>&#8211;clean-duplicates</code> option does not import any new files, but any files found in the import location that are duplicates of content in the annex are deleted.</p>
<dt>
<dd> (Note that using <code>&#8211;deduplicate</code> or <code>&#8211;clean-duplicates</code> with the WORM backend does not look at file content, but filename and mtime.)</p>
<dt>
<dd>
<dt><code>importfeed [url &#8230;]</code></p>
<dd> Imports the contents of podcast feeds. Only downloads files whose urls have not already been added to the repository before, so you can delete, rename, etc the resulting files and repeated runs won&#8217;t duplicate them. (Use <code>&#8211;force</code> to force downloading urls it&#8217;s seen before.)</p>
<dt>
<dd> Use <code>&#8211;template</code> to control where the files are stored. The default template is &#8216;${feedtitle}/${itemtitle}${extension}&#8217; (Other available variables: feedauthor, itemauthor, itemsummary, itemdescription, itemrights, itemid)</p>
<dt>
<dd> The <code>&#8211;relaxed</code> and <code>&#8211;fast</code> options behave the same as they do in addurl.</p>
<dt>
<dd> When quvi is installed, links in the feed are tested to see if they are on a video hosting site, and the video is downloaded. This allows importing eg, youtube playlists.</p>
<dt>
<dd>
<dt><code>watch</code></p>
<dd> Watches for changes to files in the current directory and its subdirectories, and takes care of automatically adding new files, as well as dealing with deleted, copied, and moved files. With this running as a daemon in the background, you no longer need to manually run git commands when manipulating your files.</p>
<dt>
<dd> By default, all files in the directory will be added to the repository. (Including dotfiles.) To block some files from being added, use <code>.gitignore</code> files.</p>
<dt>
<dd> By default, all files that are added are added to the annex, the same as when you run <code>git annex add</code>. If you configure annex.largefiles, files that it does not match will instead be added with <code>git add</code>.</p>
<dt>
<dd> To not daemonize, run with <code>&#8211;foreground</code> ; to stop a running daemon, run with <code>&#8211;stop</code>.</p>
<dt>
<dd>
<dt><code>assistant</code></p>
<dd> Like watch, but also automatically syncs changes to other remotes. Typically started at boot, or when you log in.</p>
<dt>
<dd> With the <code>&#8211;autostart</code> option, the assistant is started in any repositories it has created. These are listed in <code>~/.config/git-annex/autostart</code>.</p>
<dt>
<dd>
<dt><code>webapp</code></p>
<dd> Opens a web app, that allows easy setup of a git-annex repository, and control of the git-annex assistant.</p>
<dt>
<dd> By default, the webapp can only be accessed from localhost, and running it opens a browser window.</p>
<dt>
<dd> With the <code>&#8211;listen=address[:port]</code> option, the webapp can be made to listen for connections on the specified address. This disables running a local web browser, and outputs the url you can use to open the webapp from a remote computer. Note that this does not yet use HTTPS for security, so use with caution!</p>
<dt>
<dd></dl>
<h2>REPOSITORY SETUP COMMANDS</h2>
<dl>
<dt><code>init [description]</code></p>
<dd>
<dt>
<dd> Until a repository (or one of its remotes) has been initialized, git-annex will refuse to operate on it, to avoid accidentally using it in a repository that was not intended to have an annex.</p>
<dt>
<dd> It&#8217;s useful, but not mandatory, to initialize each new clone of a repository with its own description. If you don&#8217;t provide one, one will be generated using the username, hostname and the path.</p>
<dt>
<dd>
<dt><code>describe repository description</code></p>
<dd> Changes the description of a repository.</p>
<dt>
<dd> The repository to describe can be specified by git remote name or by uuid. To change the description of the current repository, use &quot;here&quot;.</p>
<dt>
<dd>
<dt><code>initremote name [param=value &#8230;]</code></p>
<dd> Creates a new special remote, and adds it to <code>.git/config</code>.</p>
<dt>
<dd> The remote&#8217;s configuration is specified by the parameters. Different types of special remotes need different configuration values. The command will prompt for parameters as needed.</p>
<dt>
<dd> All special remotes support encryption. You can either specify <code>encryption=none</code> to disable encryption, or specify <code>encryption=hybrid keyid=$keyid &#8230;</code> to specify a GPG key id (or an email address associated with a key).</p>
<dt>
<dd> There are actually three schemes that can be used for management of the encryption keys. When using the encryption=hybrid scheme, additional GPG keys can be given access to the encrypted special remote easily (without re-encrypting everything). When using encryption=shared, a shared key is generated and stored in the git repository, allowing anyone who can clone the git repository to access it. Finally, when using encryption=pubkey, content in the special remote is directly encrypted to the specified GPG keys, and additional ones cannot easily be given access.</p>
<dt>
<dd> Note that with encryption enabled, a cryptographic key is created. This requires sufficient entropy. If initremote seems to hang or take a long time while generating the key, you may want to Ctrl-c it and re-run with <code>&#8211;fast</code>, which causes it to use a lower-quality source of randomness.</p>
<dt>
<dd> Example Amazon S3 remote:</p>
<dt>
<dd>
&nbsp;<wbr>git annex initremote mys3 type=S3 encryption=hybrid keyid=me [at] example.com datacenter=EU</p>
<dt>
<dd>
<dt><code>enableremote name [param=value &#8230;]</code></p>
<dd> Enables use of an existing special remote in the current repository, which may be a different repository than the one in which it was originally created with the initremote command.</p>
<dt>
<dd> The name of the remote is the same name used when originally creating that remote with &quot;initremote&quot;. Run &quot;git annex enableremote&quot; with no parameters to get a list of special remote names.</p>
<dt>
<dd> Some special remotes may need parameters to be specified every time. For example, the directory special remote requires a directory= parameter.</p>
<dt>
<dd> This command can also be used to modify the configuration of an existing special remote, by specifying new values for parameters that were originally set when using initremote. (However, some settings such as the as the encryption scheme cannot be changed once a special remote has been created.)</p>
<dt>
<dd> The GPG keys that an encrypted special remote is encrypted with can be changed using the keyid+= and keyid-= parameters. These respectively add and remove keys from the list. However, note that removing a key does NOT necessarily prevent the key&#8217;s owner from accessing data in the encrypted special remote (which is by design impossible, short of deleting the remote).</p>
<dt>
<dd> One use-case of keyid-= is to replace a revoked key with a new key:</p>
<dt>
<dd>
&nbsp;<wbr>git annex enableremote mys3 keyid-=revokedkey keyid+=newkey</p>
<dt>
<dd> Also, note that for encrypted special remotes using plain public-key encryption (encryption=pubkey), adding or removing a key has NO effect on files that have already been copied to the remote. Hence using keyid+= and keyid-= with such remotes should be used with care, and make little sense except in cases like the revoked key example above.</p>
<dt>
<dd>
<dt><code>numcopies [N]</code></p>
<dd> Tells git-annex how many copies it should preserve of files, over all repositories. The default is 1.</p>
<dt>
<dd> Run without a number to get the current value.</p>
<dt>
<dd> When git-annex is asked to drop a file, it first verifies that the required number of copies can be satisfied amoung all the other repositories that have a copy of the file.</p>
<dt>
<dd> This can be overridden on a per-file basis by the annex.numcopies setting in .gitattributes files.</p>
<dt>
<dd>
<dt><code>trust [repository &#8230;]</code></p>
<dd> Records that a repository is trusted to not unexpectedly lose content. Use with care.</p>
<dt>
<dd> To trust the current repository, use &quot;here&quot;.</p>
<dt>
<dd>
<dt><code>untrust [repository &#8230;]</code></p>
<dd> Records that a repository is not trusted and could lose content at any time.</p>
<dt>
<dd>
<dt><code>semitrust [repository &#8230;]</code></p>
<dd> Returns a repository to the default semi trusted state.</p>
<dt>
<dd>
<dt><code>dead [repository &#8230;]</code></p>
<dd> Indicates that the repository has been irretrievably lost. (To undo, use semitrust.)</p>
<dt>
<dd>
<dt><code>group repository groupname</code></p>
<dd> Adds a repository to a group, such as &quot;archival&quot;, &quot;enduser&quot;, or &quot;transfer&quot;. The groupname must be a single word.</p>
<dt>
<dd>
<dt><code>ungroup repository groupname</code></p>
<dd> Removes a repository from a group.</p>
<dt>
<dd>
<dt><code>wanted repository [expression]</code></p>
<dd> When run with an expression, configures the content that is preferred to be held in the archive. See PREFERRED CONTENT below.</p>
<dt>
<dd> For example:</p>
<dt>
<dd>
&nbsp;<wbr>git annex wanted .&nbsp;<wbr>&quot;include=*.mp3 or include=*.ogg&quot;</p>
<dt>
<dd> Without an expression, displays the current preferred content setting of the repository.</p>
<dt>
<dd>
<dt><code>schedule repository [expression]</code></p>
<dd> When run with an expression, configures scheduled jobs to run at a particular time. This can be used to make the assistant periodically run incremental fscks. See SCHEDULED JOBS below.</p>
<dt>
<dd>
<dt><code>vicfg</code></p>
<dd> Opens EDITOR on a temp file containing most of the above configuration settings, and when it exits, stores any changes made back to the git-annex branch.</p>
<dt>
<dd>
<dt><code>direct</code></p>
<dd> Switches a repository to use direct mode, where rather than symlinks to files, the files are directly present in the repository.</p>
<dt>
<dd> As part of the switch to direct mode, any changed files will be committed.</p>
<dt>
<dd> Note that git commands that operate on the work tree are often unsafe to use in direct mode repositories, and can result in data loss or other bad behavior.</p>
<dt>
<dd>
<dt><code>indirect</code></p>
<dd> Switches a repository back from direct mode to the default, indirect mode.</p>
<dt>
<dd> As part of the switch from direct mode, any changed files will be committed.</p>
<dt>
<dd></dl>
<h2>REPOSITORY MAINTENANCE COMMANDS</h2>
<dl>
<dt><code>fsck [path &#8230;]</code></p>
<dd>
<dt>
<dd> With no parameters, this command checks the whole annex for consistency, and warns about or fixes any problems found. This is a good compliment to <code>git fsck</code>.</p>
<dt>
<dd> With parameters, only the specified files are checked.</p>
<dt>
<dd> To check a remote to fsck, specify <code>&#8211;from</code>.</p>
<dt>
<dd> To avoid expensive checksum calculations (and expensive transfers when fscking a remote), specify <code>&#8211;fast</code>.</p>
<dt>
<dd> To start a new incremental fsck, use the <code>&#8211;incremental</code> option. Then the next time you fsck, you can instead use the <code>&#8211;more</code> option to skip over files that have already been checked, and continue where it left off.</p>
<dt>
<dd> The <code>&#8211;incremental-schedule</code> option makes a new incremental fsck be started a configurable time after the last incremental fsck was started. Once the current incremental fsck has completely finished, it causes a new one to start.</p>
<dt>
<dd> Maybe you&#8217;d like to run a fsck for 5 hours at night, picking up each night where it left off. You&#8217;d like this to continue until all files have been fscked. And once it&#8217;s done, you&#8217;d like a new fsck pass to start, but no more often than once a month. Then put this in a nightly cron job:</p>
<dt>
<dd>
&nbsp;<wbr>git annex fsck &#8211;incremental-schedule 30d &#8211;time-limit 5h</p>
<dt>
<dd> To verify data integrity only while disregarding required number of copies, use <code>&#8211;numcopies=1</code>.</p>
<dt>
<dd>
<dt><code>unused</code></p>
<dd> Checks the annex for data that does not correspond to any files present in any tag or branch, and prints a numbered list of the data.</p>
<dt>
<dd> To only show unused temp and bad files, specify <code>&#8211;fast</code>.</p>
<dt>
<dd> To check for annexed data on a remote, specify <code>&#8211;from</code>.</p>
<dt>
<dd> After running this command, you can use the <code>&#8211;unused</code> option to operate on all the unused data that was found. For example, to move all unused data to origin:</p>
<dt>
<dd>
&nbsp;<wbr>git annex unused;&nbsp;<wbr>git annex move &#8211;unused &#8211;to origin</p>
<dt>
<dd>
<dt><code>dropunused [number|range &#8230;]</code></p>
<dd> Drops the data corresponding to the numbers, as listed by the last <code>git annex unused</code></p>
<dt>
<dd> You can also specify ranges of numbers, such as &quot;1-1000&quot;. Or, specify &quot;all&quot; to drop all unused data.</p>
<dt>
<dd> To drop the data from a remote, specify <code>&#8211;from.</code></p>
<dt>
<dd>
<dt><code>addunused [number|range &#8230;]</code></p>
<dd> Adds back files for the content corresponding to the numbers or ranges, as listed by the last <code>git annex unused</code>. The files will have names starting with &quot;unused.&quot;</p>
<dt>
<dd>
<dt><code>fix [path &#8230;]</code></p>
<dd> Fixes up symlinks that have become broken to again point to annexed content. This is useful to run if you have been moving the symlinks around, but is done automatically when committing a change with git too.</p>
<dt>
<dd>
<dt><code>upgrade</code></p>
<dd> Upgrades the repository to current layout.</p>
<dt>
<dd>
<dt><code>forget</code></p>
<dd> Causes the git-annex branch to be rewritten, throwing away historical data about past locations of files. The resulting branch will use less space, but <code>git annex log</code> will not be able to show where files used to be located.</p>
<dt>
<dd> To also prune references to repositories that have been marked as dead, specify <code>&#8211;drop-dead</code>.</p>
<dt>
<dd> When this rewritten branch is merged into other clones of the repository, <code>git-annex</code> will automatically perform the same rewriting to their local <code>git-annex</code> branches. So the forgetfulness will automatically propagate out from its starting point until all repositories running git-annex have forgotten their old history. (You may need to force git to push the branch to any git repositories not running git-annex.)</p>
<dt>
<dd>
<dt><code>repair</code></p>
<dd> This can repair many of the problems with git repositories that <code>git fsck</code> detects, but does not itself fix. It&#8217;s useful if a repository has become badly damaged. One way this can happen is if a repository used by git-annex is on a removable drive that gets unplugged at the wrong time.</p>
<dt>
<dd> This command can actually be used inside git repositories that do not use git-annex at all; when used in a repository using git-annex, it does additional repairs of the git-annex branch.</p>
<dt>
<dd> It works by deleting any corrupt objects from the git repository, and retrieving all missing objects it can from the remotes of the repository.</p>
<dt>
<dd> If that is not sufficient to fully recover the repository, it can also reset branches back to commits before the corruption happened, delete branches that are no longer available due to the lost data, and remove any missing files from the index. It will only do this if run with the <code>&#8211;force</code> option, since that rewrites history and throws out missing data. Note that the <code>&#8211;force</code> option never touches tags, even if they are no longer usable due to missing data.</p>
<dt>
<dd> After running this command, you will probably want to run <code>git fsck</code> to verify it fixed the repository. Note that fsck may still complain about objects referenced by the reflog, or the stash, if they were unable to be recovered. This command does not try to clean up either the reflog or the stash.</p>
<dt>
<dd> It is also a good idea to run <code>git annex fsck &#8211;fast</code> after this command, to make sure that the git-annex branch reflects reality.</p>
<dt>
<dd></dl>
<h2>QUERY COMMANDS</h2>
<dl>
<dt><code>find [path &#8230;]</code></p>
<dd>
<dt>
<dd> Outputs a list of annexed files in the specified path. With no path, finds files in the current directory and its subdirectories.</p>
<dt>
<dd> By default, only lists annexed files whose content is currently present. This can be changed by specifying matching options. To list all annexed files, present or not, specify <code>&#8211;include &quot;*&quot;</code>. To list all annexed files whose content is not present, specify <code>&#8211;not &#8211;in=here</code></p>
<dt>
<dd> To output filenames terminated with nulls, for use with xargs -0, specify <code>&#8211;print0</code>. Or, a custom output formatting can be specified using <code>&#8211;format</code>. The default output format is the same as <code>&#8211;format=&#8217;${file}
&#8217;</code></p>
<dt>
<dd> These variables are available for use in formats: file, key, backend, bytesize, humansize, keyname, hashdirlower, hashdirmixed, mtime.</p>
<dt>
<dd>
<dt><code>whereis [path &#8230;]</code></p>
<dd> Displays a information about where the contents of files are located.</p>
<dt>
<dd>
<dt><code>list [path &#8230;]</code></p>
<dd> Displays a table of remotes that contain the contents of the specified files. This is similar to whereis but a more compact display. Only configured remotes are shown by default; specify &#8211;allrepos to list all repositories.</p>
<dt>
<dd>
<dt><code>log [path &#8230;]</code></p>
<dd> Displays the location log for the specified file or files, showing each repository they were added to (&quot;+&quot;) and removed from (&quot;-&quot;).</p>
<dt>
<dd> To limit how far back to search for location log changes, the options <code>&#8211;since</code>, <code>&#8211;after</code>, <code>&#8211;until</code>, <code>&#8211;before</code>, and <code>&#8211;max-count</code> can be specified. They are passed through to git log. For example, <code>&#8211;since &quot;1 month ago&quot;</code></p>
<dt>
<dd> To generate output suitable for the gource visualization program, specify <code>&#8211;gource</code>.</p>
<dt>
<dd>
<dt><code>info [directory &#8230;]</code></p>
<dd> Displays some statistics and other information, including how much data is in the annex and a list of all known repositories.</p>
<dt>
<dd> To only show the data that can be gathered quickly, use <code>&#8211;fast</code>.</p>
<dt>
<dd> When a directory is specified, shows a differently formatted info display for that directory. In this mode, all of the matching options can be used to filter the files that will be included in the information.</p>
<dt>
<dd> For example, suppose you want to run &quot;git annex get .&quot;, but would first like to see how much disk space that will use. Then run:</p>
<dt>
<dd>
&nbsp;<wbr>git annex info &#8211;fast . &#8211;not &#8211;in here</p>
<dt>
<dd>
<dt><code>version</code></p>
<dd> Shows the version of git-annex, as well as repository version information.</p>
<dt>
<dd>
<dt><code>map</code></p>
<dd> Helps you keep track of your repositories, and the connections between them, by going out and looking at all the ones it can get to, and generating a Graphviz file displaying it all. If the <code>dot</code> command is available, it is used to display the file to your screen (using x11 backend). (To disable this display, specify <code>&#8211;fast</code>)</p>
<dt>
<dd> This command only connects to hosts that the host it&#8217;s run on can directly connect to. It does not try to tunnel through intermediate hosts. So it might not show all connections between the repositories in the network.</p>
<dt>
<dd> Also, if connecting to a host requires a password, you might have to enter it several times as the map is being built.</p>
<dt>
<dd> Note that this subcommand can be used to graph any git repository; it is not limited to git-annex repositories.</p>
<dt>
<dd></dl>
<h2>METADATA COMMANDS</h2>
<dl>
<dt><code>metadata [path &#8230;] [-s field=value -s field+=value -s field-=value &#8230;]</code></p>
<dd>
<dt>
<dd> Each file can have any number of metadata fields attached to it, which each in turn have any number of values. This sets metadata for the specified file or files, or if run without any values, shows the current metadata.</p>
<dt>
<dd> To set a field&#8217;s value, removing any old value(s), use -s field=value.</p>
<dt>
<dd> To add an additional value, use -s field+=value.</p>
<dt>
<dd> To remove a value, use -s field-=value.</p>
<dt>
<dd> To set a tag, use -t tag, and use -u tag to remove a tag.</p>
<dt>
<dd> For example, to set some tags on a file and also its author:</p>
<dt>
<dd>
&nbsp;<wbr>git annex metadata annexscreencast.ogv -t video -t screencast -s author+=Alice</p>
<dt>
<dd>
<dt><code>view [field=value &#8230;] [tag &#8230;]</code></p>
<dd> Uses metadata to build a view branch of the files in the current branch, and checks out the view branch. Only files in the current branch whose metadata matches all the specified field values and tags will be shown in the view.</p>
<dt>
<dd> Multiple values for a metadata field can be specified, either by using a glob (<code>field=&quot;*&quot;</code>) or by listing each wanted value. The resulting view will put files in subdirectories according to the value of their fields.</p>
<dt>
<dd> Once within a view, you can make additional directories, and copy or move files into them. When you commit, the metadata will be updated to correspond to your changes.</p>
<dt>
<dd>
<dt><code>vpop [N]</code></p>
<dd> Switches from the currently active view back to the previous view. Or, from the first view back to original branch.</p>
<dt>
<dd> The optional number tells how many views to pop.</p>
<dt>
<dd>
<dt><code>vfilter [field=value &#8230;] [tag &#8230;]</code></p>
<dd> Filters the current view to only the files that have the specified values and tags.</p>
<dt>
<dd>
<dt><code>vadd [field=glob &#8230;]</code></p>
<dd> Changes the current view, adding an additional level of directories to categorize the files.</p>
<dt>
<dd> For example, when the view is by author/tag, <code>vadd year=*</code> will change it to year/author/tag.</p>
<dt>
<dd> So will <code>vadd year=2014 year=2013</code>, but limiting the years in view to only those two.</p>
<dt>
<dd>
<dt><code>vcycle</code></p>
<dd> When a view involves nested subdirectories, this cycles the order.</p>
<dt>
<dd> For example, when the view is by year/author/tag, <code>vcycle</code> will switch it to author/tag/year.</p>
<dt>
<dd></dl>
<h2>UTILITY COMMANDS</h2>
<dl>
<dt><code>migrate [path &#8230;]</code></p>
<dd>
<dt>
<dd> Changes the specified annexed files to use the default key-value backend (or the one specified with <code>&#8211;backend</code>). Only files whose content is currently available are migrated.</p>
<dt>
<dd> Note that the content is also still available using the old key after migration. Use <code>git annex unused</code> to find and remove the old key.</p>
<dt>
<dd> Normally, nothing will be done to files already using the new backend. However, if a backend changes the information it uses to construct a key, this can also be used to migrate files to use the new key format.</p>
<dt>
<dd>
<dt><code>reinject src dest</code></p>
<dd> Moves the src file into the annex as the content of the dest file. This can be useful if you have obtained the content of a file from elsewhere and want to put it in the local annex.</p>
<dt>
<dd> Automatically runs fsck on dest to check that the expected content was provided.</p>
<dt>
<dd> Example:</p>
<dt>
<dd>
&nbsp;<wbr>git annex reinject&nbsp;<wbr>/tmp/foo.iso foo.iso</p>
<dt>
<dd>
<dt><code>unannex [path &#8230;]</code></p>
<dd> Use this to undo an accidental <code>git annex add</code> command. It puts the file back how it was before the add.</p>
<dt>
<dd> Note that for safety, the content of the file remains in the annex, until you use <code>git annex unused</code> and <code>git annex dropunused</code>.</p>
<dt>
<dd> This is not the command you should use if you intentionally annexed a file and don&#8217;t want its contents any more. In that case you should use <code>git annex drop</code> instead, and you can also <code>git rm</code> the file.</p>
<dt>
<dd> Normally this does a slow copy of the file. In <code>&#8211;fast</code> mode, it instead makes a hard link from the file to the content in the annex. But use &#8211;fast mode with caution, because editing the file will change the content in the annex.</p>
<dt>
<dd>
<dt><code>uninit</code></p>
<dd> Use this to stop using git annex. It will unannex every file in the repository, and remove all of git-annex&#8217;s other data, leaving you with a git repository plus the previously annexed files.</p>
<dt>
<dd></dl>
<h2>PLUMBING COMMANDS</h2>
<dl>
<dt><code>pre-commit [path &#8230;]</code></p>
<dd>
<dt>
<dd> This is meant to be called from git&#8217;s pre-commit hook. <code>git annex init</code> automatically creates a pre-commit hook using this.</p>
<dt>
<dd> Fixes up symlinks that are staged as part of a commit, to ensure they point to annexed content. Also handles injecting changes to unlocked files into the annex. When in a view, updates metadata to reflect changes made to files in the view.</p>
<dt>
<dd>
<dt><code>lookupkey [file &#8230;]</code></p>
<dd> This plumbing-level command looks up the key used for a file in the index. The key is output to stdout. If there is no key (because the file is not present in the index, or is not a git-annex managed file), nothing is output, and it exits nonzero.</p>
<dt>
<dd>
<dt><code>examinekey [key &#8230;]</code></p>
<dd> This plumbing-level command is given a key, and prints information that can be determined purely by looking at the key.</p>
<dt>
<dd> To specify what information to print, use <code>&#8211;format</code>. Or use <code>&#8211;json</code> to get all available information in JSON format.</p>
<dt>
<dd> The same variables can be used in the format string as can be used in the format string of git annex find (except there is no file option here).</p>
<dt>
<dd> For example, the location a key&#8217;s value is stored (in indirect mode) can be looked up by running:</p>
<dt>
<dd>
&nbsp;<wbr>git annex examinekey &#8211;format=&#8217;.git/annex/objects/${hashdirmixed}${key}/${key}&#8217;</p>
<dt>
<dd>
<dt><code>fromkey key file</code></p>
<dd> This plumbing-level command can be used to manually set up a file in the git repository to link to a specified key.</p>
<dt>
<dd>
<dt><code>dropkey [key &#8230;]</code></p>
<dd> This plumbing-level command drops the annexed data for the specified keys from this repository.</p>
<dt>
<dd> This can be used to drop content for arbitrary keys, which do not need to have a file in the git repository pointing at them.</p>
<dt>
<dd>
<dt><code>transferkey</code></p>
<dd> This plumbing-level command is used to request a single key be transferred. Either the &#8211;from or the &#8211;to option can be used to specify the remote to use. A &#8211;file option can be used to hint at the file associated with the key.</p>
<dt>
<dd>
<dt><code>transferkeys</code></p>
<dd> This plumbing-level command is used by the assistant to transfer data. It is fed instructions about the keys to transfer using an internal stdio protocol, which is intentionally not documented (as it may change at any time).</p>
<dt>
<dd>
<dt><code>rekey [file key &#8230;]</code></p>
<dd> This plumbing-level command is similar to migrate, but you specify both the file, and the new key to use for it.</p>
<dt>
<dd> With <code>&#8211;force</code>, even files whose content is not currently available will be rekeyed. Use with caution.</p>
<dt>
<dd>
<dt><code>test</code></p>
<dd> This runs git-annex&#8217;s built-in test suite.</p>
<dt>
<dd> There are several parameters, provided by Haskell&#8217;s tasty test framework.</p>
<dt>
<dd>
<dt><code>xmppgit</code></p>
<dd> This command is used internally to perform git pulls over XMPP.</p>
<dt>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;force</code></p>
<dd>
<dt>
<dd> Force unsafe actions, such as dropping a file&#8217;s content when no other source of it can be verified to still exist, or adding ignored files. Use with care.</p>
<dt>
<dd>
<dt><code>&#8211;fast</code></p>
<dd> Enable less expensive, but also less thorough versions of some commands. What is avoided depends on the command.</p>
<dt>
<dd>
<dt><code>&#8211;auto</code></p>
<dd> Enable automatic mode. Commands that get, drop, or move file contents will only do so when needed to help satisfy the setting of numcopies, and preferred content configuration.</p>
<dt>
<dd>
<dt><code>&#8211;all</code></p>
<dd> Operate on all data that has been stored in the git annex, including old versions of files. This is the default behavior when running git-annex in a bare repository; in a non-bare repository the normal behavior is to only operate on specified files in the working tree.</p>
<dt>
<dd>
<dt><code>&#8211;unused</code></p>
<dd> Operate on all data that has been determined to be unused by a previous run of <code>git-annex unused</code>.</p>
<dt>
<dd>
<dt><code>&#8211;key=key</code></p>
<dd> Operate on only the specified key.</p>
<dt>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Avoid the default verbose display of what is done; only show errors and progress displays.</p>
<dt>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose display.</p>
<dt>
<dd>
<dt><code>&#8211;json</code></p>
<dd> Rather than the normal output, generate JSON. This is intended to be parsed by programs that use git-annex. Each line of output is a JSON object. Note that JSON output is only usable with some git-annex commands, like info, find, and whereis.</p>
<dt>
<dd>
<dt><code>&#8211;debug</code></p>
<dd> Show debug messages.</p>
<dt>
<dd>
<dt><code>&#8211;no-debug</code></p>
<dd> Disable debug messages.</p>
<dt>
<dd>
<dt><code>&#8211;from=repository</code></p>
<dd> Specifies a repository that content will be retrieved from, or that should otherwise be acted on.</p>
<dt>
<dd> It should be specified using the name of a configured remote.</p>
<dt>
<dd>
<dt><code>&#8211;to=repository</code></p>
<dd> Specifies a repository that content will be sent to.</p>
<dt>
<dd> It should be specified using the name of a configured remote.</p>
<dt>
<dd>
<dt><code>&#8211;numcopies=n</code></p>
<dd> Overrides the numcopies setting, forcing git-annex to ensure the specified number of copies exist.</p>
<dt>
<dd> Note that setting numcopies to 0 is very unsafe.</p>
<dt>
<dd>
<dt><code>&#8211;time-limit=time</code></p>
<dd> Limits how long a git-annex command runs. The time can be something like &quot;5h&quot;, or &quot;30m&quot; or even &quot;45s&quot; or &quot;10d&quot;.</p>
<dt>
<dd> Note that git-annex may continue running a little past the specified time limit, in order to finish processing a file.</p>
<dt>
<dd> Also, note that if the time limit prevents git-annex from doing all it was asked to, it will exit with a special code, 101.</p>
<dt>
<dd>
<dt><code>&#8211;trust=repository</code></p>
<dd>
<dt><code>&#8211;semitrust=repository</code></p>
<dd>
<dt><code>&#8211;untrust=repository</code></p>
<dd> Overrides trust settings for a repository. May be specified more than once.</p>
<dt>
<dd> The repository should be specified using the name of a configured remote, or the UUID or description of a repository.</p>
<dt>
<dd>
<dt><code>&#8211;trust-glacier-inventory</code></p>
<dd> Amazon Glacier inventories take hours to retrieve, and may not represent the current state of a repository. So git-annex does not trust that files that the inventory claims are in Glacier are really there. This switch can be used to allow it to trust the inventory.</p>
<dt>
<dd> Be careful using this, especially if you or someone else might have recently removed a file from Glacier. If you try to drop the only other copy of the file, and this switch is enabled, you could lose data!</p>
<dt>
<dd>
<dt><code>&#8211;backend=name</code></p>
<dd> Specifies which key-value backend to use. This can be used when adding a file to the annex, or migrating a file. Once files are in the annex, their backend is known and this option is not necessary.</p>
<dt>
<dd>
<dt><code>&#8211;format=value</code></p>
<dd> Specifies a custom output format. The value is a format string, in which &#8216;${var}&#8217; is expanded to the value of a variable. To right-justify a variable with whitespace, use &#8216;${var;width}&#8217; ; to left-justify a variable, use &#8216;${var;-width}&#8217;; to escape unusual characters in a variable, use &#8216;${escaped_var}&#8217;</p>
<dt>
<dd> Also, &#8216;
&#8217; is a newline, &#8216;
