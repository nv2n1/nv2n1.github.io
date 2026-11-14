---
title: "sloccount(1)"
name: "sloccount"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sloccount/"
description: "sloccount – count source lines of code (SLOC)"
---

<h2>NAME</h2>
<p> sloccount &#8211; count source lines of code (SLOC)</p>
<h2>SYNOPSIS</h2>
<p> <code>sloccount</code> [<code>&#8211;version</code>] [<code>&#8211;cached</code>] [<code>&#8211;append</code>] [ <code>&#8211;datadir</code> <i>directory</i> ] [<code>&#8211;follow</code>] [<code>&#8211;duplicates</code>] [<code>&#8211;crossdups</code>] [<code>&#8211;autogen</code>] [<code>&#8211;multiproject</code>] [<code>&#8211;filecount</code>] [<code>&#8211;wide</code>] [<code>&#8211;details</code>] [ <code>&#8211;effort</code> <i>F</i> <i>E</i> ] [ <code>&#8211;schedule</code> <i>F</i> <i>E</i> ] [ <code>&#8211;personcost</code> <i>cost</i> ] [ <code>&#8211;overhead</code> <i>overhead</i> ] [ <code>&#8211;addlang</code> <i>language</i> ] [ <code>&#8211;addlangall</code> ] [<code>&#8212;</code>] <i>directories</i></p>
<h2>DESCRIPTION</h2>
<p> sloccount counts the physical source lines of code (SLOC) contained in descendants of the specified set of directories. It automatically determines which files are source code files, and it automatically determines the computer language used in each file. By default it summarizes the SLOC results and presents various estimates (such as effort and cost to develop), but its output can be controlled by various options. </p>
<p> If you give sloccount a list of two or more directories, the counts will be broken up according to that list. There is one important limitation: the basenames of the directories given as parameters must be different, because those names are used to group summary information. Thus, you can&#8217;t run &quot;sloccount /usr/src/hello /usr/local/src/hello&quot;. This limitation only applies to parameters of sloccount &#8211; subdirectories descended from the top directories can have the same basename. </p>
<p> If you give sloccount only a single directory, sloccount tries to automatically find a reasonable breakdown for purposes of reporting (so it&#8217;ll produce a useful report). In this case, if the directory has at least two subdirectories, then those subdirectories will be used as the breakdown. If the single directory contains files as well as directories (or if you give sloccount some files as parameters), those files will be assigned to the directory &quot;top_dir&quot; so you can tell them apart from other contents. Finally, if there&#8217;s a subdirectory named &quot;src&quot;, then that subdirectory is again broken down, with all the further subdirectories prefixed with &quot;src_&quot;. Thus, if directory &quot;X&quot; has a subdirectory &quot;src&quot;, which contains subdirectory &quot;modules&quot;, sloccount will report a separate count for &quot;src_modules&quot;. </p>
<p> sloccount normally considers all descendants of these directories, though unless told otherwise it ignores symbolic links. </p>
<p> sloccount is the usual front-end of the package of tools named &quot;SLOCCount&quot;. Note that the name of the entire package has capital letters, while the name of this front-end program does not. </p>
<p> sloccount will normally report estimates of schedule time, effort, and cost, and for single projects it also estimates the average number of active developers. These are merely estimates, not etched in stone; you can modify the parameters used to improve the estimates. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Report the version number of SLOCCount and immediately exit. This option can&#8217;t be usefully combined with any other option. </p>
<dt><code>&#8211;cached</code></p>
<dd> Do not recalculate; instead, use cached results from a previous execution. Without the &#8211;cached or &#8211;append option, sloccount automatically removes the data directory and recreates it. </p>
<dt><code>&#8211;append</code></p>
<dd> Do not remove previous calculations from the data directory; instead, add the analysis to the current contents of the data directory. </p>
<dt><code>&#8211;datadir</code><i> directory</i></p>
<dd> Store or use cached data in the given data directory; default value is &quot;~/.slocdata&quot;. </p>
<dt><code>&#8211;follow</code></p>
<dd> Follow symbolic links. </p>
<dt><code>&#8211;duplicates</code></p>
<dd> Count all duplicates. Normally, if files have equal content (as determined using MD5 hash values), only one is counted. </p>
<dt><code>&#8211;crossdups</code></p>
<dd> Count duplicates if they occur in different portions of the breakdown. Thus, if the top directory contains many different projects, and you want the duplicates in different projects to count in each project, choose this option. </p>
<dt><code>&#8211;autogen</code></p>
<dd> Count source code files that appear to be automatically generated. Normally these are excluded. </p>
<dt><code>&#8211;multiproject</code></p>
<dd> The different directories represent different projects; otherwise, it&#8217;s assumed that all of the source code belongs to a single project. This doesn&#8217;t change the total number of files or SLOC values, but it does affect the effort and schedule estimates. Given this option, effort is computed separately for each project (and then summed), and the schedule is the estimated schedule of the largest project. </p>
<dt><code>&#8211;filecount</code></p>
<dd> Display counts of files instead of SLOC. </p>
<dt><code>&#8211;wide</code></p>
<dd> Display in the &quot;wide&quot; (tab-separated) format. </p>
<dt><code>&#8211;details</code></p>
<dd> Display details, that is, results for every source code file. </p>
<dt><code>&#8211;effort</code><i> F E</i></p>
<dd> Change the factor and exponent for the effort model. Effort (in person-months) is computed as F*(SLOC/1000)^E. </p>
<dt><code>&#8211;schedule</code><i> F E</i></p>
<dd> Change the factor and exponent for the schedule model. Schedule (in months) is computed as F*(effort)^E. </p>
<dt><code>&#8211;personcost</code><i> cost</i></p>
<dd> Change the average annual salary to <i>cost</i>. </p>
<dt><code>&#8211;overhead</code><i> overhead</i></p>
<dd> Change the overhead value to <i>overhead</i>. Estimated cost is computed as effort * personcost * overhead. </p>
<dt><code>&#8211;addlang</code><i> language</i></p>
<dd> Add a language not considered by default to be a &#8220;language&#8221; to be reported. Currently the only legal values for language are &quot;makefile&quot;, &quot;sql&quot;, and &quot;html&quot;. These files are not normally included in the SLOC counts, although their SLOCs are internally calculated and they are shown in the file counts. If you want to include more than one such language, do it by passing &#8211;addlang more than once, e.g., &#8211;addlang makefile &#8211;addlang sql. </p>
<dt><code>&#8211;addlangall</code></p>
<dd> Add all languages not normally included in final reports. </p>
</dl>
<h2>NOTES</h2>
<p> As with many other programs using Unix-like options, directories whose names begin with a dash (&#8220;-&#8221;) can be misinterpreted as options. If the directories to be analyzed might begin with a dash, use the double-dash (&#8220;- -&#8221;) to indicate the end of the option list before listing the directories. </p>
<h2>BUGS</h2>
<p> Filenames with embedded newlines (in the directories or their descendants) won&#8217;t be handled correctly; they will be interpreted as separate filenames where the newlines are inserted. An attacker could prevent sloccount from working by creating filenames of the form /normal/directory &#8230; NEWLINE/dev/zero. Such filenames are exceedingly rare in source code because they&#8217;re a pain to work with using other tools, too. Future versions of sloccount may internally use NUL-separated filenames (like GNU find&#8217;s -print0 command) to fix this. </p>
<p> There are many more languages not yet handled by SLOCCount. </p>
<p> SLOCCount only reports physical source lines of code. It would be very useful if it could also report logical lines of code, and perhaps other common metrics such as McCabe&#8217;s complexity measures and complexity density (complexity/SLOC for each function or procedure). </p>
<h2>SEE ALSO</h2>
<p> See the SLOCCount website at <a rel="nofollow" href="http://www.dwheeler.com/sloccount.">http://www.dwheeler.com/sloccount.</a> Note that more detailed documentation is available both on the website and with the SLOCCount package. </p>
<h2>AUTHOR</h2>
<p> David A. Wheeler (dwheeler [at] dwheeler.com). </p>
<h2>Index</h2>
