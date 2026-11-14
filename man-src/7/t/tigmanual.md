---
title: "tigmanual(7)"
name: "tigmanual"
section: "7"
letter: "t"
url: "/docs/linux/man/7-tigmanual/"
description: "tigmanual – text-mode interface for Git"
---

<p>tigmanual &#8211; text-mode interface for Git</p>
<h2>Synopsis</h2>
<pre>tig [options] [revisions] [--] [paths]
tig show [options] [revisions] [--] [paths]
tig blame [options] [rev] [--] path
tig status
tig &lt; [Git command output]</pre>
<h2>Description</h2>
<p>This is the manual for Tig, the ncurses-based text-mode interface for git. Tig allows you to browse changes in a Git repository and can additionally act as a pager for output of various Git commands. When used as a pager, it will display input from stdin and colorize it. </p>
<p> When browsing repositories, Tig uses the underlying Git commands to present the user with various views, such as summarized commit log and showing the commit with the log message, diffstat, and the diff.</p>
<h2>Calling Conventions</h2>
<h3>Pager Mode</h3>
<p>If stdin is a pipe, any log or diff options will be ignored and the pager view will be opened loading data from stdin. The pager mode can be used for colorizing output from various Git commands. </p>
<p> Example on how to colorize the output of <a href="/docs/linux/man/1-git-show/">git-show</a>(1): </p>
<dl>
<dd>
<pre>$ git show | tig</pre>
</dl>
<h3>Git Command Options</h3>
<p>All Git command options specified on the command line will be passed to the given command and all will be shell quoted before they are passed to the shell. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If you specify options for the main view, you should not use the &#8211;pretty option as this option will be set automatically to the format expected by the main view. </p>
</dl>
<p> Example on how to view a commit and show both author and committer information: </p>
<dl>
<dd>
<pre>$ tig show --pretty=fuller</pre>
</dl>
<p> See the section on specifying revisions for an introduction to revision options supported by the Git commands. For details on specific Git command options, refer to the man page of the command in question.</p>
<h2>The Viewer</h2>
<p>The display consists of a status window on the last line of the screen and one or more views. The default is to only show one view at a time but it is possible to split both the main and log view to also show the commit diff. </p>
<p> If you are in the log view and press <i>Enter</i> when the current line is a commit line, such as: </p>
<dl>
<dd>
<pre>commit 4d55caff4cc89335192f3e566004b4ceef572521</pre>
</dl>
<p> You will split the view so that the log view is displayed in the top window and the diff view in the bottom window. You can switch between the two views by pressing <i>Tab</i>. To maximize the log view again, simply press <i>l</i>.</p>
<h3>Views</h3>
<p>Various <i>views</i> of a repository are presented. Each view is based on output from an external command, most often <i>git log</i>, <i>git diff</i>, or <i>git show</i>. </p>
<p> The main view</p>
<dl>
<dd>Is the default view, and it shows a one line summary of each commit in the chosen list of revisions. The summary includes author date, author, and the first line of the log message. Additionally, any repository references, such as tags, will be shown.</dl>
<p> The log view</p>
<dl>
<dd>Presents a more rich view of the revision log showing the whole log message and the diffstat.</dl>
<p> The reflog view</p>
<dl>
<dd>Presents a view of the reflog allowing to navigate the repo history.</dl>
<p> The diff view</p>
<dl>
<dd>Shows either the diff of the current working tree, that is, what has changed since the last commit, or the commit diff complete with log message, diffstat and diff.</dl>
<p> The tree view</p>
<dl>
<dd>Lists directory trees associated with the current revision allowing subdirectories to be descended or ascended and file blobs to be viewed.</dl>
<p> The blob view</p>
<dl>
<dd>Displays the file content or &quot;blob&quot; of data associated with a file name.</dl>
<p> The blame view</p>
<dl>
<dd>Displays the file content annotated or blamed by commits.</dl>
<p> The refs view</p>
<dl>
<dd>Displays the branches, remotes and tags in the repository.</dl>
<p> The status view</p>
<dl>
<dd>Displays status of files in the working tree and allows changes to be staged/unstaged as well as adding of untracked files.</dl>
<p> The stage view</p>
<dl>
<dd>Displays diff changes for staged or unstaged files being tracked or file content of untracked files.</dl>
<p> The stash view</p>
<dl>
<dd>Displays the list of stashes in the repository.</dl>
<p> The grep view</p>
<dl>
<dd>Displays a list of files and all the lines that matches a search pattern.</dl>
<p> The pager view</p>
<dl>
<dd>Is used for displaying both input from stdin and output from Git commands entered in the internal prompt.</dl>
<p> The help view</p>
<dl>
<dd>Displays a quick reference of key bindings.</dl>
<h3>Browsing State and User-defined Commands</h3>
<p>The viewer keeps track of both what head and commit ID you are currently viewing. The commit ID will follow the cursor line and change every time you highlight a different commit. Whenever you reopen the diff view it will be reloaded, if the commit ID changed. The head ID is used when opening the main and log view to indicate from what revision to show history. </p>
<p> Some of the commands used or provided by Tig can be configured. This goes for some of the environment variables as well as the external commands. These user-defined commands can use arguments that refer to the current browsing state by using one of the following variables. </p>
<p> <code>Table 1. Browsing state variables</code> </p>
<table>
<tr VALIGN=top>
<td>
<p> %(head) </td>
<td>
<p> The currently viewed <i>head</i> ID. Defaults to HEAD
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(commit) </td>
<td>
<p> The currently selected commit ID.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(blob) </td>
<td>
<p> The currently selected blob ID.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(branch) </td>
<td>
<p> The currently selected branch name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(remote) </td>
<td>
<p> The currently selected remote name. For remote branches %(branch) will contain the branch name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(tag) </td>
<td>
<p> The currently selected tag name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(stash) </td>
<td>
<p> The currently selected stash name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(directory) </td>
<td>
<p> The current directory path in the tree view or &quot;.&quot; if undefined.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(file) </td>
<td>
<p> The currently selected file.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(lineno) </td>
<td>
<p> The currently selected line number. Defaults to 0.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(ref) </td>
<td>
<p> The reference given to blame or HEAD if undefined.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(revargs) </td>
<td>
<p> The revision arguments passed on the command line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(fileargs) </td>
<td>
<p> The file arguments passed on the command line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(cmdlineargs) </td>
<td>
<p> All other options passed on the command line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(diffargs) </td>
<td>
<p> Options from <i>diff-options</i> or <i>TIG_DIFF_OPTS</i> used by the diff and stage view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(blameargs) </td>
<td>
<p> Options from <i>blame-options</i> used by the blame view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(logargs) </td>
<td>
<p> Options from <i>log-options</i> used by the log view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(mainargs) </td>
<td>
<p> Options from <i>main-options</i> used by the main view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(prompt) </td>
<td>
<p> Prompt for the argument value. Optionally specify a custom prompt using &quot;%(prompt Enter branch name: )&quot;
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(text) </td>
<td>
<p> The text of the currently selected line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:head) </td>
<td>
<p> The name of the checked out branch, e.g. master
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:head-id) </td>
<td>
<p> The commit ID of the checked out branch.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:remote) </td>
<td>
<p> The remote associated with the checked out branch, e.g. origin/master.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:cdup) </td>
<td>
<p> The path to change directory to the repository root, e.g. ../
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:prefix) </td>
<td>
<p> The path prefix of the current work directory, e.g subdir/.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:git-dir) </td>
<td>
<p> The path to the Git directory, e.g. /src/repo/.git.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:worktree) </td>
<td>
<p> The worktree path, if defined.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:is-inside-work-tree) </td>
<td>
<p> Whether Tig is running inside a work tree, either true or false.
</td>
</tr>
</table>
<p> Example user-defined commands: </p>
<dl>
<dd>&bull; Allow to amend the last commit: </p>
<dl>
<dd>
<pre>bind generic + !git commit --amend</pre>
</dl>
</dl>
<dl>
<dd>&bull; Copy commit ID to clipboard: </p>
<dl>
<dd>
<pre>bind generic 9 !@sh -c &quot;echo -n %(commit) | xclip -selection c&quot;</pre>
</dl>
</dl>
<dl>
<dd>&bull; Add/edit notes for the current commit used during a review: </p>
<dl>
<dd>
<pre>bind generic T !git notes edit %(commit)</pre>
</dl>
</dl>
<dl>
<dd>&bull; Enter Git&#8217;s interactive add for fine-grained staging of file content: </p>
<dl>
<dd>
<pre>bind generic I !git add -i %(file)</pre>
</dl>
</dl>
<dl>
<dd>&bull; Rebase current branch on top of the selected branch: </p>
<dl>
<dd>
<pre>bind refs 3 !git rebase -i %(branch)</pre>
</dl>
</dl>
<h3>Title Windows</h3>
<p>Each view has a title window which shows the name of the view, current commit ID if available, and where the view is positioned: </p>
<dl>
<dd>
<pre>[main] c622eefaa485995320bc743431bae0d497b1d875 - commit 1 of 61 (1%)</pre>
</dl>
<p> By default, the title of the current view is highlighted using bold font. For long loading views (taking over 3 seconds) the time since loading started will be appended: </p>
<dl>
<dd>
<pre>[main] 77d9e40fbcea3238015aea403e06f61542df9a31 - commit 1 of 779 (0%) 5s</pre>
</dl>
<h2>Environment Variables</h2>
<p>Several options related to the interface with Git can be configured via environment options.</p>
<h3>Configuration Files</h3>
<p>Upon startup, Tig first reads the system wide configuration file ({sysconfdir}/tigrc by default) and then proceeds to read the user&#8217;s configuration file (~/.tigrc or $XDG_CONFIG_HOME/tig/config by default). The paths to either of these files can be overridden through the following environment variables: </p>
<p> TIGRC_USER</p>
<dl>
<dd>Path of the user configuration file.</dl>
<p> TIGRC_SYSTEM</p>
<dl>
<dd>Path of the system wide configuration file.</dl>
<h3>History Files</h3>
<p>If compiled with readline support, Tig writes a persistent command and search history to ~/.tig_history or $XDG_DATA_HOME/tig/history.</p>
<h3>Repository References</h3>
<p>Commits that are referenced by tags and branch heads will be marked by the reference name surrounded by <i>[</i> and <i>]</i>: </p>
<dl>
<dd>
<pre>2006-03-26 19:42 Petr Baudis | [cogito-0.17.1] Cogito 0.17.1</pre>
</dl>
<p> If you want to limit what branches are shown, say only show branches named master or those which start with the feature/ prefix, you can do it by setting the following variable: </p>
<dl>
<dd>
<pre>$ TIG_LS_REMOTE=&quot;git ls-remote . master feature/*&quot; tig</pre>
</dl>
<p> Or set the variable permanently in your environment. </p>
<p> TIG_LS_REMOTE</p>
<dl>
<dd>Command for retrieving all repository references. The command should output data in the same format as <a href="/docs/linux/man/1-git-ls-remote/">git-ls-remote</a>(1). Defaults to:</dl>
<dl>
<dd>
<pre>git ls-remote .</pre>
</dl>
<h3>Diff options</h3>
<p>It is possible to alter how diffs are shown by the diff view. If for example you prefer to have commit and author dates shown as relative dates, use: </p>
<dl>
<dd>
<pre>$ TIG_DIFF_OPTS=&quot;--relative-date&quot; tig</pre>
</dl>
<p> Or set the variable permanently in your environment.</p>
<h2>Default Keybindings</h2>
<p>Below the default key bindings are shown.</p>
<h3>View Switching</h3>
<table>
<tr VALIGN=top>
<td><code> Key </code></td>
<td><code> Action </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> m </td>
<td>
<p> Switch to main view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> d </td>
<td>
<p> Switch to diff view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> l </td>
<td>
<p> Switch to log view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> p </td>
<td>
<p> Switch to pager view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> t </td>
<td>
<p> Switch to (directory) tree view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> f </td>
<td>
<p> Switch to (file) blob view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> g </td>
<td>
<p> Switch to grep view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> b </td>
<td>
<p> Switch to blame view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> r </td>
<td>
<p> Switch to refs view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> y </td>
<td>
<p> Switch to stash view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> h </td>
<td>
<p> Switch to help view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> s </td>
<td>
<p> Switch to status view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> c </td>
<td>
<p> Switch to stage view
</td>
</tr>
</table>
<h3>View Manipulation</h3>
<table>
<tr VALIGN=top>
<td><code> Key </code></td>
<td><code> Action </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> q </td>
<td>
<p> Close view, if multiple views are open it will jump back to the previous view in the view stack. If it is the last open view it will quit. Use <i>Q</i> to quit all views at once.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Enter </td>
<td>
<p> This key is &quot;context sensitive&quot; depending on what view you are currently in. When in log view on a commit line or in the main view, split the view and show the commit diff. In the diff view pressing Enter will simply scroll the view one line down.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Tab </td>
<td>
<p> Switch to next view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> R </td>
<td>
<p> Reload and refresh the current view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> O </td>
<td>
<p> Maximize the current view to fill the whole display.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Up </td>
<td>
<p> This key is &quot;context sensitive&quot; and will move the cursor one line up. However, if you opened a split view it will change the cursor to point to the previous commit in the parent view and update the child view to display it. If you prefer this key to move the cursor or scroll within the diff view instead, use bind diff &lt;Up&gt; move-up or bind diff &lt;Up&gt; scroll-line-up, respectively.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Down </td>
<td>
<p> Similar to <i>Up</i> but will move down.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> , </td>
<td>
<p> Move to parent. In the tree view, this means switch to the parent directory. In the blame view it will load blame for the parent commit. For merges the parent is queried.
</td>
</tr>
</table>
<h3>View Specific Actions</h3>
<table>
<tr VALIGN=top>
<td><code> Key </code></td>
<td><code> Action </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> u </td>
<td>
<p> Update status of file. In the status view, this allows you to add an untracked file or stage changes to a file for next commit (similar to running git-add &lt;filename&gt;). In the stage view, when pressing this on a diff chunk line stages only that chunk for next commit, when not on a diff chunk line all changes in the displayed diff are staged.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> M </td>
<td>
<p> Resolve unmerged file by launching <a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a>(1). Note, to work correctly this might require some initial configuration of your preferred merge tool. See the manpage of <a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a>(1).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ! </td>
<td>
<p> Checkout file with unstaged changes. This will reset the file to contain the content it had at last commit.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 1 </td>
<td>
<p> Stage single diff line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> @ </td>
<td>
<p> Move to next chunk in the stage view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ] </td>
<td>
<p> Increase the diff context.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> [ </td>
<td>
<p> Decrease the diff context.
</td>
</tr>
</table>
<h3>Cursor Navigation</h3>
<table>
<tr VALIGN=top>
<td><code> Key </code></td>
<td><code> Action </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> k </td>
<td>
<p> Move cursor one line up.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> j </td>
<td>
<p> Move cursor one line down.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> PgUp,-,a </td>
<td>
<p> Move cursor one page up.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> PgDown, Space </td>
<td>
<p> Move cursor one page down.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> End </td>
<td>
<p> Jump to last line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Home </td>
<td>
<p> Jump to first line.
</td>
</tr>
</table>
<h3>Scrolling</h3>
<table>
<tr VALIGN=top>
<td><code> Key </code></td>
<td><code> Action </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Insert </td>
<td>
<p> Scroll view one line up.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Delete </td>
<td>
<p> Scroll view one line down.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ScrollBack </td>
<td>
<p> Scroll view one page up.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ScrollFwd </td>
<td>
<p> Scroll view one page down.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Left </td>
<td>
<p> Scroll view one column left.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Right </td>
<td>
<p> Scroll view one column right.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> | </td>
<td>
<p> Scroll view to the first column.
</td>
</tr>
</table>
<h3>Searching</h3>
<table>
<tr VALIGN=top>
<td><code> Key </code></td>
<td><code> Action </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> / </td>
<td>
<p> Search the view. Opens a prompt for entering search regexp to use.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ? </td>
<td>
<p> Search backwards in the view. Also prompts for regexp.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> n </td>
<td>
<p> Find next match for the current search regexp.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> N </td>
<td>
<p> Find previous match for the current search regexp.
</td>
</tr>
</table>
<h3>Misc</h3>
<table>
<tr VALIGN=top>
<td><code> Key </code></td>
<td><code> Action </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Q </td>
<td>
<p> Quit.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> &lt;C-L&gt; </td>
<td>
<p> Redraw screen.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> z </td>
<td>
<p> Stop all background loading. This can be useful if you use Tig in a repository with a long history without limiting the revision log.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> v </td>
<td>
<p> Show version.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> o </td>
<td>
<p> Open option menu
</td>
</tr>
<tr VALIGN=top>
<td>
<p> # </td>
<td>
<p> Toggle line numbers on/off.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> D </td>
<td>
<p> Toggle date display on/off/relative/relative-compact/custom
</td>
</tr>
<tr VALIGN=top>
<td>
<p> A </td>
<td>
<p> Toggle author display on/off/abbreviated/email/email user name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> G </td>
<td>
<p> Toggle revision graph visualization on/off.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ~ </td>
<td>
<p> Toggle (line) graphics mode
</td>
</tr>
<tr VALIGN=top>
<td>
<p> F </td>
<td>
<p> Toggle reference display on/off (tag and branch names).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> W </td>
<td>
<p> Toggle ignoring whitespace on/off for diffs
</td>
</tr>
<tr VALIGN=top>
<td>
<p> X </td>
<td>
<p> Toggle commit ID display on/off
</td>
</tr>
<tr VALIGN=top>
<td>
<p> % </td>
<td>
<p> Toggle file filtering in order to see the full diff instead of only the diff concerning the currently selected file.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> $ </td>
<td>
<p> Toggle highlighting of commit title overflow.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> H </td>
<td>
<p> Go to the HEAD commit.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> : </td>
<td>
<p> Open prompt. This allows you to specify what command to run and also to jump to a specific line, e.g. :23
</td>
</tr>
<tr VALIGN=top>
<td>
<p> e </td>
<td>
<p> Open file in editor.
</td>
</tr>
</table>
<h3>Prompt</h3>
<table>
<tr VALIGN=top>
<td><code> Key </code></td>
<td><code> Action </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :&lt;number&gt; </td>
<td>
<p> Jump to the specific line number, e.g. :80.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :&lt;sha&gt; </td>
<td>
<p> Jump to a specific commit, e.g. :2f12bcc.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :&lt;x&gt; </td>
<td>
<p> Execute the corresponding key binding, e.g. :q.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :!&lt;command&gt; </td>
<td>
<p> Execute a system command in a pager, e.g. :!git log -p.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :&lt;action&gt; </td>
<td>
<p> Execute a Tig command, e.g. :edit.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :goto &lt;rev&gt; </td>
<td>
<p> Jump to a specific revision, e.g. :goto %(commit)^2 to goto the current commit&#8217;s 2nd parent or :goto some/branch to goto the commit denoting the branch some/branch.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :save-display &lt;file&gt; </td>
<td>
<p> Save current display to &lt;file&gt;.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :save-options &lt;file&gt; </td>
<td>
<p> Save current options to &lt;file&gt;.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :save-view &lt;file&gt; </td>
<td>
<p> Save view info to &lt;file&gt; (for testing purposes).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :script &lt;file&gt; </td>
<td>
<p> Execute commands from &lt;file&gt;.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :exec &lt;flags&gt;&lt;args&#8230;&gt; </td>
<td>
<p> Execute command using &lt;args&gt; with external user-defined command option flags defined in &lt;flags&gt;.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> :echo &lt;args&#8230;&gt; </td>
<td>
<p> Display text in the status bar.
</td>
</tr>
</table>
<h3>External Commands</h3>
<p>For more custom needs, external commands provide a way to easily execute a script or program. They are bound to keys and use information from the current browsing state, such as the current commit ID. Tig comes with the following built-in external commands: </p>
<table>
<tr VALIGN=top>
<td><code> Keymap </code></td>
<td><code> Key </code></td>
<td><code> Action </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main </td>
<td>
<p> C </td>
<td>
<p> git cherry-pick %(commit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> status </td>
<td>
<p> C </td>
<td>
<p> git commit
</td>
</tr>
<tr VALIGN=top>
<td>
<p> generic </td>
<td>
<p> G </td>
<td>
<p> git gc
</td>
</tr>
</table>
<h2>Revision Specification</h2>
<p>This section describes various ways to specify what revisions to display or otherwise limit the view to. Tig does not itself parse the described revision options so refer to the relevant Git man pages for further information. Relevant man pages besides <a href="/docs/linux/man/1-git-log/">git-log</a>(1) are <a href="/docs/linux/man/1-git-diff/">git-diff</a>(1) and <a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a>(1). </p>
<p> You can tune the interaction with Git by making use of the options explained in this section. For example, by configuring the environment variable described in the section on diff options.</p>
<h3>Limit by Path Name</h3>
<p>If you are interested only in those revisions that made changes to a specific file (or even several files) list the files like this: </p>
<dl>
<dd>
<pre>$ tig Makefile README</pre>
</dl>
<p> To avoid ambiguity with Tig&#8217;s subcommands or repository references such as tag names, be sure to separate file names from other Git options using &quot;&#8211;&quot;. So if you have a file named <i>status</i> it will clash with the <i>status</i> subcommand, and thus you will have to use: </p>
<dl>
<dd>
<pre>$ tig -- status</pre>
</dl>
<h3>Limit by Date or Number</h3>
<p>To speed up interaction with Git, you can limit the amount of commits to show both for the log and main view. Either limit by date using e.g. &#8211;since=1.month or limit by the number of commits using -n400. </p>
<p> If you are only interested in changes that happened between two dates you can use: </p>
<dl>
<dd>
<pre>$ tig --after=&quot;May 5th&quot; --before=&quot;2006-05-16 15:44&quot;</pre>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If you want to avoid having to quote dates containing spaces you can use &quot;.&quot; instead, e.g. &#8211;after=May.5th. </p>
</dl>
<h3>Limiting by Commit Ranges</h3>
<p>Alternatively, commits can be limited to a specific range, such as &quot;all commits between <i>tag-1.0</i> and <i>tag-2.0</i>&quot;. For example: </p>
<dl>
<dd>
<pre>$ tig tag-1.0..tag-2.0</pre>
</dl>
<p> This way of commit limiting makes it trivial to only browse the commits which haven&#8217;t been pushed to a remote branch. Assuming <i>origin</i> is your upstream remote branch, using: </p>
<dl>
<dd>
<pre>$ tig origin..HEAD</pre>
</dl>
<p> will list what will be pushed to the remote branch. Optionally, the ending <i>HEAD</i> can be left out since it is implied.</p>
<h3>Limiting by Reachability</h3>
<p>Git interprets the range specifier &quot;tag-1.0..tag-2.0&quot; as &quot;all commits reachable from <i>tag-2.0</i> but not from <i>tag-1.0</i>&quot;. Where reachability refers to what commits are ancestors (or part of the history) of the branch or tagged revision in question. </p>
<p> If you prefer to specify which commit to preview in this way use the following: </p>
<dl>
<dd>
<pre>$ tig tag-2.0 ^tag-1.0</pre>
</dl>
<p> You can think of <i>^</i> as a negation operator. Using this alternate syntax, it is possible to further prune commits by specifying multiple branch cut offs.</p>
<h3>Combining Revisions Specification</h3>
<p>Revision options can to some degree be combined, which makes it possible to say &quot;show at most 20 commits from within the last month that changed files under the Documentation/ directory.&quot; </p>
<dl>
<dd>
<pre>$ tig --since=1.month -n20 -- Documentation/</pre>
</dl>
<h3>Examining All Repository References</h3>
<p>In some cases, it can be useful to query changes across all references in a repository. An example is to ask &quot;did any line of development in this repository change a particular file within the last week&quot;. This can be accomplished using: </p>
<dl>
<dd>
<pre>$ tig --all --since=1.week -- Makefile</pre>
</dl>
<h2>More Information</h2>
<p>Please visit Tig&#8217;s m[blue]<code>home page</code>m[]<font SIZE="-2">[1]</font> or m[blue]<code>main Git repository</code>m[]<font SIZE="-2">[2]</font> for information about new releases and how to report bugs and feature requests.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2006-2014 Jonas Fonseca &lt;m[blue]<code>jonas.fonseca [at] gmail.com</code>m[]<font SIZE="-2">[3]</font>&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p>Manpages: </p>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-tig/">tig</a></code>(1)</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/5-tigrc/">tigrc</a></code>(5)</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>home page</p>
<dl>
<dd><a rel="nofollow" href="https://jonas.github.io/tig">https://jonas.github.io/tig</a></dl>
<dt> 2.</p>
<dd>main Git repository</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/jonas/tig">https://github.com/jonas/tig</a></dl>
<dt> 3.</p>
<dd>jonas.fonseca [at] gmail.com</p>
<dl>
<dd>mailto:jonas.fonseca [at] gmail.com</dl>
