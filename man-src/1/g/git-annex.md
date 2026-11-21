---

title: "git-annex(1)"
name: "git-annex"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-annex/"
description: "git-annex – manage files with git, without checking their contents in"
---

<h2>NAME</h2>
<p> git-annex - manage files with git, without checking their contents in </p>
<p> git annex command [params ...] </p>
<p> git-annex allows managing files with git, without checking the file contents into git. While that may seem paradoxical, it is useful when dealing with files larger than git can currently easily handle, whether due to limitations in memory, checksumming time, or disk space. </p>
<p> Even without file content tracking, being able to manage files with git, move files around and delete files with versioned directory trees, and use branches and distributed clones, are all very handy reasons to use git. And annexed files can co-exist in the same git repository with regularly versioned files, which is convenient for maintaining documents, Makefiles, etc that are associated with annexed files but that benefit from full revision control. </p>
<p> When a file is annexed, its content is moved into a key-value store, and a symlink is made that points to the content. These symlinks are checked into git and versioned like regular files. You can move them around, delete them, and so on. Pushing to another git repository will make git-annex there aware of the annexed file, and it can be used to retrieve its content from the key-value store. </p>
<h2>EXAMPLES</h2>
<p> <br />
&nbsp;<wbr>#&nbsp;<wbr>git annex get video/hackity_hack_and_kaxxt.mov <br />
&nbsp;<wbr>get video/_why_hackity_hack_and_kaxxt.mov&nbsp;<wbr>(not available) <br />
I was unable to access these remotes: server <br />
Try making some of these repositories available: <br />
<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>5863d8c0-d9a9-11df-adb2-af51e6559a49&nbsp;<wbr>&nbsp;<wbr>-- my home file server<br />
 <br />
&nbsp;<wbr><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>58d84e8a-d9ae-11df-a1aa-ab9aa8c00826&nbsp;<wbr>&nbsp;<wbr>-- portable USB drive<br />
 <br />
&nbsp;<wbr><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>ca20064c-dbb5-11df-b2fe-002170d25c55&nbsp;<wbr>&nbsp;<wbr>-- backup SATA drive<br />
 <br />
&nbsp;<wbr>failed <br />
&nbsp;<wbr>#&nbsp;<wbr>sudo mount&nbsp;<wbr>/media/usb <br />
&nbsp;<wbr>#&nbsp;<wbr>git remote add usbdrive&nbsp;<wbr>/media/usb <br />
&nbsp;<wbr>#&nbsp;<wbr>git annex get video/hackity_hack_and_kaxxt.mov <br />
&nbsp;<wbr>get video/hackity_hack_and_kaxxt.mov&nbsp;<wbr>(from usbdrive...)&nbsp;<wbr>ok <br />
&nbsp;<wbr> <br />
&nbsp;<wbr>#&nbsp;<wbr>git annex add iso <br />
&nbsp;<wbr>add iso/Debian_5.0.iso ok <br />
&nbsp;<wbr> <br />
&nbsp;<wbr>#&nbsp;<wbr>git annex drop iso/Debian_4.0.iso <br />
&nbsp;<wbr>drop iso/Debian_4.0.iso ok <br />
&nbsp;<wbr> <br />
&nbsp;<wbr>#&nbsp;<wbr>git annex move iso --to=usbdrive <br />
&nbsp;<wbr>move iso/Debian_5.0.iso&nbsp;<wbr>(moving to usbdrive...)&nbsp;<wbr>ok </p>
<h2>COMMONLY USED COMMANDS</h2>
<p> Like many git commands, git-annex can be passed a path that is either a file or a directory. In the latter case it acts on all relevant files in the directory. When no path is specified, most git-annex commands default to acting on all relevant files in the current directory (and subdirectories). </p>
<dl>
<dt><code>add [path ...]</code></dt>
<dd> <p> Adds files in the path to the annex. Files that are already checked into git, or that git has been configured to ignore will be silently skipped. (Use <code>--force</code> to add ignored files.) Dotfiles are skipped unless explicitly listed. </p>
 </dd>
<dd>  </dd>
<dt><code>get [path ...]</code></dt>
<dd> <p> Makes the content of annexed files available in this repository. This will involve copying them from another repository, or downloading them, or transferring them from some kind of key-value store. </p>
 </dd>
<dd> <p> Normally git-annex will choose which repository to copy the content from, but you can override this using the <code>--from</code> option. </p>
 </dd>
<dd>  </dd>
<dt><code>drop [path ...]</code></dt>
<dd> <p> Drops the content of annexed files from this repository. </p>
 </dd>
<dd> <p> git-annex will refuse to drop content if it cannot verify it is safe to do so. This can be overridden with the <code>--force</code> switch. </p>
 </dd>
<dd> <p> To drop content from a remote, specify <code>--from</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>move [path ...]</code></dt>
<dd> <p> When used with the <code>--from</code> option, moves the content of annexed files from the specified repository to the current one. </p>
 </dd>
<dd> <p> When used with the <code>--to</code> option, moves the content of annexed files from the current repository to the specified one. </p>
 </dd>
<dd>  </dd>
<dt><code>copy [path ...]</code></dt>
<dd> <p> When used with the <code>--from</code> option, copies the content of annexed files from the specified repository to the current one. </p>
 </dd>
<dd> <p> When used with the <code>--to</code> option, copies the content of annexed files from the current repository to the specified one. </p>
 </dd>
<dd> <p> To avoid contacting the remote to check if it has every file when copying --to the repository, specify <code>--fast</code> </p>
 </dd>
<dd> <p> To force checking the remote for every file when copying --from the repository, specify <code>--force</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>status [path ...]</code></dt>
<dd> <p> Similar to <code>git status --short</code>, displays the status of the files in the working tree. Shows files that are not checked into git, files that have been deleted, and files that have been modified. Particularly useful in direct mode. </p>
 </dd>
<dd>  </dd>
<dt><code>unlock [path ...]</code></dt>
<dd> <p> Normally, the content of annexed files is protected from being changed. Unlocking an annexed file allows it to be modified. This replaces the symlink for each specified file with a copy of the file&#8217;s content. You can then modify it and <code>git annex add</code> (or <code>git commit</code>) to inject it back into the annex. </p>
 </dd>
<dd>  </dd>
<dt><code>edit [path ...]</code></dt>
<dd> <p> This is an alias for the unlock command. May be easier to remember, if you think of this as allowing you to edit an annexed file. </p>
 </dd>
<dd>  </dd>
<dt><code>lock [path ...]</code></dt>
<dd> <p> Use this to undo an unlock command if you don&#8217;t want to modify the files, or have made modifications you want to discard. </p>
 </dd>
<dd>  </dd>
<dt><code>sync [remote ...]</code></dt>
<dd> <p> Use this command when you want to synchronize the local repository with one or more of its remotes. You can specify the remotes to sync with; the default is to sync with all remotes. Or specify <code>--fast</code> to sync with the remotes with the lowest annex-cost value. </p>
 </dd>
<dd> <p> The sync process involves first committing all local changes, then fetching and merging the <code>synced/master</code> and the <code>git-annex</code> branch from the remote repositories, and finally pushing the changes back to those branches on the remote repositories. You can use standard git commands to do each of those steps by hand, or if you don&#8217;t want to worry about the details, you can use sync. </p>
 </dd>
<dd> <p> Merge conflicts are automatically handled by sync. When two conflicting versions of a file have been committed, both will be added to the tree, under different filenames. For example, file &quot;foo&quot; would be replaced with &quot;foo.somekey&quot; and &quot;foo.otherkey&quot;. </p>
 </dd>
<dd> <p> Note that syncing with a remote will not update the remote&#8217;s working tree with changes made to the local repository. However, those changes are pushed to the remote, so they can be merged into its working tree by running &quot;git annex sync&quot; on the remote. </p>
 </dd>
<dd> <p> With the <code>--content</code> option, the contents of annexed files in the work tree will also be uploaded and downloaded from remotes. By default, this tries to get each annexed file that the local repository does not yet have, and then copies each file to every remote that it is syncing with. This behavior can be overridden by configuring the preferred content of a repository. See see PREFERRED CONTENT below. </p>
 </dd>
<dd>  </dd>
<dt><code>merge</code></dt>
<dd> <p> This performs the same merging that is done by the sync command, but without pushing or pulling any data. </p>
 </dd>
<dd> <p> One way to use this is to put <code>git annex merge</code> into a repository&#8217;s post-receive hook. Then any syncs to the repository will update its working copy automatically. </p>
 </dd>
<dd>  </dd>
<dt><code>mirror [path ...]</code></dt>
<dd> <p> This causes a destination repository to mirror a source repository. </p>
 </dd>
