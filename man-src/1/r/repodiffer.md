---
title: "repodiffer(1)"
name: "repodiffer"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repodiffer/"
description: "repodiffer – report differences between repository histories"
---

<h2 class="name">NAME</h2>
<p> repodiffer &#8211; report differences between repository histories </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>repodiffer</code> [&#8211;ignore&nbsp;<wbr><i>parts</i>] [&#8211;quiet] [&#8211;verbose&nbsp;<wbr><i>level</i>] [&#8211;show-equal] [&#8211;changes-only] [&#8211;full-hash] [&#8211;tree-diff] [&#8211;legacy-map&nbsp;<wbr><i>mapfile</i>] [&#8211;single&nbsp;<wbr><i>id1=id2</i>] <i>repo-or-stream1</i> <i>repo-or-stream2</i></dl>
<h2>DESCRIPTION</h2>
<dd>This tool reports differences between two repository histories. The histories may be presented as git repository directories or as fast-import streams, or as one of each. </p>
<p> Revisions are first paired into correspondence by committer and commit date. Any revision in the left-hand (L) history that cannot be paired with a revision in the right-hand (R) history is interpreted as having been deleted; any revision in the R history that cannot be paired with a revision in the L history is interpreted as having been inserted. </p>
<p> For each changed, inserted, or deleted revision, a summary line is emitted identifying it by commit ID (for a repo) or mark (for a stream file) in the first history. In change reports, the corresponding revision in the second history is similarly identified and the report indicates the nature of the changes. </p>
<p> A trailing statistics line summarizes the operation counts. </p>
<p> Tags and heads are compared as well. Two tags match if their contents do and they point at paired commits.</p>
<h2>OPTIONS</h2>
<p> The &#8211;changes-only or -c option shows changes only, suppressing listing of insertions and deletions. </p>
<p> The &#8211;show-equal or -e option enables listing of equal commits. </p>
<p> The &#8211;legacy-map or -m option takes a legacy map file in the format produced by reposurgeon, associating legacy commit IDs with committer/time pairs. If the tool can find a matching committer/time pair for a commit in this file, reports on this commit (and any matched pair it is part of) will be decorated with the legacy ID of the commit. (This will work, in particular, for displaying Subversion revisions of commits lifted from a Subversion file.) </p>
<p> The &#8211;single or -s option compares single commits in detail. The argument must be a pair of commit IDs (marks or hashes) separated by an equals sign. </p>
<p> The &#8211;ignore or -i option causes differences between specified parts to be ignored. Part tags are as follows: </p>
<p> author</p>
<dl>
<dt>
<dd> Ignore differences in the (name part of the) author field.</dl>
<p> authordate</p>
<dl>
<dt>
<dd> Ignore differences in the author date part.</dl>
<p> committer</p>
<dl>
<dt>
<dd> Ignore differences in the (name part of the) committer field.</dl>
<p> committerdate</p>
<dl>
<dt>
<dd> Ignore differences in the commit date part</dl>
<p> parents</p>
<dl>
<dt>
<dd> Ignore differences in parent links.</dl>
<p> timezone</p>
<dl>
<dt>
<dd> Apply a modulo 360 operation to timestamps before comparison, so as to ignore time-zone skew.</dl>
<p> tree</p>
<dl>
<dt>
<dd> Ignore tree-content differences. (It is not expected that this option will be useful; it is provided for completeness&#8217;s sake.)</dl>
<p> gitignore</p>
<dl>
<dt>
<dd> Ignore .gitignore and .cvsignore files when comparing tree content. Useful if you are comparing translations done by pairs of lifting tools only one of which lifts these; a notable case of this is reposurgeon vs. git-svn.</dl>
<p> email</p>
<dl>
<dt>
<dd> Ignore email addresses when comparing names. This can be useful when comparing two repositories translated from Subversion; typically they&#8217;ll have the Subversion Unix user ID as the name part of the address, but whether and how a host part is generated for the address varies.</dl>
<p> One of these or a comma-separated list of several can be specified. </p>
<p> The &#8211;fullhash or -f option forces reporting of full 40-digit hash IDs, rather than the normal short hash. </p>
<p> Normally only the names of differing files are listed. With the &#8211;tree-diff option, context diffs of the files are listed. </p>
<p> The &#8211;quiet or -q option suppresses the progress meter. </p>
<p> The &#8211;verbose or -v option enables debugging messages that are probably only of interest to developers; consult the source code for details.</p>
<h2>RETURN VALUES</h2>
<p> For scripting use, this program returns 0 unless content (tree) differences were found in matching commits, in which case it returns 1. Right-side-only or left-side-only commits do not cause a return of 1, nor do differences in change comments only.</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. This tool is distributed with reposurgeon; see the project page at m[blue]<code><a rel="nofollow" href="http://www.catb.org/~esr/reposurgeon">http://www.catb.org/~esr/reposurgeon</a></code>m[]. </p>
<h2>Index</h2>
