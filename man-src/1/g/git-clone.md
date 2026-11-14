---
title: "git-clone(1)"
name: "git-clone"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-clone/"
description: "git-clone – Clone a repository into a new directory"
---

<h2 class="name">NAME</h2>
<p> git-clone &#8211; Clone a repository into a new directory </p>
<h2>SYNOPSIS</h2>
<pre><code>
git clone[--template = &lt;template_directory&gt;]
         [-l][-s][--no - hardlinks][-q][-n][--bare][--mirror]
         [-o&lt;name&gt;][-b&lt;name&gt;][-u&lt;upload - pack&gt;][--reference&lt;repository&gt;]
         [--dissociate][--separate - git - dir&lt;git dir&gt;]
         [--depth&lt;depth&gt;][--[no - ] single - branch][--no - tags]
         [--recurse - submodules[=&lt;pathspec&gt;]][--[no - ] shallow - submodules]
         [--[no - ] remote - submodules][--jobs&lt;n&gt;][--sparse][--[no - ] reject - shallow]
         [--filter = &lt;filter&gt;][--]&lt;repository&gt;[&lt;directory&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Clones a repository into a newly created directory, creates remote-tracking branches for each branch in the cloned repository (visible using <code>git branch &#8211;remotes</code>), and creates and checks out an initial branch that is forked from the cloned repository&#8217;s currently active branch. </p>
<p> After the clone, a plain <code>git fetch</code> without arguments will update all the remote-tracking branches, and a <code>git pull</code> without arguments will in addition merge the remote master branch into the current master branch, if any (this is untrue when &quot;&#8211;single-branch&quot; is given; see below). </p>
<p> This default configuration is achieved by creating references to the remote branch heads under <code>refs/remotes/origin</code> and by initializing <code>remote.origin.url</code> and <code>remote.origin.fetch</code> configuration variables.</p>
<h2>OPTIONS</h2>
<p> -l, &#8211;local</p>
<dl>
<dt>
<dd> When the repository to clone from is on a local machine, this flag bypasses the normal &quot;Git aware&quot; transport mechanism and clones the repository by making a copy of HEAD and everything under objects and refs directories. The files under <code>.git/objects/</code> directory are hardlinked to save space when possible. </p>
<p> If the repository is specified as a local path (e.g., <code>/path/to/repo</code>), this is the default, and &#8211;local is essentially a no-op. If the repository is specified as a URL, then this flag is ignored (and we never use the local optimizations). Specifying <code>&#8211;no-local</code> will override the default when <code>/path/to/repo</code> is given, using the regular Git transport instead. </p>
<p> <code>NOTE</code>: this operation can race with concurrent modification to the source repository, similar to running <code>cp -r src dst</code> while modifying <code>src</code>.</dl>
<p> &#8211;no-hardlinks</p>
<dl>
<dt>
<dd> Force the cloning process from a repository on a local filesystem to copy the files under the <code>.git/objects</code> directory instead of using hardlinks. This may be desirable if you are trying to make a back-up of your repository.</dl>
<p> -s, &#8211;shared</p>
<dl>
<dt>
<dd> When the repository to clone is on the local machine, instead of using hard links, automatically setup <code>.git/objects/info/alternates</code> to share the objects with the source repository. The resulting repository starts out without any object of its own. </p>
<p> <code>NOTE</code>: this is a possibly dangerous operation; do <code>not</code> use it unless you understand what it does. If you clone your repository using this option and then delete branches (or use any other Git command that makes any existing commit unreferenced) in the source repository, some objects may become unreferenced (or dangling). These objects may be removed by normal Git operations (such as <code>git commit</code>) which automatically call <code>git maintenance run &#8211;auto</code>. (See <code><a href="/docs/linux/man/1-git-maintenance/">git-maintenance</a></code>(1).) If these objects are removed and were referenced by the cloned repository, then the cloned repository will become corrupt. </p>
<p> Note that running <code>git repack</code> without the <code>&#8211;local</code> option in a repository cloned with <code>&#8211;shared</code> will copy objects from the source repository into a pack in the cloned repository, removing the disk space savings of <code>clone &#8211;shared</code>. It is safe, however, to run <code>git gc</code>, which uses the <code>&#8211;local</code> option by default. </p>
<p> If you want to break the dependency of a repository cloned with <code>&#8211;shared</code> on its source repository, you can simply run <code>git repack -a</code> to copy all objects from the source repository into a pack in the cloned repository.</dl>
<p> &#8211;reference[-if-able] &lt;repository&gt;</p>
<dl>
<dt>
<dd> If the reference repository is on the local machine, automatically setup <code>.git/objects/info/alternates</code> to obtain objects from the reference repository. Using an already existing repository as an alternate will require fewer objects to be copied from the repository being cloned, reducing network and local storage costs. When using the <code>&#8211;reference-if-able</code>, a non existing directory is skipped with a warning instead of aborting the clone. </p>
<p> <code>NOTE</code>: see the NOTE for the <code>&#8211;shared</code> option, and also the <code>&#8211;dissociate</code> option.</dl>
<p> &#8211;dissociate</p>
<dl>
<dt>
<dd> Borrow the objects from reference repositories specified with the <code>&#8211;reference</code> options only to reduce network transfer, and stop borrowing from them after a clone is made by making necessary local copies of borrowed objects. This option can also be used when cloning locally from a repository that already borrows objects from another repository&#8212;the new repository will borrow objects from the same repository, and this option can be used to stop the borrowing.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Operate quietly. Progress is not reported to the standard error stream.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Run verbosely. Does not affect the reporting of progress status to the standard error stream.</dl>
<p> &#8211;progress</p>
<dl>
<dt>
<dd> Progress status is reported on the standard error stream by default when it is attached to a terminal, unless <code>&#8211;quiet</code> is specified. This flag forces progress status even if the standard error stream is not directed to a terminal.</dl>
<p> &#8211;server-option=&lt;option&gt;</p>
<dl>
<dt>
<dd> Transmit the given string to the server when communicating using protocol version 2. The given string must not contain a NUL or LF character. The server&#8217;s handling of server options, including unknown ones, is server-specific. When multiple <code>&#8211;server-option=&lt;option&gt;</code> are given, they are all sent to the other side in the order listed on the command line.</dl>
<p> -n, &#8211;no-checkout</p>
<dl>
<dt>
<dd> No checkout of HEAD is performed after the clone is complete.</dl>
<p> &#8211;[no-]reject-shallow</p>
<dl>
<dt>
<dd> Fail if the source repository is a shallow repository. The <i>clone.rejectShallow</i> configuration variable can be used to specify the default.</dl>
<p> &#8211;bare</p>
<dl>
<dt>
<dd> Make a <i>bare</i> Git repository. That is, instead of creating <code>&lt;directory&gt;</code> and placing the administrative files in <code>&lt;directory&gt;/.git</code>, make the <code>&lt;directory&gt;</code> itself the <code>$GIT_DIR</code>. This obviously implies the <code>&#8211;no-checkout</code> because there is nowhere to check out the working tree. Also the branch heads at the remote are copied directly to corresponding local branch heads, without mapping them to <code>refs/remotes/origin/</code>. When this option is used, neither remote-tracking branches nor the related configuration variables are created.</dl>
<p> &#8211;sparse</p>
<dl>
<dt>
<dd> Initialize the sparse-checkout file so the working directory starts with only the files in the root of the repository. The sparse-checkout file can be modified to grow the working directory as needed.</dl>
<p> &#8211;filter=&lt;filter-spec&gt;</p>
<dl>
<dt>
<dd> Use the partial clone feature and request that the server sends a subset of reachable objects according to a given object filter. When using <code>&#8211;filter</code>, the supplied <code>&lt;filter-spec&gt;</code> is used for the partial clone filter. For example, <code>&#8211;filter=blob:none</code> will filter out all blobs (file contents) until needed by Git. Also, <code>&#8211;filter=blob:limit=&lt;size&gt;</code> will filter out all blobs of size at least <code>&lt;size&gt;</code>. For more details on filter specifications, see the <code>&#8211;filter</code> option in <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1).</dl>
<p> &#8211;mirror</p>
<dl>
<dt>
<dd> Set up a mirror of the source repository. This implies <code>&#8211;bare</code>. Compared to <code>&#8211;bare</code>, <code>&#8211;mirror</code> not only maps local branches of the source to local branches of the target, it maps all refs (including remote-tracking branches, notes etc.) and sets up a refspec configuration such that all these refs are overwritten by a <code>git remote update</code> in the target repository.</dl>
<p> -o &lt;name&gt;, &#8211;origin &lt;name&gt;</p>
<dl>
<dt>
<dd> Instead of using the remote name <code>origin</code> to keep track of the upstream repository, use <code>&lt;name&gt;</code>. Overrides <code>clone.defaultRemoteName</code> from the config.</dl>
<p> -b &lt;name&gt;, &#8211;branch &lt;name&gt;</p>
<dl>
<dt>
<dd> Instead of pointing the newly created HEAD to the branch pointed to by the cloned repository&#8217;s HEAD, point to <code>&lt;name&gt;</code> branch instead. In a non-bare repository, this is the branch that will be checked out. <code>&#8211;branch</code> can also take tags and detaches the HEAD at that commit in the resulting repository.</dl>
<p> -u &lt;upload-pack&gt;, &#8211;upload-pack &lt;upload-pack&gt;</p>
<dl>
<dt>
<dd> When given, and the repository to clone from is accessed via ssh, this specifies a non-default path for the command run on the other end.</dl>
<p> &#8211;template=&lt;template_directory&gt;</p>
<dl>
<dt>
<dd> Specify the directory from which templates will be used; (See the &quot;TEMPLATE DIRECTORY&quot; section of <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1).)</dl>
<p> -c &lt;key&gt;=&lt;value&gt;, &#8211;config &lt;key&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> Set a configuration variable in the newly-created repository; this takes effect immediately after the repository is initialized, but before the remote history is fetched or any files checked out. The key is in the same format as expected by <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) (e.g., <code>core.eol=true</code>). If multiple values are given for the same key, each value will be written to the config file. This makes it safe, for example, to add additional fetch refspecs to the origin remote. </p>
<p> Due to limitations of the current implementation, some configuration variables do not take effect until after the initial fetch and checkout. Configuration variables known to not take effect are: <code>remote.&lt;name&gt;.mirror</code> and <code>remote.&lt;name&gt;.tagOpt</code>. Use the corresponding <code>&#8211;mirror</code> and <code>&#8211;no-tags</code> options instead.</dl>
<p> &#8211;depth &lt;depth&gt;</p>
<dl>
<dt>
<dd> Create a <i>shallow</i> clone with a history truncated to the specified number of commits. Implies <code>&#8211;single-branch</code> unless <code>&#8211;no-single-branch</code> is given to fetch the histories near the tips of all branches. If you want to clone submodules shallowly, also pass <code>&#8211;shallow-submodules</code>.</dl>
<p> &#8211;shallow-since=&lt;date&gt;</p>
<dl>
<dt>
<dd> Create a shallow clone with a history after the specified time.</dl>
<p> &#8211;shallow-exclude=&lt;revision&gt;</p>
<dl>
<dt>
<dd> Create a shallow clone with a history, excluding commits reachable from a specified remote branch or tag. This option can be specified multiple times.</dl>
<p> &#8211;[no-]single-branch</p>
<dl>
<dt>
<dd> Clone only the history leading to the tip of a single branch, either specified by the <code>&#8211;branch</code> option or the primary branch remote&#8217;s <code>HEAD</code> points at. Further fetches into the resulting repository will only update the remote-tracking branch for the branch this option was used for the initial cloning. If the HEAD at the remote did not point at any branch when <code>&#8211;single-branch</code> clone was made, no remote-tracking branch is created.</dl>
<p> &#8211;no-tags</p>
<dl>
<dt>
<dd> Don&#8217;t clone any tags, and set <code>remote.&lt;remote&gt;.tagOpt=&#8211;no-tags</code> in the config, ensuring that future <code>git pull</code> and <code>git fetch</code> operations won&#8217;t follow any tags. Subsequent explicit tag fetches will still work, (see <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1)). </p>
<p> Can be used in conjunction with <code>&#8211;single-branch</code> to clone and maintain a branch with no references other than a single cloned branch. This is useful e.g. to maintain minimal clones of the default branch of some repository for search indexing.</dl>
<p> &#8211;recurse-submodules[=&lt;pathspec&gt;]</p>
<dl>
<dt>
<dd> After the clone is created, initialize and clone submodules within based on the provided pathspec. If no pathspec is provided, all submodules are initialized and cloned. This option can be given multiple times for pathspecs consisting of multiple entries. The resulting clone has <code>submodule.active</code> set to the provided pathspec, or &quot;.&quot; (meaning all submodules) if no pathspec is provided. </p>
<p> Submodules are initialized and cloned using their default settings. This is equivalent to running <code>git submodule update &#8211;init &#8211;recursive &lt;pathspec&gt;</code> immediately after the clone is finished. This option is ignored if the cloned repository does not have a worktree/checkout (i.e. if any of <code>&#8211;no-checkout</code>/<code>-n</code>, <code>&#8211;bare</code>, or <code>&#8211;mirror</code> is given)</dl>
<p> &#8211;[no-]shallow-submodules</p>
<dl>
<dt>
<dd> All submodules which are cloned will be shallow with a depth of 1.</dl>
<p> &#8211;[no-]remote-submodules</p>
<dl>
<dt>
<dd> All submodules which are cloned will use the status of the submodule&#8217;s remote-tracking branch to update the submodule, rather than the superproject&#8217;s recorded SHA-1. Equivalent to passing <code>&#8211;remote</code> to <code>git submodule update</code>.</dl>
<p> &#8211;separate-git-dir=&lt;git dir&gt;</p>
<dl>
<dt>
<dd> Instead of placing the cloned repository where it is supposed to be, place the cloned repository at the specified directory, then make a filesystem-agnostic Git symbolic link to there. The result is Git repository can be separated from working tree.</dl>
<p> -j &lt;n&gt;, &#8211;jobs &lt;n&gt;</p>
<dl>
<dt>
<dd> The number of submodules fetched at the same time. Defaults to the <code>submodule.fetchJobs</code> option.</dl>
<p> &lt;repository&gt;</p>
<dl>
<dt>
<dd> The (possibly remote) repository to clone from. See the GIT URLS section below for more information on specifying repositories.</dl>
<p> &lt;directory&gt;</p>
<dl>
<dt>
<dd> The name of a new directory to clone into. The &quot;humanish&quot; part of the source repository is used if no directory is explicitly given (<code>repo</code> for <code>/path/to/repo.git</code> and <code>foo</code> for <code>host.xz:foo/.git</code>). Cloning into an existing directory is only allowed if the directory is empty.</dl>
<h2>GIT URLS</h2>
<p> In general, URLs contain information about the transport protocol, the address of the remote server, and the path to the repository. Depending on the transport protocol, some of this information may be absent. </p>
<p> Git supports ssh, git, http, and https protocols (in addition, ftp, and ftps can be used for fetching, but this is inefficient and deprecated; do not use it). </p>
<p> The native transport (i.e. git:// URL) does no authentication and should be used with caution on unsecured networks. </p>
<p> The following syntaxes may be used with them: </p>
<dl>
<dt>
<dd> &bull; <a href="ssh://[user@]host.xz[:port]/path/to/repo.git/">ssh://[user@]host.xz[:port]/path/to/repo.git/</a></dl>
<dl>
<dt>
<dd> &bull; <a href="git://host.xz[:port]/path/to/repo.git/">git://host.xz[:port]/path/to/repo.git/</a></dl>
<dl>
<dt>
<dd> &bull; http[s]://host.xz[:port]/path/to/repo.git/</dl>
<dl>
<dt>
<dd> &bull; ftp[s]://host.xz[:port]/path/to/repo.git/</dl>
<p> An alternative scp-like syntax may also be used with the ssh protocol: </p>
<dl>
<dt>
<dd> &bull; [user@]host.xz:path/to/repo.git/</dl>
<p> This syntax is only recognized if there are no slashes before the first colon. This helps differentiate a local path that contains a colon. For example the local path <code>foo:bar</code> could be specified as an absolute path or <code>./foo:bar</code> to avoid being misinterpreted as an ssh url. </p>
<p> The ssh and git protocols additionally support ~username expansion: </p>
<dl>
<dt>
<dd> &bull; <a href="ssh://[user@]host.xz[:port]/~[user]/path/to/repo.git/">ssh://[user@]host.xz[:port]/~[user]/path/to/repo.git/</a></dl>
<dl>
<dt>
<dd> &bull; <a href="git://host.xz[:port]/~[user]/path/to/repo.git/">git://host.xz[:port]/~[user]/path/to/repo.git/</a></dl>
<dl>
<dt>
<dd> &bull; [user@]host.xz:/~[user]/path/to/repo.git/</dl>
<p> For local repositories, also supported by Git natively, the following syntaxes may be used: </p>
<dl>
<dt>
<dd> &bull; /path/to/repo.git/</dl>
<dl>
<dt>
<dd> &bull; file:///path/to/repo.git/</dl>
<p> These two syntaxes are mostly equivalent, except the former implies &#8211;local option. </p>
<p> <i>git clone</i>, <i>git fetch</i> and <i>git pull</i>, but not <i>git push</i>, will also accept a suitable bundle file. See <code><a href="/docs/linux/man/1-git-bundle/">git-bundle</a></code>(1). </p>
<p> When Git doesn&#8217;t know how to handle a certain transport protocol, it attempts to use the <i>remote-&lt;transport&gt;</i> remote helper, if one exists. To explicitly request a remote helper, the following syntax may be used: </p>
<dl>
<dt>
<dd> &bull; &lt;transport&gt;::&lt;address&gt;</dl>
<p> where &lt;address&gt; may be a path, a server and path, or an arbitrary URL-like string recognized by the specific remote helper being invoked. See <code><a href="/docs/linux/man/7-gitremote-helpers/">gitremote-helpers</a></code>(7) for details. </p>
<p> If there are a large number of similarly-named remote repositories and you want to use a different format for them (such that the URLs you use will be rewritten into URLs that work), you can create a configuration section of the form: </p>
<dl>
<dt>
<dd>
<pre>
        [url &quot;&lt;actual url base&gt;&quot;]
                insteadOf = &lt;other url base&gt;
</pre>
</dl>
<p> For example, with this: </p>
<dl>
<dt>
<dd>
<pre>
        [url &quot;<a href="git://git.host.xz/">git://git.host.xz/</a>&quot;]
                insteadOf = host.xz:/path/to/
                insteadOf = work:
</pre>
</dl>
<p> a URL like &quot;work:repo.git&quot; or like &quot;host.xz:/path/to/repo.git&quot; will be rewritten in any context that takes a URL to be &quot;<a href="git://git.host.xz/repo.git">git://git.host.xz/repo.git</a>&quot;. </p>
<p> If you want to rewrite URLs for push only, you can create a configuration section of the form: </p>
<dl>
<dt>
<dd>
<pre>
        [url &quot;&lt;actual url base&gt;&quot;]
                pushInsteadOf = &lt;other url base&gt;
</pre>
</dl>
<p> For example, with this: </p>
<dl>
<dt>
<dd>
<pre>
        [url &quot;<a href="ssh://example.org/">ssh://example.org/</a>&quot;]
                pushInsteadOf = <a href="git://example.org/">git://example.org/</a>
</pre>
</dl>
<p> a URL like &quot;<a href="git://example.org/path/to/repo.git">git://example.org/path/to/repo.git</a>&quot; will be rewritten to &quot;<a href="ssh://example.org/path/to/repo.git">ssh://example.org/path/to/repo.git</a>&quot; for pushes, but pulls will still use the original URL.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Clone from upstream: </p>
<dl>
<dt>
<dd>
<pre>
$ git clone <a href="git://git.kernel.org/pub/scm/.../linux.git">git://git.kernel.org/pub/scm/.../linux.git</a> my-linux
$ cd my-linux
$ make
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Make a local clone that borrows from the current directory, without checking things out: </p>
<dl>
<dt>
<dd>
<pre>
$ git clone -l -s -n . ../copy
$ cd ../copy
$ git show-branch
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Clone from upstream while borrowing from an existing local directory: </p>
<dl>
<dt>
<dd>
<pre>
$ git clone --reference /git/linux.git \
        <a href="git://git.kernel.org/pub/scm/.../linux.git">git://git.kernel.org/pub/scm/.../linux.git</a> \
        my-linux
$ cd my-linux
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Create a bare repository to publish your changes to the public: </p>
<dl>
<dt>
<dd>
<pre>
$ git clone --bare -l /home/proj/.git /pub/scm/proj.git
</pre>
</dl>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
