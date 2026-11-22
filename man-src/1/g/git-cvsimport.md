---

title: "git-cvsimport(1)"
name: "git-cvsimport"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cvsimport/"
description: "git-cvsimport – Salvage your data out of another SCM people love to hate"
---

<p> git-cvsimport &#8211; Salvage your data out of another SCM people love to hate </p>
<h2>SYNOPSIS</h2>
<pre><code>
git cvsimport [-o &lt;branch-for-HEAD&gt;] [-h] [-v] [-d &lt;CVSROOT&gt;]
              [-A &lt;author-conv-file&gt;] [-p &lt;options-for-cvsps&gt;] [-P &lt;file&gt;]
              [-C &lt;git_repository&gt;] [-z &lt;fuzz&gt;] [-i] [-k] [-u] [-s &lt;subst&gt;]
              [-a] [-m] [-M &lt;regex&gt;] [-S &lt;regex&gt;] [-L &lt;commitlimit&gt;]
              [-r &lt;remote&gt;] [-R] [&lt;CVS_module&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>WARNING:</code> git cvsimport uses cvsps version 2, which is considered deprecated; it does not work with cvsps version 3 and later. If you are performing a one-shot import of a CVS repository consider using m[blue]<code>cvs2git</code>m[][1] or m[blue]<code>parsecvs</code>m[][2]. </p>
<p> Imports a CVS repository into Git. It will either create a new repository, or incrementally import into an existing one. </p>
<p> Splitting the CVS log into patch sets is done by <i>cvsps</i>. At least version 2.1 is required. </p>
<p> <code>WARNING:</code> for certain situations the import leads to incorrect results. Please see the section ISSUES for further reference. </p>
<p> You should <code>never</code> do any work of your own on the branches that are created by <i>git cvsimport</i>. By default initial import will create and populate a &quot;master&quot; branch from the CVS repository&#8217;s main branch which you&#8217;re free to work with; after that, you need to <i>git merge</i> incremental imports, or any CVS branches, yourself. It is advisable to specify a named remote via -r to separate and protect the incoming branches. </p>
<p> If you intend to set up a shared public repository that all developers can read/write, or if you want to use <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1), then you probably want to make a bare clone of the imported repository, and use the clone as the shared repository. See <code><a href="/docs/linux/man/7-gitcvs-migration/">gitcvs-migration</a></code>(7).</p>
<h2>OPTIONS</h2>
<p> -v</p>
<dl>
<dt>
</dt><dd> Verbosity: let <i>cvsimport</i> report what it is doing.</dd></dl>
<p> -d &lt;CVSROOT&gt;</p>
<dl>
<dt>
</dt><dd> The root of the CVS archive. May be local (a simple path) or remote; currently, only the :local:, :ext: and :pserver: access methods are supported. If not given, <i>git cvsimport</i> will try to read it from CVS/Root. If no such file exists, it checks for the CVSROOT environment variable.</dd></dl>
<p> &lt;CVS_module&gt;</p>
<dl>
<dt>
</dt><dd> The CVS module you want to import. Relative to &lt;CVSROOT&gt;. If not given, <i>git cvsimport</i> tries to read it from CVS/Repository.</dd></dl>
<p> -C &lt;target-dir&gt;</p>
<dl>
<dt>
</dt><dd> The Git repository to import to. If the directory doesn&#8217;t exist, it will be created. Default is the current directory.</dd></dl>
<p> -r &lt;remote&gt;</p>
<dl>
<dt>
</dt><dd> The Git remote to import this CVS repository into. Moves all CVS branches into remotes/&lt;remote&gt;/&lt;branch&gt; akin to the way <i>git clone</i> uses <i>origin</i> by default.</dd></dl>
<p> -o &lt;branch-for-HEAD&gt;</p>
<dl>
<dt>
</dt><dd> When no remote is specified (via -r) the <i>HEAD</i> branch from CVS is imported to the <i>origin</i> branch within the Git repository, as <i>HEAD</i> already has a special meaning for Git. When a remote is specified the <i>HEAD</i> branch is named remotes/&lt;remote&gt;/master mirroring <i>git clone</i> behaviour. Use this option if you want to import into a different branch. </dd>
<p> Use <i>-o master</i> for continuing an import that was initially done by the old cvs2git tool.</dl>
<p> -i</p>
<dl>
<dt>
</dt><dd> Import-only: don&#8217;t perform a checkout after importing. This option ensures the working directory and index remain untouched and will not create them if they do not exist.</dd></dl>
<p> -k</p>
<dl>
<dt>
</dt><dd> Kill keywords: will extract files with <i>-kk</i> from the CVS archive to avoid noisy changesets. Highly recommended, but off by default to preserve compatibility with early imported trees.</dd></dl>
<p> -u</p>
<dl>
<dt>
</dt><dd> Convert underscores in tag and branch names to dots.</dd></dl>
<p> -s &lt;subst&gt;</p>
<dl>
<dt>
</dt><dd> Substitute the character &quot;/&quot; in branch names with &lt;subst&gt;</dd></dl>
<p> -p &lt;options-for-cvsps&gt;</p>
<dl>
<dt>
</dt><dd> Additional options for cvsps. The options <i>-u</i> and <i>-A</i> are implicit and should not be used here. </dd>
<p> If you need to pass multiple options, separate them with a comma.</dl>
<p> -z &lt;fuzz&gt;</p>
<dl>
<dt>
</dt><dd> Pass the timestamp fuzz factor to cvsps, in seconds. If unset, cvsps defaults to 300s.</dd></dl>
<p> -P &lt;cvsps-output-file&gt;</p>
<dl>
<dt>
</dt><dd> Instead of calling cvsps, read the provided cvsps output file. Useful for debugging or when cvsps is being handled outside cvsimport.</dd></dl>
<p> -m</p>
<dl>
<dt>
</dt><dd> Attempt to detect merges based on the commit message. This option will enable default regexes that try to capture the source branch name from the commit message.</dd></dl>
<p> -M &lt;regex&gt;</p>
<dl>
<dt>
</dt><dd> Attempt to detect merges based on the commit message with a custom regex. It can be used with <i>-m</i> to enable the default regexes as well. You must escape forward slashes. </dd>
<p> The regex must capture the source branch name in $1. </p>
<p> This option can be used several times to provide several detection regexes.</dl>
<p> -S &lt;regex&gt;</p>
<dl>
<dt>
</dt><dd> Skip paths matching the regex.</dd></dl>
<p> -a</p>
<dl>
<dt>
</dt><dd> Import all commits, including recent ones. cvsimport by default skips commits that have a timestamp less than 10 minutes ago.</dd></dl>
<p> -L &lt;limit&gt;</p>
<dl>
<dt>
</dt><dd> Limit the number of commits imported. Workaround for cases where cvsimport leaks memory.</dd></dl>
<p> -A &lt;author-conv-file&gt;</p>
<dl>
<dt>
</dt><dd> CVS by default uses the Unix username when writing its commit logs. Using this option and an author-conv-file maps the name recorded in CVS to author name, e-mail and optional timezone: </dd>
<dl>
<dt>
</dt><dd>
<pre><code>
exon = Andreas Ericsson&lt;ae[at] op5.se&gt;
    spawn = Simon Pawn&lt;spawn[at] frog - pond.org&gt; America / Chicago