<dd> <p> To use the local repository as the source repository, specify mirror <code>--to</code> remote. </p>
 </dd>
<dd> <p> To use a remote as the source repository, specify mirror <code>--from</code> remote. </p>
 </dd>
<dd> <p> Each specified file in the source repository is mirrored to the destination repository. If a file&#8217;s content is present in the source repository, it is copied to the destination repository. If a file&#8217;s content is not present in the source repository, it will be dropped from the destination repository when the numcopies setting allows. </p>
 </dd>
<dd> <p> Note that mirror does not sync the git repository, but only the file contents. </p>
 </dd>
<dd> <p> Also, --all may be specified to mirror all objects stored in the git annex, not only objects used by currently existing files. However, this bypasses checking the .gitattributes annex.numcopies setting when dropping files. </p>
 </dd>
<dd>  </dd>
<dt><code>addurl [url ...]</code></dt>
<dd> <p> Downloads each url to its own file, which is added to the annex. </p>
 </dd>
<dd> <p> To avoid immediately downloading the url, specify <code>--fast</code>. </p>
 </dd>
<dd> <p> To avoid storing the size of the url&#8217;s content, and accept whatever is there at a future point, specify <code>--relaxed</code>. (Implies <code>--fast</code>.) </p>
 </dd>
<dd> <p> Normally the filename is based on the full url, so will look like &quot;<a rel="nofollow" href="http://www.example.com_dir_subdir_bigfile">www.example.com_dir_subdir_bigfile</a>&quot;. For a shorter filename, specify <code>--pathdepth=N</code>. For example, <code>--pathdepth=1</code> will use &quot;dir/subdir/bigfile&quot;, while <code>--pathdepth=3</code> will use &quot;bigfile&quot;. It can also be negative; <code>--pathdepth=-2</code> will use the last two parts of the url. </p>
 </dd>
<dd> <p> Or, to directly specify what file the url is added to, specify <code>--file</code>. This changes the behavior; now all the specified urls are recorded as alternate locations from which the file can be downloaded. In this mode, addurl can be used both to add new files, or to add urls to existing files. </p>
 </dd>
<dd> <p> When quvi is installed, urls are automatically tested to see if they point to a video hosting site, and the video is downloaded instead. </p>
 </dd>
<dd>  </dd>
<dt><code>rmurl file url</code></dt>
<dd> <p> Record that the file is no longer available at the url. </p>
 </dd>
