---

title: "vcstools(1)"
name: "vcstools"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcstools/"
description: "vcstools – vcstools Documentation"
---

<p> vcstools &#8211; vcstools Documentation </p>
<p> The <code>vcstools</code> module provides a Python API for interacting with different version control systems (VCS/SCMs). The <code>VcsClient</code> class provides an API for seamless interacting with Git, Mercurial (Hg), Bzr and SVN. The focus of the API is manipulating on-disk checkouts of source-controlled trees. Its main use is to support the <i>rosinstall</i> tool.</p>
<h2>GENERAL VCS/SCM API</h2>
<p> The <code>VcsClient</code> class provides a generic API for</p>
<dl>
<dt>&bull;</dt>
<dd> Subversion (<code>svn</code>)</dd>
<dt>&bull;</dt>
<dd> Mercurial (<code>hg</code>)</dd>
<dt>&bull;</dt>
<dd> Git (<code>git</code>)</dd>
<dt>&bull;</dt>
<dd> Bazaar (<code>bzr</code>)</dd>
<dt><code>class vcstools.VcsClient(vcs_type, path)</code></dt>
<dd> API for interacting with source-controlled paths independent of actual version-control implementation.</dd>
<dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>vcs_type</code> &#8212; type of VCS to use (e.g. &#8216;svn&#8217;, &#8216;hg&#8217;, &#8216;bzr&#8217;, &#8216;git&#8217;), <code>str</code></dd>
<dt>&bull;</dt>
<dd> <code>path</code> &#8212; filesystem path where code is/will be checked out , <code>str</code></dd>
<dt><code>path_exists() -&gt; bool</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> True if path exists on disk.</dd>
<dt><code>get_path() -&gt; str</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> filesystem path this client is initialized with.</dd>
<dt><code>url_matches(self, url, url_or_shortcut) -&gt; bool</code></dt>
<dd> client can decide whether the url and the other url are equivalent. Checks string equality by default</dd>
<dt><code>Parameters</code></dt>
<dd> <code>url_or_shortcut</code> &#8212; url or shortcut (e.g. bzr launchpad url)</dd>
<dt><code>Returns</code></dt>
<dd> bool if params are equivalent</dd>
<dt><code>get_version([spec=None]) -&gt; str</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd> <code>spec</code> &#8212; </dd>
<p> token for identifying repository revision desired. Token might be a tagname, branchname, version-id, or SHA-ID depending on the VCS implementation.</p>
<dt>&bull;</dt>
<dd> svn: anything accepted by <code>svn info &#8211;help</code>, e.g. a <code>revnumber</code>, <code>{date}</code>, <code>HEAD</code>, <code>BASE</code>, <code>PREV</code>, or <code>COMMITTED</code></dd>
<dt>&bull;</dt>
<dd> git: anything accepted by <code>git log</code>, e.g. a tagname, branchname, or sha-id.</dd>
<dt>&bull;</dt>
<dd> hg: anything accepted by <code>hg log -r</code>, e.g. a tagname, sha-ID, revision-number</dd>
<dt>&bull;</dt>
<dd> bzr: revisionspec as returned by <code>bzr help revisionspec</code>, e.g. a tagname or <code>revno:&lt;number&gt;</code> </dd>
<dt><code>Returns</code></dt>
<dd> current revision number of the repository. Or if spec is provided, the globally unique identifier (e.g. revision number, or SHA-ID) of a revision specified by some token.</dd>
<dt><code>get_remote_version(self, fatch=False) -&gt; str</code></dt>
<dd> Find an identifier for the current revision on remote. Token spec might be a tagname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</dd>
<dt><code>Parameters</code></dt>
<dd> <code>fetch</code> &#8212; if False, only local information may be used</dd>
<dt><code>Returns</code></dt>
<dd> current revision number of the remote repository.</dd>
<dt><code>get_current_version_label() -&gt; str</code></dt>
<dd> Find an description for the current local version. Token spec might be a branchname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</dd>
<dt><code>returns</code></dt>
<dd> short description of local version (e.g. branchname, tagename).</dd>
<dt><code>checkout(url[, version=&#8221;][, verbose=False][, shallow=False])</code></dt>
<dd> Checkout the given URL to the path associated with this client.</dd>
<dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>url</code> &#8212; URL of source control to check out</dd>
<dt>&bull;</dt>
<dd> <code>version</code> &#8212; specific version to check out</dd>
<dt>&bull;</dt>
<dd> <code>verbose</code> &#8212; flag to run verbosely</dd>
<dt>&bull;</dt>
<dd> <code>shallow</code> &#8212; flag to create shallow clone without history</dd>
<dt><code>update(version)</code></dt>
<dd> Update the local checkout from upstream source control.</dd>
<dt><code>detect_presence() -&gt; bool</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> True if path has a checkout with matching VCS type, e.g. if the type of this client is &#8216;svn&#8217;, the checkout at the path is managed by Subversion.</dd>
<dt><code>get_vcs_type_name() -&gt; str</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> type of VCS this client is initialized with.</dd>
<dt><code>get_url() -&gt; str</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> Upstream URL that this code was checked out from.</dd>
<dt><code>get_branch_parent()</code></dt>
<dd> (Git Only)</dd>
<dt><code>Returns</code></dt>
<dd> parent branch.</dd>
<dt><code>get_diff([basepath=None])</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd> <code>basepath</code> &#8212; compute diff relative to this path, if provided</dd>
<dt><code>Returns</code></dt>
<dd> A string showing local differences</dd>
<dt><code>get_status([basepath=None[, untracked=False]])</code></dt>
<dd> Calls scm status command. semantics of untracked are difficult to generalize. In SVN, this would be new files only. In git, hg, bzr, this would be changes that have not been added for commit.</dd>
<dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>basepath</code> &#8212; status path will be relative to this, if provided.</dd>
<dt>&bull;</dt>
<dd> <code>untracked</code> &#8212; If True, also show changes that would not commit</dd>
<dt><code>Returns</code></dt>
<dd> A string summarizing locally modified files </dd>
<p> Example: </p>
<pre>
import vcstools
# interrogate an existing tree
client = vcstools.VcsClient('svn', '/path/to/checkout')
print client.get_url()
print client.get_version()
print client.get_diff()
# create a new tree
client = vcstools.VcsClient('hg', '/path/to/new/checkout')
client.checkout('<a rel="nofollow" href="https://bitbucket.org/foo/bar')">https://bitbucket.org/foo/bar')</a>
</pre>
<p> vcstools is available on pypi and can be installed via <code>pip</code> </p>
<pre>
pip install vcstools
</pre>
<p> or <code>easy_install</code>: </p>
<pre>
easy_install vcstools
</pre>
<p> The <code>vcstools</code> module is meant to be used as a normal Python module. After it has been installed, you can <code>import</code> it normally and do not need to declare as a ROS package dependency.</dl>
<h2>DEVELOPER&#8217;S GUIDE</h2>
<h3>Code API</h3>
<h3>Packages</h3>
<h3>vcstools Package</h3>
<h3><code>vcstools</code> Package</h3>
<p> Library for tools that need to interact with ROS-support version control systems.</p>
<dl>
<dt><code>vcstools.setup_logger()</code></dt>
<dd> creates a logger &#8216;vcstools&#8217;</dd></dl>
<h3><code>bzr</code> Module</h3>
<p> bzr vcs support.</p>
<dl>
<dt><code>vcstools.bzr.BZRClient</code></dt>
<dd> alias of <code>BzrClient</code></dd>
<dt><code>class vcstools.bzr.BzrClient(path)</code></dt>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></dd>
<dt><code>__init__(path)</code></dt>
<dd>
</dd><dt><code>Raises </code></dt>
<dd> VcsError if bzr not detected</dd>
<dt><code>checkout(url, version=None, verbose=False, shallow=False, timeout=None)</code></dt>
<dd>
</dd><dt><code>export_repository(version, basepath)</code></dt>
<dd>
</dd><dt><code>get_branches(local_only=False)</code></dt>
<dd>
</dd><dt><code>get_current_version_label()</code></dt>
<dd>
</dd><dt><code>get_diff(basepath=None)</code></dt>
<dd>
</dd><dt><code>static get_environment_metadata()</code></dt>
<dd>
</dd><dt><code>get_log(relpath=None, limit=None)</code></dt>
<dd>
</dd><dt><code>get_remote_version(fetch=False)</code></dt>
<dd>
</dd><dt><code>get_status(basepath=None, untracked=False)</code></dt>
<dd>
</dd><dt><code>get_url()</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> BZR URL of the branch (output of bzr info command), </dd>
<p> or None if it cannot be determined</p>
<dt><code>get_version(spec=None)</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd> <code>spec</code> &#8212; (optional) revisionspec of desired version. May be any revisionspec as returned by &#8216;bzr help revisionspec&#8217;, e.g. a tagname or &#8216;revno:&lt;number&gt;&#8217;</dd>
<dt><code>Returns</code></dt>
<dd> the current revision number of the repository. Or if spec is provided, the number of a revision specified by some token.</dd>
<dt><code>static static_detect_presence(path)</code></dt>
<dd>
</dd><dt><code>update(version=u&#8221;, verbose=False, timeout=None)</code></dt>
<dd>
</dd><dt><code>url_matches(url, url_or_shortcut)</code></dt>
<dd>
</dd><dt><code>vcstools.bzr._get_bzr_version()</code></dt>
<dd> Looks up bzr version by calling bzr &#8211;version. :raises: VcsError if bzr is not installed</dd></dl>
<h3><code>git</code> Module</h3>
<p> git vcs support. </p>
<p> refnames in git can be branchnames, hashes, partial hashes, tags. On checkout, git will disambiguate by checking them in that order, taking the first that applies </p>
<p> This class aims to provide git for linear centralized workflows. This means in case of ambiguity, we assume that the only relevant remote is the one named &quot;origin&quot;, and we assume that commits once on origin remain on origin. </p>
<p> A challenge with git is that it has strong reasonable conventions, but is very allowing for breaking them. E.g. it is possible to name remotes and branches with names like &quot;refs/heads/master&quot;, give branches and tags the same name, or a valid SHA-ID as name, etc. Similarly git allows plenty of ways to reference any object, in case of ambiguities, git attempts to take the most reasonable disambiguation, and in some cases warns.</p>
<dl>
<dt><code>vcstools.git.GITClient</code></dt>
<dd> alias of <code>GitClient</code></dd>
<dt><code>class vcstools.git.GitClient(path)</code></dt>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></dd>
<dt><code>__init__(path)</code></dt>
<dd>
</dd><dt><code>Raises </code></dt>
<dd> VcsError if git not detected</dd>
<dt><code>_do_checkout(refname, fetch=True, verbose=False)</code></dt>
<dd> meaning git checkout, not vcstools checkout. This works for local branches, remote branches, tagnames, hashes, etc. git will create local branch of same name when no such local branch exists, and also setup tracking. Git decides with own rules whether local changes would cause conflicts, and refuses to checkout else.</dd>
<dt><code>Raises GitError</code></dt>
<dd> when checkout fails</dd>
<dt><code>_do_fast_forward(branch_parent, fetch=True, verbose=False)</code></dt>
<dd> Execute git fetch if necessary, and if we can fast-foward, do so to the last fetched version using git rebase.</dd>
<dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>branch_parent</code> &#8212; name of branch we track</dd>
<dt>&bull;</dt>
<dd> <code>fetch</code> &#8212; whether fetch should be done first for remote refs</dd>
<dt><code>Returns</code></dt>
<dd> True if up-to-date or after succesful fast-forward</dd>
<dt><code>Raises </code></dt>
<dd> GitError when git fetch fails</dd>
<dt><code>_do_fetch(timeout=None)</code></dt>
<dd> calls git fetch :raises: GitError when call fails</dd>
<dt><code>_do_update(refname=None, verbose=False, fast_foward=True, timeout=None, update_submodules=True)</code></dt>
<dd> updates without fetching, thus any necessary fetching must be done before allows arguments to reduce unnecessary steps after checkout</dd>
<dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>fast_foward</code> &#8212; if false, does not perform fast-forward</dd>
<dt>&bull;</dt>
<dd> <code>update_submodules</code> &#8212; if false, does not attempt to update submodules</dd>
<dt><code>_get_branch()</code></dt>
<dd>
</dd><dt><code>_get_branch_parent(fetch=False, current_branch=None)</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>fetch</code> &#8212; if true, performs git fetch first</dd>
<dt>&bull;</dt>
<dd> <code>current_branch</code> &#8212; if not None, this is used as current branch (else extra shell call)</dd>
<dt><code>Returns</code></dt>
<dd> (branch, remote) the name of the branch this branch tracks and its remote</dd>
<dt><code>Raises </code></dt>
<dd> GitError if fetch fails</dd>
<dt><code>_get_default_remote()</code></dt>
<dd> in order to support users who name their default origin something else than origin, read remote name.</dd>
<dt><code>_is_commit_in_orphaned_subtree(version, mask_self=False, fetch=True)</code></dt>
<dd> checks git log &#8211;all (the list of all commits reached by references, meaning branches or tags) for version. If it shows up, that means git garbage collection will not remove the commit. Else it would eventually be deleted.</dd>
<dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>version</code> &#8212; SHA IDs (if partial, caller is responsible for mismatch)</dd>
<dt>&bull;</dt>
<dd> <code>mask_self</code> &#8212; whether to consider direct references to this commit (rather than only references on descendants) as well</dd>
<dt>&bull;</dt>
<dd> <code>fetch</code> &#8212; whether fetch should be done first for remote refs</dd>
<dt><code>Returns</code></dt>
<dd> True if version is not recursively referenced by a branch or tag</dd>
<dt><code>Raises </code></dt>
<dd> GitError if git fetch fails</dd>
<dt><code>_is_local_branch(branch_name)</code></dt>
<dd>
</dd><dt><code>_is_remote_branch(branch_name, remote_name=None, fetch=True)</code></dt>
<dd> checks list of remote branches for match. Set fetch to False if you just fetched already.</dd>
<dt><code>Returns</code></dt>
<dd> True if branch_name exists for remote &lt;remote_name&gt; (or &#8216;origin&#8217; if None)</dd>
<dt><code>Raises </code></dt>
<dd> GitError when git fetch fails</dd>
<dt><code>_rev_list_contains(refname, version, fetch=True)</code></dt>
<dd> calls git rev-list with refname and returns True if version can be found in rev-list result</dd>
<dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>refname</code> &#8212; a git refname</dd>
<dt>&bull;</dt>
<dd> <code>version</code> &#8212; an SHA IDs (if partial, caller is responsible for mismatch)</dd>
<dt><code>Returns</code></dt>
<dd> True if version is an ancestor commit from refname</dd>
<dt><code>Raises </code></dt>
<dd> GitError when call to git fetch fails</dd>
<dt><code>_update_submodules(verbose=False, timeout=None)</code></dt>
<dd>
</dd><dt><code>checkout(url, version=None, verbose=False, shallow=False, timeout=None)</code></dt>
<dd> calls git clone and then, if version was given, update(version)</dd>
<dt><code>export_repository(version, basepath)</code></dt>
<dd>
</dd><dt><code>get_branches(local_only=False)</code></dt>
<dd>
</dd><dt><code>get_current_version_label()</code></dt>
<dd> For git we change the label to clarify when a different remote is configured.</dd>
<dt><code>get_default_remote_version_label()</code></dt>
<dd>
</dd><dt><code>get_diff(basepath=None)</code></dt>
<dd>
</dd><dt><code>static get_environment_metadata()</code></dt>
<dd>
</dd><dt><code>get_log(relpath=None, limit=None)</code></dt>
<dd>
</dd><dt><code>get_remote_version(fetch=False)</code></dt>
<dd>
</dd><dt><code>get_status(basepath=None, untracked=False)</code></dt>
<dd>
</dd><dt><code>get_url()</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> git URL of the directory path (output of git info command), or None if it cannot be determined</dd>
<dt><code>get_version(spec=None)</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>spec</code> &#8212; (optional) token to identify desired version. For git, this may be anything accepted by git log, e.g. a tagname, branchname, or sha-id.</dd>
<dt>&bull;</dt>
<dd> <code>fetch</code> &#8212; When spec is given, can be used to suppress git fetch call</dd>
<dt><code>Returns</code></dt>
<dd> current SHA-ID of the repository. Or if spec is provided, the SHA-ID of a commit specified by some token if found, else None</dd>
<dt><code>is_tag(tag_name, fetch=True)</code></dt>
<dd> checks list of tags for match. Set fetch to False if you just fetched already.</dd>
<dt><code>Returns</code></dt>
<dd> True if tag_name among known tags</dd>
<dt><code>Raises </code></dt>
<dd> GitError when call to git fetch fails</dd>
<dt><code>static static_detect_presence(path)</code></dt>
<dd>
</dd><dt><code>update(version=None, verbose=False, force_fetch=False, timeout=None)</code></dt>
<dd> if version is None, attempts fast-forwarding current branch, if any. </dd>
<p> Else interprets version as a local branch, remote branch, tagname, hash, etc. </p>
<p> If it is a branch, attempts to move to it unless already on it, and to fast-forward, unless not a tracking branch. Else go untracked on tag or whatever version is. Does not leave if current commit would become dangling.</p>
<dt><code>Returns</code></dt>
<dd> True if already up-to-date with remote or after successful fast_foward</dd>
<dt><code>exception vcstools.git.GitError</code></dt>
<dd> Bases: <code>exceptions.Exception</code></dd>
<dt><code>vcstools.git._get_git_version()</code></dt>
<dd> Looks up git version by calling git &#8211;version.</dd>
<dt><code>Raises </code></dt>
<dd> VcsError if git is not installed or returns </dd>
<p> something unexpected</p>
<dt><code>vcstools.git._git_diff_path_submodule_change(diff, rel_path_prefix)</code></dt>
<dd> Parses git diff result and changes the filename prefixes.</dd></dl>
<h3><code>hg</code> Module</h3>
<p> hg vcs support. </p>
<p> using ui object to redirect output into a string</p>
<dl>
<dt><code>vcstools.hg.HGClient</code></dt>
<dd> alias of <code>HgClient</code></dd>
<dt><code>class vcstools.hg.HgClient(path)</code></dt>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></dd>
<dt><code>__init__(path)</code></dt>
<dd>
</dd><dt><code>Raises </code></dt>
<dd> VcsError if hg not detected</dd>
<dt><code>_do_pull(filter=False)</code></dt>
<dd>
</dd><dt><code>checkout(url, version=u&#8221;, verbose=False, shallow=False, timeout=None)</code></dt>
<dd>
</dd><dt><code>export_repository(version, basepath)</code></dt>
<dd>
</dd><dt><code>get_branch()</code></dt>
<dd>
</dd><dt><code>get_branches(local_only=False)</code></dt>
<dd>
</dd><dt><code>get_current_version_label()</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd> <code>spec</code> &#8212; (optional) spec can be what &#8216;svn info &#8211;help&#8217; allows, meaning a revnumber, {date}, HEAD, BASE, PREV, or COMMITTED.</dd>
<dt><code>Returns</code></dt>
<dd> current revision number of the repository. Or if spec provided, the number of a revision specified by some token.</dd>
<dt><code>get_diff(basepath=None)</code></dt>
<dd>
</dd><dt><code>static get_environment_metadata()</code></dt>
<dd>
</dd><dt><code>get_log(relpath=None, limit=None)</code></dt>
<dd>
</dd><dt><code>get_remote_version(fetch=False)</code></dt>
<dd>
</dd><dt><code>get_status(basepath=None, untracked=False)</code></dt>
<dd>
</dd><dt><code>get_url()</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> HG URL of the directory path. (output of hg paths </dd>
<p> command), or None if it cannot be determined</p>
<dt><code>get_version(spec=None)</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd> <code>spec</code> &#8212; (optional) token for identifying version. spec can be a whatever is allowed by &#8216;hg log -r&#8217;, e.g. a tagname, sha-ID, revision-number</dd>
<dt><code>Returns</code></dt>
<dd> the current SHA-ID of the repository. Or if spec is provided, the SHA-ID of a revision specified by some token.</dd>
<dt><code>static static_detect_presence(path)</code></dt>
<dd>
</dd><dt><code>update(version=u&#8221;, verbose=False, timeout=None)</code></dt>
<dd>
</dd><dt><code>vcstools.hg._get_hg_version()</code></dt>
<dd> Looks up hg version by calling hg &#8211;version. :raises: VcsError if hg is not installed</dd>
<dt><code>vcstools.hg._hg_diff_path_change(diff, path)</code></dt>
<dd> Parses hg diff result and changes the filename prefixes.</dd></dl>
<h3><code>svn</code> Module</h3>
<p> svn vcs support.</p>
<dl>
<dt><code>vcstools.svn.SVNClient</code></dt>
<dd> alias of <code>SvnClient</code></dd>
<dt><code>class vcstools.svn.SvnClient(path)</code></dt>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></dd>
<dt><code>__init__(path)</code></dt>
<dd>
</dd><dt><code>Raises </code></dt>
<dd> VcsError if python-svn not detected</dd>
<dt><code>_get_version_from_path(spec=None, path=None)</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>spec</code> &#8212; (optional) spec can be what &#8216;svn info &#8211;help&#8217; allows, meaning a revnumber, {date}, HEAD, BASE, PREV, or COMMITTED.</dd>
<dt>&bull;</dt>
<dd> <code>path</code> &#8212; the url to use, default is for this repo</dd>
<dt><code>Returns</code></dt>
<dd> current revision number of the repository. Or if spec provided, the number of a revision specified by some token.</dd>
<dt><code>checkout(url, version=u&#8221;, verbose=False, shallow=False, timeout=None)</code></dt>
<dd>
</dd><dt><code>export_repository(version, basepath)</code></dt>
<dd>
</dd><dt><code>get_branches(local_only=False)</code></dt>
<dd>
</dd><dt><code>get_current_version_label()</code></dt>
<dd>
</dd><dt><code>get_diff(basepath=None)</code></dt>
<dd>
</dd><dt><code>static get_environment_metadata()</code></dt>
<dd>
</dd><dt><code>get_log(relpath=None, limit=None)</code></dt>
<dd>
</dd><dt><code>get_remote_version(fetch=False)</code></dt>
<dd>
</dd><dt><code>get_status(basepath=None, untracked=False)</code></dt>
<dd>
</dd><dt><code>get_url()</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> SVN URL of the directory path (output of svn info command), </dd>
<p> or None if it cannot be determined</p>
<dt><code>get_version(spec=None)</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>spec</code> &#8212; (optional) spec can be what &#8216;svn info &#8211;help&#8217; allows, meaning a revnumber, {date}, HEAD, BASE, PREV, or COMMITTED.</dd>
<dt>&bull;</dt>
<dd> <code>path</code> &#8212; the url to use, default is for this repo</dd>
<dt><code>Returns</code></dt>
<dd> current revision number of the repository. Or if spec provided, the number of a revision specified by some token.</dd>
<dt><code>static static_detect_presence(path)</code></dt>
<dd>
</dd><dt><code>update(version=None, verbose=False, timeout=None)</code></dt>
<dd>
</dd><dt><code>vcstools.svn._get_svn_version()</code></dt>
<dd> Looks up svn version by calling svn &#8211;version. :raises: VcsError if svn is not installed</dd>
<dt><code>vcstools.svn.canonical_svn_url_split(url)</code></dt>
<dd> checks url for traces of canonical svn structure, and return root, type, name (of tag or branch), subfolder, query and fragment (see urllib urlparse) This should allow creating a different url for switching to a different tag or branch</dd>
<dt><code>Parameters</code></dt>
<dd> <code>url</code> &#8212; location of central repo, <code>str</code></dd>
<dt><code>Returns</code></dt>
<dd> dict {root, type, name, subfolder, query, fragment} </dd>
<p> with type one of &quot;trunk&quot;, &quot;tags&quot;, &quot;branches&quot;</p>
<dt><code>vcstools.svn.get_remote_contents(url)</code></dt>
<dd></dd></dl>
<h3><code>tar</code> Module</h3>
<p> tar vcs support. </p>
<p> The implementation uses the &quot;version&quot; argument to indicate a subfolder within a tarfile. Hence one can organize sources by creating one tarfile with a folder inside for each version.</p>
<dl>
<dt><code>vcstools.tar.TARClient</code></dt>
<dd> alias of <code>TarClient</code></dd>
<dt><code>class vcstools.tar.TarClient(path)</code></dt>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></dd>
<dt><code>__init__(path)</code></dt>
<dd> @raise VcsError if tar not detected</dd>
<dt><code>checkout(url, version=u&#8221;, verbose=False, shallow=False, timeout=None)</code></dt>
<dd> untars tar at url to self.path. If version was given, only the subdirectory &#8216;version&#8217; of the tar will end up in self.path. Also creates a file next to the checkout named </dd>
<pre>
*
</pre>
<p> .tar which is a yaml file listing origin url and version arguments.</p>
<dt><code>export_repository(version, basepath)</code></dt>
<dd>
</dd><dt><code>get_current_version_label()</code></dt>
<dd>
</dd><dt><code>get_diff(basepath=None)</code></dt>
<dd>
</dd><dt><code>static get_environment_metadata()</code></dt>
<dd>
</dd><dt><code>get_remote_version(fetch=False)</code></dt>
<dd>
</dd><dt><code>get_status(basepath=None, untracked=False)</code></dt>
<dd>
</dd><dt><code>get_url()</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> TAR URL of the directory path (output of tar info </dd>
<p> command), or None if it cannot be determined</p>
<dt><code>get_version(spec=None)</code></dt>
<dd>
</dd><dt><code>static static_detect_presence(path)</code></dt>
<dd>
</dd><dt><code>update(version=u&#8221;, verbose=False, timeout=None)</code></dt>
<dd> Does nothing except returning true if tar exists in same &quot;version&quot; as checked out with vcstools.</dd></dl>
<h3><code>vcs_abstraction</code> Module</h3>
<dl>
<dt><code>undoc-members</code></dt>
<dd>
</dd><dt><code>show-inheritance</code></dt>
<dd>
</dd><dt><code>vcstools.vcs_abstraction.VCSClient</code></dt>
<dd> alias of <code>VcsClient</code></dd>
<dt><code>class vcstools.vcs_abstraction.VcsClient(vcs_type, path)</code></dt>
<dd> Bases: <code>object</code> </dd>
<p> <i>DEPRECATED</i> API for interacting with source-controlled paths independent of actual version-control implementation.</p>
<dt><code>vcstools.vcs_abstraction.get_registered_vcs_types()</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> list of valid key to use as vcs_type</dd>
<dt><code>vcstools.vcs_abstraction.get_vcs(vcs_type)</code></dt>
<dd> Returns the class interfacing with vcs of given type</dd>
<dt><code>Parameters</code></dt>
<dd> <code>vcs_type</code> &#8212; id of the tpye, e.g. git, svn, hg, bzr</dd>
<dt><code>Returns</code></dt>
<dd> class extending VcsClientBase</dd>
<dt><code>Raises </code></dt>
<dd> ValueError for unknown vcs_type</dd>
<dt><code>vcstools.vcs_abstraction.get_vcs_client(vcs_type, path)</code></dt>
<dd> Returns a client with which to interact with the vcs at given path</dd>
<dt><code>Parameters</code></dt>
<dd> <code>vcs_type</code> &#8212; id of the tpye, e.g. git, svn, hg, bzr</dd>
<dt><code>Returns</code></dt>
<dd> instance of VcsClientBase</dd>
<dt><code>Raises </code></dt>
<dd> ValueError for unknown vcs_type</dd>
<dt><code>vcstools.vcs_abstraction.register_vcs(vcs_type, clazz)</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>vcs_type</code> &#8212; id, <code>str</code></dd>
<dt>&bull;</dt>
<dd> <code>clazz</code> &#8212; class extending VcsClientBase</dd></dl>
<h3><code>vcs_base</code> Module</h3>
<p> vcs support library base class.</p>
<dl>
<dt><code>undoc-members</code></dt>
<dd>
</dd><dt><code>show-inheritance</code></dt>
<dd>
</dd><dt><code>class vcstools.vcs_base.VcsClientBase(vcs_type_name, path)</code></dt>
<dd> Bases: <code>object</code> </dd>
<p> parent class for all vcs clients, provides their public API</p>
<dt><code>__init__(vcs_type_name, path)</code></dt>
<dd> subclasses may raise VcsError when a dependency is missing</dd>
<dt><code>checkout(url, version=None, verbose=False, shallow=False, timeout=None)</code></dt>
<dd> Attempts to create a local repository given a remote url. Fails if a target path exists, unless it&#8217;s an empty directory. If a version is provided, the local repository will be updated to that revision. It is possible that after a failed call to checkout, a repository still exists, e.g. if an invalid revision was given. If shallow is provided, the scm client may checkout less than the full repository history to save time / disk space. If a timeout is specified, any pending operation will fail after the specified amount (in seconds). NOTE: this parameter might or might not be honored, depending on VCS client implementation. :param url: where to checkout from :type url: str :param version: token for identifying repository revision :type version: str :param shallow: hint to checkout less than a full repository :type shallow: bool :param timeout: maximum allocated time to perform operation :type shallow: int :returns: True if successful</dd>
<dt><code>detect_presence()</code></dt>
<dd> For auto detection</dd>
<dt><code>export_repository(version, basepath)</code></dt>
<dd> Calls scm equivalent to <i>svn export</i>, removing scm meta information and tar gzip&#8217;ing the repository at a given version to the given basepath.</dd>
<dt><code>Parameters</code></dt>
<dd> <code>version</code> &#8212; version of the repository to export. This can </dd>
<p> be a branch, tag, or path (svn). When specifying the version as a path for svn, the path should be relative to the root of the svn repository, i.e. &#8216;trunk&#8217;, or &#8216;tags/1.2.3&#8217;, or &#8216;./&#8217; for the root. :param basepath: this is the path to the tar gzip, excluding the extension which will be .tar.gz :returns: True on success, False otherwise.</p>
<dt><code>get_branches(local_only=False)</code></dt>
<dd> Returns a list of all branches in the vcs repository.</dd>
<dt><code>Parameters</code></dt>
<dd> <code>local_only</code> &#8212; if True it will only list local branches</dd>
<dt><code>Returns</code></dt>
<dd> list of branches in the repository, [] if none exist</dd>
<dt><code>get_current_version_label()</code></dt>
<dd> Find an description for the current local version. Token spec might be a branchname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</dd>
<dt><code>Returns</code></dt>
<dd> short description of local version (e.g. branchname, tagename).</dd>
<dt><code>Return type</code></dt>
<dd> str</dd>
<dt><code>get_default_remote_version_label()</code></dt>
<dd> Find a label for the default branch on remote, meaning the one that would be checked out on a clean checkout.</dd>
<dt><code>Returns</code></dt>
<dd> a label or None (if not applicable)</dd>
<dt><code>Return type</code></dt>
<dd> str</dd>
<dt><code>get_diff(basepath=None)</code></dt>
<dd>
</dd><dt><code>Parameters</code></dt>
<dd> <code>basepath</code> &#8212; diff paths will be relative to this, if any</dd>
<dt><code>Returns</code></dt>
<dd> A string showing local differences</dd>
<dt><code>Return type</code></dt>
<dd> str</dd>
<dt><code>static get_environment_metadata()</code></dt>
<dd> For debugging purposes, returns a dict containing information about the environment, like the version of the SCM client, or version of libraries involved. Suggest considering keywords &quot;version&quot;, &quot;dependency&quot;, &quot;features&quot; first. :returns: a dict containing relevant information :rtype: dict</dd>
<dt><code>get_log(relpath=None, limit=None)</code></dt>
<dd> Calls scm log command.</dd>
<dt><code>This returns a list of dictionaries with the following fields:</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> id: the commit SHA or revision number</dd>
<dt>&bull;</dt>
<dd> date: the date the commit was made (python datetime)</dd>
<dt>&bull;</dt>
<dd> author: the name of the author of the commit, if available</dd>
<dt>&bull;</dt>
<dd> email: the e-mail address of the author of the commit</dd>
<dt>&bull;</dt>
<dd> message: the commit message, if any</dd>
<dt><code>Parameters</code></dt>
<dd> <code>relpath</code> &#8212; (optional) restrict logs to events on this </dd>
<p> resource path (folder or file) relative to the root of the repository. If None (default), this is the root of the repository. :param limit: (optional) the maximum number of log entries that should be retrieved. If None (default), there is no limit.</p>
<dt><code>get_path()</code></dt>
<dd> returns the path this client was configured for</dd>
<dt><code>get_remote_version(fetch=False)</code></dt>
<dd> Find an identifier for the current revision on remote. Token spec might be a tagname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</dd>
<dt><code>Parameters</code></dt>
<dd> <code>fetch</code> &#8212; if False, only local information may be used</dd>
<dt><code>Returns</code></dt>
<dd> current revision number of the remote repository.</dd>
<dt><code>Return type</code></dt>
<dd> str</dd>
<dt><code>get_status(basepath=None, untracked=False)</code></dt>
<dd> Calls scm status command. Output must be terminated by newline unless empty. </dd>
<p> Semantics of untracked are difficult to generalize. In SVN, this would be new files only. In git, hg, bzr, this would be changes that have not been added for commit.</p>
<dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>basepath</code> &#8212; status path will be relative to this, if any</dd>
<dt>&bull;</dt>
<dd> <code>untracked</code> &#8212; whether to also show changes that would not commit</dd>
<dt><code>Returns</code></dt>
<dd> A string summarizing locally modified files</dd>
<dt><code>Return type</code></dt>
<dd> str</dd>
<dt><code>get_url()</code></dt>
<dd>
</dd><dt><code>Returns</code></dt>
<dd> The source control url for the path or None if not set</dd>
<dt><code>Return type</code></dt>
<dd> str</dd>
<dt><code>get_vcs_type_name()</code></dt>
<dd> used when auto detected</dd>
<dt><code>get_version(spec=None)</code></dt>
<dd> Find an identifier for a the current or a specified revision. Token spec might be a tagname, branchname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</dd>
<dt><code>Parameters</code></dt>
<dd> <code>spec</code> (<i>str</i>) &#8212; token for identifying repository revision</dd>
<dt><code>Returns</code></dt>
<dd> current revision number of the repository. Or if spec is provided, the respective revision number.</dd>
<dt><code>Return type</code></dt>
<dd> str</dd>
<dt><code>path_exists()</code></dt>
<dd> helper function</dd>
<dt><code>static static_detect_presence(path)</code></dt>
<dd> For auto detection</dd>
<dt><code>update(version=None, verbose=False, timeout=None)</code></dt>
<dd> Sets the local copy of the repository to a version matching the version parameter. Fails when there are uncommited changes. On failures (also e.g. network failure) grants the checked out files are in the same state as before the call. If a timeout is specified, any pending operation will fail after the specified amount (in seconds)</dd>
<dt><code>Parameters</code></dt>
<dd>
</dd><dt>&bull;</dt>
<dd> <code>version</code> &#8212; token for identifying repository revision desired. Token might be a tagname, branchname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</dd>
<dt>&bull;</dt>
<dd> <code>timeout</code> &#8212; maximum allocated time to perform operation</dd>
<dt><code>Returns</code></dt>
<dd> True on success, False else</dd>
<dt><code>url_matches(url, url_or_shortcut)</code></dt>
<dd> client can decide whether the url and the other url are equivalent. Checks string equality by default :param url_or_shortcut: url or shortcut (e.g. bzr launchpad url) :returns: bool if params are equivalent</dd>
<dt><code>exception vcstools.vcs_base.VcsError(value)</code></dt>
<dd> Bases: <code>exceptions.Exception</code> </dd>
<p> To be thrown when an SCM Client faces a situation because of a violated assumption</dl>
<h3>Changelog</h3>
<h3>Changelog</h3>
<h3>0.1</h3>
<h3>0.1.38</h3>
<dl>
<dt>&bull;</dt>
<dd> Fixed test failures due to SVN 1.9.</dd>
<dt>&bull;</dt>
<dd> Added the <code>get_default_remote_version_label()</code> API method to support changes in <code>wstool</code>.</dd>
<dt>&bull;</dt>
<dd> Renamed some internal functions to have a leading <code>_</code> to indicate that they are private.</dd></dl>
<h3>0.1.37</h3>
<dl>
<dt>&bull;</dt>
<dd> Fix an issue where log were restricted to the named branch (hg).</dd>
<dt>&bull;</dt>
<dd> Fixed svn to use a global revision number rather than a branch-local revision.</dd>
<dt>&bull;</dt>
<dd> Added the get_remote_version() and get_current_version_label() API calls.</dd>
<dt>&bull;</dt>
<dd> Enhanced use of <code>no_warn</code> in run_shell_command().</dd>
<dt>&bull;</dt>
<dd> Fix get_version() to catch stderr.</dd>
<dt>&bull;</dt>
<dd> Added get_branches() API call.</dd>
<dt>&bull;</dt>
<dd> Fix some errors and warnings to output to stderr.</dd>
<dt>&bull;</dt>
<dd> Fix output to avoid extra newlines when show_stdout=True.</dd></dl>
<h3>0.1.36</h3>
<dl>
<dt>&bull;</dt>
<dd> Updates to the release platforms (-lucid +utopic +vivid)</dd>
<dt>&bull;</dt>
<dd> Fix an issue with updating branches on git, see vcstools/wstool#25</dd></dl>
<h3>0.1.31</h3>
<dl>
<dt>&bull;</dt>
<dd> Fix submodule support on checkout #71</dd></dl>
<h3>0.1.30</h3>
<dl>
<dt>&bull;</dt>
<dd> use netrc to download tars from private repos, also will work for private rosinstall files</dd>
<dt>&bull;</dt>
<dd> Fix checks for empty repository #62</dd></dl>
<h3>0.1.29</h3>
<dl>
<dt>&bull;</dt>
<dd> fix #57 shallow checkout of non-master breaks with git &gt;= 1.8.0</dd>
<dt>&bull;</dt>
<dd> unit test fixes</dd></dl>
<h3>0.1.28</h3>
<dl>
<dt>&bull;</dt>
<dd> test of new upload method</dd></dl>
<h3>0.1.27</h3>
<dl>
<dt>&bull;</dt>
<dd> fix #51 hg status and diff dont work if workspace is inside hg repo</dd>
<dt>&bull;</dt>
<dd> fix #47 several performance improvements by removing unecessary update actions after checkout</dd>
<dt>&bull;</dt>
<dd> fix #46 https tar download fails behind proxy</dd>
<dt>&bull;</dt>
<dd> fix #45 sometimes commands run forever</dd>
<dt>&bull;</dt>
<dd> fix #44 minor bug when checking out from repo with default branch not master</dd>
<dt>&bull;</dt>
<dd> fix #41 improvedAPI, get_vcs_client function part of vcstools module</dd></dl>
<h3>0.1.26</h3>
<dl>
<dt>&bull;</dt>
<dd> fix #38 git commands fail in local repositories with many (&gt;2000) references</dd>
<dt>&bull;</dt>
<dd> fix #31 get_log() svn xml not available on Ubuntu Lucid (hg 1.4.2)</dd>
<dt>&bull;</dt>
<dd> fix #37 update() returns True even when fetch failed</dd></dl>
<h3>0.1.25</h3>
<dl>
<dt>&bull;</dt>
<dd> minor bugfixes</dd>
<dt>&bull;</dt>
<dd> travis-ci config file</dd>
<dt>&bull;</dt>
<dd> fix unit tests for svn diff&amp;status ordering changes</dd>
<dt>&bull;</dt>
<dd> deprecated VcsClient Class</dd>
<dt>&bull;</dt>
<dd> added get_log function</dd></dl>
<h3>0.1.24</h3>
<dl>
<dt>&bull;</dt>
<dd> fix git update return value to False when fast-forward not possible due to diverge</dd>
<dt>&bull;</dt>
<dd> fix. svn certificate prompt invisible, svn checkout and update become verbose due to this</dd></dl>
<h3>0.1.22</h3>
<dl>
<dt>&bull;</dt>
<dd> Changed the way that git implements detect_presence to fix a bug with submodules in newer versions of git</dd>
<dt>&bull;</dt>
<dd> fix for git single quotes on Windows</dd>
<dt>&bull;</dt>
<dd> minor internal api bug where a git function always returned True</dd>
<dt>&bull;</dt>
<dd> fix gub in svn export_repository</dd></dl>
<h3>0.1.21</h3>
<dl>
<dt>&bull;</dt>
<dd> bugfix #66: hg http username prompt hidden</dd>
<dt>&bull;</dt>
<dd> add export_repository method to vcs_base and all implementations with tests</dd>
<dt>&bull;</dt>
<dd> bugfix #64: unicode decoding problems</dd></dl>
<h3>0.1.20</h3>
<dl>
<dt>&bull;</dt>
<dd> rosws update &#8211;verbose for git prints small message when rebasing</dd>
<dt>&bull;</dt>
<dd> improved python3 compatibility</dd></dl>
<h3>0.1.19</h3>
<dl>
<dt>&bull;</dt>
<dd> more python3 compatibility</dd>
<dt>&bull;</dt>
<dd> code style improved</dd>
<dt>&bull;</dt>
<dd> match_url to compare bzr shortcuts to real urls</dd>
<dt>&bull;</dt>
<dd> more unit tests</dd>
<dt>&bull;</dt>
<dd> get_status required to end with newline, to fix #55</dd></dl>
<h3>0.1.18</h3>
<dl>
<dt>&bull;</dt>
<dd> added shallow flag to API, implemented for git</dd></dl>
<h3>0.1.17</h3>
<dl>
<dt>&bull;</dt>
<dd> svn stdout output on get_version removed</dd></dl>
<h3>0.1.16</h3>
<dl>
<dt>&bull;</dt>
<dd> All SCMs show some output when update caused changes</dd>
<dt>&bull;</dt>
<dd> All SCMs have verbose option to show all changes done on update</dd>
<dt>&bull;</dt>
<dd> bugfix for bazaar getUrl() being a joined abspath</dd>
<dt>&bull;</dt>
<dd> bugfix for not all output being shown when requested</dd></dl>
<h3>0.1.15</h3>
<dl>
<dt>&bull;</dt>
<dd> Added pyyaml as a proper dependency, removed detection code.</dd>
<dt>&bull;</dt>
<dd> remove use of tar entirely, switch to tarfile module</dd>
<dt>&bull;</dt>
<dd> fix #36 allowing for tar being bsdtar on OSX</dd></dl>
<h3>0.1.14</h3>
<dl>
<dt>&bull;</dt>
<dd> Added tarball uncompression.</dd></dl>
<h3>0.1.13</h3>
<dl>
<dt>&bull;</dt>
<dd> added this changelog</dd>
<dt>&bull;</dt>
<dd> git get-version fetches only when local lookup fails</dd>
<dt>&bull;</dt>
<dd> hg get-version pulls if label not found</dd>
<dt>&bull;</dt>
<dd> Popen error message incudes cwd path</dd></dl>
<h3>0.1.12</h3>
<dl>
<dt>&bull;</dt>
<dd> py_checker clean after all refactorings since 0.1.0</dd></dl>
<h3>0.1.11</h3>
<dl>
<dt>&bull;</dt>
<dd> svn and hg update without user interaction</dd>
<dt>&bull;</dt>
<dd> bugfix #30</dd>
<dt>&bull;</dt>
<dd> minor bugfixes</dd></dl>
<h3>0.1.10</h3>
<dl>
<dt>&bull;</dt>
<dd> minor bugs</dd></dl>
<h3>0.1.9</h3>
<dl>
<dt>&bull;</dt>
<dd> safer sanitization of shell params</dd>
<dt>&bull;</dt>
<dd> git diff and stat recurse for submodules</dd>
<dt>&bull;</dt>
<dd> base class manages all calls to Popen</dd></dl>
<h3>0.1.8</h3>
<dl>
<dt>&bull;</dt>
<dd> several bugfixes</dd>
<dt>&bull;</dt>
<dd> reverted using shell commands instead of bazaar API</dd></dl>
<h3>0.1.7</h3>
<dl>
<dt>&bull;</dt>
<dd> reverted using shell commands instaed of pysvn and mercurial APIs</dd>
<dt>&bull;</dt>
<dd> protection against shell incection attempts</dd></dl>
<h3>0.1.6</h3>
<dl>
<dt>&bull;</dt>
<dd> bugfixes to svn and bzr</dd>
<dt>&bull;</dt>
<dd> unified all calls through Popen</dd></dl>
<h3>0.1.5</h3>
<dl>
<dt>&bull;</dt>
<dd> missing dependency to dateutil added</dd></dl>
<h3>0.1.4</h3>
<p> switched shell calls to calls to python API of mercurial, bazaar, py-svn</p>
<h3>0.1.3</h3>
<dl>
<dt>&bull;</dt>
<dd> fix #6</dd></dl>
<h3>0.1.2</h3>
<dl>
<dt>&bull;</dt>
<dd> fix #15</dd></dl>
<h3>0.1.1</h3>
<dl>
<dt>&bull;</dt>
<dd> more unit tests</dd>
<dt>&bull;</dt>
<dd> diverse bugfixes</dd>
<dt>&bull;</dt>
<dd> major change to git client behavior, based around git <i><a rel="nofollow" href="https://kforge.ros.org/vcstools/trac/ticket/1">https://kforge.ros.org/vcstools/trac/ticket/1</a></i></dd></dl>
<h3>0.1.0</h3>
<dl>
<dt>&bull;</dt>
<dd> documentation fixes</dd></dl>
<h3>0.0.3</h3>
<dl>
<dt>&bull;</dt>
<dd> import from svn</dd></dl>
<h3>Bug reports and feature requests</h3>
<dl>
<dt>&bull;</dt>
<dd> <i>Submit a bug report</i></dd></dl>
<h3>Developer Setup</h3>
<p> vcstools uses <i>setuptools</i>, which you will need to download and install in order to run the packaging. We use setuptools instead of distutils in order to be able use <code>setup()</code> keys like <code>install_requires</code>. cd vcstools python setup.py develop</p>
<h3>Testing</h3>
<p> Install test dependencies </p>
<pre>
pip install nose
pip install mock
</pre>
<p> vcstools uses <i>Python nose</i> for testing, which is a fairly simple and straightfoward test framework. The vcstools mainly use <code>unittest</code> to construct test fixtures, but with nose you can also just write a function that starts with the name <code>test</code> and use normal <code>assert</code> statements. </p>
<p> vcstools also uses <i>mock</i> to create mocks for testing. </p>
<p> You can run the tests, including coverage, as follows: </p>
<pre>
cd vcstools
make test
</pre>
<h3>Documentation</h3>
<p> Sphinx is used to provide API documentation for vcstools. The documents are stored in the <code>doc</code> subdirectory.</p>
<dl>
<dt>&bull;</dt>
<dd> <i>genindex</i></dd>
<dt>&bull;</dt>
<dd> <i>modindex</i></dd>
<dt>&bull;</dt>
<dd> <i>search</i></dd></dl>
<h2>AUTHOR</h2>
<p> Tully Foote, Thibault Kruse, Ken Conley</p>
<h2>COPYRIGHT</h2>
<p> 2010, Willow Garage </p>
