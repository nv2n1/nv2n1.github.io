---
title: "git-init(1)"
name: "git-init"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-init/"
description: "git-init – Create an empty Git repository or reinitialize an existing one"
---

<h2 class="name">NAME</h2>
<p> git-init &#8211; Create an empty Git repository or reinitialize an existing one </p>
<h2>SYNOPSIS</h2>
<pre><code>
git init[-q | --quiet][--bare][--template = &lt;template_directory&gt;]
        [--separate - git - dir&lt;git dir&gt;][--object - format = &lt;format&gt;]
        [-b&lt;branch - name&gt; | --initial - branch = &lt;branch - name&gt;]
        [--shared[=&lt;permissions&gt;]][directory]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command creates an empty Git repository &#8211; basically a <code>.git</code> directory with subdirectories for <code>objects</code>, <code>refs/heads</code>, <code>refs/tags</code>, and template files. An initial branch without any commits will be created (see the <code>&#8211;initial-branch</code> option below for its name). </p>
<p> If the <code>$GIT_DIR</code> environment variable is set then it specifies a path to use instead of <code>./.git</code> for the base of the repository. </p>
<p> If the object storage directory is specified via the <code>$GIT_OBJECT_DIRECTORY</code> environment variable then the sha1 directories are created underneath &#8211; otherwise the default <code>$GIT_DIR/objects</code> directory is used. </p>
<p> Running <i>git init</i> in an existing repository is safe. It will not overwrite things that are already there. The primary reason for rerunning <i>git init</i> is to pick up newly added templates (or to move the repository to another place if &#8211;separate-git-dir is given).</p>
<h2>OPTIONS</h2>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Only print error and warning messages; all other output will be suppressed.</dl>
<p> &#8211;bare</p>
<dl>
<dt>
<dd> Create a bare repository. If <code>GIT_DIR</code> environment is not set, it is set to the current working directory.</dl>
<p> &#8211;object-format=&lt;format&gt;</p>
<dl>
<dt>
<dd> Specify the given object format (hash algorithm) for the repository. The valid values are <i>sha1</i> and (if enabled) <i>sha256</i>. <i>sha1</i> is the default. </p>
<p> THIS OPTION IS EXPERIMENTAL! SHA-256 support is experimental and still in an early stage. A SHA-256 repository will in general not be able to share work with &quot;regular&quot; SHA-1 repositories. It should be assumed that, e.g., Git internal file formats in relation to SHA-256 repositories may change in backwards-incompatible ways. Only use <code>&#8211;object-format=sha256</code> for testing purposes.</dl>
<p> &#8211;template=&lt;template_directory&gt;</p>
<dl>
<dt>
<dd> Specify the directory from which templates will be used. (See the &quot;TEMPLATE DIRECTORY&quot; section below.)</dl>
<p> &#8211;separate-git-dir=&lt;git dir&gt;</p>
<dl>
<dt>
<dd> Instead of initializing the repository as a directory to either <code>$GIT_DIR</code> or <code>./.git/</code>, create a text file there containing the path to the actual repository. This file acts as filesystem-agnostic Git symbolic link to the repository. </p>
<p> If this is reinitialization, the repository will be moved to the specified path.</dl>
<p> -b &lt;branch-name&gt;, &#8211;initial-branch=&lt;branch-name&gt;</p>
<dl>
<dt>
<dd> Use the specified name for the initial branch in the newly created repository. If not specified, fall back to the default name (currently <code>master</code>, but this is subject to change in the future; the name can be customized via the <code>init.defaultBranch</code> configuration variable).</dl>
<p> &#8211;shared[=(false|true|umask|group|all|world|everybody|0xxx)]</p>
<dl>
<dt>
<dd> Specify that the Git repository is to be shared amongst several users. This allows users belonging to the same group to push into that repository. When specified, the config variable &quot;core.sharedRepository&quot; is set so that files and directories under <code>$GIT_DIR</code> are created with the requested permissions. When not specified, Git will use permissions reported by <a href="/docs/linux/man/2-umask/">umask</a>(2). </p>
<p> The option can have the following values, defaulting to <i>group</i> if no value is given: </p>
<p> <i>umask</i> (or <i>false</i>)</p>
<dl>
<dt>
<dd> Use permissions reported by <a href="/docs/linux/man/2-umask/">umask</a>(2). The default, when <code>&#8211;shared</code> is not specified.</dl>
<p> <i>group</i> (or <i>true</i>)</p>
<dl>
<dt>
<dd> Make the repository group-writable, (and g+sx, since the git group may be not the primary group of all users). This is used to loosen the permissions of an otherwise safe <a href="/docs/linux/man/2-umask/">umask</a>(2) value. Note that the umask still applies to the other permission bits (e.g. if umask is <i>0022</i>, using <i>group</i> will not remove read privileges from other (non-group) users). See <i>0xxx</i> for how to exactly specify the repository permissions.</dl>
<p> <i>all</i> (or <i>world</i> or <i>everybody</i>)</p>
<dl>
<dt>
<dd> Same as <i>group</i>, but make the repository readable by all users.</dl>
<p> <i>0xxx</i></p>
<dl>
<dt>
<dd> <i>0xxx</i> is an octal number and each file will have mode <i>0xxx</i>. <i>0xxx</i> will override users&#8217; <a href="/docs/linux/man/2-umask/">umask</a>(2) value (and not only loosen permissions as <i>group</i> and <i>all</i> does). <i>0640</i> will create a repository which is group-readable, but not group-writable or accessible to others. <i>0660</i> will create a repo that is readable and writable to the current user and group, but inaccessible to others.</dl>
</dl>
<p> By default, the configuration flag <code>receive.denyNonFastForwards</code> is enabled in shared repositories, so that you cannot force a non fast-forwarding push into it. </p>
<p> If you provide a <i>directory</i>, the command is run inside it. If this directory does not exist, it will be created.</p>
<h2>TEMPLATE DIRECTORY</h2>
<p> Files and directories in the template directory whose name do not start with a dot will be copied to the <code>$GIT_DIR</code> after it is created. </p>
<p> The template directory will be one of the following (in order): </p>
<dl>
<dt>
<dd> &bull; the argument given with the <code>&#8211;template</code> option;</dl>
<dl>
<dt>
<dd> &bull; the contents of the <code>$GIT_TEMPLATE_DIR</code> environment variable;</dl>
<dl>
<dt>
<dd> &bull; the <code>init.templateDir</code> configuration variable; or</dl>
<dl>
<dt>
<dd> &bull; the default template directory: <code>/usr/share/git-core/templates</code>.</dl>
<p> The default template directory includes some directory structure, suggested &quot;exclude patterns&quot; (see <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)), and sample hook files. </p>
<p> The sample hooks are all disabled by default. To enable one of the sample hooks rename it by removing its <code>.sample</code> suffix. </p>
<p> See <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5) for more general info on hook execution.</p>
<h2>EXAMPLES</h2>
<p> Start a new Git repository for an existing code base</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ cd /path/to/my/codebase
$ git init      <code>(1)</code>
$ git add .     <code>(2)</code>
$ git commit    <code>(3)</code>
</pre>
</dl>
<p> <code>1. </code>Create a /path/to/my/codebase/.git directory.<br />
 <code>2. </code>Add all existing files to the index.<br />
 <code>3. </code>Record the pristine state as the first commit in the history.
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
