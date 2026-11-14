---
title: "git-p4(1)"
name: "git-p4"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-p4/"
description: "git-p4 – Import from and submit to Perforce repositories"
---

<h2 class="name">NAME</h2>
<p> git-p4 &#8211; Import from and submit to Perforce repositories </p>
<h2>SYNOPSIS</h2>
<pre><code>
git p4 clone[&lt;sync options&gt;][&lt;clone options&gt;]&lt;p4 depot path&gt;... git p4 sync[&lt;sync options&gt;][&lt;p4 depot path&gt;...] git p4 rebase
    git p4 submit[&lt;submit options&gt;][&lt;master branch name&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command provides a way to interact with p4 repositories using Git. </p>
<p> Create a new Git repository from an existing p4 repository using <i>git p4 clone</i>, giving it one or more p4 depot paths. Incorporate new commits from p4 changes with <i>git p4 sync</i>. The <i>sync</i> command is also used to include new branches from other p4 depot paths. Submit Git changes back to p4 using <i>git p4 submit</i>. The command <i>git p4 rebase</i> does a sync plus rebases the current branch onto the updated p4 remote branch.</p>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd> &bull; Clone a repository: </p>
<dl>
<dt>
<dd>
<pre>
$ git p4 clone //depot/path/project
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Do some work in the newly created Git repository: </p>
<dl>
<dt>
<dd>
<pre>
$ cd project
$ vi foo.h
$ git commit -a -m &quot;edited foo.h&quot;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Update the Git repository with recent changes from p4, rebasing your work on top: </p>
<dl>
<dt>
<dd>
<pre>
$ git p4 rebase
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Submit your commits back to p4: </p>
<dl>
<dt>
<dd>
<pre>
$ git p4 submit
</pre>
</dl>
</dl>
<h2>COMMANDS</h2>
<h3>Clone</h3>
<p> Generally, <i>git p4 clone</i> is used to create a new Git directory from an existing p4 repository: </p>
<dl>
<dt>
<dd>
<pre>
$ git p4 clone //depot/path/project
</pre>
</dl>
<p> This: </p>
<dl>
<dt>
<dd> 1. Creates an empty Git repository in a subdirectory called <i>project</i>.</dl>
<dl>
<dt>
<dd> 2. Imports the full contents of the head revision from the given p4 depot path into a single commit in the Git branch <i>refs/remotes/p4/master</i>.</dl>
<dl>
<dt>
<dd> 3. Creates a local branch, <i>master</i> from this remote and checks it out.</dl>
<p> To reproduce the entire p4 history in Git, use the <i>@all</i> modifier on the depot path: </p>
<dl>
<dt>
<dd>
<pre>
$ git p4 clone //depot/path/project@all
</pre>
</dl>
<h3>Sync</h3>
<p> As development continues in the p4 repository, those changes can be included in the Git repository using: </p>
<dl>
<dt>
<dd>
<pre>
$ git p4 sync
</pre>
</dl>
<p> This command finds new changes in p4 and imports them as Git commits. </p>
<p> P4 repositories can be added to an existing Git repository using <i>git p4 sync</i> too: </p>
<dl>
<dt>
<dd>
<pre>
$ mkdir repo-git
$ cd repo-git
$ git init
$ git p4 sync //path/in/your/perforce/depot
</pre>
</dl>
<p> This imports the specified depot into <i>refs/remotes/p4/master</i> in an existing Git repository. The <i>&#8211;branch</i> option can be used to specify a different branch to be used for the p4 content. </p>
<p> If a Git repository includes branches <i>refs/remotes/origin/p4</i>, these will be fetched and consulted first during a <i>git p4 sync</i>. Since importing directly from p4 is considerably slower than pulling changes from a Git remote, this can be useful in a multi-developer environment. </p>
<p> If there are multiple branches, doing <i>git p4 sync</i> will automatically use the &quot;BRANCH DETECTION&quot; algorithm to try to partition new changes into the right branch. This can be overridden with the <i>&#8211;branch</i> option to specify just a single branch to update.</p>
<h3>Rebase</h3>
<p> A common working pattern is to fetch the latest changes from the p4 depot and merge them with local uncommitted changes. Often, the p4 repository is the ultimate location for all code, thus a rebase workflow makes sense. This command does <i>git p4 sync</i> followed by <i>git rebase</i> to move local commits on top of updated p4 changes. </p>
<dl>
<dt>
<dd>
<pre>
$ git p4 rebase
</pre>
</dl>
<h3>Submit</h3>
<p> Submitting changes from a Git repository back to the p4 repository requires a separate p4 client workspace. This should be specified using the <i>P4CLIENT</i> environment variable or the Git configuration variable <i>git-p4.client</i>. The p4 client must exist, but the client root will be created and populated if it does not already exist. </p>
<p> To submit all changes that are in the current Git branch but not in the <i>p4/master</i> branch, use: </p>
<dl>
<dt>
<dd>
<pre>
$ git p4 submit
</pre>
</dl>
<p> To specify a branch other than the current one, use: </p>
<dl>
<dt>
<dd>
<pre>
$ git p4 submit topicbranch
</pre>
</dl>
<p> The upstream reference is generally <i>refs/remotes/p4/master</i>, but can be overridden using the <i>&#8211;origin=</i> command-line option. </p>
<p> The p4 changes will be created as the user invoking <i>git p4 submit</i>. The <i>&#8211;preserve-user</i> option will cause ownership to be modified according to the author of the Git commit. This option requires admin privileges in p4, which can be granted using <i>p4 protect</i>.</p>
<h2>OPTIONS</h2>
<h3>General options</h3>
<p> All commands except clone accept these options. </p>
<p> &#8211;git-dir &lt;dir&gt;</p>
<dl>
<dt>
<dd> Set the <i>GIT_DIR</i> environment variable. See <code><a href="/docs/linux/man/1-git/">git</a></code>(1).</dl>
<p> &#8211;verbose, -v</p>
<dl>
<dt>
<dd> Provide more progress information.</dl>
<h3>Sync options</h3>
<p> These options can be used in the initial <i>clone</i> as well as in subsequent <i>sync</i> operations. </p>
<p> &#8211;branch &lt;branch&gt;</p>
<dl>
<dt>
<dd> Import changes into given branch. If the branch starts with <i>refs/</i>, it will be used as is. Otherwise if it does not start with <i>p4/</i>, that prefix is added. The branch is assumed to name a remote tracking, but this can be modified using <i>&#8211;import-local</i>, or by giving a full ref name. The default branch is <i>master</i>. </p>
<p> This example imports a new remote &quot;p4/proj2&quot; into an existing Git repository: </p>
<dl>
<dt>
<dd>
<pre>
    $ git init
    $ git p4 sync --branch=refs/remotes/p4/proj2 //depot/proj2
</pre>
</dl>
</dl>
<p> &#8211;detect-branches</p>
<dl>
<dt>
<dd> Use the branch detection algorithm to find new paths in p4. It is documented below in &quot;BRANCH DETECTION&quot;.</dl>
<p> &#8211;changesfile &lt;file&gt;</p>
<dl>
<dt>
<dd> Import exactly the p4 change numbers listed in <i>file</i>, one per line. Normally, <i>git p4</i> inspects the current p4 repository state and detects the changes it should import.</dl>
<p> &#8211;silent</p>
<dl>
<dt>
<dd> Do not print any progress information.</dl>
<p> &#8211;detect-labels</p>
<dl>
<dt>
<dd> Query p4 for labels associated with the depot paths, and add them as tags in Git. Limited usefulness as only imports labels associated with new changelists. Deprecated.</dl>
<p> &#8211;import-labels</p>
<dl>
<dt>
<dd> Import labels from p4 into Git.</dl>
<p> &#8211;import-local</p>
<dl>
<dt>
<dd> By default, p4 branches are stored in <i>refs/remotes/p4/</i>, where they will be treated as remote-tracking branches by <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) and other commands. This option instead puts p4 branches in <i>refs/heads/p4/</i>. Note that future sync operations must specify <i>&#8211;import-local</i> as well so that they can find the p4 branches in refs/heads.</dl>
<p> &#8211;max-changes &lt;n&gt;</p>
<dl>
<dt>
<dd> Limit the number of imported changes to <i>n</i>. Useful to limit the amount of history when using the <i>@all</i> p4 revision specifier.</dl>
<p> &#8211;keep-path</p>
<dl>
<dt>
<dd> The mapping of file names from the p4 depot path to Git, by default, involves removing the entire depot path. With this option, the full p4 depot path is retained in Git. For example, path <i>//depot/main/foo/bar.c</i>, when imported from <i>//depot/main/</i>, becomes <i>foo/bar.c</i>. With <i>&#8211;keep-path</i>, the Git path is instead <i>depot/main/foo/bar.c</i>.</dl>
<p> &#8211;use-client-spec</p>
<dl>
<dt>
<dd> Use a client spec to find the list of interesting files in p4. See the &quot;CLIENT SPEC&quot; section below.</dl>
<h3>Clone options</h3>
<p> These options can be used in an initial <i>clone</i>, along with the <i>sync</i> options described above. </p>
<p> &#8211;destination &lt;directory&gt;</p>
<dl>
<dt>
<dd> Where to create the Git repository. If not provided, the last component in the p4 depot path is used to create a new directory.</dl>
<p> &#8211;bare</p>
<dl>
<dt>
<dd> Perform a bare clone. See <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1).</dl>
<p> -/ &lt;path&gt;</p>
<dl>
<dt>
<dd> Exclude selected depot paths when cloning.</dl>
<h3>Submit options</h3>
<p> These options can be used to modify <i>git p4 submit</i> behavior. </p>
<p> &#8211;origin &lt;commit&gt;</p>
<dl>
<dt>
<dd> Upstream location from which commits are identified to submit to p4. By default, this is the most recent p4 commit reachable from <i>HEAD</i>.</dl>
<p> -M</p>
<dl>
<dt>
<dd> Detect renames. See <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1). Renames will be represented in p4 using explicit <i>move</i> operations. There is no corresponding option to detect copies, but there are variables for both moves and copies.</dl>
<p> &#8211;preserve-user</p>
<dl>
<dt>
<dd> Re-author p4 changes before submitting to p4. This option requires p4 admin privileges.</dl>
<p> &#8211;export-labels</p>
<dl>
<dt>
<dd> Export tags from Git as p4 labels. Tags found in Git are applied to the perforce working directory.</dl>
<p> &#8211;dry-run, -n</p>
<dl>
<dt>
<dd> Show just what commits would be submitted to p4; do not change state in Git or p4.</dl>
<p> &#8211;prepare-p4-only</p>
<dl>
<dt>
<dd> Apply a commit to the p4 workspace, opening, adding and deleting files in p4 as for a normal submit operation. Do not issue the final &quot;p4 submit&quot;, but instead print a message about how to submit manually or revert. This option always stops after the first (oldest) commit. Git tags are not exported to p4.</dl>
<p> &#8211;conflict=(ask|skip|quit)</p>
<dl>
<dt>
<dd> Conflicts can occur when applying a commit to p4. When this happens, the default behavior (&quot;ask&quot;) is to prompt whether to skip this commit and continue, or quit. This option can be used to bypass the prompt, causing conflicting commits to be automatically skipped, or to quit trying to apply commits, without prompting.</dl>
<p> &#8211;branch &lt;branch&gt;</p>
<dl>
<dt>
<dd> After submitting, sync this named branch instead of the default p4/master. See the &quot;Sync options&quot; section above for more information.</dl>
<h3>Rebase options</h3>
<p> These options can be used to modify <i>git p4 rebase</i> behavior. </p>
<p> &#8211;import-labels</p>
<dl>
<dt>
<dd> Import p4 labels.</dl>
<h2>DEPOT PATH SYNTAX</h2>
<p> The p4 depot path argument to <i>git p4 sync</i> and <i>git p4 clone</i> can be one or more space-separated p4 depot paths, with an optional p4 revision specifier on the end: </p>
<p> &quot;//depot/my/project&quot;</p>
<dl>
<dt>
<dd> Import one commit with all files in the <i>#head</i> change under that tree.</dl>
<p> &quot;//depot/my/project@all&quot;</p>
<dl>
<dt>
<dd> Import one commit for each change in the history of that depot path.</dl>
<p> &quot;//depot/my/project@1,6&quot;</p>
<dl>
<dt>
<dd> Import only changes 1 through 6.</dl>
<p> &quot;//depot/proj1@all //depot/proj2@all&quot;</p>
<dl>
<dt>
<dd> Import all changes from both named depot paths into a single repository. Only files below these directories are included. There is not a subdirectory in Git for each &quot;proj1&quot; and &quot;proj2&quot;. You must use the <i>&#8211;destination</i> option when specifying more than one depot path. The revision specifier must be specified identically on each depot path. If there are files in the depot paths with the same name, the path with the most recently updated version of the file is the one that appears in Git.</dl>
<p> See <i>p4 help revisions</i> for the full syntax of p4 revision specifiers.</p>
<h2>CLIENT SPEC</h2>
<p> The p4 client specification is maintained with the <i>p4 client</i> command and contains among other fields, a View that specifies how the depot is mapped into the client repository. The <i>clone</i> and <i>sync</i> commands can consult the client spec when given the <i>&#8211;use-client-spec</i> option or when the useClientSpec variable is true. After <i>git p4 clone</i>, the useClientSpec variable is automatically set in the repository configuration file. This allows future <i>git p4 submit</i> commands to work properly; the submit command looks only at the variable and does not have a command-line option. </p>
<p> The full syntax for a p4 view is documented in <i>p4 help views</i>. <i>git p4</i> knows only a subset of the view syntax. It understands multi-line mappings, overlays with <i>+</i>, exclusions with <i>&#8211;</i> and double-quotes around whitespace. Of the possible wildcards, <i>git p4</i> only handles <i>&#8230;</i>, and only when it is at the end of the path. <i>git p4</i> will complain if it encounters an unhandled wildcard. </p>
<p> Bugs in the implementation of overlap mappings exist. If multiple depot paths map through overlays to the same location in the repository, <i>git p4</i> can choose the wrong one. This is hard to solve without dedicating a client spec just for <i>git p4</i>. </p>
<p> The name of the client can be given to <i>git p4</i> in multiple ways. The variable <i>git-p4.client</i> takes precedence if it exists. Otherwise, normal p4 mechanisms of determining the client are used: environment variable P4CLIENT, a file referenced by P4CONFIG, or the local host name.</p>
<h2>BRANCH DETECTION</h2>
<p> P4 does not have the same concept of a branch as Git. Instead, p4 organizes its content as a directory tree, where by convention different logical branches are in different locations in the tree. The <i>p4 branch</i> command is used to maintain mappings between different areas in the tree, and indicate related content. <i>git p4</i> can use these mappings to determine branch relationships. </p>
<p> If you have a repository where all the branches of interest exist as subdirectories of a single depot path, you can use <i>&#8211;detect-branches</i> when cloning or syncing to have <i>git p4</i> automatically find subdirectories in p4, and to generate these as branches in Git. </p>
<p> For example, if the P4 repository structure is: </p>
<dl>
<dt>
<dd>
<pre>
//depot/main/...
//depot/branch1/...
</pre>
</dl>
<p> And &quot;p4 branch -o branch1&quot; shows a View line that looks like: </p>
<dl>
<dt>
<dd>
<pre>
//depot/main/... //depot/branch1/...
</pre>
</dl>
<p> Then this <i>git p4 clone</i> command: </p>
<dl>
<dt>
<dd>
<pre>
git p4 clone --detect-branches //depot@all
</pre>
</dl>
<p> produces a separate branch in <i>refs/remotes/p4/</i> for //depot/main, called <i>master</i>, and one for //depot/branch1 called <i>depot/branch1</i>. </p>
<p> However, it is not necessary to create branches in p4 to be able to use them like branches. Because it is difficult to infer branch relationships automatically, a Git configuration setting <i>git-p4.branchList</i> can be used to explicitly identify branch relationships. It is a list of &quot;source:destination&quot; pairs, like a simple p4 branch specification, where the &quot;source&quot; and &quot;destination&quot; are the path elements in the p4 repository. The example above relied on the presence of the p4 branch. Without p4 branches, the same result will occur with: </p>
<dl>
<dt>
<dd>
<pre>
git init depot
cd depot
git config git-p4.branchList main:branch1
git p4 clone --detect-branches //depot@all .
</pre>
</dl>
<h2>PERFORMANCE</h2>
<p> The fast-import mechanism used by <i>git p4</i> creates one pack file for each invocation of <i>git p4 sync</i>. Normally, Git garbage compression (<code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1)) automatically compresses these to fewer pack files, but explicit invocation of <i>git repack -adf</i> may improve performance.</p>
<h2>CONFIGURATION VARIABLES</h2>
<p> The following config settings can be used to modify <i>git p4</i> behavior. They all are in the <i>git-p4</i> section.</p>
<h3>General variables</h3>
<p> git-p4.user</p>
<dl>
<dt>
<dd> User specified as an option to all p4 commands, with <i>-u &lt;user&gt;</i>. The environment variable <i>P4USER</i> can be used instead.</dl>
<p> git-p4.password</p>
<dl>
<dt>
<dd> Password specified as an option to all p4 commands, with <i>-P &lt;password&gt;</i>. The environment variable <i>P4PASS</i> can be used instead.</dl>
<p> git-p4.port</p>
<dl>
<dt>
<dd> Port specified as an option to all p4 commands, with <i>-p &lt;port&gt;</i>. The environment variable <i>P4PORT</i> can be used instead.</dl>
<p> git-p4.host</p>
<dl>
<dt>
<dd> Host specified as an option to all p4 commands, with <i>-h &lt;host&gt;</i>. The environment variable <i>P4HOST</i> can be used instead.</dl>
<p> git-p4.client</p>
<dl>
<dt>
<dd> Client specified as an option to all p4 commands, with <i>-c &lt;client&gt;</i>, including the client spec.</dl>
<h3>Clone and sync variables</h3>
<p> git-p4.syncFromOrigin</p>
<dl>
<dt>
<dd> Because importing commits from other Git repositories is much faster than importing them from p4, a mechanism exists to find p4 changes first in Git remotes. If branches exist under <i>refs/remote/origin/p4</i>, those will be fetched and used when syncing from p4. This variable can be set to <i>false</i> to disable this behavior.</dl>
<p> git-p4.branchUser</p>
<dl>
<dt>
<dd> One phase in branch detection involves looking at p4 branches to find new ones to import. By default, all branches are inspected. This option limits the search to just those owned by the single user named in the variable.</dl>
<p> git-p4.branchList</p>
<dl>
<dt>
<dd> List of branches to be imported when branch detection is enabled. Each entry should be a pair of branch names separated by a colon (:). This example declares that both branchA and branchB were created from main: </p>
<dl>
<dt>
<dd>
<pre>
git config       git-p4.branchList main:branchA
git config --add git-p4.branchList main:branchB
</pre>
</dl>
</dl>
<p> git-p4.ignoredP4Labels</p>
<dl>
<dt>
<dd> List of p4 labels to ignore. This is built automatically as unimportable labels are discovered.</dl>
<p> git-p4.importLabels</p>
<dl>
<dt>
<dd> Import p4 labels into git, as per &#8211;import-labels.</dl>
<p> git-p4.labelImportRegexp</p>
<dl>
<dt>
<dd> Only p4 labels matching this regular expression will be imported. The default value is <i>[a-zA-Z0-9_\-.]+$</i>.</dl>
<p> git-p4.useClientSpec</p>
<dl>
<dt>
<dd> Specify that the p4 client spec should be used to identify p4 depot paths of interest. This is equivalent to specifying the option <i>&#8211;use-client-spec</i>. See the &quot;CLIENT SPEC&quot; section above. This variable is a boolean, not the name of a p4 client.</dl>
<h3>Submit variables</h3>
<p> git-p4.detectRenames</p>
<dl>
<dt>
<dd> Detect renames. See <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1). This can be true, false, or a score as expected by <i>git diff -M</i>.</dl>
<p> git-p4.detectCopies</p>
<dl>
<dt>
<dd> Detect copies. See <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1). This can be true, false, or a score as expected by <i>git diff -C</i>.</dl>
<p> git-p4.detectCopiesHarder</p>
<dl>
<dt>
<dd> Detect copies harder. See <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1). A boolean.</dl>
<p> git-p4.preserveUser</p>
<dl>
<dt>
<dd> On submit, re-author changes to reflect the Git author, regardless of who invokes <i>git p4 submit</i>.</dl>
<p> git-p4.allowMissingP4Users</p>
<dl>
<dt>
<dd> When <i>preserveUser</i> is true, <i>git p4</i> normally dies if it cannot find an author in the p4 user map. This setting submits the change regardless.</dl>
<p> git-p4.skipSubmitEdit</p>
<dl>
<dt>
<dd> The submit process invokes the editor before each p4 change is submitted. If this setting is true, though, the editing step is skipped.</dl>
<p> git-p4.skipSubmitEditCheck</p>
<dl>
<dt>
<dd> After editing the p4 change message, <i>git p4</i> makes sure that the description really was changed by looking at the file modification time. This option disables that test.</dl>
<p> git-p4.allowSubmit</p>
<dl>
<dt>
<dd> By default, any branch can be used as the source for a <i>git p4 submit</i> operation. This configuration variable, if set, permits only the named branches to be used as submit sources. Branch names must be the short names (no &quot;refs/heads/&quot;), and should be separated by commas (&quot;,&quot;), with no spaces.</dl>
<p> git-p4.skipUserNameCheck</p>
<dl>
<dt>
<dd> If the user running <i>git p4 submit</i> does not exist in the p4 user map, <i>git p4</i> exits. This option can be used to force submission regardless.</dl>
<p> git-p4.attemptRCSCleanup</p>
<dl>
<dt>
<dd> If enabled, <i>git p4 submit</i> will attempt to cleanup RCS keywords ($Header$, etc). These would otherwise cause merge conflicts and prevent the submit going ahead. This option should be considered experimental at present.</dl>
<p> git-p4.exportLabels</p>
<dl>
<dt>
<dd> Export Git tags to p4 labels, as per &#8211;export-labels.</dl>
<p> git-p4.labelExportRegexp</p>
<dl>
<dt>
<dd> Only p4 labels matching this regular expression will be exported. The default value is <i>[a-zA-Z0-9_\-.]+$</i>.</dl>
<p> git-p4.conflict</p>
<dl>
<dt>
<dd> Specify submit behavior when a conflict with p4 is found, as per &#8211;conflict. The default behavior is <i>ask</i>.</dl>
<h2>IMPLEMENTATION DETAILS</h2>
<dl>
<dt>
<dd> &bull; Changesets from p4 are imported using Git fast-import.</dl>
<dl>
<dt>
<dd> &bull; Cloning or syncing does not require a p4 client; file contents are collected using <i>p4 print</i>.</dl>
<dl>
<dt>
<dd> &bull; Submitting requires a p4 client, which is not in the same location as the Git repository. Patches are applied, one at a time, to this p4 client and submitted from there.</dl>
<dl>
<dt>
<dd> &bull; Each commit imported by <i>git p4</i> has a line at the end of the log message indicating the p4 depot location and change number. This line is used by later <i>git p4 sync</i> operations to know which p4 changes are new.</dl>
<h2>Index</h2>
