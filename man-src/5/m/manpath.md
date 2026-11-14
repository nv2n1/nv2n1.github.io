---
title: "manpath(5)"
name: "manpath"
section: "5"
letter: "m"
url: "/docs/linux/man/5-manpath/"
description: "manpath – format of the /etc/manpath.config file"
---

<p>manpath &#8211; format of the /etc/manpath.config file</p>
<h2>Description</h2>
<p>The manpath configuration file is used by the manual page utilities to assess users&#8217; manpaths at run time, to indicate which manual page hierarchies (manpaths) are to be treated as system hierarchies and to assign them directories to be used for storing cat files. </p>
<p> If the environment variable $<code>MANPATH</code> is already set, the information contained within /etc/manpath.config will not override it.</p>
<h2>Search Path</h2>
<p>By default, man-db examines the user&#8217;s $<code>PATH</code>. For each <i>path_element</i> found there, it adds <i>manpath_element</i> to the search path. </p>
<p> If there is no <code>MANPATH_MAP</code> line in the configuration file for a given <i>path_element</i>, then it adds all of <i>path_element/../man</i>, <i>path_element/man</i>, <i>path_element/../share/man</i>, and <i>path_element/share/man</i> that exist as directories to the search path. </p>
<p> It then adds any <code>MANDATORY_MANPATH</code> entries from the configuration file to the search path. </p>
<p> Finally, if the <code>&#8211;systems</code> option is used or the $<code>SYSTEM</code> environment variable is set, then that should consist of a sequence of operating system names separated by commas or colons. This acts as a template, expanding the search path once more to allow access to other operating systems&#8217; manual pages: for each system name, man-db looks for that name as a subdirectory of each entry in the search path, and adds it to the final search path if it exists. A system name of <code>man</code> inserts the normal search path without subdirectories. For example, if the search path would otherwise have been <i>/usr/share/man:/usr/local/man</i>, and $<code>SYSTEM</code> is set to <i>newOS:man</i>, then the final search path will be <i>/usr/share/man/newOS:/usr/share/man:/usr/local/man/newOS:/usr/local/man</i>. </p>
<p> The $<code>MANPATH</code> environment variable overrides man-db&#8217;s default manual page search paths. Most users should not need to set it. Its syntax is similar to the $<code>PATH</code> environment variable: it consists of a sequence of directory names separated by colons. It overrides the default search path described above. </p>
<p> If the value of $<code>MANPATH</code> starts with a colon, then the default search path is added at its start. If the value of $<code>MANPATH</code> ends with a colon, then the default search path is added at its end. If the value of $<code>MANPATH</code> contains a double colon (<code>::</code>), then the default search path is inserted in the middle of the value, between the two colons.</p>
<h2>Format</h2>
<p>The following field types are currently recognised:</p>
<dl>
<dt><code>#</code><i>&nbsp;comment</i></p>
<dd>Blank lines or those beginning with a <code>#</code> will be treated as comments and ignored.</p>
<dt><code>MANDATORY_MANPATH</code><i>&nbsp;manpath_element</i></p>
<dd>Lines of this form indicate manpaths that every automatically generated $<code>MANPATH</code> should contain. This will typically include <i>/usr/man</i>.</p>
<dt><code>MANPATH_MAP</code><i>&nbsp;path_element manpath_element</i></p>
<dd>Lines of this form set up $<code>PATH</code> to $<code>MANPATH</code> mappings. For each <i>path_element</i> found in the user&#8217;s $<code>PATH</code>, <i>manpath_element</i> will be added to the $<code>MANPATH</code>.</p>
<dt><code>MANDB_MAP </code><i>manpath_element </i>[ <i>catpath_element</i> ]</p>
<dd>Lines of this form indicate which manpaths are to be treated as system manpaths, and optionally where their cat files should be stored. This field type is particularly important if <code>man</code> is a setuid program, as (when in the system configuration file /etc/manpath.config rather than the per-user configuration file .manpath) it indicates which manual page hierarchies to access as the setuid user and which as the invoking user. </p>
<p> The system manual page hierarchies are usually those stored under <i>/usr</i> such as <i>/usr/man</i>, <i>/usr/local/man</i> and <i>/usr/X11R6/man</i>. </p>
<p> If cat pages from a particular <i>manpath_element</i> are not to be stored or are to be stored in the traditional location, <i>catpath_element</i> may be omitted. </p>
<p> Traditional cat placement would be impossible for read only mounted manual page hierarchies and because of this it is possible to specify any valid directory hierarchy for their storage. To observe the <code>Linux FSSTND</code> the keyword <code>FSSTND</code> can be used in place of an actual directory. </p>
<p> Unfortunately, it is necessary to specify <code>all</code> system man tree paths, including alternate operating system paths such as <i>/usr/man/sun</i> and any <code>NLS locale</code> paths such as <i>/usr/man/de_DE.88591</i>. </p>
<p> As the information is parsed line by line in the order written, it is necessary for any manpath that is a sub-hierarchy of another hierarchy to be listed first, otherwise an incorrect match will be made. An example is that <i>/usr/man/de_DE.88591</i> must come before <i>/usr/man</i>.</p>
<dt><code>DEFINE</code><i>&nbsp;key value</i></p>
<dd>Lines of this form define miscellaneous configuration variables; see the default configuration file for those variables used by the manual pager utilities. They include default paths to various programs (such as <i>grep</i> and <i>tbl</i>), and default sets of arguments to those programs.</p>
<dt><code>SECTION</code> <i>section</i> &#8230;</p>
<dd>
<dl>
<dd>Lines of this form define the order in which manual sections should be searched. If there are no <code>SECTION</code> directives in the configuration file, the default is: </p>
<dl>
<dd>
<pre>SECTION 1 n l 8 3 0 2 5 4 9 6 7</pre>
</dl>
<p> If multiple <code>SECTION</code> directives are given, their section lists will be concatenated. </p>
<p> If a particular extension is not in this list (say, 1mh) it will be displayed with the rest of the section it belongs to. The effect of this is that you only need to explicitly list extensions if you want to force a particular order. Sections with extensions should usually be adjacent to their main section (e.g. &quot;1 1mh 8 &#8230;&quot;). </p>
<p> <code>SECTIONS</code> is accepted as an alternative name for this directive.</dl>
<dt><code>MINCATWIDTH</code><i>&nbsp;width</i></p>
<dd>If the terminal width is less than <i>width</i>, cat pages will not be created (if missing) or displayed. The default is 80.</p>
<dt><code>MAXCATWIDTH</code><i>&nbsp;width</i></p>
<dd>If the terminal width is greater than <i>width</i>, cat pages will not be created (if missing) or displayed. The default is 80.</p>
<dt><code>CATWIDTH</code><i>&nbsp;width</i></p>
<dd>If <i>width</i> is non-zero, cat pages will always be formatted for a terminal of the given width, regardless of the width of the terminal actually being used. This should generally be within the range set by <code>MINCATWIDTH</code> and <code>MAXCATWIDTH</code>.</p>
<dt><code>NOCACHE</code></p>
<dd>This flag prevents <code><a href="/docs/linux/man/1-man/">man</a></code>(1) from creating cat pages automatically.</dl>
<h2>Bugs</h2>
<p>Unless the rules above are followed and observed precisely, the manual pager utilities will not function as desired. The rules are overly complicated. <a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
