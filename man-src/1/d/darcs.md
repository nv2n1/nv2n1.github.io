---
title: "darcs(1)"
name: "darcs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-darcs/"
description: "darcs – an advanced revision control system"
---

<h2>NAME</h2>
<p> darcs &#8211; an advanced revision control system</p>
<h2>SYNOPSIS</h2>
<p> <code>darcs</code> <i>command</i> &lt;<i>arguments</i>|[<i>options</i>]&gt;&#8230; </p>
<p> Where the <i>commands</i> and their respective <i>arguments</i> are </p>
<p> <code>darcs help</code> [&lt;<i>darcs</i>_<i>command</i>&gt; [<i>darcs</i>_<i>subcommand</i>]]<br />
 <code>darcs add</code> &lt;<i>file</i>|<i>directory</i>&gt; &#8230;<br />
 <code>darcs remove</code> &lt;<i>file</i>|<i>directory</i>&gt; &#8230;<br />
 <code>darcs move</code> &lt;<i>source</i>&gt; &#8230; &lt;<i>destination</i>&gt;<br />
 <code>darcs replace</code> &lt;<i>old</i>&gt; &lt;<i>new</i>&gt; &lt;<i>file</i>&gt; &#8230;<br />
 <code>darcs revert</code> [<i>file</i>|<i>directory</i>]&#8230;<br />
 <code>darcs unrevert</code><br />
 <code>darcs whatsnew</code> [<i>file</i>|<i>directory</i>]&#8230;<br />
 <code>darcs record</code> [<i>file</i>|<i>directory</i>]&#8230;<br />
 <code>darcs unrecord</code><br />
 <code>darcs amend-record</code> [<i>file</i>|<i>directory</i>]&#8230;<br />
 <code>darcs mark-conflicts</code><br />
 <code>darcs tag</code> [<i>tagname</i>]<br />
 <code>darcs setpref</code> &lt;<i>pref</i>&gt; &lt;<i>value</i>&gt;<br />
 <code>darcs diff</code> [<i>file</i>|<i>directory</i>]&#8230;<br />
 <code>darcs changes</code> [<i>file</i>|<i>directory</i>]&#8230;<br />
 <code>darcs annotate</code> [<i>file</i>|<i>directory</i>]&#8230;<br />
 <code>darcs dist</code><br />
 <code>darcs test</code><br />
 <code>darcs trackdown</code> [[<i>initialization</i>] command<i>]</i><br />
 <code>darcs show contents</code> [<i>file</i>]&#8230;<br />
 <code>darcs show files</code> [<i>file</i>|<i>directory</i>]&#8230;<br />
 <code>darcs show index</code><br />
 <code>darcs show pristine</code><br />
 <code>darcs show repo</code><br />
 <code>darcs show authors</code><br />
 <code>darcs show tags</code><br />
 <code>darcs pull</code> [<i>repository</i>]&#8230;<br />
 <code>darcs fetch</code> [<i>repository</i>]&#8230;<br />
 <code>darcs obliterate</code><br />
 <code>darcs rollback</code> [<i>file</i>|<i>directory</i>]&#8230;<br />
 <code>darcs push</code> [<i>repository</i>]<br />
 <code>darcs send</code> [<i>repository</i>]<br />
 <code>darcs apply</code> &lt;<i>patchfile</i>&gt;<br />
 <code>darcs get</code> &lt;<i>repository</i>&gt; [&lt;<i>directory</i>&gt;]<br />
 <code>darcs put</code> &lt;<i>new</i> <i>repository</i>&gt;<br />
 <code>darcs initialize</code><br />
 <code>darcs optimize</code><br />
 <code>darcs check</code><br />
 <code>darcs repair</code><br />
 <code>darcs convert</code> &lt;<i>source</i>&gt; [&lt;<i>destination</i>&gt;] </p>
