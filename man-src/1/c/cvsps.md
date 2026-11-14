---
title: "cvsps(1)"
name: "cvsps"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cvsps/"
description: "CVSps – create patchset information from CVS"
---

<h2>NAME</h2>
<p> CVSps &#8211; create patchset information from CVS</p>
<h2>SYNOPSIS</h2>
<p> <code>cvsps</code> [-h] [-x] [-u] [-z &lt;fuzz&gt;] [-g] [-s &lt;patchset&gt;] [-a &lt;author&gt;] [-f &lt;file&gt;] [-d &lt;date1&gt; [-d &lt;date2&gt;]] [-l &lt;text&gt;] [-b &lt;branch&gt;] [-r &lt;tag&gt; [-r &lt;tag&gt;]] [-p &lt;directory&gt;] [-v] [-t] [&#8211;norc] [&#8211;summary-first] [&#8211;test-log &lt;filename&gt;] [&#8211;bkcvs] [&#8211;no-rlog] [&#8211;diff-opts &lt;option string&gt;] [&#8211;cvs-direct] [&#8211;debuglvl &lt;bitmask&gt;] [-Z &lt;compression&gt;] [&#8211;root &lt;cvsroot&gt;] [-q] [-A] [&lt;repository&gt;]</p>
<h2>DESCRIPTION</h2>
<p> CVSps is a program for generating &#8216;patchset&#8217; information from a CVS repository. A patchset in this case is defined as a set of changes made to a collection of files, and all committed at the same time (using a single &#8216;cvs commit&#8217; command). This information is valuable to seeing the big picture of the evolution of a cvs project. While cvs tracks revision information, it is often difficult to see what changes were committed &#8216;atomically&#8217; to the repository.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> display usage summary</p>
<dt><code>-x</code></p>
<dd> ignore (and rebuild) ~/.cvsps/cvsps.cache file</p>
<dt><code>-u</code></p>
<dd> update ~/.cvsps/cvsps.cache file</p>
<dt><code>-z &lt;fuzz&gt;</code></p>
<dd> set the timestamp fuzz factor for identifying patch sets</p>
<dt><code>-g</code></p>
<dd> generate diffs of the selected patch sets</p>
<dt><code>-s &lt;patchset&gt;[-[&lt;patchset&gt;]][,&lt;patchset&gt;&#8230;]</code></p>
<dd> generate a diff for a given patchsets and patchset ranges</p>
<dt><code>-a &lt;author&gt;</code></p>
<dd> restrict output to patchsets created by author</p>
<dt><code>-f &lt;file&gt;</code></p>
<dd> restrict output to patchsets involving file</p>
<dt><code>-d &lt;date1&gt; -d &lt;date2&gt;</code></p>
<dd> if just one date specified, show revisions newer than date1. If two dates specified, show revisions between two dates.</p>
<dt><code>-l &lt;regex&gt;</code></p>
<dd> restrict output to patchsets matching regex in log message</p>
<dt><code>-b &lt;branch&gt;</code></p>
<dd> restrict output to patchsets affecting history of branch. If you want to restrict to the main branch, use a branch of &#8216;HEAD&#8217;.</p>
<dt><code>-r &lt;tag1&gt; -r &lt;tag2&gt;</code></p>
<dd> if just one tag specified, show revisions since tag1. If two tags specified, show revisions between the two tags.</p>
<dt><code>-p &lt;dir&gt;</code></p>
<dd> output individual patchsets as files in &lt;dir&gt; as &lt;dir&gt;/&lt;patchset&gt;.patch</p>
<dt><code>-v</code></p>
<dd> show very verbose parsing messages</p>
<dt><code>-t</code></p>
<dd> show some brief memory usage statistics</p>
<dt><code>&#8211;norc</code></p>
<dd> when invoking cvs, ignore the .cvsrc file</p>
<dt><code>&#8211;summary-first</code></p>
<dd> when multiple patchset diffs are being generated, put the patchset summary for all patchsets at the beginning of the output.</p>
<dt><code>&#8211;test-log &lt;captured cvs log file&gt;</code></p>
<dd> for testing changes, you can capture cvs log output, then test against this captured file instead of hammering some poor CVS server</p>
<dt><code>&#8211;bkcvs</code></p>
<dd> (see note below) for use in parsing the BK-&gt;CVS tree log formats only. This enables some hacks which are not generally applicable.</p>
<dt><code>&#8211;no-rlog</code></p>
<dd> disable the use of rlog internally. Note: rlog is required for stable PatchSet numbering. Use with care.</p>
<dt><code>&#8211;diff-opts &lt;option string&gt;</code></p>
<dd> send a custom set of options to diff, for example to increase the number of context lines, or change the diff format.</p>
<dt><code>&#8211;cvs-direct (&#8211;no-cvs-direct)</code></p>
<dd> enable (disable) built-in cvs client code. This enables the &#8216;pipelining&#8217; of multiple requests over a single client, reducing the overhead of handshaking and authentication to one per PatchSet instead of one per file.</p>
<dt><code>&#8211;debuglvl &lt;bitmask&gt;</code></p>
<dd> enable various debug output channels.</p>
<dt><code>-Z &lt;compression&gt;</code></p>
<dd> A value 1-9 which specifies amount of compression. A value of 0 disables compression.</p>
<dt><code>&#8211;root &lt;cvsroot&gt;</code></p>
<dd> Override the setting of CVSROOT (overrides working dir. and environment). For &#8211;cvs-direct only.</p>
<dt><code>-q</code></p>
<dd> Be quiet about warnings.</p>
<dt><code>-A</code></p>
<dd> Show ancestor branch when a new branch is found.</p>
<dt><code>&lt;repository&gt;</code></p>
<dd> Operate on the specified repository (overrides working dir.)</dl>
<h2>NOTE ON TAG HANDLING</h2>
<p> Tags are fundamentally &#8216;file at a time&#8217; in cvs, but like everything else, it would be nice to imagine that they are &#8216;repository at a time.&#8217; The approach cvsps takes is that a tag is assigned to a patchset. The meaning of this is that after this patchset, every revision of every file is after the tag (and conversely, before this patchset, at least one file is still before the tag). However, there are two kinds of inconsistent (or &#8216;funky&#8217;) tags that can be created, even when following best practices for cvs. </p>
<p> The first is what is called a FUNKY tag. A funky tag is one where there are patchsets which are chronologically (and thus by patchset id) earlier than the tag, but are tagwise after. These tags will be marked as &#8216;**FUNKY**&#8217; in the Tag: section of the cvsps output. When a funky tag is specified as one of the &#8216;-r&#8217; arguments, there are some number of patchsets which need to be considered out of sequence. In this case, the patchsets themselves will be labeled FUNKY and will be processed correctly. </p>
<p> The second is called an INVALID tag. An invalid tag is a tag where there are patchsets which are chronologically (and thus by patchset id) earlier than the tag, but which have members which are tagwise both before, and after the tag, in the same patchset. If an INVALID tag is specified as one of the &#8216;-r&#8217; arguments, cvsps will flag each member of the affected patchsets as before or after the tag and the patchset summary will indicate which members are which, and diffs will be generated accordingly.</p>
<h2>NOTE ON CVS VERSIONS</h2>
<p> Among the different cvs subcommands used by cvsps is the &#8216;rlog&#8217; command. The rlog command is used to get revision history of a module, and it disregards the current working directory. The important difference between &#8216;rlog&#8217; and &#8216;log&#8217; (from cvsps perspective) is the &#8216;rlog&#8217; will include log data for files not in the current working directory. The impact of this is mainly when there are directories which at one time had files, but are now empty, and have been pruned from the working directory with the &#8216;-P&#8217; option. If &#8216;rlog&#8217; is not used, these files logs will not be parsed, and the PatchSet numbering will be unstable. </p>
<p> The main problem with &#8216;rlog&#8217; is that, until cvs version 1.11.1, &#8216;rlog&#8217; was an alias for the &#8216;log&#8217; command. This means, for old versions of cvs, &#8216;rlog&#8217; has different semantics and usage. cvsps will attempt to work around this problem by detecting capable versions of cvs. If an old version is detected, &#8216;log&#8217; will be used instead of &#8216;rlog&#8217;, and YMMV.</p>
<h2>NOTE ON GENERATED DIFFS</h2>
<p> Another important note is that cvsps will attempt, whenever possible, to use the r-commands (rlog, rdiff and co) instead of the local commands (log, diff, and update). This is to allow cvsps to function without a completely checked out tree. Because these r-commands are used, the generated diffs will include the module directory in them, and it is recommended to apply them in the working directory with the -p1 option to the patch command. However, if the &#8211;diff-opts option is specified (to change, for example, the lines of context), then rdiff cannot be used, because it doesn&#8217;t support arbitrary options. In this case, the patches will be generated without the module directory in the path, and -p0 will be required when applying the patch. When diffs are generated in cvs-direct mode (see below), however, they will always be -p1 style patches.</p>
<h2>NOTE ON BKCVS</h2>
<p> The &#8211;bkcvs option is a special operating mode that should only be used when parsing the log files from the BK -&gt; CVS exported linux kernel trees. cvsps uses special semantics for recreating the BK ChangeSet metadata that has been embedded in the log files for those trees. The &#8211;bkcvs option should only be specified when the cache file is being created or updated (i.e. initial run of cvsps, or when -u and -x options are used).</p>
<h2>NOTE ON CVS-DIRECT</h2>
<p> As of version 2.0b6 cvsps has a partial implementation of the cvs client code built in. This reduces the RTT and/or handshaking overhead from one per patchset member to one per patchset. This dramatically increases the speed of generating diffs over a slow link, and improves the consistency of operation. Currently the &#8211;cvs-direct option turns on the use of this code, but it very well may be default by the time 2.0 comes out. The built-in cvs code attempts to be compatible with cvs, but may have problems, which should be reported. It honors the CVS_RSH and CVS_SERVER environment variables, but does not parse the ~/.cvsrc file.</p>
<h2>NOTE ON CVSPS RC FILE</h2>
<p> CVSps parses an rc file at startup. This file should be located in ~/.cvsps/cvspsrc. The file should contain arguments, in the exact syntax as the command line, one per line. If an argument takes a parameter, the parameter should be on the same line as the argument.</p>
<h2>NOTE ON DATE FORMATS</h2>
<p> All dates are reported in localtime. This can be overridden (as usual) using the TZ environment variable. Dates as arguments must be in the format &#8216;yyyy/mm/dd hh:mm:ss&#8217;; for example,</p>
<dl>
<dt>
<dd> $ cvsps -d &#8216;2004/05/01 00:00:00&#8217; -d &#8216;2004/07/07 12:00:00&#8217;</dl>
<h2>SEE ALSO</h2>
<p> <code>cvs</code>(<code>1</code>), <code>ci</code>(<code>1</code>), <code>co</code>(<code>1</code>), <code>cvs</code>(<code>5</code>), <code>cvsbug</code>(<code>8</code>), <code>diff</code>(<code>1</code>), <code>grep</code>(<code>1</code>), <code>patch</code>(<code>1</code>), <code>rcs</code>(<code>1</code>), <code>rcsdiff</code>(<code>1</code>), <code>rcsmerge</code>(<code>1</code>), <code>rlog</code>(<code>1</code>).</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &quot;David Mansfield &lt;cvsps [at] dm.cobite.com&gt;&quot;</p>
<h2>BUGS</h2>
<p> No known bugs. </p>
<h2>Index</h2>
