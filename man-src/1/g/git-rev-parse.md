---
title: "git-rev-parse(1)"
name: "git-rev-parse"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-rev-parse/"
description: "git-rev-parse – Pick out and massage parameters"
---

<h2 class="name">NAME</h2>
<p> git-rev-parse &#8211; Pick out and massage parameters </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git rev-parse</i> [&lt;options&gt;] &lt;args&gt;...
</pre>
<h2>DESCRIPTION</h2>
<p> Many Git porcelainish commands take mixture of flags (i.e. parameters that begin with a dash <i>&#8211;</i>) and parameters meant for the underlying <i>git rev-list</i> command they use internally and flags and parameters for the other commands they use downstream of <i>git rev-list</i>. This command is used to distinguish between them.</p>
<h2>OPTIONS</h2>
<h3>Operation Modes</h3>
<p> Each of these options must appear first on the command line. </p>
<p> &#8211;parseopt</p>
<dl>
<dt>
<dd> Use <i>git rev-parse</i> in option parsing mode (see PARSEOPT section below).</dl>
<p> &#8211;sq-quote</p>
<dl>
<dt>
<dd> Use <i>git rev-parse</i> in shell quoting mode (see SQ-QUOTE section below). In contrast to the <code>&#8211;sq</code> option below, this mode does only quoting. Nothing else is done to command input.</dl>
<h3>Options for &#8211;parseopt</h3>
<p> &#8211;keep-dashdash</p>
<dl>
<dt>
<dd> Only meaningful in <code>&#8211;parseopt</code> mode. Tells the option parser to echo out the first <code>&#8212;</code> met instead of skipping it.</dl>
<p> &#8211;stop-at-non-option</p>
<dl>
<dt>
<dd> Only meaningful in <code>&#8211;parseopt</code> mode. Lets the option parser stop at the first non-option argument. This can be used to parse sub-commands that take options themselves.</dl>
<p> &#8211;stuck-long</p>
<dl>
<dt>
<dd> Only meaningful in <code>&#8211;parseopt</code> mode. Output the options in their long form if available, and with their arguments stuck.</dl>
<h3>Options for Filtering</h3>
<p> &#8211;revs-only</p>
<dl>
<dt>
<dd> Do not output flags and parameters not meant for <i>git rev-list</i> command.</dl>
<p> &#8211;no-revs</p>
<dl>
<dt>
<dd> Do not output flags and parameters meant for <i>git rev-list</i> command.</dl>
<p> &#8211;flags</p>
<dl>
<dt>
<dd> Do not output non-flag parameters.</dl>
<p> &#8211;no-flags</p>
<dl>
<dt>
<dd> Do not output flag parameters.</dl>
<h3>Options for Output</h3>
<p> &#8211;default &lt;arg&gt;</p>
<dl>
<dt>
<dd> If there is no parameter given by the user, use <code>&lt;arg&gt;</code> instead.</dl>
<p> &#8211;prefix &lt;arg&gt;</p>
<dl>
<dt>
<dd> Behave as if <i>git rev-parse</i> was invoked from the <code>&lt;arg&gt;</code> subdirectory of the working tree. Any relative filenames are resolved as if they are prefixed by <code>&lt;arg&gt;</code> and will be printed in that form. </p>
<p> This can be used to convert arguments to a command run in a subdirectory so that they can still be used after moving to the top-level of the repository. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
prefix = $(git rev - parse-- show - prefix)
    cd "$(git rev-parse --show-toplevel)"
#rev - parse provides the-- needed for 'set'
    eval "set $(git rev-parse --sq --prefix " $prefix " -- " $ @")"
</code></pre>
</dl>
</dl>
<p> &#8211;verify</p>
<dl>
<dt>
<dd> Verify that exactly one parameter is provided, and that it can be turned into a raw 20-byte SHA-1 that can be used to access the object database. If so, emit it to the standard output; otherwise, error out. </p>
<p> If you want to make sure that the output actually names an object in your object database and/or can be used as a specific type of object you require, you can add the <code>^{type}</code> peeling operator to the parameter. For example, <code>git rev-parse &quot;$VAR^{commit}&quot;</code> will make sure <code>$VAR</code> names an existing object that is a commit-ish (i.e. a commit, or an annotated tag that points at a commit). To make sure that <code>$VAR</code> names an existing object of any type, <code>git rev-parse &quot;$VAR^{object}&quot;</code> can be used. </p>
<p> Note that if you are verifying a name from an untrusted source, it is wise to use <code>&#8211;end-of-options</code> so that the name argument is not mistaken for another option.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Only meaningful in <code>&#8211;verify</code> mode. Do not output an error message if the first argument is not a valid object name; instead exit with non-zero status silently. SHA-1s for valid object names are printed to stdout on success.</dl>
<p> &#8211;sq</p>
<dl>
<dt>
<dd> Usually the output is made one line per flag and parameter. This option makes output a single line, properly quoted for consumption by shell. Useful when you expect your parameter to contain whitespaces and newlines (e.g. when using pickaxe <code>-S</code> with <i>git diff-*</i>). In contrast to the <code>&#8211;sq-quote</code> option, the command input is still interpreted as usual.</dl>
<p> &#8211;short[=length]</p>
<dl>
<dt>
<dd> Same as <code>&#8211;verify</code> but shortens the object name to a unique prefix with at least <code>length</code> characters. The minimum length is 4, the default is the effective value of the <code>core.abbrev</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> &#8211;not</p>
<dl>
<dt>
<dd> When showing object names, prefix them with <i>^</i> and strip <i>^</i> prefix from the object names that already have one.</dl>
<p> &#8211;abbrev-ref[=(strict|loose)]</p>
<dl>
<dt>
<dd> A non-ambiguous short name of the objects name. The option core.warnAmbiguousRefs is used to select the strict abbreviation mode.</dl>
<p> &#8211;symbolic</p>
<dl>
<dt>
<dd> Usually the object names are output in SHA-1 form (with possible <i>^</i> prefix); this option makes them output in a form as close to the original input as possible.</dl>
<p> &#8211;symbolic-full-name</p>
<dl>
<dt>
<dd> This is similar to &#8211;symbolic, but it omits input that are not refs (i.e. branch or tag names; or more explicitly disambiguating &quot;heads/master&quot; form, when you want to name the &quot;master&quot; branch when there is an unfortunately named tag &quot;master&quot;), and show them as full refnames (e.g. &quot;refs/heads/master&quot;).</dl>
<h3>Options for Objects</h3>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Show all refs found in <code>refs/</code>.</dl>
<p> &#8211;branches[=pattern], &#8211;tags[=pattern], &#8211;remotes[=pattern]</p>
<dl>
<dt>
<dd> Show all branches, tags, or remote-tracking branches, respectively (i.e., refs found in <code>refs/heads</code>, <code>refs/tags</code>, or <code>refs/remotes</code>, respectively). </p>
<p> If a <code>pattern</code> is given, only refs matching the given shell glob are shown. If the pattern does not contain a globbing character (<code>?</code>, <code>*</code>, or <code>[</code>), it is turned into a prefix match by appending <code>/*</code>.</dl>
<p> &#8211;glob=pattern</p>
<dl>
<dt>
<dd> Show all refs matching the shell glob pattern <code>pattern</code>. If the pattern does not start with <code>refs/</code>, this is automatically prepended. If the pattern does not contain a globbing character (<code>?</code>, <code>*</code>, or <code>[</code>), it is turned into a prefix match by appending <code>/*</code>.</dl>
<p> &#8211;exclude=&lt;glob-pattern&gt;</p>
<dl>
<dt>
<dd> Do not include refs matching <i>&lt;glob-pattern&gt;</i> that the next <code>&#8211;all</code>, <code>&#8211;branches</code>, <code>&#8211;tags</code>, <code>&#8211;remotes</code>, or <code>&#8211;glob</code> would otherwise consider. Repetitions of this option accumulate exclusion patterns up to the next <code>&#8211;all</code>, <code>&#8211;branches</code>, <code>&#8211;tags</code>, <code>&#8211;remotes</code>, or <code>&#8211;glob</code> option (other options or arguments do not clear accumulated patterns). </p>
<p> The patterns given should not begin with <code>refs/heads</code>, <code>refs/tags</code>, or <code>refs/remotes</code> when applied to <code>&#8211;branches</code>, <code>&#8211;tags</code>, or <code>&#8211;remotes</code>, respectively, and they must begin with <code>refs/</code> when applied to <code>&#8211;glob</code> or <code>&#8211;all</code>. If a trailing <i>/*</i> is intended, it must be given explicitly.</dl>
<p> &#8211;disambiguate=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Show every object whose name begins with the given prefix. The &lt;prefix&gt; must be at least 4 hexadecimal digits long to avoid listing each and every object in the repository by mistake.</dl>
<h3>Options for Files</h3>
<p> &#8211;local-env-vars</p>
<dl>
<dt>
<dd> List the GIT_* environment variables that are local to the repository (e.g. GIT_DIR or GIT_WORK_TREE, but not GIT_EDITOR). Only the names of the variables are listed, not their value, even if they are set.</dl>
<p> &#8211;path-format=(absolute|relative)</p>
<dl>
<dt>
<dd> Controls the behavior of certain other options. If specified as absolute, the paths printed by those options will be absolute and canonical. If specified as relative, the paths will be relative to the current working directory if that is possible. The default is option specific. </p>
<p> This option may be specified multiple times and affects only the arguments that follow it on the command line, either to the end of the command line or the next instance of this option.</dl>
<p> The following options are modified by <code>&#8211;path-format</code>: </p>
<p> &#8211;git-dir</p>
<dl>
<dt>
<dd> Show <code>$GIT_DIR</code> if defined. Otherwise show the path to the .git directory. The path shown, when relative, is relative to the current working directory. </p>
<p> If <code>$GIT_DIR</code> is not defined and the current directory is not detected to lie in a Git repository or work tree print a message to stderr and exit with nonzero status.</dl>
<p> &#8211;git-common-dir</p>
<dl>
<dt>
<dd> Show <code>$GIT_COMMON_DIR</code> if defined, else <code>$GIT_DIR</code>.</dl>
<p> &#8211;resolve-git-dir &lt;path&gt;</p>
<dl>
<dt>
<dd> Check if &lt;path&gt; is a valid repository or a gitfile that points at a valid repository, and print the location of the repository. If &lt;path&gt; is a gitfile then the resolved path to the real repository is printed.</dl>
<p> &#8211;git-path &lt;path&gt;</p>
<dl>
<dt>
<dd> Resolve &quot;$GIT_DIR/&lt;path&gt;&quot; and takes other path relocation variables such as $GIT_OBJECT_DIRECTORY, $GIT_INDEX_FILE&#8230; into account. For example, if $GIT_OBJECT_DIRECTORY is set to /foo/bar then &quot;git rev-parse &#8211;git-path objects/abc&quot; returns /foo/bar/abc.</dl>
<p> &#8211;show-toplevel</p>
<dl>
<dt>
<dd> Show the (by default, absolute) path of the top-level directory of the working tree. If there is no working tree, report an error.</dl>
<p> &#8211;show-superproject-working-tree</p>
<dl>
<dt>
<dd> Show the absolute path of the root of the superproject&#8217;s working tree (if exists) that uses the current repository as its submodule. Outputs nothing if the current repository is not used as a submodule by any project.</dl>
<p> &#8211;shared-index-path</p>
<dl>
<dt>
<dd> Show the path to the shared index file in split index mode, or empty if not in split-index mode.</dl>
<p> The following options are unaffected by <code>&#8211;path-format</code>: </p>
<p> &#8211;absolute-git-dir</p>
<dl>
<dt>
<dd> Like <code>&#8211;git-dir</code>, but its output is always the canonicalized absolute path.</dl>
<p> &#8211;is-inside-git-dir</p>
<dl>
<dt>
<dd> When the current working directory is below the repository directory print &quot;true&quot;, otherwise &quot;false&quot;.</dl>
<p> &#8211;is-inside-work-tree</p>
<dl>
<dt>
<dd> When the current working directory is inside the work tree of the repository print &quot;true&quot;, otherwise &quot;false&quot;.</dl>
<p> &#8211;is-bare-repository</p>
<dl>
<dt>
<dd> When the repository is bare print &quot;true&quot;, otherwise &quot;false&quot;.</dl>
<p> &#8211;is-shallow-repository</p>
<dl>
<dt>
<dd> When the repository is shallow print &quot;true&quot;, otherwise &quot;false&quot;.</dl>
<p> &#8211;show-cdup</p>
<dl>
<dt>
<dd> When the command is invoked from a subdirectory, show the path of the top-level directory relative to the current directory (typically a sequence of &quot;../&quot;, or an empty string).</dl>
<p> &#8211;show-prefix</p>
<dl>
<dt>
<dd> When the command is invoked from a subdirectory, show the path of the current directory relative to the top-level directory.</dl>
<p> &#8211;show-object-format[=(storage|input|output)]</p>
<dl>
<dt>
<dd> Show the object format (hash algorithm) used for the repository for storage inside the <code>.git</code> directory, input, or output. For input, multiple algorithms may be printed, space-separated. If not specified, the default is &quot;storage&quot;.</dl>
<h3>Other Options</h3>
<p> &#8211;since=datestring, &#8211;after=datestring</p>
<dl>
<dt>
<dd> Parse the date string, and output the corresponding &#8211;max-age= parameter for <i>git rev-list</i>.</dl>
<p> &#8211;until=datestring, &#8211;before=datestring</p>
<dl>
<dt>
<dd> Parse the date string, and output the corresponding &#8211;min-age= parameter for <i>git rev-list</i>.</dl>
<p> &lt;args&gt;&#8230;</p>
<dl>
<dt>
<dd> Flags and parameters to be parsed.</dl>
<h2>SPECIFYING REVISIONS</h2>
<p> A revision parameter <i>&lt;rev&gt;</i> typically, but not necessarily, names a commit object. It uses what is called an <i>extended SHA-1</i> syntax. Here are various ways to spell object names. The ones listed near the end of this list name trees and blobs contained in a commit. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> This document shows the &quot;raw&quot; syntax as seen by git. The shell and other UIs might require additional quoting to protect special characters and to avoid word splitting. </p>
</dl>
<p> <i>&lt;sha1&gt;</i>, e.g. <i>dae86e1950b1277e545cee180551750029cfe735</i>, <i>dae86e</i></p>
<dl>
<dt>
<dd> The full SHA-1 object name (40-byte hexadecimal string), or a leading substring that is unique within the repository. E.g. dae86e1950b1277e545cee180551750029cfe735 and dae86e both name the same commit object if there is no other object in your repository whose object name starts with dae86e.</dl>
<p> <i>&lt;describeOutput&gt;</i>, e.g. <i>v1.7.4.2-679-g3bee7fb</i></p>
<dl>
<dt>
<dd> Output from <code>git describe</code>; i.e. a closest tag, optionally followed by a dash and a number of commits, followed by a dash, a <i>g</i>, and an abbreviated object name.</dl>
<p> <i>&lt;refname&gt;</i>, e.g. <i>master</i>, <i>heads/master</i>, <i>refs/heads/master</i></p>
<dl>
<dt>
<dd> A symbolic ref name. E.g. <i>master</i> typically means the commit object referenced by <i>refs/heads/master</i>. If you happen to have both <i>heads/master</i> and <i>tags/master</i>, you can explicitly say <i>heads/master</i> to tell Git which one you mean. When ambiguous, a <i>&lt;refname&gt;</i> is disambiguated by taking the first match in the following rules: </p>
<dl>
<dt>
<dd> 1. If <i>$GIT_DIR/&lt;refname&gt;</i> exists, that is what you mean (this is usually useful only for <code>HEAD</code>, <code>FETCH_HEAD</code>, <code>ORIG_HEAD</code>, <code>MERGE_HEAD</code> and <code>CHERRY_PICK_HEAD</code>);</dl>
<dl>
<dt>
<dd> 2. otherwise, <i>refs/&lt;refname&gt;</i> if it exists;</dl>
<dl>
<dt>
<dd> 3. otherwise, <i>refs/tags/&lt;refname&gt;</i> if it exists;</dl>
<dl>
<dt>
<dd> 4. otherwise, <i>refs/heads/&lt;refname&gt;</i> if it exists;</dl>
<dl>
<dt>
<dd> 5. otherwise, <i>refs/remotes/&lt;refname&gt;</i> if it exists;</dl>
<dl>
<dt>
<dd> 6. otherwise, <i>refs/remotes/&lt;refname&gt;/HEAD</i> if it exists. </p>
<p> <code>HEAD</code> names the commit on which you based the changes in the working tree. <code>FETCH_HEAD</code> records the branch which you fetched from a remote repository with your last <code>git fetch</code> invocation. <code>ORIG_HEAD</code> is created by commands that move your <code>HEAD</code> in a drastic way, to record the position of the <code>HEAD</code> before their operation, so that you can easily change the tip of the branch back to the state before you ran them. <code>MERGE_HEAD</code> records the commit(s) which you are merging into your branch when you run <code>git merge</code>. <code>CHERRY_PICK_HEAD</code> records the commit which you are cherry-picking when you run <code>git cherry-pick</code>. </p>
<p> Note that any of the <i>refs/*</i> cases above may come either from the <code>$GIT_DIR/refs</code> directory or from the <code>$GIT_DIR/packed-refs</code> file. While the ref name encoding is unspecified, UTF-8 is preferred as some output processing may assume ref names in UTF-8.</dl>
</dl>
<p> <i>@</i></p>
<dl>
<dt>
<dd> <i>@</i> alone is a shortcut for <code>HEAD</code>.</dl>
<p> <i>[&lt;refname&gt;]@{&lt;date&gt;}</i>, e.g. <i>master@{yesterday}</i>, <i>HEAD@{5 minutes ago}</i></p>
<dl>
<dt>
<dd> A ref followed by the suffix <i>@</i> with a date specification enclosed in a brace pair (e.g. <i>{yesterday}</i>, <i>{1 month 2 weeks 3 days 1 hour 1 second ago}</i> or <i>{1979-02-26 18:30:00}</i>) specifies the value of the ref at a prior point in time. This suffix may only be used immediately following a ref name and the ref must have an existing log (<i>$GIT_DIR/logs/&lt;ref&gt;</i>). Note that this looks up the state of your <code>local</code> ref at a given time; e.g., what was in your local <i>master</i> branch last week. If you want to look at commits made during certain times, see <code>&#8211;since</code> and <code>&#8211;until</code>.</dl>
<p> <i>&lt;refname&gt;@{&lt;n&gt;}</i>, e.g. <i>master@{1}</i></p>
<dl>
<dt>
<dd> A ref followed by the suffix <i>@</i> with an ordinal specification enclosed in a brace pair (e.g. <i>{1}</i>, <i>{15}</i>) specifies the n-th prior value of that ref. For example <i>master@{1}</i> is the immediate prior value of <i>master</i> while <i>master@{5}</i> is the 5th prior value of <i>master</i>. This suffix may only be used immediately following a ref name and the ref must have an existing log (<i>$GIT_DIR/logs/&lt;refname&gt;</i>).</dl>
<p> <i>@{&lt;n&gt;}</i>, e.g. <i>@{1}</i></p>
<dl>
<dt>
<dd> You can use the <i>@</i> construct with an empty ref part to get at a reflog entry of the current branch. For example, if you are on branch <i>blabla</i> then <i>@{1}</i> means the same as <i>blabla@{1}</i>.</dl>
<p> <i>@{-&lt;n&gt;}</i>, e.g. <i>@{-1}</i></p>
<dl>
<dt>
<dd> The construct <i>@{-&lt;n&gt;}</i> means the &lt;n&gt;th branch/commit checked out before the current one.</dl>
<p> <i>[&lt;branchname&gt;]@{upstream}</i>, e.g. <i>master@{upstream}</i>, <i>@{u}</i></p>
<dl>
<dt>
<dd> The suffix <i>@{upstream}</i> to a branchname (short form <i>&lt;branchname&gt;@{u}</i>) refers to the branch that the branch specified by branchname is set to build on top of (configured with <code>branch.&lt;name&gt;.remote</code> and <code>branch.&lt;name&gt;.merge</code>). A missing branchname defaults to the current one. These suffixes are also accepted when spelled in uppercase, and they mean the same thing no matter the case.</dl>
<p> <i>[&lt;branchname&gt;]@{push}</i>, e.g. <i>master@{push}</i>, <i>@{push}</i></p>
<dl>
<dt>
<dd> The suffix <i>@{push}</i> reports the branch &quot;where we would push to&quot; if <code>git push</code> were run while <code>branchname</code> was checked out (or the current <code>HEAD</code> if no branchname is specified). Since our push destination is in a remote repository, of course, we report the local tracking branch that corresponds to that branch (i.e., something in <code>refs/remotes/</code>). </p>
<p> Here&#8217;s an example to make it more clear: </p>
<dl>
<dt>
<dd>
$ git config push.default current<br />
        $ git config remote.pushdefault myfork<br />
            $ git switch &#8211;<br />
    c mybranch origin / master<br />
                            $ git rev &#8211;<br />
    parse&#8211; symbolic &#8211; full &#8211; name @{upstream} refs / remotes / origin / master $ git rev &#8211; parse&#8211; symbolic &#8211; full &#8211; name @{push} refs / remotes / myfork / mybranch
</dl>
<p> Note in the example that we set up a triangular workflow, where we pull from one location and push to another. In a non-triangular workflow, <i>@{push}</i> is the same as <i>@{upstream}</i>, and there is no need for it. </p>
<p> This suffix is also accepted when spelled in uppercase, and means the same thing no matter the case.</dl>
<p> <i>&lt;rev&gt;^[&lt;n&gt;]</i>, e.g. <i>HEAD^, v1.5.1^0</i></p>
<dl>
<dt>
<dd> A suffix <i>^</i> to a revision parameter means the first parent of that commit object. <i>^&lt;n&gt;</i> means the &lt;n&gt;th parent (i.e. <i>&lt;rev&gt;^</i> is equivalent to <i>&lt;rev&gt;^1</i>). As a special rule, <i>&lt;rev&gt;^0</i> means the commit itself and is used when <i>&lt;rev&gt;</i> is the object name of a tag object that refers to a commit object.</dl>
<p> <i>&lt;rev&gt;~[&lt;n&gt;]</i>, e.g. <i>HEAD~, master~3</i></p>
<dl>
<dt>
<dd> A suffix <i>~</i> to a revision parameter means the first parent of that commit object. A suffix <i>~&lt;n&gt;</i> to a revision parameter means the commit object that is the &lt;n&gt;th generation ancestor of the named commit object, following only the first parents. I.e. <i>&lt;rev&gt;~3</i> is equivalent to <i>&lt;rev&gt;^^^</i> which is equivalent to <i>&lt;rev&gt;^1^1^1</i>. See below for an illustration of the usage of this form.</dl>
<p> <i>&lt;rev&gt;^{&lt;type&gt;}</i>, e.g. <i>v0.99.8^{commit}</i></p>
<dl>
<dt>
<dd> A suffix <i>^</i> followed by an object type name enclosed in brace pair means dereference the object at <i>&lt;rev&gt;</i> recursively until an object of type <i>&lt;type&gt;</i> is found or the object cannot be dereferenced anymore (in which case, barf). For example, if <i>&lt;rev&gt;</i> is a commit-ish, <i>&lt;rev&gt;^{commit}</i> describes the corresponding commit object. Similarly, if <i>&lt;rev&gt;</i> is a tree-ish, <i>&lt;rev&gt;^{tree}</i> describes the corresponding tree object. <i>&lt;rev&gt;^0</i> is a short-hand for <i>&lt;rev&gt;^{commit}</i>. </p>
<p> <i>&lt;rev&gt;^{object}</i> can be used to make sure <i>&lt;rev&gt;</i> names an object that exists, without requiring <i>&lt;rev&gt;</i> to be a tag, and without dereferencing <i>&lt;rev&gt;</i>; because a tag is already an object, it does not have to be dereferenced even once to get to an object. </p>
<p> <i>&lt;rev&gt;^{tag}</i> can be used to ensure that <i>&lt;rev&gt;</i> identifies an existing tag object.</dl>
<p> <i>&lt;rev&gt;^{}</i>, e.g. <i>v0.99.8^{}</i></p>
<dl>
<dt>
<dd> A suffix <i>^</i> followed by an empty brace pair means the object could be a tag, and dereference the tag recursively until a non-tag object is found.</dl>
<p> <i>&lt;rev&gt;^{/&lt;text&gt;}</i>, e.g. <i>HEAD^{/fix nasty bug}</i></p>
<dl>
<dt>
<dd> A suffix <i>^</i> to a revision parameter, followed by a brace pair that contains a text led by a slash, is the same as the <i>:/fix nasty bug</i> syntax below except that it returns the youngest matching commit which is reachable from the <i>&lt;rev&gt;</i> before <i>^</i>.</dl>
<p> <i>:/&lt;text&gt;</i>, e.g. <i>:/fix nasty bug</i></p>
<dl>
<dt>
<dd> A colon, followed by a slash, followed by a text, names a commit whose commit message matches the specified regular expression. This name returns the youngest matching commit which is reachable from any ref, including HEAD. The regular expression can match any part of the commit message. To match messages starting with a string, one can use e.g. <i>:/^foo</i>. The special sequence <i>:/!</i> is reserved for modifiers to what is matched. <i>:/!-foo</i> performs a negative match, while <i>:/!!foo</i> matches a literal <i>!</i> character, followed by <i>foo</i>. Any other sequence beginning with <i>:/!</i> is reserved for now. Depending on the given text, the shell&#8217;s word splitting rules might require additional quoting.</dl>
<p> <i>&lt;rev&gt;:&lt;path&gt;</i>, e.g. <i>HEAD:README</i>, <i>master:./README</i></p>
<dl>
<dt>
<dd> A suffix <i>:</i> followed by a path names the blob or tree at the given path in the tree-ish object named by the part before the colon. A path starting with <i>./</i> or <i>../</i> is relative to the current working directory. The given path will be converted to be relative to the working tree&#8217;s root directory. This is most useful to address a blob or tree from a commit or tree that has the same tree structure as the working tree.</dl>
<p> <i>:[&lt;n&gt;:]&lt;path&gt;</i>, e.g. <i>:0:README</i>, <i>:README</i></p>
<dl>
<dt>
<dd> A colon, optionally followed by a stage number (0 to 3) and a colon, followed by a path, names a blob object in the index at the given path. A missing stage number (and the colon that follows it) names a stage 0 entry. During a merge, stage 1 is the common ancestor, stage 2 is the target branch&#8217;s version (typically the current branch), and stage 3 is the version from the branch which is being merged.</dl>
<p> Here is an illustration, by Jon Loeliger. Both commit nodes B and C are parents of commit node A. Parent commits are ordered left-to-right. </p>
<dl>
<dt>
<dd>
<pre>
G   H   I   J
 \ /     \ /
  D   E   F
   \  |  / \
    \ | /   |
     \|/    |
      B     C
       \   /
        \ /
         A
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
A =      = A^0
B = A^   = A^1     = A~1
C =      = A^2
D = A^^  = A^1^1   = A~2
E = B^2  = A^^2
F = B^3  = A^^3
G = A^^^ = A^1^1^1 = A~3
H = D^2  = B^^2    = A^^^2  = A~2^2
I = F^   = B^3^    = A^^3^
J = F^2  = B^3^2   = A^^3^2
</pre>
</dl>
<h2>SPECIFYING RANGES</h2>
<p> History traversing commands such as <code>git log</code> operate on a set of commits, not just a single commit. </p>
<p> For these commands, specifying a single revision, using the notation described in the previous section, means the set of commits <code>reachable</code> from the given commit. </p>
<p> Specifying several revisions means the set of commits reachable from any of the given commits. </p>
<p> A commit&#8217;s reachable set is the commit itself and the commits in its ancestry chain. </p>
<p> There are several notations to specify a set of connected commits (called a &quot;revision range&quot;), illustrated below.</p>
<h3>Commit Exclusions</h3>
<p> <i>^&lt;rev&gt;</i> (caret) Notation</p>
<dl>
<dt>
<dd> To exclude commits reachable from a commit, a prefix <i>^</i> notation is used. E.g. <i>^r1 r2</i> means commits reachable from <i>r2</i> but exclude the ones reachable from <i>r1</i> (i.e. <i>r1</i> and its ancestors).</dl>
<h3>Dotted Range Notations</h3>
<p> The <i>..</i> (two-dot) Range Notation</p>
<dl>
<dt>
<dd> The <i>^r1 r2</i> set operation appears so often that there is a shorthand for it. When you have two commits <i>r1</i> and <i>r2</i> (named according to the syntax explained in SPECIFYING REVISIONS above), you can ask for commits that are reachable from r2 excluding those that are reachable from r1 by <i>^r1 r2</i> and it can be written as <i>r1..r2</i>.</dl>
<p> The <i>&#8230;</i> (three-dot) Symmetric Difference Notation</p>
<dl>
<dt>
<dd> A similar notation <i>r1&#8230;r2</i> is called symmetric difference of <i>r1</i> and <i>r2</i> and is defined as <i>r1 r2 &#8211;not $(git merge-base &#8211;all r1 r2)</i>. It is the set of commits that are reachable from either one of <i>r1</i> (left side) or <i>r2</i> (right side) but not from both.</dl>
<p> In these two shorthand notations, you can omit one end and let it default to HEAD. For example, <i>origin..</i> is a shorthand for <i>origin..HEAD</i> and asks &quot;What did I do since I forked from the origin branch?&quot; Similarly, <i>..origin</i> is a shorthand for <i>HEAD..origin</i> and asks &quot;What did the origin do since I forked from them?&quot; Note that <i>..</i> would mean <i>HEAD..HEAD</i> which is an empty range that is both reachable and unreachable from HEAD. </p>
<p> Commands that are specifically designed to take two distinct ranges (e.g. &quot;git range-diff R1 R2&quot; to compare two ranges) do exist, but they are exceptions. Unless otherwise noted, all &quot;git&quot; commands that operate on a set of commits work on a single revision range. In other words, writing two &quot;two-dot range notation&quot; next to each other, e.g. </p>
<dl>
<dt>
<dd>
<pre>
$ git log A..B C..D
</pre>
</dl>
<p> does <code>not</code> specify two revision ranges for most commands. Instead it will name a single connected set of commits, i.e. those that are reachable from either B or D but are reachable from neither A or C. In a linear history like this: </p>
<dl>
<dt>
<dd>
&#8212; -A&#8211; &#8211; B&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; C&#8211; &#8211; D
</dl>
<p> because A and B are reachable from C, the revision range specified by these two dotted ranges is a single commit D.</p>
<h3>Other &lt;rev&gt;^ Parent Shorthand Notations</h3>
<p> Three other shorthands exist, particularly useful for merge commits, for naming a set that is formed by a commit and its parent commits. </p>
<p> The <i>r1^@</i> notation means all parents of <i>r1</i>. </p>
<p> The <i>r1^!</i> notation includes commit <i>r1</i> but excludes all of its parents. By itself, this notation denotes the single commit <i>r1</i>. </p>
<p> The <i>&lt;rev&gt;^-[&lt;n&gt;]</i> notation includes <i>&lt;rev&gt;</i> but excludes the &lt;n&gt;th parent (i.e. a shorthand for <i>&lt;rev&gt;^&lt;n&gt;..&lt;rev&gt;</i>), with <i>&lt;n&gt;</i> = 1 if not given. This is typically useful for merge commits where you can just pass <i>&lt;commit&gt;^-</i> to get all the commits in the branch that was merged in merge commit <i>&lt;commit&gt;</i> (including <i>&lt;commit&gt;</i> itself). </p>
<p> While <i>&lt;rev&gt;^&lt;n&gt;</i> was about specifying a single commit parent, these three notations also consider its parents. For example you can say <i>HEAD^2^@</i>, however you cannot say <i>HEAD^@^2</i>.</p>
<h2>REVISION RANGE SUMMARY</h2>
<p> <i>&lt;rev&gt;</i></p>
<dl>
<dt>
<dd> Include commits that are reachable from &lt;rev&gt; (i.e. &lt;rev&gt; and its ancestors).</dl>
<p> <i>^&lt;rev&gt;</i></p>
<dl>
<dt>
<dd> Exclude commits that are reachable from &lt;rev&gt; (i.e. &lt;rev&gt; and its ancestors).</dl>
<p> <i>&lt;rev1&gt;..&lt;rev2&gt;</i></p>
<dl>
<dt>
<dd> Include commits that are reachable from &lt;rev2&gt; but exclude those that are reachable from &lt;rev1&gt;. When either &lt;rev1&gt; or &lt;rev2&gt; is omitted, it defaults to <code>HEAD</code>.</dl>
<p> <i>&lt;rev1&gt;&#8230;&lt;rev2&gt;</i></p>
<dl>
<dt>
<dd> Include commits that are reachable from either &lt;rev1&gt; or &lt;rev2&gt; but exclude those that are reachable from both. When either &lt;rev1&gt; or &lt;rev2&gt; is omitted, it defaults to <code>HEAD</code>.</dl>
<p> <i>&lt;rev&gt;^@</i>, e.g. <i>HEAD^@</i></p>
<dl>
<dt>
<dd> A suffix <i>^</i> followed by an at sign is the same as listing all parents of <i>&lt;rev&gt;</i> (meaning, include anything reachable from its parents, but not the commit itself).</dl>
<p> <i>&lt;rev&gt;^!</i>, e.g. <i>HEAD^!</i></p>
<dl>
<dt>
<dd> A suffix <i>^</i> followed by an exclamation mark is the same as giving commit <i>&lt;rev&gt;</i> and then all its parents prefixed with <i>^</i> to exclude them (and their ancestors).</dl>
<p> <i>&lt;rev&gt;^-&lt;n&gt;</i>, e.g. <i>HEAD^-, HEAD^-2</i></p>
<dl>
<dt>
<dd> Equivalent to <i>&lt;rev&gt;^&lt;n&gt;..&lt;rev&gt;</i>, with <i>&lt;n&gt;</i> = 1 if not given.</dl>
<p> Here are a handful of examples using the Loeliger illustration above, with each step in the notation&#8217;s expansion and selection carefully spelt out: </p>
<dl>
<dt>
<dd>
<pre>
   Args   Expanded arguments    Selected commits
   D                            G H D
   D F                          G H I J D F
   ^G D                         H D
   ^D B                         E I J F B
   ^D B C                       E I J F B C
   C                            I J F C
   B..C   = ^B C                C
   B...C  = B ^F C              G H D E B C
   B^-    = B^..B
          = ^B^1 B              E I J F B
   C^@    = C^1
          = F                   I J F
   B^@    = B^1 B^2 B^3
          = D E F               D G H E F I J
   C^!    = C ^C^@
          = C ^C^1
          = C ^F                C
   B^!    = B ^B^@
          = B ^B^1 ^B^2 ^B^3
          = B ^D ^E ^F          B
   F^! D  = F ^I ^J D           G H D F
</pre>
</dl>
<h2>PARSEOPT</h2>
<p> In <code>&#8211;parseopt</code> mode, <i>git rev-parse</i> helps massaging options to bring to shell scripts the same facilities C builtins have. It works as an option normalizer (e.g. splits single switches aggregate values), a bit like <code><a href="/docs/linux/man/1-getopt/">getopt</a>(1)</code> does. </p>
<p> It takes on the standard input the specification of the options to parse and understand, and echoes on the standard output a string suitable for <code><a href="/docs/linux/man/1-sh/">sh</a>(1)</code> <code>eval</code> to replace the arguments with normalized ones. In case of error, it outputs usage on the standard error stream, and exits with code 129. </p>
<p> Note: Make sure you quote the result when passing it to <code>eval</code>. See below for an example.</p>
<h3>Input Format</h3>
<p> <i>git rev-parse &#8211;parseopt</i> input format is fully text based. It has two parts, separated by a line that contains only <code>&#8212;</code>. The lines before the separator (should be one or more) are used for the usage. The lines after the separator describe the options. </p>
<p> Each line of options has this format: </p>
<dl>
<dt>
<dd>
<pre>
&lt;opt-spec&gt;&lt;flags&gt;*&lt;arg-hint&gt;? SP+ help LF
</pre>
</dl>
<p> <code>&lt;opt-spec&gt;</code></p>
<dl>
<dt>
<dd> its format is the short option character, then the long option name separated by a comma. Both parts are not required, though at least one is necessary. May not contain any of the <code>&lt;flags&gt;</code> characters. <code>h,help</code>, <code>dry-run</code> and <code>f</code> are examples of correct <code>&lt;opt-spec&gt;</code>.</dl>
<p> <code>&lt;flags&gt;</code></p>
<dl>
<dt>
<dd> <code>&lt;flags&gt;</code> are of <code>*</code>, <code>=</code>, <code>?</code> or <code>!</code>. </p>
<dl>
<dt>
<dd> &bull; Use <code>=</code> if the option takes an argument.</dl>
<dl>
<dt>
<dd> &bull; Use <code>?</code> to mean that the option takes an optional argument. You probably want to use the <code>&#8211;stuck-long</code> mode to be able to unambiguously parse the optional argument.</dl>
<dl>
<dt>
<dd> &bull; Use <code>*</code> to mean that this option should not be listed in the usage generated for the <code>-h</code> argument. It&#8217;s shown for <code>&#8211;help-all</code> as documented in <code><a href="/docs/linux/man/7-gitcli/">gitcli</a></code>(7).</dl>
<dl>
<dt>
<dd> &bull; Use <code>!</code> to not make the corresponding negated long option available.</dl>
</dl>
<p> <code>&lt;arg-hint&gt;</code></p>
<dl>
<dt>
<dd> <code>&lt;arg-hint&gt;</code>, if specified, is used as a name of the argument in the help output, for options that take arguments. <code>&lt;arg-hint&gt;</code> is terminated by the first whitespace. It is customary to use a dash to separate words in a multi-word argument hint.</dl>
<p> The remainder of the line, after stripping the spaces, is used as the help associated to the option. </p>
<p> Blank lines are ignored, and lines that don&#8217;t match this specification are used as option group headers (start the line with a space to create such lines on purpose).</p>
<h3>Example</h3>
<dl>
<dt>
<dd>
OPTS_SPEC = &#8220;\<br />
some-command [&lt;options&gt;] &lt;args&gt;&#8230;<br />
                some &#8211;<br />
                command does foo and<br />
            bar !&#8211;h,<br />
    help show the help<br />
        foo some nifty option&#8211; foo<br />
            bar = some cool option&#8211; bar with an argument<br />
                baz = arg another cool option&#8211; baz with a named argument<br />
                    qux<br />
    ? path qux may take a path argument but has meaning by itself<br />
          An option group Header<br />
              C<br />
    ? option C with an optional argument &#8221;<br />
    eval &#8220;$(echo &#8221; $OPTS_SPEC &#8221; | git rev-parse &#8211;parseopt &#8212; &#8221; $ @&#8221; || echo exit $?)&#8221;
</dl>
<h3>Usage text</h3>
<p> When <code>&quot;$@&quot;</code> is <code>-h</code> or <code>&#8211;help</code> in the above example, the following usage text would be shown: </p>
<dl>
<dt>
<dd>
usage : some &#8211; command[&lt;options&gt;]&lt;args&gt;&#8230; some &#8211; command does foo and bar !-h, &#8211;help show the help&#8211; foo some nifty option&#8211; foo&#8211; bar&#8230; some cool option&#8211; bar with an argument&#8211; baz&lt;arg&gt; another cool option&#8211; baz with a named argument&#8211; qux[=&lt;path&gt;] qux may take a path argument but has meaning by itself<br />
                                                                                        An option group Header &#8211;<br />
                                                                                    C[&#8230;] option C with an optional argument
</dl>
<h2>SQ-QUOTE</h2>
<p> In <code>&#8211;sq-quote</code> mode, <i>git rev-parse</i> echoes on the standard output a single line suitable for <code><a href="/docs/linux/man/1-sh/">sh</a>(1)</code> <code>eval</code>. This line is made by normalizing the arguments following <code>&#8211;sq-quote</code>. Nothing other than quoting the arguments is done. </p>
<p> If you want command input to still be interpreted as usual by <i>git rev-parse</i> before the output is shell quoted, see the <code>&#8211;sq</code> option.</p>
<h3>Example</h3>
<dl>
<dt>
<dd>
<pre>
$ cat &gt;your-git-script.sh &lt;&lt;\EOF
#!/bin/sh
args=$(git rev-parse --sq-quote &quot;$@&quot;)   # quote user-supplied arguments
command=&quot;git frotz -n24 $args&quot;          # and use it inside a handcrafted
                                        # command line
eval &quot;$command&quot;
EOF
$ sh your-git-script.sh &quot;a b'c&quot;
</pre>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Print the object name of the current commit: </p>
<dl>
<dt>
<dd>
<pre>
$ git rev-parse --verify HEAD
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Print the commit object name from the revision in the $REV shell variable: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git rev - parse-- verify-- end - of - options $REV ^ { commit }
</code></pre>
</dl>
<p> This will error out if $REV is empty or not a valid revision.</dl>
<dl>
<dt>
<dd> &bull; Similar to above: </p>
<dl>
<dt>
<dd>
<pre>
$ git rev-parse --default master --verify --end-of-options $REV
</pre>
</dl>
<p> but if $REV is empty, the commit object name from master will be printed.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