<h2>DESCRIPTION</h2>
<p> Darcs is a free, open source revision control system. It is:</p>
<dl>
<dt>&bull;</p>
<dd> Distributed: Every user has access to the full command set, removing boundaries between server and client or committer and non-committers.</p>
<dt>&bull;</p>
<dd> Interactive: Darcs is easy to learn and efficient to use because it asks you questions in response to simple commands, giving you choices in your work flow. You can choose to record one change in a file, while ignoring another. As you update from upstream, you can review each patch name, even the full `diff&#8217; for interesting patches.</p>
<dt>&bull;</p>
<dd> Smart: Originally developed by physicist David Roundy, darcs is based on a unique algebra of patches. This smartness lets you respond to changing demands in ways that would otherwise not be possible. Learn more about spontaneous branches with darcs.</dl>
<h2>OPTIONS</h2>
<p> Different options are accepted by different Darcs commands. Each command&#8217;s most important options are listed in the <code>COMMANDS</code> section. For a full list of all options accepted by a particular command, run `darcs <i>command</i> &#8211;help&#8217;.</p>
<h3>Selecting Patches:</h3>
<p> The &#8211;patches option yields patches with names matching an `extended&#8217; regular expression. See <a href="/docs/linux/man/7-regex/">regex</a>(7) for details. The &#8211;matches option yields patches that match a logical (Boolean) expression: one or more primitive expressions combined by grouping (parentheses) and the complement (not), conjunction (and) and disjunction (or) operators. The C notation for logic operators (!, &amp;&amp; and ||) can also be used. </p>
<p>&nbsp;<wbr>&#8211;patches=regex is a synonym for &#8211;matches=&#8217;name regex&#8217;<br />
&nbsp;<wbr>&#8211;from-patch and &#8211;to-patch are synonyms for &#8211;from-match=&#8217;name&#8230; and &#8211;to-match=&#8217;name&#8230;<br />
&nbsp;<wbr>&#8211;from-patch and &#8211;to-match can be unproblematically combined:<br />
&nbsp;<wbr>darcs changes &#8211;from-patch=&#8217;html.*documentation&#8217;&nbsp;<wbr>&#8211;to-match=&#8217;date 20040212&#8242; </p>
<p> The following primitive Boolean expressions are supported:<br />
&nbsp;<wbr>&nbsp;<wbr>exact &#8211; check a literal string against the patch name.<br />
&nbsp;<wbr>&nbsp;<wbr>name &#8211; check a regular expression against the patch name.<br />
&nbsp;<wbr>&nbsp;<wbr>author &#8211; check a regular expression against the author name.<br />
&nbsp;<wbr>&nbsp;<wbr>hunk &#8211; check a regular expression against the contents of a hunk patch.<br />
&nbsp;<wbr>&nbsp;<wbr>comment &#8211; check a regular expression against the log message.<br />
&nbsp;<wbr>&nbsp;<wbr>hash &#8211; match the darcs hash for a patch.<br />
&nbsp;<wbr>&nbsp;<wbr>date &#8211; match the patch date.<br />
&nbsp;<wbr>&nbsp;<wbr>touch &#8211; match file paths for a patch. </p>
<p> Here are some examples:<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;exact&nbsp;<wbr>&quot;Resolve issue17: use dynamic memory allocation.&quot;&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;name issue17&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;name&nbsp;<wbr>&quot;^[Rr]esolve issue17\&gt;&quot;&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;author&nbsp;<wbr>&quot;David Roundy&quot;&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;author droundy&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;author droundy [at] darcs.net&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;hunk&nbsp;<wbr>&quot;foo&nbsp;<wbr>=&nbsp;<wbr>2&quot;&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;hunk&nbsp;<wbr>&quot;^instance .*&nbsp;<wbr>Foo where$&quot;&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;comment&nbsp;<wbr>&quot;prevent deadlocks&quot;&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;hash 20040403105958-53a90-c719567e92c3b0ab9eddd5290b705712b8b918ef&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;date&nbsp;<wbr>&quot;2006-04-02 22:41&quot;&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;date&nbsp;<wbr>&quot;tea time yesterday&quot;&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;touch src/foo.c&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;touch src/&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>darcs annotate &#8211;summary &#8211;match&nbsp;<wbr>&#8216;touch&nbsp;<wbr>&quot;src/*.(c|h)&quot;&#8217; </p>
<h2>COMMANDS</h2>
<p> <code>darcs help</code> [&lt;<i>darcs</i>_<i>command</i>&gt; [<i>darcs</i>_<i>subcommand</i>]]</p>
<dl>
<dt>
<dd> Without arguments, `darcs help&#8217; prints a categorized list of darcs commands and a short description of each one. With an extra argument, `darcs help foo&#8217; prints detailed help about the darcs command foo. </p>
</dl>
<h3>Changing and querying the working copy:</h3>
<p> <code>darcs add</code> &lt;<i>file</i>|<i>directory</i>&gt; &#8230;</p>
<dl>
<dt>
<dd> Generally a repository contains both files that should be version controlled (such as source code) and files that Darcs should ignore (such as executables compiled from the source code). The `darcs add&#8217; command is used to tell Darcs which files to version control. </p>
<p> When an existing project is first imported into a Darcs repository, it is common to run `darcs add -r *&#8217; or `darcs record -l&#8217; to add all initial source files into darcs. </p>
<p> Adding symbolic links (symlinks) is not supported. </p>
<p> Darcs will ignore all files and folders that look `boring&#8217;. The &#8211;boring option overrides this behaviour. </p>
<p> Darcs will not add file if another file in the same folder has the same name, except for case. The &#8211;case-ok option overrides this behaviour. Windows and OS X usually use filesystems that do not allow files a folder to have the same name except for case (for example, `ReadMe&#8217; and `README&#8217;). If &#8211;case-ok is used, the repository might be unusable on those systems! </p>
</dl>
<p> <code>darcs remove</code> &lt;<i>file</i>|<i>directory</i>&gt; &#8230;</p>
<dl>
<dt>
<dd> The `darcs remove&#8217; command exists primarily for symmetry with `darcs add&#8217;, as the normal way to remove a file from version control is simply to delete it from the working tree. This command is only useful in the unusual case where one wants to record a removal patch WITHOUT deleting the copy in the working tree (which can be re-added). </p>
<p> Note that applying a removal patch to a repository (e.g. by pulling the patch) will ALWAYS affect the working tree of that repository. </p>
</dl>
<p> <code>darcs move</code> &lt;<i>source</i>&gt; &#8230; &lt;<i>destination</i>&gt;</p>
<dl>
<dt>
<dd> Darcs cannot reliably distinguish between a file being deleted and a new one added, and a file being moved. Therefore Darcs always assumes the former, and provides the `darcs mv&#8217; command to let Darcs know when you want the latter. This command will also move the file in the working tree (unlike `darcs remove&#8217;), unless it has already been moved. </p>
<p> Darcs will not rename a file if another file in the same folder has the same name, except for case. The &#8211;case-ok option overrides this behaviour. Windows and OS X usually use filesystems that do not allow files a folder to have the same name except for case (for example, `ReadMe&#8217; and `README&#8217;). If &#8211;case-ok is used, the repository might be unusable on those systems! </p>
</dl>
<p> <code>darcs replace</code> &lt;<i>old</i>&gt; &lt;<i>new</i>&gt; &lt;<i>file</i>&gt; &#8230;</p>
<dl>
<dt>
<dd> In addition to line-based patches, Darcs supports a limited form of lexical substitution. Files are treated as sequences of words, and each occurrence of the old word is replaced by the new word. This is intended to provide a clean way to rename a function or variable. Such renamings typically affect lines all through the source code, so a traditional line-based patch would be very likely to conflict with other branches, requiring manual merging. </p>
<p> Files are tokenized according to one simple rule: words are strings of valid token characters, and everything between them (punctuation and whitespace) is discarded. By default, valid token characters are letters, numbers and the underscore (i.e. [A-Za-z0-9_]). However if the old and/or new token contains either a hyphen or period, BOTH hyphen and period are treated as valid (i.e. [A-Za-z0-9_.-]). </p>
<p> The set of valid characters can be customized using the &#8211;token-chars option. The argument must be surrounded by square brackets. If a hyphen occurs between two characters in the set, it is treated as a set range. For example, in most locales [A-Z] denotes all uppercase letters. If the first character is a caret, valid tokens are taken to be the complement of the remaining characters. For example, [^:
] could be used to match fields in the <a href="/docs/linux/man/5-passwd/">passwd</a>(5), where records and fields are separated by newlines and colons respectively. </p>
<p> If you choose to use &#8211;token-chars, you are STRONGLY encouraged to do so consistently. The consequences of using multiple replace patches with different &#8211;token-chars arguments on the same file are not well tested nor well understood. </p>
<p> By default Darcs will refuse to perform a replacement if the new token is already in use, because the replacements would be not be distinguishable from the existing tokens. This behaviour can be overridden by supplying the &#8211;force option, but an attempt to `darcs rollback&#8217; the resulting patch will affect these existing tokens. </p>
<p> Limitations: </p>
<p> The tokenizer treats files as byte strings, so it is not possible for &#8211;token-chars to include multi-byte characters, such as the non-ASCII parts of UTF-8. Similarly, trying to replace a `high-bit&#8217; character from a unibyte encoding will also result in replacement of the same byte in files with different encodings. For example, an acute a from ISO 8859-1 will also match an alpha from ISO 8859-7. </p>
<p> Due to limitations in the patch file format, &#8211;token-chars arguments cannot contain literal whitespace. For example, [^ 
	] cannot be used to declare all characters except the space, tab and newline as valid within a word, because it contains a literal space. </p>