<dd>  </dd>
<dt><code>import [path ...]</code></dt>
<dd> <p> Moves files from somewhere outside the git working copy, and adds them to the annex. Individual files to import can be specified. If a directory is specified, the entire directory is imported. </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex import&nbsp;<wbr>/media/camera/DCIM/* </p>
 </dd>
<dd> <p> By default, importing two files with the same contents from two different locations will result in both files being added to the repository. (With all checksumming backends, including the default SHA256E, only one copy of the data will be stored.) </p>
 </dd>
<dd> <p> To not delete files from the import location, use the <code>--duplicate</code> option. This could allow importing the same files repeatedly to different locations in a repository. More likely, it could be used to import the same files to a number of different branches or separate git repositories. </p>
 </dd>
<dd> <p> To only import files whose content has not been seen before by git-annex, use the <code>--deduplicate</code> option. Duplicate files will be deleted from the import location. </p>
 </dd>
<dd> <p> To only import files whose content has not been seen before by git-annex, but avoid deleting duplicate files, use the <code>--skip-duplicates</code> option. </p>
 </dd>
<dd> <p> The <code>--clean-duplicates</code> option does not import any new files, but any files found in the import location that are duplicates of content in the annex are deleted. </p>
 </dd>
<dd> <p> (Note that using <code>--deduplicate</code> or <code>--clean-duplicates</code> with the WORM backend does not look at file content, but filename and mtime.) </p>
 </dd>
<dd>  </dd>
<dt><code>importfeed [url ...]</code></dt>
<dd> <p> Imports the contents of podcast feeds. Only downloads files whose urls have not already been added to the repository before, so you can delete, rename, etc the resulting files and repeated runs won&#8217;t duplicate them. (Use <code>--force</code> to force downloading urls it&#8217;s seen before.) </p>
 </dd>
<dd> <p> Use <code>--template</code> to control where the files are stored. The default template is &#8216;${feedtitle}/${itemtitle}${extension}&#8216; (Other available variables: feedauthor, itemauthor, itemsummary, itemdescription, itemrights, itemid) </p>
 </dd>
<dd> <p> The <code>--relaxed</code> and <code>--fast</code> options behave the same as they do in addurl. </p>
 </dd>
<dd> <p> When quvi is installed, links in the feed are tested to see if they are on a video hosting site, and the video is downloaded. This allows importing eg, youtube playlists. </p>
 </dd>
<dd>  </dd>
<dt><code>watch</code></dt>
<dd> <p> Watches for changes to files in the current directory and its subdirectories, and takes care of automatically adding new files, as well as dealing with deleted, copied, and moved files. With this running as a daemon in the background, you no longer need to manually run git commands when manipulating your files. </p>
 </dd>
<dd> <p> By default, all files in the directory will be added to the repository. (Including dotfiles.) To block some files from being added, use <code>.gitignore</code> files. </p>
 </dd>
<dd> <p> By default, all files that are added are added to the annex, the same as when you run <code>git annex add</code>. If you configure annex.largefiles, files that it does not match will instead be added with <code>git add</code>. </p>
 </dd>
<dd> <p> To not daemonize, run with <code>--foreground</code> ; to stop a running daemon, run with <code>--stop</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>assistant</code></dt>
<dd> <p> Like watch, but also automatically syncs changes to other remotes. Typically started at boot, or when you log in. </p>
 </dd>
<dd> <p> With the <code>--autostart</code> option, the assistant is started in any repositories it has created. These are listed in <code>~/.config/git-annex/autostart</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>webapp</code></dt>
<dd> <p> Opens a web app, that allows easy setup of a git-annex repository, and control of the git-annex assistant. </p>
 </dd>
<dd> <p> By default, the webapp can only be accessed from localhost, and running it opens a browser window. </p>
 </dd>
<dd> <p> With the <code>--listen=address[:port]</code> option, the webapp can be made to listen for connections on the specified address. This disables running a local web browser, and outputs the url you can use to open the webapp from a remote computer. Note that this does not yet use HTTPS for security, so use with caution! </p>
 </dd>
<dd>  </dd></dl>
<h2>REPOSITORY SETUP COMMANDS</h2>
<dl>
<dt><code>init [description]</code></dt>
<dd>  </dd>
<dd> <p> Until a repository (or one of its remotes) has been initialized, git-annex will refuse to operate on it, to avoid accidentally using it in a repository that was not intended to have an annex. </p>
 </dd>
<dd> <p> It&#8217;s useful, but not mandatory, to initialize each new clone of a repository with its own description. If you don&#8217;t provide one, one will be generated using the username, hostname and the path. </p>
 </dd>
<dd>  </dd>
<dt><code>describe repository description</code></dt>
<dd> <p> Changes the description of a repository. </p>
 </dd>
<dd> <p> The repository to describe can be specified by git remote name or by uuid. To change the description of the current repository, use &quot;here&quot;. </p>
 </dd>
<dd>  </dd>
<dt><code>initremote name [param=value ...]</code></dt>
<dd> <p> Creates a new special remote, and adds it to <code>.git/config</code>. </p>
 </dd>
<dd> <p> The remote&#8217;s configuration is specified by the parameters. Different types of special remotes need different configuration values. The command will prompt for parameters as needed. </p>
 </dd>
<dd> <p> All special remotes support encryption. You can either specify <code>encryption=none</code> to disable encryption, or specify <code>encryption=hybrid keyid=$keyid ...</code> to specify a GPG key id (or an email address associated with a key). </p>
 </dd>
<dd> <p> There are actually three schemes that can be used for management of the encryption keys. When using the encryption=hybrid scheme, additional GPG keys can be given access to the encrypted special remote easily (without re-encrypting everything). When using encryption=shared, a shared key is generated and stored in the git repository, allowing anyone who can clone the git repository to access it. Finally, when using encryption=pubkey, content in the special remote is directly encrypted to the specified GPG keys, and additional ones cannot easily be given access. </p>
 </dd>
<dd> <p> Note that with encryption enabled, a cryptographic key is created. This requires sufficient entropy. If initremote seems to hang or take a long time while generating the key, you may want to Ctrl-c it and re-run with <code>--fast</code>, which causes it to use a lower-quality source of randomness. </p>
 </dd>
<dd> <p> Example Amazon S3 remote: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex initremote mys3 type=S3 encryption=hybrid keyid=me [at] example.com datacenter=EU </p>
 </dd>
<dd>  </dd>
<dt><code>enableremote name [param=value ...]</code></dt>
<dd> <p> Enables use of an existing special remote in the current repository, which may be a different repository than the one in which it was originally created with the initremote command. </p>
 </dd>
<dd> <p> The name of the remote is the same name used when originally creating that remote with &quot;initremote&quot;. Run &quot;git annex enableremote&quot; with no parameters to get a list of special remote names. </p>
 </dd>
<dd> <p> Some special remotes may need parameters to be specified every time. For example, the directory special remote requires a directory= parameter. </p>
 </dd>
<dd> <p> This command can also be used to modify the configuration of an existing special remote, by specifying new values for parameters that were originally set when using initremote. (However, some settings such as the as the encryption scheme cannot be changed once a special remote has been created.) </p>
 </dd>
<dd> <p> The GPG keys that an encrypted special remote is encrypted with can be changed using the keyid+= and keyid-= parameters. These respectively add and remove keys from the list. However, note that removing a key does NOT necessarily prevent the key&#8217;s owner from accessing data in the encrypted special remote (which is by design impossible, short of deleting the remote). </p>
 </dd>
<dd> <p> One use-case of keyid-= is to replace a revoked key with a new key: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex enableremote mys3 keyid-=revokedkey keyid+=newkey </p>
 </dd>
<dd> <p> Also, note that for encrypted special remotes using plain public-key encryption (encryption=pubkey), adding or removing a key has NO effect on files that have already been copied to the remote. Hence using keyid+= and keyid-= with such remotes should be used with care, and make little sense except in cases like the revoked key example above. </p>
 </dd>
<dd>  </dd>
<dt><code>numcopies [N]</code></dt>
<dd> <p> Tells git-annex how many copies it should preserve of files, over all repositories. The default is 1. </p>
 </dd>
<dd> <p> Run without a number to get the current value. </p>
 </dd>
<dd> <p> When git-annex is asked to drop a file, it first verifies that the required number of copies can be satisfied amoung all the other repositories that have a copy of the file. </p>
 </dd>
<dd> <p> This can be overridden on a per-file basis by the annex.numcopies setting in .gitattributes files. </p>
 </dd>
<dd>  </dd>
<dt><code>trust [repository ...]</code></dt>
<dd> <p> Records that a repository is trusted to not unexpectedly lose content. Use with care. </p>
 </dd>
<dd> <p> To trust the current repository, use &quot;here&quot;. </p>
 </dd>
<dd>  </dd>
<dt><code>untrust [repository ...]</code></dt>
<dd> <p> Records that a repository is not trusted and could lose content at any time. </p>
 </dd>
<dd>  </dd>
<dt><code>semitrust [repository ...]</code></dt>
<dd> <p> Returns a repository to the default semi trusted state. </p>
 </dd>
<dd>  </dd>
<dt><code>dead [repository ...]</code></dt>
<dd> <p> Indicates that the repository has been irretrievably lost. (To undo, use semitrust.) </p>
 </dd>
<dd>  </dd>
<dt><code>group repository groupname</code></dt>
<dd> <p> Adds a repository to a group, such as &quot;archival&quot;, &quot;enduser&quot;, or &quot;transfer&quot;. The groupname must be a single word. </p>
 </dd>
<dd>  </dd>
<dt><code>ungroup repository groupname</code></dt>
<dd> <p> Removes a repository from a group. </p>
 </dd>
<dd>  </dd>
<dt><code>wanted repository [expression]</code></dt>
<dd> <p> When run with an expression, configures the content that is preferred to be held in the archive. See PREFERRED CONTENT below. </p>
 </dd>
<dd> <p> For example: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex wanted .&nbsp;<wbr>&quot;include=*.mp3 or include=*.ogg&quot; </p>
 </dd>
<dd> <p> Without an expression, displays the current preferred content setting of the repository. </p>
 </dd>
<dd>  </dd>
<dt><code>schedule repository [expression]</code></dt>
<dd> <p> When run with an expression, configures scheduled jobs to run at a particular time. This can be used to make the assistant periodically run incremental fscks. See SCHEDULED JOBS below. </p>
 </dd>
<dd>  </dd>
<dt><code>vicfg</code></dt>
<dd> <p> Opens EDITOR on a temp file containing most of the above configuration settings, and when it exits, stores any changes made back to the git-annex branch. </p>
 </dd>
<dd>  </dd>
<dt><code>direct</code></dt>
<dd> <p> Switches a repository to use direct mode, where rather than symlinks to files, the files are directly present in the repository. </p>
 </dd>
<dd> <p> As part of the switch to direct mode, any changed files will be committed. </p>
 </dd>
<dd> <p> Note that git commands that operate on the work tree are often unsafe to use in direct mode repositories, and can result in data loss or other bad behavior. </p>
 </dd>
<dd>  </dd>
<dt><code>indirect</code></dt>
<dd> <p> Switches a repository back from direct mode to the default, indirect mode. </p>
 </dd>
<dd> <p> As part of the switch from direct mode, any changed files will be committed. </p>
 </dd>
<dd>  </dd></dl>
<h2>REPOSITORY MAINTENANCE COMMANDS</h2>
<dl>
<dt><code>fsck [path ...]</code></dt>
<dd>  </dd>
<dd> <p> With no parameters, this command checks the whole annex for consistency, and warns about or fixes any problems found. This is a good compliment to <code>git fsck</code>. </p>
 </dd>
<dd> <p> With parameters, only the specified files are checked. </p>
 </dd>
<dd> <p> To check a remote to fsck, specify <code>--from</code>. </p>
 </dd>
<dd> <p> To avoid expensive checksum calculations (and expensive transfers when fscking a remote), specify <code>--fast</code>. </p>
 </dd>
<dd> <p> To start a new incremental fsck, use the <code>--incremental</code> option. Then the next time you fsck, you can instead use the <code>--more</code> option to skip over files that have already been checked, and continue where it left off. </p>
 </dd>
<dd> <p> The <code>--incremental-schedule</code> option makes a new incremental fsck be started a configurable time after the last incremental fsck was started. Once the current incremental fsck has completely finished, it causes a new one to start. </p>
 </dd>
<dd> <p> Maybe you&#8217;d like to run a fsck for 5 hours at night, picking up each night where it left off. You&#8217;d like this to continue until all files have been fscked. And once it&#8217;s done, you&#8217;d like a new fsck pass to start, but no more often than once a month. Then put this in a nightly cron job: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex fsck --incremental-schedule 30d --time-limit 5h </p>
 </dd>
<dd> <p> To verify data integrity only while disregarding required number of copies, use <code>--numcopies=1</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>unused</code></dt>
<dd> <p> Checks the annex for data that does not correspond to any files present in any tag or branch, and prints a numbered list of the data. </p>
 </dd>
<dd> <p> To only show unused temp and bad files, specify <code>--fast</code>. </p>
 </dd>
<dd> <p> To check for annexed data on a remote, specify <code>--from</code>. </p>
 </dd>
<dd> <p> After running this command, you can use the <code>--unused</code> option to operate on all the unused data that was found. For example, to move all unused data to origin: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex unused;&nbsp;<wbr>git annex move --unused --to origin </p>
 </dd>
<dd>  </dd>
<dt><code>dropunused [number|range ...]</code></dt>
<dd> <p> Drops the data corresponding to the numbers, as listed by the last <code>git annex unused</code> </p>
 </dd>
<dd> <p> You can also specify ranges of numbers, such as &quot;1-1000&quot;. Or, specify &quot;all&quot; to drop all unused data. </p>
 </dd>
<dd> <p> To drop the data from a remote, specify <code>--from.</code> </p>
 </dd>
<dd>  </dd>
<dt><code>addunused [number|range ...]</code></dt>
<dd> <p> Adds back files for the content corresponding to the numbers or ranges, as listed by the last <code>git annex unused</code>. The files will have names starting with &quot;unused.&quot; </p>
 </dd>
<dd>  </dd>
<dt><code>fix [path ...]</code></dt>
<dd> <p> Fixes up symlinks that have become broken to again point to annexed content. This is useful to run if you have been moving the symlinks around, but is done automatically when committing a change with git too. </p>
 </dd>
<dd>  </dd>
<dt><code>upgrade</code></dt>
<dd> <p> Upgrades the repository to current layout. </p>
 </dd>
<dd>  </dd>
<dt><code>forget</code></dt>
<dd> <p> Causes the git-annex branch to be rewritten, throwing away historical data about past locations of files. The resulting branch will use less space, but <code>git annex log</code> will not be able to show where files used to be located. </p>
 </dd>
<dd> <p> To also prune references to repositories that have been marked as dead, specify <code>--drop-dead</code>. </p>
 </dd>
<dd> <p> When this rewritten branch is merged into other clones of the repository, <code>git-annex</code> will automatically perform the same rewriting to their local <code>git-annex</code> branches. So the forgetfulness will automatically propagate out from its starting point until all repositories running git-annex have forgotten their old history. (You may need to force git to push the branch to any git repositories not running git-annex.) </p>
 </dd>
<dd>  </dd>
<dt><code>repair</code></dt>
<dd> <p> This can repair many of the problems with git repositories that <code>git fsck</code> detects, but does not itself fix. It&#8217;s useful if a repository has become badly damaged. One way this can happen is if a repository used by git-annex is on a removable drive that gets unplugged at the wrong time. </p>
 </dd>
<dd> <p> This command can actually be used inside git repositories that do not use git-annex at all; when used in a repository using git-annex, it does additional repairs of the git-annex branch. </p>
 </dd>
<dd> <p> It works by deleting any corrupt objects from the git repository, and retrieving all missing objects it can from the remotes of the repository. </p>
 </dd>
<dd> <p> If that is not sufficient to fully recover the repository, it can also reset branches back to commits before the corruption happened, delete branches that are no longer available due to the lost data, and remove any missing files from the index. It will only do this if run with the <code>--force</code> option, since that rewrites history and throws out missing data. Note that the <code>--force</code> option never touches tags, even if they are no longer usable due to missing data. </p>
 </dd>
<dd> <p> After running this command, you will probably want to run <code>git fsck</code> to verify it fixed the repository. Note that fsck may still complain about objects referenced by the reflog, or the stash, if they were unable to be recovered. This command does not try to clean up either the reflog or the stash. </p>
 </dd>
<dd> <p> It is also a good idea to run <code>git annex fsck --fast</code> after this command, to make sure that the git-annex branch reflects reality. </p>
 </dd>
<dd>  </dd></dl>
<h2>QUERY COMMANDS</h2>
<dl>
<dt><code>find [path ...]</code></dt>
<dd>  </dd>
<dd> <p> Outputs a list of annexed files in the specified path. With no path, finds files in the current directory and its subdirectories. </p>
 </dd>
<dd> <p> By default, only lists annexed files whose content is currently present. This can be changed by specifying matching options. To list all annexed files, present or not, specify <code>--include &quot;*&quot;</code>. To list all annexed files whose content is not present, specify <code>--not --in=here</code> </p>
 </dd>
<dd> <p> To output filenames terminated with nulls, for use with xargs -0, specify <code>--print0</code>. Or, a custom output formatting can be specified using <code>--format</code>. The default output format is the same as <code>--format=&#8216;${file}\n&#8217;</code> </p>
 </dd>
<dd> <p> These variables are available for use in formats: file, key, backend, bytesize, humansize, keyname, hashdirlower, hashdirmixed, mtime. </p>
 </dd>
<dd>  </dd>
<dt><code>whereis [path ...]</code></dt>
<dd> <p> Displays a information about where the contents of files are located. </p>
 </dd>
<dd>  </dd>
<dt><code>list [path ...]</code></dt>
<dd> <p> Displays a table of remotes that contain the contents of the specified files. This is similar to whereis but a more compact display. Only configured remotes are shown by default; specify --allrepos to list all repositories. </p>
 </dd>
<dd>  </dd>
<dt><code>log [path ...]</code></dt>
<dd> <p> Displays the location log for the specified file or files, showing each repository they were added to (&quot;+&quot;) and removed from (&quot;-&quot;). </p>
 </dd>
<dd> <p> To limit how far back to search for location log changes, the options <code>--since</code>, <code>--after</code>, <code>--until</code>, <code>--before</code>, and <code>--max-count</code> can be specified. They are passed through to git log. For example, <code>--since &quot;1 month ago&quot;</code> </p>
 </dd>
<dd> <p> To generate output suitable for the gource visualization program, specify <code>--gource</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>info [directory ...]</code></dt>
<dd> <p> Displays some statistics and other information, including how much data is in the annex and a list of all known repositories. </p>
 </dd>
<dd> <p> To only show the data that can be gathered quickly, use <code>--fast</code>. </p>
 </dd>
<dd> <p> When a directory is specified, shows a differently formatted info display for that directory. In this mode, all of the matching options can be used to filter the files that will be included in the information. </p>
 </dd>
<dd> <p> For example, suppose you want to run &quot;git annex get .&quot;, but would first like to see how much disk space that will use. Then run: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex info --fast . --not --in here </p>
 </dd>
<dd>  </dd>
<dt><code>version</code></dt>
<dd> <p> Shows the version of git-annex, as well as repository version information. </p>
 </dd>
<dd>  </dd>
<dt><code>map</code></dt>
<dd> <p> Helps you keep track of your repositories, and the connections between them, by going out and looking at all the ones it can get to, and generating a Graphviz file displaying it all. If the <code>dot</code> command is available, it is used to display the file to your screen (using x11 backend). (To disable this display, specify <code>--fast</code>) </p>
 </dd>
<dd> <p> This command only connects to hosts that the host it&#8217;s run on can directly connect to. It does not try to tunnel through intermediate hosts. So it might not show all connections between the repositories in the network. </p>
 </dd>
<dd> <p> Also, if connecting to a host requires a password, you might have to enter it several times as the map is being built. </p>
 </dd>
<dd> <p> Note that this subcommand can be used to graph any git repository; it is not limited to git-annex repositories. </p>
 </dd>
<dd>  </dd></dl>
<h2>METADATA COMMANDS</h2>
<dl>
<dt><code>metadata [path ...] [-s field=value -s field+=value -s field-=value ...]</code></dt>
<dd>  </dd>
<dd> <p> Each file can have any number of metadata fields attached to it, which each in turn have any number of values. This sets metadata for the specified file or files, or if run without any values, shows the current metadata. </p>
 </dd>
<dd> <p> To set a field&#8217;s value, removing any old value(s), use -s field=value. </p>
 </dd>
<dd> <p> To add an additional value, use -s field+=value. </p>
 </dd>
<dd> <p> To remove a value, use -s field-=value. </p>
 </dd>
<dd> <p> To set a tag, use -t tag, and use -u tag to remove a tag. </p>
 </dd>
<dd> <p> For example, to set some tags on a file and also its author: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex metadata annexscreencast.ogv -t video -t screencast -s author+=Alice </p>
 </dd>
<dd>  </dd>
<dt><code>view [field=value ...] [tag ...]</code></dt>
<dd> <p> Uses metadata to build a view branch of the files in the current branch, and checks out the view branch. Only files in the current branch whose metadata matches all the specified field values and tags will be shown in the view. </p>
 </dd>
<dd> <p> Multiple values for a metadata field can be specified, either by using a glob (<code>field=&quot;*&quot;</code>) or by listing each wanted value. The resulting view will put files in subdirectories according to the value of their fields. </p>
 </dd>
<dd> <p> Once within a view, you can make additional directories, and copy or move files into them. When you commit, the metadata will be updated to correspond to your changes. </p>
 </dd>
<dd>  </dd>
<dt><code>vpop [N]</code></dt>
<dd> <p> Switches from the currently active view back to the previous view. Or, from the first view back to original branch. </p>
 </dd>
<dd> <p> The optional number tells how many views to pop. </p>
 </dd>
<dd>  </dd>
<dt><code>vfilter [field=value ...] [tag ...]</code></dt>
<dd> <p> Filters the current view to only the files that have the specified values and tags. </p>
 </dd>
<dd>  </dd>
<dt><code>vadd [field=glob ...]</code></dt>
<dd> <p> Changes the current view, adding an additional level of directories to categorize the files. </p>
 </dd>
<dd> <p> For example, when the view is by author/tag, <code>vadd year=*</code> will change it to year/author/tag. </p>
 </dd>
<dd> <p> So will <code>vadd year=2014 year=2013</code>, but limiting the years in view to only those two. </p>
 </dd>
<dd>  </dd>
<dt><code>vcycle</code></dt>
<dd> <p> When a view involves nested subdirectories, this cycles the order. </p>
 </dd>
<dd> <p> For example, when the view is by year/author/tag, <code>vcycle</code> will switch it to author/tag/year. </p>
 </dd>
<dd>  </dd></dl>
<h2>UTILITY COMMANDS</h2>
<dl>
<dt><code>migrate [path ...]</code></dt>
<dd>  </dd>
<dd> <p> Changes the specified annexed files to use the default key-value backend (or the one specified with <code>--backend</code>). Only files whose content is currently available are migrated. </p>
 </dd>
<dd> <p> Note that the content is also still available using the old key after migration. Use <code>git annex unused</code> to find and remove the old key. </p>
 </dd>
<dd> <p> Normally, nothing will be done to files already using the new backend. However, if a backend changes the information it uses to construct a key, this can also be used to migrate files to use the new key format. </p>
 </dd>
<dd>  </dd>
<dt><code>reinject src dest</code></dt>
<dd> <p> Moves the src file into the annex as the content of the dest file. This can be useful if you have obtained the content of a file from elsewhere and want to put it in the local annex. </p>
 </dd>
<dd> <p> Automatically runs fsck on dest to check that the expected content was provided. </p>
 </dd>
<dd> <p> Example: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex reinject&nbsp;<wbr>/tmp/foo.iso foo.iso </p>
 </dd>
<dd>  </dd>
<dt><code>unannex [path ...]</code></dt>
<dd> <p> Use this to undo an accidental <code>git annex add</code> command. It puts the file back how it was before the add. </p>
 </dd>
<dd> <p> Note that for safety, the content of the file remains in the annex, until you use <code>git annex unused</code> and <code>git annex dropunused</code>. </p>
 </dd>
<dd> <p> This is not the command you should use if you intentionally annexed a file and don&#8217;t want its contents any more. In that case you should use <code>git annex drop</code> instead, and you can also <code>git rm</code> the file. </p>
 </dd>
<dd> <p> Normally this does a slow copy of the file. In <code>--fast</code> mode, it instead makes a hard link from the file to the content in the annex. But use --fast mode with caution, because editing the file will change the content in the annex. </p>
 </dd>
<dd>  </dd>
<dt><code>uninit</code></dt>
<dd> <p> Use this to stop using git annex. It will unannex every file in the repository, and remove all of git-annex&#8217;s other data, leaving you with a git repository plus the previously annexed files. </p>
 </dd>
<dd>  </dd></dl>
<h2>PLUMBING COMMANDS</h2>
<dl>
<dt><code>pre-commit [path ...]</code></dt>
<dd>  </dd>
<dd> <p> This is meant to be called from git&#8217;s pre-commit hook. <code>git annex init</code> automatically creates a pre-commit hook using this. </p>
 </dd>
<dd> <p> Fixes up symlinks that are staged as part of a commit, to ensure they point to annexed content. Also handles injecting changes to unlocked files into the annex. When in a view, updates metadata to reflect changes made to files in the view. </p>
 </dd>
<dd>  </dd>
<dt><code>lookupkey [file ...]</code></dt>
<dd> <p> This plumbing-level command looks up the key used for a file in the index. The key is output to stdout. If there is no key (because the file is not present in the index, or is not a git-annex managed file), nothing is output, and it exits nonzero. </p>
 </dd>
<dd>  </dd>
<dt><code>examinekey [key ...]</code></dt>
<dd> <p> This plumbing-level command is given a key, and prints information that can be determined purely by looking at the key. </p>
 </dd>
<dd> <p> To specify what information to print, use <code>--format</code>. Or use <code>--json</code> to get all available information in JSON format. </p>
 </dd>
<dd> <p> The same variables can be used in the format string as can be used in the format string of git annex find (except there is no file option here). </p>
 </dd>
<dd> <p> For example, the location a key&#8217;s value is stored (in indirect mode) can be looked up by running: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>git annex examinekey --format=&#8216;.git/annex/objects/${hashdirmixed}${key}/${key}&#8216; </p>
 </dd>
<dd>  </dd>
<dt><code>fromkey key file</code></dt>
<dd> <p> This plumbing-level command can be used to manually set up a file in the git repository to link to a specified key. </p>
 </dd>
<dd>  </dd>
<dt><code>dropkey [key ...]</code></dt>
<dd> <p> This plumbing-level command drops the annexed data for the specified keys from this repository. </p>
 </dd>
<dd> <p> This can be used to drop content for arbitrary keys, which do not need to have a file in the git repository pointing at them. </p>
 </dd>
<dd>  </dd>
<dt><code>transferkey</code></dt>
<dd> <p> This plumbing-level command is used to request a single key be transferred. Either the --from or the --to option can be used to specify the remote to use. A --file option can be used to hint at the file associated with the key. </p>
 </dd>
<dd>  </dd>
<dt><code>transferkeys</code></dt>
<dd> <p> This plumbing-level command is used by the assistant to transfer data. It is fed instructions about the keys to transfer using an internal stdio protocol, which is intentionally not documented (as it may change at any time). </p>
 </dd>
<dd>  </dd>
<dt><code>rekey [file key ...]</code></dt>
<dd> <p> This plumbing-level command is similar to migrate, but you specify both the file, and the new key to use for it. </p>
 </dd>
<dd> <p> With <code>--force</code>, even files whose content is not currently available will be rekeyed. Use with caution. </p>
 </dd>
<dd>  </dd>
<dt><code>test</code></dt>
<dd> <p> This runs git-annex&#8217;s built-in test suite. </p>
 </dd>
<dd> <p> There are several parameters, provided by Haskell&#8217;s tasty test framework. </p>
 </dd>
<dd>  </dd>
<dt><code>xmppgit</code></dt>
<dd> <p> This command is used internally to perform git pulls over XMPP. </p>
 </dd>
<dd>  </dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>--force</code></dt>
<dd>  </dd>
<dd> <p> Force unsafe actions, such as dropping a file&#8217;s content when no other source of it can be verified to still exist, or adding ignored files. Use with care. </p>
 </dd>
<dd>  </dd>
<dt><code>--fast</code></dt>
<dd> <p> Enable less expensive, but also less thorough versions of some commands. What is avoided depends on the command. </p>
 </dd>
<dd>  </dd>
<dt><code>--auto</code></dt>
<dd> <p> Enable automatic mode. Commands that get, drop, or move file contents will only do so when needed to help satisfy the setting of numcopies, and preferred content configuration. </p>
 </dd>
<dd>  </dd>
<dt><code>--all</code></dt>
<dd> <p> Operate on all data that has been stored in the git annex, including old versions of files. This is the default behavior when running git-annex in a bare repository; in a non-bare repository the normal behavior is to only operate on specified files in the working tree. </p>
 </dd>
<dd>  </dd>
<dt><code>--unused</code></dt>
<dd> <p> Operate on all data that has been determined to be unused by a previous run of <code>git-annex unused</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>--key=key</code></dt>
<dd> <p> Operate on only the specified key. </p>
 </dd>
<dd>  </dd>
<dt><code>--quiet</code></dt>
<dd> <p> Avoid the default verbose display of what is done; only show errors and progress displays. </p>
 </dd>
<dd>  </dd>
<dt><code>--verbose</code></dt>
<dd> <p> Enable verbose display. </p>
 </dd>
<dd>  </dd>
<dt><code>--json</code></dt>
<dd> <p> Rather than the normal output, generate JSON. This is intended to be parsed by programs that use git-annex. Each line of output is a JSON object. Note that JSON output is only usable with some git-annex commands, like info, find, and whereis. </p>
 </dd>
<dd>  </dd>
<dt><code>--debug</code></dt>
<dd> <p> Show debug messages. </p>
 </dd>
<dd>  </dd>
<dt><code>--no-debug</code></dt>
<dd> <p> Disable debug messages. </p>
 </dd>
<dd>  </dd>
<dt><code>--from=repository</code></dt>
<dd> <p> Specifies a repository that content will be retrieved from, or that should otherwise be acted on. </p>
 </dd>
<dd> <p> It should be specified using the name of a configured remote. </p>
 </dd>
<dd>  </dd>
<dt><code>--to=repository</code></dt>
<dd> <p> Specifies a repository that content will be sent to. </p>
 </dd>
<dd> <p> It should be specified using the name of a configured remote. </p>
 </dd>
<dd>  </dd>
<dt><code>--numcopies=n</code></dt>
<dd> <p> Overrides the numcopies setting, forcing git-annex to ensure the specified number of copies exist. </p>
 </dd>
<dd> <p> Note that setting numcopies to 0 is very unsafe. </p>
 </dd>
<dd>  </dd>
<dt><code>--time-limit=time</code></dt>
<dd> <p> Limits how long a git-annex command runs. The time can be something like &quot;5h&quot;, or &quot;30m&quot; or even &quot;45s&quot; or &quot;10d&quot;. </p>
 </dd>
<dd> <p> Note that git-annex may continue running a little past the specified time limit, in order to finish processing a file. </p>
 </dd>
<dd> <p> Also, note that if the time limit prevents git-annex from doing all it was asked to, it will exit with a special code, 101. </p>
 </dd>
<dd>  </dd>
<dt><code>--trust=repository</code></dt>
<dd>  </dd>
<dt><code>--semitrust=repository</code></dt>
<dd>  </dd>
<dt><code>--untrust=repository</code></dt>
<dd> <p> Overrides trust settings for a repository. May be specified more than once. </p>
 </dd>
<dd> <p> The repository should be specified using the name of a configured remote, or the UUID or description of a repository. </p>
 </dd>
<dd>  </dd>
<dt><code>--trust-glacier-inventory</code></dt>
<dd> <p> Amazon Glacier inventories take hours to retrieve, and may not represent the current state of a repository. So git-annex does not trust that files that the inventory claims are in Glacier are really there. This switch can be used to allow it to trust the inventory. </p>
 </dd>
<dd> <p> Be careful using this, especially if you or someone else might have recently removed a file from Glacier. If you try to drop the only other copy of the file, and this switch is enabled, you could lose data! </p>
 </dd>
<dd>  </dd>
<dt><code>--backend=name</code></dt>
<dd> <p> Specifies which key-value backend to use. This can be used when adding a file to the annex, or migrating a file. Once files are in the annex, their backend is known and this option is not necessary. </p>
 </dd>
<dd>  </dd>
<dt><code>--format=value</code></dt>
<dd> <p> Specifies a custom output format. The value is a format string, in which &#8216;${var}&#8216; is expanded to the value of a variable. To right-justify a variable with whitespace, use &#8216;${var;width}&#8216; ; to left-justify a variable, use &#8216;${var;-width}&#8216;; to escape unusual characters in a variable, use &#8216;${escaped_var}&#8216; </p>
 </dd>
<dd> <p> Also, &#8216;\n&#8217; is a newline, &#8216;\000&#8217; is a NULL, etc. </p>
 </dd>
<dd>  </dd>
<dt><code>--user-agent=value</code></dt>
<dd> <p> Overrides the User-Agent to use when downloading files from the web. </p>
 </dd>
<dd>  </dd>
<dt><code>-c name=value</code></dt>
<dd> <p> Overrides git configuration settings. May be specified multiple times. </p>
 </dd>
<dd>  </dd></dl>
<h2>MATCHING OPTIONS</h2>
<p> These options can all be specified multiple times, and can be combined to limit which files git-annex acts on. </p>
<p> Arbitrarily complicated expressions can be built using these options. For example: </p>
<p> <br />
&nbsp;<wbr>--exclude&nbsp;<wbr>&#8216;*.mp3&#8217;&nbsp;<wbr>--and --not -(&nbsp;<wbr>--in=usbdrive --or --in=archive -) </p>
<p> The above example prevents git-annex from working on mp3 files whose file contents are present at either of two repositories. </p>
<dl>
<dt><code>--exclude=glob</code></dt>
<dd> <p> Skips files matching the glob pattern. The glob is matched relative to the current directory. For example: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>--exclude=&#8216;*.mp3&#8217;&nbsp;<wbr>--exclude=&#8216;subdir/*&#8216; </p>
 </dd>
<dd> <p> Note that this will not match anything when using --all or --unused. </p>
 </dd>
<dd>  </dd>
<dt><code>--include=glob</code></dt>
<dd> <p> Skips files not matching the glob pattern. (Same as <code>--not --exclude</code>.) For example, to include only mp3 and ogg files: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>--include=&#8216;*.mp3&#8217;&nbsp;<wbr>--or --include=&#8216;*.ogg&#8217; </p>
 </dd>
<dd> <p> Note that this will not skip anything when using --all or --unused. </p>
 </dd>
<dd>  </dd>
<dt><code>--in=repository</code></dt>
<dd> <p> Matches only files that git-annex believes have their contents present in a repository. Note that it does not check the repository to verify that it still has the content. </p>
 </dd>
<dd> <p> The repository should be specified using the name of a configured remote, or the UUID or description of a repository. For the current repository, use <code>--in=here</code> </p>
 </dd>
<dd>  </dd>
<dt><code>--in=repository@{date}</code></dt>
<dd> <p> Matches files currently in the work tree whose content was present in the repository on the given date. </p>
 </dd>
<dd> <p> The date is specified in the same syntax documented in <a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a>(7). Note that this uses the reflog, so dates far in the past cannot be queried. </p>
 </dd>
<dd> <p> For example, you might need to run <code>git annex drop .</code> to temporarily free up disk space. The next day, you can get back the files you dropped using <code>git annex get . --in=here@{yesterday}</code> </p>
 </dd>
<dd>  </dd>
<dt><code>--copies=number</code></dt>
<dd> <p> Matches only files that git-annex believes to have the specified number of copies, or more. Note that it does not check remotes to verify that the copies still exist. </p>
 </dd>
<dd>  </dd>
<dt><code>--copies=trustlevel:number</code></dt>
<dd> <p> Matches only files that git-annex believes have the specified number of copies, on remotes with the specified trust level. For example, <code>--copies=trusted:2</code> </p>
 </dd>
<dd> <p> To match any trust level at or higher than a given level, use &#8216;trustlevel+&#8216;. For example, <code>--copies=semitrusted+:2</code> </p>
 </dd>
<dd>  </dd>
<dt><code>--copies=groupname:number</code></dt>
<dd> <p> Matches only files that git-annex believes have the specified number of copies, on remotes in the specified group. For example, <code>--copies=archive:2</code> </p>
 </dd>
<dd>  </dd>
<dt><code>--lackingcopies=number</code></dt>
<dd> <p> Matches only files that git-annex believes need the specified number or more additional copies to be made in order to satisfy their numcopies settings. </p>
 </dd>
<dd>  </dd>
<dt><code>--approxlackingcopies=number</code></dt>
<dd> <p> Like lackingcopies, but does not look at .gitattributes annex.numcopies settings. This makes it significantly faster. </p>
 </dd>
<dd>  </dd>
<dt><code>--inbackend=name</code></dt>
<dd> <p> Matches only files whose content is stored using the specified key-value backend. </p>
 </dd>
<dd>  </dd>
<dt><code>--inallgroup=groupname</code></dt>
<dd> <p> Matches only files that git-annex believes are present in all repositories in the specified group. </p>
 </dd>
<dd>  </dd>
<dt><code>--smallerthan=size</code></dt>
<dd>  </dd>
<dt><code>--largerthan=size</code></dt>
<dd> <p> Matches only files whose content is smaller than, or larger than the specified size. </p>
 </dd>
<dd> <p> The size can be specified with any commonly used units, for example, &quot;0.5 gb&quot; or &quot;100 KiloBytes&quot; </p>
 </dd>
<dd>  </dd>
<dt><code>--metadata field=value</code></dt>
<dd> <p> Matches only files that have a metadata field attached with the specified value. </p>
 </dd>
<dd>  </dd>
<dt><code>--want-get</code></dt>
<dd> <p> Matches files that the preferred content settings for the repository make it want to get. Note that this will match even files that are already present, unless limited with e.g., <code>--not --in .</code> </p>
 </dd>
<dd> <p> Note that this will not match anything when using --all or --unused. </p>
 </dd>
<dd>  </dd>
<dt><code>--want-drop</code></dt>
<dd> <p> Matches files that the preferred content settings for the repository make it want to drop. Note that this will match even files that have already been dropped, unless limited with e.g., <code>--in .</code> </p>
 </dd>
<dd> <p> Note that this will not match anything when using --all or --unused. </p>
 </dd>
<dd>  </dd>
<dt><code>--not</code></dt>
<dd> <p> Inverts the next matching option. For example, to only act on files with less than 3 copies, use <code>--not --copies=3</code> </p>
 </dd>
<dd>  </dd>
<dt><code>--and</code></dt>
<dd> <p> Requires that both the previous and the next matching option matches. The default. </p>
 </dd>
<dd>  </dd>
<dt><code>--or</code></dt>
<dd> <p> Requires that either the previous, or the next matching option matches. </p>
 </dd>
<dd>  </dd>
<dt><code>-(</code></dt>
<dd> <p> Opens a group of matching options. </p>
 </dd>
<dd>  </dd>
<dt><code>-)</code></dt>
<dd> <p> Closes a group of matching options. </p>
 </dd>
<dd>  </dd></dl>
<h2>PREFERRED CONTENT</h2>
<p> Each repository has a preferred content setting, which specifies content that the repository wants to have present. These settings can be configured using <code>git annex vicfg</code> or <code>git annex wanted</code>. They are used by the <code>--auto</code> option, and by the git-annex assistant. </p>
<p> The preferred content settings are similar, but not identical to the matching options specified above, just without the dashes. For example: </p>
<p> <br />
&nbsp;<wbr>exclude=archive/*&nbsp;<wbr>and&nbsp;<wbr>(include=*.mp3 or smallerthan=1mb) </p>
<p> The main differences are that <code>exclude=</code> and <code>include=</code> always match relative to the top of the git repository, and that there is no equivilant to <code>--in</code>. </p>
<p> When a repository is in one of the standard predefined groups, like &quot;backup&quot; and &quot;client&quot;, setting its preferred content to &quot;standard&quot; will use a built-in preferred content expression developed for that group. </p>
<h2>SCHEDULED JOBS</h2>
<p> The git-annex assistant daemon can be configured to run scheduled jobs. This is similar to cron and anacron (and you can use them if you prefer), but has the advantage of being integrated into git-annex, and so being able to e.g., fsck a repository on a removable drive when the drive gets connected. </p>
<p> The scheduled jobs can be configured using <code>git annex vicfg</code> or <code>git annex schedule</code>. </p>
<p> These actions are available: &quot;fsck self&quot;, &quot;fsck UUID&quot; (where UUID is the UUID of a remote to fsck). After the action comes the duration to allow the action to run, and finally the schedule of when to run it. </p>
<p> To schedule multiple jobs, separate them with &quot;; &quot;. </p>
<p> Some examples: </p>
<p> <br />
&nbsp;<wbr>fsck self 30m every day at any time <br />
&nbsp;<wbr>fsck self 1h every month at 3 AM <br />
&nbsp;<wbr>fsck self 1h on day 1 of every month at any time <br />
&nbsp;<wbr>fsck self 1h every week divisible by 2 at any time </p>
<h2>CONFIGURATION VIA .git/config</h2>
<p> Like other git commands, git-annex is configured via <code>.git/config</code>. Here are all the supported configuration settings. </p>
<dl>
<dt><code>annex.uuid</code></dt>
<dd> <p> A unique UUID for this repository (automatically set). </p>
 </dd>
<dd>  </dd>
<dt><code>annex.backends</code></dt>
<dd> <p> Space-separated list of names of the key-value backends to use. The first listed is used to store new files by default. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.diskreserve</code></dt>
<dd> <p> Amount of disk space to reserve. Disk space is checked when transferring content to avoid running out, and additional free space can be reserved via this option, to make space for more important content (such as git commit logs). Can be specified with any commonly used units, for example, &quot;0.5 gb&quot;, &quot;500M&quot;, or &quot;100 KiloBytes&quot; </p>
 </dd>
<dd> <p> The default reserve is 1 megabyte. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.largefiles</code></dt>
<dd> <p> Allows configuring which files <code>git annex add</code> and the assistant consider to be large enough to need to be added to the annex. By default, all files are added to the annex. </p>
 </dd>
<dd> <p> The value is a preferred content expression. See PREFERRED CONTENT for details. </p>
 </dd>
<dd> <p> Example: </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>annex.largefiles&nbsp;<wbr>=&nbsp;<wbr>largerthan=100kb and not&nbsp;<wbr>(include=*.c or include=*.h) </p>
 </dd>
<dd>  </dd>
<dt><code>annex.numcopies</code></dt>
<dd> <p> This is a deprecated setting. You should instead use the <code>git annex numcopies</code> command to configure how many copies of files are kept acros all repositories. </p>
 </dd>
<dd> <p> This config setting is only looked at when <code>git annex numcopies</code> has never been configured. </p>
 </dd>
<dd> <p> Note that setting numcopies to 0 is very unsafe. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.queuesize</code></dt>
<dd> <p> git-annex builds a queue of git commands, in order to combine similar commands for speed. By default the size of the queue is limited to 10240 commands; this can be used to change the size. If you have plenty of memory and are working with very large numbers of files, increasing the queue size can speed it up. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.bloomcapacity</code></dt>
<dd> <p> The <code>git annex unused</code> command uses a bloom filter to determine what data is no longer used. The default bloom filter is sized to handle up to 500000 keys. If your repository is larger than that, you can adjust this to avoid <code>git annex unused</code> not noticing some unused data files. Increasing this will make <code>git-annex unused</code> consume more memory; run <code>git annex info</code> for memory usage numbers. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.bloomaccuracy</code></dt>
<dd> <p> Adjusts the accuracy of the bloom filter used by <code>git annex unused</code>. The default accuracy is 1000 -- 1 unused file out of 1000 will be missed by <code>git annex unused</code>. Increasing the accuracy will make <code>git annex unused</code> consume more memory; run <code>git annex info</code> for memory usage numbers. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.sshcaching</code></dt>
<dd> <p> By default, git-annex caches ssh connections using ssh&#8217;s ControlMaster and ControlPersist settings (if built using a new enough ssh). To disable this, set to <code>false</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.alwayscommit</code></dt>
<dd> <p> By default, git-annex automatically commits data to the git-annex branch after each command is run. To disable these commits, set to <code>false</code>. Then data will only be committed when running <code>git annex merge</code> (or by automatic merges) or <code>git annex sync</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.delayadd</code></dt>
<dd> <p> Makes the watch and assistant commands delay for the specified number of seconds before adding a newly created file to the annex. Normally this is not needed, because they already wait for all writers of the file to close it. On Mac OSX, when not using direct mode this defaults to 1 second, to work around a bad interaction with software there. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.expireunused</code></dt>
<dd> <p> Controls what the assistant does about unused file contents that are stored in the repository. </p>
 </dd>
<dd> <p> The default is <code>false</code>, which causes all old and unused file contents to be retained, unless the assistant is able to move them to some other repository (such as a backup repository). </p>
 </dd>
<dd> <p> Can be set to a time specification, like &quot;7d&quot; or &quot;1m&quot;, and then file contents that have been known to be unused for a week or a month will be deleted. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.fscknudge</code></dt>
<dd> <p> When set to false, prevents the webapp from reminding you when using repositories that lack consistency checks. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.autoupgrade</code></dt>
<dd> <p> When set to ask (the default), the webapp will check for new versions and prompt if they should be upgraded to. When set to true, automatically upgrades without prompting (on some supported platforms). When set to false, disables any upgrade checking. </p>
 </dd>
<dd> <p> Note that upgrade checking is only done when git-annex is installed from one of the prebuilt images from its website. This does not bypass e.g., a Linux distribution&#8217;s own upgrade handling code. </p>
 </dd>
<dd> <p> This setting also controls whether to restart the git-annex assistant when the git-annex binary is detected to have changed. That is useful no matter how you installed git-annex. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.autocommit</code></dt>
<dd> <p> Set to false to prevent the git-annex assistant from automatically committing changes to files in the repository. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.debug</code></dt>
<dd> <p> Set to true to enable debug logging by default. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.version</code></dt>
<dd> <p> Automatically maintained, and used to automate upgrades between versions. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.direct</code></dt>
<dd> <p> Set to true when the repository is in direct mode. Should not be set manually; use the &quot;git annex direct&quot; and &quot;git annex indirect&quot; commands instead. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.crippledfilesystem</code></dt>
<dd> <p> Set to true if the repository is on a crippled filesystem, such as FAT, which does not support symbolic links, or hard links, or unix permissions. This is automatically probed by &quot;git annex init&quot;. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-cost</code></dt>
<dd> <p> When determining which repository to transfer annexed files from or to, ones with lower costs are preferred. The default cost is 100 for local repositories, and 200 for remote repositories. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-cost-command</code></dt>
<dd> <p> If set, the command is run, and the number it outputs is used as the cost. This allows varying the cost based on e.g., the current network. The cost-command can be any shell command line. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-start-command</code></dt>
<dd> <p> A command to run when git-annex begins to use the remote. This can be used to, for example, mount the directory containing the remote. </p>
 </dd>
<dd> <p> The command may be run repeatedly when multiple git-annex processes are running concurrently. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-stop-command</code></dt>
<dd> <p> A command to run when git-annex is done using the remote. </p>
 </dd>
<dd> <p> The command will only be run once *all* running git-annex processes are finished using the remote. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-ignore</code></dt>
<dd> <p> If set to <code>true</code>, prevents git-annex from storing file contents on this remote by default. (You can still request it be used by the <code>--from</code> and <code>--to</code> options.) </p>
 </dd>
<dd> <p> This is, for example, useful if the remote is located somewhere without git-annex-shell. (For example, if it&#8217;s on GitHub). Or, it could be used if the network connection between two repositories is too slow to be used normally. </p>
 </dd>
<dd> <p> This does not prevent git-annex sync (or the git-annex assistant) from syncing the git repository to the remote. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-sync</code></dt>
<dd> <p> If set to <code>false</code>, prevents git-annex sync (and the git-annex assistant) from syncing with this remote. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-readonly</code></dt>
<dd> <p> If set to <code>true</code>, prevents git-annex from making changes to a remote. This both prevents git-annex sync from pushing changes, and prevents storing or removing files from read-only remote. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annexUrl</code></dt>
<dd> <p> Can be used to specify a different url than the regular <code>remote.&lt;name&gt;.url</code> for git-annex to use when talking with the remote. Similar to the <code>pushUrl</code> used by git-push. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-uuid</code></dt>
<dd> <p> git-annex caches UUIDs of remote repositories here. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-trustlevel</code></dt>
<dd> <p> Configures a local trust level for the remote. This overrides the value configured by the trust and untrust commands. The value can be any of &quot;trusted&quot;, &quot;semitrusted&quot; or &quot;untrusted&quot;. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-availability</code></dt>
<dd> <p> Can be used to tell git-annex whether a remote is LocallyAvailable or GloballyAvailable. Normally, git-annex determines this automatically. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-bare</code></dt>
<dd> <p> Can be used to tell git-annex if a remote is a bare repository or not. Normally, git-annex determines this automatically. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-ssh-options</code></dt>
<dd> <p> Options to use when using ssh to talk to this remote. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-rsync-options</code></dt>
<dd> <p> Options to use when using rsync to or from this remote. For example, to force ipv6, and limit the bandwidth to 100Kbyte/s, set it to <code>-6 --bwlimit 100</code> </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-rsync-upload-options</code></dt>
<dd> <p> Options to use when using rsync to upload a file to a remote. </p>
 </dd>
<dd> <p> These options are passed after other applicable rsync options, so can be used to override them. For example, to limit upload bandwidth to 10Kbye/s, set <code>--bwlimit 10</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-rsync-download-options</code></dt>
<dd> <p> Options to use when using rsync to download a file from a remote. </p>
 </dd>
<dd> <p> These options are passed after other applicable rsync options, so can be used to override them. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-rsync-transport</code></dt>
<dd> <p> The remote shell to use to connect to the rsync remote. Possible values are <code>ssh</code> (the default) and <code>rsh</code>, together with their arguments, for instance <code>ssh -p 2222 -c blowfish</code>; Note that the remote hostname should not appear there, see <a href="/docs/linux/man/1-rsync/">rsync</a>(1) for details. When the transport used is <code>ssh</code>, connections are automatically cached unless <code>annex.sshcaching</code> is unset. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-bup-split-options</code></dt>
<dd> <p> Options to pass to bup split when storing content in this remote. For example, to limit the bandwidth to 100Kbyte/s, set it to <code>--bwlimit 100k</code> (There is no corresponding option for bup join.) </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-gnupg-options</code></dt>
<dd> <p> Options to pass to GnuPG for symmetric encryption. For instance, to use the AES cipher with a 256 bits key and disable compression, set it to <code>--cipher-algo AES256 --compress-algo none</code>. (These options take precedence over the default GnuPG configuration, which is otherwise used.) </p>
 </dd>
<dd>  </dd>
<dt><code>annex.ssh-options</code>, <code>annex.rsync-options</code>,</dt>
<dd> <p> <code>annex.rsync-upload-options</code>, <code>annex.rsync-download-options</code>, <code>annex.bup-split-options</code>, <code>annex.gnupg-options</code> </p>
 </dd>
<dd> <p> Default options to use if a remote does not have more specific options as described above. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.web-options</code></dt>
<dd> <p> Options to use when using wget or curl to download a file from the web. (wget is always used in preference to curl if available.) For example, to force ipv4 only, set it to &quot;-4&quot; </p>
 </dd>
<dd>  </dd>
<dt><code>annex.quvi-options</code></dt>
<dd> <p> Options to pass to quvi when using it to find the url to download for a video. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.http-headers</code></dt>
<dd> <p> HTTP headers to send when downloading from the web. Multiple lines of this option can be set, one per header. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.http-headers-command</code></dt>
<dd> <p> If set, the command is run and each line of its output is used as a HTTP header. This overrides annex.http-headers. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.web-download-command</code></dt>
<dd> <p> Use to specify a command to run to download a file from the web. (The default is to use wget or curl.) </p>
 </dd>
<dd> <p> In the command line, %url is replaced with the url to download, and %file is replaced with the file that it should be saved to. </p>
 </dd>
<dd>  </dd>
<dt><code>annex.secure-erase-command</code></dt>
<dd> <p> This can be set to a command that should be run whenever git-annex removes the content of a file from the repository. </p>
 </dd>
<dd> <p> In the command line, %file is replaced with the file that should be erased. </p>
 </dd>
<dd> <p> For example, to use the wipe command, set it to <code>wipe -f %file</code> </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.rsyncurl</code></dt>
<dd> <p> Used by rsync special remotes, this configures the location of the rsync repository to use. Normally this is automatically set up by <code>git annex initremote</code>, but you can change it if needed. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.buprepo</code></dt>
<dd> <p> Used by bup special remotes, this configures the location of the bup repository to use. Normally this is automatically set up by <code>git annex initremote</code>, but you can change it if needed. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.directory</code></dt>
<dd> <p> Used by directory special remotes, this configures the location of the directory where annexed files are stored for this remote. Normally this is automatically set up by <code>git annex initremote</code>, but you can change it if needed. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.s3</code></dt>
<dd> <p> Used to identify Amazon S3 special remotes. Normally this is automatically set up by <code>git annex initremote</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.glacier</code></dt>
<dd> <p> Used to identify Amazon Glacier special remotes. Normally this is automatically set up by <code>git annex initremote</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.webdav</code></dt>
<dd> <p> Used to identify webdav special remotes. Normally this is automatically set up by <code>git annex initremote</code>. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.tahoe</code></dt>
<dd> <p> Used to identify tahoe special remotes. Points to the configuration directory for tahoe. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.annex-xmppaddress</code></dt>
<dd> <p> Used to identify the XMPP address of a Jabber buddy. Normally this is set up by the git-annex assistant when pairing over XMPP. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.gcrypt</code></dt>
<dd> <p> Used to identify gcrypt special remotes. Normally this is automatically set up by <code>git annex initremote</code>. </p>
 </dd>
<dd> <p> It is set to &quot;true&quot; if this is a gcrypt remote. If the gcrypt remote is accessible over ssh and has git-annex-shell available to manage it, it&#8217;s set to &quot;shell&quot;. </p>
 </dd>
<dd>  </dd>
<dt><code>remote.&lt;name&gt;.hooktype</code>, <code>remote.&lt;name&gt;.externaltype</code></dt>
<dd> <p> Used by hook special remotes and external special remotes to record the type of the remote. </p>
 </dd>
<dd>  </dd></dl>
<h2>CONFIGURATION VIA .gitattributes</h2>
<p> The key-value backend used when adding a new file to the annex can be configured on a per-file-type basis via <code>.gitattributes</code> files. In the file, the <code>annex.backend</code> attribute can be set to the name of the backend to use. For example, this here&#8217;s how to use the WORM backend by default, but the SHA256E backend for ogg files: </p>
<p> <br />
&nbsp;<wbr>*&nbsp;<wbr>annex.backend=WORM <br />
&nbsp;<wbr>*.ogg annex.backend=SHA256E </p>
<p> The numcopies setting can also be configured on a per-file-type basis via the <code>annex.numcopies</code> attribute in <code>.gitattributes</code> files. This overrides other numcopies settings. For example, this makes two copies be needed for wav files and 3 copies for flac files: </p>
<p> <br />
&nbsp;<wbr>*.wav annex.numcopies=2 <br />
&nbsp;<wbr>*.flac annex.numcopies=3 </p>
<p> Note that setting numcopies to 0 is very unsafe. </p>
<p> These settings are honored by git-annex whenever it&#8217;s operating on a matching file. However, when using --all, --unused, or --key to specify keys to operate on, git-annex is operating on keys and not files, so will not honor the settings from .gitattributes. </p>
<p> Also note that when using views, only the toplevel .gitattributes file is preserved in the view, so other settings in other files won&#8217;t have any efffect. </p>
<h2>FILES</h2>
<p> These files are used by git-annex: </p>
<p> <code>.git/annex/objects/</code> in your git repository contains the annexed file contents that are currently available. Annexed files in your git repository symlink to that content. </p>
<p> <code>.git/annex/</code> in your git repository contains other run-time information used by git-annex. </p>
<p> <code>~/.config/git-annex/autostart</code> is a list of git repositories to start the git-annex assistant in. </p>
<h2>SEE ALSO</h2>
<p> Most of git-annex&#8217;s documentation is available on its web site, &lt;<a rel="nofollow" href="http://git-annex.branchable.com/">http://git-annex.branchable.com/</a>&gt; </p>
<p> If git-annex is installed from a package, a copy of its documentation should be included, in, for example, <code>/usr/share/doc/git-annex/</code>. </p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joey [at] kitenet.net&gt; </p>
<p> &lt;<a rel="nofollow" href="http://git-annex.branchable.com/">http://git-annex.branchable.com/</a>&gt; </p>
