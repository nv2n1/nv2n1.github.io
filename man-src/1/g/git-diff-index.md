---
title: "git-diff-index(1)"
name: "git-diff-index"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-diff-index/"
description: "git-diff-index – Compare a tree to the working tree or index"
---

<h2 class="name">NAME</h2>
<p> git-diff-index &#8211; Compare a tree to the working tree or index </p>
<h2>SYNOPSIS</h2>
<pre><code>
git diff - index[-m][--cached][--merge - base][&lt;common diff options&gt;]&lt;tree - ish&gt;[&lt;path&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Compares the content and mode of the blobs found in a tree object with the corresponding tracked files in the working tree, or with the corresponding paths in the index. When &lt;path&gt; arguments are present, compares only paths matching those patterns. Otherwise all tracked files are compared.</p>
<h2>OPTIONS</h2>
<p> -p, -u, &#8211;patch</p>
<dl>
<dt>
<dd> Generate patch (see section on generating patches).</dl>
<p> -s, &#8211;no-patch</p>
<dl>
<dt>
<dd> Suppress diff output. Useful for commands like <code>git show</code> that show the patch by default, or to cancel the effect of <code>&#8211;patch</code>.</dl>
<p> -U&lt;n&gt;, &#8211;unified=&lt;n&gt;</p>
<dl>
<dt>
<dd> Generate diffs with &lt;n&gt; lines of context instead of the usual three. Implies <code>&#8211;patch</code>.</dl>
<p> &#8211;output=&lt;file&gt;</p>
<dl>
<dt>
<dd> Output to a specific file instead of stdout.</dl>
<p> &#8211;output-indicator-new=&lt;char&gt;, &#8211;output-indicator-old=&lt;char&gt;, &#8211;output-indicator-context=&lt;char&gt;</p>
<dl>
<dt>
<dd> Specify the character used to indicate new, old or context lines in the generated patch. Normally they are <i>+</i>, <i>&#8211;</i> and &#8216; &#8216; respectively.</dl>
<p> &#8211;raw</p>
<dl>
<dt>
<dd> Generate the diff in raw format. This is the default.</dl>
<p> &#8211;patch-with-raw</p>
<dl>
<dt>
<dd> Synonym for <code>-p &#8211;raw</code>.</dl>
<p> &#8211;indent-heuristic</p>
<dl>
<dt>
<dd> Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default.</dl>
<p> &#8211;no-indent-heuristic</p>
<dl>
<dt>
<dd> Disable the indent heuristic.</dl>
<p> &#8211;minimal</p>
<dl>
<dt>
<dd> Spend extra time to make sure the smallest possible diff is produced.</dl>
<p> &#8211;patience</p>
<dl>
<dt>
<dd> Generate a diff using the &quot;patience diff&quot; algorithm.</dl>
<p> &#8211;histogram</p>
<dl>
<dt>
<dd> Generate a diff using the &quot;histogram diff&quot; algorithm.</dl>
<p> &#8211;anchored=&lt;text&gt;</p>
<dl>
<dt>
<dd> Generate a diff using the &quot;anchored diff&quot; algorithm. </p>
<p> This option may be specified more than once. </p>
<p> If a line exists in both the source and destination, exists only once, and starts with this text, this algorithm attempts to prevent it from appearing as a deletion or addition in the output. It uses the &quot;patience diff&quot; algorithm internally.</dl>
<p> &#8211;diff-algorithm={patience|minimal|histogram|myers}</p>
<dl>
<dt>
<dd> Choose a diff algorithm. The variants are as follows: </p>
<p> <code>default</code>, <code>myers</code></p>
<dl>
<dt>
<dd> The basic greedy diff algorithm. Currently, this is the default.</dl>
<p> <code>minimal</code></p>
<dl>
<dt>
<dd> Spend extra time to make sure the smallest possible diff is produced.</dl>
<p> <code>patience</code></p>
<dl>
<dt>
<dd> Use &quot;patience diff&quot; algorithm when generating patches.</dl>
<p> <code>histogram</code></p>
<dl>
<dt>
<dd> This algorithm extends the patience algorithm to &quot;support low-occurrence common elements&quot;.</dl>
<p> For instance, if you configured the <code>diff.algorithm</code> variable to a non-default value and want to use the default one, then you have to use <code>&#8211;diff-algorithm=default</code> option.</dl>
<p> &#8211;stat[=&lt;width&gt;[,&lt;name-width&gt;[,&lt;count&gt;]]]</p>
<dl>
<dt>
<dd> Generate a diffstat. By default, as much space as necessary will be used for the filename part, and the rest for the graph part. Maximum width defaults to terminal width, or 80 columns if not connected to a terminal, and can be overridden by <code>&lt;width&gt;</code>. The width of the filename part can be limited by giving another width <code>&lt;name-width&gt;</code> after a comma. The width of the graph part can be limited by using <code>&#8211;stat-graph-width=&lt;width&gt;</code> (affects all commands generating a stat graph) or by setting <code>diff.statGraphWidth=&lt;width&gt;</code> (does not affect <code>git format-patch</code>). By giving a third parameter <code>&lt;count&gt;</code>, you can limit the output to the first <code>&lt;count&gt;</code> lines, followed by <code>&#8230;</code> if there are more. </p>
<p> These parameters can also be set individually with <code>&#8211;stat-width=&lt;width&gt;</code>, <code>&#8211;stat-name-width=&lt;name-width&gt;</code> and <code>&#8211;stat-count=&lt;count&gt;</code>.</dl>
<p> &#8211;compact-summary</p>
<dl>
<dt>
<dd> Output a condensed summary of extended header information such as file creations or deletions (&quot;new&quot; or &quot;gone&quot;, optionally &quot;+l&quot; if it&#8217;s a symlink) and mode changes (&quot;+x&quot; or &quot;-x&quot; for adding or removing executable bit respectively) in diffstat. The information is put between the filename part and the graph part. Implies <code>&#8211;stat</code>.</dl>
<p> &#8211;numstat</p>
<dl>
<dt>
<dd> Similar to <code>&#8211;stat</code>, but shows number of added and deleted lines in decimal notation and pathname without abbreviation, to make it more machine friendly. For binary files, outputs two <code>&#8211;</code> instead of saying <code>0 0</code>.</dl>
<p> &#8211;shortstat</p>
<dl>
<dt>
<dd> Output only the last line of the <code>&#8211;stat</code> format containing total number of modified files, as well as number of added and deleted lines.</dl>
<p> -X[&lt;param1,param2,&#8230;&gt;], &#8211;dirstat[=&lt;param1,param2,&#8230;&gt;]</p>
<dl>
<dt>
<dd> Output the distribution of relative amount of changes for each sub-directory. The behavior of <code>&#8211;dirstat</code> can be customized by passing it a comma separated list of parameters. The defaults are controlled by the <code>diff.dirstat</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). The following parameters are available: </p>
<p> <code>changes</code></p>
<dl>
<dt>
<dd> Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given.</dl>
<p> <code>lines</code></p>
<dl>
<dt>
<dd> Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive <code>&#8211;dirstat</code> behavior than the <code>changes</code> behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other <code>&#8211;*stat</code> options.</dl>
<p> <code>files</code></p>
<dl>
<dt>
<dd> Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest <code>&#8211;dirstat</code> behavior, since it does not have to look at the file contents at all.</dl>
<p> <code>cumulative</code></p>
<dl>
<dt>
<dd> Count changes in a child directory for the parent directory as well. Note that when using <code>cumulative</code>, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the <code>noncumulative</code> parameter.</dl>
<p> &lt;limit&gt;</p>
<dl>
<dt>
<dd> An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.</dl>
<p> Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: <code>&#8211;dirstat=files,10,cumulative</code>.</dl>
<p> &#8211;cumulative</p>
<dl>
<dt>
<dd> Synonym for &#8211;dirstat=cumulative</dl>
<p> &#8211;dirstat-by-file[=&lt;param1,param2&gt;&#8230;]</p>
<dl>
<dt>
<dd> Synonym for &#8211;dirstat=files,param1,param2&#8230;</dl>
<p> &#8211;summary</p>
<dl>
<dt>
<dd> Output a condensed summary of extended header information such as creations, renames and mode changes.</dl>
<p> &#8211;patch-with-stat</p>
<dl>
<dt>
<dd> Synonym for <code>-p &#8211;stat</code>.</dl>
<p> -z</p>
<dl>
<dt>
<dd> When <code>&#8211;raw</code>, <code>&#8211;numstat</code>, <code>&#8211;name-only</code> or <code>&#8211;name-status</code> has been given, do not munge pathnames and use NULs as output field terminators. </p>
<p> Without this option, pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> &#8211;name-only</p>
<dl>
<dt>
<dd> Show only names of changed files. The file names are often encoded in UTF-8. For more information see the discussion about encoding in the <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) manual page.</dl>
<p> &#8211;name-status</p>
<dl>
<dt>
<dd> Show only names and status of changed files. See the description of the <code>&#8211;diff-filter</code> option on what the status letters mean. Just like <code>&#8211;name-only</code> the file names are often encoded in UTF-8.</dl>
<p> &#8211;submodule[=&lt;format&gt;]</p>
<dl>
<dt>
<dd> Specify how differences in submodules are shown. When specifying <code>&#8211;submodule=short</code> the <i>short</i> format is used. This format just shows the names of the commits at the beginning and end of the range. When <code>&#8211;submodule</code> or <code>&#8211;submodule=log</code> is specified, the <i>log</i> format is used. This format lists the commits in the range like <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1) <code>summary</code> does. When <code>&#8211;submodule=diff</code> is specified, the <i>diff</i> format is used. This format shows an inline diff of the changes in the submodule contents between the commit range. Defaults to <code>diff.submodule</code> or the <i>short</i> format if the config option is unset.</dl>
<p> &#8211;color[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Show colored diff. <code>&#8211;color</code> (i.e. without <i>=&lt;when&gt;</i>) is the same as <code>&#8211;color=always</code>. <i>&lt;when&gt;</i> can be one of <code>always</code>, <code>never</code>, or <code>auto</code>.</dl>
<p> &#8211;no-color</p>
<dl>
<dt>
<dd> Turn off colored diff. It is the same as <code>&#8211;color=never</code>.</dl>
<p> &#8211;color-moved[=&lt;mode&gt;]</p>
<dl>
<dt>
<dd> Moved lines of code are colored differently. The &lt;mode&gt; defaults to <i>no</i> if the option is not given and to <i>zebra</i> if the option with no mode is given. The mode must be one of: </p>
<p> no</p>
<dl>
<dt>
<dd> Moved lines are not highlighted.</dl>
<p> default</p>
<dl>
<dt>
<dd> Is a synonym for <code>zebra</code>. This may change to a more sensible mode in the future.</dl>
<p> plain</p>
<dl>
<dt>
<dd> Any line that is added in one location and was removed in another location will be colored with <i>color.diff.newMoved</i>. Similarly <i>color.diff.oldMoved</i> will be used for removed lines that are added somewhere else in the diff. This mode picks up any moved line, but it is not very useful in a review to determine if a block of code was moved without permutation.</dl>
<p> blocks</p>
<dl>
<dt>
<dd> Blocks of moved text of at least 20 alphanumeric characters are detected greedily. The detected blocks are painted using either the <i>color.diff.{old,new}Moved</i> color. Adjacent blocks cannot be told apart.</dl>
<p> zebra</p>
<dl>
<dt>
<dd> Blocks of moved text are detected as in <i>blocks</i> mode. The blocks are painted using either the <i>color.diff.{old,new}Moved</i> color or <i>color.diff.{old,new}MovedAlternative</i>. The change between the two colors indicates that a new block was detected.</dl>
<p> dimmed-zebra</p>
<dl>
<dt>
<dd> Similar to <i>zebra</i>, but additional dimming of uninteresting parts of moved code is performed. The bordering lines of two adjacent blocks are considered interesting, the rest is uninteresting. <code>dimmed_zebra</code> is a deprecated synonym.</dl>
</dl>
<p> &#8211;no-color-moved</p>
<dl>
<dt>
<dd> Turn off move detection. This can be used to override configuration settings. It is the same as <code>&#8211;color-moved=no</code>.</dl>
<p> &#8211;color-moved-ws=&lt;modes&gt;</p>
<dl>
<dt>
<dd> This configures how whitespace is ignored when performing the move detection for <code>&#8211;color-moved</code>. These modes can be given as a comma separated list: </p>
<p> no</p>
<dl>
<dt>
<dd> Do not ignore whitespace when performing move detection.</dl>
<p> ignore-space-at-eol</p>
<dl>
<dt>
<dd> Ignore changes in whitespace at EOL.</dl>
<p> ignore-space-change</p>
<dl>
<dt>
<dd> Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent.</dl>
<p> ignore-all-space</p>
<dl>
<dt>
<dd> Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none.</dl>
<p> allow-indentation-change</p>
<dl>
<dt>
<dd> Initially ignore any whitespace in the move detection, then group the moved code blocks only into a block if the change in whitespace is the same per line. This is incompatible with the other modes.</dl>
</dl>
<p> &#8211;no-color-moved-ws</p>
<dl>
<dt>
<dd> Do not ignore whitespace when performing move detection. This can be used to override configuration settings. It is the same as <code>&#8211;color-moved-ws=no</code>.</dl>
<p> &#8211;word-diff[=&lt;mode&gt;]</p>
<dl>
<dt>
<dd> Show a word diff, using the &lt;mode&gt; to delimit changed words. By default, words are delimited by whitespace; see <code>&#8211;word-diff-regex</code> below. The &lt;mode&gt; defaults to <i>plain</i>, and must be one of: </p>
<p> color</p>
<dl>
<dt>
<dd> Highlight changed words using only colors. Implies <code>&#8211;color</code>.</dl>
<p> plain</p>
<dl>
<dt>
<dd> Show words as <code>[-removed-]</code> and <code>{+added+}</code>. Makes no attempts to escape the delimiters if they appear in the input, so the output may be ambiguous.</dl>
<p> porcelain</p>
<dl>
<dt>
<dd> Use a special line-based format intended for script consumption. Added/removed/unchanged runs are printed in the usual unified diff format, starting with a <code>+</code>/<code>&#8211;</code>/` ` character at the beginning of the line and extending to the end of the line. Newlines in the input are represented by a tilde <code>~</code> on a line of its own.</dl>
<p> none</p>
<dl>
<dt>
<dd> Disable word diff again.</dl>
<p> Note that despite the name of the first mode, color is used to highlight the changed parts in all modes if enabled.</dl>
<p> &#8211;word-diff-regex=&lt;regex&gt;</p>
<dl>
<dt>
<dd> Use &lt;regex&gt; to decide what a word is, instead of considering runs of non-whitespace to be a word. Also implies <code>&#8211;word-diff</code> unless it was already enabled. </p>
<p> Every non-overlapping match of the &lt;regex&gt; is considered a word. Anything between these matches is considered whitespace and ignored(!) for the purposes of finding differences. You may want to append <code>|[^[:space:]]</code> to your regular expression to make sure that it matches all non-whitespace characters. A match that contains a newline is silently truncated(!) at the newline. </p>
<p> For example, <code>&#8211;word-diff-regex=.</code> will treat each character as a word and, correspondingly, show differences character by character. </p>
<p> The regex can also be set via a diff driver or configuration option, see <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) or <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). Giving it explicitly overrides any diff driver or configuration setting. Diff drivers override configuration settings.</dl>
<p> &#8211;color-words[=&lt;regex&gt;]</p>
<dl>
<dt>
<dd> Equivalent to <code>&#8211;word-diff=color</code> plus (if a regex was specified) <code>&#8211;word-diff-regex=&lt;regex&gt;</code>.</dl>
<p> &#8211;no-renames</p>
<dl>
<dt>
<dd> Turn off rename detection, even when the configuration file gives the default to do so.</dl>
<p> &#8211;[no-]rename-empty</p>
<dl>
<dt>
<dd> Whether to use empty blobs as rename source.</dl>
<p> &#8211;check</p>
<dl>
<dt>
<dd> Warn if changes introduce conflict markers or whitespace errors. What are considered whitespace errors is controlled by <code>core.whitespace</code> configuration. By default, trailing whitespaces (including lines that consist solely of whitespaces) and a space character that is immediately followed by a tab character inside the initial indent of the line are considered whitespace errors. Exits with non-zero status if problems are found. Not compatible with &#8211;exit-code.</dl>
<p> &#8211;ws-error-highlight=&lt;kind&gt;</p>
<dl>
<dt>
<dd> Highlight whitespace errors in the <code>context</code>, <code>old</code> or <code>new</code> lines of the diff. Multiple values are separated by comma, <code>none</code> resets previous values, <code>default</code> reset the list to <code>new</code> and <code>all</code> is a shorthand for <code>old,new,context</code>. When this option is not given, and the configuration variable <code>diff.wsErrorHighlight</code> is not set, only whitespace errors in <code>new</code> lines are highlighted. The whitespace errors are colored with <code>color.diff.whitespace</code>.</dl>
<p> &#8211;full-index</p>
<dl>
<dt>
<dd> Instead of the first handful of characters, show the full pre- and post-image blob object names on the &quot;index&quot; line when generating patch format output.</dl>
<p> &#8211;binary</p>
<dl>
<dt>
<dd> In addition to <code>&#8211;full-index</code>, output a binary diff that can be applied with <code>git-apply</code>. Implies <code>&#8211;patch</code>.</dl>
<p> &#8211;abbrev[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Instead of showing the full 40-byte hexadecimal object name in diff-raw format output and diff-tree header lines, show the shortest prefix that is at least <i>&lt;n&gt;</i> hexdigits long that uniquely refers the object. In diff-patch output format, <code>&#8211;full-index</code> takes higher precedence, i.e. if <code>&#8211;full-index</code> is specified, full blob names will be shown regardless of <code>&#8211;abbrev</code>. Non default number of digits can be specified with <code>&#8211;abbrev=&lt;n&gt;</code>.</dl>
<p> -B[&lt;n&gt;][/&lt;m&gt;], &#8211;break-rewrites[=[&lt;n&gt;][/&lt;m&gt;]]</p>
<dl>
<dt>
<dd> Break complete rewrite changes into pairs of delete and create. This serves two purposes: </p>
<p> It affects the way a change that amounts to a total rewrite of a file not as a series of deletion and insertion mixed together with a very few lines that happen to match textually as the context, but as a single deletion of everything old followed by a single insertion of everything new, and the number <code>m</code> controls this aspect of the -B option (defaults to 60%). <code>-B/70%</code> specifies that less than 30% of the original should remain in the result for Git to consider it a total rewrite (i.e. otherwise the resulting patch will be a series of deletion and insertion mixed together with context lines). </p>
<p> When used with -M, a totally-rewritten file is also considered as the source of a rename (usually -M only considers a file that disappeared as the source of a rename), and the number <code>n</code> controls this aspect of the -B option (defaults to 50%). <code>-B20%</code> specifies that a change with addition and deletion compared to 20% or more of the file&#8217;s size are eligible for being picked up as a possible source of a rename to another file.</dl>
<p> -M[&lt;n&gt;], &#8211;find-renames[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Detect renames. If <code>n</code> is specified, it is a threshold on the similarity index (i.e. amount of addition/deletions compared to the file&#8217;s size). For example, <code>-M90%</code> means Git should consider a delete/add pair to be a rename if more than 90% of the file hasn&#8217;t changed. Without a <code>%</code> sign, the number is to be read as a fraction, with a decimal point before it. I.e., <code>-M5</code> becomes 0.5, and is thus the same as <code>-M50%</code>. Similarly, <code>-M05</code> is the same as <code>-M5%</code>. To limit detection to exact renames, use <code>-M100%</code>. The default similarity index is 50%.</dl>
<p> -C[&lt;n&gt;], &#8211;find-copies[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Detect copies as well as renames. See also <code>&#8211;find-copies-harder</code>. If <code>n</code> is specified, it has the same meaning as for <code>-M&lt;n&gt;</code>.</dl>
<p> &#8211;find-copies-harder</p>
<dl>
<dt>
<dd> For performance reasons, by default, <code>-C</code> option finds copies only if the original file of the copy was modified in the same changeset. This flag makes the command inspect unmodified files as candidates for the source of copy. This is a very expensive operation for large projects, so use it with caution. Giving more than one <code>-C</code> option has the same effect.</dl>
<p> -D, &#8211;irreversible-delete</p>
<dl>
<dt>
<dd> Omit the preimage for deletes, i.e. print only the header but not the diff between the preimage and <code>/dev/null</code>. The resulting patch is not meant to be applied with <code>patch</code> or <code>git apply</code>; this is solely for people who want to just concentrate on reviewing the text after the change. In addition, the output obviously lacks enough information to apply such a patch in reverse, even manually, hence the name of the option. </p>
<p> When used together with <code>-B</code>, omit also the preimage in the deletion part of a delete/create pair.</dl>
<p> -l&lt;num&gt;</p>
<dl>
<dt>
<dd> The <code>-M</code> and <code>-C</code> options involve some preliminary steps that can detect subsets of renames/copies cheaply, followed by an exhaustive fallback portion that compares all remaining unpaired destinations to all relevant sources. (For renames, only remaining unpaired sources are relevant; for copies, all original sources are relevant.) For N sources and destinations, this exhaustive check is O(N^2). This option prevents the exhaustive portion of rename/copy detection from running if the number of source/destination files involved exceeds the specified number. Defaults to diff.renameLimit. Note that a value of 0 is treated as unlimited.</dl>
<p> &#8211;diff-filter=[(A|C|D|M|R|T|U|X|B)&#8230;[*]]</p>
<dl>
<dt>
<dd> Select only files that are Added (<code>A</code>), Copied (<code>C</code>), Deleted (<code>D</code>), Modified (<code>M</code>), Renamed (<code>R</code>), have their type (i.e. regular file, symlink, submodule, &#8230;) changed (<code>T</code>), are Unmerged (<code>U</code>), are Unknown (<code>X</code>), or have had their pairing Broken (<code>B</code>). Any combination of the filter characters (including none) can be used. When <code>*</code> (All-or-none) is added to the combination, all paths are selected if there is any file that matches other criteria in the comparison; if there is no file that matches other criteria, nothing is selected. </p>
<p> Also, these upper-case letters can be downcased to exclude. E.g. <code>&#8211;diff-filter=ad</code> excludes added and deleted paths. </p>
<p> Note that not all diffs can feature all types. For instance, diffs from the index to the working tree can never have Added entries (because the set of paths included in the diff is limited by what is in the index). Similarly, copied and renamed entries cannot appear if detection for those types is disabled.</dl>
<p> -S&lt;string&gt;</p>
<dl>
<dt>
<dd> Look for differences that change the number of occurrences of the specified string (i.e. addition/deletion) in a file. Intended for the scripter&#8217;s use. </p>
<p> It is useful when you&#8217;re looking for an exact block of code (like a struct), and want to know the history of that block since it first came into being: use the feature iteratively to feed the interesting block in the preimage back into <code>-S</code>, and keep going until you get the very first version of the block. </p>
<p> Binary files are searched as well.</dl>
<p> -G&lt;regex&gt;</p>
<dl>
<dt>
<dd> Look for differences whose patch text contains added/removed lines that match &lt;regex&gt;. </p>
<p> To illustrate the difference between <code>-S&lt;regex&gt; &#8211;pickaxe-regex</code> and <code>-G&lt;regex&gt;</code>, consider a commit with the following diff in the same file: </p>
<dl>
<dt>
<dd>
+ return frotz(nitfol, two-&gt;ptr, 1, 0);<br />
&#8230; &#8211; hit = frotz(nitfol, mf2.ptr, 1, 0);
</dl>
<p> While <code>git log -G&quot;frotz\(nitfol&quot;</code> will show this commit, <code>git log -S&quot;frotz\(nitfol&quot; &#8211;pickaxe-regex</code> will not (because the number of occurrences of that string did not change). </p>
<p> Unless <code>&#8211;text</code> is supplied patches of binary files without a textconv filter will be ignored. </p>
<p> See the <i>pickaxe</i> entry in <code><a href="/docs/linux/man/7-gitdiffcore/">gitdiffcore</a></code>(7) for more information.</dl>
<p> &#8211;find-object=&lt;object-id&gt;</p>
<dl>
<dt>
<dd> Look for differences that change the number of occurrences of the specified object. Similar to <code>-S</code>, just the argument is different in that it doesn&#8217;t search for a specific string but for a specific object id. </p>
<p> The object can be a blob or a submodule commit. It implies the <code>-t</code> option in <code>git-log</code> to also find trees.</dl>
<p> &#8211;pickaxe-all</p>
<dl>
<dt>
<dd> When <code>-S</code> or <code>-G</code> finds a change, show all the changes in that changeset, not just the files that contain the change in &lt;string&gt;.</dl>
<p> &#8211;pickaxe-regex</p>
<dl>
<dt>
<dd> Treat the &lt;string&gt; given to <code>-S</code> as an extended POSIX regular expression to match.</dl>
<p> -O&lt;orderfile&gt;</p>
<dl>
<dt>
<dd> Control the order in which files appear in the output. This overrides the <code>diff.orderFile</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). To cancel <code>diff.orderFile</code>, use <code>-O/dev/null</code>. </p>
<p> The output order is determined by the order of glob patterns in &lt;orderfile&gt;. All files with pathnames that match the first pattern are output first, all files with pathnames that match the second pattern (but not the first) are output next, and so on. All files with pathnames that do not match any pattern are output last, as if there was an implicit match-all pattern at the end of the file. If multiple pathnames have the same rank (they match the same pattern but no earlier patterns), their output order relative to each other is the normal order. </p>
<p> &lt;orderfile&gt; is parsed as follows: </p>
<dl>
<dt>
<dd> &bull; Blank lines are ignored, so they can be used as separators for readability.</dl>
<dl>
<dt>
<dd> &bull; Lines starting with a hash (&quot;<code>#</code>&quot;) are ignored, so they can be used for comments. Add a backslash (&quot;<code>\</code>&quot;) to the beginning of the pattern if it starts with a hash.</dl>
<dl>
<dt>
<dd> &bull; Each other line contains a single pattern.</dl>
<p> Patterns have the same syntax and semantics as patterns used for <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) without the FNM_PATHNAME flag, except a pathname also matches a pattern if removing any number of the final pathname components matches the pattern. For example, the pattern &quot;<code>foo*bar</code>&quot; matches &quot;<code>fooasdfbar</code>&quot; and &quot;<code>foo/bar/baz/asdf</code>&quot; but not &quot;<code>foobarx</code>&quot;.</dl>
<p> &#8211;skip-to=&lt;file&gt;, &#8211;rotate-to=&lt;file&gt;</p>
<dl>
<dt>
<dd> Discard the files before the named &lt;file&gt; from the output (i.e. <i>skip to</i>), or move them to the end of the output (i.e. <i>rotate to</i>). These were invented primarily for use of the <code>git difftool</code> command, and may not be very useful otherwise.</dl>
<p> -R</p>
<dl>
<dt>
<dd> Swap two inputs; that is, show differences from index or on-disk file to tree contents.</dl>
<p> &#8211;relative[=&lt;path&gt;], &#8211;no-relative</p>
<dl>
<dt>
<dd> When run from a subdirectory of the project, it can be told to exclude changes outside the directory and show pathnames relative to it with this option. When you are not in a subdirectory (e.g. in a bare repository), you can name which subdirectory to make the output relative to by giving a &lt;path&gt; as an argument. <code>&#8211;no-relative</code> can be used to countermand both <code>diff.relative</code> config option and previous <code>&#8211;relative</code>.</dl>
<p> -a, &#8211;text</p>
<dl>
<dt>
<dd> Treat all files as text.</dl>
<p> &#8211;ignore-cr-at-eol</p>
<dl>
<dt>
<dd> Ignore carriage-return at the end of line when doing a comparison.</dl>
<p> &#8211;ignore-space-at-eol</p>
<dl>
<dt>
<dd> Ignore changes in whitespace at EOL.</dl>
<p> -b, &#8211;ignore-space-change</p>
<dl>
<dt>
<dd> Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent.</dl>
<p> -w, &#8211;ignore-all-space</p>
<dl>
<dt>
<dd> Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none.</dl>
<p> &#8211;ignore-blank-lines</p>
<dl>
<dt>
<dd> Ignore changes whose lines are all blank.</dl>
<p> -I&lt;regex&gt;, &#8211;ignore-matching-lines=&lt;regex&gt;</p>
<dl>
<dt>
<dd> Ignore changes whose all lines match &lt;regex&gt;. This option may be specified more than once.</dl>
<p> &#8211;inter-hunk-context=&lt;lines&gt;</p>
<dl>
<dt>
<dd> Show the context between diff hunks, up to the specified number of lines, thereby fusing hunks that are close to each other. Defaults to <code>diff.interHunkContext</code> or 0 if the config option is unset.</dl>
<p> -W, &#8211;function-context</p>
<dl>
<dt>
<dd> Show whole function as context lines for each change. The function names are determined in the same way as <code>git diff</code> works out patch hunk headers (see <i>Defining a custom hunk-header</i> in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)).</dl>
<p> &#8211;exit-code</p>
<dl>
<dt>
<dd> Make the program exit with codes similar to <a href="/docs/linux/man/1-diff/">diff</a>(1). That is, it exits with 1 if there were differences and 0 means no differences.</dl>
<p> &#8211;quiet</p>
<dl>
<dt>
<dd> Disable all output of the program. Implies <code>&#8211;exit-code</code>.</dl>
<p> &#8211;ext-diff</p>
<dl>
<dt>
<dd> Allow an external diff helper to be executed. If you set an external diff driver with <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5), you need to use this option with <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) and friends.</dl>
<p> &#8211;no-ext-diff</p>
<dl>
<dt>
<dd> Disallow external diff drivers.</dl>
<p> &#8211;textconv, &#8211;no-textconv</p>
<dl>
<dt>
<dd> Allow (or disallow) external text conversion filters to be run when comparing binary files. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. Because textconv filters are typically a one-way conversion, the resulting diff is suitable for human consumption, but cannot be applied. For this reason, textconv filters are enabled by default only for <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) and <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), but not for <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) or diff plumbing commands.</dl>
<p> &#8211;ignore-submodules[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Ignore changes to submodules in the diff generation. &lt;when&gt; can be either &quot;none&quot;, &quot;untracked&quot;, &quot;dirty&quot; or &quot;all&quot;, which is the default. Using &quot;none&quot; will consider the submodule modified when it either contains untracked or modified files or its HEAD differs from the commit recorded in the superproject and can be used to override any settings of the <i>ignore</i> option in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) or <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5). When &quot;untracked&quot; is used submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). Using &quot;dirty&quot; ignores all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior until 1.7.0). Using &quot;all&quot; hides all changes to submodules.</dl>
<p> &#8211;src-prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Show the given source prefix instead of &quot;a/&quot;.</dl>
<p> &#8211;dst-prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Show the given destination prefix instead of &quot;b/&quot;.</dl>
<p> &#8211;no-prefix</p>
<dl>
<dt>
<dd> Do not show any source or destination prefix.</dl>
<p> &#8211;line-prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Prepend an additional prefix to every line of output.</dl>
<p> &#8211;ita-invisible-in-index</p>
<dl>
<dt>
<dd> By default entries added by &quot;git add -N&quot; appear as an existing empty file in &quot;git diff&quot; and a new file in &quot;git diff &#8211;cached&quot;. This option makes the entry appear as a new file in &quot;git diff&quot; and non-existent in &quot;git diff &#8211;cached&quot;. This option could be reverted with <code>&#8211;ita-visible-in-index</code>. Both options are experimental and could be removed in future.</dl>
<p> For more detailed explanation on these common options, see also <code><a href="/docs/linux/man/7-gitdiffcore/">gitdiffcore</a></code>(7). </p>
<p> &lt;tree-ish&gt;</p>
<dl>
<dt>
<dd> The id of a tree object to diff against.</dl>
<p> &#8211;cached</p>
<dl>
<dt>
<dd> Do not consider the on-disk file at all.</dl>
<p> &#8211;merge-base</p>
<dl>
<dt>
<dd> Instead of comparing &lt;tree-ish&gt; directly, use the merge base between &lt;tree-ish&gt; and HEAD instead. &lt;tree-ish&gt; must be a commit.</dl>
<p> -m</p>
<dl>
<dt>
<dd> By default, files recorded in the index but not checked out are reported as deleted. This flag makes <i>git diff-index</i> say that all non-checked-out files are up to date.</dl>
<h2>RAW OUTPUT FORMAT</h2>
<p> The raw output format from &quot;git-diff-index&quot;, &quot;git-diff-tree&quot;, &quot;git-diff-files&quot; and &quot;git diff &#8211;raw&quot; are very similar. </p>
<p> These commands all compare two sets of things; what is compared differs: </p>
<p> git-diff-index &lt;tree-ish&gt;</p>
<dl>
<dt>
<dd> compares the &lt;tree-ish&gt; and the files on the filesystem.</dl>
<p> git-diff-index &#8211;cached &lt;tree-ish&gt;</p>
<dl>
<dt>
<dd> compares the &lt;tree-ish&gt; and the index.</dl>
<p> git-diff-tree [-r] &lt;tree-ish-1&gt; &lt;tree-ish-2&gt; [&lt;pattern&gt;&#8230;]</p>
<dl>
<dt>
<dd> compares the trees named by the two arguments.</dl>
<p> git-diff-files [&lt;pattern&gt;&#8230;]</p>
<dl>
<dt>
<dd> compares the index and the files on the filesystem.</dl>
<p> The &quot;git-diff-tree&quot; command begins its output by printing the hash of what is being compared. After that, all the commands print one output line per changed file. </p>
<p> An output line is formatted this way: </p>
<dl>
<dt>
<dd>
<pre>
in-place edit  :100644 100644 bcd1234 0123456 M file0
copy-edit      :100644 100644 abcd123 1234567 C68 file1 file2
rename-edit    :100644 100644 abcd123 1234567 R86 file1 file3
create         :000000 100644 0000000 1234567 A file4
delete         :100644 000000 1234567 0000000 D file5
unmerged       :000000 000000 0000000 0000000 U file6
</pre>
</dl>
<p> That is, from the left to the right: </p>
<dl>
<dt>
<dd> 1. a colon.</dl>
<dl>
<dt>
<dd> 2. mode for &quot;src&quot;; 000000 if creation or unmerged.</dl>
<dl>
<dt>
<dd> 3. a space.</dl>
<dl>
<dt>
<dd> 4. mode for &quot;dst&quot;; 000000 if deletion or unmerged.</dl>
<dl>
<dt>
<dd> 5. a space.</dl>
<dl>
<dt>
<dd> 6. sha1 for &quot;src&quot;; 0{40} if creation or unmerged.</dl>
<dl>
<dt>
<dd> 7. a space.</dl>
<dl>
<dt>
<dd> 8. sha1 for &quot;dst&quot;; 0{40} if creation, unmerged or &quot;look at work tree&quot;.</dl>
<dl>
<dt>
<dd> 9. a space.</dl>
<dl>
<dt>
<dd> 10. status, followed by optional &quot;score&quot; number.</dl>
<dl>
<dt>
<dd> 11. a tab or a NUL when <code>-z</code> option is used.</dl>
<dl>
<dt>
<dd> 12. path for &quot;src&quot;</dl>
<dl>
<dt>
<dd> 13. a tab or a NUL when <code>-z</code> option is used; only exists for C or R.</dl>
<dl>
<dt>
<dd> 14. path for &quot;dst&quot;; only exists for C or R.</dl>
<dl>
<dt>
<dd> 15. an LF or a NUL when <code>-z</code> option is used, to terminate the record.</dl>
<p> Possible status letters are: </p>
<dl>
<dt>
<dd> &bull; A: addition of a file</dl>
<dl>
<dt>
<dd> &bull; C: copy of a file into a new one</dl>
<dl>
<dt>
<dd> &bull; D: deletion of a file</dl>
<dl>
<dt>
<dd> &bull; M: modification of the contents or mode of a file</dl>
<dl>
<dt>
<dd> &bull; R: renaming of a file</dl>
<dl>
<dt>
<dd> &bull; T: change in the type of the file (regular file, symbolic link or submodule)</dl>
<dl>
<dt>
<dd> &bull; U: file is unmerged (you must complete the merge before it can be committed)</dl>
<dl>
<dt>
<dd> &bull; X: &quot;unknown&quot; change type (most probably a bug, please report it)</dl>
<p> Status letters C and R are always followed by a score (denoting the percentage of similarity between the source and target of the move or copy). Status letter M may be followed by a score (denoting the percentage of dissimilarity) for file rewrites. </p>
<p> &lt;sha1&gt; is shown as all 0&#8217;s if a file is new on the filesystem and it is out of sync with the index. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
:100644 100644 5be4a4a 0000000 M file.c
</pre>
</dl>
<p> Without the <code>-z</code> option, pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). Using <code>-z</code> the filename is output verbatim and the line is terminated by a NUL byte.</p>
<h2>DIFF FORMAT FOR MERGES</h2>
<p> &quot;git-diff-tree&quot;, &quot;git-diff-files&quot; and &quot;git-diff &#8211;raw&quot; can take <code>-c</code> or <code>&#8211;cc</code> option to generate diff output also for merge commits. The output differs from the format described above in the following way: </p>
<dl>
<dt>
<dd> 1. there is a colon for each parent</dl>
<dl>
<dt>
<dd> 2. there are more &quot;src&quot; modes and &quot;src&quot; sha1</dl>
<dl>
<dt>
<dd> 3. status is concatenated status characters for each parent</dl>
<dl>
<dt>
<dd> 4. no optional &quot;score&quot; number</dl>
<dl>
<dt>
<dd> 5. tab-separated pathname(s) of the file</dl>
<p> For <code>-c</code> and <code>&#8211;cc</code>, only the destination or final path is shown even if the file was renamed on any side of history. With <code>&#8211;combined-all-paths</code>, the name of the path in each parent is shown followed by the name of the path in the merge commit. </p>
<p> Examples for <code>-c</code> and <code>&#8211;cc</code> without <code>&#8211;combined-all-paths</code>: </p>
<dl>
<dt>
<dd>
<pre>
::100644 100644 100644 fabadb8 cc95eb0 4866510 MM       desc.c
::100755 100755 100755 52b7a2d 6d1ac04 d2ac7d7 RM       bar.sh
::100644 100644 100644 e07d6c5 9042e82 ee91881 RR       phooey.c
</pre>
</dl>
<p> Examples when <code>&#8211;combined-all-paths</code> added to either <code>-c</code> or <code>&#8211;cc</code>: </p>
<dl>
<dt>
<dd>
<pre>
::100644 100644 100644 fabadb8 cc95eb0 4866510 MM       desc.c  desc.c  desc.c
::100755 100755 100755 52b7a2d 6d1ac04 d2ac7d7 RM       foo.sh  bar.sh  bar.sh
::100644 100644 100644 e07d6c5 9042e82 ee91881 RR       fooey.c fuey.c  phooey.c
</pre>
</dl>
<p> Note that <i>combined diff</i> lists only files which were modified from all parents.</p>
<h2>GENERATING PATCH TEXT WITH -P</h2>
<p> Running <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1), <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1), <code><a href="/docs/linux/man/1-git-diff-index/">git-diff-index</a></code>(1), <code><a href="/docs/linux/man/1-git-diff-tree/">git-diff-tree</a></code>(1), or <code><a href="/docs/linux/man/1-git-diff-files/">git-diff-files</a></code>(1) with the <code>-p</code> option produces patch text. You can customize the creation of patch text via the <code>GIT_EXTERNAL_DIFF</code> and the <code>GIT_DIFF_OPTS</code> environment variables (see <code><a href="/docs/linux/man/1-git/">git</a></code>(1)), and the <code>diff</code> attribute (see <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)). </p>
<p> What the -p option produces is slightly different from the traditional diff format: </p>
<dl>
<dt>
<dd> 1. It is preceded with a &quot;git diff&quot; header that looks like this: </p>
<dl>
<dt>
<dd>
<pre>
diff --git a/file1 b/file2
</pre>
</dl>
<p> The <code>a/</code> and <code>b/</code> filenames are the same unless rename/copy is involved. Especially, even for a creation or a deletion, <code>/dev/null</code> is <i>not</i> used in place of the <code>a/</code> or <code>b/</code> filenames. </p>
<p> When rename/copy is involved, <code>file1</code> and <code>file2</code> show the name of the source file of the rename/copy and the name of the file that rename/copy produces, respectively.</dl>
<dl>
<dt>
<dd> 2. It is followed by one or more extended header lines: </p>
<dl>
<dt>
<dd>
<pre>
old mode &lt;mode&gt;
new mode &lt;mode&gt;
deleted file mode &lt;mode&gt;
new file mode &lt;mode&gt;
copy from &lt;path&gt;
copy to &lt;path&gt;
rename from &lt;path&gt;
rename to &lt;path&gt;
similarity index &lt;number&gt;
dissimilarity index &lt;number&gt;
index &lt;hash&gt;..&lt;hash&gt; &lt;mode&gt;
</pre>
</dl>
<p> File modes are printed as 6-digit octal numbers including the file type and file permission bits. </p>
<p> Path names in extended headers do not include the <code>a/</code> and <code>b/</code> prefixes. </p>
<p> The similarity index is the percentage of unchanged lines, and the dissimilarity index is the percentage of changed lines. It is a rounded down integer, followed by a percent sign. The similarity index value of 100% is thus reserved for two equal files, while 100% dissimilarity means that no line from the old file made it into the new one. </p>
<p> The index line includes the blob object names before and after the change. The &lt;mode&gt; is included if the file mode does not change; otherwise, separate lines indicate the old and the new mode.</dl>
<dl>
<dt>
<dd> 3. Pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<dl>
<dt>
<dd> 4. All the <code>file1</code> files in the output refer to files before the commit, and all the <code>file2</code> files refer to files after the commit. It is incorrect to apply each change to each file sequentially. For example, this patch will swap a and b: </p>
<dl>
<dt>
<dd>
<pre>
diff --git a/a b/b
rename from a
rename to b
diff --git a/b b/a
rename from b
rename to a
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 5. Hunk headers mention the name of the function to which the hunk applies. See &quot;Defining a custom hunk-header&quot; in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details of how to tailor to this to specific languages.</dl>
<h2>COMBINED DIFF FORMAT</h2>
<p> Any diff-generating command can take the <code>-c</code> or <code>&#8211;cc</code> option to produce a <i>combined diff</i> when showing a merge. This is the default format when showing merges with <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) or <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1). Note also that you can give suitable <code>&#8211;diff-merges</code> option to any of these commands to force generation of diffs in specific format. </p>
<p> A &quot;combined diff&quot; format looks like this: </p>
<dl>
<dt>
<dd>
diff&#8211; combined describe.c<br />
    index fabadb8,<br />
    cc95eb0..4866510 &#8212; -a / describe.c++ + b / describe.c<br />
                                                @ @ @-98,<br />
    20 &#8211; 98, 12 + 98, 20 @ @ @ return (a_date &gt; b_date) ? -1 : (a_date == b_date) ? 0<br />
                                                                                  : 1;<br />
}<br />
&#8211; static void describe(char *arg) &#8211; static void describe(struct commit *cmit, int last_one)++ static void describe(char *arg, int last_one)<br />
{<br />
    +unsigned char sha1[20];<br />
    +struct commit *cmit;<br />
    struct commit_list *list;<br />
    static int initialized = 0;<br />
    struct commit_name *n;<br />
    +if (get_sha1(arg, sha1) &lt; 0) + usage(describe_usage);<br />
    +cmit = lookup_commit_reference(sha1);<br />
    +if (!cmit) + usage(describe_usage);<br />
    +if (!initialized)<br />
    {<br />
        initialized = 1;<br />
        for_each_ref(get_name);
</dl>
<dl>
<dt>
<dd> 1. It is preceded with a &quot;git diff&quot; header, that looks like this (when the <code>-c</code> option is used): </p>
<dl>
<dt>
<dd>
<pre>
diff --combined file
</pre>
</dl>
<p> or like this (when the <code>&#8211;cc</code> option is used): </p>
<dl>
<dt>
<dd>
<pre>
diff --cc file
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 2. It is followed by one or more extended header lines (this example shows a merge with two parents): </p>
<dl>
<dt>
<dd>
<pre>
index &lt;hash&gt;,&lt;hash&gt;..&lt;hash&gt;
mode &lt;mode&gt;,&lt;mode&gt;..&lt;mode&gt;
new file mode &lt;mode&gt;
deleted file mode &lt;mode&gt;,&lt;mode&gt;
</pre>
</dl>
<p> The <code>mode &lt;mode&gt;,&lt;mode&gt;..&lt;mode&gt;</code> line appears only if at least one of the &lt;mode&gt; is different from the rest. Extended headers with information about detected contents movement (renames and copying detection) are designed to work with diff of two &lt;tree-ish&gt; and are not used by combined diff format.</dl>
<dl>
<dt>
<dd> 3. It is followed by two-line from-file/to-file header </p>
<dl>
<dt>
<dd>
<pre>
--- a/file
+++ b/file
</pre>
</dl>
<p> Similar to two-line header for traditional <i>unified</i> diff format, <code>/dev/null</code> is used to signal created or deleted files. </p>
<p> However, if the &#8211;combined-all-paths option is provided, instead of a two-line from-file/to-file you get a N+1 line from-file/to-file header, where N is the number of parents in the merge commit </p>
<dl>
<dt>
<dd>
<pre><code>
-- -a / file-- - a / file-- - a / file++ + b / file
</code></pre>
</dl>
<p> This extended format can be useful if rename or copy detection is active, to allow you to see the original name of the file in different parents.</dl>
<dl>
<dt>
<dd> 4. Chunk header format is modified to prevent people from accidentally feeding it to <code>patch -p1</code>. Combined diff format was created for review of merge commit changes, and was not meant to be applied. The change is similar to the change in the extended <i>index</i> header: </p>
<dl>
<dt>
<dd>
<pre>
@@@ &lt;from-file-range&gt; &lt;from-file-range&gt; &lt;to-file-range&gt; @@@
</pre>
</dl>
<p> There are (number of parents + 1) <code>@</code> characters in the chunk header for combined diff format.</dl>
<p> Unlike the traditional <i>unified</i> diff format, which shows two files A and B with a single column that has <code>&#8211;</code> (minus &#8212; appears in A but removed in B), <code>+</code> (plus &#8212; missing in A but added to B), or <code>&quot; &quot;</code> (space &#8212; unchanged) prefix, this format compares two or more files file1, file2,&#8230; with one file X, and shows how X differs from each of fileN. One column for each of fileN is prepended to the output line to note how X&#8217;s line is different from it. </p>
<p> A <code>&#8211;</code> character in the column N means that the line appears in fileN but it does not appear in the result. A <code>+</code> character in the column N means that the line appears in the result, and fileN does not have that line (in other words, the line was added, from the point of view of that parent). </p>
<p> In the above example output, the function signature was changed from both files (hence two <code>&#8211;</code> removals from both file1 and file2, plus <code>++</code> to mean one line that was added does not appear in either file1 or file2). Also eight other lines are the same from file1 but do not appear in file2 (hence prefixed with <code>+</code>). </p>
<p> When shown by <code>git diff-tree -c</code>, it compares the parents of a merge commit with the merge result (i.e. file1..fileN are the parents). When shown by <code>git diff-files -c</code>, it compares the two unresolved merge parents with the working tree file (i.e. file1 is stage 2 aka &quot;our version&quot;, file2 is stage 3 aka &quot;their version&quot;).</p>
<h2>OTHER DIFF FORMATS</h2>
<p> The <code>&#8211;summary</code> option describes newly added, deleted, renamed and copied files. The <code>&#8211;stat</code> option adds <a href="/docs/linux/man/1-diffstat/">diffstat</a>(1) graph to the output. These options can be combined with other options, such as <code>-p</code>, and are meant for human consumption. </p>
<p> When showing a change that involves a rename or a copy, <code>&#8211;stat</code> output formats the pathnames compactly by combining common prefix and suffix of the pathnames. For example, a change that moves <code>arch/i386/Makefile</code> to <code>arch/x86/Makefile</code> while modifying 4 lines will be shown like this: </p>
<dl>
<dt>
<dd>
<pre>
arch/{i386 =&gt; x86}/Makefile    |   4 +--
</pre>
</dl>
<p> The <code>&#8211;numstat</code> option gives the <a href="/docs/linux/man/1-diffstat/">diffstat</a>(1) information but is designed for easier machine consumption. An entry in <code>&#8211;numstat</code> output looks like this: </p>
<dl>
<dt>
<dd>
<pre>
1       2       README
3       1       arch/{i386 =&gt; x86}/Makefile
</pre>
</dl>
<p> That is, from left to right: </p>
<dl>
<dt>
<dd> 1. the number of added lines;</dl>
<dl>
<dt>
<dd> 2. a tab;</dl>
<dl>
<dt>
<dd> 3. the number of deleted lines;</dl>
<dl>
<dt>
<dd> 4. a tab;</dl>
<dl>
<dt>
<dd> 5. pathname (possibly with rename/copy information);</dl>
<dl>
<dt>
<dd> 6. a newline.</dl>
<p> When <code>-z</code> output option is in effect, the output is formatted this way: </p>
<dl>
<dt>
<dd>
<pre>
1       2       README NUL
3       1       NUL arch/i386/Makefile NUL arch/x86/Makefile NUL
</pre>
</dl>
<p> That is: </p>
<dl>
<dt>
<dd> 1. the number of added lines;</dl>
<dl>
<dt>
<dd> 2. a tab;</dl>
<dl>
<dt>
<dd> 3. the number of deleted lines;</dl>
<dl>
<dt>
<dd> 4. a tab;</dl>
<dl>
<dt>
<dd> 5. a NUL (only exists if renamed/copied);</dl>
<dl>
<dt>
<dd> 6. pathname in preimage;</dl>
<dl>
<dt>
<dd> 7. a NUL (only exists if renamed/copied);</dl>
<dl>
<dt>
<dd> 8. pathname in postimage (only exists if renamed/copied);</dl>
<dl>
<dt>
<dd> 9. a NUL.</dl>
<p> The extra <code>NUL</code> before the preimage path in renamed case is to allow scripts that read the output to tell if the current record being read is a single-path record or a rename/copy record without reading ahead. After reading added and deleted lines, reading up to <code>NUL</code> would yield the pathname, but if that is <code>NUL</code>, the record will show two paths.</p>
<h2>OPERATING MODES</h2>
<p> You can choose whether you want to trust the index file entirely (using the <code>&#8211;cached</code> flag) or ask the diff logic to show any files that don&#8217;t match the stat state as being &quot;tentatively changed&quot;. Both of these operations are very useful indeed.</p>
<h2>CACHED MODE</h2>
<p> If <code>&#8211;cached</code> is specified, it allows you to ask: </p>
<dl>
<dt>
<dd>
<pre>
show me the differences between HEAD and the current index
contents (the ones I'd write using 'git write-tree')
</pre>
</dl>
<p> For example, let&#8217;s say that you have worked on your working directory, updated some files in the index and are ready to commit. You want to see exactly <code>what</code> you are going to commit, without having to write a new tree object and compare it that way, and to do that, you just do </p>
<dl>
<dt>
<dd>
<pre>
git diff-index --cached HEAD
</pre>
</dl>
<p> Example: let&#8217;s say I had renamed <code>commit.c</code> to <code>git-commit.c</code>, and I had done an <code>update-index</code> to make that effective in the index file. <code>git diff-files</code> wouldn&#8217;t show anything at all, since the index file matches my working directory. But doing a <i>git diff-index</i> does: </p>
<dl>
<dt>
<dd>
<pre>
torvalds [at] ppc970:~/git&gt; git diff-index --cached HEAD
-100644 blob    4161aecc6700a2eb579e842af0b7f22b98443f74        commit.c
+100644 blob    4161aecc6700a2eb579e842af0b7f22b98443f74        git-commit.c
</pre>
</dl>
<p> You can see easily that the above is a rename. </p>
<p> In fact, <code>git diff-index &#8211;cached</code> <code>should</code> always be entirely equivalent to actually doing a <i>git write-tree</i> and comparing that. Except this one is much nicer for the case where you just want to check where you are. </p>
<p> So doing a <code>git diff-index &#8211;cached</code> is basically very useful when you are asking yourself &quot;what have I already marked for being committed, and what&#8217;s the difference to a previous tree&quot;.</p>
<h2>NON-CACHED MODE</h2>
<p> The &quot;non-cached&quot; mode takes a different approach, and is potentially the more useful of the two in that what it does can&#8217;t be emulated with a <i>git write-tree</i> + <i>git diff-tree</i>. Thus that&#8217;s the default mode. The non-cached version asks the question: </p>
<dl>
<dt>
<dd>
<pre>
show me the differences between HEAD and the currently checked out
tree - index contents _and_ files that aren't up to date
</pre>
</dl>
<p> which is obviously a very useful question too, since that tells you what you <code>could</code> commit. Again, the output matches the <i>git diff-tree -r</i> output to a tee, but with a twist. </p>
<p> The twist is that if some file doesn&#8217;t match the index, we don&#8217;t have a backing store thing for it, and we use the magic &quot;all-zero&quot; sha1 to show that. So let&#8217;s say that you have edited <code>kernel/sched.c</code>, but have not actually done a <i>git update-index</i> on it yet &#8211; there is no &quot;object&quot; associated with the new state, and you get: </p>
<dl>
<dt>
<dd>
<pre>
torvalds [at] ppc970:~/v2.6/linux&gt; git diff-index --abbrev HEAD
:100644 100664 7476bb... 000000...      kernel/sched.c
</pre>
</dl>
<p> i.e., it shows that the tree has changed, and that <code>kernel/sched.c</code> is not up to date and may contain new stuff. The all-zero sha1 means that to get the real diff, you need to look at the object in the working directory directly rather than do an object-to-object diff. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> As with other commands of this type, <i>git diff-index</i> does not actually look at the contents of the file at all. So maybe <code>kernel/sched.c</code> hasn&#8217;t actually changed, and it&#8217;s just that you touched it. In either case, it&#8217;s a note that you need to <i>git update-index</i> it to make the index be in sync. </p>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> You can have a mixture of files show up as &quot;has been updated&quot; and &quot;is still dirty in the working directory&quot; together. You can always tell which file is in which state, since the &quot;has been updated&quot; ones show a valid sha1, and the &quot;not in sync with the index&quot; ones will always have the special all-zero sha1. </p>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
