---
title: "patch(1)"
name: "patch"
section: "1"
letter: "p"
url: "/docs/linux/man/1-patch/"
description: "patch – apply a diff file to an original"
---

<h2 class="name">NAME</h2>
<p> patch &#8211; apply a diff file to an original </p>
<h2>SYNOPSIS</h2>
<p> <code>patch</code> [<i>options</i>] [<i>originalfile</i> [<i>patchfile</i>]] </p>
<p> but usually just </p>
<p> <code>patch -p</code><i>num</i> <code>&lt;</code><i>patchfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>patch</code> takes a patch file <i>patchfile</i> containing a difference listing produced by the <code>diff</code> program and applies those differences to one or more original files, producing patched versions. Normally the patched versions are put in place of the originals. Backups can be made; see the <code>-b</code> or <code>&#8211;backup</code> option. The names of the files to be patched are usually taken from the patch file, but if there&#8217;s just one file to be patched it can be specified on the command line as <i>originalfile</i>. </p>
<p> Upon startup, patch attempts to determine the type of the diff listing, unless overruled by a <code>-c</code> (<code>&#8211;context</code>), <code>-e</code> (<code>&#8211;ed</code>), <code>-n</code> (<code>&#8211;normal</code>), or <code>-u</code> (<code>&#8211;unified</code>) option. Context diffs (old-style, new-style, and unified) and normal diffs are applied by the <code>patch</code> program itself, while <code>ed</code> diffs are simply fed to the <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1) editor via a pipe. </p>
<p> <code>patch</code> tries to skip any leading garbage, apply the diff, and then skip any trailing garbage. Thus you could feed an article or message containing a diff listing to <code>patch</code>, and it should work. If the entire diff is indented by a consistent amount, if lines end in <font SIZE="-1">CRLF</font>, or if a diff is encapsulated one or more times by prepending &quot;<code>&#8211; </code>&quot; to lines starting with &quot;<code>&#8211;</code>&quot; as specified by Internet RFC 934, this is taken into account. After removing indenting or encapsulation, lines beginning with <code>#</code> are ignored, as they are considered to be comments. </p>
<p> With context diffs, and to a lesser extent with normal diffs, <code>patch</code> can detect when the line numbers mentioned in the patch are incorrect, and attempts to find the correct place to apply each hunk of the patch. As a first guess, it takes the line number mentioned for the hunk, plus or minus any offset used in applying the previous hunk. If that is not the correct place, <code>patch</code> scans both forwards and backwards for a set of lines matching the context given in the hunk. First <code>patch</code> looks for a place where all lines of the context match. If no such place is found, and it&#8217;s a context diff, and the maximum fuzz factor is set to 1 or more, then another scan takes place ignoring the first and last line of context. If that fails, and the maximum fuzz factor is set to 2 or more, the first two and last two lines of context are ignored, and another scan is made. (The default maximum fuzz factor is 2.) </p>
<p> Hunks with less prefix context than suffix context (after applying fuzz) must apply at the start of the file if their first line number is 1. Hunks with more prefix context than suffix context (after applying fuzz) must apply at the end of the file. </p>
<p> If <code>patch</code> cannot find a place to install that hunk of the patch, it puts the hunk out to a reject file, which normally is the name of the output file plus a <code>.rej</code> suffix, or <code>#</code> if <code>.rej</code> would generate a file name that is too long (if even appending the single character <code>#</code> makes the file name too long, then <code>#</code> replaces the file name&#8217;s last character). </p>
<p> The rejected hunk comes out in unified or context diff format. If the input was a normal diff, many of the contexts are simply null. The line numbers on the hunks in the reject file may be different than in the patch file: they reflect the approximate location patch thinks the failed hunks belong in the new file rather than the old one. </p>
<p> As each hunk is completed, you are told if the hunk failed, and if so which line (in the new file) <code>patch</code> thought the hunk should go on. If the hunk is installed at a different line from the line number specified in the diff, you are told the offset. A single large offset <i>may</i> indicate that a hunk was installed in the wrong place. You are also told if a fuzz factor was used to make the match, in which case you should also be slightly suspicious. If the <code>&#8211;verbose</code> option is given, you are also told about hunks that match exactly. </p>
<p> If no original file <i>origfile</i> is specified on the command line, <code>patch</code> tries to figure out from the leading garbage what the name of the file to edit is, using the following rules. </p>
<p> First, <code>patch</code> takes an ordered list of candidate file names as follows:</p>
<dl>
<dt><code> &bull;</code></p>
<dd> If the header is that of a context diff, <code>patch</code> takes the old and new file names in the header. A name is ignored if it does not have enough slashes to satisfy the <code>-p</code><i>num</i> or <code>&#8211;strip=</code><i>num</i> option. The name <code>/dev/null</code> is also ignored.</p>
<dt><code> &bull;</code></p>
<dd> If there is an <code>Index:</code> line in the leading garbage and if either the old and new names are both absent or if <code>patch</code> is conforming to <font SIZE="-1">POSIX</font>, <code>patch</code> takes the name in the <code>Index:</code> line.</p>
<dt><code> &bull;</code></p>
<dd> For the purpose of the following rules, the candidate file names are considered to be in the order (old, new, index), regardless of the order that they appear in the header.</dl>
<p> Then <code>patch</code> selects a file name from the candidate list as follows:</p>
<dl>
<dt><code> &bull;</code></p>
<dd> If some of the named files exist, <code>patch</code> selects the first name if conforming to <font SIZE="-1">POSIX</font>, and the best name otherwise.</p>
<dt><code> &bull;</code></p>
<dd> If <code>patch</code> is not ignoring <font SIZE="-1">RCS</font>, ClearCase, Perforce, and <font SIZE="-1">SCCS</font> (see the <code>-g&nbsp;</code><i>num</i> or <code>&#8211;get=</code><i>num</i> option), and no named files exist but an <font SIZE="-1">RCS</font>, ClearCase, Perforce, or <font SIZE="-1">SCCS</font> master is found, <code>patch</code> selects the first named file with an <font SIZE="-1">RCS</font>, ClearCase, Perforce, or <font SIZE="-1">SCCS</font> master.</p>
<dt><code> &bull;</code></p>
<dd> If no named files exist, no <font SIZE="-1">RCS</font>, ClearCase, Perforce, or <font SIZE="-1">SCCS</font> master was found, some names are given, <code>patch</code> is not conforming to <font SIZE="-1">POSIX</font>, and the patch appears to create a file, <code>patch</code> selects the best name requiring the creation of the fewest directories.</p>
<dt><code> &bull;</code></p>
<dd> If no file name results from the above heuristics, you are asked for the name of the file to patch, and <code>patch</code> selects that name.</dl>
<p> To determine the <i>best</i> of a nonempty list of file names, <code>patch</code> first takes all the names with the fewest path name components; of those, it then takes all the names with the shortest basename; of those, it then takes all the shortest names; finally, it takes the first remaining name. </p>
<p> Additionally, if the leading garbage contains a <code>Prereq:</code> line, <code>patch</code> takes the first word from the prerequisites line (normally a version number) and checks the original file to see if that word can be found. If not, <code>patch</code> asks for confirmation before proceeding. </p>
<p> The upshot of all this is that you should be able to say, while in a news interface, something like the following: </p>
<dl>
<dt>
<dd> <code>| patch -d /usr/src/local/blurfl</code></dl>
<p> and patch a file in the <code>blurfl</code> directory directly from the article containing the patch. </p>
<p> If the patch file contains more than one patch, <code>patch</code> tries to apply each of them as if they came from separate patch files. This means, among other things, that it is assumed that the name of the file to patch must be determined for each diff listing, and that the garbage before each diff listing contains interesting things such as file names and revision level, as mentioned previously.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code> or <code>&#8211;backup</code></p>
<dd> Make backup files. That is, when patching a file, rename or copy the original instead of removing it. See the <code>-V</code> or <code>&#8211;version-control</code> option for details about how backup file names are determined.</p>
<dt><code>&#8211;backup-if-mismatch</code></p>
<dd> Back up a file if the patch does not match the file exactly and if backups are not otherwise requested. This is the default unless <code>patch</code> is conforming to <font SIZE="-1">POSIX</font>.</p>
<dt><code>&#8211;no-backup-if-mismatch</code></p>
<dd> Do not back up a file if the patch does not match the file exactly and if backups are not otherwise requested. This is the default if <code>patch</code> is conforming to <font SIZE="-1">POSIX</font>.</p>
<dt><code>-B</code> <i>pref</i> or <code>&#8211;prefix=</code><i>pref</i></p>
<dd> Use the <code>simple</code> method to determine backup file names (see the <code>-V </code><i>method</i> or <code>&#8211;version-control </code><i>method</i> option), and append <i>pref</i> to a file name when generating its backup file name. For example, with <code>-B&nbsp;/junk/</code> the simple backup file name for <code>src/patch/util.c</code> is <code>/junk/src/patch/util.c</code>.</p>
<dt><code>&#8211;binary</code></p>
<dd> Write all files in binary mode, except for standard output and <code>/dev/tty</code>. When reading, disable the heuristic for transforming CRLF line endings into LF line endings. This option is needed on <font SIZE="-1">POSIX</font> systems when applying patches generated on non-<font SIZE="-1">POSIX</font> systems to non-<font SIZE="-1">POSIX</font> files. (On <font SIZE="-1">POSIX</font> systems, file reads and writes never transform line endings. On Windows, reads and writes do transform line endings by default, and patches should be generated by <code>diff &#8211;binary</code> when line endings are significant.)</p>
<dt><code>-c</code> or <code>&#8211;context</code></p>
<dd> Interpret the patch file as a ordinary context diff.</p>
<dt><code>-d</code> <i>dir</i> or <code>&#8211;directory=</code><i>dir</i></p>
<dd> Change to the directory <i>dir</i> immediately, before doing anything else.</p>
<dt><code>-D</code> <i>define</i> or <code>&#8211;ifdef=</code><i>define</i></p>
<dd> Use the <code>#ifdef</code> &#8230; <code>#endif</code> construct to mark changes, with <i>define</i> as the differentiating symbol.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Print the results of applying the patches without actually changing any files.</p>
<dt><code>-e</code> or <code>&#8211;ed</code></p>
<dd> Interpret the patch file as an <code>ed</code> script.</p>
<dt><code>-E</code> or <code>&#8211;remove-empty-files</code></p>
<dd> Remove output files that are empty after the patches have been applied. Normally this option is unnecessary, since <code>patch</code> can examine the time stamps on the header to determine whether a file should exist after patching. However, if the input is not a context diff or if <code>patch</code> is conforming to <font SIZE="-1">POSIX</font>, <code>patch</code> does not remove empty patched files unless this option is given. When <code>patch</code> removes a file, it also attempts to remove any empty ancestor directories.</p>
<dt><code>-f</code> or <code>&#8211;force</code></p>
<dd> Assume that the user knows exactly what he or she is doing, and do not ask any questions. Skip patches whose headers do not say which file is to be patched; patch files even though they have the wrong version for the <code>Prereq:</code> line in the patch; and assume that patches are not reversed even if they look like they are. This option does not suppress commentary; use <code>-s</code> for that.</p>
<dt><code>-F</code> <i>num</i> or <code>&#8211;fuzz=</code><i>num</i></p>
<dd> Set the maximum fuzz factor. This option only applies to diffs that have context, and causes <code>patch</code> to ignore up to that many lines of context in looking for places to install a hunk. Note that a larger fuzz factor increases the odds of a faulty patch. The default fuzz factor is 2. A fuzz factor greater than or equal to the number of lines of context in the context diff, ordinarily 3, ignores all context.</p>
<dt><code>-g</code> <i>num</i> or <code>&#8211;get=</code><i>num</i></p>
<dd> This option controls <code>patch</code>&#8216;s actions when a file is under <font SIZE="-1">RCS</font> or <font SIZE="-1">SCCS</font> control, and does not exist or is read-only and matches the default version, or when a file is under ClearCase or Perforce control and does not exist. If <i>num</i> is positive, <code>patch</code> gets (or checks out) the file from the revision control system; if zero, <code>patch</code> ignores <font SIZE="-1">RCS</font>, ClearCase, Perforce, and <font SIZE="-1">SCCS</font> and does not get the file; and if negative, <code>patch</code> asks the user whether to get the file. The default value of this option is given by the value of the <code>PATCH_GET</code> environment variable if it is set; if not, the default value is zero.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of options and exit.</p>
<dt><code>-i</code> <i>patchfile</i> or <code>&#8211;input=</code><i>patchfile</i></p>
<dd> Read the patch from <i>patchfile</i>. If <i>patchfile</i> is <code>&#8211;</code>, read from standard input, the default.</p>
<dt><code>-l</code> or <code>&#8211;ignore-whitespace</code></p>
<dd> Match patterns loosely, in case tabs or spaces have been munged in your files. Any sequence of one or more blanks in the patch file matches any sequence in the original file, and sequences of blanks at the ends of lines are ignored. Normal characters must still match exactly. Each line of the context must still match a line in the original file.</p>
<dt><code>&#8211;merge</code> or <code>&#8211;merge=merge</code> or <code>&#8211;merge=diff3</code></p>
<dd> Merge a patch file into the original files similar to <code><a href="/docs/linux/man/1-diff3/">diff3</a></code>(1) or <code><a href="/docs/linux/man/1-merge/">merge</a></code>(1). If a conflict is found, <code>patch</code> outputs a warning and brackets the conflict with <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code> and <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> lines. A typical conflict will look like this:</dl>
<dl>
<dt>
<dd>
<pre><code>
&lt;&lt;&lt;&lt;&lt;&lt;&lt;
lines from the original file
|||||||
original lines from the patch
=======
new lines from the patch
&gt;&gt;&gt;&gt;&gt;&gt;&gt;

</code></pre>
<dl>
<dt>
<dd> The optional argument of <code>&#8211;merge</code> determines the output format for conflicts: the diff3 format shows the <code>|||||||</code> section with the original lines from the patch; in the merge format, this section is missing. The merge format is the default. </p>
<p> This option implies <code>&#8211;forward</code> and does not take the <code>&#8211;fuzz</code>=<i>num</i> option into account.</p>
<dt><code>-n</code> or <code>&#8211;normal</code></p>
<dd> Interpret the patch file as a normal diff.</p>
<dt><code>-N</code> or <code>&#8211;forward</code></p>
<dd> When a patch does not apply, patch usually checks if the patch looks like it has been applied already by trying to reverse-apply the first hunk. The <code>&#8211;forward</code> option prevents that. See also <code>-R</code>.</p>
<dt><code>-o</code> <i>outfile</i> or <code>&#8211;output=</code><i>outfile</i></p>
<dd> Send output to <i>outfile</i> instead of patching files in place. Do not use this option if <i>outfile</i> is one of the files to be patched. When <i>outfile</i> is <code>&#8211;</code>, send output to standard output, and send any messages that would usually go to standard output to standard error.</p>
<dt><code>-p</code><i>num</i> or <code>&#8211;strip</code><code>=</code><i>num</i></p>
<dd> Strip the smallest prefix containing <i>num</i> leading slashes from each file name found in the patch file. A sequence of one or more adjacent slashes is counted as a single slash. This controls how file names found in the patch file are treated, in case you keep your files in a different directory than the person who sent out the patch. For example, supposing the file name in the patch file was </p>
<dl>
<dt>
<dd> <code>/u/howard/src/blurfl/blurfl.c</code></dl>
<p> setting <code>-p0</code> gives the entire file name unmodified, <code>-p1</code> gives </p>
<dl>
<dt>
<dd> <code>u/howard/src/blurfl/blurfl.c</code></dl>
<p> without the leading slash, <code>-p4</code> gives </p>
<dl>
<dt>
<dd> <code>blurfl/blurfl.c</code></dl>
<p> and not specifying <code>-p</code> at all just gives you <code>blurfl.c</code>. Whatever you end up with is looked for either in the current directory, or the directory specified by the <code>-d</code> option.</p>
<dt><code>&#8211;posix</code></p>
<dd> Conform more strictly to the <font SIZE="-1">POSIX</font> standard, as follows.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code> &bull;</code></p>
<dd> Take the first existing file from the list (old, new, index) when intuiting file names from diff headers.</p>
<dt><code> &bull;</code></p>
<dd> Do not remove files that are empty after patching.</p>
<dt><code> &bull;</code></p>
<dd> Do not ask whether to get files from <font SIZE="-1">RCS</font>, ClearCase, Perforce, or <font SIZE="-1">SCCS</font>.</p>
<dt><code> &bull;</code></p>
<dd> Require that all options precede the files in the command line.</p>
<dt><code> &bull;</code></p>
<dd> Do not backup files when there is a mismatch.</dl>
</dl>
<dt><code>&#8211;quoting-style=</code><i>word</i></p>
<dd> Use style <i>word</i> to quote output names. The <i>word</i> should be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>literal</code></p>
<dd> Output names as-is.</p>
<dt><code>shell</code></p>
<dd> Quote names for the shell if they contain shell metacharacters or would cause ambiguous output.</p>
<dt><code>shell-always</code></p>
<dd> Quote names for the shell, even if they would normally not require quoting.</p>
<dt><code>c</code></p>
<dd> Quote names as for a C language string.</p>
<dt><code>escape</code></p>
<dd> Quote as with <code>c</code> except omit the surrounding double-quote characters.</dl>
<p> You can specify the default value of the <code>&#8211;quoting-style</code> option with the environment variable <code>QUOTING_STYLE</code>. If that environment variable is not set, the default value is <code>shell</code>.</dl>
<dt><code>-r</code> <i>rejectfile</i> or <code>&#8211;reject-file=</code><i>rejectfile</i></p>
<dd> Put rejects into <i>rejectfile</i> instead of the default <code>.rej</code> file. When <i>rejectfile</i> is <code>&#8211;</code>, discard rejects.</p>
<dt><code>-R</code> or <code>&#8211;reverse</code></p>
<dd> Assume that this patch was created with the old and new files swapped. (Yes, I&#8217;m afraid that does happen occasionally, human nature being what it is.) <code>patch</code> attempts to swap each hunk around before applying it. Rejects come out in the swapped format. The <code>-R</code> option does not work with <code>ed</code> diff scripts because there is too little information to reconstruct the reverse operation. </p>
<p> If the first hunk of a patch fails, <code>patch</code> reverses the hunk to see if it can be applied that way. If it can, you are asked if you want to have the <code>-R</code> option set. If it can&#8217;t, the patch continues to be applied normally. (Note: this method cannot detect a reversed patch if it is a normal diff and if the first command is an append (i.e. it should have been a delete) since appends always succeed, due to the fact that a null context matches anywhere. Luckily, most patches add or change lines rather than delete them, so most reversed normal diffs begin with a delete, which fails, triggering the heuristic.)</p>
<dt><code>&#8211;read-only=</code><i>behavior</i></p>
<dd> Behave as requested when trying to modify a read-only file: <code>ignore</code> the potential problem, <code>warn</code> about it (the default), or <code>fail</code>.</p>
<dt><code>&#8211;reject-format=</code><i>format</i></p>
<dd> Produce reject files in the specified <i>format</i> (either <code>context</code> or <code>unified</code>). Without this option, rejected hunks come out in unified diff format if the input patch was of that format, otherwise in ordinary context diff form.</p>
<dt><code>-s</code> or <code>&#8211;silent</code> or <code>&#8211;quiet</code></p>
<dd> Work silently, unless an error occurs.</p>
<dt><code>&#8211;follow-symlinks</code></p>
<dd> When looking for input files, follow symbolic links. Replaces the symbolic links, instead of modifying the files the symbolic links point to. Git-style patches to symbolic links will no longer apply. This option exists for backwards compatibility with previous versions of patch; its use is discouraged.</p>
<dt><code>-t</code> or <code>&#8211;batch</code></p>
<dd> Suppress questions like <code>-f</code>, but make some different assumptions: skip patches whose headers do not contain file names (the same as <code>-f</code>); skip patches for which the file has the wrong version for the <code>Prereq:</code> line in the patch; and assume that patches are reversed if they look like they are.</p>
<dt><code>-T</code> or <code>&#8211;set-time</code></p>
<dd> Set the modification and access times of patched files from time stamps given in context diff headers. Unless specified in the time stamps, assume that the context diff headers use local time. </p>
<p> Use of this option with time stamps that do not include time zones is not recommended, because patches using local time cannot easily be used by people in other time zones, and because local time stamps are ambiguous when local clocks move backwards during daylight-saving time adjustments. Make sure that time stamps include time zones, or generate patches with <font SIZE="-1">UTC</font> and use the <code>-Z</code> or <code>&#8211;set-utc</code> option instead.</p>
<dt><code>-u</code> or <code>&#8211;unified</code></p>
<dd> Interpret the patch file as a unified context diff.</p>
<dt><code>-v</code> or <code>&#8211;version</code></p>
<dd> Print out <code>patch</code>&#8216;s revision header and patch level, and exit.</p>
<dt><code>-V</code> <i>method</i> or <code>&#8211;version-control=</code><i>method</i></p>
<dd> Use <i>method</i> to determine backup file names. The method can also be given by the <code>PATCH_VERSION_CONTROL</code> (or, if that&#8217;s not set, the <code>VERSION_CONTROL</code>) environment variable, which is overridden by this option. The method does not affect whether backup files are made; it affects only the names of any backup files that are made. </p>
<p> The value of <i>method</i> is like the <font SIZE="-1">GNU</font> Emacs `version-control&#8217; variable; <code>patch</code> also recognizes synonyms that are more descriptive. The valid values for <i>method</i> are (unique abbreviations are accepted):</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>existing</code> or <code>nil</code></p>
<dd> Make numbered backups of files that already have them, otherwise simple backups. This is the default.</p>
<dt><code>numbered</code> or <code>t</code></p>
<dd> Make numbered backups. The numbered backup file name for <i>F</i> is <i>F</i><code>.~</code><i>N</i><code>~</code> where <i>N</i> is the version number.</p>
<dt><code>simple</code> or <code>never</code></p>
<dd> Make simple backups. The <code>-B</code> or <code>&#8211;prefix</code>, <code>-Y</code> or <code>&#8211;basename-prefix</code>, and <code>-z</code> or <code>&#8211;suffix</code> options specify the simple backup file name. If none of these options are given, then a simple backup suffix is used; it is the value of the <code>SIMPLE_BACKUP_SUFFIX</code> environment variable if set, and is <code>.orig</code> otherwise.</dl>
<p> With numbered or simple backups, if the backup file name is too long, the backup suffix <code>~</code> is used instead; if even appending <code>~</code> would make the name too long, then <code>~</code> replaces the last character of the file name.</dl>
<dt><code>&#8211;verbose</code></p>
<dd> Output extra information about the work being done.</p>
<dt><code>-x</code> <i>num</i> or <code>&#8211;debug=</code><i>num</i></p>
<dd> Set internal debugging flags of interest only to <code>patch</code> patchers.</p>
<dt><code>-Y</code> <i>pref</i> or <code>&#8211;basename-prefix=</code><i>pref</i></p>
<dd> Use the <code>simple</code> method to determine backup file names (see the <code>-V </code><i>method</i> or <code>&#8211;version-control </code><i>method</i> option), and prefix <i>pref</i> to the basename of a file name when generating its backup file name. For example, with <code>-Y .del/</code> the simple backup file name for <code>src/patch/util.c</code> is <code>src/patch/.del/util.c</code>.</p>
<dt><code>-z</code> <i>suffix</i> or <code>&#8211;suffix=</code><i>suffix</i></p>
<dd> Use the <code>simple</code> method to determine backup file names (see the <code>-V </code><i>method</i> or <code>&#8211;version-control </code><i>method</i> option), and use <i>suffix</i> as the suffix. For example, with <code>-z &#8211;</code> the backup file name for <code>src/patch/util.c</code> is <code>src/patch/util.c-</code>.</p>
<dt><code>-Z</code> or <code>&#8211;set-utc</code></p>
<dd> Set the modification and access times of patched files from time stamps given in context diff headers. Unless specified in the time stamps, assume that the context diff headers use Coordinated Universal Time (<font SIZE="-1">UTC</font>, often known as <font SIZE="-1">GMT</font>). Also see the <code>-T</code> or <code>&#8211;set-time</code> option. </p>
<p> The <code>-Z</code> or <code>&#8211;set-utc</code> and <code>-T</code> or <code>&#8211;set-time</code> options normally refrain from setting a file&#8217;s time if the file&#8217;s original time does not match the time given in the patch header, or if its contents do not match the patch exactly. However, if the <code>-f</code> or <code>&#8211;force</code> option is given, the file time is set regardless. </p>
<p> Due to the limitations of <code>diff</code> output format, these options cannot update the times of files whose contents have not changed. Also, if you use these options, you should remove (e.g. with <code>make clean</code>) all files that depend on the patched files, so that later invocations of <code>make</code> do not get confused by the patched files&#8217; times.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>PATCH_GET</code></p>
<dd> This specifies whether <code>patch</code> gets missing or read-only files from <font SIZE="-1">RCS</font>, ClearCase, Perforce, or <font SIZE="-1">SCCS</font> by default; see the <code>-g</code> or <code>&#8211;get</code> option.</p>
<dt><code>POSIXLY_CORRECT</code></p>
<dd> If set, <code>patch</code> conforms more strictly to the <font SIZE="-1">POSIX</font> standard by default: see the <code>&#8211;posix</code> option.</p>
<dt><code>QUOTING_STYLE</code></p>
<dd> Default value of the <code>&#8211;quoting-style</code> option.</p>
<dt><code>SIMPLE_BACKUP_SUFFIX</code></p>
<dd> Extension to use for simple backup file names instead of <code>.orig</code>.</p>
<dt><code>TMPDIR</code>, <code>TMP</code>, <code>TEMP</code></p>
<dd> Directory to put temporary files in; <code>patch</code> uses the first environment variable in this list that is set. If none are set, the default is system-dependent; it is normally <code>/tmp</code> on Unix hosts.</p>
<dt><code>VERSION_CONTROL</code> or <code>PATCH_VERSION_CONTROL</code></p>
<dd> Selects version control style; see the <code>-v</code> or <code>&#8211;version-control</code> option.</dl>
<h2>FILES</h2>
<dl>
<dt><i>$TMPDIR</i><code>/p*</code></p>
<dd> temporary files</p>
<dt><code>/dev/tty</code></p>
<dd> controlling terminal; used to get answers to questions asked of the user</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1), <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1), <code><a href="/docs/linux/man/1-merge/">merge</a></code>(1). </p>
<p> Marshall T. Rose and Einar A. Stefferud, Proposed Standard for Message Encapsulation, Internet RFC 934 &lt;URL:<a href="ftp://ftp.isi.edu/in-notes/rfc934.txt">ftp://ftp.isi.edu/in-notes/rfc934.txt</a>&gt; (1985-01).</p>
<h2>NOTES FOR PATCH SENDERS</h2>
<p> There are several things you should bear in mind if you are going to be sending out patches. </p>
<p> Create your patch systematically. A good method is the command <code>diff -Naur&nbsp;</code><i>old new</i> where <i>old</i> and <i>new</i> identify the old and new directories. The names <i>old</i> and <i>new</i> should not contain any slashes. The <code>diff</code> command&#8217;s headers should have dates and times in Universal Time using traditional Unix format, so that patch recipients can use the <code>-Z</code> or <code>&#8211;set-utc</code> option. Here is an example command, using Bourne shell syntax: </p>
<dl>
<dt>
<dd> <code>LC_ALL=C TZ=UTC0 diff -Naur gcc-2.7 gcc-2.8</code></dl>
<p> Tell your recipients how to apply the patch by telling them which directory to <code>cd</code> to, and which <code>patch</code> options to use. The option string <code>-Np1</code> is recommended. Test your procedure by pretending to be a recipient and applying your patch to a copy of the original files. </p>
<p> You can save people a lot of grief by keeping a <code>patchlevel.h</code> file which is patched to increment the patch level as the first diff in the patch file you send out. If you put a <code>Prereq:</code> line in with the patch, it won&#8217;t let them apply patches out of order without some warning. </p>
<p> You can create a file by sending out a diff that compares <code>/dev/null</code> or an empty file dated the Epoch (1970-01-01 00:00:00 <font SIZE="-1">UTC</font>) to the file you want to create. This only works if the file you want to create doesn&#8217;t exist already in the target directory. Conversely, you can remove a file by sending out a context diff that compares the file to be deleted with an empty file dated the Epoch. The file will be removed unless <code>patch</code> is conforming to <font SIZE="-1">POSIX</font> and the <code>-E</code> or <code>&#8211;remove-empty-files</code> option is not given. An easy way to generate patches that create and remove files is to use <font SIZE="-1">GNU</font> <code>diff</code>&#8216;s <code>-N</code> or <code>&#8211;new-file</code> option. </p>
<p> If the recipient is supposed to use the <code>-p</code><i>N</i> option, do not send output that looks like this: </p>
<dl>
<dt>
<dd> diff -Naur v2.0.29/prog/README prog/README<br />
 &#8212; v2.0.29/prog/README Mon Mar 10 15:13:12 1997<br />
 +++ prog/README Mon Mar 17 14:58:22 1997</dl>
<p> because the two file names have different numbers of slashes, and different versions of <code>patch</code> interpret the file names differently. To avoid confusion, send output that looks like this instead: </p>
<dl>
<dt>
<dd> diff -Naur v2.0.29/prog/README v2.0.30/prog/README<br />
 &#8212; v2.0.29/prog/README Mon Mar 10 15:13:12 1997<br />
 +++ v2.0.30/prog/README Mon Mar 17 14:58:22 1997</dl>
<p> Avoid sending patches that compare backup file names like <code>README.orig</code>, since this might confuse <code>patch</code> into patching a backup file instead of the real file. Instead, send patches that compare the same base file names in different directories, e.g. <code>old/README</code> and <code>new/README</code>. </p>
<p> Take care not to send out reversed patches, since it makes people wonder whether they already applied the patch. </p>
<p> Try not to have your patch modify derived files (e.g. the file <code>configure</code> where there is a line <code>configure: configure.in</code> in your makefile), since the recipient should be able to regenerate the derived files anyway. If you must send diffs of derived files, generate the diffs using <font SIZE="-1">UTC</font>, have the recipients apply the patch with the <code>-Z</code> or <code>&#8211;set-utc</code> option, and have them remove any unpatched files that depend on patched files (e.g. with <code>make clean</code>). </p>
<p> While you may be able to get away with putting 582 diff listings into one file, it may be wiser to group related patches into separate files in case something goes haywire.</p>
<h2>DIAGNOSTICS</h2>
<p> Diagnostics generally indicate that <code>patch</code> couldn&#8217;t parse your patch file. </p>
<p> If the <code>&#8211;verbose</code> option is given, the message <code>Hmm&#8230;</code> indicates that there is unprocessed text in the patch file and that <code>patch</code> is attempting to intuit whether there is a patch in that text and, if so, what kind of patch it is. </p>
<p> <code>patch</code>&#8216;s exit status is 0 if all hunks are applied successfully, 1 if some hunks cannot be applied or there were merge conflicts, and 2 if there is more serious trouble. When applying a set of patches in a loop it behooves you to check this exit status so you don&#8217;t apply a later patch to a partially patched file.</p>
<h2>CAVEATS</h2>
<p> Context diffs cannot reliably represent the creation or deletion of empty files, empty directories, or special files such as symbolic links. Nor can they represent changes to file metadata like ownership, permissions, or whether one file is a hard link to another. If changes like these are also required, separate instructions (e.g. a shell script) to accomplish them should accompany the patch. </p>
<p> <code>patch</code> cannot tell if the line numbers are off in an <code>ed</code> script, and can detect bad line numbers in a normal diff only when it finds a change or deletion. A context diff using fuzz factor 3 may have the same problem. You should probably do a context diff in these cases to see if the changes made sense. Of course, compiling without errors is a pretty good indication that the patch worked, but not always. </p>
<p> <code>patch</code> usually produces the correct results, even when it has to do a lot of guessing. However, the results are guaranteed to be correct only when the patch is applied to exactly the same version of the file that the patch was generated from.</p>
<h2>COMPATIBILITY ISSUES</h2>
<p> The <font SIZE="-1">POSIX</font> standard specifies behavior that differs from <code>patch</code>&#8216;s traditional behavior. You should be aware of these differences if you must interoperate with <code>patch</code> versions 2.1 and earlier, which do not conform to <font SIZE="-1">POSIX</font>.</p>
<dl>
<dt><code> &bull;</code></p>
<dd> In traditional <code>patch</code>, the <code>-p</code> option&#8217;s operand was optional, and a bare <code>-p</code> was equivalent to <code>-p0.</code> The <code>-p</code> option now requires an operand, and <code>-p 0</code> is now equivalent to <code>-p0</code>. For maximum compatibility, use options like <code>-p0</code> and <code>-p1</code>. </p>
<p> Also, traditional <code>patch</code> simply counted slashes when stripping path prefixes; <code>patch</code> now counts pathname components. That is, a sequence of one or more adjacent slashes now counts as a single slash. For maximum portability, avoid sending patches containing <code>//</code> in file names.</p>
<dt><code> &bull;</code></p>
<dd> In traditional <code>patch</code>, backups were enabled by default. This behavior is now enabled with the <code>-b</code> or <code>&#8211;backup</code> option. </p>
<p> Conversely, in <font SIZE="-1">POSIX</font> <code>patch</code>, backups are never made, even when there is a mismatch. In <font SIZE="-1">GNU</font> <code>patch</code>, this behavior is enabled with the <code>&#8211;no-backup-if-mismatch</code> option, or by conforming to <font SIZE="-1">POSIX</font> with the <code>&#8211;posix</code> option or by setting the <code>POSIXLY_CORRECT</code> environment variable. </p>
<p> The <code>-b</code><i>&nbsp;suffix</i> option of traditional <code>patch</code> is equivalent to the <code>-b -z</code><i>&nbsp;suffix</i> options of <font SIZE="-1">GNU</font> <code>patch</code>.</p>
<dt><code> &bull;</code></p>
<dd> Traditional <code>patch</code> used a complicated (and incompletely documented) method to intuit the name of the file to be patched from the patch header. This method did not conform to <font SIZE="-1">POSIX</font>, and had a few gotchas. Now <code>patch</code> uses a different, equally complicated (but better documented) method that is optionally <font SIZE="-1">POSIX</font>-conforming; we hope it has fewer gotchas. The two methods are compatible if the file names in the context diff header and the <code>Index:</code> line are all identical after prefix-stripping. Your patch is normally compatible if each header&#8217;s file names all contain the same number of slashes.</p>
<dt><code> &bull;</code></p>
<dd> When traditional <code>patch</code> asked the user a question, it sent the question to standard error and looked for an answer from the first file in the following list that was a terminal: standard error, standard output, <code>/dev/tty</code>, and standard input. Now <code>patch</code> sends questions to standard output and gets answers from <code>/dev/tty</code>. Defaults for some answers have been changed so that <code>patch</code> never goes into an infinite loop when using default answers.</p>
<dt><code> &bull;</code></p>
<dd> Traditional <code>patch</code> exited with a status value that counted the number of bad hunks, or with status 1 if there was real trouble. Now <code>patch</code> exits with status 1 if some hunks failed, or with 2 if there was real trouble.</p>
<dt><code> &bull;</code></p>
<dd> Limit yourself to the following options when sending instructions meant to be executed by anyone running <font SIZE="-1">GNU</font> <code>patch</code>, traditional <code>patch</code>, or a <code>patch</code> that conforms to <font SIZE="-1">POSIX</font>. Spaces are significant in the following list, and operands are required. </p>
<pre>
<code>-c</code>
<code>-d</code><i> dir</i>
<code>-D</code><i> define</i>
<code>-e</code>
<code>-l</code>
<code>-n</code>
<code>-N</code>
<code>-o</code><i> outfile</i>
<code>-p</code><i>num</i>
<code>-R</code>
<code>-r</code><i> rejectfile</i>
</pre>
</dl>
<h2>BUGS</h2>
<p> Please report bugs via email to <code>&lt;bug-patch [at] gnu.org&gt;</code>. </p>
<p> If code has been duplicated (for instance with <code>#ifdef OLDCODE</code> &#8230; <code>#else &#8230; #endif</code>), <code>patch</code> is incapable of patching both versions, and, if it works at all, will likely patch the wrong one, and tell you that it succeeded to boot. </p>
<p> If you apply a patch you&#8217;ve already applied, <code>patch</code> thinks it is a reversed patch, and offers to un-apply the patch. This could be construed as a feature. </p>
<p> Computing how to merge a hunk is significantly harder than using the standard fuzzy algorithm. Bigger hunks, more context, a bigger offset from the original location, and a worse match all slow the algorithm down.</p>
<h2>COPYING</h2>
<p> Copyright (C) 1984, 1985, 1986, 1988 Larry Wall.<br />
 Copyright (C) 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2009 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions, except that this permission notice may be included in translations approved by the copyright holders instead of in the original English.</p>
<h2>AUTHORS</h2>
<p> Larry Wall wrote the original version of <code>patch</code>. Paul Eggert removed <code>patch</code>&#8216;s arbitrary limits; added support for binary files, setting file times, and deleting files; and made it conform better to <font SIZE="-1">POSIX</font>. Other contributors include Wayne Davison, who added unidiff support, and David MacKenzie, who added configuration and backup support. Andreas Gr&uuml;nbacher added support for merging. </p>
<h2>Index</h2>
