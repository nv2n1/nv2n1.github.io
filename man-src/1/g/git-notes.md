---
title: "git-notes(1)"
name: "git-notes"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-notes/"
description: "git-notes – Add or inspect object notes"
---

<h2 class="name">NAME</h2>
<p> git-notes &#8211; Add or inspect object notes </p>
<h2>SYNOPSIS</h2>
<pre><code>
git notes[list[&lt;object&gt;]] git notes add[-f][--allow - empty][-F&lt;file&gt; | -m&lt;msg&gt; | (-c | -C) &lt; object &gt; ][&lt;object&gt;] git notes copy[-f](--stdin | &lt;from - object&gt;[&lt;to - object&gt;])
        git notes append[--allow - empty][-F&lt;file&gt; | -m&lt;msg&gt; | (-c | -C) &lt; object &gt; ][&lt;object&gt;] git notes edit[--allow - empty][&lt;object&gt;] git notes show[&lt;object&gt;] git notes merge[-v | -q][-s&lt;strategy&gt;]&lt;notes - ref&gt; git notes merge-- commit[-v | -q] git notes merge-- abort[-v | -q] git notes remove[--ignore - missing][--stdin][&lt;object&gt;...] git notes prune[-n][-v] git notes get
    - ref
</code></pre>
<h2>DESCRIPTION</h2>
<p> Adds, removes, or reads notes attached to objects, without touching the objects themselves. </p>
<p> By default, notes are saved to and read from <code>refs/notes/commits</code>, but this default can be overridden. See the OPTIONS, CONFIGURATION, and ENVIRONMENT sections below. If this ref does not exist, it will be quietly created when it is first needed to store a note. </p>
<p> A typical use of notes is to supplement a commit message without changing the commit itself. Notes can be shown by <i>git log</i> along with the original commit message. To distinguish these notes from the message stored in the commit object, the notes are indented like the message, after an unindented line saying &quot;Notes (&lt;refname&gt;):&quot; (or &quot;Notes:&quot; for <code>refs/notes/commits</code>). </p>
<p> Notes can also be added to patches prepared with <code>git format-patch</code> by using the <code>&#8211;notes</code> option. Such notes are added as a patch commentary after a three dash separator line. </p>
<p> To change which notes are shown by <i>git log</i>, see the &quot;notes.displayRef&quot; configuration in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1). </p>
<p> See the &quot;notes.rewrite.&lt;command&gt;&quot; configuration for a way to carry notes across commands that rewrite commits.</p>
<h2>SUBCOMMANDS</h2>
<p> list</p>
<dl>
<dt>
<dd> List the notes object for a given object. If no object is given, show a list of all note objects and the objects they annotate (in the format &quot;&lt;note object&gt; &lt;annotated object&gt;&quot;). This is the default subcommand if no subcommand is given.</dl>
<p> add</p>
<dl>
<dt>
<dd> Add notes for a given object (defaults to HEAD). Abort if the object already has notes (use <code>-f</code> to overwrite existing notes). However, if you&#8217;re using <code>add</code> interactively (using an editor to supply the notes contents), then &#8211; instead of aborting &#8211; the existing notes will be opened in the editor (like the <code>edit</code> subcommand).</dl>
<p> copy</p>
<dl>
<dt>
<dd> Copy the notes for the first object onto the second object (defaults to HEAD). Abort if the second object already has notes, or if the first object has none (use -f to overwrite existing notes to the second object). This subcommand is equivalent to: <code>git notes add [-f] -C $(git notes list &lt;from-object&gt;) &lt;to-object&gt;</code> </p>
<p> In <code>&#8211;stdin</code> mode, take lines in the format </p>
<dl>
<dt>
<dd>
<pre>
&lt;from-object&gt; SP &lt;to-object&gt; [ SP &lt;rest&gt; ] LF
</pre>
</dl>
<p> on standard input, and copy the notes from each &lt;from-object&gt; to its corresponding &lt;to-object&gt;. (The optional <code>&lt;rest&gt;</code> is ignored so that the command can read the input given to the <code>post-rewrite</code> hook.)</dl>
<p> append</p>
<dl>
<dt>
<dd> Append to the notes of an existing object (defaults to HEAD). Creates a new notes object if needed.</dl>
<p> edit</p>
<dl>
<dt>
<dd> Edit the notes for a given object (defaults to HEAD).</dl>
<p> show</p>
<dl>
<dt>
<dd> Show the notes for a given object (defaults to HEAD).</dl>
<p> merge</p>
<dl>
<dt>
<dd> Merge the given notes ref into the current notes ref. This will try to merge the changes made by the given notes ref (called &quot;remote&quot;) since the merge-base (if any) into the current notes ref (called &quot;local&quot;). </p>
<p> If conflicts arise and a strategy for automatically resolving conflicting notes (see the &quot;NOTES MERGE STRATEGIES&quot; section) is not given, the &quot;manual&quot; resolver is used. This resolver checks out the conflicting notes in a special worktree (<code>.git/NOTES_MERGE_WORKTREE</code>), and instructs the user to manually resolve the conflicts there. When done, the user can either finalize the merge with <i>git notes merge &#8211;commit</i>, or abort the merge with <i>git notes merge &#8211;abort</i>.</dl>
<p> remove</p>
<dl>
<dt>
<dd> Remove the notes for given objects (defaults to HEAD). When giving zero or one object from the command line, this is equivalent to specifying an empty note message to the <code>edit</code> subcommand.</dl>
<p> prune</p>
<dl>
<dt>
<dd> Remove all notes for non-existing/unreachable objects.</dl>
<p> get-ref</p>
<dl>
<dt>
<dd> Print the current notes ref. This provides an easy way to retrieve the current notes ref (e.g. from scripts).</dl>
<h2>OPTIONS</h2>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> When adding notes to an object that already has notes, overwrite the existing notes (instead of aborting).</dl>
<p> -m &lt;msg&gt;, &#8211;message=&lt;msg&gt;</p>
<dl>
<dt>
<dd> Use the given note message (instead of prompting). If multiple <code>-m</code> options are given, their values are concatenated as separate paragraphs. Lines starting with <code>#</code> and empty lines other than a single line between paragraphs will be stripped out.</dl>
<p> -F &lt;file&gt;, &#8211;file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Take the note message from the given file. Use <i>&#8211;</i> to read the note message from the standard input. Lines starting with <code>#</code> and empty lines other than a single line between paragraphs will be stripped out.</dl>
<p> -C &lt;object&gt;, &#8211;reuse-message=&lt;object&gt;</p>
<dl>
<dt>
<dd> Take the given blob object (for example, another note) as the note message. (Use <code>git notes copy &lt;object&gt;</code> instead to copy notes between objects.)</dl>
<p> -c &lt;object&gt;, &#8211;reedit-message=&lt;object&gt;</p>
<dl>
<dt>
<dd> Like <i>-C</i>, but with <code>-c</code> the editor is invoked, so that the user can further edit the note message.</dl>
<p> &#8211;allow-empty</p>
<dl>
<dt>
<dd> Allow an empty note object to be stored. The default behavior is to automatically remove empty notes.</dl>
<p> &#8211;ref &lt;ref&gt;</p>
<dl>
<dt>
<dd> Manipulate the notes tree in &lt;ref&gt;. This overrides <code>GIT_NOTES_REF</code> and the &quot;core.notesRef&quot; configuration. The ref specifies the full refname when it begins with <code>refs/notes/</code>; when it begins with <code>notes/</code>, <code>refs/</code> and otherwise <code>refs/notes/</code> is prefixed to form a full name of the ref.</dl>
<p> &#8211;ignore-missing</p>
<dl>
<dt>
<dd> Do not consider it an error to request removing notes from an object that does not have notes attached to it.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Also read the object names to remove notes from the standard input (there is no reason you cannot combine this with object names from the command line).</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Do not remove anything; just report the object names whose notes would be removed.</dl>
<p> -s &lt;strategy&gt;, &#8211;strategy=&lt;strategy&gt;</p>
<dl>
<dt>
<dd> When merging notes, resolve notes conflicts using the given strategy. The following strategies are recognized: &quot;manual&quot; (default), &quot;ours&quot;, &quot;theirs&quot;, &quot;union&quot; and &quot;cat_sort_uniq&quot;. This option overrides the &quot;notes.mergeStrategy&quot; configuration setting. See the &quot;NOTES MERGE STRATEGIES&quot; section below for more information on each notes merge strategy.</dl>
<p> &#8211;commit</p>
<dl>
<dt>
<dd> Finalize an in-progress <i>git notes merge</i>. Use this option when you have resolved the conflicts that <i>git notes merge</i> stored in .git/NOTES_MERGE_WORKTREE. This amends the partial merge commit created by <i>git notes merge</i> (stored in .git/NOTES_MERGE_PARTIAL) by adding the notes in .git/NOTES_MERGE_WORKTREE. The notes ref stored in the .git/NOTES_MERGE_REF symref is updated to the resulting commit.</dl>
<p> &#8211;abort</p>
<dl>
<dt>
<dd> Abort/reset an in-progress <i>git notes merge</i>, i.e. a notes merge with conflicts. This simply removes all files related to the notes merge.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> When merging notes, operate quietly.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> When merging notes, be more verbose. When pruning notes, report all object names whose notes are removed.</dl>
<h2>DISCUSSION</h2>
<p> Commit notes are blobs containing extra information about an object (usually information to supplement a commit&#8217;s message). These blobs are taken from notes refs. A notes ref is usually a branch which contains &quot;files&quot; whose paths are the object names for the objects they describe, with some directory separators included for performance reasons <font SIZE="-2">[1]</font>. </p>
<p> Every notes change creates a new commit at the specified notes ref. You can therefore inspect the history of the notes by invoking, e.g., <code>git log -p notes/commits</code>. Currently the commit message only records which operation triggered the update, and the commit authorship is determined according to the usual rules (see <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1)). These details may change in the future. </p>
<p> It is also permitted for a notes ref to point directly to a tree object, in which case the history of the notes can be read with <code>git log -p -g &lt;refname&gt;</code>.</p>
<h2>NOTES MERGE STRATEGIES</h2>
<p> The default notes merge strategy is &quot;manual&quot;, which checks out conflicting notes in a special work tree for resolving notes conflicts (<code>.git/NOTES_MERGE_WORKTREE</code>), and instructs the user to resolve the conflicts in that work tree. When done, the user can either finalize the merge with <i>git notes merge &#8211;commit</i>, or abort the merge with <i>git notes merge &#8211;abort</i>. </p>
<p> Users may select an automated merge strategy from among the following using either -s/&#8211;strategy option or configuring notes.mergeStrategy accordingly: </p>
<p> &quot;ours&quot; automatically resolves conflicting notes in favor of the local version (i.e. the current notes ref). </p>
<p> &quot;theirs&quot; automatically resolves notes conflicts in favor of the remote version (i.e. the given notes ref being merged into the current notes ref). </p>
<p> &quot;union&quot; automatically resolves notes conflicts by concatenating the local and remote versions. </p>
<p> &quot;cat_sort_uniq&quot; is similar to &quot;union&quot;, but in addition to concatenating the local and remote versions, this strategy also sorts the resulting lines, and removes duplicate lines from the result. This is equivalent to applying the &quot;cat | sort | uniq&quot; shell pipeline to the local and remote versions. This strategy is useful if the notes follow a line-based format where one wants to avoid duplicated lines in the merge result. Note that if either the local or remote version contain duplicate lines prior to the merge, these will also be removed by this notes merge strategy.</p>
<h2>EXAMPLES</h2>
<p> You can use notes to add annotations with information that was not available at the time a commit was written. </p>
<dl>
<dt>
<dd>
<pre><code>
$ git notes add - m 'Tested-by: Johannes Sixt &lt;j6t [at] kdbg.org&gt;' 72a144e2 $ git show - s 72a144e [...] Signed - off - by : Junio C Hamano&lt;gitster[at] pobox.com&gt; Notes : Tested - by : Johannes Sixt&lt;j6t[at] kdbg.org&gt;
</code></pre>
</dl>
<p> In principle, a note is a regular Git blob, and any kind of (non-)format is accepted. You can binary-safely create notes from arbitrary files using <i>git hash-object</i>: </p>
<dl>
<dt>
<dd>
<pre>
$ cc *.c
$ blob=$(git hash-object -w a.out)
$ git notes --ref=built add --allow-empty -C &quot;$blob&quot; HEAD
</pre>
</dl>
<p> (You cannot simply use <code>git notes &#8211;ref=built add -F a.out HEAD</code> because that is not binary-safe.) Of course, it doesn&#8217;t make much sense to display non-text-format notes with <i>git log</i>, so if you use such notes, you&#8217;ll probably need to write some special-purpose tools to do something useful with them.</p>
<h2>CONFIGURATION</h2>
<p> core.notesRef</p>
<dl>
<dt>
<dd> Notes ref to read and manipulate instead of <code>refs/notes/commits</code>. Must be an unabbreviated ref name. This setting can be overridden through the environment and command line.</dl>
<p> notes.mergeStrategy</p>
<dl>
<dt>
<dd> Which merge strategy to choose by default when resolving notes conflicts. Must be one of <code>manual</code>, <code>ours</code>, <code>theirs</code>, <code>union</code>, or <code>cat_sort_uniq</code>. Defaults to <code>manual</code>. See &quot;NOTES MERGE STRATEGIES&quot; section above for more information on each strategy. </p>
<p> This setting can be overridden by passing the <code>&#8211;strategy</code> option.</dl>
<p> notes.&lt;name&gt;.mergeStrategy</p>
<dl>
<dt>
<dd> Which merge strategy to choose when doing a notes merge into refs/notes/&lt;name&gt;. This overrides the more general &quot;notes.mergeStrategy&quot;. See the &quot;NOTES MERGE STRATEGIES&quot; section above for more information on each available strategy.</dl>
<p> notes.displayRef</p>
<dl>
<dt>
<dd> Which ref (or refs, if a glob or specified more than once), in addition to the default set by <code>core.notesRef</code> or <code>GIT_NOTES_REF</code>, to read notes from when showing commit messages with the <i>git log</i> family of commands. This setting can be overridden on the command line or by the <code>GIT_NOTES_DISPLAY_REF</code> environment variable. See <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1).</dl>
<p> notes.rewrite.&lt;command&gt;</p>
<dl>
<dt>
<dd> When rewriting commits with &lt;command&gt; (currently <code>amend</code> or <code>rebase</code>), if this variable is <code>false</code>, git will not copy notes from the original to the rewritten commit. Defaults to <code>true</code>. See also &quot;<code>notes.rewriteRef</code>&quot; below. </p>
<p> This setting can be overridden by the <code>GIT_NOTES_REWRITE_REF</code> environment variable.</dl>
<p> notes.rewriteMode</p>
<dl>
<dt>
<dd> When copying notes during a rewrite, what to do if the target commit already has a note. Must be one of <code>overwrite</code>, <code>concatenate</code>, <code>cat_sort_uniq</code>, or <code>ignore</code>. Defaults to <code>concatenate</code>. </p>
<p> This setting can be overridden with the <code>GIT_NOTES_REWRITE_MODE</code> environment variable.</dl>
<p> notes.rewriteRef</p>
<dl>
<dt>
<dd> When copying notes during a rewrite, specifies the (fully qualified) ref whose notes should be copied. May be a glob, in which case notes in all matching refs will be copied. You may also specify this configuration several times. </p>
<p> Does not have a default value; you must configure this variable to enable note rewriting. </p>
<p> Can be overridden with the <code>GIT_NOTES_REWRITE_REF</code> environment variable.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>GIT_NOTES_REF</code></p>
<dl>
<dt>
<dd> Which ref to manipulate notes from, instead of <code>refs/notes/commits</code>. This overrides the <code>core.notesRef</code> setting.</dl>
<p> <code>GIT_NOTES_DISPLAY_REF</code></p>
<dl>
<dt>
<dd> Colon-delimited list of refs or globs indicating which refs, in addition to the default from <code>core.notesRef</code> or <code>GIT_NOTES_REF</code>, to read notes from when showing commit messages. This overrides the <code>notes.displayRef</code> setting. </p>
<p> A warning will be issued for refs that do not exist, but a glob that does not match any refs is silently ignored.</dl>
<p> <code>GIT_NOTES_REWRITE_MODE</code></p>
<dl>
<dt>
<dd> When copying notes during a rewrite, what to do if the target commit already has a note. Must be one of <code>overwrite</code>, <code>concatenate</code>, <code>cat_sort_uniq</code>, or <code>ignore</code>. This overrides the <code>core.rewriteMode</code> setting.</dl>
<p> <code>GIT_NOTES_REWRITE_REF</code></p>
<dl>
<dt>
<dd> When rewriting commits, which notes to copy from the original to the rewritten commit. Must be a colon-delimited list of refs or globs. </p>
<p> If not set in the environment, the list of notes to copy depends on the <code>notes.rewrite.&lt;command&gt;</code> and <code>notes.rewriteRef</code> settings.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Permitted pathnames have the form <i>bf</i><code>/</code><i>fe</i><code>/</code><i>30</i><code>/</code><i>&#8230;</i><code>/</code><i>680d5a&#8230;</i>: a sequence of directory names of two hexadecimal digits each followed by a filename with the rest of the object ID. </p>
</dl>
<h2>Index</h2>
