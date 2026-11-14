---
title: "git-sh-setup(1)"
name: "git-sh-setup"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-sh-setup/"
description: "git-sh-setup – Common Git shell script setup code"
---

<h2 class="name">NAME</h2>
<p> git-sh-setup &#8211; Common Git shell script setup code </p>
<h2>SYNOPSIS</h2>
<pre>
<i>. &quot;$(git --exec-path)/git-sh-setup&quot;</i>
</pre>
<h2>DESCRIPTION</h2>
<p> This is not a command the end user would want to run. Ever. This documentation is meant for people who are studying the Porcelain-ish scripts and/or are writing new ones. </p>
<p> The <i>git sh-setup</i> scriptlet is designed to be sourced (using <code>.</code>) by other shell scripts to set up some variables pointing at the normal Git directories and a few helper shell functions. </p>
<p> Before sourcing it, your script should set up a few variables; <code>USAGE</code> (and <code>LONG_USAGE</code>, if any) is used to define message given by <code>usage()</code> shell function. <code>SUBDIRECTORY_OK</code> can be set if the script can run from a subdirectory of the working tree (some commands do not). </p>
<p> The scriptlet sets <code>GIT_DIR</code> and <code>GIT_OBJECT_DIRECTORY</code> shell variables, but does <code>not</code> export them to the environment.</p>
<h2>FUNCTIONS</h2>
<p> die</p>
<dl>
<dt>
<dd> exit after emitting the supplied error message to the standard error stream.</dl>
<p> usage</p>
<dl>
<dt>
<dd> die with the usage message.</dl>
<p> set_reflog_action</p>
<dl>
<dt>
<dd> Set <code>GIT_REFLOG_ACTION</code> environment to a given string (typically the name of the program) unless it is already set. Whenever the script runs a <code>git</code> command that updates refs, a reflog entry is created using the value of this string to leave the record of what command updated the ref.</dl>
<p> git_editor</p>
<dl>
<dt>
<dd> runs an editor of user&#8217;s choice (GIT_EDITOR, core.editor, VISUAL or EDITOR) on a given file, but error out if no editor is specified and the terminal is dumb.</dl>
<p> is_bare_repository</p>
<dl>
<dt>
<dd> outputs <code>true</code> or <code>false</code> to the standard output stream to indicate if the repository is a bare repository (i.e. without an associated working tree).</dl>
<p> cd_to_toplevel</p>
<dl>
<dt>
<dd> runs chdir to the toplevel of the working tree.</dl>
<p> require_work_tree</p>
<dl>
<dt>
<dd> checks if the current directory is within the working tree of the repository, and otherwise dies.</dl>
<p> require_work_tree_exists</p>
<dl>
<dt>
<dd> checks if the working tree associated with the repository exists, and otherwise dies. Often done before calling cd_to_toplevel, which is impossible to do if there is no working tree.</dl>
<p> require_clean_work_tree &lt;action&gt; [&lt;hint&gt;]</p>
<dl>
<dt>
<dd> checks that the working tree and index associated with the repository have no uncommitted changes to tracked files. Otherwise it emits an error message of the form <code>Cannot &lt;action&gt;: &lt;reason&gt;. &lt;hint&gt;</code>, and dies. Example: </p>
<dl>
<dt>
<dd>
<pre>
require_clean_work_tree rebase &quot;Please commit or stash them.&quot;
</pre>
</dl>
</dl>
<p> get_author_ident_from_commit</p>
<dl>
<dt>
<dd> outputs code for use with eval to set the GIT_AUTHOR_NAME, GIT_AUTHOR_EMAIL and GIT_AUTHOR_DATE variables for a given commit.</dl>
<p> create_virtual_base</p>
<dl>
<dt>
<dd> modifies the first file so only lines in common with the second file remain. If there is insufficient common material, then the first file is left empty. The result is suitable as a virtual base input for a 3-way merge.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
