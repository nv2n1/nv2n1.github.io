---
title: "git-ls-files(1)"
name: "git-ls-files"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-ls-files/"
description: "git-ls-files – Show information about files in the index and the working tree"
---

<h2 class="name">NAME</h2>
<p> git-ls-files &#8211; Show information about files in the index and the working tree </p>
<h2>SYNOPSIS</h2>
<pre><code>
git ls - files[-z][-t][-v][-f](--[cached | deleted | others | ignored | stage | unmerged | killed | modified]) *
             (-[c | d | o | i | s | u | k | m]) *
             [--eol]
                 [--deduplicate]
                 [-x&lt;pattern&gt; | --exclude = &lt;pattern&gt;]
                 [-X&lt;file&gt; | --exclude - from = &lt;file&gt;]
                 [--exclude - per - directory = &lt;file&gt;]
                 [--exclude - standard]
                 [--error - unmatch][--with - tree = &lt;tree - ish&gt;]
                 [--full - name][--recurse - submodules]
                 [--abbrev[=&lt;n&gt;]][--][&lt;file&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This merges the file listing in the index with the actual working directory list, and shows different combinations of the two. </p>
<p> One or more of the options below may be used to determine the files shown:</p>
<h2>OPTIONS</h2>
<p> -c, &#8211;cached</p>
<dl>
<dt>
</dt><dd> Show cached files in the output (default)</dd></dl>
<p> -d, &#8211;deleted</p>
<dl>
<dt>
</dt><dd> Show deleted files in the output</dd></dl>
<p> -m, &#8211;modified</p>
<dl>
<dt>
</dt><dd> Show modified files in the output</dd></dl>
<p> -o, &#8211;others</p>
<dl>
<dt>
</dt><dd> Show other (i.e. untracked) files in the output</dd></dl>
<p> -i, &#8211;ignored</p>
<dl>
<dt>
</dt><dd> Show only ignored files in the output. When showing files in the index, print only those matched by an exclude pattern. When showing &quot;other&quot; files, show only those matched by an exclude pattern. Standard ignore rules are not automatically activated, therefore at least one of the <code>&#8211;exclude*</code> options is required.</dd></dl>
<p> -s, &#8211;stage</p>
<dl>
<dt>
</dt><dd> Show staged contents&#8217; mode bits, object name and stage number in the output.</dd></dl>
<p> &#8211;directory</p>
<dl>
<dt>
</dt><dd> If a whole directory is classified as &quot;other&quot;, show just its name (with a trailing slash) and not its whole contents.</dd></dl>
<p> &#8211;no-empty-directory</p>
<dl>
<dt>
</dt><dd> Do not list empty directories. Has no effect without &#8211;directory.</dd></dl>
<p> -u, &#8211;unmerged</p>
<dl>
<dt>
</dt><dd> Show unmerged files in the output (forces &#8211;stage)</dd></dl>
<p> -k, &#8211;killed</p>
<dl>
<dt>
</dt><dd> Show files on the filesystem that need to be removed due to file/directory conflicts for checkout-index to succeed.</dd></dl>
<p> -z</p>
<dl> <dl>
<dd>  \0 line termination on output and do not quote filenames. See OUTPUT below for more information.  </dd></dl>
<p> --deduplicate </p>
<dl>
<dd> <p> When only filenames are shown, suppress duplicates that may come from having multiple stages during a merge, or giving <code>--deleted</code> and <code>--modified</code> option at the same time. When any of the <code>-t</code>, <code>--unmerged</code>, or <code>--stage</code> option is in use, this option has no effect. </p>
 </dd></dl>
<p> -x &lt;pattern&gt;, --exclude=&lt;pattern&gt; </p>
<dl>
<dd> <p> Skip untracked files matching pattern. Note that pattern is a shell wildcard pattern. See EXCLUDE PATTERNS below for more information. </p>
 </dd></dl>
<p> -X &lt;file&gt;, --exclude-from=&lt;file&gt; </p>
<dl>
<dd> <p> Read exclude patterns from &lt;file&gt;; 1 per line. </p>
 </dd></dl>
<p> --exclude-per-directory=&lt;file&gt; </p>
<dl>
<dd> <p> Read additional exclude patterns that apply only to the directory and its subdirectories in &lt;file&gt;. </p>
 </dd></dl>
<p> --exclude-standard </p>
<dl>
<dd> <p> Add the standard Git exclusions: .git/info/exclude, .gitignore in each directory, and the user&#8217;s global exclusion file. </p>
 </dd></dl>
<p> --error-unmatch </p>
<dl>
<dd> <p> If any &lt;file&gt; does not appear in the index, treat this as an error (return 1). </p>
 </dd></dl>
<p> --with-tree=&lt;tree-ish&gt; </p>
<dl>
<dd> <p> When using --error-unmatch to expand the user supplied &lt;file&gt; (i.e. path pattern) arguments to paths, pretend that paths which were removed in the index since the named &lt;tree-ish&gt; are still present. Using this option with <code>-s</code> or <code>-u</code> options does not make any sense. </p>
 </dd></dl>
<p> -t </p>
<dl>
<dd> <p> This feature is semi-deprecated. For scripting purpose, <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) <code>--porcelain</code> and <code><a href="/docs/linux/man/1-git-diff-files/">git-diff-files</a></code>(1) <code>--name-status</code> are almost always superior alternatives, and users should look at <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) <code>--short</code> or <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>--name-status</code> for more user-friendly alternatives. </p>
<p> This option identifies the file status with the following tags (followed by a space) at the start of each line: </p>
<p> H </p>
 </dd>