</code></pre>
</dd></dl>
<p> <i>git cvsimport</i> will make it appear as those authors had their GIT_AUTHOR_NAME and GIT_AUTHOR_EMAIL set properly all along. If a timezone is specified, GIT_AUTHOR_DATE will have the corresponding offset applied. </p>
<p> For convenience, this data is saved to $GIT_DIR/cvs-authors each time the <i>-A</i> option is provided and read from that same file each time <i>git cvsimport</i> is run. </p>
<p> It is not recommended to use this feature if you intend to export changes back to CVS again later with <i>git cvsexportcommit</i>.</dl>
<p> -R</p>
<dl>
<dt>
</dt><dd> Generate a $GIT_DIR/cvs-revisions file containing a mapping from CVS revision numbers to newly-created Git commit IDs. The generated file will contain one line for each (filename, revision) pair imported; each line will look like </dd>
<dl>
<dt>
</dt><dd>
<pre>
src/widget.c 1.1 1d862f173cdc7325b6fa6d2ae1cfd61fd1b512b7
</pre>
</dd></dl>
<p> The revision data is appended to the file if it already exists, for use when doing incremental imports. </p>
<p> This option may be useful if you have CVS revision numbers stored in commit messages, bug-tracking systems, email archives, and the like.</dl>
<p> -h</p>
<dl>
<dt>
</dt><dd> Print a short usage message and exit.</dd></dl>
<h2>OUTPUT</h2>
<p> If <i>-v</i> is specified, the script reports what it is doing. </p>
<p> Otherwise, success is indicated the Unix way, i.e. by simply exiting with a zero exit status.</p>
<h2>ISSUES</h2>
<p> Problems related to timestamps: </p>
<dl>
<dt>
</dt><dd> &bull; If timestamps of commits in the CVS repository are not stable enough to be used for ordering commits changes may show up in the wrong order.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; If any files were ever &quot;cvs import&quot;ed more than once (e.g., import of more than one vendor release) the HEAD contains the wrong content.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; If the timestamp order of different files cross the revision order within the commit matching time window the order of commits may be wrong.</dd></dl>
<p> Problems related to branches: </p>
<dl>
<dt>
</dt><dd> &bull; Branches on which no commits have been made are not imported.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; All files from the branching point are added to a branch even if never added in CVS.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; This applies to files added to the source branch <code>after</code> a daughter branch was created: if previously no commit was made on the daughter branch they will erroneously be added to the daughter branch in git.</dd></dl>
<p> Problems related to tags: </p>
<dl>
<dt>
</dt><dd> &bull; Multiple tags on the same revision are not imported.</dd></dl>
<p> If you suspect that any of these issues may apply to the repository you want to imort, consider using cvs2git: </p>
<dl>
<dt>
</dt><dd> &bull; cvs2git (part of cvs2svn), <a rel="nofollow" href="http://subversion.apache.org/">http://subversion.apache.org/</a></dd></dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> cvs2git</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://cvs2svn.tigris.org/cvs2git.html">http://cvs2svn.tigris.org/cvs2git.html</a></dd></dl>
<dt> 2.</dt>
<dd> parsecvs</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="https://github.com/BartMassey/parsecvs">https://github.com/BartMassey/parsecvs</a></dd></dl>
</dl>
