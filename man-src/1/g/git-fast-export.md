---
title: "git-fast-export(1)"
name: "git-fast-export"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-fast-export/"
description: "git-fast-export – Git data exporter"
---

<h2 class="name">NAME</h2>
<p> git-fast-export &#8211; Git data exporter </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git fast-export [&lt;options&gt;]</i> | <i>git fast-import</i>
</pre>
<h2>DESCRIPTION</h2>
<p> This program dumps the given revisions in a form suitable to be piped into <i>git fast-import</i>. </p>
<p> You can use it as a human-readable bundle replacement (see <code><a href="/docs/linux/man/1-git-bundle/">git-bundle</a></code>(1)), or as a format that can be edited before being fed to <i>git fast-import</i> in order to do history rewrites (an ability relied on by tools like <i>git filter-repo</i>).</p>
<h2>OPTIONS</h2>
<p> &#8211;progress=&lt;n&gt;</p>
<dl>
<dt>
<dd> Insert <i>progress</i> statements every &lt;n&gt; objects, to be shown by <i>git fast-import</i> during import.</dl>
<p> &#8211;signed-tags=(verbatim|warn|warn-strip|strip|abort)</p>
<dl>
<dt>
<dd> Specify how to handle signed tags. Since any transformation after the export can change the tag names (which can also happen when excluding revisions) the signatures will not match. </p>
<p> When asking to <i>abort</i> (which is the default), this program will die when encountering a signed tag. With <i>strip</i>, the tags will silently be made unsigned, with <i>warn-strip</i> they will be made unsigned but a warning will be displayed, with <i>verbatim</i>, they will be silently exported and with <i>warn</i>, they will be exported, but you will see a warning.</dl>
<p> &#8211;tag-of-filtered-object=(abort|drop|rewrite)</p>
<dl>
<dt>
<dd> Specify how to handle tags whose tagged object is filtered out. Since revisions and files to export can be limited by path, tagged objects may be filtered completely. </p>
<p> When asking to <i>abort</i> (which is the default), this program will die when encountering such a tag. With <i>drop</i> it will omit such tags from the output. With <i>rewrite</i>, if the tagged object is a commit, it will rewrite the tag to tag an ancestor commit (via parent rewriting; see <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1))</dl>
<p> -M, -C</p>
<dl>
<dt>
<dd> Perform move and/or copy detection, as described in the <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) manual page, and use it to generate rename and copy commands in the output dump. </p>
<p> Note that earlier versions of this command did not complain and produced incorrect results if you gave these options.</dl>
<p> &#8211;export-marks=&lt;file&gt;</p>
<dl>
<dt>
<dd> Dumps the internal marks table to &lt;file&gt; when complete. Marks are written one per line as <code>:markid SHA-1</code>. Only marks for revisions are dumped; marks for blobs are ignored. Backends can use this file to validate imports after they have been completed, or to save the marks table across incremental runs. As &lt;file&gt; is only opened and truncated at completion, the same path can also be safely given to &#8211;import-marks. The file will not be written if no new object has been marked/exported.</dl>
<p> &#8211;import-marks=&lt;file&gt;</p>
<dl>
<dt>
<dd> Before processing any input, load the marks specified in &lt;file&gt;. The input file must exist, must be readable, and must use the same format as produced by &#8211;export-marks.</dl>
<p> &#8211;mark-tags</p>
<dl>
<dt>
<dd> In addition to labelling blobs and commits with mark ids, also label tags. This is useful in conjunction with <code>&#8211;export-marks</code> and <code>&#8211;import-marks</code>, and is also useful (and necessary) for exporting of nested tags. It does not hurt other cases and would be the default, but many fast-import frontends are not prepared to accept tags with mark identifiers. </p>
<p> Any commits (or tags) that have already been marked will not be exported again. If the backend uses a similar &#8211;import-marks file, this allows for incremental bidirectional exporting of the repository by keeping the marks the same across runs.</dl>
<p> &#8211;fake-missing-tagger</p>
<dl>
<dt>
<dd> Some old repositories have tags without a tagger. The fast-import protocol was pretty strict about that, and did not allow that. So fake a tagger to be able to fast-import the output.</dl>
<p> &#8211;use-done-feature</p>
<dl>
<dt>
<dd> Start the stream with a <i>feature done</i> stanza, and terminate it with a <i>done</i> command.</dl>
<p> &#8211;no-data</p>
<dl>
<dt>
<dd> Skip output of blob objects and instead refer to blobs via their original SHA-1 hash. This is useful when rewriting the directory structure or history of a repository without touching the contents of individual files. Note that the resulting stream can only be used by a repository which already contains the necessary objects.</dl>
<p> &#8211;full-tree</p>
<dl>
<dt>
<dd> This option will cause fast-export to issue a &quot;deleteall&quot; directive for each commit followed by a full list of all files in the commit (as opposed to just listing the files which are different from the commit&#8217;s first parent).</dl>
<p> &#8211;anonymize</p>
<dl>
<dt>
<dd> Anonymize the contents of the repository while still retaining the shape of the history and stored tree. See the section on <code>ANONYMIZING</code> below.</dl>
<p> &#8211;anonymize-map=&lt;from&gt;[:&lt;to&gt;]</p>
<dl>
<dt>
<dd> Convert token <code>&lt;from&gt;</code> to <code>&lt;to&gt;</code> in the anonymized output. If <code>&lt;to&gt;</code> is omitted, map <code>&lt;from&gt;</code> to itself (i.e., do not anonymize it). See the section on <code>ANONYMIZING</code> below.</dl>
<p> &#8211;reference-excluded-parents</p>
<dl>
<dt>
<dd> By default, running a command such as <code>git fast-export master~5..master</code> will not include the commit master~5 and will make master~4 no longer have master~5 as a parent (though both the old master~4 and new master~4 will have all the same files). Use &#8211;reference-excluded-parents to instead have the stream refer to commits in the excluded range of history by their sha1sum. Note that the resulting stream can only be used by a repository which already contains the necessary parent commits.</dl>
<p> &#8211;show-original-ids</p>
<dl>
<dt>
<dd> Add an extra directive to the output for commits and blobs, <code>original-oid &lt;SHA1SUM&gt;</code>. While such directives will likely be ignored by importers such as git-fast-import, it may be useful for intermediary filters (e.g. for rewriting commit messages which refer to older commits, or for stripping blobs by id).</dl>
<p> &#8211;reencode=(yes|no|abort)</p>
<dl>
<dt>
<dd> Specify how to handle <code>encoding</code> header in commit objects. When asking to <i>abort</i> (which is the default), this program will die when encountering such a commit object. With <i>yes</i>, the commit message will be re-encoded into UTF-8. With <i>no</i>, the original encoding will be preserved.</dl>
<p> &#8211;refspec</p>
<dl>
<dt>
<dd> Apply the specified refspec to each ref exported. Multiple of them can be specified.</dl>
<p> [&lt;git-rev-list-args&gt;&#8230;]</p>
<dl>
<dt>
<dd> A list of arguments, acceptable to <i>git rev-parse</i> and <i>git rev-list</i>, that specifies the specific objects and references to export. For example, <code>master~10..master</code> causes the current master reference to be exported along with all objects added since its 10th ancestor commit and (unless the &#8211;reference-excluded-parents option is specified) all files common to master~9 and master~10.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ git fast-export --all | (cd /empty/repository &amp;&amp; git fast-import)
</pre>
</dl>
<p> This will export the whole repository and import it into the existing empty repository. Except for reencoding commits that are not in UTF-8, it would be a one-to-one mirror. </p>
<dl>
<dt>
<dd>
<pre>
$ git fast-export master~5..master |
        sed &quot;s|refs/heads/master|refs/heads/other|&quot; |
        git fast-import
</pre>
</dl>
<p> This makes a new branch called <i>other</i> from <i>master~5..master</i> (i.e. if <i>master</i> has linear history, it will take the last 5 commits). </p>
<p> Note that this assumes that none of the blobs and commit messages referenced by that revision range contains the string <i>refs/heads/master</i>.</p>
<h2>ANONYMIZING</h2>
<p> If the <code>&#8211;anonymize</code> option is given, git will attempt to remove all identifying information from the repository while still retaining enough of the original tree and history patterns to reproduce some bugs. The goal is that a git bug which is found on a private repository will persist in the anonymized repository, and the latter can be shared with git developers to help solve the bug. </p>
<p> With this option, git will replace all refnames, paths, blob contents, commit and tag messages, names, and email addresses in the output with anonymized data. Two instances of the same string will be replaced equivalently (e.g., two commits with the same author will have the same anonymized author in the output, but bear no resemblance to the original author string). The relationship between commits, branches, and tags is retained, as well as the commit timestamps (but the commit messages and refnames bear no resemblance to the originals). The relative makeup of the tree is retained (e.g., if you have a root tree with 10 files and 3 trees, so will the output), but their names and the contents of the files will be replaced. </p>
<p> If you think you have found a git bug, you can start by exporting an anonymized stream of the whole repository: </p>
<dl>
<dt>
<dd>
<pre>
$ git fast-export --anonymize --all &gt;anon-stream
</pre>
</dl>
<p> Then confirm that the bug persists in a repository created from that stream (many bugs will not, as they really do depend on the exact repository contents): </p>
<dl>
<dt>
<dd>
<pre>
$ git init anon-repo
$ cd anon-repo
$ git fast-import &lt;../anon-stream
$ ... test your bug ...
</pre>
</dl>
<p> If the anonymized repository shows the bug, it may be worth sharing <code>anon-stream</code> along with a regular bug report. Note that the anonymized stream compresses very well, so gzipping it is encouraged. If you want to examine the stream to see that it does not contain any private data, you can peruse it directly before sending. You may also want to try: </p>
<dl>
<dt>
<dd>
<pre>
$ perl -pe 's/\d+/X/g' &lt;anon-stream | sort -u | less
</pre>
</dl>
<p> which shows all of the unique lines (with numbers converted to &quot;X&quot;, to collapse &quot;User 0&quot;, &quot;User 1&quot;, etc into &quot;User X&quot;). This produces a much smaller output, and it is usually easy to quickly confirm that there is no private data in the stream. </p>
<p> Reproducing some bugs may require referencing particular commits or paths, which becomes challenging after refnames and paths have been anonymized. You can ask for a particular token to be left as-is or mapped to a new value. For example, if you have a bug which reproduces with <code>git rev-list sensitive &#8212; secret.c</code>, you can run: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git fast - export --anonymize-- all-- anonymize - map = sensitive : foo-- anonymize - map = secret.c : bar.c &gt; stream
</code></pre>
</dl>
<p> After importing the stream, you can then run <code>git rev-list foo &#8212; bar.c</code> in the anonymized repository. </p>
<p> Note that paths and refnames are split into tokens at slash boundaries. The command above would anonymize <code>subdir/secret.c</code> as something like <code>path123/bar.c</code>; you could then search for <code>bar.c</code> in the anonymized repository to determine the final pathname. </p>
<p> To make referencing the final pathname simpler, you can map each path component; so if you also anonymize <code>subdir</code> to <code>publicdir</code>, then the final pathname would be <code>publicdir/bar.c</code>.</p>
<h2>LIMITATIONS</h2>
<p> Since <i>git fast-import</i> cannot tag trees, you will not be able to export the linux.git repository completely, as it contains a tag referencing a tree instead of a commit.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-fast-import/">git-fast-import</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