<dl>
<dd> <p> cached </p>
 </dd></dl>
<p> S </p>
<dl>
<dd> <p> skip-worktree </p>
 </dd></dl>
<p> M </p>
<dl>
<dd> <p> unmerged </p>
 </dd></dl>
<p> R </p>
<dl>
<dd> <p> removed/deleted </p>
 </dd></dl>
<p> C </p>
<dl>
<dd> <p> modified/changed </p>
 </dd></dl>
<p> K </p>
<dl>
<dd> <p> to be killed </p>
 </dd></dl>
<p> ? </p>
<dl>
<dd> <p> other </p>
 </dd></dl>
</dl>
<p> -v </p>
<dl>
<dd> <p> Similar to <code>-t</code>, but use lowercase letters for files that are marked as <i>assume unchanged</i> (see <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1)). </p>
 </dd></dl>
<p> -f </p>
<dl>
<dd> <p> Similar to <code>-t</code>, but use lowercase letters for files that are marked as <i>fsmonitor valid</i> (see <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1)). </p>
 </dd></dl>
<p> --full-name </p>
<dl>
<dd> <p> When run from a subdirectory, the command usually outputs paths relative to the current directory. This option forces paths to be output relative to the project top directory. </p>
 </dd></dl>
<p> --recurse-submodules </p>
<dl>
<dd> <p> Recursively calls ls-files on each active submodule in the repository. Currently there is only support for the --cached mode. </p>
 </dd></dl>
<p> --abbrev[=&lt;n&gt;] </p>
<dl>
<dd> <p> Instead of showing the full 40-byte hexadecimal object lines, show the shortest prefix that is at least <i>&lt;n&gt;</i> hexdigits long that uniquely refers the object. Non default number of digits can be specified with --abbrev=&lt;n&gt;. </p>
 </dd></dl>
<p> --debug </p>
<dl>
<dd> <p> After each line that describes a file, add more data about its cache entry. This is intended to show as much information as possible for manual inspection; the exact format may change at any time. </p>
 </dd></dl>
