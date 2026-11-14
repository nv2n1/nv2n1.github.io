---
title: "reposurgeon(1)"
name: "reposurgeon"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reposurgeon/"
description: "reposurgeon – surgical operations on repositories"
---

<h2 class="name">NAME</h2>
<p> reposurgeon &#8211; surgical operations on repositories </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>reposurgeon</code> [<i>command</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>The purpose of <code>reposurgeon</code> is to enable risky operations that VCSes (version-control systems) don&#8217;t want to let you do, such as (a) editing past comments and metadata, (b) excising commits, (c) coalescing and splitting commits, (d) removing files and subtrees from repo history, (e) merging or grafting two or more repos, and (f) cutting a repo in two by cutting a parent-child link, preserving the branch structure of both child repos. </p>
<p> A major use of reposurgeon is to assist a human operator to perform higher-quality conversions among version control systems than can be achieved with fully automated converters. </p>
<p> The original motivation for <code>reposurgeon</code> was to clean up artifacts created by repository conversions. It was foreseen that the tool would also have applications when code needs to be removed from repositories for legal or policy reasons. </p>
<p> To keep <code>reposurgeon</code> simple and flexible, it normally does not do its own repository reading and writing. Instead, it relies on being able to parse and emit the command streams created by git-fast-export and read by git-fast-import. This means that it can be used on any version-control system that has both fast-export and fast-import utilities. The git-import stream format also implicitly defines a common language of primitive operations for <code>reposurgeon</code> to speak. </p>
<p> Fully supported systems (those for which <code>reposurgeon</code> can both read and write repositories) include git, hg, bzr, svn, darcs, bk, RCS, and SRC. For a complete list, with dependencies and technical notes, type <code>prefer</code> to the <code>reposurgeon</code> prompt. </p>
<p> Writing to the file-oriented systems RCS and SRC is done via <code><a href="/docs/linux/man/1-rcs-fast-import/">rcs-fast-import</a></code>(1) and has some serious limitations because those systems cannot represent all the metadata in a git-fast-export stream. Consult that tool&#8217;s documentation for details and partial workarounds. </p>
<p> Writing Subversion repositories also has some significant limitations, discussed in the section on Working With Subversion. </p>
<p> Fossil repository files can be read in using the <code>&#8211;format=fossil</code> option of the <code>read</code> command and written out with the <code>&#8211;format=fossil</code> option of the <code>write</code>. Ignore patterns are not translated in either direction. </p>
<p> CVS is supported for read only, not write. For CVS, <code>reposurgeon</code> must be run from within a repository directory (one with a CVSROOT subdirectory). Each module becomes a subdirectory in the the <code>reposurgeon</code> representation of the change history. </p>
<p> In order to deal with version-control systems that do not have fast-export equivalents, <code>reposurgeon</code> can also host extractor code that reads repositories directly. For each version-control system supported through an extractor, <code>reposurgeon</code> uses a small amount of knowledge about the system&#8217;s command-line tools to (in effect) replay repository history into an input stream internally. Repositories under systems supported through extractors can be read by <code>reposurgeon</code>, but not modified by it. In particular, <code>reposurgeon</code> can be used to move a repository history from any VCS supported by an extractor to any VCS supported by a normal importer/exporter pair. </p>
<p> Mercurial repository reading is implemented with an extractor class; writing is handled with the stock &quot;hg fastimport&quot; command. A test extractor exists for git, but is normally disabled in favor of the regular exporter. </p>
<p> For guidance on the pragmatics of repository conversion, see the m[blue]<code>DVCS Migration HOWTO</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>SAFETY WARNINGS</h2>
<p> <code>reposurgeon</code> is a sharp enough tool to cut you. It takes care not to ever write a repository in an actually inconsistent state, and will terminate with an error message rather than proceed when its internal data structures are confused. However, there are lots of things you can do with it &#8211; like altering stored commit timestamps so they no longer match the commit sequence &#8211; that are likely to cause havoc after you&#8217;re done. Proceed with caution and check your work. </p>
<p> Also note that, if your DVCS does the usual thing of making commit IDs a cryptographic hash of content and parent links, editing a publicly-accessible repository with this tool would be a bad idea. All of the surgical operations in <code>reposurgeon</code> will modify the hash chains. </p>
<p> Please also see the notes on system-specific issues under the section called &#8220;LIMITATIONS AND GUARANTEES&#8221;.</p>
<h2>OPERATION</h2>
<p> The program can be run in one of two modes, either as an interactive command interpreter or in batch mode to execute commands given as arguments on the <code>reposurgeon</code> invocation line. The only differences between these modes are (1) the interactive one begins by turning on the &#8216;verbose 1&#8217; option, (2) in batch mode all errors (including normally recoverable errors in selection-set syntax) are fatal, and (3) each command-line argument beginning with &#8220;&#8211;&#8221; has that stripped off (which, in particular means that &#8211;help and &#8211;version will work as expected). Also, in interactive mode, Ctrl-P and Ctrl-N will be available to scroll through your command history and tab completion of both command keywords and name arguments (wherever that makes semantic sense) is available. </p>
<p> A git-fast-import stream consists of a sequence of commands which must be executed in the specified sequence to build the repo; to avoid confusion with <code>reposurgeon</code> commands we will refer to the stream commands as <i>events</i> in this documentation. These events are implicitly numbered from 1 upwards. Most commands require specifying a selection of event sequence numbers so <code>reposurgeon</code> will know which events to modify or delete. </p>
<p> For all the details of event types and semantics, see the <code><a href="/docs/linux/man/1-git-fast-import/">git-fast-import</a></code>(1) manual page; the rest of this paragraph is a quick start for the impatient. Most events in a stream are <code>commits</code> describing revision states of the repository; these group together under a single change comment one or more <code>fileops</code> (file operations), which usually point to <code>blobs</code> that are revision states of individual files. A fileop may also be a delete operation indicating that a specified previously-existing file was deleted as part of the version commit; there are a couple of other special fileop types of lesser importance. </p>
<p> Commands to <code>reposurgeon</code> consist of a command keyword, sometimes preceded by a selection set, sometimes followed by whitespace-separated arguments. It is often possible to omit the selection-set argument and have it default to something reasonable. </p>
<p> Here are some motivating examples. The commands will be explained in more detail after the description of selection syntax. </p>
<dl>
<dt>
<dd>
<pre><code>
:15 edit               ;
;
edit the object associated with mark : 15 edit;
;
edit all editable objects 29..71 list;
;
list summary index of events 29..71 236.. $ list;
;
List events from 236 to the last&lt;#523&gt; inspect;
; Look for commit #523;
they are numbered;
;
1 - origin from the beginning of the repository.&lt;2317&gt;inspect;
; Look for a tag with the name 2317, a tip commit
                       ;
;
of a branch named 2317, or a commit with legacy ID;
;
2317. Inspect what is found.A plain number is;
;
probably a legacy ID inherited from a Subversion;
;
revision number./ regression / list;
;
list all commits and tags with comments or
    ;
;
committer headers or author headers containing;
;
the string "regression" 1.. : 97 &amp; = T delete;
;
delete tags from event 1 to mark 97
    [Makefile] inspect;
;
Inspect all commits with a file op touching Makefile;
;
and all blobs referred to in a fileop;
;
touching Makefile. : 46 tip;
;
Display the branch tip that owns commit : 46.
    @dsc( : 55) list;
;
Display all commits with ancestry tracing to : 55
    @min([.gitignore]) remove.gitignore delete;
