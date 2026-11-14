---
title: "repotool(1)"
name: "repotool"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repotool/"
description: "repotool – query or manipulate a CVS, Subversion, git, bzr, hg, or darcs repository in a uniform way"
---

<h2 class="name">NAME</h2>
<p> repotool &#8211; query or manipulate a CVS, Subversion, git, bzr, hg, or darcs repository in a uniform way </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>repotool</code> [<i>action</i>] [<i>URL-or-dir</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>repotool is a script wrapper around repository operations that differ by version-control system. It is little use by itself, existing mainly to generate and simplify a conversion makefile usable with <code><a href="/docs/linux/man/1-reposurgeon/">reposurgeon</a></code>(1). </p>
<p> Not all actions are supported on all systems. You will get an error message and a return value of 1 when attempting an unsupported action. </p>
<p> The &quot;initialize&quot; option takes a project name (and, optionally, following source and target VCCS types) and generates a Makefile that will sequence various steps of a repository conversion. It also generates stub lift and options files. This is meant to be run in an empty work directory, and it is an error to do &#8216;initialize&#8217; where any of these files already exist. Afterwards, you will need to set some variables in the Makefile; read its header comment. </p>
<p> The &#8216;export&#8217; action, run from within a repository directory, dumps a copy of a CVS, Subversion, git, bzr, hg, or darcs repository to a flat history file readable by reposurgeon. The format is usually a git-fast-import stream, except that Subversion repositories export as Subversion dump files; the point is to be a lossless erepresentation, or as close to one as possible. </p>
<p> The &#8216;tags&#8217; option, run from within a repository directory, returns a list of the repository&#8217;s release tags. </p>
<p> The &#8216;branches&#8217; option, run from within a repository directory , returns a list of the repository&#8217;s branch names. </p>
<p> The &#8216;checkout&#8217; option checks out a working copy of the repository. It must be called from within the repository. It takes one required argument &#8211; the checkout directory location. It may take a following optional argument which is a tag or revision specification; if this argument is not given, the tip (most recent) mainline revision is assumed. </p>
<p> The &#8216;compare&#8217; action takes two repository directories and a revision spec (typically a tag name). If the revision spec is omitted, the tip of the main line of both repositories will be used. The selected revisions are cpmpared with diff -q -r, with noise due to SCCS/RCS/CVS keyword expansion ignored. You can follow the command verb with one or more -x options followed by basenames of paths to exclude from comparison. You can get a context-diff report on file differences with the -u option. </p>
<p> The &#8216;compare-tags&#8217; action takes two repository directories, extracts a list of tags from the first, then compares the repository contents at each tag in the list, generating a compare report for each. You can follow the command verb with one or more -x options followed by basenames of paths to exclude from comparison. You can get a context-diff report on file differences with the -u option. </p>
<p> The &#8216;compare-branches&#8217; action takes two repository directories, extracts a list of branches common to both, then compares the repository contents at each branch in the list, generating a compare report for each. You can follow the command verb with one or more -x options followed by basenames of paths to exclude from comparison. You can get a context-diff report on file differences with the -u option. </p>
<p> The &#8216;compare-all&#8217; action takes two repository directories, and runs all 3 above compare actions on them. Even if the same name is a tag in one repository and a branch in the other, it will compare them against each other. Not distinguishing them is useful as CVS tags that are not applied to every file in the repository may get converted to branches. The options are the same as &#8216;compare-tags&#8217;. </p>
<p> The &#8216;mirror&#8217; action makes or updates a local mirror of a Subversion or CVS repo. It requires a single argument, either a Subversion URL or a CVS URL, or the name of a local mirror directory created by a previous run. The first form creates a local mirror of the repository in a directory named after the last segment of the URL, with the suffix &#8220;-mirror&#8221; (the local mirror name can be overridden by an optional) second argument. The second form updates the local mirror, doing an incremental fetch; just give the mirror directory name. </p>
<p> Subversion URLs are as specified in the public documentation for Subversion. CVS URLs must specify a host and repository path, followed by a &#8216;#&#8217;, followed by a module name.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> This program uses the $TMPDIR environment variable, defaulting to /tmp if it is not set.</p>
<h2>REQUIREMENTS</h2>
<p> The export action is a wrapper around either native export facilities or the following engines: <code><a href="/docs/linux/man/1-cvs-fast-export/">cvs-fast-export</a></code>(1) (for CVS), <code><a href="/docs/linux/man/1-svnadmin/">svnadmin</a></code>(1) (for SVN), <code><a href="/docs/linux/man/1-hg-fast-export-py/">hg-fast-export.py</a></code>(1) (for hg). You must have the appropriate engine in your $PATH for whatever kind of repository you are streaming.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-reposurgeon/">reposurgeon</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. This tool is distributed with reposurgeon; see the project page at m[blue]<code><a rel="nofollow" href="http://www.catb.org/~esr/reposurgeon">http://www.catb.org/~esr/reposurgeon</a></code>m[]. </p>
<h2>Index</h2>