<p> --eol </p>
<dl>
<dd> <p> Show &lt;eolinfo&gt; and &lt;eolattr&gt; of files. &lt;eolinfo&gt; is the file content identification used by Git when the &quot;text&quot; attribute is &quot;auto&quot; (or not set and core.autocrlf is not false). &lt;eolinfo&gt; is either &quot;-text&quot;, &quot;none&quot;, &quot;lf&quot;, &quot;crlf&quot;, &quot;mixed&quot; or &quot;&quot;. </p>
<p> &quot;&quot; means the file is not a regular file, it is not in the index or not accessible in the working tree. </p>
<p> &lt;eolattr&gt; is the attribute that is used when checking out or committing, it is either &quot;&quot;, &quot;-text&quot;, &quot;text&quot;, &quot;text=auto&quot;, &quot;text eol=lf&quot;, &quot;text eol=crlf&quot;. Since Git 2.10 &quot;text=auto eol=lf&quot; and &quot;text=auto eol=crlf&quot; are supported. </p>
<p> Both the &lt;eolinfo&gt; in the index (&quot;i/&lt;eolinfo&gt;&quot;) and in the working tree (&quot;w/&lt;eolinfo&gt;&quot;) are shown for regular files, followed by the (&quot;attr/&lt;eolattr&gt;&quot;). </p>
 </dd></dl>
<p> -- </p>
<dl>
<dd> <p> Do not interpret any more arguments as options. </p>
 </dd></dl>
<p> &lt;file&gt; </p>
<dl>
<dd> <p> Files to show. If no files are given all files which match the other specified criteria are shown. </p>
 </dd></dl>
<h2>OUTPUT</h2>
<p> <i>git ls-files</i> just outputs the filenames unless <code>--stage</code> is specified in which case it outputs: </p>
<dl>
<dd> <pre><code>[&lt;tag&gt; ]&lt;mode&gt; &lt;object&gt; &lt;stage&gt; &lt;file&gt;
</code></pre>
 </dd></dl>
<p> <i>git ls-files --eol</i> will show i/&lt;eolinfo&gt;&lt;SPACES&gt;w/&lt;eolinfo&gt;&lt;SPACES&gt;attr/&lt;eolattr&gt;&lt;SPACE*&gt;&lt;TAB&gt;&lt;file&gt; </p>
<p> <i>git ls-files --unmerged</i> and <i>git ls-files --stage</i> can be used to examine detailed information on unmerged paths. </p>
<p> For an unmerged path, instead of recording a single mode/SHA-1 pair, the index records up to three such pairs; one from tree O in stage 1, A in stage 2, and B in stage 3. This information can be used by the user (or the porcelain) to see what should eventually be recorded at the path. (see <code><a href="/docs/linux/man/1-git-read-tree/">git-read-tree</a></code>(1) for more information on state) </p>
<p> Without the <code>-z</code> option, pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). Using <code>-z</code> the filename is output verbatim and the line is terminated by a NUL byte.  </p>
<h2>EXCLUDE PATTERNS</h2>
<p> <i>git ls-files</i> can use a list of &quot;exclude patterns&quot; when traversing the directory tree and finding files to show when the flags --others or --ignored are specified. <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5) specifies the format of exclude patterns. </p>
<p> These exclude patterns come from these places, in order: </p>
<dl>
<dd> <p> 1. The command-line flag --exclude=&lt;pattern&gt; specifies a single pattern. Patterns are ordered in the same order they appear in the command line. </p>
 </dd></dl>
<dl>
<dd> <p> 2. The command-line flag --exclude-from=&lt;file&gt; specifies a file containing a list of patterns. Patterns are ordered in the same order they appear in the file. </p>
 </dd></dl>
<dl>
<dd> <p> 3. The command-line flag --exclude-per-directory=&lt;name&gt; specifies a name of the file in each directory <i>git ls-files</i> examines, normally <code>.gitignore</code>. Files in deeper directories take precedence. Patterns are ordered in the same order they appear in the files. </p>
 </dd></dl>
<p> A pattern specified on the command line with --exclude or read from the file specified with --exclude-from is relative to the top of the directory tree. A pattern read from a file specified by --exclude-per-directory is relative to the directory that the pattern file appears in.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-read-tree/">git-read-tree</a></code>(1), <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)  </p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