;
Remove the first.gitignore fileop in the repo.
</code></pre>
</dl>
<h3>SELECTION SYNTAX</h3>
<p> The selection-set specification syntax is an expression-oriented minilanguage. The most basic term in this language is a location. The following sorts of primitive locations are supported: </p>
<p> event numbers</p>
<dl>
<dt>
<dd> A plain numeric literal is interpreted as a 1-origin event-sequence number.</dl>
<p> marks</p>
<dl>
<dt>
<dd> A numeric literal preceded by a colon is interpreted as a mark; see the import stream format documentation for explanation of the semantics of marks.</dl>
<p> tag and branch names</p>
<dl>
<dt>
<dd> The basename of a branch (including branches in the refs/tags namespace) refers to its tip commit. The name of a tag is equivalent to its mark (that of the tag itself, not the commit it refers to). Tag and branch locations are bracketed with &lt; &gt; (angle brackets) to distinguish them from command keywords.</dl>
<p> legacy IDs</p>
<dl>
<dt>
<dd> If the contents of name brackets (&lt; &gt;) does not match a tag or branch name, the interpreter next searches legacy IDs of commits. This is especially useful when you have imported a Subversion dump; it means that commits made from it can be referred to by their corresponding Subversion revision numbers.</dl>
<p> commit numbers</p>
<dl>
<dt>
<dd> A numeric literal within name brackets (&lt; &gt;) preceded by # is interpreted as a 1-origin commit-sequence number.</dl>
<p> $</p>
<dl>
<dt>
<dd> Refers to the last event.</dl>
<p> These may be grouped into sets in the following ways: </p>
<p> ranges</p>
<dl>
<dt>
<dd> A range is two locations separated by &quot;..&quot;, and is the set of events beginning at the left-hand location and ending at the right-hand location (inclusive).</dl>
<p> lists</p>
<dl>
<dt>
<dd> Comma-separated lists of locations and ranges are accepted, with the obvious meaning.</dl>
<p> There are some other ways to construct event sets: </p>
<p> visibility sets</p>
<dl>
<dt>
<dd> A visibility set is an expression specifying a set of event types. It will consist of a leading equal sign, followed by type letters. These are the type letters: <center></p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center> B </td>
<td ALIGN=center> blobs </td>
<td ALIGN=center> Most default selection sets exclude blobs; they have to be manipulated through the commits they are attached to.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> C </td>
<td ALIGN=center> commits </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> D </td>
<td ALIGN=center> all-delete commits </td>
<td ALIGN=center> These are artifacts produced by some older repository-conversion tools.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> H </td>
<td ALIGN=center> head (branch tip) commits </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> O </td>
<td ALIGN=center> orphaned (parentless) commits </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> U </td>
<td ALIGN=center> commits with callouts as parents </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> Z </td>
<td ALIGN=center> commits with no fileops </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> M </td>
<td ALIGN=center> merge (multi-parent) commits </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> F </td>
<td ALIGN=center> fork (multi-child) commits </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> L </td>
<td ALIGN=center> commits with unclean multi-line comments (without a separating empty line after the first) </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> I </td>
<td ALIGN=center> commits for which metadata cannot be decoded to UTF-8 </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> T </td>
<td ALIGN=center> tags </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> R </td>
<td ALIGN=center> resets </td>
<td ALIGN=center> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> P </td>
<td ALIGN=center> Passthrough </td>
<td ALIGN=center> All event types simply passed through, including comments, <code>progress</code> commands, and <code>checkpoint</code> commands.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> N </td>
<td ALIGN=center> Legacy IDs </td>
<td ALIGN=center> Any string matching a cookie (legacy-ID) format.
</td>
</tr>
</table>
<p></center> </p>
</dl>
<p> references</p>
<dl>
<dt>
<dd> A reference name (bracketed by angle brackets) resolves to a single object, either a commit or tag. <center></p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center><code> type </code></td>
<td ALIGN=center><code> interpretation </code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> tag name </td>
<td ALIGN=center> annotated tag with that name
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> branch name </td>
<td ALIGN=center> the branch tip commit
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> legacy ID </td>
<td ALIGN=center> commit with that legacy ID
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> assigned name </td>
<td ALIGN=center> name equated to a selection by assign
</td>
</tr>
</table>
<p></center> </p>
<p> Note that if an annotated tag and a branch have the same name foo, &lt;foo&gt; will resolve to the tag rather than the branch tip commit.</dl>
<p> dates and action stamps</p>
<dl>
<dt>
<dd> A date or action stamp in angle brackets resolves to a selection set of all matching commits. <center></p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center><code> type </code></td>
<td ALIGN=center><code> interpretation </code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> RFC3339 timestamp </td>
<td ALIGN=center> commit or tag with that time/date
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> action stamp (timestamp!email) </td>
<td ALIGN=center> commits or tags with that timestamp and author (or committer if no author).
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> yyyy-mm-dd part of RFC3339 timestamp </td>
<td ALIGN=center> all commits and tags with that date
</td>
</tr>
</table>
<p></center> </p>
<p> To refine the match to a single commit, use a 1-origin index suffix separated by &#8216;#&#8217;. Thus &quot;&lt;2000-02-06T09:35:10Z&gt;&quot; can match multiple commits, but &quot;&lt;2000-02-06T09:35:10Z#2&gt;&quot; matches only the second in the set.</dl>
<p> text search</p>
<dl>
<dt>
<dd> A text search expression is a Python regular expression surrounded by forward slashes (to embed a forward slash in it, use a Python string escape such as /). </p>
<p> A text search normally matches against the comment fields of commits and annotated tags, or against their author/committer names, or against the names of tags; also the text of passthrough objects. </p>
<p> The scope of a text search can be changed with qualifier letters after the trailing slash. These are as follows: <center></p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center><code> letter </code></td>
<td ALIGN=center><code> interpretation </code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> a </td>
<td ALIGN=center> author name in commit
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> b </td>
<td ALIGN=center> branch name in commit; also matches blobs referenced by commits on matching branches, and tags which point to commmits on patching branches.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> c </td>
<td ALIGN=center> comment text of commit or tag
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> r </td>
<td ALIGN=center> committish reference in tag or reset
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> p </td>
<td ALIGN=center> text in passthrough
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> t </td>
<td ALIGN=center> tagger in tag
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> n </td>
<td ALIGN=center> name of tag
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> B </td>
<td ALIGN=center> blob content
</td>
</tr>
</table>
<p></center> </p>
<p> Multiple qualifier letters can add more search scopes. </p>
<p> (The &#8220;b&#8221; qualifier replaces the branchset syntax in earlier versions of <code>reposurgeon</code>.)</dl>
<p> paths</p>
<dl>
<dt>
<dd> A &quot;path expression&quot; enclosed in square brackets resolves to the set of all commits and blobs related to a path matching the given expression. The path expression itself is either a path literal or a regular expression surrounded by slashes. Immediately after the trailing / of a path regexp you can put any number of the following characters which act as flags: &#8216;a&#8217;, &#8216;c&#8217;, &#8216;D&#8217;, &quot;M&#8217;, &#8216;R&#8217;, &#8216;C&#8217;, &#8216;N&#8217;. </p>
<p> By default, a path is related to a commit if the latter has a fileop that touches that file path &#8211; modifies that change it, deletes that remove it, renames and copies that have it as a source or target. When the &#8216;c&#8217; flag is in use the meaning changes: the paths related to a commit become all paths that would be present in a checkout for that commit. </p>
<p> A path literal matches a commit if and only if the path literal is exactly one of the paths related to the commit (no prefix or suffix operation is done). In particular a path literal won&#8217;t match if it corresponds to a directory in the chosen repository. </p>
<p> A regular expression matches a commit if it matches any path related to the commit anywhere in the path. You can use &#8216;^&#8217; or &#8216;$&#8217; if you want the expression to only match at the beginning or end of paths. When the &#8216;a&#8217; flag is in use, the path expression selects commits whose every path matches the regular expression. This is not always a subset of commits selected without the &#8216;a&#8217; flag because it also selects commits with no related paths (e.g. empty commits, deletealls and commits with empty trees). If you want to avoid those, you can use e.g. &#8216;[/regex/] &amp; [/regex/a]&#8217;. </p>
<p> The flags &#8216;D&#8217;, &quot;M&#8217;, &#8216;R&#8217;, &#8216;C&#8217;, &#8216;N&#8217; restrict match checking to the corresponding fileop types. Note that this means an &#8216;a&#8217; match is easier (not harder) to achieve. These are no-iops when used with &#8216;c&#8217;. </p>
<p> A path or literal matches a blob if it matches any path that appeared in a modification fileop that referred to that blob. To select purely matching blobs or matching commits, compose a path expression with =B or =C. </p>
<p> If you need to embed &#8216;[^/]&#8217; into your regular expression (e.g. to express &quot;all characters but a slash&quot;) you can use a Python string escape such as /.</dl>
<p> function calls</p>
<dl>
<dt>
<dd> The expression language has named special functions. The sequence for a named function is &#8220;@&#8221; followed by a function name, followed by an argument in parentheses. Presently the following functions are defined: <center></p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center><code> name </code></td>
<td ALIGN=center><code> interpretation </code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> min </td>
<td ALIGN=center> minimum member of a selection set
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> max </td>
<td ALIGN=center> maximum member of a selection set
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> amp </td>
<td ALIGN=center> nonempty selection set becomes all objects, empty set is returned empty
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> par </td>
<td ALIGN=center> all parents of commits in the argument set
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> chn </td>
<td ALIGN=center> all children of commits in the argument set
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> dsc </td>
<td ALIGN=center> all commits descended from the argument set (argument set included)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> anc </td>
<td ALIGN=center> all commits whom the argument set is descended from (argument set included)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> pre </td>
<td ALIGN=center> events before the argument set; empty if the argument set includes the first event.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> suc </td>
<td ALIGN=center> events after the argument set; empty if the argument set includes the last event.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> srt </td>
<td ALIGN=center> sort the argument set by event number.
</td>
</tr>
</table>
<p></center> </p>
</dl>
<p> Set expressions may be combined with the operators | and &amp;; these are, respectively, set union and intersection. The | has lower precedence than intersection, but you may use parentheses &#8216;(&#8216; and &#8216;)&#8217; to group expressions in case there is ambiguity (this replaces the curly brackets used in older versions of the syntax). </p>
<p> Any set operation may be followed by &#8216;?&#8217; to add the set members&#8217; neighbors and referents. This extends the set to include the parents and children of all commits in the set, and the referents of any tags and resets in the set. Each blob reference in the set is replaced by all commit events that refer to it. The &#8216;?&#8217; can be repeated to extend the neighborhood depth. </p>
<p> Do set negation with prefix ~; it has higher precedence than &amp; and | but lower than ?</p>
<h3>IMPORT AND EXPORT</h3>
<p> <code>reposurgeon</code> can hold multiple repository states in core. Each has a name. At any given time, one may be selected for editing. Commands in this group import repositories, export them, and manipulate the in-core list and the selection. </p>
<p> <code>read</code> [&#8211;format=fossil] [<i>directory</i>|<i>&#8211;</i>|<i>&lt;infile</i>]</p>
<dl>
<dt>
<dd> With a directory-name argument, this command attempts to read in the contents of a repository in any supported version-control system under that directory; read with no arguments does this in the current directory. If output is redirected to a plain file, it will be read in as a fast-import stream or Subversion dumpfile. With an argument of &#8220;-&#8220;, this command reads a fast-import stream or Subversion dumpfile from standard input (this will be useful in filters constructed with command-line arguments). </p>
<p> If the contents is a fast-import stream, any &quot;cvs-revision&quot; property on a commit is taken to be a newline-separated list of CVS revision cookies pointing to the commit, and used for reference lifting. </p>
<p> If the contents is a fast-import stream, any &quot;legacy-id&quot; property on a commit is taken to be a legacy ID token pointing to the commit, and used for reference-lifting. </p>
<p> If the read location is a git repository and contains a .git/cvsauthors file (such as is left in place by <code>git cvsimport -A</code>) that file will be read in as if it had been given to the <code>authors read</code> command. </p>
<p> If the read location is a directory, and its repository subdirectory has a file named legacy-map, that file will be read as though passed to a legacy read command. </p>
<p> If the read location is a file and the <code>&#8211;format=fossil</code> is used, the file is interpreted as a Fossil repository. </p>
<p> The just-read-in repo is added to the list of loaded repositories and becomes the current one, selected for surgery. If it was read from a plain file and the file name ends with one of the extensions .fi or .svn, that extension is removed from the load list name. </p>
<p> Note: this command does not take a selection set.</dl>
<p> <code>write</code> [&#8211;legacy] [&#8211;format=fossil] [&#8211;noincremental] [&#8211;callout] [<i>&gt;outfile</i>|<i>&#8211;</i>]</p>
<dl>
<dt>
<dd> Dump selected events as a fast-import stream representing the edited repository; the default selection set is all events. Where to dump to is standard output if there is no argument or the argument is &#8216;-&#8216;, or the target of an output redirect. </p>
<p> Alternatively, if there is no redirect and the argument names a directory, the repository is rebuilt into that directory, with any selection set being ignored; if that target directory is nonempty its contents are backed up to a save directory. </p>
<p> If the write location is a file and the <code>&#8211;format=fossil</code> is used, the file is written in Fossil repository format. </p>
<p> With the <code>&#8211;legacy</code> option, the Legacy-ID of each commit is appended to its commit comment at write time. This option is mainly useful for debugging conversion edge cases. </p>
<p> If you specify a partial selection set such that some commits are included but their parents are not, the output will include incremental dump cookies for each branch with an origin outside the selection set, just before the first reference to that branch in a commit. An incremental dump cookie looks like &quot;refs/heads/foo^0&quot; and is a clue to export-stream loaders that the branch should be glued to the tip of a pre-existing branch of the same name. The <code>&#8211;noincremental</code> option suppresses this behavior. </p>
<p> When you specify a partial selection set, including a commit object forces the inclusion of every blob to which it refers and every tag that refers to it. </p>
<p> Specifying a partial selection may cause a situation in which some parent marks in merges don&#8217;t correspond to commits present in the dump. When this happens and <code>&#8211;callout</code> option was specified, the write code replaces the merge mark with a callout, the action stamp of the parent commit; otherwise the parent mark is omitted. Importers will fail when reading a stream dump with callouts; it is intended to be used by the <code>graft</code> command. </p>
<p> Specifying a write selection set with gaps in it is allowed but unlikely to lead to good results if it is loaded by an importer. </p>
<p> Property extensions will be be omitted from the output if the importer for the preferred repository type cannot digest them. </p>
<p> Note: to examine small groups of commits without the progress meter, use <code>inspect</code>.</dl>
<p> <code>choose</code> [<i>reponame</i>]</p>
<dl>
<dt>
<dd> Choose a named repo on which to operate. The name of a repo is normally the basename of the directory or file it was loaded from, but repos loaded from standard input are &quot;unnamed&quot;. <code>reposurgeon</code> will add a disambiguating suffix if there have been multiple reads from the same source. </p>
<p> With no argument, lists the names of the currently stored repositories and their load times. The second column is &#8216;*&#8217; for the currently selected repository, &#8216;-&#8216; for others.</dl>
<p> <code>drop</code> [<i>reponame</i>]</p>
<dl>
<dt>
<dd> Drop a repo named by the argument from reposurgeon&#8217;s list, freeing the memory used for its metadata and deleting on-disk blobs. With no argument, drops the currently chosen repo.</dl>
<p> <code>rename</code> <i>reponame</i></p>
<dl>
<dt>
<dd> Rename the currently chosen repo; requires an argument. Won&#8217;t do it if there is already one by the new name.</dl>
<h3>REBUILDS IN PLACE</h3>
<p> <code>reposurgeon</code> can rebuild an altered repository in place. Untracked files are normally saved and restored when the contents of the new repository is checked out (but see the documentation of the &#8220;preserve&#8221; command for a caveat). </p>
<p> <code>rebuild</code> [<i>directory</i>]</p>
<dl>
<dt>
<dd> Rebuild a repository from the state held by <code>reposurgeon</code>. This command does not take a selection set. </p>
<p> The single argument, if present, specifies the target directory in which to do the rebuild; if the repository read was from a repo directory (and not a git-import stream), it defaults to that directory. If the target directory is nonempty its contents are backed up to a save directory. Files and directories on the repository&#8217;s preserve list are copied back from the backup directory after repo rebuild. The default preserve list depends on the repository type, and can be displayed with the <code>stats</code> command. </p>
<p> If <code>reposurgeon</code> has a nonempty legacy map, it will be written to a file named legacy-map in the repository subdirectory as though by a legacy write command. (This will normally be the case for Subversion and CVS conversions.)</dl>
<p> <code>preserve</code> [<i>file&#8230;</i>]</p>
<dl>
<dt>
<dd> Add (presumably untracked) files or directories to the repo&#8217;s list of paths to be restored from the backup directory after a <code>rebuild</code>. Each argument, if any, is interpreted as a pathname. The current preserve list is displayed afterwards. </p>
<p> It is only necessary to use this feature if your version-control system lacks a command to list files under version control. Under systems with such a command (which include git and hg), all files that are neither beneath the repository dot directory nor under reposurgeon temporary directories are preserved automatically.</dl>
<p> <code>unpreserve</code> [<i>file&#8230;</i>]</p>
<dl>
<dt>
<dd> Remove (presumably untracked) files or directories to the repo&#8217;s list of paths to be restored from the backup directory after a <code>rebuild</code>. Each argument, if any, is interpreted as a pathname. The current preserve list is displayed afterwards.</dl>
<h3>INFORMATION AND REPORTS</h3>
<p> Commands in this group report information about the selected repository. </p>
<p> The output of these commands can individually be redirected to a named output file. Where indicated in the syntax, you can prefix the output filename with &#8220;&gt;&#8221; and give it as a following argument. If you use &#8220;&gt;&gt;&#8221; the file is opened for append rather than write. </p>
<p> <code>list</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> This is the main command for identifying the events you want to modify. It lists commits in the selection set by event sequence number with summary information. The first column is raw event numbers, the second a timestamp in local time. If the repository has legacy IDs, they will be displayed in the third column. The leading portion of the comment follows.</dl>
<p> <code>stamp</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Alternative form of listing that displays full action stamps, usable as references in selections. Supports &gt; redirection.</dl>
<p> <code>tip</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Display the branch tip names associated with commits in the selection set. These will not necessarily be the same as their branch fields (which will often be tag names if the repo contains either annotated or lightweight tags). </p>
<p> If a commit is at a branch tip, its tip is its branch name. If it has only one child, its tip is the child&#8217;s tip. If it has multiple children, then if there is a child with a matching branch name its tip is the child&#8217;s tip. Otherwise this function throws a recoverable error.</dl>
<p> <code>tags</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Display tags and resets: three fields, an event number and a type and a name. Branch tip commits associated with tags are also displayed with the type field &#8216;commit&#8217;. Supports &gt; redirection.</dl>
<p> <code>stats</code> [<i>repo-name</i>&#8230;] [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Report size statistics and import/export method information about named repositories, or with no argument the currently chosen repository.</dl>
<p> <code>count</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Report a count of items in the selection set. Default set is everything in the currently-selected repo. Supports &gt; redirection.</dl>
<p> <code>inspect</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Dump a fast-import stream representing selected events to standard output. Just like a write, except (1) the progress meter is disabled, and (2) there is an identifying header before each event dump.</dl>
<p> <code>graph</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Emit a visualization of the commit graph in the DOT markup language used by the graphviz tool suite. This can be fed as input to the main graphviz rendering program <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1), which will yield a viewable image. Supports &gt; redirection. </p>
<p> You may find a script like this useful: </p>
<dl>
<dt>
<dd>
<pre>
graph $1 &gt;/tmp/foo$$
shell dot &lt;/tmp/foo$$ -Tpng | display -; rm /tmp/foo$$
</pre>
</dl>
<p> You can substitute in your own preferred image viewer, of course.</dl>
<p> <code>sizes</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Print a report on data volume per branch; takes a selection set, defaulting to all events. The numbers tally the size of uncompressed blobs, commit and tag comments, and other metadata strings (a blob is counted each time a commit points at it). </p>
<p> The numbers are not an exact measure of storage size: they are intended mainly as a way to get information on how to efficiently partition a repository that has become large enough to be unwieldy. </p>
<p> Supports &gt; redirection.</dl>
<p> <code>lint</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Look for DAG and metadata configurations that may indicate a problem. Presently checks for: (1) Mid-branch deletes, (2) disconnected commits, (3) parentless commits, (4) the existence of multiple roots, (5) committer and author IDs that don&#8217;t look well-formed as DVCS IDs, (6) multiple child links with identical branch labels descending from the same commit, (7) time and action-stamp collisions. </p>
<p> Options to issue only partial reports are supported; &quot;lint &#8211;options&quot; or &quot;lint -?&quot; lists them. </p>
<p> The options and output format of this command are unstable; they may change without notice as more sanity checks are added.</dl>
<p> <code>when</code> &gt;<i>timespec</i></p>
<dl>
<dt>
<dd> Interconvert between git timestamps (integer Unix time plus TZ) and RFC3339 format. Takes one argument, autodetects the format. Useful when eyeballing export streams. Also accepts any other supported date format and converts to RFC3339.</dl>
<h3>SURGICAL OPERATIONS</h3>
<p> These are the operations the rest of reposurgeon is designed to support. </p>
<p> <code>squash</code> [<i>policy&#8230;</i>]</p>
<dl>
<dt>
<dd> Combine or delete commits in a selection set of events. The default selection set for this command is empty. Has no effect on events other than commits unless the &#8211;delete policy is selected; see the &#8216;delete&#8217; command for discussion. </p>
<p> Normally, when a commit is squashed, its file operation list (and any associated blob references) gets either prepended to the beginning of the operation list of each of the commit&#8217;s children or appended to the operation list of each of the commit&#8217;s parents. Then children of a deleted commit get it removed from their parent set and its parents added to their parent set. </p>
<p> The default is to squash forward, modifying children; but see the list of policy modifiers below for how to change this. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font><br />
 It is easy to get the bounds of a squash command wrong, with confusing and destructive results. Beware thinking you can squash on a selection set to merge all commits except the last one into the last one; what you will actually do is to merge all of them to the first commit <i>after</i> the selected set. </p>
</dl>
<p> Normally, any tag pointing to a combined commit will also be pushed forward. But see the list of policy modifiers below for how to change this. </p>
<p> Following all operation moves, every one of the altered file operation lists is reduced to a shortest normalized form. The normalized form detects various combinations of modification, deletion, and renaming and simplifies the operation sequence as much as it can without losing any information. </p>
<p> After canonicalization, a file op list may still end up containing multiple M operations on the same file. Normally the tool utters a warning when this occurs but does not try to resolve it. </p>
<p> The following modifiers change these policies: </p>
<p> <code>&#8211;delete</code></p>
<dl>
<dt>
<dd> Simply discards all file ops and tags associated with deleted commit(s).</dl>
<p> <code>&#8211;coalesce</code></p>
<dl>
<dt>
<dd> Discard all M operations (and associated blobs) except the last.</dl>
<p> <code>&#8211;pushback</code></p>
<dl>
<dt>
<dd> Append fileops to parents, rather than prepending to children.</dl>
<p> <code>&#8211;pushforward</code></p>
<dl>
<dt>
<dd> Prepend fileops to children. This is the default; it can be specified in a lift script for explicitness about intentions.</dl>
<p> <code>&#8211;tagforward</code></p>
<dl>
<dt>
<dd> With the &quot;tagforward&quot; modifier, any tag on the deleted commit is pushed forward to the first child rather than being deleted. This is the default; it can be specified for explicitness.</dl>
<p> <code>&#8211;tagback</code></p>
<dl>
<dt>
<dd> With the &quot;&#8211;tagback&quot; modifier, any tag on the deleted commit is pushed backward to the first parent rather than being deleted.</dl>
<p> <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Suppresses warning messages about deletion of commits with non-delete fileops.</dl>
<p> <code>&#8211;complain</code></p>
<dl>
<dt>
<dd> The opposite of quiet. Can be specified for explicitness.</dl>
<p> Under any of these policies except &#8220;&#8211;delete&#8221;, deleting a commit that has children does not back out the changes made by that commit, as they will still be present in the blobs attached to versions past the end of the deletion set. All a delete does when the commit has children is lose the metadata information about when and by who those changes were actually made; after the delete any such changes will be attributed to the first undeleted children of the deleted commits. It is expected that this command will be useful mainly for removing commits mechanically generated by repository converters such as <code>cvs2svn</code>.</dl>
<p> <code>delete</code> [<i>policy&#8230;</i>]</p>
<dl>
<dt>
<dd> Delete a selection set of events. The default selection set for this command is empty. On a set of commits, this is equivalent to a squash with the &#8211;delete flag. It unconditionally deletes tags, resets, and passthroughs; blobs can be removed only as a side effect of deleting every commit that points at them.</dl>
<p> <code>divide</code> <i>parent</i> [<i>child</i>]</p>
<dl>
<dt>
<dd> Attempt to partition a repo by cutting the parent-child link between two specified commits (they must be adjacent). Does not take a general selection set. It is only necessary to specify the parent commit, unless it has multiple children in which case the child commit must follow (separate it with a comma). </p>
<p> If the repo was named &#8216;foo&#8217;, you will normally end up with two repos named &#8216;foo-early&#8217; and &#8216;foo-late&#8217; (option and feature events at the beginning of the early segment will be duplicated onto the beginning of the late one.). But if the commit graph would remain connected through another path after the cut, the behavior changes. In this case, if the parent and child were on the same branch &#8216;qux&#8217;, the branch segments are renamed &#8216;qux-early&#8217; and &#8216;qux-late&#8217; but the repo is not divided.</dl>
<p> <code>expunge</code> <i>[&#8211;notagify] [path | /regexp/]&#8230;</i></p>
<dl>
<dt>
<dd> Expunge files from the selected portion of the repo history; the default is the entire history. The arguments to this command may be paths or Python regular expressions matching paths (regexps must be marked by being surrounded with //). </p>
<p> All filemodify (M) operations and delete (D) operations involving a matched file in the selected set of events are disconnected from the repo and put in a removal set. Renames are followed as the tool walks forward in the selection set; each triggers a warning message. If a selected file is a copy (C) target, the copy will be deleted and a warning message issued. If a selected file is a copy source, the copy target will be added to the list of paths to be deleted and a warning issued. </p>
<p> After file expunges have been performed, any commits with no remaining file operations will be removed, and any tags pointing to them. By default each deleted commit is replaced with a tag of the form &#8217;emptycommit-<i>ident</i>&#8216; on the preceding commit unless &#8211;notagify is specified as an argument. Commits with deleted fileops pointing both in and outside the path set are not deleted, but are cloned into the removal set. </p>
<p> The removal set is not discarded. It is assembled into a new repository named after the old one with the suffix &quot;-expunges&quot; added. Thus, this command can be used to carve a repository into sections by file path matches.</dl>
<p> <code>tagify</code> [<code>&#8211;canonicalize</code>] [<code>&#8211;tipdeletes</code>] [<code>&#8211;tagify-merges</code>]</p>
<dl>
<dt>
<dd> Search for empty commits and turn them into tags. Takes an optional selection set argument defaulting to all commits. For each commit in the selection set, turn it into a tag with the same message and author information if it has no fileops. By default merge commits are not considered, even if they have no fileops (thus no tree differences with their first parent). To change that, use the <code>&#8211;tagify-merges</code> option. </p>
<p> The name of the generated tag will be &#8217;emptycommit-<i>ident</i>&#8216;, where <i>ident</i> is generated from the legacy ID of the deleted commit, or from its mark, or from its index in the repository, with a disambiguation suffix if needed. </p>
<p> With the <code>&#8211;canonicalize</code>, tagify tries harder to detect trivial commits by first ensuring that all fileops of selected commits will have an actual effect when processed by fast-import. </p>
<p> With the <code>&#8211;tipdeletes</code>, tagify also considers branch tips with only deleteall fileops to be candidates for tagification. The corresponding tags get names of the form &#8216;tipdelete-<i>branchname</i>&#8216; rather than the default &#8217;emptycommit-<i>ident</i>&#8216;. </p>
<p> With the <code>&#8211;tagify-merges</code>, tagify also tagifies merge commits that have no fileops. When this is done the merge link is move to the yagified commit&#8217;s parent.</dl>
<p> <code>coalesce</code> [<code>&#8211;debug</code>|<code>&#8211;changelog</code>] [<i>timefuzz</i>]</p>
<dl>
<dt>
<dd> Scan the selection set for runs of commits with identical comments close to each other in time (this is a common form of scar tissues in repository up-conversions from older file-oriented version-control systems). Merge these cliques by deleting all but the last commit, in order; fileops from the deleted commits are pushed forward to that last one </p>
<p> The optional second argument, if present, is a maximum time separation in seconds; the default is 90 seconds. </p>
<p> The default selection set for this command is =C, all commits. Occasionally you may want to restrict it, for example to avoid coalescing unrelated cliques of &quot;*** empty log message ***&quot; commits from CVS lifts. </p>
<p> With the &#8211;debug option, show messages about mismatches. </p>
<p> With the &#8211;changelog option, any commit with a comment containing the string &#8217;empty log message&#8217; (such as is generated by CVS) and containing exactly one file operation modifying a path ending in ChangeLog is treated specially. Such ChangeLog commits are considered to match any commit before them by content, and will coalesce with it if the committer matches and the commit separation is small enough. This option handles a convention used by Free Software Foundation projects.</dl>
<p> <code>split</code> <code>{at|by}</code> <i>item</i></p>
<dl>
<dt>
<dd> The first argument is required to be a commit location; the second is a preposition which indicates which splitting method to use. If the preposition is &#8216;at&#8217;, then the third argument must be an integer 1-origin index of a file operation within the commit. If it is &#8216;by&#8217;, then the third argument must be a pathname to be prefix-matched, pathname match is done first). </p>
<p> The commit is copied and inserted into a new position in the event sequence, immediately following itself; the duplicate becomes the child of the original, and replaces it as parent of the original&#8217;s children. Commit metadata is duplicated; the new commit then gets a new mark. If the new commit has a legacy ID, the suffix &#8216;.split&#8217; is appended to it. </p>
<p> Finally, some file operations &#8211; starting at the one matched or indexed by the split argument &#8211; are moved forward from the original commit into the new one. Legal indices are 2-n, where n is the number of file operations in the original commit.</dl>
<p> <code>add</code> {<i>D</i> <i>path</i> | <i>M</i> <i>perm</i> <i>mark</i> <i>path</i> | <i>R</i> <i>source</i> <i>target</i> | <i>C</i> <i>source</i> <i>target</i>}</p>
<dl>
<dt>
<dd> To a specified commit, add a specified fileop. </p>
<p> For a D operation to be valid there must be an M operation for the path in the commit&#8217;s ancestry. For an M operation to be valid, the &#8216;perm&#8217; part must be a token ending with 755 or 644 and the &#8216;mark&#8217; must refer to a blob that precedes the commit location. For an R or C operation to be valid, there must be an M operation for the source in the commit&#8217;s ancestry.</dl>
<p> <code>remove</code> [<i>index</i> | <i>path</i> | <code>deletes</code>] [<code>to</code> <i>commit</i>]</p>
<dl>
<dt>
<dd> From a specified commit, remove a specified fileop. The op must be one of (a) the keyword &#8220;deletes&#8221;, (b) a file path, (c) a file path preceded by an op type set (some subset of the letters DMRCN), or (d) a 1-origin numeric index. The &#8220;deletes&#8221; keyword selects all D fileops in the commit; the others select one each. </p>
<p> If the &#8220;to&#8221; clause is present, the removed op is appended to the commit specified by the following singleton selection set. This option cannot be combined with &#8220;deletes&#8221;. </p>
<p> Note that this command does not attempt to scavenge blobs even if the deleted fileop might be the only reference to them. This behavior may change in a future release.</dl>
<p> <code>blob</code></p>
<dl>
<dt>
<dd> Create a blob at mark :1 after renumbering other marks starting from :2. Data is taken from stdin, which may be a here-doc. This can be used with the add command to patch synthetic data into a repository.</dl>
<p> <code>renumber</code></p>
<dl>
<dt>
<dd> Renumber the marks in a repository, from :1 up to :&lt;n&gt; where &lt;n&gt; is the count of the last mark. Just in case an importer ever cares about mark ordering or gaps in the sequence. </p>
<p> A side effect of this comment is to clean up stray &quot;done&quot; passthroughs that may have entered the repository via graft operations. After a renumber, the repository will have at most one &quot;done&quot; and it will be at the end of the events.</dl>
<p> <code>mailbox_out</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Emit a mailbox file of messages in RFC822 format representing the contents of repository metadata. Takes a selection set; members of the set other than commits, annotated tags, and passthroughs are ignored (that is, presently, blobs and resets). </p>
<p> The output from this command can optionally be redirected to a named output file. Prefix the filename with &#8220;&gt;&#8221; and give it as a following argument. </p>
<p> May have an option &#8211;filter, followed by = and a /-enclosed regular expression. If this is given, only headers with names matching it are emitted. In this context the name of the header includes its trailing colon.</dl>
<p> <code>mailbox_in</code> [&lt;<i>infile</i>] [<i>&#8211;changed</i> &gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Accept a mailbox file of messages in RFC822 format representing the contents of the metadata in selected commits and annotated tags. Takes no selection set. If there is an argument it will be taken as the name of a mailbox file to read from; no argument, or one of &#8216;-&#8216;; reads from standard input. </p>
<p> Users should be aware that modifying an Event-Number or Event-Mark field will change which event the update from that message is applied to. This is unlikely to have good results. </p>
<p> If the Event-Number and Event-Mark fields are absent, the mailbox_in logic will attempt to match the commit or tag first by Legacy-ID, then by a unique committer ID and timestamp pair. </p>
<p> If output is redirected and the modifier &#8220;&#8211;changed&#8221; appears, a minimal set of modifications actually made is written to the output file in a form that can be fed back in.</dl>
<p> <code>setfield</code> <i>attribute</i> <i>value</i></p>
<dl>
<dt>
<dd> In the selected objects (defaulting to none) set every instance of a named field to a string value. The string may be quoted to include whitespace, and use backslash escapes interpreted by the Python string-escape codec, such as 
 and 	. </p>
<p> Attempts to set nonexistent attributes are ignored. Valid values for the attribute are internal Python field names; in particular, for commits, &#8220;comment&#8221; and &#8220;branch&#8221; are legal. Consult the source code for other interesting values.</dl>
<p> <code>append</code> [<code>&#8211;rstrip</code>] [&gt;<i>text</i>]</p>
<dl>
<dt>
<dd> Append text to the comments of commits and tags in the specified selection set. The text is the first token of the command and may be a quoted string. C-style escape sequences in the string are interpreted using Python&#8217;s string_decode codec. </p>
<p> If the option &#8211;rstrip is given, the comment is right-stripped before the new text is appended.</dl>
<p> <code>filter</code> [<i>&#8211;shell</i>|<i>&#8211;regex</i>|<i>&#8211;replace</i>|<i>&#8211;dedos</i>]</p>
<dl>
<dt>
<dd> Run blobs, commit comments, or tag comments in the selection set through the filter specified on the command line. </p>
<p> In any mode other than &#8211;dedos, attempting to specify a selection set including both blobs and non-blobs (that is, commits or tags) throws an error. Inline content in commits is filtered when the selection set contains (only) blobs and the commit is within the range bounded by the earliest and latest blob in the specification. </p>
<p> When filtering blobs, if the command line contains the magic cookie &#8216;%PATHS%&#8217; it is replaced with a space-separated list of all paths that reference the blob. </p>
<p> With &#8211;shell, the remainder of the line specifies a filter as a shell command. Each blob or comment is presented to the filter on standard input; the content is replaced with whatever the filter emits to standard output. </p>
<p> With &#8211;regex, the remainder of the line is expected to be a Python regular expression substitution written as /from/to/ with from and to being passed as arguments to the standard re.sub() function and it applied to modify the content. Actually, any non-space character will work as a delimiter in place of the /; this makes it easier to use / in patterns. Ordinarily only the first such substitution is performed; putting &#8216;g&#8217; after the slash replaces globally, and a numeric literal gives the maximum number of substitutions to perform. Other flags available restrict substitution scope &#8211; &#8216;c&#8217; for comment text only, &#8216;C&#8217; for committer name only, &#8216;a&#8217; for author names only. Note that parsing of a &#8211;regex argument will be confused by ant substring consisting of whitespace followed by #; use &quot;\s&quot; rather than whitespace to avoid this. </p>
<p> With &#8211;replace, the behavior is like &#8211;regexp but the expressions are not interpreted as regular expressions. (This is slightly faster). </p>
<p> With &#8211;dedos, DOS/Windows-style 
 line terminators are replaced with 
.</dl>
<p> <code>transcode</code> <i>codec</i></p>
<dl>
<dt>
<dd> Transcode blobs, commit comments and committer/author names, or tag comments and tag committer names in the selection set to UTF-8 from the character encoding specified on the command line. </p>
<p> Attempting to specify a selection set including both blobs and non-blobs (that is, commits or tags) throws an error. Inline content in commits is filtered when the selection set contains (only) blobs and the commit is within the range bounded by the earliest and latest blob in the specification. </p>
<p> The encoding argument must name one of the codecs known to the Python standard codecs library. In particular, &#8216;latin-1&#8217; is a valid codec name. </p>
<p> Errors in this command are fatal, because an error may leave repository objects in a damaged state. </p>
<p> The theory behind the design of this command is that the repository might contain a mixture of encodings used to enter commit metadata by different people at different times. After using =I to identify metadata containing non-Unicode high bytes in text, a human must use context to identify which particular encodings were used in particular event spans and compose appropriate transcode commands to fix them up.</dl>
<p> <code>edit</code></p>
<dl>
<dt>
<dd> Report the selection set of events to a tempfile as mailbox_out does, call an editor on it, and update from the result as mailbox_in does. If you do not specify an editor name as second argument, it will be taken from the $EDITOR variable in your environment. </p>
<p> Normally this command ignores blobs because <code>mailbox_out</code> does. However, if you specify a selection set consisting of a single blob, your editor will be called directly on the blob file.</dl>
<p> <code>timeoffset</code> offset [<i>timezone</i>]</p>
<dl>
<dt>
<dd> Apply a time offset to all time/date stamps in the selected set. An offset argument is required; it may be in the form [+-]ss, [+-]mm:ss or [+-]hh:mm:ss. The leading sign is required to distinguish it from a selection expression. </p>
<p> Optionally you may also specify another argument in the form [+-]hhmm, a timezone literal to apply. To apply a timezone without an offset, use an offset literal of +0 or -0.</dl>
<p> <code>unite</code> [&#8211;prune] <i>reponame</i>&#8230;</p>
<dl>
<dt>
<dd> Unite repositories. Name any number of loaded repositories; they will be united into one union repo and removed from the load list. The union repo will be selected. </p>
<p> The root of each repo (other than the oldest repo) will be grafted as a child to the last commit in the dump with a preceding commit date. This will produce a union repository with one branch for each part. Running last to first, duplicate tag and branch names will be disambiguated using the source repository name (thus, recent duplicates will get priority over older ones). After all grafts, marks will be renumbered. </p>
<p> The name of the new repo will be the names of all parts concatenated, separated by &#8216;+&#8217;. It will have no source directory or preferred system type. </p>
<p> With the option &#8211;prune, at each join D operations for every ancestral file existing will be prepended to the root commit, then it will be canonicalized using the rules for squashing the effect will be that only files with properly matching M, R, and C operations in the root survive.</dl>
<p> <code>graft</code> [&#8211;prune] <i>reponame</i></p>
<dl>
<dt>
<dd> For when unite doesn&#8217;t give you enough control. This command may have either of two forms, selected by the size of the selection set. The first argument is always required to be the name of a loaded repo. </p>
<p> If the selection set is of size 1, it must identify a single commit in the currently chosen repo; in this case the name repo&#8217;s root will become a child of the specified commit. If the selection set is empty, the named repo must contain one or more callouts matching a commits in the currently chosen repo. </p>
<p> Labels and branches in the named repo are prefixed with its name; then it is grafted to the selected one. Any other callouts in the named repo are also resolved in the context of the currently chosen one. Finally, the named repo is removed from the load list. </p>
<p> With the option &#8211;prune, prepend a deleteall operation into the root of the grafted repository.</dl>
<p> <code>path</code> [<i>source</i>] <code>rename</code> [<code>&#8211;force</code>] [<i>target</i>]</p>
<dl>
<dt>
<dd> Rename a path in every fileop of every selected commit. The default selection set is all commits. The first argument is interpreted as a Python regular expression to match against paths; the second may contain back-reference syntax. </p>
<p> Ordinarily, if the target path already exists in the fileops, or is visible in the ancestry of the commit, this command throws an error. With the <code>&#8211;force</code> option, these checks are skipped.</dl>
<p> <code>paths</code> [<code>{sub|sup}</code>] [<code>dirname</code>] [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Takes a selection set. Without a modifier, list all paths touched by fileops in the selection set (which defaults to the entire repo). This reporting variant does &gt;-redirection. </p>
<p> With the &#8216;sub&#8217; modifier, take a second argument that is a directory name and prepend it to every path. With the &#8216;sup&#8217; modifier, strip any directory argument from the start of the path if it appears there; with no argument, strip the first directory component from every path.</dl>
<p> <code>merge</code></p>
<dl>
<dt>
<dd> Create a merge link. Takes a selection set argument, ignoring all but the lowest (source) and highest (target) members. Creates a merge link from the highest member (child) to the lowest (parent).</dl>
<p> <code>unmerge</code></p>
<dl>
<dt>
<dd> Linearize a commit. Takes a selection set argument, which must resolve to a single commit, and removes all its parents except for the first. </p>
<p> It is equivalent to <code>reparent</code><i>first_parent</i>,<i>commit</i><code>rebase</code>, where <i>commit</i> is the same selection set as used with unmerge and <i>first_parent</i> is a set resolving <i>commit</i>&#8216;s first parent (see the <code>reparent</code> command below </p>
<p> The main interest of the <code>unmerge</code> is that you don&#8217;t have to find and specify the first parent yourself, saving time and avoiding errors when nearby surgery would make a manual first parent argument stale.</dl>
<p> <code>reparent</code> [<i>options</i>&#8230;] [<i>policy</i>]</p>
<dl>
<dt>
<dd> Changes the parent list of a commit. Takes a selection set, zero or more option arguments, and an optional policy argument. </p>
<p> Selection set:</p>
<dl>
<dt>
<dd> The selection set must resolve to one or more commits. The selected commit with the highest event number (not necessarily the last one selected) is the commit to modify. The remainder of the selected commits, if any, become its parents: the selected commit with the lowest event number (which is not necessarily the first one selected) becomes the first parent, the selected commit with second lowest event number becomes the second parent, and so on. All original parent links are removed. Examples: </p>
<dl>
<dt>
<dd>
<pre>
# this makes 17 the parent of 33
17,33 reparent
# this also makes 17 the parent of 33
33,17 reparent
# this makes 33 a root (parentless) commit
33 reparent
# this makes 33 an octopus merge commit.  its first parent
# is commit 15, second parent is 17, and third parent is 22
22,33,15,17 reparent
</pre>
</dl>
</dl>
<p> Options:</p>
<dl>
<dt>
<dd>
<p> <code>&#8211;use-order</code></p>
<dl>
<dt>
<dd> Use the selection order to determine which selected commit is the commit to modify and which are the parents (and if there are multiple parents, their order). The last selected commit (not necessarily the one with the highest event number) is the commit to modify, the first selected commit (not necessarily the one with the lowest event number) becomes the first parent, the second selected commit becomes the second parent, and so on. Examples: </p>
<dl>
<dt>
<dd>
<pre>
# this makes 33 the parent of 17
33|17 reparent --use-order
# this makes 17 an octopus merge commit.  its first parent
# is commit 22, second parent is 33, and third parent is 15
22,33,15|17 reparent --use-order
</pre>
</dl>
<p> Because ancestor commit events must appear before their descendants, giving a commit with a low event number a parent with a high event number triggers a re-sort of the events. A re-sort assigns different event numbers to some or all of the events. Re-sorting only works if the reparenting does not introduce any cycles. To swap the order of two commits that have an ancestor-descendant relationship without introducing a cycle during the process, you must reparent the descendant commit first.</dl>
</dl>
<p> Policy:</p>
<dl>
<dt>
<dd> By default, the manifest of the reparented commit is computed before modifying it; a deleteall and some fileops are prepended so that the manifest stays unchanged even when the first parent has been changed. This behavior can be changed by specifying a policy: </p>
<p> <code>rebase</code></p>
<dl>
<dt>
<dd> Inhibits the default behavior&#8212;no deleteall is issued and the tree contents of all descendents can be modified as a result.</dl>
</dl>
</dl>
<p> <code>branch</code> <i>branchname</i>&#8230; {<code>rename</code>|<code>delete</code>} [<i>arg</i>]</p>
<dl>
<dt>
<dd> Rename or delete a branch (and any associated resets). First argument must be an existing branch name; second argument must one of the verbs &#8216;rename&#8217; or &#8216;delete&#8217;. </p>
<p> For a &#8216;rename&#8217;, the third argument may be any token that is a syntactically valid branch name (but not the name of an existing branch). For a &#8216;delete&#8217;, no third argument is required. </p>
<p> For either name, if it does not contain a &#8216;/&#8217; the prefix &#8216;refs/heads&#8217; is prepended.</dl>
<p> <code>tag</code> <i>tagname</i>&#8230; <code>{move|rename|delete}</code> <code>[arg]</code>.</p>
<dl>
<dt>
<dd> Create, move, rename, or delete a tag. </p>
<p> Creation is a special case. First argument is a nane, which must not be an existing tag. Takes a singleton event second argument which must point to a commit. A tag object pointing to the commit is created and inserted just after the last tag in the repo (or just after the last commit if there are no tags). The tagger, committish, and comment fields are copied from the commit&#8217;s committer, mark, and comment fields. </p>
<p> Otherwise, first argument must be an existing tag name; second argument must be one of the verbs &#8220;move&#8221;, &#8220;rename&#8221;, or &#8220;delete&#8221;. </p>
<p> For a &#8220;move&#8221;, a third argument must be a singleton selection set. For a &#8220;rename&#8221;, the third argument may be any token that is a syntactically valid tag name (but not the name of an existing tag). For a &#8220;delete&#8221;, no third argument is required. </p>
<p> The behavior of this command is complex because features which present as tags may be any of three things: (1) True tag objects, (2) lightweight tags, actually sequences of commits with a common branchname beginning with &#8220;refs/tags&#8221; &#8211; in this case the tag is considered to point to the last commit in the sequence, (3) Reset objects. These may occur in combination; in fact, stream exporters from systems with annotation tags commonly express each of these as a true tag object (1) pointing at the tip commit of a sequence (2) in which the basename of the common branch field is identical to the tag name. An exporter that generates lightweight-tagged commit sequences (2) may or may not generate resets pointing at their tip commits. </p>
<p> This command tries to handle all combinations in a natural way by doing up to three operations on any true tag, commit sequence, and reset matching the source name. In a rename, all are renamed together. In a delete, any matching tag or reset is deleted; then matching branch fields are changed to match the branch of the unique descendent of the tagged commit, if there is one. When a tag is moved, no branch fields are changed and a warning is issued. </p>
<p> Attempts to delete a lightweight tag may fail with the message &#8220;couldn&#8217;t determine a unique successor&#8221;. When this happens, the tag is on a commit with multiple children that have different branch labels. There is a hole in the specification of git fast-import streams that leaves it uncertain how branch labels can be safely reassigned in this case; rather than do something risky, <code>reposurgeon</code> throws a recoverable error.</dl>
<p> <code>reset</code> <i>resetname</i>&#8230; <code>{move|rename|delete}</code> <code>[arg]</code>.</p>
<dl>
<dt>
<dd> Move, rename, or delete a reset. First argument must match an existing reset name; second argument must be one of the verbs &#8220;move&#8221;, &#8220;rename&#8221;, or &#8220;delete&#8221;. </p>
<p> For a &#8220;move&#8221;, a third argument must be a singleton selection set. For a &#8220;rename&#8221;, the third argument may be any token token that matches a syntactically valid reset name (but not the name of an existing reset). For a &#8220;delete&#8221;, no third argument is required. </p>
<p> For either name, if it does not contain a &#8220;/&#8221; the prefix &#8220;heads/&#8221; is prepended. If it does not begin with &#8220;refs/&#8221;, &#8220;refs/&#8221; is prepended. </p>
<p> An argument matches a reset&#8217;s name if it is either the entire reference (refs/heads/FOO or refs/tags/FOO for some some value of FOO) or the basename (e.g. FOO), or a suffix of the form heads/FOO or tags/FOO. An unqualified basename is assumed to refer to a head. </p>
<p> When a reset is renamed, commit branch fields matching the tag are renamed with it to match. When a reset is deleted, matching branch fields are changed to match the branch of the unique descendent of the tip commit of the associated branch, if there is one. When a reset is moved, no branch fields are changed.</dl>
<p> <code>debranch</code> <i>source-branch</i>&#8230; <code>[target-branch]</code>.</p>
<dl>
<dt>
<dd> Takes one or two arguments which must be the names of source and target branches; if the second (target) argument is omitted it defaults to refs/heads/master. Any trailing segment of a branch name is accepted as a synonym for it; thus master is the same as refs/heads/master. Does not take a selection set. </p>
<p> The history of the source branch is merged into the history of the target branch, becoming the history of a subdirectory with the name of the source branch. Any resets of the source branch are removed.</dl>
<p> <code>strip</code> <code>[blobs|reduce]</code>.</p>
<dl>
<dt>
<dd> Reduce the selected repository to make it a more tractable test case. Use this when reporting bugs. </p>
<p> With the modifier &#8216;blobs&#8217;, replace each blob in the repository with a small, self-identifying stub, leaving all metadata and DAG topology intact. This is useful when you are reporting a bug, for reducing large repositories to test cases of manageable size. </p>
<p> A selection set is effective only with the &#8216;blobs&#8217; option, defaulting to all blobs. The &#8216;reduce&#8217; mode always acts on the entire repository. </p>
<p> With the modifier &#8216;reduce&#8217;, perform a topological reduction that throws out uninteresting commits. If a commit has all file modifications (no deletions or copies or renames) and has exactly one ancestor and one descendant, then it may be boring. To be fully boring, it must also not be referred to by any tag or reset. Interesting commits are not boring, or have a non-boring parent or non-boring child. </p>
<p> With no modifiers, this command strips blobs.</dl>
<p> <code>ignores</code> <code>[rename]</code>. <code>[translate]</code>. <code>[defaults]</code>.</p>
<dl>
<dt>
<dd> Intelligent handling of ignore-pattern files. This command fails if no repository has been selected or no preferred write type has been set for the repository. It does not take a selection set. </p>
<p> If the rename modifier is present, this command attempts to rename all ignore-pattern files to whatever is appropriate for the preferred type &#8211; e.g. .gitignore for git, .hgignore for hg, etc. This option does not cause any translation of the ignore files it renames. </p>
<p> If the translate modifier is present, syntax translation of each ignore file is attempted. At present, the only transformation the code knows is to prepend a &#8216;syntax: glob&#8217; header if the preferred type is hg. </p>
<p> If the defaults modifier is present, the command attempts to prepend these default patterns to all ignore files. If no ignore file is created by the first commit, it will be modified to create one containing the defaults. This command will error out on prefer types that have no default ignore patterns (git and hg, in particular). It will also error out when it knows the import tool has already set default patterns.</dl>
<h3>REFERENCE LIFTING</h3>
<p> This group of commands is meant for fixing up references in commits that are in the format of older version control systems. The general workflow is this: first, go over the comment history and change all old-fashioned commit references into machine-parseable cookies. Then, automatically turn the machine-parseable cookie into action stamps. The point of dividing the process this way is that the first part is hard for a machine to get right, while the second part is prone to errors when a human does it. </p>
<p> A Subversion cookie is a comment substring of the form [[SVN:ddddd]] (example: [[SVN:2355]] with the revision read directly via the Subversion exporter, deduced from git-svn metadata, or matching a $Revision$ header embedded in blob data for the filename. </p>
<p> A CVS cookie is a comment substring of the form [[CVS:filename:revision]] (example: [[CVS:src/README:1.23]] with the revision matching a CVS $Id$ or $Revision$ header embedded in blob data for the filename. </p>
<p> A mark cookie is of the form [[:dddd]] and is simply a reference to the specified mark. You may want to hand-patch this in when one of previous forms is inconvenient. </p>
<p> An action stamp is an RFC3339 timestamp, followed by a &#8216;!&#8217;, followed by an author email address (author rather than committer because that timestamp is not changed when a patch is replayed on to a branch). It attempts to refer to a commit without being VCS-specific. Thus, instead of &quot;commit 304a53c2&quot; or &quot;r2355&quot;, &quot;2011-10-25T15:11:09Z!fred [at] foonly.com&quot;. </p>
<p> The following git aliases allow git to work directly with action stamps. Append it to your ~/.gitconfig; if you already have an [alias] section, leave off the first line. </p>
<dl>
<dt>
<dd>
[alias]<br />
#git stamp &lt; commit &#8211; ish&gt; &#8211; print a reposurgeon &#8211; style action stamp<br />
    stamp = show &#8211; s&#8211; format = &#8216;%cI!%ce&#8217;<br />
#git scommit &lt; stamp&gt; &lt; rev &#8211; list &#8211; args&gt; &#8211; list most recent commit that matches &lt; stamp&gt;.<br />
#Must also specify a branch to search or &#8211;all, after these arguments.<br />
    scommit = &#8220;!f(){ d=${1%%!*}; a=${1##*!}; arg=\&#8221;&#8211;until=$d -1\&#8221;; if [ $a != $1 ]; then arg=\&#8221;$arg &#8211;committer=$a\&#8221;; fi; shift; git rev-list $arg ${1:+\&#8221;$@\&#8221;}; }; f&#8221;<br />
#git scommits &lt; stamp&gt; &lt; rev &#8211; list &#8211; args&gt; &#8211; as above, but list all matching commits.<br />
    scommits = &#8220;!f(){ d=${1%%!*}; a=${1##*!}; arg=\&#8221;&#8211;until=$d &#8211;after $d\&#8221;; if [ $a != $1 ]; then arg=\&#8221;$arg &#8211;committer=$a\&#8221;; fi; shift; git rev-list $arg ${1:+\&#8221;$@\&#8221;}; }; f&#8221;<br />
#git smaster &lt; stamp&gt; &#8211; list most recent commit on master that matches &lt; stamp&gt;.<br />
    smaster = &#8220;!f(){ git scommit \&#8221;$1\&#8221; master &#8211;first-parent; }; f&#8221; smasters = &#8220;!f(){ git scommits \&#8221;$1\&#8221; master &#8211;first-parent; }; f&#8221;<br />
#git shs &lt; stamp&gt; &#8211; show the commits on master that match &lt; stamp&gt;.<br />
    shs = &#8220;!f(){ stamp=$(git smasters $1); shift; git show ${stamp:?not found} $*; }; f&#8221;<br />
#git slog &lt; stamp&gt; &lt; log &#8211; args&gt; &#8211; start git log at &lt; stamp&gt; on master<br />
    slog = &#8220;!f(){ stamp=$(git smaster $1); shift; git log ${stamp:?not found} $*; }; f&#8221;<br />
#git sco &lt; stamp&gt; &#8211; check out most recent commit on master that matches &lt; stamp&gt;.<br />
    sco = &#8220;!f(){ stamp=$(git smaster $1); shift; git checkout ${stamp:?not found} $*; }; f&#8221;
</dl>
<p> There is a rare case in which an action stamp will not refer uniquely to one commit. It is theoretically possible that the same author might check in revisions on different branches within the one-second resolution of the timestamps in a fast-import stream. There is nothing to be done about this; tools using action stamps need to be aware of the possibility and throw a warning when it occurs. </p>
<p> In order to support reference lifting, <code>reposurgeon</code> internally builds a legacy-reference map that associates revision identifiers in older version-control systems with commits. The contents of this map comes from three places: (1) cvs2svn:rev properties if the repository was read from a Subversion dump stream, (2) $Id$ and $Revision$ headers in repository files, and (3) the .git/cvs-revisions created by <code>git cvsimport</code>. </p>
<p> The detailed sequence for lifting possible references is this: first, find possible CVS and Subversion references with the <code>references</code> or =N visibility set; then replace them with equivalent cookies; then run <code>references lift</code> to turn the cookies into action stamps (using the information in the legacy-reference map) without having to do the lookup by hand. </p>
<p> <code>references</code> [<code>list</code>|<code>edit</code>|<code>lift</code>] [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> With the modifier &#8216;list&#8217;, list commit and tag comments for strings that might be CVS- or Subversion-style revision identifiers. This will be useful when you want to replace them with equivalent cookies that can automatically be translated into VCS-independent action stamps. This reporting command supports &gt;-redirection. It is equivalent to &#8216;=N list&#8217;. </p>
<p> With the modifier &#8216;edit&#8217;, edit the set where revision IDs are found. This is equivalent to &#8216;=N edit&#8217;. </p>
<p> With the modifier &quot;lift&quot;, attempt to resolve Subversion and CVS cookies in comments into action stamps using the legacy map. An action stamp is a timestamp/email/sequence-number combination uniquely identifying the commit associated with that blob, as described in the section called &#8220;TRANSLATION STYLE&#8221;. </p>
<p> It is not guaranteed that every such reference will be resolved, or even that any at all will be. Normally all references in history from a Subversion repository will resolve, but CVS references are less likely to be resolvable.</dl>
<h3>VARIABLES, MACROS AND EXTENSIONS</h3>
<p> Occasionally you will need to issue a large number of complex surgical commands of very similar form, and it&#8217;s convenient to be able to package that form so you don&#8217;t need to do a lot of error-prone typing. For those occasions, <code>reposurgeon</code> supports simple forms of named variables and macro expansion. </p>
<p> <code>assign</code> [<i>name</i>]</p>
<dl>
<dt>
<dd> Compute a leading selection set and assign it to a symbolic name. It is an error to assign to a name that is already assigned, or to any existing branch name. Assignments may be cleared by sequence mutations (though not ordinary deletions); you will see a warning when this occurs. </p>
<p> With no selection set and no name, list all assignments.&gt; </p>
<p> Use this to optimize out location and selection computations that would otherwise be performed repeatedly, e.g. in macro calls.</dl>
<p> <code>unassign</code> [<i>name</i>]</p>
<dl>
<dt>
<dd> Unassign a symbolic name. Throws an error if the name is not assigned.</dl>
<p> <code>names</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> List the names of all known branches and tags. Tells you what things are legal within angle brackets and parentheses.</dl>
<p> <code>define</code> <i>name</i> <i>body</i></p>
<dl>
<dt>
<dd> Define a macro. The first whitespace-separated token is the name; the remainder of the line is the body, unless it is &#8220;{&#8220;, which begins a multi-line macro terminated by a line beginning with &#8220;}&#8221;. </p>
<p> A later &#8220;do&#8221; call can invoke this macro. </p>
<p> The command &#8220;define&#8221; by itself without a name or body produces a macro list.</dl>
<p> <code>do</code> <i>name</i> <i>arguments</i>&#8230;</p>
<dl>
<dt>
<dd> Expand and perform a macro. The first whitespace-separated token is the name of the macro to be called; remaining tokens replace {0}, {1}&#8230; in the macro definition (the conventions used are those of the Python format method). Tokens may contain whitespace if they are string-quoted; string quotes are stripped. Macros can call macros. </p>
<p> If the macro expansion does not itself begin with a selection set, whatever set was specified before the &quot;do&quot; keyword is available to the command generated by the expansion.</dl>
<p> <code>undefine</code> <i>name</i>]</p>
<dl>
<dt>
<dd> Undefine the named macro.</dl>
<p> Here&#8217;s an example to illustrate how you might use this. In CVS repositories of projects that use the GNU ChangeLog convention, a very common pre-conversion artifact is a commit with the comment &quot;***empty log message***&quot; that modifies only a ChangeLog entry explaining the commit immediately previous to it. The following </p>
<dl>
<dt>
<dd>
define changelog&lt;{0}&gt; &amp; / empty log message / squash&#8211; pushback do changelog 2012 &#8211; 08 &#8211; 14T21 : 51 : 35Z do changelog 2012 &#8211; 08 &#8211; 08T22 : 52 : 14Z do changelog 2012 &#8211; 08 &#8211; 07T04 : 48 : 26Z do changelog 2012 &#8211; 08 &#8211; 08T07 : 19 : 09Z do changelog 2012 &#8211; 07 &#8211; 28T18 : 40 : 10Z
</dl>
<p> is equivalent to the more verbose </p>
<dl>
<dt>
<dd>
&lt;2012-08-14T21:51:35Z&gt; &amp; /empty log message/ squash &#8211;pushback<br />
&lt;2012-08-08T22:52:14Z&gt; &amp; /empty log message/ squash &#8211;pushback<br />
&lt;2012-08-07T04:48:26Z&gt; &amp; /empty log message/ squash &#8211;pushback<br />
&lt;2012-08-08T07:19:09Z&gt; &amp; /empty log message/ squash &#8211;pushback<br />
&lt;2012-07-28T18:40:10Z&gt; &amp; /empty log message/ squash &#8211;pushback
</dl>
<p> but you are less likely to make difficult-to-notice errors typing the first version. </p>
<p> (Also note how the text regexp acts as a failsafe against the possibility of typing a wrong date that doesn&#8217;t refer to a commit with an empty comment. This was a real-world example from the CVS-to-git conversion of groff.) </p>
<p> When even a macro is not enough, you can write and call custom Python extensions. </p>
<p> <code>exec</code> <i>name</i></p>
<dl>
<dt>
<dd> Execute custom code from standard input (normally a file via &lt; redirection). Use this to set up custom extension functions for later eval calls. The code has full access to all internal data structures. Functions defined are accessible to later <code>eval</code> calls. </p>
<p> This can be called in a script with the extension code in a here-doc.</dl>
<p> <code>eval</code> <i>function-name</i></p>
<dl>
<dt>
<dd> Evaluate a line of code in the current interpreter context. Typically this will be a call to a function defined by a previous exec. The variables <i>_repository</i> and <i>_selection</i> will have the obvious values. Note that <i>_selection</i> will be a list of integers, not objects.</dl>
<p> <code>script</code> <i>filename</i> [<i>arg</i>&#8230;]</p>
<dl>
<dt>
<dd> Takes a filename and optional following arguments. Reads each line from the file and executes it as a command. </p>
<p> During execution of the script, the script name replaces the string $0 and the optional following arguments (if any) replace the strings $1, $2 &#8230; $n in the script text. This is done before tokenization, so the $1 in a string like &#8220;foo$1bar&#8221; will be expanded. Additionally, $$ is expanded to the current process ID (which may be useful for scripts that use tempfiles). </p>
<p> Within scripts (and only within scripts) <code>reposurgeon</code> accepts a slightly extended syntax: First, a backslash ending a line signals that the command continues on the next line. Any number of consecutive lines thus escaped are concatenated, without the ending backslashes, prior to evaluation. Second, a command that takes an input filename argument can instead take literal following data in the syntax of a shell here-document. That is: if the filename is replaced by &quot;&lt;&lt;EOF&quot;, all following lines in the script up to a terminating line consisting only of &quot;EOF&quot; will be read, placed in a temporary file, and that file fed to the command and afterwards deleted. EOF may be replaced by any string. Backslashes have no special meaning while reading a here-document. </p>
<p> Scripts may have comments. Any line beginning with a &#8216;#&#8217; is ignored. If a line has a trailing position that begins with one or more whitespace characters followed by &#8216;#&#8217;, that trailing portion is ignored.</dl>
<h3>ARTIFACT REMOVAL</h3>
<p> Some commands automate fixing various kinds of artifacts associated with repository conversions from older systems. </p>
<p> <code>authors</code> [<code>read</code>|<code>write</code>] [&lt;<code>filename</code>] [&gt;<code>filename</code>]</p>
<dl>
<dt>
<dd> Apply or dump author-map information for the specified selection set, defaulting to all events. </p>
<p> Lifts from CVS and Subversion may have only usernames local to the repository host in committer and author IDs. DVCSes want email addresses (net-wide identifiers) and complete names. To supply the map from one to the other, an authors file is expected to consist of lines each beginning with a local user ID, followed by a &#8216;=&#8217; (possibly surrounded by whitespace) followed by a full name and email address, optionally followed by a timezone offset field. Thus: </p>
<dl>
<dt>
<dd>
<pre>
ferd = Ferd J. Foonly &lt;foonly [at] foo.com&gt; -0500
</pre>
</dl>
<p> An authors file may have comment lines beginning with &#8216;#&#8217;; these are ignored. </p>
<p> When an authors file is applied, email addresses in committer and author metadata for which the local ID matches between &lt; and @ are replaced according to the mapping (this handles git-svn lifts). Alternatively, if the local ID is the entire address, this is also considered a match (this handles what git-cvsimport and cvs2git do) </p>
<p> With the &#8216;read&#8217; modifier, or no modifier, apply author mapping data (from standard input or a &lt;-redirected file). May be useful if you are editing a repo or dump created by <code>cvs2git</code> or by <code>git-svn</code> invoked without -A. </p>
<p> With the &#8216;write&#8217; modifier, write a mapping file that could be interpreted by <code>authors read</code>, with entries for each unique committer, author, and tagger (to standard output or a &lt;-redirected mapping file). This may be helpful as a start on building an authors file, though each part to the right of an equals sign will need editing.</dl>
<p> <code>branchify</code> [<i>path-set</i>]</p>
<dl>
<dt>
<dd> Specify the list of directories to be treated as potential branches (to become tags if there are no modifications after the creation copies) when analyzing a Subversion repo. This list is ignored when the <code>&#8211;nobranch</code> read option is used. It defaults to the &#8216;standard layout&#8217; set of directories, plus any unrecognized directories in the repository root. </p>
<p> With no arguments, displays the current branchification set. </p>
<p> An asterisk at the end of a path in the set means &#8216;all immediate subdirectories of this path, unless they are part of another (longer) path in the branchify set&#8217;. </p>
<p> Note that the branchify set is a property of the reposurgeon interpreter, not of any individual repository, and will persist across Subversion dumpfile reads. This may lead to unexpected results if you forget to re-set it.</dl>
<p> <code>branchify_map</code> [<i>/regex/branch/</i>&#8230;]</p>
<dl>
<dt>
<dd> Specify the list of regular expressions used for mapping the svn branches that are detected by branchify. If none of the expressions match the default behaviour applies. This maps a branch to the name of the last directory, except for trunk and &#8220;*&#8221; which are mapped to master and root. </p>
<p> With no arguments the current regex replacement pairs are shown. Passing &#8216;reset&#8217; will clear the mapping. </p>
<p> The branchify command will match each branch name against regex1 and if it matches rewrite its branch name to branch1. If not it will try regex2 and so forth until it either found a matching regex or there are no regexs left. The regular expressions should be in m[blue]<code>Python&#8217;s</code>m[]<font SIZE="-2">[2]</font>. format. The branch name can use backreferences (see the re.sub function in the Python documentation). </p>
<p> Note that the regular expressions are appended to &#8216;refs/&#8217; without either the needed &#8216;heads/&#8217; or &#8216;tags/&#8217;. This allows for choosing the right kind of branch type. </p>
<p> While the syntax template above uses slashes, any first character will be used as a delimeter (and you will need to use a different one in the common case that the paths contain slashes). </p>
<p> Note that the branchify_map set is a property of the reposurgeon interpreter, not of any individual repository, and will persist across Subversion dumpfile reads. This may lead to unexpected results if you forget to re-set it.</dl>
<h3>EXAMINING TREE STATES</h3>
<p> <code>manifest</code> [<i>regular expression</i>] [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Takes an optional selection set argument defaulting to all commits, and an optional Python regular expression. For each commit in the selection set, print the mapping of all paths in that commit tree to the corresponding blob marks, mirroring what files would be created in a checkout of the commit. If a regular expression is given, only print &quot;path -&gt; mark&quot; lines for paths matching it. This command supports &gt; redirection.</dl>
<p> <code>checkout</code> <i>directory</i></p>
<dl>
<dt>
<dd> Takes a selection set which must resolve to a single commit, and a second argument. The second argument is interpreted as a directory name. The state of the code tree at that commit is materialized beneath the directory.</dl>
<p> <code>diff</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Display the difference between commits. Takes a selection-set argument which must resolve to exactly two commits. Supports output redirection.</dl>
<h3>HOUSEKEEPING</h3>
<p> These are backed up by the following housekeeping commands, none of which take a selection set: </p>
<p> <code>help</code></p>
<dl>
<dt>
<dd> Get help on the interpreter commands. Optionally follow with whitespace and a command name; with no argument, lists all commands. &#8216;?&#8217; also invokes this.</dl>
<p> <code>shell</code></p>
<dl>
<dt>
<dd> Execute the shell command given in the remainder of the line. &#8216;!&#8217; also invokes this.</dl>
<p> <code>prefer</code> [<i>repotype</i>]</p>
<dl>
<dt>
<dd> With no arguments, describe capabilities of all supported systems. With an argument (which must be the name of a supported system) this has two effects: </p>
<p> First, if there are multiple repositories in a directory you do a read on, reposurgeon will read the preferred one (otherwise it will complain that it can&#8217;t choose among them). </p>
<p> Secondly, this will change reposurgeon&#8217;s preferred type for output. This means that you do a write to a directory, it will build a repo of the preferred type rather than its original type (if it had one). </p>
<p> If no preferred type has been explicitly selected, reading in a repository (but not a fast-import stream) will implicitly set the preferred type to the type of that repository. </p>
<p> In older versions of reposurgeon this command changed the type of the selected repository, if there is one. That behavior interacted badly with attempts to interpret legacy IDs and has been removed.</dl>
<p> <code>sourcetype</code> [<i>repotype</i>]</p>
<dl>
<dt>
<dd> Report (with no arguments) or select (with one argument) the current repository&#8217;s source type. This type is normally set at repository-read time, but may remain unset if the source was a stream file. </p>
<p> The source type affects the interpretation of legacy IDs (for purposes of the =N visibility set and the &#8216;references&#8217; command) by controlling the regular expressions used to recognize them. If no preferred output type has been set, it may also change the output format of stream files made from the repository. </p>
<p> The source type is reliably set whenever a live repository is read, or when a Subversion stream or Fossil dump is interpreted but not necessarily by other stream files. Streams generated by <code><a href="/docs/linux/man/1-cvs-fast-export/">cvs-fast-export</a></code>(1) using the <code>&#8211;reposurgeon</code> are detected as CVS. In some other cases, the source system is detected from the presence of magic $-headers in contents blobs.</dl>
<h3>INSTRUMENTATION</h3>
<p> A few commands have been implemented primarily for debugging and regression-testing purposes, but may be useful in unusual circumstances. </p>
<p> The output of most of these commands can individually be redirected to a named output file. Where indicated in the syntax, you can prefix the output filename with &#8220;&gt;&#8221; and give it as a following argument. </p>
<p> <code>index</code> [&gt;<i>outfile</i>]</p>
<dl>
<dt>
<dd> Display four columns of info on objects in the selection set: their number, their type, the associate mark (or &#8216;-&#8216; if no mark) and a summary field varying by type. For a branch or tag it&#8217;s the reference; for a commit it&#8217;s the commit branch; for a blob it&#8217;s the repository path of the file in the blob. </p>
<p> The default selection set for this command is =CTRU, all objects except blobs.</dl>
<p> <code>resolve</code> [<i>label-text&#8230;</i>]</p>
<dl>
<dt>
<dd> Does nothing but resolve a selection-set expression and echo the resulting event-number set to standard output. The remainder of the line after the command is used as a label for the output. </p>
<p> Implemented mainly for regression testing, but may be useful for exploring the selection-set language.</dl>
<p> <code>verbose</code> [<i>n</i>]</p>
<dl>
<dt>
<dd> &#8216;verbose 1&#8217; enables the progress meter and messages, &#8216;verbose 0&#8217; disables them. Higher levels of verbosity are available but intended for developers only.</dl>
<p> <code>quiet</code> [<i>on | off</i>]</p>
<dl>
<dt>
<dd> Without an argument, this command requests a report of the quiet boolean; with the argument &#8216;on&#8217; or &#8216;off&#8217; it is changed. When quiet is on, time-varying report fields which would otherwise cause spurious failures in regression testing are suppressed.</dl>
<p> <code>print</code> <i>output-text&#8230;</i></p>
<dl>
<dt>
<dd> Does nothing but ship its argument line to standard output. Useful in regression tests.</dl>
<p> <code>echo</code> [<i>number</i>]</p>
<dl>
<dt>
<dd> &#8216;echo 1&#8217; causes each <code>reposurgeon</code> command to be echoed to standard output just before its output. This can be useful in constructing regression tests that are easily checked by eyeball.</dl>
<p> <code>version</code> [<i>version</i>&#8230;]</p>
<dl>
<dt>
<dd> With no argument, display the program version and the list of VCSes directly supported. With argument, declare the major version (single digit) or full version (major.minor) under which the enclosing script was developed. The program will error out if the major version has changed (which means the surgical language is not backwards compatible). </p>
<p> It is good practice to start your lift script with a version requirement, especially if you are going to archive it for later reference.</dl>
<p> <code>prompt</code> [<i>format</i>&#8230;]</p>
<dl>
<dt>
<dd> Set the command prompt format to the value of the command line; with an empty command line, display it. The prompt format is evaluated in Python after each command with the following dictionary substitutions: </p>
<p> chosen</p>
<dl>
<dt>
<dd> The name of the selected repository, or None if none is currently selected.</dl>
<p> Thus, one useful format might be &#8216;rs[%(chosen)s]%% &#8216;. </p>
<p> More format items may be added in the future. The default prompt corresponds to the format &#8216;reposurgeon%% &#8216;. The format line is evaluated with shell quotng of tokens, so that spaces can be included.</dl>
<p> <code>history</code></p>
<dl>
<dt>
<dd> List the commands you have entered this session.</dl>
<p> <code>legacy</code> [<code>read</code>|<code>write</code>] [<code>&lt;filename</code>] [<code>&gt;filename</code>]</p>
<dl>
<dt>
<dd> Apply or list legacy-reference information. Does not take a selection set. The &#8216;read&#8217; variant reads from standard input or a &lt;-redirected filename; the &#8216;write&#8217; variant writes to standard output or a &gt;-redirected filename. </p>
<p> A legacy-reference file maps reference cookies to (committer, commit-date, sequence-number) pairs; these in turn (should) uniquely identify a commit. The format is two whitespace-separated fields: the cookie followed by an action stamp identifying the commit. </p>
<p> It should not normally be necessary to use this command. The legacy map is automatically preserved through repository reads and rebuilds, being stored in the file legacy-map under the repository subdirectory..</dl>
<p> <code>set</code> [<code>option</code>]</p>
<dl>
<dt>
<dd> Turn on an option flag. With no arguments, list all options </p>
<p> Most options are described in conjunction with the specific operations that the modify. One of general interest is &#8220;compressblobs&#8221;; this enables compression on the blob files in the internal representation reposurgeon uses for editing repositories. With this option, reading and writing of repositories is slower, but editing a repository requires less (sometimes much less) disk space.</dl>
<p> <code>clear</code> [<code>option</code>]</p>
<dl>
<dt>
<dd> Turn off an option flag. With no arguments, list all options</dl>
<p> <code>profile</code></p>
<dl>
<dt>
<dd> Enable profiling. Profile statistics are dumped to the path given as argument. Must be one of the initial command-line arguments, and gathers statistics only on code executed via &#8216;-&#8216;.</dl>
<p> <code>timing</code></p>
<dl>
<dt>
<dd> Display statistics on phase timing in repository analysis. Mainly of interest to developers trying to speed up the program.</dl>
<p> <code>exit</code></p>
<dl>
<dt>
<dd> Exit, reporting the time. Included here because, while EOT will also cleanly exit the interpreter, this command reports elapsed time since start.</dl>
<h2>WORKING WITH MERCURIAL</h2>
<p> reposurgeon uses a built-in extractor class to perform extractions from Mercurial repositories. </p>
<p> Mercurial branches are exported as branches in the exported repository and tags are exported as tags. By default, bookmarks are ignored. You can specify explicit handling for bookmarks by setting <i>reposurgeon.bookmarks</i> in your .hg/hgrc. Set the value to the prefix that reposurgeon should use for bookmarks. </p>
<p> For example, if your bookmarks represent branches, put this at the bottom of your .hg/hgrc: </p>
<dl>
<dt>
<dd>
<pre>
[reposurgeon]
bookmarks=heads/
</pre>
</dl>
<p> If you do that, it&#8217;s your responsibility to ensure that branch names do not conflict with bookmark names. You can add a prefix like bookmarks=heads/feature- to disambiguate as necessary.</p>
<h2>WORKING WITH SUBVERSION</h2>
<p> reposurgeon can read Subversion dumpfiles or edit a Subversion repository (and you must point it at a repository, not a checkout directory). The reposurgeon distribution includes a script named &#8220;repotool&#8221; that you can use to make and then incrementally update a local mirror of a remote repository for editing or conversion purposes.</p>
<h3>READING SUBVERSION REPOSITORIES</h3>
<p> Certain optional modifiers on the read command change its behavior when reading Subversion repositories: </p>
<p> &#8211;nobranch</p>
<dl>
<dt>
<dd> Suppress branch analysis.</dl>
<p> &#8211;ignore-properties</p>
<dl>
<dt>
<dd> Suppress read-time warnings about discarded property settings.</dl>
<p> &#8211;user-ignores</p>
<dl>
<dt>
<dd> Don&#8217;t generate .gitignore files from svn:ignore properties. Instead, just pass through .gitignore files found in the history.</dl>
<p> &#8211;use-uuid</p>
<dl>
<dt>
<dd> If the &#8211;use-uuid read option is set, the repository&#8217;s UUID will be used as the hostname when faking up email addresses, a la git-svn. Otherwise, addresses will be generated the way git cvs-import does it, simply ciopying the username into the address field.</dl>
<p> These modifiers can go anywhere in any order on the read command line after the read verb. They must be whitespace-separated. </p>
<p> Here are the rules used for mapping subdirectories in a Subversion repository to branches: </p>
<dl>
<dt>
<dd> 1. At any given time there is a set of eligible paths and path wildcards which declare potential branches. See the documentation of the <code>branchify</code> for how to alter this set, which initially consists of {trunk, tags/*, branches/*, and &#8216;*&#8217;}.</dl>
<dl>
<dt>
<dd> 2. A repository is considered &quot;flat&quot; if it has no directory that matches a path or path wildcard in the branchify set. All commits in a flat repository are assigned to branch master, and what would have been branch structure becomes directory structure. In this case, we&#8217;re done; all the other rules apply to non-flat repos. </p>
<p> If you give the option <code>&#8211;nobranch</code> when reading a Subversion repository, branch analysis is skipped and the repository is treated as though flat (left as a linear sequence of commits on refs/heads/master). This may be useful if your repository configuration is highly unusual and you need to do your own branch surgery. Note that this option will disable partitioning of mixed commits.</dl>
<dl>
<dt>
<dd> 3. If &quot;trunk&quot; is eligible, it always becomes the master branch.</dl>
<dl>
<dt>
<dd> 4. If an element of the branchify set ends with *, each immediate subdirectory of it is considered a potential branch. If &#8216;*&#8217; is in the branchify set (which is true by default) all top-level directories other than /trunk, /tags, and /branches are also considered potential branches.</dl>
<dl>
<dt>
<dd> 5. Each potential branch is checked to see if it has commits on it after the initial creation or copy. If there are such commits, it becomes a branch. If not, it becomes a tag in order to preserve the commit metadata. (In all cases, the name of the tag or branch is the basename of the directory.)</dl>
<dl>
<dt>
<dd> 6. Files in the top-level directory are assigned to a synthetic branch named &#8216;root&#8217;.</dl>
<p> Each commit that only creates or deletes directories (in particular, copy commits for tags and branches, and commits that only change properties) will be transformed into a tag named after the branch, containing the date/author/comment metadata from the commit. While this produces a desirable result for tags, non-tag branches (including trunk) will also get root tags this way. This apparent misfeature has been accepted so that reposurgeon will never destroy human-generated metadata that might have value; it is left up to the user to manually remove unwanted tags. </p>
<p> Subversion branch deletions are turned into deletealls, clearing the fileset of the import-stream branch. When a branch finishes with a deleteall at its tip, the deleteall is transformed into a tag. This rule cleans up after aborted branch renames. </p>
<p> Occasionally (and usually by mistake) a branchy Subversion repository will contain revisions that touch multiple branches. These are handled by partitioning them into multiple import-stream commits, one on each affected branch. The Legacy-ID of such a split commit will have a pseudo-decimal part &#8211; for example, if Subversion revision 2317 touches three branches, the three generated commits will have IDs 2317.1, 2317.2, and 2317.3. </p>
<p> The svn:executable and svn:special properties are translated into permission settings in the input stream; svn:executable becomes 100755 and svn:special becomes 120000 (indicating a symlink; the blob contents will be the path to which the symlink should resolve). </p>
<p> Any cvs2svn:rev properties generated by cvs2svn are incorporated into the internal map used for reference-lifting, then discarded. </p>
<p> Normally, per-directory svn:ignore properties become .gitignore files. Actual .gitignore files in a Subversion directory are presumed to have been created by git-svn users separately from native Subversion ignore properties and discarded with a warning. It is up to the user to merge the content of such files into the target repository by hand. But this behavior is inverted by the &#8211;user-ignores option; if that is on, .gitignore files are passed through and Subversion svn:ignore properties are discarded. </p>
<p> (Regardless of the setting of the &#8211;user-ignores option, .cvsignore files found in Subversion repositories always become .gitignores in the translation. The assumption is that these date from before a CVS-to-SVN lift and should be preserved to affect behavior when browsing that section of the repository.) </p>
<p> svn:mergeinfo properties are interpreted. Any svn:mergeinfo property on a revision A with a merge source range ending in revision B produces a merge link such that B becomes a parent of A. </p>
<p> All other Subversion properties are discarded. (This may change in a future release.) The property for which this is most likely to cause semantic problems is svn:eol-style. However, since property-change-only commits get turned into annotated tags, the translated tags will retain information about setting changes. </p>
<p> The sub-second resolution on Subversion commit dates is discarded; Git wants integer timestamps only. </p>
<p> Because fast-import format cannot represent an empty directory, empty directories in Subversion repositories will be lost in translation. </p>
<p> Normally, Subversion local usernames are mapped in the style of git cvs-import; thus user &quot;foo&quot; becomes &quot;foo &lt;foo&gt;&quot;, which is sufficient to pacify git and other systems that require email addresses. With the option &quot;svn_use_uuid&quot;, usernames are mapped in the git-svn style, with the repository&#8217;s UUID used as a fake domain in the email address. Both forms can be remapped to real address using the <code>authors read</code> command. </p>
<p> Reading a Subversion stream enables writing of the legacy map as &#8216;legacy&#8217; passthroughs when the repo is written to a stream file. </p>
<p> <code>reposurgeon</code> tries hard to silently do the right thing, but there are Subversion edge cases in which it emits warnings because a human may need to intervene and perform fixups by hand. Here are the less obvious messages it may emit: </p>
<p> user-generated .gitignore</p>
<dl>
<dt>
<dd> This message means means <code>reposurgeon</code> has found a .gitignore file in the Subversion repository it is analyzing. This probably happened because somebody was using <code>git-svn</code> as a live gateway, and created ignores which may or may not be congruent with those in the generated .gitignore files that the Subversion ignore properties will be translated into. You&#8217;ll need to make a policy decision about which set of ignores to use in the conversion, and possibly set the &#8211;user-ignores option on read to pass through user-created .gitignore files; in that case this warning will not be emitted.</dl>
<p> can&#8217;t connect nonempty branch XXXX to origin</p>
<dl>
<dt>
<dd> This is a serious error. <code>reposurgeon</code> has been unable to find a link from a specified branch to the trunk (master) branch. The commit graph will not be fully connected and will need manual repair.</dl>
<p> permission information may be lost</p>
<dl>
<dt>
<dd> A Subversion node change on a file sets or clears properties, but no ancestor can be found for this file. Executable or symlink position may be set wrongly on later revisions of this file. Subversion user-defined properties may also be scrambled or lost. Usually this error can be ignored.</dl>
<p> properties set</p>
<dl>
<dt>
<dd> <code>reposurgeon</code> has detected a setting of a user-defined property, or the Subversion properties svn:externals. These properties cannot be expressed in an import stream; the user is notified in case this is a showstopper for the conversion or some corrective action is required, but normally this error can be ignored. This warning is suppressed by the &#8211;ignore-properties option.</dl>
<p> branch links detected by file ops only</p>
<dl>
<dt>
<dd> Branch links are normally deduced by examining Subversion directory copy operations. A common user error (making a branch with a non-Subversion directory copy and then doing an svn add on the contends) can defeat this. While <code>reposurgeon</code> should detect and cope with most such copies correctly, you should examine the commit graph to check that the branch is rooted at the correct place.</dl>
<p> could not tagify root commit</p>
<dl>
<dt>
<dd> The earliest commit in your Subversion repository has file operations, rather than being a pure directory creation. This probably means your Subversion dump file is malformed, or you may have attempted to lift from an incremental dump. Proceed with caution.</dl>
<p> deleting parentless tip delete</p>
<dl>
<dt>
<dd> This message may be triggered by a Subversion branch move followed by a re-creation under the source name. Check near the indicated revision to make sure the renamed branch is connected to master.</dl>
<p> mid-branch deleteall</p>
<dl>
<dt>
<dd> A deleteall operation has been found in the middle of a branch history. This usually indicates that a Subversion tag or branch was created by mistake, and someone later tried to undo the error by deleting the tag/branch directory before recreating it with a copy operation. Examine the topology near the deleteall closely, it may need hand-hacking. It is fairly likely that both (a) the <code>reposurgeon</code> translation will be different from what other translators (such as <code>git-svn</code>) produce, and (b) it will not be immediately obvious which is right.</dl>
<p> lookback for XXX failed, not making branch link</p>
<dl>
<dt>
<dd> Branch analysis failed, probably due to a set of file copies that <code>reposurgeon</code> thought it should interpret as a botched branch creation but couldn&#8217;t deduce a history for. This is a warning; check how the directory XXX is converted, it may need post-editing into a branch.</dl>
<h3>WRITING SUBVERSION REPOSITORIES</h3>
<p> reposurgeon has support for writing Subversion repositories. Due to mismatches between the ontology of Subversion and that of git import streams, this support has some significant limitations and bugs. </p>
<p> In summary, Subversion repository histories do not round-trip through reposurgeon editing. File content changes are preserved but some metadata is unavoidably lost. Furthermore, writing out a DVCS history in Subversion also loses significant portions of its metadata. Details follow. </p>
<p> Writing a Subversion repository or dump stream discards author information, the committer&#8217;s name, and the hostname part of the commit address; only the commit timestamp and the local part of the committer&#8217;s email address are preserved, the latter becoming the Subversion author field. However, reading a Subversion repository and writing it out again will preserve the author fields. </p>
<p> Import-stream timestamps have 1-second granularity. The sub-second parts of Subversion commit timestamps will be lost on their way through reposurgeon. </p>
<p> Empty directories aren&#8217;t represented in import streams. Consequently, reading and writing Subversion repositories preserves file content, but not empty directories. It is also not guaranteed that after editing a Subversion repository that the sequence of directory creations and deletions relative to other operations will be identical; the only guarantee is that enclosing directories will be created before any files in them are. </p>
<p> When reading a Subversion repository, reposurgeon discards the special directory-copy nodes associated with branch creations. These can&#8217;t be recreated if and when the repository is written back out to Subversion; rather, each branch copy node from the original translates into a branch creation plus the first set of file modifications on the branch. </p>
<p> When reading a Subversion repository, reposurgeon also automatically breaks apart mixed-branch commits. These are not re-united if the repository is written back out. </p>
<p> When writing to a Subversion repository, all lightweight tags become Subversion tag copies with empty log comments, named for the tag basename. The committer name and timestamp are copied from the commit the tag points to. The distinction between heads and tags is lost. </p>
<p> Because of the preceding two points, it is not guaranteed that even revision numbers will be stable when a Subversion repository is read in and then written out! </p>
<p> Subversion repositories are always written with a standard (trunk/tags/branches) layout. Thus, a repository with a nonstandard shape that has been analyzed by reposurgeon won&#8217;t be written out with the same shape. </p>
<p> When writing a Subversion repository, branch merges are translated into svn:mergeinfo properties in the simplest possible way &#8211; as an svn:mergeinfo property of the translated merge commit listing the merge source revisions. </p>
<p> Subversion has a concept of &quot;flows&quot;; that is, named segments of history corresponding to files or directories that are created when the path is added, cloned when the path is copied, and deleted when the path is deleted. This information is not preserved in import streams or the internal representation that reposurgeon uses. Thus, after editing, the flow boundaries of a Subversion history may be arbitrarily changed.</p>
<h2>IGNORE PATTERNS</h2>
<p> <code>reposurgeon</code> recognizes how supported VCSes represent file ignores (CVS .cvsignore files lurking untranslated in older Subversion repositories, Subversion ignore properties, .gitignore/.hgignore/.bzrignore file in other systems) and moves ignore declarations among these containers on repo input and output. This will be sufficient if the ignore patterns are exact filenames. </p>
<p> Translation may not, however, be perfect when the ignore patterns are Unix glob patterns or regular expressions. This compatibility table describes which patterns will translate; &#8220;plain&#8221; indicates a plain filename with no glob or regexp syntax or negation. </p>
<p> RCS has no ignore files or patterns and is therefore not included in the table. <center></p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center><code> &nbsp;<wbr> </code></td>
<td ALIGN=center><code> from CVS </code></td>
<td ALIGN=center><code> from svn </code></td>
<td ALIGN=center><code> from git </code></td>
<td ALIGN=center><code> from hg </code></td>
<td ALIGN=center><code> from bzr </code></td>
<td ALIGN=center><code> from darcs </code></td>
<td ALIGN=center><code> from SRC </code></td>
<td ALIGN=center><code> from bk </code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> <code>to CVS</code> </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all except !-prefixed but nonempty </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all except RE:- and !-prefixed </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> <code>to svn</code> </td>
<td ALIGN=center> all except !.PP </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all except !-prefixed </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all except RE:- and !-prefixed </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> <code>to git</code> </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all except !-prefixed </td>
<td ALIGN=center>
<p> all except RE:-prefixed </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> <code>to hg</code> </td>
<td ALIGN=center>
<p> all except ! </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all except !-prefixed </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all except RE:- and !-prefixed </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> <code>to bzr</code> </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> <code>to darcs</code> </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
<p> <code>to SRC</code> </td>
<td ALIGN=center>
<p> all except ! </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all except !-prefixed </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all except RE:- and !-prefixed </td>
<td ALIGN=center>
<p> plain </td>
<td ALIGN=center>
<p> all </td>
<td ALIGN=center>
<p> all
</td>
</tr>
</table>
<p></center> </p>
<p> The hg rows and columns of the table describes compatibility to hg&#8217;s glob syntax rather than its default regular-expression syntax. When writing to an hg repository from any other kind, <code>reposurgeon</code> prepends to the output .hgignore a &quot;syntax: glob&quot; line.</p>
<h2>TRANSLATION STYLE</h2>
<p> After converting a CVS, SVN, or BitKeeper repository, check for and remove $-cookies in the head revision(s) of the files. The full Subversion set is $Date:, $Revision:, $Author:, $HeadURL and $Id:. CVS uses $Author:, $Date:, $Header:, $Id:, $Log:, $Revision:, also (rarely) $Locker:, $Name:, $RCSfile:, $Source:, and $State:. </p>
<p> When you need to specify a commit, use the action-stamp format that <code>references lift</code> generates when it can resolve an SVN or CVS reference in a comment. It is best that you <i>not vary from this format</i>, even in trivial ways like omitting the &#8216;Z&#8217; or changing the &#8216;T&#8217; or &#8216;!&#8217; or &#8216;:&#8217;. Making action stamps uniform and machine-parseable will have good consequences for future repository-browsing tools. </p>
<p> Sometimes, in converting a repository, you may need to insert an explanatory comment &#8211; for example, if metadata has been garbled or missing and you need to point to that fact. It&#8217;s helpful for repository-browsing tools if there is a uniform syntax for this that is highly unlikely to show up in repository comments. We recommend enclosing translation notes in [[ ]]. This has the advantage of being visually similar to the [ ] traditionally used for editorial comments in text. </p>
<p> It is good practice to include, in the comment for the root commit of the repository, a note dating and attributing the conversion work and explaining these conventions. Example: </p>
<p> [[This repository was converted from Subversion to git on 2011-10-24 by Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. Here and elsewhere, conversion notes are enclosed in double square brackets. Junk commits generated by cvs2svn have been removed, commit references have been mapped into a uniform VCS-independent syntax, and some comments edited into summary-plus-continuation form.]] </p>
<p> It is also good practice to include a generated tag at the point of conversion. E.g </p>
<dl>
<dt>
<dd>
<pre>
mailbox_in --create &lt;&lt;EOF
Tag-Name: git-conversion
Marks the spot at which this repository was converted from Subversion to git.
EOF
</pre>
</dl>
<h2>ADVANCED EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
define lastchange
{
    @max(= B &amp; [/ ChangeLog / ] &amp; / {0} / B) ? list
}
</code></pre>
</dl>
<p> List the last commit that refers to a ChangeLog file containing a specified string. (The trick here is that ? extends the singleton set consisting of the last eligible ChangeLog blob to its set of referring commits, and <code>list</code>only notices the commits.)</p>
<h2>STREAM SYNTAX EXTENSIONS</h2>
<p> The event-stream parser in &#8220;reposurgeon&#8221; supports some extended syntax. Exporters designed to work with &#8220;reposurgeon&#8221; may have a &#8211;reposurgeon option that enables emission of extended syntax; notably, this is true of <code><a href="/docs/linux/man/1-cvs-fast-export/">cvs-fast-export</a></code>(1). The remainder of this section describes these syntax extensions. The properties they set are (usually) preserved and re-output when the stream file is written. </p>
<p> The token &#8220;#reposurgeon&#8221; at the start of a comment line in a fast-import stream signals reposurgeon that the remainder is an extension command to be interpreted by &#8220;reposurgeon&#8221;. </p>
<p> One such extension command is implemented: <code>#sourcetype</code>, which behaves identically to the reposurgeon<code>sourcetype</code> command. An exporter for a version-control system named &#8220;frobozz&#8221; could, for example, say </p>
<dl>
<dt>
<dd>
<pre>
#reposurgeon sourcetype frobozz
</pre>
</dl>
<p> Within a commit, a magic comment of the form &#8220;#legacy-id&#8221; declares a legacy ID from the stream file&#8217;s source version-control system. </p>
<p> Also accepted is the bzr syntax for setting per-commit properties. While parsing commit syntax, a line beginning with the token &#8220;property&#8221; must contibue with a whitespace-separated property-name token. If it is then followed by a newline it is taken to set that boolean-valued property to true. Otherwise it must be followed by a numeric token specifying a data length, a space, following data (which may contain newlines) and a terminating newline. For example: </p>
<dl>
<dt>
<dd>
<pre>
commit refs/heads/master
mark :1
committer Eric S. Raymond &lt;esr [at] thyrsus.com&gt; 1289147634 -0500
data 16
Example commit.
property legacy-id 2 r1
M 644 inline README
</pre>
</dl>
<p> Unlike other extensions, bzr properties are only preserved on stream output if the preferred type is bzr, because any importer other than bzr&#8217;s will choke on them.</p>
<h2>INCOMPATIBLE LANGUAGE CHANGES</h2>
<p> In versions before 3.23, &#8220;prefer&#8221; changed the repository type as well as the preferred output format. </p>
<p> In versions before 3.0, the general command syntax put the command verb first, then the selection set (if any) then modifiers (VSO). It has changed to optional selection set first, then command verb, then modifiers (SVO). The change made parsing simpler, allowed abolishing some noise keywords, and recapitulates a successful design pattern in some other Unix tools &#8211; notably <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1). </p>
<p> In versions before 3.0, path expressions only matched commits, not commits and the associated blobs as well. The names of the &#8220;a&#8221; and &#8220;c&#8221; flags were different. </p>
<p> In <code>reposurgeon</code> versions before 3.0, the delete command had the semantics of squash; also, the policy flags did not require a &#8220;&#8211;&#8221; prefix. The &#8220;&#8211;delete&#8221; flag was named &#8220;obliterate&#8221;. </p>
<p> In <code>reposurgeon</code> versions before 3.0, read and write optionally took file arguments rather than requiring redirects (and the write command never wrote into directories). This was changed in order to allow these commands to have modifiers. These modifiers replaced several global options that no longer exist. </p>
<p> In <code>reposurgeon</code> versions before 3.0, the earliest factor in a unite command always kept its tag and branch names unaltered. The new rule for resolving name conflicts, giving priority to the latest factor, produces more natural behavior when uniting two repositories end to end; the master branch of the second (later) one keeps its name. </p>
<p> In <code>reposurgeon</code> versions before 3.0, the tagify command expected policies as trailing arguments to alter its behaviour. The new syntax uses similarly named options with leading dashes, that can appear anywhere after the tagify command </p>
<p> In versions before 2.9. the syntax of &quot;authors&quot;, &quot;legacy&quot;, &quot;list&quot;, and &quot;mailbox_{in|out}&quot; was different (and &quot;legacy&quot; was &quot;fossils&quot;). They took plain filename arguments rather that using redirect &lt; and &gt;.</p>
<h2>LIMITATIONS AND GUARANTEES</h2>
<p> Guarantee: In DVCses that use commit hashes, editing with <code>reposurgeon</code> never changes the hash of a commit object unless (a) you edit the commit, or (b) it is a descendant of an edited commit in a VCS that includes parent hashes in the input of a child object&#8217;s hash (git and hg both do this). </p>
<p> Guarantee: <code>reposurgeon</code> only requires main memory proportional to the size of a repository&#8217;s metadata history, not its entire content history. (Exception: the data from inline content is held in memory.) </p>
<p> Guarantee: In the worst case, <code>reposurgeon</code> makes its own copy of every content blob in the repository&#8217;s history and thus uses intermediate disk space approximately equal to the size of a repository&#8217;s content history. However, when the repository to be edited is presented as a stream file, <code>reposurgeon</code> requires no or only very little extra disk space to represent it; the internal representation of content blobs is a (seek-offset, length) pair pointing into the stream file. </p>
<p> Guarantee: <code>reposurgeon</code> never modifies the contents of a repository it reads, nor deletes any repository. The results of surgery are always expressed in a new repository. </p>
<p> Guarantee: Any line in a fast-import stream that is not a part of a command <code>reposurgeon</code> parses and understands will be passed through unaltered. At present the set of potential passthroughs is known to include the <code>progress</code>, the <code>options</code>, and <code>checkpoint</code> commands as well as comments led by #. </p>
<p> Guarantee: All <code>reposurgeon</code> operations either preserve all repository state they are not explicitly told to modify or warn you when they cannot do so. </p>
<p> Guarantee: <code>reposurgeon</code> handles the bzr commit-properties extension, correctly passing through property items including those with embedded newlines. (Such properties are also editable in the mailbox format.) </p>
<p> Limitation: Because <code>reposurgeon</code> relies on other programs to generate and interpret the fast-import command stream, it is subject to bugs in those programs. </p>
<p> Limitation: bzr suffers from deep confusion over whether its unit of work is a repository or a floating branch that might have been cloned from a repo or created from scratch, and might or might not be destined to be merged to a repo one day. Its exporter only works on branches, but its importer creates repos. Thus, a rebuild operation will produce a subdirectory structure that differs from what you expect. Look for your content under the subdirectory &#8216;trunk&#8217;. </p>
<p> Limitation: under git, signed tags are imported verbatim. However, any operation that modifies any commit upstream of the target of the tag will invalidate it. </p>
<p> Limitation: Stock git (at least as of version 1.7.3.2) will choke on property extension commands. Accordingly, <code>reposurgeon</code> omits them when rebuilding a repo with git type. </p>
<p> Limitation: Converting an hg repo that uses bookmarks (not branches) to git can lose information; the branch ref that git assigns to each commit may not be the same as the hg bookmark that was active when the commit was originally made under hg. Unfortunately, this is a real ontological mismatch, not a problem that can be fixed by cleverness in <code>reposurgeon</code>. </p>
<p> Limitation: Converting an hg repo that uses branches to git can lose information because git does not store an explicit branch as part of commit metadata, but colors commits with branch or tag names on the fly using a specific coloring algorithm, which might not match the explicit branch assignments to commits in the original hg repo. Reposurgeon preserves the hg branch information when reading an hg repo, so it is available from within reposurgeon itself, but there is no way to preserve it if the repo is written to git. </p>
<p> Limitation: While the Subversion read-side support is in good shape, the write-side support is more of a sketch or proof-of-concept than a robust implementation; it only works on very simple cases and does not round-trip. It may improve in future releases. </p>
<p> Limitation: Not all BitKeeper versions have the fast-import and fast-export commands that <code>reposurgeon</code> requires. They are present back to the 7.3 opensource version. </p>
<p> Limitation: <code>reposurgeon</code> may misbehave under a filesystem which smashes case in filenames, or which nominally preserves case but maps names differing only by case to the same filesystem node (Mac OS X behaves like this by default). Problems will arise if any two paths in a repo differ by case only. To avoid the problem on a Mac, do all your surgery on an HFS+ file system formatted with case sensitivity specifically enabled. </p>
<p> Limitation: If whitespace followed by # appears in a string or regexp command argument, it will be misinterpreted as the beginning of a line-ending comment and screw up parsing. </p>
<p> Guarantee: As version-control systems add support for the fast-import format, their repositories will become editable by <code>reposurgeon</code>.</p>
<h2>REQUIREMENTS</h2>
<p> <code>reposurgeon</code> relies on importers and exporters associated with the VCSes it supports. </p>
<p> git</p>
<dl>
<dt>
<dd> Core git supports both export and import.</dl>
<p> bzr</p>
<dl>
<dt>
<dd> Requires bzr plus the bzr-fast-import plugin.</dl>
<p> hg</p>
<dl>
<dt>
<dd> Requires core hg, the hg-fastimport plugin, and the third-party hg-fast-export.py script.</dl>
<p> svn</p>
<dl>
<dt>
<dd> Stock Subversion commands support export and import.</dl>
<p> darcs</p>
<dl>
<dt>
<dd> Stock darcs commands support export and import.</dl>
<p> CVS</p>
<dl>
<dt>
<dd> Requires cvs-fast-export. Note that the quality of CVS lifts may be poor, with individual lifts requiring serious hand-hacking. This is due to inherent problems with CVS&#8217;s file-oriented model.</dl>
<p> RCS</p>
<dl>
<dt>
<dd> Requires cvs-fast-export (yes, that&#8217;s not a typo; cvs-fast-export handles RCS collections as well). The caveat for CVS applies.</dl>
<h2>CANONICALIZATION RULES</h2>
<p> It is expected that <code>reposurgeon</code> will be extended with more deletion policies. Policy authors may need to know more about how a commit&#8217;s file operation sequence is reduced to normal form after operations from deleted commits are prepended to it. </p>
<p> Recall that each commit has a list of file operations, each a M (modify), D (delete), R (rename), C (copy), or &#8216;deleteall&#8217; (delete all files). Only M operations have associated blobs. Normally there is only one M operation per individual file in a commit&#8217;s operation list. </p>
<p> To understand how the reduction process works, it&#8217;s enough to understand the case where all the operation in the list are working on the same file. Sublists of operations referring to different files don&#8217;t affect each other and reducing them can be thought of as separate operations. Also, a &quot;deleteall&quot; acts as a D for everything and cancels all operations before it in the list. </p>
<p> The reduction process walks through the list from the beginning looking for adjacent pairs of operations it can compose. The following table describes all possible cases and all but one of the reductions. <center></p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center> M + D &rarr; D </td>
<td>
<p> If a file is modified then deleted, the result is as though it had been deleted. If the M was the only modify for the file, it&#8217;s removed too.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> M a + R a b &rarr; R a b + M b </td>
<td>
<p> The purpose of this transformation is to push renames toward the beginning of the list, where they may become adjacent to another R or C they can be composed with. If the M is the only modify operation for this file, the rename is dropped.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> M a + C a b </td>
<td>
<p> No reduction.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> M b + R a b &rarr; nothing </td>
<td>
<p> Should be impossible, and may indicate repository corruption.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> M b + C a b &rarr; nothing </td>
<td>
<p> The copy undoes the modification.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> D + M &rarr; M </td>
<td>
<p> If a file is deleted and modified, the result is as though the deletion had not taken place (because M operations store entire files, not deltas).
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> D + {D|R|C} </td>
<td>
<p> These cases should be impossible and would suggest the repository has been corrupted.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> R a b + D a </td>
<td>
<p> Should never happen, and is another case that would suggest repository corruption.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> R a b + D b &rarr; D a </td>
<td>
<p> The delete removes the just-renamed file.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> {R|C} + M </td>
<td>
<p> No reduction.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> R a b + R b c &rarr; R a c </td>
<td>
<p> The b terms have to match for these operations to have made sense when they lived in separate commits; if they don&#8217;t, it indicates repository corruption.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> R a b + C b c </td>
<td>
<p> No reduction.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> C a b + D a &rarr; R a b </td>
<td>
<p> Copy followed by delete of the source is a rename.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> C a b + D b &rarr; nothing </td>
<td>
<p> This delete undoes the copy.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> C a b + R a c </td>
<td>
<p> No reduction.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> C a b + R b c &rarr; C a c </td>
<td>
<p> Copy followed by a rename of the target reduces to single copy
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> C + C </td>
<td>
<p> No reduction.
</td>
</tr>
</table>
<p></center> </p>
<h2>CRASH RECOVERY</h2>
<p> This section will become relevant only if <code>reposurgeon</code> or something underneath it in the software and hardware stack crashes while in the middle of writing out a repository, in particular if the target directory of the rebuild is your current directory. </p>
<p> The tool has two conflicting objectives. On the one hand, we never want to risk clobbering a pre-existing repo. On the other hand, we want to be able to run this tool in a directory with a repo and modify it in place. </p>
<p> We resolve this dilemma by playing a game of three-directory monte. </p>
<dl>
<dt>
<dd> 1. First, we build the repo in a freshly-created staging directory. If your target directory is named /path/to/foo, the staging directory will be a peer named /path/to/foo-stageNNNN, where NNNN is a cookie derived from <code>reposurgeon</code>&#8216;s process ID.</dl>
<dl>
<dt>
<dd> 2. We then make an empty backup directory. This directory will be named /path/to/foo.~N~, where N is incremented so as not to conflict with any existing backup directories. <code>reposurgeon</code> never, under any circumstances, ever deletes a backup directory. </p>
<p> So far, all operations are safe; the worst that can happen up to this point if the process gets interrupted is that the staging and backup directories get left behind.</dl>
<dl>
<dt>
<dd> 3. The critical region begins. We first move everything in the target directory to the backup directory.</dl>
<dl>
<dt>
<dd> 4. Then we move everything in the staging directory to the target.</dl>
<dl>
<dt>
<dd> 5. We finish off by restoring untracked files in the target directory from the backup directory. That ends the critical region.</dl>
<p> During the critical region, all signals that can be ignored are ignored.</p>
<h2>ERROR RETURNS</h2>
<p> Returns 1 on fatal error, 0 otherwise. In batch mode all errors are fatal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bzr/">bzr</a></code>(1), <code><a href="/docs/linux/man/1-cvs/">cvs</a></code>(1), <code><a href="/docs/linux/man/1-darcs/">darcs</a></code>(1), <code><a href="/docs/linux/man/1-git/">git</a></code>(1), <code><a href="/docs/linux/man/1-hg/">hg</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-svn/">svn</a></code>(1). <code><a href="/docs/linux/man/1-bk/">bk</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;; project page at m[blue]<code><a rel="nofollow" href="http://www.catb.org/~esr/reposurgeon">http://www.catb.org/~esr/reposurgeon</a></code>m[].</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> DVCS Migration HOWTO</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.catb.org/esr/dvcs-migration-guide.html">http://www.catb.org/esr/dvcs-migration-guide.html</a></dl>
<dt> 2.</p>
<dd> Python&#8217;s</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://docs.python.org/2/library/re.html">http://docs.python.org/2/library/re.html</a></dl>
</dl>
<h2>Index</h2>
