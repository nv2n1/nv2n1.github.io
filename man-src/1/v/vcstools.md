---
title: "vcstools(1)"
name: "vcstools"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcstools/"
description: "vcstools – vcstools Documentation"
---

<h2>NAME</h2>
<p> vcstools &#8211; vcstools Documentation </p>
<p> The <code>vcstools</code> module provides a Python API for interacting with different version control systems (VCS/SCMs). The <code>VcsClient</code> class provides an API for seamless interacting with Git, Mercurial (Hg), Bzr and SVN. The focus of the API is manipulating on-disk checkouts of source-controlled trees. Its main use is to support the <i>rosinstall</i> tool.</p>
<h2>GENERAL VCS/SCM API</h2>
<p> The <code>VcsClient</code> class provides a generic API for</p>
<dl>
<dt>&bull;</p>
<dd> Subversion (<code>svn</code>)</p>
<dt>&bull;</p>
<dd> Mercurial (<code>hg</code>)</p>
<dt>&bull;</p>
<dd> Git (<code>git</code>)</p>
<dt>&bull;</p>
<dd> Bazaar (<code>bzr</code>)</p>
<dt><code>class vcstools.VcsClient(vcs_type, path)</code></p>
<dd> API for interacting with source-controlled paths independent of actual version-control implementation.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>vcs_type</code> &#8212; type of VCS to use (e.g. &#8216;svn&#8217;, &#8216;hg&#8217;, &#8216;bzr&#8217;, &#8216;git&#8217;), <code>str</code></p>
<dt>&bull;</p>
<dd> <code>path</code> &#8212; filesystem path where code is/will be checked out , <code>str</code></p>
<dt><code>path_exists() -&gt; bool</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> True if path exists on disk.</p>
<dt><code>get_path() -&gt; str</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> filesystem path this client is initialized with.</p>
<dt><code>url_matches(self, url, url_or_shortcut) -&gt; bool</code></p>
<dd> client can decide whether the url and the other url are equivalent. Checks string equality by default</p>
<dt><code>Parameters</code></p>
<dd> <code>url_or_shortcut</code> &#8212; url or shortcut (e.g. bzr launchpad url)</p>
<dt><code>Returns</code></p>
<dd> bool if params are equivalent</p>
<dt><code>get_version([spec=None]) -&gt; str</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd> <code>spec</code> &#8212; </p>
<p> token for identifying repository revision desired. Token might be a tagname, branchname, version-id, or SHA-ID depending on the VCS implementation.</p>
<dt>&bull;</p>
<dd> svn: anything accepted by <code>svn info &#8211;help</code>, e.g. a <code>revnumber</code>, <code>{date}</code>, <code>HEAD</code>, <code>BASE</code>, <code>PREV</code>, or <code>COMMITTED</code></p>
<dt>&bull;</p>
<dd> git: anything accepted by <code>git log</code>, e.g. a tagname, branchname, or sha-id.</p>
<dt>&bull;</p>
<dd> hg: anything accepted by <code>hg log -r</code>, e.g. a tagname, sha-ID, revision-number</p>
<dt>&bull;</p>
<dd> bzr: revisionspec as returned by <code>bzr help revisionspec</code>, e.g. a tagname or <code>revno:&lt;number&gt;</code> </p>
<dt><code>Returns</code></p>
<dd> current revision number of the repository. Or if spec is provided, the globally unique identifier (e.g. revision number, or SHA-ID) of a revision specified by some token.</p>
<dt><code>get_remote_version(self, fatch=False) -&gt; str</code></p>
<dd> Find an identifier for the current revision on remote. Token spec might be a tagname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</p>
<dt><code>Parameters</code></p>
<dd> <code>fetch</code> &#8212; if False, only local information may be used</p>
<dt><code>Returns</code></p>
<dd> current revision number of the remote repository.</p>
<dt><code>get_current_version_label() -&gt; str</code></p>
<dd> Find an description for the current local version. Token spec might be a branchname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</p>
<dt><code>returns</code></p>
<dd> short description of local version (e.g. branchname, tagename).</p>
<dt><code>checkout(url[, version=&#8221;][, verbose=False][, shallow=False])</code></p>
<dd> Checkout the given URL to the path associated with this client.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>url</code> &#8212; URL of source control to check out</p>
<dt>&bull;</p>
<dd> <code>version</code> &#8212; specific version to check out</p>
<dt>&bull;</p>
<dd> <code>verbose</code> &#8212; flag to run verbosely</p>
<dt>&bull;</p>
<dd> <code>shallow</code> &#8212; flag to create shallow clone without history</p>
<dt><code>update(version)</code></p>
<dd> Update the local checkout from upstream source control.</p>
<dt><code>detect_presence() -&gt; bool</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> True if path has a checkout with matching VCS type, e.g. if the type of this client is &#8216;svn&#8217;, the checkout at the path is managed by Subversion.</p>
<dt><code>get_vcs_type_name() -&gt; str</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> type of VCS this client is initialized with.</p>
<dt><code>get_url() -&gt; str</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> Upstream URL that this code was checked out from.</p>
<dt><code>get_branch_parent()</code></p>
<dd> (Git Only)</p>
<dt><code>Returns</code></p>
<dd> parent branch.</p>
<dt><code>get_diff([basepath=None])</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd> <code>basepath</code> &#8212; compute diff relative to this path, if provided</p>
<dt><code>Returns</code></p>
<dd> A string showing local differences</p>
<dt><code>get_status([basepath=None[, untracked=False]])</code></p>
<dd> Calls scm status command. semantics of untracked are difficult to generalize. In SVN, this would be new files only. In git, hg, bzr, this would be changes that have not been added for commit.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>basepath</code> &#8212; status path will be relative to this, if provided.</p>
<dt>&bull;</p>
<dd> <code>untracked</code> &#8212; If True, also show changes that would not commit</p>
<dt><code>Returns</code></p>
<dd> A string summarizing locally modified files </p>
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
<dt><code>vcstools.setup_logger()</code></p>
<dd> creates a logger &#8216;vcstools&#8217;</dl>
<h3><code>bzr</code> Module</h3>
<p> bzr vcs support.</p>
<dl>
<dt><code>vcstools.bzr.BZRClient</code></p>
<dd> alias of <code>BzrClient</code></p>
<dt><code>class vcstools.bzr.BzrClient(path)</code></p>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></p>
<dt><code>__init__(path)</code></p>
<dd>
<dt><code>Raises </code></p>
<dd> VcsError if bzr not detected</p>
<dt><code>checkout(url, version=None, verbose=False, shallow=False, timeout=None)</code></p>
<dd>
<dt><code>export_repository(version, basepath)</code></p>
<dd>
<dt><code>get_branches(local_only=False)</code></p>
<dd>
<dt><code>get_current_version_label()</code></p>
<dd>
<dt><code>get_diff(basepath=None)</code></p>
<dd>
<dt><code>static get_environment_metadata()</code></p>
<dd>
<dt><code>get_log(relpath=None, limit=None)</code></p>
<dd>
<dt><code>get_remote_version(fetch=False)</code></p>
<dd>
<dt><code>get_status(basepath=None, untracked=False)</code></p>
<dd>
<dt><code>get_url()</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> BZR URL of the branch (output of bzr info command), </p>
<p> or None if it cannot be determined</p>
<dt><code>get_version(spec=None)</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd> <code>spec</code> &#8212; (optional) revisionspec of desired version. May be any revisionspec as returned by &#8216;bzr help revisionspec&#8217;, e.g. a tagname or &#8216;revno:&lt;number&gt;&#8217;</p>
<dt><code>Returns</code></p>
<dd> the current revision number of the repository. Or if spec is provided, the number of a revision specified by some token.</p>
<dt><code>static static_detect_presence(path)</code></p>
<dd>
<dt><code>update(version=u&#8221;, verbose=False, timeout=None)</code></p>
<dd>
<dt><code>url_matches(url, url_or_shortcut)</code></p>
<dd>
<dt><code>vcstools.bzr._get_bzr_version()</code></p>
<dd> Looks up bzr version by calling bzr &#8211;version. :raises: VcsError if bzr is not installed</dl>
<h3><code>git</code> Module</h3>
<p> git vcs support. </p>
<p> refnames in git can be branchnames, hashes, partial hashes, tags. On checkout, git will disambiguate by checking them in that order, taking the first that applies </p>
<p> This class aims to provide git for linear centralized workflows. This means in case of ambiguity, we assume that the only relevant remote is the one named &quot;origin&quot;, and we assume that commits once on origin remain on origin. </p>
<p> A challenge with git is that it has strong reasonable conventions, but is very allowing for breaking them. E.g. it is possible to name remotes and branches with names like &quot;refs/heads/master&quot;, give branches and tags the same name, or a valid SHA-ID as name, etc. Similarly git allows plenty of ways to reference any object, in case of ambiguities, git attempts to take the most reasonable disambiguation, and in some cases warns.</p>
<dl>
<dt><code>vcstools.git.GITClient</code></p>
<dd> alias of <code>GitClient</code></p>
<dt><code>class vcstools.git.GitClient(path)</code></p>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></p>
<dt><code>__init__(path)</code></p>
<dd>
<dt><code>Raises </code></p>
<dd> VcsError if git not detected</p>
<dt><code>_do_checkout(refname, fetch=True, verbose=False)</code></p>
<dd> meaning git checkout, not vcstools checkout. This works for local branches, remote branches, tagnames, hashes, etc. git will create local branch of same name when no such local branch exists, and also setup tracking. Git decides with own rules whether local changes would cause conflicts, and refuses to checkout else.</p>
<dt><code>Raises GitError</code></p>
<dd> when checkout fails</p>
<dt><code>_do_fast_forward(branch_parent, fetch=True, verbose=False)</code></p>
<dd> Execute git fetch if necessary, and if we can fast-foward, do so to the last fetched version using git rebase.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>branch_parent</code> &#8212; name of branch we track</p>
<dt>&bull;</p>
<dd> <code>fetch</code> &#8212; whether fetch should be done first for remote refs</p>
<dt><code>Returns</code></p>
<dd> True if up-to-date or after succesful fast-forward</p>
<dt><code>Raises </code></p>
<dd> GitError when git fetch fails</p>
<dt><code>_do_fetch(timeout=None)</code></p>
<dd> calls git fetch :raises: GitError when call fails</p>
<dt><code>_do_update(refname=None, verbose=False, fast_foward=True, timeout=None, update_submodules=True)</code></p>
<dd> updates without fetching, thus any necessary fetching must be done before allows arguments to reduce unnecessary steps after checkout</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>fast_foward</code> &#8212; if false, does not perform fast-forward</p>
<dt>&bull;</p>
<dd> <code>update_submodules</code> &#8212; if false, does not attempt to update submodules</p>
<dt><code>_get_branch()</code></p>
<dd>
<dt><code>_get_branch_parent(fetch=False, current_branch=None)</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>fetch</code> &#8212; if true, performs git fetch first</p>
<dt>&bull;</p>
<dd> <code>current_branch</code> &#8212; if not None, this is used as current branch (else extra shell call)</p>
<dt><code>Returns</code></p>
<dd> (branch, remote) the name of the branch this branch tracks and its remote</p>
<dt><code>Raises </code></p>
<dd> GitError if fetch fails</p>
<dt><code>_get_default_remote()</code></p>
<dd> in order to support users who name their default origin something else than origin, read remote name.</p>
<dt><code>_is_commit_in_orphaned_subtree(version, mask_self=False, fetch=True)</code></p>
<dd> checks git log &#8211;all (the list of all commits reached by references, meaning branches or tags) for version. If it shows up, that means git garbage collection will not remove the commit. Else it would eventually be deleted.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>version</code> &#8212; SHA IDs (if partial, caller is responsible for mismatch)</p>
<dt>&bull;</p>
<dd> <code>mask_self</code> &#8212; whether to consider direct references to this commit (rather than only references on descendants) as well</p>
<dt>&bull;</p>
<dd> <code>fetch</code> &#8212; whether fetch should be done first for remote refs</p>
<dt><code>Returns</code></p>
<dd> True if version is not recursively referenced by a branch or tag</p>
<dt><code>Raises </code></p>
<dd> GitError if git fetch fails</p>
<dt><code>_is_local_branch(branch_name)</code></p>
<dd>
<dt><code>_is_remote_branch(branch_name, remote_name=None, fetch=True)</code></p>
<dd> checks list of remote branches for match. Set fetch to False if you just fetched already.</p>
<dt><code>Returns</code></p>
<dd> True if branch_name exists for remote &lt;remote_name&gt; (or &#8216;origin&#8217; if None)</p>
<dt><code>Raises </code></p>
<dd> GitError when git fetch fails</p>
<dt><code>_rev_list_contains(refname, version, fetch=True)</code></p>
<dd> calls git rev-list with refname and returns True if version can be found in rev-list result</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>refname</code> &#8212; a git refname</p>
<dt>&bull;</p>
<dd> <code>version</code> &#8212; an SHA IDs (if partial, caller is responsible for mismatch)</p>
<dt><code>Returns</code></p>
<dd> True if version is an ancestor commit from refname</p>
<dt><code>Raises </code></p>
<dd> GitError when call to git fetch fails</p>
<dt><code>_update_submodules(verbose=False, timeout=None)</code></p>
<dd>
<dt><code>checkout(url, version=None, verbose=False, shallow=False, timeout=None)</code></p>
<dd> calls git clone and then, if version was given, update(version)</p>
<dt><code>export_repository(version, basepath)</code></p>
<dd>
<dt><code>get_branches(local_only=False)</code></p>
<dd>
<dt><code>get_current_version_label()</code></p>
<dd> For git we change the label to clarify when a different remote is configured.</p>
<dt><code>get_default_remote_version_label()</code></p>
<dd>
<dt><code>get_diff(basepath=None)</code></p>
<dd>
<dt><code>static get_environment_metadata()</code></p>
<dd>
<dt><code>get_log(relpath=None, limit=None)</code></p>
<dd>
<dt><code>get_remote_version(fetch=False)</code></p>
<dd>
<dt><code>get_status(basepath=None, untracked=False)</code></p>
<dd>
<dt><code>get_url()</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> git URL of the directory path (output of git info command), or None if it cannot be determined</p>
<dt><code>get_version(spec=None)</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>spec</code> &#8212; (optional) token to identify desired version. For git, this may be anything accepted by git log, e.g. a tagname, branchname, or sha-id.</p>
<dt>&bull;</p>
<dd> <code>fetch</code> &#8212; When spec is given, can be used to suppress git fetch call</p>
<dt><code>Returns</code></p>
<dd> current SHA-ID of the repository. Or if spec is provided, the SHA-ID of a commit specified by some token if found, else None</p>
<dt><code>is_tag(tag_name, fetch=True)</code></p>
<dd> checks list of tags for match. Set fetch to False if you just fetched already.</p>
<dt><code>Returns</code></p>
<dd> True if tag_name among known tags</p>
<dt><code>Raises </code></p>
<dd> GitError when call to git fetch fails</p>
<dt><code>static static_detect_presence(path)</code></p>
<dd>
<dt><code>update(version=None, verbose=False, force_fetch=False, timeout=None)</code></p>
<dd> if version is None, attempts fast-forwarding current branch, if any. </p>
<p> Else interprets version as a local branch, remote branch, tagname, hash, etc. </p>
<p> If it is a branch, attempts to move to it unless already on it, and to fast-forward, unless not a tracking branch. Else go untracked on tag or whatever version is. Does not leave if current commit would become dangling.</p>
<dt><code>Returns</code></p>
<dd> True if already up-to-date with remote or after successful fast_foward</p>
<dt><code>exception vcstools.git.GitError</code></p>
<dd> Bases: <code>exceptions.Exception</code></p>
<dt><code>vcstools.git._get_git_version()</code></p>
<dd> Looks up git version by calling git &#8211;version.</p>
<dt><code>Raises </code></p>
<dd> VcsError if git is not installed or returns </p>
<p> something unexpected</p>
<dt><code>vcstools.git._git_diff_path_submodule_change(diff, rel_path_prefix)</code></p>
<dd> Parses git diff result and changes the filename prefixes.</dl>
<h3><code>hg</code> Module</h3>
<p> hg vcs support. </p>
<p> using ui object to redirect output into a string</p>
<dl>
<dt><code>vcstools.hg.HGClient</code></p>
<dd> alias of <code>HgClient</code></p>
<dt><code>class vcstools.hg.HgClient(path)</code></p>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></p>
<dt><code>__init__(path)</code></p>
<dd>
<dt><code>Raises </code></p>
<dd> VcsError if hg not detected</p>
<dt><code>_do_pull(filter=False)</code></p>
<dd>
<dt><code>checkout(url, version=u&#8221;, verbose=False, shallow=False, timeout=None)</code></p>
<dd>
<dt><code>export_repository(version, basepath)</code></p>
<dd>
<dt><code>get_branch()</code></p>
<dd>
<dt><code>get_branches(local_only=False)</code></p>
<dd>
<dt><code>get_current_version_label()</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd> <code>spec</code> &#8212; (optional) spec can be what &#8216;svn info &#8211;help&#8217; allows, meaning a revnumber, {date}, HEAD, BASE, PREV, or COMMITTED.</p>
<dt><code>Returns</code></p>
<dd> current revision number of the repository. Or if spec provided, the number of a revision specified by some token.</p>
<dt><code>get_diff(basepath=None)</code></p>
<dd>
<dt><code>static get_environment_metadata()</code></p>
<dd>
<dt><code>get_log(relpath=None, limit=None)</code></p>
<dd>
<dt><code>get_remote_version(fetch=False)</code></p>
<dd>
<dt><code>get_status(basepath=None, untracked=False)</code></p>
<dd>
<dt><code>get_url()</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> HG URL of the directory path. (output of hg paths </p>
<p> command), or None if it cannot be determined</p>
<dt><code>get_version(spec=None)</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd> <code>spec</code> &#8212; (optional) token for identifying version. spec can be a whatever is allowed by &#8216;hg log -r&#8217;, e.g. a tagname, sha-ID, revision-number</p>
<dt><code>Returns</code></p>
<dd> the current SHA-ID of the repository. Or if spec is provided, the SHA-ID of a revision specified by some token.</p>
<dt><code>static static_detect_presence(path)</code></p>
<dd>
<dt><code>update(version=u&#8221;, verbose=False, timeout=None)</code></p>
<dd>
<dt><code>vcstools.hg._get_hg_version()</code></p>
<dd> Looks up hg version by calling hg &#8211;version. :raises: VcsError if hg is not installed</p>
<dt><code>vcstools.hg._hg_diff_path_change(diff, path)</code></p>
<dd> Parses hg diff result and changes the filename prefixes.</dl>
<h3><code>svn</code> Module</h3>
<p> svn vcs support.</p>
<dl>
<dt><code>vcstools.svn.SVNClient</code></p>
<dd> alias of <code>SvnClient</code></p>
<dt><code>class vcstools.svn.SvnClient(path)</code></p>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></p>
<dt><code>__init__(path)</code></p>
<dd>
<dt><code>Raises </code></p>
<dd> VcsError if python-svn not detected</p>
<dt><code>_get_version_from_path(spec=None, path=None)</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>spec</code> &#8212; (optional) spec can be what &#8216;svn info &#8211;help&#8217; allows, meaning a revnumber, {date}, HEAD, BASE, PREV, or COMMITTED.</p>
<dt>&bull;</p>
<dd> <code>path</code> &#8212; the url to use, default is for this repo</p>
<dt><code>Returns</code></p>
<dd> current revision number of the repository. Or if spec provided, the number of a revision specified by some token.</p>
<dt><code>checkout(url, version=u&#8221;, verbose=False, shallow=False, timeout=None)</code></p>
<dd>
<dt><code>export_repository(version, basepath)</code></p>
<dd>
<dt><code>get_branches(local_only=False)</code></p>
<dd>
<dt><code>get_current_version_label()</code></p>
<dd>
<dt><code>get_diff(basepath=None)</code></p>
<dd>
<dt><code>static get_environment_metadata()</code></p>
<dd>
<dt><code>get_log(relpath=None, limit=None)</code></p>
<dd>
<dt><code>get_remote_version(fetch=False)</code></p>
<dd>
<dt><code>get_status(basepath=None, untracked=False)</code></p>
<dd>
<dt><code>get_url()</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> SVN URL of the directory path (output of svn info command), </p>
<p> or None if it cannot be determined</p>
<dt><code>get_version(spec=None)</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>spec</code> &#8212; (optional) spec can be what &#8216;svn info &#8211;help&#8217; allows, meaning a revnumber, {date}, HEAD, BASE, PREV, or COMMITTED.</p>
<dt>&bull;</p>
<dd> <code>path</code> &#8212; the url to use, default is for this repo</p>
<dt><code>Returns</code></p>
<dd> current revision number of the repository. Or if spec provided, the number of a revision specified by some token.</p>
<dt><code>static static_detect_presence(path)</code></p>
<dd>
<dt><code>update(version=None, verbose=False, timeout=None)</code></p>
<dd>
<dt><code>vcstools.svn._get_svn_version()</code></p>
<dd> Looks up svn version by calling svn &#8211;version. :raises: VcsError if svn is not installed</p>
<dt><code>vcstools.svn.canonical_svn_url_split(url)</code></p>
<dd> checks url for traces of canonical svn structure, and return root, type, name (of tag or branch), subfolder, query and fragment (see urllib urlparse) This should allow creating a different url for switching to a different tag or branch</p>
<dt><code>Parameters</code></p>
<dd> <code>url</code> &#8212; location of central repo, <code>str</code></p>
<dt><code>Returns</code></p>
<dd> dict {root, type, name, subfolder, query, fragment} </p>
<p> with type one of &quot;trunk&quot;, &quot;tags&quot;, &quot;branches&quot;</p>
<dt><code>vcstools.svn.get_remote_contents(url)</code></p>
<dd></dl>
<h3><code>tar</code> Module</h3>
<p> tar vcs support. </p>
<p> The implementation uses the &quot;version&quot; argument to indicate a subfolder within a tarfile. Hence one can organize sources by creating one tarfile with a folder inside for each version.</p>
<dl>
<dt><code>vcstools.tar.TARClient</code></p>
<dd> alias of <code>TarClient</code></p>
<dt><code>class vcstools.tar.TarClient(path)</code></p>
<dd> Bases: <code>vcstools.vcs_base.VcsClientBase</code></p>
<dt><code>__init__(path)</code></p>
<dd> @raise VcsError if tar not detected</p>
<dt><code>checkout(url, version=u&#8221;, verbose=False, shallow=False, timeout=None)</code></p>
<dd> untars tar at url to self.path. If version was given, only the subdirectory &#8216;version&#8217; of the tar will end up in self.path. Also creates a file next to the checkout named </p>
<pre>
*
</pre>
<p> .tar which is a yaml file listing origin url and version arguments.</p>
<dt><code>export_repository(version, basepath)</code></p>
<dd>
<dt><code>get_current_version_label()</code></p>
<dd>
<dt><code>get_diff(basepath=None)</code></p>
<dd>
<dt><code>static get_environment_metadata()</code></p>
<dd>
<dt><code>get_remote_version(fetch=False)</code></p>
<dd>
<dt><code>get_status(basepath=None, untracked=False)</code></p>
<dd>
<dt><code>get_url()</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> TAR URL of the directory path (output of tar info </p>
<p> command), or None if it cannot be determined</p>
<dt><code>get_version(spec=None)</code></p>
<dd>
<dt><code>static static_detect_presence(path)</code></p>
<dd>
<dt><code>update(version=u&#8221;, verbose=False, timeout=None)</code></p>
<dd> Does nothing except returning true if tar exists in same &quot;version&quot; as checked out with vcstools.</dl>
<h3><code>vcs_abstraction</code> Module</h3>
<dl>
<dt><code>undoc-members</code></p>
<dd>
<dt><code>show-inheritance</code></p>
<dd>
<dt><code>vcstools.vcs_abstraction.VCSClient</code></p>
<dd> alias of <code>VcsClient</code></p>
<dt><code>class vcstools.vcs_abstraction.VcsClient(vcs_type, path)</code></p>
<dd> Bases: <code>object</code> </p>
<p> <i>DEPRECATED</i> API for interacting with source-controlled paths independent of actual version-control implementation.</p>
<dt><code>vcstools.vcs_abstraction.get_registered_vcs_types()</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> list of valid key to use as vcs_type</p>
<dt><code>vcstools.vcs_abstraction.get_vcs(vcs_type)</code></p>
<dd> Returns the class interfacing with vcs of given type</p>
<dt><code>Parameters</code></p>
<dd> <code>vcs_type</code> &#8212; id of the tpye, e.g. git, svn, hg, bzr</p>
<dt><code>Returns</code></p>
<dd> class extending VcsClientBase</p>
<dt><code>Raises </code></p>
<dd> ValueError for unknown vcs_type</p>
<dt><code>vcstools.vcs_abstraction.get_vcs_client(vcs_type, path)</code></p>
<dd> Returns a client with which to interact with the vcs at given path</p>
<dt><code>Parameters</code></p>
<dd> <code>vcs_type</code> &#8212; id of the tpye, e.g. git, svn, hg, bzr</p>
<dt><code>Returns</code></p>
<dd> instance of VcsClientBase</p>
<dt><code>Raises </code></p>
<dd> ValueError for unknown vcs_type</p>
<dt><code>vcstools.vcs_abstraction.register_vcs(vcs_type, clazz)</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>vcs_type</code> &#8212; id, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>clazz</code> &#8212; class extending VcsClientBase</dl>
<h3><code>vcs_base</code> Module</h3>
<p> vcs support library base class.</p>
<dl>
<dt><code>undoc-members</code></p>
<dd>
<dt><code>show-inheritance</code></p>
<dd>
<dt><code>class vcstools.vcs_base.VcsClientBase(vcs_type_name, path)</code></p>
<dd> Bases: <code>object</code> </p>
<p> parent class for all vcs clients, provides their public API</p>
<dt><code>__init__(vcs_type_name, path)</code></p>
<dd> subclasses may raise VcsError when a dependency is missing</p>
<dt><code>checkout(url, version=None, verbose=False, shallow=False, timeout=None)</code></p>
<dd> Attempts to create a local repository given a remote url. Fails if a target path exists, unless it&#8217;s an empty directory. If a version is provided, the local repository will be updated to that revision. It is possible that after a failed call to checkout, a repository still exists, e.g. if an invalid revision was given. If shallow is provided, the scm client may checkout less than the full repository history to save time / disk space. If a timeout is specified, any pending operation will fail after the specified amount (in seconds). NOTE: this parameter might or might not be honored, depending on VCS client implementation. :param url: where to checkout from :type url: str :param version: token for identifying repository revision :type version: str :param shallow: hint to checkout less than a full repository :type shallow: bool :param timeout: maximum allocated time to perform operation :type shallow: int :returns: True if successful</p>
<dt><code>detect_presence()</code></p>
<dd> For auto detection</p>
<dt><code>export_repository(version, basepath)</code></p>
<dd> Calls scm equivalent to <i>svn export</i>, removing scm meta information and tar gzip&#8217;ing the repository at a given version to the given basepath.</p>
<dt><code>Parameters</code></p>
<dd> <code>version</code> &#8212; version of the repository to export. This can </p>
<p> be a branch, tag, or path (svn). When specifying the version as a path for svn, the path should be relative to the root of the svn repository, i.e. &#8216;trunk&#8217;, or &#8216;tags/1.2.3&#8217;, or &#8216;./&#8217; for the root. :param basepath: this is the path to the tar gzip, excluding the extension which will be .tar.gz :returns: True on success, False otherwise.</p>
<dt><code>get_branches(local_only=False)</code></p>
<dd> Returns a list of all branches in the vcs repository.</p>
<dt><code>Parameters</code></p>
<dd> <code>local_only</code> &#8212; if True it will only list local branches</p>
<dt><code>Returns</code></p>
<dd> list of branches in the repository, [] if none exist</p>
<dt><code>get_current_version_label()</code></p>
<dd> Find an description for the current local version. Token spec might be a branchname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</p>
<dt><code>Returns</code></p>
<dd> short description of local version (e.g. branchname, tagename).</p>
<dt><code>Return type</code></p>
<dd> str</p>
<dt><code>get_default_remote_version_label()</code></p>
<dd> Find a label for the default branch on remote, meaning the one that would be checked out on a clean checkout.</p>
<dt><code>Returns</code></p>
<dd> a label or None (if not applicable)</p>
<dt><code>Return type</code></p>
<dd> str</p>
<dt><code>get_diff(basepath=None)</code></p>
<dd>
<dt><code>Parameters</code></p>
<dd> <code>basepath</code> &#8212; diff paths will be relative to this, if any</p>
<dt><code>Returns</code></p>
<dd> A string showing local differences</p>
<dt><code>Return type</code></p>
<dd> str</p>
<dt><code>static get_environment_metadata()</code></p>
<dd> For debugging purposes, returns a dict containing information about the environment, like the version of the SCM client, or version of libraries involved. Suggest considering keywords &quot;version&quot;, &quot;dependency&quot;, &quot;features&quot; first. :returns: a dict containing relevant information :rtype: dict</p>
<dt><code>get_log(relpath=None, limit=None)</code></p>
<dd> Calls scm log command.</p>
<dt><code>This returns a list of dictionaries with the following fields:</code></p>
<dd>
<dt>&bull;</p>
<dd> id: the commit SHA or revision number</p>
<dt>&bull;</p>
<dd> date: the date the commit was made (python datetime)</p>
<dt>&bull;</p>
<dd> author: the name of the author of the commit, if available</p>
<dt>&bull;</p>
<dd> email: the e-mail address of the author of the commit</p>
<dt>&bull;</p>
<dd> message: the commit message, if any</p>
<dt><code>Parameters</code></p>
<dd> <code>relpath</code> &#8212; (optional) restrict logs to events on this </p>
<p> resource path (folder or file) relative to the root of the repository. If None (default), this is the root of the repository. :param limit: (optional) the maximum number of log entries that should be retrieved. If None (default), there is no limit.</p>
<dt><code>get_path()</code></p>
<dd> returns the path this client was configured for</p>
<dt><code>get_remote_version(fetch=False)</code></p>
<dd> Find an identifier for the current revision on remote. Token spec might be a tagname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</p>
<dt><code>Parameters</code></p>
<dd> <code>fetch</code> &#8212; if False, only local information may be used</p>
<dt><code>Returns</code></p>
<dd> current revision number of the remote repository.</p>
<dt><code>Return type</code></p>
<dd> str</p>
<dt><code>get_status(basepath=None, untracked=False)</code></p>
<dd> Calls scm status command. Output must be terminated by newline unless empty. </p>
<p> Semantics of untracked are difficult to generalize. In SVN, this would be new files only. In git, hg, bzr, this would be changes that have not been added for commit.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>basepath</code> &#8212; status path will be relative to this, if any</p>
<dt>&bull;</p>
<dd> <code>untracked</code> &#8212; whether to also show changes that would not commit</p>
<dt><code>Returns</code></p>
<dd> A string summarizing locally modified files</p>
<dt><code>Return type</code></p>
<dd> str</p>
<dt><code>get_url()</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> The source control url for the path or None if not set</p>
<dt><code>Return type</code></p>
<dd> str</p>
<dt><code>get_vcs_type_name()</code></p>
<dd> used when auto detected</p>
<dt><code>get_version(spec=None)</code></p>
<dd> Find an identifier for a the current or a specified revision. Token spec might be a tagname, branchname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</p>
<dt><code>Parameters</code></p>
<dd> <code>spec</code> (<i>str</i>) &#8212; token for identifying repository revision</p>
<dt><code>Returns</code></p>
<dd> current revision number of the repository. Or if spec is provided, the respective revision number.</p>
<dt><code>Return type</code></p>
<dd> str</p>
<dt><code>path_exists()</code></p>
<dd> helper function</p>
<dt><code>static static_detect_presence(path)</code></p>
<dd> For auto detection</p>
<dt><code>update(version=None, verbose=False, timeout=None)</code></p>
<dd> Sets the local copy of the repository to a version matching the version parameter. Fails when there are uncommited changes. On failures (also e.g. network failure) grants the checked out files are in the same state as before the call. If a timeout is specified, any pending operation will fail after the specified amount (in seconds)</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>version</code> &#8212; token for identifying repository revision desired. Token might be a tagname, branchname, version-id, SHA-ID, &#8230; depending on the VCS implementation.</p>
<dt>&bull;</p>
<dd> <code>timeout</code> &#8212; maximum allocated time to perform operation</p>
<dt><code>Returns</code></p>
<dd> True on success, False else</p>
<dt><code>url_matches(url, url_or_shortcut)</code></p>
<dd> client can decide whether the url and the other url are equivalent. Checks string equality by default :param url_or_shortcut: url or shortcut (e.g. bzr launchpad url) :returns: bool if params are equivalent</p>
<dt><code>exception vcstools.vcs_base.VcsError(value)</code></p>
<dd> Bases: <code>exceptions.Exception</code> </p>
<p> To be thrown when an SCM Client faces a situation because of a violated assumption</dl>
<h3>Changelog</h3>
<h3>Changelog</h3>
<h3>0.1</h3>
<h3>0.1.38</h3>
<dl>
<dt>&bull;</p>
<dd> Fixed test failures due to SVN 1.9.</p>
<dt>&bull;</p>
<dd> Added the <code>get_default_remote_version_label()</code> API method to support changes in <code>wstool</code>.</p>
<dt>&bull;</p>
<dd> Renamed some internal functions to have a leading <code>_</code> to indicate that they are private.</dl>
<h3>0.1.37</h3>
<dl>
<dt>&bull;</p>
<dd> Fix an issue where log were restricted to the named branch (hg).</p>
<dt>&bull;</p>
<dd> Fixed svn to use a global revision number rather than a branch-local revision.</p>
<dt>&bull;</p>
<dd> Added the get_remote_version() and get_current_version_label() API calls.</p>
<dt>&bull;</p>
<dd> Enhanced use of <code>no_warn</code> in run_shell_command().</p>
<dt>&bull;</p>
<dd> Fix get_version() to catch stderr.</p>
<dt>&bull;</p>
<dd> Added get_branches() API call.</p>
<dt>&bull;</p>
<dd> Fix some errors and warnings to output to stderr.</p>
<dt>&bull;</p>
<dd> Fix output to avoid extra newlines when show_stdout=True.</dl>
<h3>0.1.36</h3>
<dl>
<dt>&bull;</p>
<dd> Updates to the release platforms (-lucid +utopic +vivid)</p>
<dt>&bull;</p>
<dd> Fix an issue with updating branches on git, see vcstools/wstool#25</dl>
<h3>0.1.31</h3>
<dl>
<dt>&bull;</p>
<dd> Fix submodule support on checkout #71</dl>
<h3>0.1.30</h3>
<dl>
<dt>&bull;</p>
<dd> use netrc to download tars from private repos, also will work for private rosinstall files</p>
<dt>&bull;</p>
<dd> Fix checks for empty repository #62</dl>
<h3>0.1.29</h3>
<dl>
<dt>&bull;</p>
<dd> fix #57 shallow checkout of non-master breaks with git &gt;= 1.8.0</p>
<dt>&bull;</p>
<dd> unit test fixes</dl>
<h3>0.1.28</h3>
<dl>
<dt>&bull;</p>
<dd> test of new upload method</dl>
<h3>0.1.27</h3>
<dl>
<dt>&bull;</p>
<dd> fix #51 hg status and diff dont work if workspace is inside hg repo</p>
<dt>&bull;</p>
<dd> fix #47 several performance improvements by removing unecessary update actions after checkout</p>
<dt>&bull;</p>
<dd> fix #46 https tar download fails behind proxy</p>
<dt>&bull;</p>
<dd> fix #45 sometimes commands run forever</p>
<dt>&bull;</p>
<dd> fix #44 minor bug when checking out from repo with default branch not master</p>
<dt>&bull;</p>
<dd> fix #41 improvedAPI, get_vcs_client function part of vcstools module</dl>
<h3>0.1.26</h3>
<dl>
<dt>&bull;</p>
<dd> fix #38 git commands fail in local repositories with many (&gt;2000) references</p>
<dt>&bull;</p>
<dd> fix #31 get_log() svn xml not available on Ubuntu Lucid (hg 1.4.2)</p>
<dt>&bull;</p>
<dd> fix #37 update() returns True even when fetch failed</dl>
<h3>0.1.25</h3>
<dl>
<dt>&bull;</p>
<dd> minor bugfixes</p>
<dt>&bull;</p>
<dd> travis-ci config file</p>
<dt>&bull;</p>
<dd> fix unit tests for svn diff&amp;status ordering changes</p>
<dt>&bull;</p>
<dd> deprecated VcsClient Class</p>
<dt>&bull;</p>
<dd> added get_log function</dl>
<h3>0.1.24</h3>
<dl>
<dt>&bull;</p>
<dd> fix git update return value to False when fast-forward not possible due to diverge</p>
<dt>&bull;</p>
<dd> fix. svn certificate prompt invisible, svn checkout and update become verbose due to this</dl>
<h3>0.1.22</h3>
<dl>
<dt>&bull;</p>
<dd> Changed the way that git implements detect_presence to fix a bug with submodules in newer versions of git</p>
<dt>&bull;</p>
<dd> fix for git single quotes on Windows</p>
<dt>&bull;</p>
<dd> minor internal api bug where a git function always returned True</p>
<dt>&bull;</p>
<dd> fix gub in svn export_repository</dl>
<h3>0.1.21</h3>
<dl>
<dt>&bull;</p>
<dd> bugfix #66: hg http username prompt hidden</p>
<dt>&bull;</p>
<dd> add export_repository method to vcs_base and all implementations with tests</p>
<dt>&bull;</p>
<dd> bugfix #64: unicode decoding problems</dl>
<h3>0.1.20</h3>
<dl>
<dt>&bull;</p>
<dd> rosws update &#8211;verbose for git prints small message when rebasing</p>
<dt>&bull;</p>
<dd> improved python3 compatibility</dl>
<h3>0.1.19</h3>
<dl>
<dt>&bull;</p>
<dd> more python3 compatibility</p>
<dt>&bull;</p>
<dd> code style improved</p>
<dt>&bull;</p>
<dd> match_url to compare bzr shortcuts to real urls</p>
<dt>&bull;</p>
<dd> more unit tests</p>
<dt>&bull;</p>
<dd> get_status required to end with newline, to fix #55</dl>
<h3>0.1.18</h3>
<dl>
<dt>&bull;</p>
<dd> added shallow flag to API, implemented for git</dl>
<h3>0.1.17</h3>
<dl>
<dt>&bull;</p>
<dd> svn stdout output on get_version removed</dl>
<h3>0.1.16</h3>
<dl>
<dt>&bull;</p>
<dd> All SCMs show some output when update caused changes</p>
<dt>&bull;</p>
<dd> All SCMs have verbose option to show all changes done on update</p>
<dt>&bull;</p>
<dd> bugfix for bazaar getUrl() being a joined abspath</p>
<dt>&bull;</p>
<dd> bugfix for not all output being shown when requested</dl>
<h3>0.1.15</h3>
<dl>
<dt>&bull;</p>
<dd> Added pyyaml as a proper dependency, removed detection code.</p>
<dt>&bull;</p>
<dd> remove use of tar entirely, switch to tarfile module</p>
<dt>&bull;</p>
<dd> fix #36 allowing for tar being bsdtar on OSX</dl>
<h3>0.1.14</h3>
<dl>
<dt>&bull;</p>
<dd> Added tarball uncompression.</dl>
<h3>0.1.13</h3>
<dl>
<dt>&bull;</p>
<dd> added this changelog</p>
<dt>&bull;</p>
<dd> git get-version fetches only when local lookup fails</p>
<dt>&bull;</p>
<dd> hg get-version pulls if label not found</p>
<dt>&bull;</p>
<dd> Popen error message incudes cwd path</dl>
<h3>0.1.12</h3>
<dl>
<dt>&bull;</p>
<dd> py_checker clean after all refactorings since 0.1.0</dl>
<h3>0.1.11</h3>
<dl>
<dt>&bull;</p>
<dd> svn and hg update without user interaction</p>
<dt>&bull;</p>
<dd> bugfix #30</p>
<dt>&bull;</p>
<dd> minor bugfixes</dl>
<h3>0.1.10</h3>
<dl>
<dt>&bull;</p>
<dd> minor bugs</dl>
<h3>0.1.9</h3>
<dl>
<dt>&bull;</p>
<dd> safer sanitization of shell params</p>
<dt>&bull;</p>
<dd> git diff and stat recurse for submodules</p>
<dt>&bull;</p>
<dd> base class manages all calls to Popen</dl>
<h3>0.1.8</h3>
<dl>
<dt>&bull;</p>
<dd> several bugfixes</p>
<dt>&bull;</p>
<dd> reverted using shell commands instead of bazaar API</dl>
<h3>0.1.7</h3>
<dl>
<dt>&bull;</p>
<dd> reverted using shell commands instaed of pysvn and mercurial APIs</p>
<dt>&bull;</p>
<dd> protection against shell incection attempts</dl>
<h3>0.1.6</h3>
<dl>
<dt>&bull;</p>
<dd> bugfixes to svn and bzr</p>
<dt>&bull;</p>
<dd> unified all calls through Popen</dl>
<h3>0.1.5</h3>
<dl>
<dt>&bull;</p>
<dd> missing dependency to dateutil added</dl>
<h3>0.1.4</h3>
<p> switched shell calls to calls to python API of mercurial, bazaar, py-svn</p>
<h3>0.1.3</h3>
<dl>
<dt>&bull;</p>
<dd> fix #6</dl>
<h3>0.1.2</h3>
<dl>
<dt>&bull;</p>
<dd> fix #15</dl>
<h3>0.1.1</h3>
<dl>
<dt>&bull;</p>
<dd> more unit tests</p>
<dt>&bull;</p>
<dd> diverse bugfixes</p>
<dt>&bull;</p>
<dd> major change to git client behavior, based around git <i><a rel="nofollow" href="https://kforge.ros.org/vcstools/trac/ticket/1">https://kforge.ros.org/vcstools/trac/ticket/1</a></i></dl>
<h3>0.1.0</h3>
<dl>
<dt>&bull;</p>
<dd> documentation fixes</dl>
<h3>0.0.3</h3>
<dl>
<dt>&bull;</p>
<dd> import from svn</dl>
<h3>Bug reports and feature requests</h3>
<dl>
<dt>&bull;</p>
<dd> <i>Submit a bug report</i></dl>
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
<dt>&bull;</p>
<dd> <i>genindex</i></p>
<dt>&bull;</p>
<dd> <i>modindex</i></p>
<dt>&bull;</p>
<dd> <i>search</i></dl>
<h2>AUTHOR</h2>
<p> Tully Foote, Thibault Kruse, Ken Conley</p>
<h2>COPYRIGHT</h2>
<p> 2010, Willow Garage </p>
<h2>Index</h2>
<dt><a href="#lbCF">AUTHOR</a></p>
<dd>
<dt><a href="#lbCG">COPYRIGHT</a></p>
<dd></dl>
