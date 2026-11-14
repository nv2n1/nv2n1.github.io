---
title: "mtn(1)"
name: "mtn"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtn/"
description: "monotone – a distributed version control system"
---

<h2>NAME</h2>
<p> monotone &#8211; a distributed version control system</p>
<h2>SYNOPSIS</h2>
<p> <code>mtn</code> <i>[options&#8230;] command [arguments&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> monotone is a highly reliable, very customizable distributed version control system that provides lightweight branches, history-sensitive merging and a flexible trust setup. monotone has an easy-to-learn command set and comes with a rich interface for scripting purposes and thorough documentation. </p>
<p> For more information on monotone, visit <code><a rel="nofollow" href="http://www.monotone.ca">http://www.monotone.ca</a></code>. </p>
<p> The complete documentation, including a tutorial for a quick start with the system, can be found online on <code><a rel="nofollow" href="http://www.monotone.ca/docs">http://www.monotone.ca/docs</a></code>.</p>
<h2>GLOBAL OPTIONS</h2>
<dl>
<dt>&#8211;confdir &lt;arg&gt;</p>
<dd> set location of configuration directory</p>
<dt>&#8211;date-format &lt;arg&gt;</p>
<dd> <a href="/docs/linux/man/3-strftime/">strftime</a>(3) format specification for printing dates</p>
<dt>&#8211;db [ -d ] &lt;arg&gt;</p>
<dd> set name of database</p>
<dt>&#8211;dump &lt;arg&gt;</p>
<dd> file to dump debugging log to, on failure</p>
<dt>&#8211;help [ -h ]</p>
<dd> display help message</p>
<dt>&#8211;ignore-suspend-certs / &#8211;no-ignore-suspend-certs</p>
<dd> do not ignore revisions marked as suspended</p>
<dt>&#8211;key [ -k ] &lt;arg&gt; / &#8211;use-default-key</p>
<dd> sets the key for signatures, using either the key name or the key hash</p>
<dt>&#8211;keydir &lt;arg&gt;</p>
<dd> set location of key store</p>
<dt>&#8211;log &lt;arg&gt;</p>
<dd> file to write the log to</p>
<dt>&#8211;no-builtin-rcfile / &#8211;builtin-rcfile</p>
<dd> do not load the built-in lua file with the default hooks</p>
<dt>&#8211;no-default-confdir / &#8211;allow-default-confdir</p>
<dd> forbid use of the default confdir</p>
<dt>&#8211;no-format-dates</p>
<dd> print date certs exactly as stored in the database</p>
<dt>&#8211;no-standard-rcfiles / &#8211;standard-rcfiles</p>
<dd> do not load &#8216;~/.monotone/monotonerc&#8217; or &#8216;_MTN/monotonerc&#8217; lua files</p>
<dt>&#8211;no-workspace / &#8211;allow-workspace</p>
<dd> don&#8217;t look for a workspace</p>
<dt>&#8211;non-interactive / &#8211;interactive</p>
<dd> do not prompt the user for input</p>
<dt>&#8211;quiet [ -q ]</p>
<dd> decrease verbosity (undo previous &#8216;-v&#8217;, then disable informational output, then disable warnings)</p>
<dt>&#8211;rcfile &lt;arg&gt; / &#8211;clear-rcfiles</p>
<dd> load extra lua file</p>
<dt>&#8211;root &lt;arg&gt;</p>
<dd> limit search for workspace to specified root</p>
<dt>&#8211;ssh-sign &lt;arg&gt;</p>
<dd> controls use of ssh-agent. valid arguments are: &#8216;yes&#8217; to use ssh-agent to make signatures if possible, &#8216;no&#8217; to force use of monotone&#8217;s internal code, &#8216;only&#8217; to force use of ssh-agent, &#8216;check&#8217; to sign with both and compare</p>
<dt>&#8211;ticker &lt;arg&gt;</p>
<dd> set ticker style (count|dot|none)</p>
<dt>&#8211;timestamps</p>
<dd> show timestamps in front of errors, warnings and progress messages</p>
<dt>&#8211;verbose [ -v ]</p>
<dd> increase verbosity (undo previous &#8216;-q&#8217;, and then enable debug output)</p>
<dt>&#8211;version</p>
<dd> print version number, then exit</p>
<dt>&#8211;xargs [ -@ ] &lt;arg&gt;</p>
<dd> insert command line arguments taken from the given file </p>
</dl>
<h2>COMMANDS</h2>
<h3>command group &#8216;automation&#8217;</h3>
<p> Commands that aid in scripted execution.</p>
<dl>
<dt><code>automate ancestors </code> REV1 [REV2 [REV3 [&#8230;]]]</p>
<dd> Prints the ancestors of the given revisions.</p>
<dt><code>automate ancestry_difference </code> NEW_REV [OLD_REV1 [OLD_REV2 [&#8230;]]]</p>
<dd> Lists the ancestors of the first revision given, not in the others.</p>
<dt><code>automate branches </code></p>
<dd> Prints all branch certs in the revision graph.</p>
<dt><code>automate cert </code> REVISION-ID NAME VALUE</p>
<dd> Adds a revision certificate.</p>
<dt><code>automate certs </code> REV</p>
<dd> Prints all certificates attached to a revision.</p>
<dt><code>automate checkout </code> [DIRECTORY]</p>
<dd> Checks out a revision from the database into a directory. If a revision is given, that&#8217;s the one that will be checked out. Otherwise, it will be the head of the branch (given or implicit). If no directory is given, the branch name will be used as directory.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>automate children </code> REV</p>
<dd> Prints the children of a revision.</p>
<dt><code>automate common_ancestors </code> REV1 [REV2 [REV3 [&#8230;]]]</p>
<dd> Prints revisions that are common ancestors of a list of revisions.</p>
<dt><code>automate content_diff </code> [FILE [&#8230;]]</p>
<dd> Calculates diffs of files.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;reverse</p>
<dd> reverse order of diff</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</p>
<dt>&#8211;with-header / &#8211;without-header</p>
<dd> show the matching cset in the diff header</dl>
</dl>
<dt><code>automate descendents </code> REV1 [REV2 [REV3 [&#8230;]]]</p>
<dd> Prints the descendents of the given revisions.</p>
<dt><code>automate drop_attribute </code> PATH [KEY]</p>
<dd> Drops an attribute or all of them from a certain path.</p>
<dt><code>automate drop_db_variables </code> DOMAIN [NAME]</p>
<dd> Drops a database variable.</p>
<dt><code>automate drop_public_key </code> KEY_NAME_OR_HASH</p>
<dd> Drops a public key.</p>
<dt><code>automate erase_ancestors </code> [REV1 [REV2 [REV3 [&#8230;]]]]</p>
<dd> Erases the ancestors in a list of revisions.</p>
<dt><code>automate erase_descendants </code> [REV1 [REV2 [REV3 [&#8230;]]]]</p>
<dd> Erases the descendants in a list of revisions.</p>
<dt><code>automate file_merge </code> LEFT_REVID LEFT_FILENAME RIGHT_REVID RIGHT_FILENAME</p>
<dd> Prints the results of the internal line merger, given two child revisions and file names.</p>
<dt><code>automate generate_key </code> KEY_NAME PASSPHRASE</p>
<dd> Generates an RSA key-pair.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;force-duplicate-key</p>
<dd> force genkey to not error out when the named key already exists</dl>
</dl>
<dt><code>automate get_attributes </code> PATH</p>
<dd> Prints all attributes for the specified path. If an explicit revision is given, the file&#8217;s attributes at this specific revision are returned.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>automate get_base_revision_id </code></p>
<dd> Shows the revision on which the workspace is based.</p>
<dt><code>automate get_content_changed </code> REV FILE</p>
<dd> Lists the revisions that changed the content relative to another revision.</p>
<dt><code>automate get_corresponding_path </code> REV1 FILE REV2</p>
<dd> Prints the name of a file in a target revision relative to a given revision.</p>
<dt><code>automate get_current_revision </code> [PATHS &#8230;]</p>
<dd> Shows change information for a workspace.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</dl>
</dl>
<dt><code>automate get_current_revision_id </code></p>
<dd> Shows the revision of the current workspace.</p>
<dt><code>automate get_db_variables </code> [DOMAIN]</p>
<dd> Retrieve database variables.</p>
<dt><code>automate get_extended_manifest_of </code> REVISION</p>
<dd> Prints the extended manifest for the given identifier.</p>
<dt><code>automate get_file </code> FILEID</p>
<dd> Prints the contents of a file (given an identifier).</p>
<dt><code>automate get_file_of </code> FILENAME</p>
<dd> Prints the contents of a file (given a name).</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>automate get_file_size </code> FILEID</p>
<dd> Prints the size of a file (given an identifier).</p>
<dt><code>automate get_manifest_of </code> [REVID]</p>
<dd> Shows the manifest associated with a revision.</p>
<dt><code>automate get_option </code> OPTION</p>
<dd> Shows the value of an option.</p>
<dt><code>automate get_public_key </code> KEY_NAME_OR_HASH</p>
<dd> Prints a public key packet.</p>
<dt><code>automate get_revision </code> REVID</p>
<dd> Shows change information for a revision.</p>
<dt><code>automate get_workspace_root </code></p>
<dd> Prints the workspace root for the current directory.</p>
<dt><code>automate graph </code></p>
<dd> Prints the complete ancestry graph.</p>
<dt><code>automate heads </code> [BRANCH]</p>
<dd> Prints the heads of the given branch.</p>
<dt><code>automate identify </code> PATH</p>
<dd> Prints the file identifier of a file.</p>
<dt><code>automate interface_version </code></p>
<dd> Prints the automation interface&#8217;s version.</p>
<dt><code>automate inventory </code> [PATH]&#8230;</p>
<dd> Prints a summary of files found in the workspace.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;no-corresponding-renames / &#8211;corresponding-renames</p>
<dd> don&#8217;t output corresponding renames if restricted on such nodes</p>
<dt>&#8211;no-ignored / &#8211;ignored</p>
<dd> don&#8217;t output ignored files</p>
<dt>&#8211;no-unchanged / &#8211;unchanged</p>
<dd> don&#8217;t output unchanged files</p>
<dt>&#8211;no-unknown / &#8211;unknown</p>
<dd> don&#8217;t output unknown files</dl>
</dl>
<dt><code>automate keys </code></p>
<dd> Lists all keys in the keystore.</p>
<dt><code>automate leaves </code></p>
<dd> Lists the leaves of the revision graph.</p>
<dt><code>automate log </code> [PATH] &#8230;</p>
<dd> Lists the selected revision history.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;from &lt;arg&gt; / &#8211;clear-from</p>
<dd> revision(s) to start logging at</p>
<dt>&#8211;last &lt;arg&gt;</p>
<dd> limit log output to the last number of entries</p>
<dt>&#8211;next &lt;arg&gt;</p>
<dd> limit log output to the next number of entries</p>
<dt>&#8211;no-merges / &#8211;merges</p>
<dd> exclude merges when printing logs</p>
<dt>&#8211;to &lt;arg&gt; / &#8211;clear-to</p>
<dd> revision(s) to stop logging at</dl>
</dl>
<dt><code>automate lua </code> LUA_FUNCTION [ARG1 [ARG2 [&#8230;]]]</p>
<dd> Executes the given lua function and returns the result.</p>
<dt><code>automate packet_for_fdata </code> FILEID</p>
<dd> Prints the file data in packet format.</p>
<dt><code>automate packet_for_fdelta </code> OLD_FILE NEW_FILE</p>
<dd> Prints the file delta in packet format.</p>
<dt><code>automate packet_for_rdata </code> REVID</p>
<dd> Prints the revision data in packet format.</p>
<dt><code>automate packets_for_certs </code> REVID</p>
<dd> Prints the certs associated with a revision in packet format.</p>
<dt><code>automate parents </code> REV</p>
<dd> Prints the parents of a revision.</p>
<dt><code>automate pull </code> [URI]</p>
<dd>
<dt><code>automate pull </code> [ADDRESS[:PORTNUMBER] [PATTERN &#8230;]]</p>
<dd> Pulls branches from a netsync server.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;dry-run / &#8211;no-dry-run</p>
<dd> don&#8217;t perform the operation, just show what would have happened</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;set-default / &#8211;no-set-default</p>
<dd> use the current netsync arguments and options as the future default</dl>
</dl>
<dt><code>automate push </code> [URI]</p>
<dd>
<dt><code>automate push </code> [ADDRESS[:PORTNUMBER] [PATTERN &#8230;]]</p>
<dd> Pushes branches to a netsync server.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;dry-run / &#8211;no-dry-run</p>
<dd> don&#8217;t perform the operation, just show what would have happened</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;key-to-push &lt;arg&gt;</p>
<dd> push the specified key even if it hasn&#8217;t signed anything</p>
<dt>&#8211;set-default / &#8211;no-set-default</p>
<dd> use the current netsync arguments and options as the future default</dl>
</dl>
<dt><code>automate put_file </code> [FILEID] CONTENTS</p>
<dd> Stores a file in the database.</p>
<dt><code>automate put_public_key </code> KEY-PACKET-DATA</p>
<dd> Store the public key in the database.</p>
<dt><code>automate put_revision </code> REVISION-DATA</p>
<dd> Stores a revision into the database.</p>
<dt><code>automate read_packets </code> PACKET-DATA</p>
<dd> Load the given packets into the database.</p>
<dt><code>automate remote </code> COMMAND [ARGS]</p>
<dd> Executes COMMAND on a remote server.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;remote-stdio-host &lt;arg&gt;</p>
<dd> sets the host (and optionally the port) for a remote netsync action</p>
<dt>&#8211;set-default / &#8211;no-set-default</p>
<dd> use the current netsync arguments and options as the future default</dl>
</dl>
<dt><code>automate remote_stdio </code> [URI]</p>
<dd>
<dt><code>automate remote_stdio </code> [ADDRESS[:PORTNUMBER]]</p>
<dd> Opens an &#8216;automate stdio&#8217; connection to a remote server.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;set-default / &#8211;no-set-default</p>
<dd> use the current netsync arguments and options as the future default</dl>
</dl>
<dt><code>automate roots </code></p>
<dd> Lists the roots of the revision graph.</p>
<dt><code>automate select </code> SELECTOR</p>
<dd> Lists the revisions that match a selector.</p>
<dt><code>automate set_attribute </code> PATH KEY VALUE</p>
<dd> Sets an attribute on a certain path.</p>
<dt><code>automate set_db_variable </code> DOMAIN NAME VALUE</p>
<dd> Sets a database variable.</p>
<dt><code>automate show_conflicts </code> [LEFT_REVID RIGHT_REVID]</p>
<dd> Shows the conflicts between two revisions. If no arguments are given, LEFT_REVID and RIGHT_REVID default to the first two heads that would be chosen by the &#8216;merge&#8217; command.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;ignore-suspend-certs / &#8211;no-ignore-suspend-certs</p>
<dd> do not ignore revisions marked as suspended</dl>
</dl>
<dt><code>automate stdio </code></p>
<dd> Automates several commands in one run.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;automate-stdio-size &lt;arg&gt;</p>
<dd> block size in bytes for &#8216;automate stdio&#8217; output</dl>
</dl>
<dt><code>automate sync </code> [URI]</p>
<dd>
<dt><code>automate sync </code> [ADDRESS[:PORTNUMBER] [PATTERN &#8230;]]</p>
<dd> Synchronizes branches with a netsync server.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;dry-run / &#8211;no-dry-run</p>
<dd> don&#8217;t perform the operation, just show what would have happened</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;key-to-push &lt;arg&gt;</p>
<dd> push the specified key even if it hasn&#8217;t signed anything</p>
<dt>&#8211;set-default / &#8211;no-set-default</p>
<dd> use the current netsync arguments and options as the future default</dl>
</dl>
<dt><code>automate tags </code> [BRANCH_PATTERN]</p>
<dd> Prints all tags attached to a set of branches.</p>
<dt><code>automate toposort </code> [REV1 [REV2 [REV3 [&#8230;]]]]</p>
<dd> Topologically sorts a list of revisions.</p>
<dt><code>automate update </code></p>
<dd> Updates the workspace.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
</dl>
<h3>command group &#8216;database&#8217;</h3>
<p> Commands that manipulate the database.</p>
<dl>
<dt><code>db changesetify </code></p>
<dd> Converts the database to the changeset format.</p>
<dt><code>db check </code></p>
<dd> Does some sanity checks on the database. Ensures that the database is consistent by issuing multiple checks.</p>
<dt><code>db dump </code></p>
<dd> Dumps the contents of the database. Generates a list of SQL instructions that represent the whole contents of the database. The resulting output is useful to later restore the database from a text file that serves as a backup.</p>
<dt><code>db execute </code></p>
<dd> Executes an SQL command on the database. Directly executes the given SQL command on the database</p>
<dt><code>db fix_certs </code></p>
<dd> Attempt to fix bad certs. Older monotone versions could sometimes associate certs with the wrong key. This fixes such certs if you have the correct key, and can optionally drop any certs that you don&#8217;t have the correct key for. This should only be needed if you had such certs in your db when upgrading from 0.44 or earlier, or if you loaded such certs with &#8216;mtn read&#8217;.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;drop-bad-certs</p>
<dd> drop certs signed by keys we don&#8217;t know about</dl>
</dl>
<dt><code>db info </code></p>
<dd> Shows information about the database.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;full / &#8211;concise</p>
<dd> print detailed information</dl>
</dl>
<dt><code>db init </code></p>
<dd> Initializes a database. Creates a new database file and initializes it.</p>
<dt><code>db load </code></p>
<dd> Loads the contents of the database. Reads a list of SQL instructions that regenerate the contents of the database. This is supposed to be used in conjunction with the output generated by the &#8216;dump&#8217; command.</p>
<dt><code>db migrate </code></p>
<dd> Migrates the database to a newer schema. Updates the database&#8217;s internal schema to the most recent one. Needed to automatically resolve incompatibilities that may be introduced in newer versions of monotone.</p>
<dt><code>db regenerate_caches </code></p>
<dd> Regenerates the caches stored in the database.</p>
<dt><code>db rosterify </code></p>
<dd> Converts the database to the rosters format.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;drop-attr &lt;arg&gt;</p>
<dd> when rosterifying, drop attrs entries with the given key</dl>
</dl>
<dt><code>db set_epoch </code> BRANCH EPOCH</p>
<dd> Sets the branch&#8217;s epoch.</p>
<dt><code>db version </code></p>
<dd> Shows the database&#8217;s version.</p>
<dt><code>local kill_certs </code> SELECTOR CERTNAME [CERTVAL]</p>
<dd> Deletes the specified certs from the local database. Deletes all certs which are on the given revision(s) and have the given name and if a value is specified then also the given value.</p>
<dt><code>local kill_revision </code> REVID</p>
<dd> Kills a revision from the local database.</dl>
<h3>command group &#8216;debug&#8217;</h3>
<p> Commands that aid in program debugging.</p>
<dl>
<dt><code>asciik </code> SELECTOR</p>
<dd> Prints an ASCII representation of the revisions&#8217; graph.</p>
<dt><code>fdiff </code> SRCNAME DESTNAME SRCID DESTID</p>
<dd> Differences 2 files and outputs the result.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;context</p>
<dd> use context diff format</p>
<dt>&#8211;diff-args &lt;arg&gt;</p>
<dd> argument to pass external diff hook</p>
<dt>&#8211;external</p>
<dd> use external diff hook for generating diffs</p>
<dt>&#8211;no-show-encloser / &#8211;show-encloser</p>
<dd> do not show the function containing each block of changes</p>
<dt>&#8211;reverse</p>
<dd> reverse order of diff</p>
<dt>&#8211;unified</p>
<dd> use unified diff format</p>
<dt>&#8211;with-header / &#8211;without-header</p>
<dd> show the matching cset in the diff header</dl>
</dl>
<dt><code>fload </code></p>
<dd> Loads a file&#8217;s contents into the database.</p>
<dt><code>fmerge </code> PARENT_FILEID LEFT_FILEID RIGHT_FILEID</p>
<dd> Merges 3 files and outputs the result.</p>
<dt><code>get_roster </code> [REVID]</p>
<dd> Dumps the roster associated with a given identifier. If no REVID is given, the workspace is used.</p>
<dt><code>identify </code> [PATH]</p>
<dd> Calculates the identity of a file or stdin. If any PATH is given, calculates their identity; otherwise, the one from the standard input is calculated.</p>
<dt><code>rcs_import </code> RCSFILE&#8230;</p>
<dd> Parses versions in RCS files. This command doesn&#8217;t reconstruct or import revisions. You probably want to use cvs_import.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</dl>
</dl>
</dl>
<h3>command group &#8216;informative&#8217;</h3>
<p> Commands for information retrieval.</p>
<dl>
<dt><code>annotate </code> PATH</p>
<dd> Prints an annotated copy of a file. Calculates and prints an annotated copy of the given file from the specified REVISION.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</p>
<dt>&#8211;revs-only</p>
<dd> annotate using full revision ids only</dl>
</dl>
<dt><code>bisect bad </code></p>
<dd> Marks the current revision or specified revisions as bad. Known bad revisions are removed from the set being searched.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>bisect good </code></p>
<dd> Marks the current revision or specified revisions as good. Known good revisions are removed from the set being searched.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>bisect reset </code></p>
<dd> Reset the current bisection search. Update the workspace back to the revision from which the bisection was started and remove all current search information, allowing a new search to be started.</p>
<dt><code>bisect skip </code></p>
<dd> Excludes the current revision or specified revisions from the search. Skipped revisions are removed from the set being searched. Revisions that cannot be tested for some reason should be skipped.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>bisect status </code></p>
<dd> Reports on the current status of the bisection search. Lists the total number of revisions in the search set, the number of revisions that have been determined to be good or bad, the number of revisions that have been skipped and the number of revisions remaining to be tested.</p>
<dt><code>bisect update </code></p>
<dd> Updates the workspace to the next revision to be tested by bisection. This command can be used if updates by good, bad or skip commands fail due to blocked paths or other problems.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</dl>
</dl>
<dt><code>cat </code> FILENAME</p>
<dd> Prints a file from the database. Fetches the given file FILENAME from the database and prints it to the standard output.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>complete </code> (revision|file|key) PARTIAL-ID</p>
<dd> Completes a partial identifier.</p>
<dt><code>di </code> [PATH]&#8230;</p>
<dd>
<dt><code>diff </code> [PATH]&#8230;</p>
<dd> Shows current differences. Compares the current tree with the files in the repository and prints the differences on the standard output. If one revision is given, the diff between the workspace and that revision is shown. If two revisions are given, the diff between them is given. If no format is specified, unified is used by default.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;context</p>
<dd> use context diff format</p>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;diff-args &lt;arg&gt;</p>
<dd> argument to pass external diff hook</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;external</p>
<dd> use external diff hook for generating diffs</p>
<dt>&#8211;no-show-encloser / &#8211;show-encloser</p>
<dd> do not show the function containing each block of changes</p>
<dt>&#8211;reverse</p>
<dd> reverse order of diff</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</p>
<dt>&#8211;unified</p>
<dd> use unified diff format</p>
<dt>&#8211;with-header / &#8211;without-header</p>
<dd> show the matching cset in the diff header</dl>
</dl>
<dt><code>help </code> command [ARGS&#8230;]</p>
<dd> Displays help about commands and options.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;hidden / &#8211;no-hidden</p>
<dd> show hidden commands and options</dl>
</dl>
<dt><code>list branches </code> [PATTERN]</p>
<dd> Lists branches in the database that match a pattern.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</dl>
</dl>
<dt><code>list certs </code> REVID</p>
<dd> Lists certificates attached to a revision.</p>
<dt><code>list changed </code> [PATH&#8230;]</p>
<dd> Lists files that have changed with respect to the current revision.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</dl>
</dl>
<dt><code>list databases </code></p>
<dd>
<dt><code>list dbs </code></p>
<dd> Lists managed databases and their known workspaces.</p>
<dt><code>list duplicates </code></p>
<dd> Lists duplicate files in the specified revision. If no revision is specified, use the workspace.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>list epochs </code> [BRANCH [&#8230;]]</p>
<dd> Lists the current epoch of branches that match a pattern.</p>
<dt><code>list ignored </code> [PATH]</p>
<dd> Lists workspace files that are ignored in the current branch.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;recursive [ -R ] / &#8211;no-recursive</p>
<dd> also operate on the contents of any listed directories</dl>
</dl>
<dt><code>list keys </code> [PATTERN]</p>
<dd> Lists keys that match a pattern.</p>
<dt><code>list known </code></p>
<dd> Lists workspace files that belong to the current branch.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</dl>
</dl>
<dt><code>list missing </code></p>
<dd> Lists files that belong to the branch but are not in the workspace.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</dl>
</dl>
<dt><code>list tags </code> [PATTERN]</p>
<dd> Lists all tags in the database.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</dl>
</dl>
<dt><code>list unknown </code> [PATH]</p>
<dd> Lists workspace files that are unknown in the current branch.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;recursive [ -R ] / &#8211;no-recursive</p>
<dd> also operate on the contents of any listed directories</dl>
</dl>
<dt><code>list vars </code> [DOMAIN]</p>
<dd> Lists variables in the whole database or a domain.</p>
<dt><code>list workspaces </code></p>
<dd> Lists known workspaces of a specified database.</p>
<dt><code>log </code> [PATH] &#8230;</p>
<dd> Prints selected history in forward or reverse order. This command prints selected history in forward or reverse order, filtering it by PATH if given.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;brief / &#8211;no-brief</p>
<dd> print a brief version of the normal output</p>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;diffs / &#8211;no-diffs</p>
<dd> print diffs along with logs</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;from &lt;arg&gt; / &#8211;clear-from</p>
<dd> revision(s) to start logging at</p>
<dt>&#8211;last &lt;arg&gt;</p>
<dd> limit log output to the last number of entries</p>
<dt>&#8211;next &lt;arg&gt;</p>
<dd> limit log output to the next number of entries</p>
<dt>&#8211;no-files / &#8211;files</p>
<dd> exclude files when printing logs</p>
<dt>&#8211;no-graph / &#8211;graph</p>
<dd> do not use ASCII graph to display ancestry</p>
<dt>&#8211;no-merges / &#8211;merges</p>
<dd> exclude merges when printing logs</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</p>
<dt>&#8211;to &lt;arg&gt; / &#8211;clear-to</p>
<dd> revision(s) to stop logging at</dl>
</dl>
<dt><code>manpage </code></p>
<dd> Generate a manual page from monotone&#8217;s command help.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;formatted / &#8211;plain</p>
<dd> automatically run the output through nroff (default if the output is a terminal)</p>
<dt>&#8211;hidden / &#8211;no-hidden</p>
<dd> show hidden commands and options</dl>
</dl>
<dt><code>show_conflicts </code> REV REV</p>
<dd> Shows what conflicts need resolution between two revisions. The conflicts are calculated based on the two revisions given in the REV parameters.</p>
<dt><code>status </code> [PATH]&#8230;</p>
<dd> Shows workspace&#8217;s status information.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</dl>
</dl>
<dt><code>version </code></p>
<dd> Shows the program version.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;full / &#8211;concise</p>
<dd> print detailed information</dl>
</dl>
</dl>
<h3>command group &#8216;key_and_cert&#8217;</h3>
<p> Commands to manage keys and certificates.</p>
<dl>
<dt><code>cert </code> SELECTOR CERTNAME [CERTVAL]</p>
<dd> Creates a certificate for a revision or set of revisions. Creates a certificate with the given name and value on each revision that matches the given selector</p>
<dt><code>dropkey </code> KEY_NAME_OR_HASH</p>
<dd> Drops a public and/or private key.</p>
<dt><code>genkey </code> KEY_NAME</p>
<dd> Generates an RSA key-pair.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;force-duplicate-key</p>
<dd> force genkey to not error out when the named key already exists</dl>
</dl>
<dt><code>passphrase </code> KEY_NAME_OR_HASH</p>
<dd> Changes the passphrase of a private RSA key.</p>
<dt><code>ssh_agent_add </code></p>
<dd> Adds a private key to ssh-agent.</p>
<dt><code>ssh_agent_export </code> [FILENAME]</p>
<dd> Exports a private key for use with ssh-agent.</p>
<dt><code>trusted </code> REVISION NAME VALUE SIGNER1 [SIGNER2 [&#8230;]]</p>
<dd> Tests whether a hypothetical certificate would be trusted. The current settings are used to run the test.</dl>
<h3>command group &#8216;network&#8217;</h3>
<p> Commands that access the network.</p>
<dl>
<dt><code>clone </code> URI [DIRECTORY]</p>
<dd>
<dt><code>clone </code> HOST[:PORTNUMBER] BRANCH [DIRECTORY]</p>
<dd> Checks out a revision from a remote database into a directory. If a revision is given, that&#8217;s the one that will be checked out. Otherwise, it will be the head of the branch supplied. If no directory is given, the branch name will be used as directory</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>pull </code> [URI]</p>
<dd>
<dt><code>pull </code> [ADDRESS[:PORTNUMBER] [PATTERN &#8230;]]</p>
<dd> Pulls branches from a netsync server. This pulls all branches that match the pattern given in PATTERN from the netsync server at the address ADDRESS.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;dry-run / &#8211;no-dry-run</p>
<dd> don&#8217;t perform the operation, just show what would have happened</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;set-default / &#8211;no-set-default</p>
<dd> use the current netsync arguments and options as the future default</p>
<dt>&#8211;update / &#8211;no-update</p>
<dd> automatically update the workspace, if it was at a head and the command creates a new head</dl>
</dl>
<dt><code>push </code> [URI]</p>
<dd>
<dt><code>push </code> [ADDRESS[:PORTNUMBER] [PATTERN &#8230;]]</p>
<dd> Pushes branches to a netsync server. This will push all branches that match the pattern given in PATTERN to the netsync server at the address ADDRESS.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;dry-run / &#8211;no-dry-run</p>
<dd> don&#8217;t perform the operation, just show what would have happened</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;key-to-push &lt;arg&gt;</p>
<dd> push the specified key even if it hasn&#8217;t signed anything</p>
<dt>&#8211;set-default / &#8211;no-set-default</p>
<dd> use the current netsync arguments and options as the future default</dl>
</dl>
<dt><code>serve </code></p>
<dd> Serves the database to connecting clients.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;bind &lt;arg&gt;</p>
<dd> address:port to listen on (default :4691)</p>
<dt>&#8211;pid-file &lt;arg&gt; / &#8211;no-pid-file</p>
<dd> record process id of server</dl>
</dl>
<dt><code>sync </code> [URI]</p>
<dd>
<dt><code>sync </code> [ADDRESS[:PORTNUMBER] [PATTERN &#8230;]]</p>
<dd> Synchronizes branches with a netsync server. This synchronizes branches that match the pattern given in PATTERN with the netsync server at the address ADDRESS.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;dry-run / &#8211;no-dry-run</p>
<dd> don&#8217;t perform the operation, just show what would have happened</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;key-to-push &lt;arg&gt;</p>
<dd> push the specified key even if it hasn&#8217;t signed anything</p>
<dt>&#8211;set-default / &#8211;no-set-default</p>
<dd> use the current netsync arguments and options as the future default</p>
<dt>&#8211;update / &#8211;no-update</p>
<dd> automatically update the workspace, if it was at a head and the command creates a new head</dl>
</dl>
</dl>
<h3>command group &#8216;packet_io&#8217;</h3>
<p> Commands for packet reading and writing.</p>
<dl>
<dt><code>privkey </code> KEY_NAME_OR_HASH</p>
<dd> Prints a private key packet.</p>
<dt><code>pubkey </code> KEY_NAME_OR_HASH</p>
<dd> Prints a public key packet.</p>
<dt><code>read </code> [FILE1 [FILE2 [&#8230;]]]</p>
<dd> Reads packets from files. If no files are provided, the standard input is used.</dl>
<h3>command group &#8216;review&#8217;</h3>
<p> Commands to review revisions.</p>
<dl>
<dt><code>approve </code> REVISION</p>
<dd> Approves a particular revision.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;update / &#8211;no-update</p>
<dd> automatically update the workspace, if it was at a head and the command creates a new head</dl>
</dl>
<dt><code>comment </code> REVISION [COMMENT]</p>
<dd> Comments on a particular revision.</p>
<dt><code>disapprove </code> [PARENT-REVISION] CHILD-REVISION</p>
<dd> Disapproves a particular revision or revision range.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;author &lt;arg&gt;</p>
<dd> override author for commit</p>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;date &lt;arg&gt;</p>
<dd> override date/time for commit</p>
<dt>&#8211;message [ -m ] &lt;arg&gt;</p>
<dd> set commit changelog message</p>
<dt>&#8211;message-file &lt;arg&gt;</p>
<dd> set filename containing commit changelog message</p>
<dt>&#8211;update / &#8211;no-update</p>
<dd> automatically update the workspace, if it was at a head and the command creates a new head</dl>
</dl>
<dt><code>suspend </code> REVISION</p>
<dd> Suspends a particular revision.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;update / &#8211;no-update</p>
<dd> automatically update the workspace, if it was at a head and the command creates a new head</dl>
</dl>
<dt><code>tag </code> REVISION TAGNAME</p>
<dd> Puts a symbolic tag certificate on a revision.</p>
<dt><code>testresult </code> REV (pass|fail|true|false|yes|no|1|0)</p>
<dd> Notes the results of running a test on a revision.</dl>
<h3>command group &#8216;tree&#8217;</h3>
<p> Commands to manipulate the tree.</p>
<dl>
<dt><code>checkout </code> [DIRECTORY]</p>
<dd>
<dt><code>co </code> [DIRECTORY]</p>
<dd> Checks out a revision from the database into a directory. If a revision is given, that&#8217;s the one that will be checked out. Otherwise, it will be the head of the branch (given or implicit). If no directory is given, the branch name will be used as directory.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>conflicts clean </code></p>
<dd> Delete any bookkeeping files related to conflict resolution.</p>
<dt><code>conflicts resolve_first </code> RESOLUTION</p>
<dd> Set the resolution for the first unresolved single-file conflict.. Use &#8216;mtn conflicts show_first&#8217; to see possible resolutions.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;conflicts-file &lt;arg&gt;</p>
<dd> file in which to store conflicts</dl>
</dl>
<dt><code>conflicts resolve_first_left </code> RESOLUTION</p>
<dd> Set the left resolution for the first unresolved two-file conflict.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;conflicts-file &lt;arg&gt;</p>
<dd> file in which to store conflicts</dl>
</dl>
<dt><code>conflicts resolve_first_right </code> RESOLUTION</p>
<dd> Set the right resolution for the first unresolved two-file conflict.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;conflicts-file &lt;arg&gt;</p>
<dd> file in which to store conflicts</dl>
</dl>
<dt><code>conflicts show_first </code></p>
<dd> Show the first unresolved conflict in the conflicts file, and possible resolutions.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;conflicts-file &lt;arg&gt;</p>
<dd> file in which to store conflicts</dl>
</dl>
<dt><code>conflicts show_remaining </code></p>
<dd> Show the remaining unresolved conflicts in the conflicts file.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;conflicts-file &lt;arg&gt;</p>
<dd> file in which to store conflicts</dl>
</dl>
<dt><code>conflicts store </code> [LEFT_REVID RIGHT_REVID]</p>
<dd> Store the conflicts from merging two revisions. If no arguments are given, LEFT_REVID and RIGHT_REVID default to the first two heads that would be chosen by the &#8216;merge&#8217; command. If &#8216;&#8211;conflicts-file&#8217; is not given, &#8216;_MTN/conflicts&#8217; is used.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;conflicts-file &lt;arg&gt;</p>
<dd> file in which to store conflicts</dl>
</dl>
<dt><code>explicit_merge </code> LEFT-REVISION RIGHT-REVISION DEST-BRANCH</p>
<dd> Merges two explicitly given revisions. The results of the merge are placed on the branch specified by DEST-BRANCH.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;author &lt;arg&gt;</p>
<dd> override author for commit</p>
<dt>&#8211;date &lt;arg&gt;</p>
<dd> override date/time for commit</p>
<dt>&#8211;message [ -m ] &lt;arg&gt;</p>
<dd> set commit changelog message</p>
<dt>&#8211;message-file &lt;arg&gt;</p>
<dd> set filename containing commit changelog message</p>
<dt>&#8211;resolve-conflicts / &#8211;no-resolve-conflicts</p>
<dd> specify conflict resolutions in a file, instead of interactively</p>
<dt>&#8211;resolve-conflicts-file &lt;arg&gt;</p>
<dd> use file to resolve conflicts</p>
<dt>&#8211;update / &#8211;no-update</p>
<dd> automatically update the workspace, if it was at a head and the command creates a new head</dl>
</dl>
<dt><code>heads </code></p>
<dd> Shows unmerged head revisions of a branch.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</dl>
</dl>
<dt><code>import </code> DIRECTORY</p>
<dd> Imports the contents of a directory into a branch.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;author &lt;arg&gt;</p>
<dd> override author for commit</p>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;date &lt;arg&gt;</p>
<dd> override date/time for commit</p>
<dt>&#8211;dry-run / &#8211;no-dry-run</p>
<dd> don&#8217;t perform the operation, just show what would have happened</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;message [ -m ] &lt;arg&gt;</p>
<dd> set commit changelog message</p>
<dt>&#8211;message-file &lt;arg&gt;</p>
<dd> set filename containing commit changelog message</p>
<dt>&#8211;no-respect-ignore / &#8211;respect-ignore</p>
<dd> do not ignore any files</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>merge </code></p>
<dd> Merges unmerged heads of a branch.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;author &lt;arg&gt;</p>
<dd> override author for commit</p>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;date &lt;arg&gt;</p>
<dd> override date/time for commit</p>
<dt>&#8211;message [ -m ] &lt;arg&gt;</p>
<dd> set commit changelog message</p>
<dt>&#8211;message-file &lt;arg&gt;</p>
<dd> set filename containing commit changelog message</p>
<dt>&#8211;resolve-conflicts / &#8211;no-resolve-conflicts</p>
<dd> specify conflict resolutions in a file, instead of interactively</p>
<dt>&#8211;resolve-conflicts-file &lt;arg&gt;</p>
<dd> use file to resolve conflicts</p>
<dt>&#8211;update / &#8211;no-update</p>
<dd> automatically update the workspace, if it was at a head and the command creates a new head</dl>
</dl>
<dt><code>merge_into_dir </code> SOURCE-BRANCH DEST-BRANCH DIR</p>
<dd> Merges one branch into a subdirectory in another branch.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;author &lt;arg&gt;</p>
<dd> override author for commit</p>
<dt>&#8211;date &lt;arg&gt;</p>
<dd> override date/time for commit</p>
<dt>&#8211;message [ -m ] &lt;arg&gt;</p>
<dd> set commit changelog message</p>
<dt>&#8211;message-file &lt;arg&gt;</p>
<dd> set filename containing commit changelog message</p>
<dt>&#8211;resolve-conflicts / &#8211;no-resolve-conflicts</p>
<dd> specify conflict resolutions in a file, instead of interactively</p>
<dt>&#8211;resolve-conflicts-file &lt;arg&gt;</p>
<dd> use file to resolve conflicts</p>
<dt>&#8211;update / &#8211;no-update</p>
<dd> automatically update the workspace, if it was at a head and the command creates a new head</dl>
</dl>
<dt><code>merge_into_workspace </code> OTHER-REVISION</p>
<dd> Merges a revision into the current workspace&#8217;s base revision. Merges OTHER-REVISION into the current workspace&#8217;s base revision, and update the current workspace with the result. There can be no pending changes in the current workspace. Both OTHER-REVISION and the workspace&#8217;s base revision will be recorded as parents on commit. The workspace&#8217;s selected branch is not changed.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</dl>
</dl>
<dt><code>migrate_workspace </code> [DIRECTORY]</p>
<dd> Migrates a workspace directory&#8217;s metadata to the latest format. If no directory is given, defaults to the current workspace.</p>
<dt><code>propagate </code> SOURCE-BRANCH DEST-BRANCH</p>
<dd> Merges from one branch to another asymmetrically.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;author &lt;arg&gt;</p>
<dd> override author for commit</p>
<dt>&#8211;date &lt;arg&gt;</p>
<dd> override date/time for commit</p>
<dt>&#8211;message [ -m ] &lt;arg&gt;</p>
<dd> set commit changelog message</p>
<dt>&#8211;message-file &lt;arg&gt;</p>
<dd> set filename containing commit changelog message</p>
<dt>&#8211;resolve-conflicts / &#8211;no-resolve-conflicts</p>
<dd> specify conflict resolutions in a file, instead of interactively</p>
<dt>&#8211;resolve-conflicts-file &lt;arg&gt;</p>
<dd> use file to resolve conflicts</dl>
</dl>
<dt><code>refresh_inodeprints </code></p>
<dd> Refreshes the inodeprint cache.</p>
<dt><code>setup </code> [DIRECTORY]</p>
<dd> Sets up a new workspace directory. If no directory is specified, uses the current directory.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</dl>
</dl>
</dl>
<h3>command group &#8216;variables&#8217;</h3>
<p> Commands to manage persistent variables.</p>
<dl>
<dt><code>cleanup_workspace_list </code></p>
<dd> Removes all invalid, registered workspace paths for the current database.</p>
<dt><code>register_workspace </code> [WORKSPACE_PATH]</p>
<dd> Registers a new workspace for the current database. This command adds WORKSPACE_PATH to the list of `known-workspaces&#8217;.</p>
<dt><code>set </code> DOMAIN NAME VALUE</p>
<dd> Sets a database variable. This command modifies (or adds if it did not exist before) the variable named NAME, stored in the database, and sets it to the given value in VALUE. The variable is placed in the domain DOMAIN.</p>
<dt><code>unregister_workspace </code> [WORKSPACE_PATH]</p>
<dd> Unregisters an existing workspace for the current database. This command removes WORKSPACE_PATH to the list of `known-workspaces&#8217;.</p>
<dt><code>unset </code> DOMAIN NAME</p>
<dd> Unsets a database variable. This command removes the variable NAME from domain DOMAIN, which was previously stored in the database.</dl>
<h3>command group &#8216;vcs&#8217;</h3>
<p> Commands for interaction with other version control systems.</p>
<dl>
<dt><code>cvs_import </code> CVSROOT</p>
<dd> Imports all versions in a CVS repository.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</dl>
</dl>
<dt><code>git_export </code></p>
<dd> Produces a git fast-export data stream on stdout.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;authors-file &lt;arg&gt;</p>
<dd> file mapping author names from original to new values</p>
<dt>&#8211;branches-file &lt;arg&gt;</p>
<dd> file mapping branch names from original to new values</p>
<dt>&#8211;export-marks &lt;arg&gt;</p>
<dd> save the internal marks table after exporting revisions</p>
<dt>&#8211;import-marks &lt;arg&gt;</p>
<dd> load the internal marks table before exporting revisions</p>
<dt>&#8211;log-certs / &#8211;no-log-certs</p>
<dd> include standard cert values in commit logs</p>
<dt>&#8211;log-revids / &#8211;no-log-revids</p>
<dd> include revision ids in commit logs</p>
<dt>&#8211;refs &lt;arg&gt;</p>
<dd> include git refs for &#8216;revs&#8217;, &#8216;roots&#8217; or &#8216;leaves&#8217;</p>
<dt>&#8211;use-one-changelog</p>
<dd> use only one changelog cert for the git commit message</dl>
</dl>
</dl>
<h3>command group &#8216;workspace&#8217;</h3>
<p> Commands that deal with the workspace.</p>
<dl>
<dt><code>add </code> [PATH]&#8230;</p>
<dd> Adds files to the workspace.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;no-respect-ignore / &#8211;respect-ignore</p>
<dd> do not ignore any files</p>
<dt>&#8211;recursive [ -R ] / &#8211;no-recursive</p>
<dd> also operate on the contents of any listed directories</p>
<dt>&#8211;unknown / &#8211;no-unknown</p>
<dd> perform the operations for unknown files from workspace</dl>
</dl>
<dt><code>attr drop </code> PATH [ATTR]</p>
<dd> Removes attributes from a file. If no attribute is specified, this command removes all attributes attached to the file given in PATH. Otherwise only removes the attribute specified in ATTR.</p>
<dt><code>attr get </code> PATH [ATTR]</p>
<dd> Gets the values of a file&#8217;s attributes. If no attribute is specified, this command prints all attributes attached to the file given in PATH. Otherwise it only prints the attribute specified in ATTR.</p>
<dt><code>attr set </code> PATH ATTR VALUE</p>
<dd> Sets an attribute on a file. Sets the attribute given on ATTR to the value specified in VALUE for the file mentioned in PATH.</p>
<dt><code>ci </code> [PATH]&#8230;</p>
<dd>
<dt><code>commit </code> [PATH]&#8230;</p>
<dd> Commits workspace changes to the database.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;author &lt;arg&gt;</p>
<dd> override author for commit</p>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;date &lt;arg&gt;</p>
<dd> override date/time for commit</p>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;message [ -m ] &lt;arg&gt;</p>
<dd> set commit changelog message</p>
<dt>&#8211;message-file &lt;arg&gt;</p>
<dd> set filename containing commit changelog message</dl>
</dl>
<dt><code>drop </code> [PATH]&#8230;</p>
<dd>
<dt><code>rm </code> [PATH]&#8230;</p>
<dd> Drops files from the workspace.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;bookkeep-only</p>
<dd> only update monotone&#8217;s internal bookkeeping, not the filesystem</p>
<dt>&#8211;missing</p>
<dd> perform the operations for files missing from workspace</p>
<dt>&#8211;recursive [ -R ] / &#8211;no-recursive</p>
<dd> also operate on the contents of any listed directories</dl>
</dl>
<dt><code>mkdir </code> [DIRECTORY&#8230;]</p>
<dd> Creates directories and adds them to the workspace.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;no-respect-ignore / &#8211;respect-ignore</p>
<dd> do not ignore any files</dl>
</dl>
<dt><code>pivot_root </code> NEW_ROOT PUT_OLD</p>
<dd> Renames the root directory. After this command, the directory that currently has the name NEW_ROOT will be the root directory, and the directory that is currently the root directory will have name PUT_OLD. Use of &#8216;&#8211;bookkeep-only&#8217; is NOT recommended.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;bookkeep-only</p>
<dd> only update monotone&#8217;s internal bookkeeping, not the filesystem</p>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</dl>
</dl>
<dt><code>pluck </code> [PATH&#8230;]</p>
<dd> Applies changes made at arbitrary places in history. This command takes changes made at any point in history, and edits your current workspace to include those changes. The end result is identical to &#8216;mtn diff -r FROM -r TO | patch -p0&#8217;, except that this command uses monotone&#8217;s merger, and thus intelligently handles renames, conflicts, and so on. If one revision is given, applies the changes made in that revision compared to its parent. If two revisions are given, applies the changes made to get from the first revision to the second.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
<dt><code>mv </code> SRC DEST</p>
<dd>
<dt><code>mv </code> SRC1 [SRC2 [&#8230;]] DEST_DIR</p>
<dd>
<dt><code>rename </code> SRC DEST</p>
<dd>
<dt><code>rename </code> SRC1 [SRC2 [&#8230;]] DEST_DIR</p>
<dd> Renames entries in the workspace.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;bookkeep-only</p>
<dd> only update monotone&#8217;s internal bookkeeping, not the filesystem</dl>
</dl>
<dt><code>revert </code> [PATH]&#8230;</p>
<dd> Reverts files and/or directories. In order to revert the entire workspace, specify &#8216;.&#8217; as the file name.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;depth &lt;arg&gt;</p>
<dd> limit the number of levels of directories to descend</p>
<dt>&#8211;exclude &lt;arg&gt;</p>
<dd> leave out anything described by its argument</p>
<dt>&#8211;missing</p>
<dd> perform the operations for files missing from workspace</dl>
</dl>
<dt><code>undrop </code> PATH&#8230;</p>
<dd> Reverses a mistaken &#8216;drop&#8217;. If the file was deleted from the workspace, this is the same as &#8216;revert&#8217;. Otherwise, it just removes the &#8216;drop&#8217; from the manifest.</p>
<dt><code>update </code></p>
<dd> Updates the workspace. This command modifies your workspace to be based off of a different revision, preserving uncommitted changes as it does so. If a revision is given, update the workspace to that revision. If not, update the workspace to the head of the branch.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;branch [ -b ] &lt;arg&gt;</p>
<dd> select branch cert for operation</p>
<dt>&#8211;move-conflicting-paths / &#8211;no-move-conflicting-paths</p>
<dd> move conflicting, unversioned paths into &#8216;_MTN/resolutions&#8217; before proceeding with any workspace change</p>
<dt>&#8211;revision [ -r ] &lt;arg&gt;</p>
<dd> select revision id for operation</dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> info mtn and the documentation on <code><a rel="nofollow" href="http://www.monotone.ca/docs">http://www.monotone.ca/docs</a></code></p>
<h2>BUGS</h2>
<p> Please report bugs to <code><a rel="nofollow" href="https://code.monotone.ca/p/monotone/issues/">https://code.monotone.ca/p/monotone/issues/</a></code>.</p>
<h2>AUTHORS</h2>
<p> monotone was written originally by Graydon Hoare &lt;graydon [at] pobox.com&gt; in 2003 and has since then received numerous contributions from many individuals. A complete list of authors can be found in AUTHORS. </p>
<p> Nowadays, monotone is maintained by a collective of enthusiastic programmers, known as the monotone development team.</p>
<h2>COPYRIGHT</h2>
<p> monotone and this man page is Copyright (c) 2003 &#8211; 2016 by the monotone development team. </p>
<h2>Index</h2>