<p> Unlike POSIX <a href="/docs/linux/man/7-regex/">regex</a>(7) bracket expressions, character classes (such as [[:alnum:]]) are NOT supported by &#8211;token-chars, and will be silently treated as a simple set of characters. </p>
</dl>
<p> <code>darcs revert</code> [<i>file</i>|<i>directory</i>]&#8230;</p>
<dl>
<dt>
<dd> The `darcs revert&#8217; command discards unrecorded changes the working tree. As with `darcs record&#8217;, you will be asked which hunks (changes) to revert. The &#8211;all switch can be used to avoid such prompting. If files or directories are specified, other parts of the working tree are not reverted. </p>
<p> In you accidentally reverted something you wanted to keep (for example, typing `darcs rev -a&#8217; instead of `darcs rec -a&#8217;), you can immediately run `darcs unrevert&#8217; to restore it. This is only guaranteed to work if the repository has not changed since `darcs revert&#8217; ran. </p>
</dl>
<p> <code>darcs unrevert</code></p>
<dl>
<dt>
<dd> Unrevert is a rescue command in case you accidentally reverted something you wanted to keep (for example, typing `darcs rev -a&#8217; instead of `darcs rec -a&#8217;). </p>
<p> This command may fail if the repository has changed since the revert took place. Darcs will ask for confirmation before executing an interactive command that will DEFINITELY prevent unreversion. </p>
</dl>
<p> <code>darcs whatsnew</code> [<i>file</i>|<i>directory</i>]&#8230;</p>
<dl>
<dt>
<dd> The `darcs whatsnew&#8217; command lists unrecorded changes to the working tree. If you specify a set of files and directories, only unrecorded changes to those files and directories are listed. </p>
<p> With the &#8211;summary option, the changes are condensed to one line per file, with mnemonics to indicate the nature and extent of the change. The &#8211;look-for-adds option causes candidates for `darcs add&#8217; to be included in the summary output. Summary mnemonics are as follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>`A f&#8217;&nbsp;<wbr>and&nbsp;<wbr>`A d/&#8217;&nbsp;<wbr>respectively mean an added file or directory.<br />
&nbsp;<wbr>&nbsp;<wbr>`R f&#8217;&nbsp;<wbr>and&nbsp;<wbr>`R d/&#8217;&nbsp;<wbr>respectively mean a removed file or directory.<br />
&nbsp;<wbr>&nbsp;<wbr>`M f -N&nbsp;<wbr>+M rP&#8217;&nbsp;<wbr>means a modified file, with N lines deleted, M<br />
&nbsp;<wbr>&nbsp;<wbr>lines added, and P lexical replacements.<br />
&nbsp;<wbr>&nbsp;<wbr>`f -&gt;&nbsp;<wbr>g&#8217;&nbsp;<wbr>means a moved file or directory.<br />
&nbsp;<wbr>&nbsp;<wbr>`a f&#8217;&nbsp;<wbr>and&nbsp;<wbr>`a d/&#8217;&nbsp;<wbr>respectively mean a new, but unadded, file or<br />
&nbsp;<wbr>&nbsp;<wbr>directory, when using &#8211;look-for-adds. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>An exclamation mark&nbsp;<wbr>(!)&nbsp;<wbr>as in&nbsp;<wbr>`R!&nbsp;<wbr>foo.c&#8217;, means the hunk is known to<br />
&nbsp;<wbr>&nbsp;<wbr>conflict with a hunk in another patch.&nbsp;<wbr>&nbsp;<wbr>The phrase&nbsp;<wbr>`duplicated&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>means the hunk is known to be identical to a hunk in another patch. </p>
<p> By default, `darcs whatsnew&#8217; uses Darcs&#8217; internal format for changes. To see some context (unchanged lines) around each change, use the &#8211;unified option. To view changes in conventional `diff&#8217; format, use the `darcs diff&#8217; command; but note that `darcs whatsnew&#8217; is faster. </p>
<p> This command exits unsuccessfully (returns a non-zero exit status) if there are no unrecorded changes. </p>
</dl>
<h3>Copying changes between the working copy and the repository:</h3>
<p> <code>darcs record</code> [<i>file</i>|<i>directory</i>]&#8230;</p>
<dl>
<dt>
<dd> The `darcs record&#8217; command is used to create a patch from changes in the working tree. If you specify a set of files and directories, changes to other files will be skipped. </p>
<p> Every patch has a name, an optional description, an author and a date. </p>
<p> The patch name should be a short sentence that concisely describes the patch, such as `Add error handling to main event loop.&#8217; You can supply it in advance with the -m option, or provide it when prompted. </p>
<p> The patch description is an optional block of free-form text. It is used to supply additional information that doesn&#8217;t fit in the patch name. For example, it might include a rationale of WHY the change was necessary. By default Darcs asks if you want to add a description; the &#8211;edit-long-comment and &#8211;skip-long-comment can be used to answer `yes&#8217; or `no&#8217; (respectively) to this prompt. Finally, the &#8211;logfile option allows you to supply a file that already contains the patch name (first line) and patch description (subsequent lines). This is useful if a previous record failed and left a darcs-record-0 file. </p>
<p> Each patch is attributed to its author, usually by email address (for example, `Fred Bloggs &lt;fred [at] example.net&gt;&#8217;). Darcs looks in several places for this author string: the &#8211;author option, the files _darcs/prefs/author (in the repository) and ~/.darcs/author (in your home directory), and the environment variables $DARCS_EMAIL and $EMAIL. If none of those exist, Darcs will prompt you for an author string and write it to _darcs/prefs/author. Note that if if you have more than one email address, note that you can put them all in ~/.darcs/author, one author per line. Darcs will still prompt you for an author, but it allows you to select from the list, or to type in an alternative. </p>
<p> The patch date is generated automatically. It can only be spoofed by using the &#8211;pipe option. </p>
<p> If a test command has been defined with `darcs setpref&#8217;, attempting to record a patch will cause the test command to be run in a clean copy of the working tree (that is, including only recorded changes). If the test fails, you will be offered to abort the record operation. </p>
<p> The &#8211;set-scripts-executable option causes scripts to be made executable in the clean copy of the working tree, prior to running the test. See `darcs get&#8217; for an explanation of the script heuristic. </p>
<p> If your test command is tediously slow (e.g. `make all&#8217;) and you are recording several patches in a row, you may wish to use &#8211;no-test to skip all but the final test. </p>
<p> To see some context (unchanged lines) around each change, use the &#8211;unified option. </p>
</dl>
<p> <code>darcs unrecord</code></p>
<dl>
<dt>
<dd> Unrecord does the opposite of record in that it makes the changes from patches active changes again which you may record or revert later. The working copy itself will not change. Beware that you should not use this command if you are going to re-record the changes in any way and there is a possibility that another user may have already pulled the patch. </p>
</dl>
<p> <code>darcs amend-record</code> [<i>file</i>|<i>directory</i>]&#8230;</p>
<dl>
<dt>
<dd> Amend-record updates a `draft&#8217; patch with additions or improvements, resulting in a single `finished&#8217; patch. This is better than recording the additions and improvements as separate patches, because then whenever the `draft&#8217; patch is copied between repositories, you would need to make sure all the extra patches are copied, too. </p>
<p> Do not copy draft patches between repositories, because a finished patch cannot be copied into a repository that contains a draft of the same patch. If this has already happened, `darcs obliterate&#8217; can be used to remove the draft patch. </p>
<p> Do not run amend-record in repository that other developers can pull from, because if they pull while an amend-record is in progress, their repository may be corrupted. </p>
<p> When recording a draft patch, it is a good idea to start the name with `DRAFT:&#8217; so that other developers know it is not finished. When finished, remove it with `darcs amend-record &#8211;edit-long-comment&#8217;. To change the patch name without starting an editor, use &#8211;patch-name. </p>
<p> Like `darcs record&#8217;, if you call amend-record with files as arguments, you will only be asked about changes to those files. So to amend a patch to foo.c with improvements in bar.c, you would run: </p>
<p>&nbsp;<wbr>darcs amend-record &#8211;match&nbsp;<wbr>&#8216;touch foo.c&#8217;&nbsp;<wbr>bar.c </p>
<p> It is usually a bad idea to amend another developer&#8217;s patch. To make amend-record only ask about your own patches by default, you can add something like `amend-record match David Roundy&#8217; to ~/.darcs/defaults, where `David Roundy&#8217; is your name. </p>
</dl>
<p> <code>darcs mark-conflicts</code></p>
<dl>
<dt>
<dd> Darcs requires human guidance to unify changes to the same part of a source file. When a conflict first occurs, darcs will add the initial state and both choices to the working tree, delimited by the markers `v v v&#8217;, `=====&#8217;, `* * *&#8217; and `^ ^ ^&#8217;, as follows: </p>
<p> v v v v v v v Initial state. ============= First choice. ************* Second choice. ^ ^ ^ ^ ^ ^ ^ </p>
<p> However, you might revert or manually delete these markers without actually resolving the conflict. In this case, `darcs mark-conflicts&#8217; is useful to show where any unresolved conflicts. It is also useful if `darcs apply&#8217; is called with &#8211;apply-conflicts, where conflicts aren&#8217;t marked initially. </p>
<p> Any unrecorded changes to the working tree WILL be lost forever when you run this command! You will be prompted for confirmation before this takes place. </p>
</dl>
<h3>Direct modification of the repository:</h3>
<p> <code>darcs tag</code> [<i>tagname</i>]</p>
<dl>
<dt>
<dd> The `darcs tag&#8217; command names the current repository state, so that it can easily be referred to later. Every `important&#8217; state should be tagged; in particular it is good practice to tag each stable release with a number or codename. Advice on release numbering can be found at <a rel="nofollow" href="http://producingoss.com/en/development-cycle.html.">http://producingoss.com/en/development-cycle.html.</a> </p>
<p> To reproduce the state of a repository `R&#8217; as at tag `t&#8217;, use the command `darcs get &#8211;tag t R&#8217;. The command `darcs show tags&#8217; lists all tags in the current repository. </p>
<p> Tagging also provides significant performance benefits: when Darcs reaches a shared tag that depends on all antecedent patches, it can simply stop processing. </p>
<p> Like normal patches, a tag has a name, an author, a timestamp and an optional long description, but it does not change the working tree. A tag can have any name, but it is generally best to pick a naming scheme and stick to it. </p>
<p> The `darcs tag&#8217; command accepts the &#8211;pipe option, which behaves as described in `darcs record&#8217;. </p>
</dl>
<p> <code>darcs setpref</code> &lt;<i>pref</i>&gt; &lt;<i>value</i>&gt;</p>
<dl>
<dt>
<dd> When working on project with multiple repositories and contributors, it is sometimes desirable for a preference to be set consistently project-wide. This is achieved by treating a preference set with `darcs setpref&#8217; as an unrecorded change, which can then be recorded and then treated like any other patch. </p>
<p> Valid preferences are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>test &#8212; a shell command that runs regression tests<br />
&nbsp;<wbr>&nbsp;<wbr>predist &#8212; a shell command to run before&nbsp;<wbr>`darcs dist&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>boringfile &#8212; the path to a version-controlled boring file<br />
&nbsp;<wbr>&nbsp;<wbr>binariesfile &#8212; the path to a version-controlled binaries file </p>
<p> For example, a project using GNU autotools, with a `make test&#8217; target to perform regression tests, might enable Darcs&#8217; integrated regression testing with the following command: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>darcs setpref test&nbsp;<wbr>&#8216;autoconf&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>./configure&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>make&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>make test&#8217; </p>
<p> Note that merging is not currently implemented for preferences: if two patches attempt to set the same preference, the last patch applied to the repository will always take precedence. This is considered a low-priority bug, because preferences are seldom set. </p>
</dl>
<h3>Querying the repository:</h3>
<p> <code>darcs diff</code> [<i>file</i>|<i>directory</i>]&#8230;</p>
<dl>
<dt>
<dd> The `darcs diff&#8217; command compares two versions of the working tree of the current repository. Without options, the pristine (recorded) and unrecorded working trees are compared. This is lower-level than the `darcs whatsnew&#8217; command, since it outputs a line-by-line diff, and it is also slower. As with `darcs whatsnew&#8217;, if you specify files or directories, changes to other files are not listed. The command always uses an external diff utility. </p>
<p> With the &#8211;patch option, the comparison will be made between working trees with and without that patch. Patches `after&#8217; the selected patch are not present in either of the compared working trees. The &#8211;from-patch and &#8211;to-patch options allow the set of patches in the `old&#8217; and `new&#8217; working trees to be specified separately. </p>
<p> The associated tag and match options are also understood, e.g. `darcs diff &#8211;from-tag 1.0 &#8211;to-tag 1.1&#8242;. All these options assume an ordering of the patch set, so results may be affected by operations such as `darcs optimize &#8211;reorder&#8217;. </p>
<p> <a href="/docs/linux/man/1-diff/">diff</a>(1) is called with the arguments -rN. The &#8211;unified option causes -u to be passed to <a href="/docs/linux/man/1-diff/">diff</a>(1). An additional argument can be passed using &#8211;diff-opts, such as &#8211;diff-opts=-ud or &#8211;diff-opts=-wU9. </p>
<p> The &#8211;diff-command option can be used to specify an alternative utility, such as meld (GNOME) or opendiff (OS X). Arguments may be included, separated by whitespace. The value is not interpreted by a shell, so shell constructs cannot be used. The arguments %1 and %2 MUST be included, these are substituted for the two working trees being compared. If this option is used, &#8211;diff-opts is ignored. </p>
</dl>
<p> <code>darcs changes</code> [<i>file</i>|<i>directory</i>]&#8230;</p>
<dl>
<dt>
<dd> The `darcs changes&#8217; command lists the patches that constitute the current repository or, with &#8211;repo, a remote repository. Without options or arguments, ALL patches will be listed. </p>
<p> When given one or more files or directories as arguments, only patches which affect those files or directories are listed. This includes changes that happened to files before they were moved or renamed. </p>
<p> When given a &#8211;from-tag, &#8211;from-patch or &#8211;from-match, only changes since that tag or patch are listed. Similarly, the &#8211;to-tag, &#8211;to-patch and &#8211;to-match options restrict the list to older patches. </p>
<p> The &#8211;last and &#8211;max-count options both limit the number of patches listed. The former applies BEFORE other filters, whereas the latter applies AFTER other filters. For example `darcs changes foo.c &#8211;max-count 3&#8242; will print the last three patches that affect foo.c, whereas `darcs changes &#8211;last 3 foo.c&#8217; will, of the last three patches, print only those that affect foo.c. </p>
<p> Three output formats exist. The default is &#8211;human-readable. You can also select &#8211;context, which is the internal format (as seen in patch bundles) that can be re-read by Darcs (e.g. `darcs get &#8211;context&#8217;). </p>
<p> Finally, there is &#8211;xml-output, which emits valid XML&#8230; unless a the patch metadata (author, name or description) contains a non-ASCII character and was recorded in a non-UTF8 locale. </p>
<p> Note that while the &#8211;context flag may be used in conjunction with &#8211;xml-output or &#8211;human-readable, in neither case will darcs get be able to read the output. On the other hand, sufficient information WILL be output for a knowledgeable human to recreate the current state of the repository. </p>
</dl>
<p> <code>darcs annotate</code> [<i>file</i>|<i>directory</i>]&#8230;</p>
<dl>
<dt>
<dd> The `darcs annotate&#8217; command provides two unrelated operations. When called on a file, it will find the patch that last modified each line in that file. When called on a patch (e.g. using &#8211;patch), it will print the internal representation of that patch. </p>
<p> The &#8211;summary option will result in a summarized patch annotation, similar to `darcs whatsnew&#8217;. It has no effect on file annotations. </p>
<p> By default, output is in a human-readable format. The &#8211;machine-readable option can be used to generate output for machine postprocessing. </p>
</dl>
<p> <code>darcs dist</code></p>
<dl>
<dt>
<dd> The `darcs dist&#8217; command creates a compressed archive (a `tarball&#8217;) in the repository&#8217;s root directory, containing the recorded state of the working tree (unrecorded changes and the _darcs directory are excluded). </p>
<p> If a predist command is set (see `darcs setpref&#8217;), that command will be run on the tarball contents prior to archiving. For example, autotools projects would set it to `autoconf &amp;&amp; automake&#8217;. </p>
<p> By default, the tarball (and the top-level directory within the tarball) has the same name as the repository, but this can be overridden with the &#8211;dist-name option. </p>
</dl>
<p> <code>darcs test</code></p>
<dl>
<dt>
<dd> If a regression test is defined (see `darcs setpref&#8217;) it will be run. </p>
</dl>
<p> <code>darcs trackdown</code> [[<i>initialization</i>] command<i>]</i></p>
<dl>
<dt>
<dd> Trackdown tries to find the most recent version in the repository which passes a test. Given no arguments, it uses the default repository test. Given one argument, it treats it as a test command. Given two arguments, the first is an initialization command with is run only once, and the second is the test command. </p>
<p> Without the &#8211;bisect option, trackdown does linear search starting from head, and moving away from head. With the &#8211;bisect option, it does binary search. </p>
<p> Under the assumption that failure is monotonous, trackdown produces the same result with and without &#8211;bisect. (Monotonous means that when moving away from head, the test result changes only once from &quot;fail&quot; to &quot;ok&quot;.) If failure is not monotonous, any one of the patches that break the test is found at random.</dl>
<p> <code>darcs show contents</code> [<i>file</i>]&#8230;</p>
<dl>
<dt>
<dd> Show contents can be used to display an earlier version of some file(s). If you give show contents no version arguments, it displays the recorded version of the file(s). </p>
</dl>
<p> <code>darcs show files</code> [<i>file</i>|<i>directory</i>]&#8230;</p>
<dl>
<dt>
<dd> The `darcs show files&#8217; command lists those files and directories in the working tree that are under version control. This command is primarily for scripting purposes; end users will probably want `darcs whatsnew &#8211;summary&#8217;. </p>
<p> A file is `pending&#8217; if it has been added but not recorded. By default, pending files (and directories) are listed; the &#8211;no-pending option prevents this. </p>
<p> By default `darcs show files&#8217; lists both files and directories, but the alias `darcs show manifest&#8217; only lists files. The &#8211;files, &#8211;directories, &#8211;no-files and &#8211;no-directories modify this behaviour. </p>
<p> By default entries are one-per-line (i.e. newline separated). This can cause problems if the files themselves contain newlines or other control characters. To get aroudn this, the &#8211;null option uses the null character instead. The script interpreting output from this command needs to understand this idiom; `xargs -0&#8242; is such a command. </p>
<p> For example, to list version-controlled files by size: </p>
<p>&nbsp;<wbr>darcs show files -0 | xargs -0 ls -ldS </p>
</dl>
<p> <code>darcs show index</code></p>
<dl>
<dt>
<dd> The `darcs show index&#8217; command lists all version-controlled files and directories along with their hashes as stored in _darcs/index. For files, the fields correspond to file size, sha256 of the current file content and the filename.</dl>
<p> <code>darcs show pristine</code></p>
<dl>
<dt>
<dd> The `darcs show pristine&#8217; command lists all version-controlled files and directories along with the hashes of their pristine copies. For files, the fields correspond to file size, sha256 of the pristine file content and the filename.</dl>
<p> <code>darcs show repo</code></p>
<dl>
<dt>
<dd> The `darcs show repo&#8217; command displays statistics about the current repository, allowing third-party scripts to access this information without inspecting _darcs directly (and without breaking when the _darcs format changes). </p>
<p> By default, the number of patches is shown. If this data isn&#8217;t needed, use &#8211;no-files to accelerate this command from <a href="/docs/linux/man/n-o/">O</a>(n) to <a href="/docs/linux/man/1-o/">O</a>(1). </p>
<p> By default, output is in a human-readable format. The &#8211;xml-output option can be used to generate output for machine postprocessing. </p>
</dl>
<p> <code>darcs show authors</code></p>
<dl>
<dt>
<dd> The `darcs show authors&#8217; command lists the authors of the current repository, sorted by the number of patches contributed. With the &#8211;verbose option, this command simply lists the author of each patch (without aggregation or sorting). </p>
<p> An author&#8217;s name or email address may change over time. To tell Darcs when multiple author strings refer to the same individual, create an `.authorspellings&#8217; file in the root of the working tree. Each line in this file begins with an author&#8217;s canonical name and address, and may be followed by a comma separated list of extended regular expressions. Blank lines and lines beginning with two hyphens are ignored. The format of .authorspelling can be described by this pattern: </p>
<p>&nbsp;<wbr>name&nbsp;<wbr>&lt;address&gt;&nbsp;<wbr>[, regexp&nbsp;<wbr>]* </p>
<p> There are some pitfalls concerning special characters: Whitespaces are stripped, if you need space in regexp use [ ]. Because comma serves as a separator you have to escape it if you want it in regexp. Note that .authorspelingfile use extended regular expressions so +, ? and so on are metacharacters and you need to escape them to be interpreted literally. </p>
<p> Any patch with an author string that matches the canonical address or any of the associated regexps is considered to be the work of that author. All matching is case-insensitive and partial (it can match a substring). Use ^,$ to match the whole string in regexps </p>
<p> Currently this canonicalization step is done only in `darcs show authors&#8217;. Other commands, such as `darcs changes&#8217; use author strings verbatim. </p>
<p> An example .authorspelling file is: </p>
<p>&nbsp;<wbr>&#8212; This is a comment.<br />
&nbsp;<wbr>Fred Nurk&nbsp;<wbr>&lt;fred [at] example.com&gt;<br />
&nbsp;<wbr>John Snagge&nbsp;<wbr>&lt;snagge [at] bbc.co.uk&gt;, John, snagge@, js@(si|mit).edu<br />
&nbsp;<wbr>Chuck Jones\, Jr.&nbsp;<wbr>&lt;chuck [at] pobox.com&gt;, cj\+user [at] example.com </p>
</dl>
<p> <code>darcs show tags</code></p>
<dl>
<dt>
<dd> The tags command writes a list of all tags in the repository to standard output. </p>
<p> Tab characters (ASCII character 9) in tag names are changed to spaces for better interoperability with shell tools. A warning is printed if this happens.</dl>
<h3>Copying patches between repositories with working copy update:</h3>
<p> <code>darcs pull</code> [<i>repository</i>]&#8230;</p>
<dl>
<dt>
<dd> Pull is used to bring changes made in another repository into the current repository (that is, either the one in the current directory, or the one specified with the &#8211;repodir option). Pull allows you to bring over all or some of the patches that are in that repository but not in this one. Pull accepts arguments, which are URLs from which to pull, and when called without an argument, pull will use the repository from which you have most recently either pushed or pulled. </p>
<p> See &#8216;darcs help apply&#8217; for detailed description of many options. </p>
</dl>
<p> <code>darcs fetch</code> [<i>repository</i>]&#8230;</p>
<dl>
<dt>
<dd> fetch is used to bring changes made in another repository into the current repository without actually applying them. Fetch allows you to bring over all or some of the patches that are in that repository but not in this one. Fetch accepts arguments, which are URLs from which to fetch, and when called without an argument, fetch will use the repository from which you have most recently either pushed or pulled. The fetched patches are stored into a patch bundle, to be later applied using &quot;darcs apply&quot;.</dl>
<p> <code>darcs obliterate</code></p>
<dl>
<dt>
<dd> Obliterate completely removes recorded patches from your local repository. The changes will be undone in your working copy and the patches will not be shown in your changes list anymore. Beware that you can lose precious code by obliterating! </p>
</dl>
<p> <code>darcs rollback</code> [<i>file</i>|<i>directory</i>]&#8230;</p>
<dl>
<dt>
<dd> Rollback is used to undo the effects of one or more patches without actually deleting them. Instead, it creates a new patch reversing selected portions. of those changes. Unlike obliterate and unrecord (which accomplish a similar goal) rollback is perfectly safe, since it leaves in the repository a record of its changes. </p>
</dl>
<p> <code>darcs push</code> [<i>repository</i>]</p>
<dl>
<dt>
<dd> Push is the opposite of pull. Push allows you to copy changes from the current repository into another repository. </p>
</dl>
<p> <code>darcs send</code> [<i>repository</i>]</p>
<dl>
<dt>
<dd> Send is used to prepare a bundle of patches that can be applied to a target repository. Send accepts the URL of the repository as an argument. When called without an argument, send will use the most recent repository that was either pushed to, pulled from or sent to. By default, the patch bundle is sent by email, although you may save it to a file. </p>
</dl>
<p> <code>darcs apply</code> &lt;<i>patchfile</i>&gt;</p>
<dl>
<dt>
<dd> The `darcs apply&#8217; command takes a patch bundle and attempts to insert it into the current repository. In addition to invoking it directly on bundles created by `darcs send&#8217;, it is used internally by `darcs push&#8217; and `darcs put&#8217; on the remote end of an SSH connection. </p>
<p> If no file is supplied, the bundle is read from standard input. </p>
<p> If given an email instead of a patch bundle, Darcs will look for the bundle as a MIME attachment to that email. Currently this will fail if the MIME boundary is rewritten, such as in Courier and Mail.app. </p>
<p> If the `&#8211;reply noreply [at] example.net&#8217; option is used, and the bundle is attached to an email, Darcs will send a report (indicating success or failure) to the sender of the bundle (the To field). The argument to noreply is the address the report will appear to originate FROM. </p>
<p> The &#8211;cc option will cause the report to be CC&#8217;d to another address, for example `&#8211;cc reports [at] lists.example.net,admin [at] lists.example.net&#8217;. Using &#8211;cc without &#8211;reply is undefined. </p>
<p> If <a href="/docs/linux/man/1-gpg/">gpg</a>(1) is installed, you can use `&#8211;verify pubring.gpg&#8217; to reject bundles that aren&#8217;t signed by a key in pubring.gpg. </p>
<p> If &#8211;test is supplied and a test is defined (see `darcs setpref&#8217;), the bundle will be rejected if the test fails after applying it. In that case, the rejection email from &#8211;reply will include the test output. </p>
<p> A patch bundle may introduce unresolved conflicts with existing patches or with the working tree. By default, Darcs will add conflict markers (see `darcs mark-conflicts&#8217;). </p>
<p> The &#8211;external-merge option lets you resolve these conflicts using an external merge tool. In the option, &#8216;%a&#8217; is replaced with the common ancestor (merge base), &#8216;%1&#8217; with the first version, &#8216;%2&#8217; with the second version, and &#8216;%o&#8217; with the path where your resolved content should go. For example, to use the xxdiff visual merge tool you&#8217;d specify: &#8211;external-merge=&#8217;xxdiff -m -O -M %o %1 %a %2&#8242; </p>
<p> The &#8211;allow-conflicts option will skip conflict marking; this is useful when you want to treat a repository as just a bunch of patches, such as using `darcs pull &#8211;union&#8217; to download of your co-workers patches before going offline. </p>
<p> This can mess up unrecorded changes in the working tree, forcing you to resolve the conflict immediately. To simply reject bundles that introduce unresolved conflicts, using the &#8211;dont-allow-conflicts option. Making this the default in push-based workflows is strongly recommended. </p>
<p> Unlike most Darcs commands, `darcs apply&#8217; defaults to &#8211;all. Use the &#8211;interactive option to pick which patches to apply from a bundle. </p>
</dl>
<p> <code>darcs get</code> &lt;<i>repository</i>&gt; [&lt;<i>directory</i>&gt;]</p>
<dl>
<dt>
<dd> Get creates a local copy of a repository. The optional second argument specifies a destination directory for the new copy; if omitted, it is inferred from the source location. </p>
<p> By default Darcs will copy every patch from the original repository. This means the copy is completely independent of the original; you can operate on the new repository even when the original is inaccessible. If you expect the original repository to remain accessible, you can use &#8211;lazy to avoid copying patches until they are needed (`copy on demand&#8217;). This is particularly useful when copying a remote repository with a long history that you don&#8217;t care about. </p>
<p> The &#8211;lazy option isn&#8217;t as useful for local copies, because Darcs will automatically use `hard linking&#8217; where possible. As well as saving time and space, you can move or delete the original repository without affecting a complete, hard-linked copy. Hard linking requires that the copy be on the same filesystem and the original repository, and that the filesystem support hard linking. This includes NTFS, HFS+ and all general-purpose Unix filesystems (such as ext3, UFS and ZFS). FAT does not support hard links. </p>
<p> Darcs get will not copy unrecorded changes to the source repository&#8217;s working tree. </p>
<p> It is often desirable to make a copy of a repository that excludes some patches. For example, if releases are tagged then `darcs get &#8211;tag .&#8217; would make a copy of the repository as at the latest release. </p>
<p> An untagged repository state can still be identified unambiguously by a context file, as generated by `darcs changes &#8211;context&#8217;. Given the name of such a file, the &#8211;context option will create a repository that includes only the patches from that context. When a user reports a bug in an unreleased version of your project, the recommended way to find out exactly what version they were running is to have them include a context file in the bug report. </p>
<p> You can also make a copy of an untagged state using the &#8211;to-patch or &#8211;to-match options, which exclude patches `after&#8217; the first matching patch. Because these options treat the set of patches as an ordered sequence, you may get different results after reordering with `darcs optimize&#8217;, so tagging is preferred. </p>
</dl>
<p> <code>darcs put</code> &lt;<i>new</i> <i>repository</i>&gt;</p>
<dl>
<dt>
<dd> The `darcs put&#8217; command creates a copy of the current repository. It is currently very inefficient, so when creating local copies you should use `darcs get . x&#8217; instead of `darcs put x&#8217;. </p>
<p> Currently this command just uses `darcs init&#8217; to create the target repository, then `darcs push &#8211;all&#8217; to copy patches to it. Options passed to `darcs put&#8217; are passed to the init and/or push commands as appropriate. See those commands for an explanation of each option. </p>
</dl>
<h3>Administrating repositories:</h3>
<p> <code>darcs initialize</code></p>
<dl>
<dt>
<dd> The `darcs initialize&#8217; command turns the current directory into a Darcs repository. Any existing files and subdirectories become UNSAVED changes: record them with `darcs record &#8211;look-for-adds&#8217;. </p>
<p> This command creates the `_darcs&#8217; directory, which stores version control metadata. It also contains per-repository settings in _darcs/prefs/, which you can read about in the user manual. </p>
<p> By default, patches of the new repository are in the darcs-2 semantics. However it is possible to create a repository in darcs-1 semantics with the flag `&#8211;hashed&#8217;, althought this is not recommended except for sharing patches with a project that uses patches in the darcs-1 semantics. </p>
<p> Initialize is commonly abbreviated to `init&#8217;. </p>
</dl>
<p> <code>darcs optimize</code></p>
<dl>
<dt>
<dd> The `darcs optimize&#8217; command modifies the current repository in an attempt to reduce its resource requirements. By default a single fast, safe optimization is performed; additional optimization techniques can be enabled by passing options to `darcs optimize&#8217;. </p>
<p> The default optimization moves recent patches (those not included in the latest tag) to the `front&#8217;, reducing the amount that a typical remote command needs to download. It should also reduce the CPU time needed for some operations. </p>
<p> The `darcs optimize &#8211;relink&#8217; command hard-links patches that the current repository has in common with its peers. Peers are those repositories listed in _darcs/prefs/sources, or defined with the `&#8211;sibling&#8217; option (which can be used multiple times). </p>
<p> Darcs uses hard-links automatically, so this command is rarely needed. It is most useful if you used `cp -r&#8217; instead of `darcs get&#8217; to copy a repository, or if you pulled the same patch from a remote repository into multiple local repositories. </p>
<p> By default patches are compressed with zlib (RFC 1951) to reduce storage (and download) size. In exceptional circumstances, it may be preferable to avoid compression. In this case the `&#8211;dont-compress&#8217; option can be used (e.g. with `darcs record&#8217;) to avoid compression. </p>
<p> The `darcs optimize &#8211;uncompress&#8217; and `darcs optimize &#8211;compress&#8217; commands can be used to ensure existing patches in the current repository are respectively uncompressed or compressed. Note that repositories in the legacy `old-fashioned-inventory&#8217; format have a .gz extension on patch files even when uncompressed. </p>
<p> There is one more optimization which CAN NOT be performed by this command. Every time your record a patch, a new inventory file is written to _darcs/inventories/, and old inventories are never reaped. </p>
<p> If _darcs/inventories/ is consuming a relatively large amount of space, you can safely reclaim it by using `darcs get&#8217; to make a complete copy of the repo. When doing so, don&#8217;t forget to copy over any unsaved changes you have made to the working tree or to unversioned files in _darcs/prefs/ (such as _darcs/prefs/author). </p>
</dl>
<p> <code>darcs check</code></p>
<dl>
<dt>
<dd> This command verifies that the patches in the repository, when applied successively to an empty tree, result in the pristine tree. If not, the differences are printed and Darcs exits unsucessfully (with a non-zero exit status). </p>
<p> If a regression test is defined (see `darcs setpref&#8217;) it will be run by `darcs check&#8217;. Use the &#8211;no-test option to disable this. </p>
</dl>
<p> <code>darcs repair</code></p>
<dl>
<dt>
<dd> The `darcs repair&#8217; command attempts to fix corruption in the current repository. Currently it can only repair damage to the pristine tree, which is where most corruption occurs. </p>
</dl>
<p> <code>darcs convert</code> &lt;<i>source</i>&gt; [&lt;<i>destination</i>&gt;]</p>
<dl>
<dt>
<dd> The current repository format is called `darcs-2&#8242;. It was introduced in Darcs 2.0 and became the default for new projects in Darcs 2.2. The `darcs convert&#8217; command allows existing projects to migrate to this format from the older `darcs-1&#8242; format. </p>
<p> This command DOES NOT modify the source repository; a new destination repository is created. It is safe to run this command more than once on a repository (e.g. for testing), before the final conversion. </p>
<p> WARNING: the repository produced by this command is not understood by Darcs 1.x, and patches cannot be exchanged between repositories in darcs-1 and darcs-2 formats. </p>
<p> Furthermore, darcs 2 repositories created by different invocations of this command SHOULD NOT exchange patches, unless those repositories had no patches in common when they were converted. (That is, within a set of repos that exchange patches, no patch should be converted more than once.) </p>
<p> Due to this limitation, migrating a multi-branch project is a little awkward. Sorry! Here is the recommended process: </p>
<p>&nbsp;<wbr>1. for each branch&nbsp;<wbr>`foo&#8217;, tag that branch with&nbsp;<wbr>`foo-final&#8217;;<br />
&nbsp;<wbr>2. merge all branches together&nbsp;<wbr>(&#8211;allow-conflicts may help);<br />
&nbsp;<wbr>3. run&nbsp;<wbr>`darcs optimize &#8211;reorder&#8217;&nbsp;<wbr>on the result;<br />
&nbsp;<wbr>4. run&nbsp;<wbr>`darcs convert&#8217;&nbsp;<wbr>to create a merged darcs-2 repository;<br />
&nbsp;<wbr>5. re-create each branch by calling&nbsp;<wbr>`darcs get &#8211;tag foo-final&#8217;&nbsp;<wbr>on<br />
&nbsp;<wbr>the darcs-2 repository;&nbsp;<wbr>and finally<br />
&nbsp;<wbr>6. use&nbsp;<wbr>`darcs obliterate&#8217;&nbsp;<wbr>to delete the foo-final tags. </p>
</dl>
<h2>ENVIRONMENT</h2>
<h3>HOME and APPDATA</h3>
<p> Per-user preferences are set in $HOME/.darcs (on Unix) or %APPDATA%/darcs (on Windows). This is also the default location of the cache.</p>
<h3>DARCS_EDITOR, DARCSEDITOR, VISUAL and EDITOR</h3>
<p> To edit a patch description of email comment, Darcs will invoke an external editor. Your preferred editor can be set as any of the environment variables $DARCS_EDITOR, $DARCSEDITOR, $VISUAL or $EDITOR. If none of these are set, <a href="/docs/linux/man/1-vi/">vi</a>(1) is used. If vi crashes or is not found in your PATH, emacs, emacs -nw, nano and (on Windows) edit are each tried in turn.</p>
<h3>DARCS_PAGER and PAGER</h3>
<p> Darcs will sometimes invoke a pager if it deems output to be too long to fit onscreen. Darcs will use the pager specified by $DARCS_PAGER or $PAGER. If neither are set, `less&#8217; will be used.</p>
<h3>DARCS_TMPDIR and TMPDIR</h3>
<p> Darcs often creates temporary directories. For example, the `darcs diff&#8217; command creates two for the working trees to be diffed. By default temporary directories are created in /tmp, or if that doesn&#8217;t exist, in _darcs (within the current repo). This can be overridden by specifying some other directory in the file _darcs/prefs/tmpdir or the environment variable $DARCS_TMPDIR or $TMPDIR.</p>
<h3>DARCS_KEEP_TMPDIR</h3>
<p> If the environment variable DARCS_KEEP_TMPDIR is defined, darcs will not remove the temporary directories it creates. This is intended primarily for debugging Darcs itself, but it can also be useful, for example, to determine why your test preference (see `darcs setpref&#8217;) is failing when you run `darcs record&#8217;, but working when run manually.</p>
<h3>DARCS_EMAIL and EMAIL</h3>
<p> Each patch is attributed to its author, usually by email address (for example, `Fred Bloggs &lt;fred [at] example.net&gt;&#8217;). Darcs looks in several places for this author string: the &#8211;author option, the files _darcs/prefs/author (in the repository) and ~/.darcs/author (in your home directory), and the environment variables $DARCS_EMAIL and $EMAIL. If none of those exist, Darcs will prompt you for an author string and write it to _darcs/prefs/author. Note that if if you have more than one email address, note that you can put them all in ~/.darcs/author, one author per line. Darcs will still prompt you for an author, but it allows you to select from the list, or to type in an alternative.</p>
<h3>SENDMAIL</h3>
<p> On Unix, the `darcs send&#8217; command relies on <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8). The `&#8211;sendmail-command&#8217; or $SENDMAIL environment variable can be used to provide an explicit path to this program; otherwise the standard locations /usr/sbin/sendmail and /usr/lib/sendmail will be tried.</p>
<h3>DARCS_SSH</h3>
<p> Repositories of the form [user@]host:[dir] are taken to be remote repositories, which Darcs accesses with the external program <a href="/docs/linux/man/1-ssh/">ssh</a>(1). </p>
<p> The environment variable $DARCS_SSH can be used to specify an alternative SSH client. Arguments may be included, separated by whitespace. The value is not interpreted by a shell, so shell constructs cannot be used; in particular, it is not possible for the program name to contain whitespace by using quoting or escaping.</p>
<h3>DARCS_SCP and DARCS_SFTP</h3>
<p> When reading from a remote repository, Darcs will attempt to run `darcs transfer-mode&#8217; on the remote host. This will fail if the remote host only has Darcs 1 installed, doesn&#8217;t have Darcs installed at all, or only allows SFTP. </p>
<p> If transfer-mode fails, Darcs will fall back on <a href="/docs/linux/man/1-scp/">scp</a>(1) and <a href="/docs/linux/man/1-sftp/">sftp</a>(1). The commands invoked can be customized with the environment variables $DARCS_SCP and $DARCS_SFTP respectively, which behave like $DARCS_SSH. If the remote end allows only sftp, try setting DARCS_SCP=sftp.</p>
<h3>SSH_PORT</h3>
<p> If this environment variable is set, it will be used as the port number for all SSH calls made by Darcs (when accessing remote repositories over SSH). This is useful if your SSH server does not run on the default port, and your SSH client does not support <a href="/docs/linux/man/5-ssh_config/">ssh_config</a>(5). OpenSSH users will probably prefer to put something like `Host *.example.net Port 443&#8242; into their ~/.ssh/config file.</p>
<h3>HTTP_PROXY, HTTPS_PROXY, FTP_PROXY, ALL_PROXY and NO_PROXY</h3>
<p> If Darcs was built with libcurl, the environment variables HTTP_PROXY, HTTPS_PROXY and FTP_PROXY can be set to the URL of a proxy in the form </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[protocol://]&lt;host&gt;[:port] </p>
<p> In which case libcurl will use the proxy for the associated protocol (HTTP, HTTPS and FTP). The environment variable ALL_PROXY can be used to set a single proxy for all libcurl requests. </p>
<p> If the environment variable NO_PROXY is a comma-separated list of host names, access to those hosts will bypass proxies defined by the above variables. For example, it is quite common to avoid proxying requests to machines on the local network with </p>
<p>&nbsp;<wbr>&nbsp;<wbr>NO_PROXY=localhost,*.localdomain </p>
<p> For compatibility with lynx et al, lowercase equivalents of these environment variables (e.g. $http_proxy) are also understood and are used in preference to the uppercase versions. </p>
<p> If Darcs was not built with libcurl, all these environment variables are silently ignored, and there is no way to use a web proxy.</p>
<h3>DARCS_PROXYUSERPWD</h3>
<p> If Darcs was built with libcurl, and you are using a web proxy that requires authentication, you can set the $DARCS_PROXYUSERPWD environment variable to the username and password expected by the proxy, separated by a colon. This environment variable is silently ignored if Darcs was not built with libcurl. </p>
<h2>FILES</h2>
<h3>_darcs/prefs/binaries</h3>
<p> This file contains a list of extended regular expressions, one per line. A file path matching any of these expressions is assumed to contain binary data (not text). The entries in ~/.darcs/binaries (if it exists) supplement those in this file. </p>
<p> Blank lines, and lines beginning with an octothorpe (#) are ignored. See <a href="/docs/linux/man/7-regex/">regex</a>(7) for a description of extended regular expressions. </p>
<h3>_darcs/prefs/boring</h3>
<p> This file contains a list of extended regular expressions, one per line. A file path matching any of these expressions will be filtered out during `darcs add&#8217;, or when the `&#8211;look-for-adds&#8217; flag is passed to `darcs whatsnew&#8217; and `record&#8217;. The entries in ~/.darcs/boring (if it exists) supplement those in this file. </p>
<p> Blank lines, and lines beginning with an octothorpe (#) are ignored. See <a href="/docs/linux/man/7-regex/">regex</a>(7) for a description of extended regular expressions. </p>
<h2>BUGS</h2>
<p> At <a rel="nofollow" href="http://bugs.darcs.net/">http://bugs.darcs.net/</a> you can find a list of known bugs in Darcs. Unknown bugs can be reported at that site (after creating an account) or by emailing the report to bugs [at] darcs.net.</p>
<h2>SEE ALSO</h2>
<p> A user manual is included with Darcs, in PDF and HTML form. It can also be found at <a rel="nofollow" href="http://darcs.net/manual/.">http://darcs.net/manual/.</a></p>
<h2>LICENSE</h2>
<p> Darcs is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<h2>Index</h2>
