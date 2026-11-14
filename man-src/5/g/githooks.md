---
title: "githooks(5)"
name: "githooks"
section: "5"
letter: "g"
url: "/docs/linux/man/5-githooks/"
description: "githooks – Hooks used by Git"
---

<p>githooks &#8211; Hooks used by Git</p>
<h2>Synopsis</h2>
<p>$GIT_DIR/hooks/* (or `git config core.hooksPath`/*)</p>
<h2>Description</h2>
<p>Hooks are programs you can place in a hooks directory to trigger actions at certain points in git&#8217;s execution. Hooks that don&#8217;t have the executable bit set are ignored. </p>
<p> By default the hooks directory is <code>$GIT_DIR/hooks</code>, but that can be changed via the <code>core.hooksPath</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> Before Git invokes a hook, it changes its working directory to either $GIT_DIR in a bare repository or the root of the working tree in a non-bare repository. An exception are hooks triggered during a push (<i>pre-receive</i>, <i>update</i>, <i>post-receive</i>, <i>post-update</i>, <i>push-to-checkout</i>) which are always executed in $GIT_DIR. </p>
<p> Hooks can get their arguments via the environment, command-line arguments, and stdin. See the documentation for each hook below for details. </p>
<p> <code>git init</code> may copy hooks to the new repository, depending on its configuration. See the &quot;TEMPLATE DIRECTORY&quot; section in <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1) for details. When the rest of this document refers to &quot;default hooks&quot; it&#8217;s talking about the default template shipped with Git. </p>
<p> The currently supported hooks are described below.</p>
<h2>Hooks</h2>
<h3>applypatch-msg</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1). It takes a single parameter, the name of the file that holds the proposed commit log message. Exiting with a non-zero status causes <code>git am</code> to abort before applying the patch. </p>
<p> The hook is allowed to edit the message file in place, and can be used to normalize the message into some project standard format. It can also be used to refuse the commit after inspecting the message file. </p>
<p> The default <i>applypatch-msg</i> hook, when enabled, runs the <i>commit-msg</i> hook, if the latter is enabled.</p>
<h3>pre-applypatch</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1). It takes no parameter, and is invoked after the patch is applied, but before a commit is made. </p>
<p> If it exits with non-zero status, then the working tree will not be committed after applying the patch. </p>
<p> It can be used to inspect the current working tree and refuse to make a commit if it does not pass certain test. </p>
<p> The default <i>pre-applypatch</i> hook, when enabled, runs the <i>pre-commit</i> hook, if the latter is enabled.</p>
<h3>post-applypatch</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1). It takes no parameter, and is invoked after the patch is applied and a commit is made. </p>
<p> This hook is meant primarily for notification, and cannot affect the outcome of <code>git am</code>.</p>
<h3>pre-commit</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1), and can be bypassed with the <code>&#8211;no-verify</code> option. It takes no parameters, and is invoked before obtaining the proposed commit log message and making a commit. Exiting with a non-zero status from this script causes the <code>git commit</code> command to abort before creating a commit. </p>
<p> The default <i>pre-commit</i> hook, when enabled, catches introduction of lines with trailing whitespaces and aborts the commit when such a line is found. </p>
<p> All the <code>git commit</code> hooks are invoked with the environment variable <code>GIT_EDITOR=:</code> if the command will not bring up an editor to modify the commit message. </p>
<p> The default <i>pre-commit</i> hook, when enabled&#8212;and with the <code>hooks.allownonascii</code> config option unset or set to false&#8212;prevents the use of non-ASCII filenames.</p>
<h3>pre-merge-commit</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1), and can be bypassed with the <code>&#8211;no-verify</code> option. It takes no parameters, and is invoked after the merge has been carried out successfully and before obtaining the proposed commit log message to make a commit. Exiting with a non-zero status from this script causes the <code>git merge</code> command to abort before creating a commit. </p>
<p> The default <i>pre-merge-commit</i> hook, when enabled, runs the <i>pre-commit</i> hook, if the latter is enabled. </p>
<p> This hook is invoked with the environment variable <code>GIT_EDITOR=:</code> if the command will not bring up an editor to modify the commit message. </p>
<p> If the merge cannot be carried out automatically, the conflicts need to be resolved and the result committed separately (see <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1)). At that point, this hook will not be executed, but the <i>pre-commit</i> hook will, if it is enabled.</p>
<h3>prepare-commit-msg</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) right after preparing the default log message, and before the editor is started. </p>
<p> It takes one to three parameters. The first is the name of the file that contains the commit log message. The second is the source of the commit message, and can be: <code>message</code> (if a <code>-m</code> or <code>-F</code> option was given); <code>template</code> (if a <code>-t</code> option was given or the configuration option <code>commit.template</code> is set); <code>merge</code> (if the commit is a merge or a <code>.git/MERGE_MSG</code> file exists); <code>squash</code> (if a <code>.git/SQUASH_MSG</code> file exists); or <code>commit</code>, followed by a commit object name (if a <code>-c</code>, <code>-C</code> or <code>&#8211;amend</code> option was given). </p>
<p> If the exit status is non-zero, <code>git commit</code> will abort. </p>
<p> The purpose of the hook is to edit the message file in place, and it is not suppressed by the <code>&#8211;no-verify</code> option. A non-zero exit means a failure of the hook and aborts the commit. It should not be used as replacement for pre-commit hook. </p>
<p> The sample <code>prepare-commit-msg</code> hook that comes with Git removes the help message found in the commented portion of the commit template.</p>
<h3>commit-msg</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) and <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1), and can be bypassed with the <code>&#8211;no-verify</code> option. It takes a single parameter, the name of the file that holds the proposed commit log message. Exiting with a non-zero status causes the command to abort. </p>
<p> The hook is allowed to edit the message file in place, and can be used to normalize the message into some project standard format. It can also be used to refuse the commit after inspecting the message file. </p>
<p> The default <i>commit-msg</i> hook, when enabled, detects duplicate <code>Signed-off-by</code> trailers, and aborts the commit if one is found.</p>
<h3>post-commit</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1). It takes no parameters, and is invoked after a commit is made. </p>
<p> This hook is meant primarily for notification, and cannot affect the outcome of <code>git commit</code>.</p>
<h3>pre-rebase</h3>
<p>This hook is called by <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) and can be used to prevent a branch from getting rebased. The hook may be called with one or two parameters. The first parameter is the upstream from which the series was forked. The second parameter is the branch being rebased, and is not set when rebasing the current branch.</p>
<h3>post-checkout</h3>
<p>This hook is invoked when a <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1) or <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1) is run after having updated the worktree. The hook is given three parameters: the ref of the previous HEAD, the ref of the new HEAD (which may or may not have changed), and a flag indicating whether the checkout was a branch checkout (changing branches, flag=1) or a file checkout (retrieving a file from the index, flag=0). This hook cannot affect the outcome of <code>git switch</code> or <code>git checkout</code>, other than that the hook&#8217;s exit status becomes the exit status of these two commands. </p>
<p> It is also run after <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1), unless the <code>&#8211;no-checkout</code> (<code>-n</code>) option is used. The first parameter given to the hook is the null-ref, the second the ref of the new HEAD and the flag is always 1. Likewise for <code>git worktree add</code> unless <code>&#8211;no-checkout</code> is used. </p>
<p> This hook can be used to perform repository validity checks, auto-display differences from the previous HEAD if different, or set working dir metadata properties.</p>
<h3>post-merge</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1), which happens when a <code>git pull</code> is done on a local repository. The hook takes a single parameter, a status flag specifying whether or not the merge being done was a squash merge. This hook cannot affect the outcome of <code>git merge</code> and is not executed, if the merge failed due to conflicts. </p>
<p> This hook can be used in conjunction with a corresponding pre-commit hook to save and restore any form of metadata associated with the working tree (e.g.: permissions/ownership, ACLS, etc). See contrib/hooks/setgitperms.perl for an example of how to do this.</p>
<h3>pre-push</h3>
<p>This hook is called by <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) and can be used to prevent a push from taking place. The hook is called with two parameters which provide the name and location of the destination remote, if a named remote is not being used both values will be the same. </p>
<p> Information about what is to be pushed is provided on the hook&#8217;s standard input with lines of the form: </p>
<dl>
<dd>
<pre>&lt;local ref&gt; SP &lt;local object name&gt; SP &lt;remote ref&gt; SP &lt;remote object name&gt; LF</pre>
</dl>
<p> For instance, if the command <code>git push origin master:foreign</code> were run the hook would receive a line like the following: </p>
<dl>
<dd>
<pre>refs/heads/master 67890 refs/heads/foreign 12345</pre>
</dl>
<p> although the full object name would be supplied. If the foreign ref does not yet exist the <code>&lt;remote object name&gt;</code> will be the all-zeroes object name. If a ref is to be deleted, the <code>&lt;local ref&gt;</code> will be supplied as <code>(delete)</code> and the <code>&lt;local object name&gt;</code> will be the all-zeroes object name. If the local commit was specified by something other than a name which could be expanded (such as <code>HEAD~</code>, or an object name) it will be supplied as it was originally given. </p>
<p> If this hook exits with a non-zero status, <code>git push</code> will abort without pushing anything. Information about why the push is rejected may be sent to the user by writing to standard error.</p>
<h3>pre-receive</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1) when it reacts to <code>git push</code> and updates reference(s) in its repository. Just before starting to update refs on the remote repository, the pre-receive hook is invoked. Its exit status determines the success or failure of the update. </p>
<p> This hook executes once for the receive operation. It takes no arguments, but for each ref to be updated it receives on standard input a line of the format: </p>
<dl>
<dd>
<pre>&lt;old-value&gt; SP &lt;new-value&gt; SP &lt;ref-name&gt; LF</pre>
</dl>
<p> where <code>&lt;old-value&gt;</code> is the old object name stored in the ref, <code>&lt;new-value&gt;</code> is the new object name to be stored in the ref and <code>&lt;ref-name&gt;</code> is the full name of the ref. When creating a new ref, <code>&lt;old-value&gt;</code> is the all-zeroes object name. </p>
<p> If the hook exits with non-zero status, none of the refs will be updated. If the hook exits with zero, updating of individual refs can still be prevented by the <i>update</i> hook. </p>
<p> Both standard output and standard error output are forwarded to <code>git send-pack</code> on the other end, so you can simply <code>echo</code> messages for the user. </p>
<p> The number of push options given on the command line of <code>git push &#8211;push-option=&#8230;</code> can be read from the environment variable <code>GIT_PUSH_OPTION_COUNT</code>, and the options themselves are found in <code>GIT_PUSH_OPTION_0</code>, <code>GIT_PUSH_OPTION_1</code>,&#8230; If it is negotiated to not use the push options phase, the environment variables will not be set. If the client selects to use push options, but doesn&#8217;t transmit any, the count variable will be set to zero, <code>GIT_PUSH_OPTION_COUNT=0</code>. </p>
<p> See the section on &quot;Quarantine Environment&quot; in <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1) for some caveats.</p>
<h3>update</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1) when it reacts to <code>git push</code> and updates reference(s) in its repository. Just before updating the ref on the remote repository, the update hook is invoked. Its exit status determines the success or failure of the ref update. </p>
<p> The hook executes once for each ref to be updated, and takes three parameters: </p>
<dl>
<dd>&bull; the name of the ref being updated,</dl>
<dl>
<dd>&bull; the old object name stored in the ref,</dl>
<dl>
<dd>&bull; and the new object name to be stored in the ref.</dl>
<p> A zero exit from the update hook allows the ref to be updated. Exiting with a non-zero status prevents <code>git receive-pack</code> from updating that ref. </p>
<p> This hook can be used to prevent <i>forced</i> update on certain refs by making sure that the object name is a commit object that is a descendant of the commit object named by the old object name. That is, to enforce a &quot;fast-forward only&quot; policy. </p>
<p> It could also be used to log the old..new status. However, it does not know the entire set of branches, so it would end up firing one e-mail per ref when used naively, though. The <i>post-receive</i> hook is more suited to that. </p>
<p> In an environment that restricts the users&#8217; access only to git commands over the wire, this hook can be used to implement access control without relying on filesystem ownership and group membership. See <code><a href="/docs/linux/man/1-git-shell/">git-shell</a></code>(1) for how you might use the login shell to restrict the user&#8217;s access to only git commands. </p>
<p> Both standard output and standard error output are forwarded to <code>git send-pack</code> on the other end, so you can simply <code>echo</code> messages for the user. </p>
<p> The default <i>update</i> hook, when enabled&#8212;and with <code>hooks.allowunannotated</code> config option unset or set to false&#8212;prevents unannotated tags to be pushed.</p>
<h3>proc-receive</h3>
<p>This hook is invoked by <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1). If the server has set the multi-valued config variable <code>receive.procReceiveRefs</code>, and the commands sent to <i>receive-pack</i> have matching reference names, these commands will be executed by this hook, instead of by the internal <code>execute_commands()</code> function. This hook is responsible for updating the relevant references and reporting the results back to <i>receive-pack</i>. </p>
<p> This hook executes once for the receive operation. It takes no arguments, but uses a pkt-line format protocol to communicate with <i>receive-pack</i> to read commands, push-options and send results. In the following example for the protocol, the letter <i>S</i> stands for <i>receive-pack</i> and the letter <i>H</i> stands for this hook. </p>
<dl>
<dd>
<pre># Version and features negotiation.
S: PKT-LINE(version=1
