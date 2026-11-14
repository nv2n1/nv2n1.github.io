---
title: "global(1)"
name: "global"
section: "1"
letter: "g"
url: "/docs/linux/man/1-global/"
description: "global – print the locations of specified object."
---

<h2>NAME</h2>
<p> global &#8211; print the locations of specified object.</p>
<h2>SYNOPSIS</h2>
<p> <code>global</code> [-aGilnqrstTvx][-e] <i>pattern</i><br />
 <code>global</code> -c[qrsv] <i>prefix</i><br />
 <code>global</code> -f[anqrstvx] <i>files</i><br />
 <code>global</code> -g[aGilnoOqtvx][-e] <i>pattern</i><br />
 <code>global</code> -I[ailnqtvx][-e] <i>pattern</i><br />
 <code>global</code> -P[aGilnoOqtvx][-e] <i>pattern</i><br />
 <code>global</code> -p[qrv]<br />
 <code>global</code> -u[qv] </p>
<h2>DESCRIPTION</h2>
<p> <code>Global</code> find the locations of specified object in C, C++, Yacc, Java, PHP and Assembly source files. <code>Global</code> can treat a source tree, that is, a directory that has sub-directories and source files as a project. You can get the relative path of objects from anywhere within the project. <code>Global</code> can locate not only object definitions but also object references and other symbols. </p>
<p> In advance of using this command, you must execute <code><a href="/docs/linux/man/1-gtags/">gtags</a></code>(1) at the root directory of the project to make tag files. Then you can execute this command at anywhere in the project.</p>
<h2>COMMANDS</h2>
<p> The following commands are available:</p>
<dl>
<dt>&lt;no command&gt; <i>pattern</i></p>
<dd> Print object which match to the <i>pattern</i>. Extended regular expressions which are the same as those accepted by <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) are available.</p>
<dt><code>-c</code>, <code>&#8211;completion</code> [<i>prefix</i>]</p>
<dd> Print the candidates of object names which start with the specified <i>prefix</i>. <i>Prefix</i> is not specified, print all object names.</p>
<dt><code>-f</code>, <code>&#8211;file</code> <i>files</i></p>
<dd> Print all tags in the <i>files</i>. This option implies the -x option.</p>
<dt><code>-g</code>, <code>&#8211;grep</code> <i>pattern</i></p>
<dd> Print all lines which match to the <i>pattern</i>.</p>
<dt><code>&#8211;help</code></p>
<dd> Show help.</p>
<dt><code>-I</code>, <code>&#8211;idutils</code> <i>pattern</i></p>
<dd> Print all lines which match to the <i>pattern</i>. This function use <code><a href="/docs/linux/man/1-idutils/">idutils</a></code>(1) as a search engine. To use this command, you need to install <code><a href="/docs/linux/man/1-idutils/">idutils</a></code>(1) in your system and you must execute <code><a href="/docs/linux/man/1-gtags/">gtags</a></code>(1) with the <code>-I</code> option.</p>
<dt><code>-P</code>, <code>&#8211;path</code> [<i>pattern</i>]</p>
<dd> Print the paths which match to the <i>pattern</i>. If no pattern specified, print all paths in the project.</p>
<dt><code>-p</code>, <code>&#8211;print-dbpath</code></p>
<dd> Print the location of &#8216;GTAGS&#8217;.</p>
<dt><code>-u</code>, <code>&#8211;update</code></p>
<dd> Locate tag files and update them incrementally.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version number.</dl>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><code>-a</code>, <code>&#8211;absolute</code></p>
<dd> Print absolute path name. By default, print relative path name.</p>
<dt><code>&#8211;from-here</code> <i>context</i></p>
<dd> Decide tag type by the context. The <i>context</i> must be &#8216;lineno:path&#8217;. If this option is specified then the <code>-s</code> and <code>-r</code> are ignored. Regular expression is not allowed in the <i>pattern</i>. This option assumes use in conversational environments such as editors and IDEs.</p>
<dt><code>-e</code>, <code>&#8211;regexp</code> <i>pattern</i></p>
<dd> Use <i>pattern</i> as the pattern; useful to protect patterns beginning with &#8216;-&#8216;.</p>
<dt><code>-G</code>, <code>&#8211;basic-regexp</code></p>
<dd> Interpret <i>pattern</i> as a basic regular expression. The default is extended regular expression.</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> ignore case distinctions in pattern.</p>
<dt><code>-l</code>, <code>&#8211;local</code></p>
<dd> Print just objects which exist under the current directory.</p>
<dt><code>-n</code>, <code>&#8211;nofilter</code></p>
<dd> Suppress sort filter and path conversion filter.</p>
<dt><code>-O</code>, <code>&#8211;only-other</code></p>
<dd> Search pattern only in other than source files like &#8216;README&#8217;. This option is valid only with <code>-g</code> or <code>-P</code> command. This option override the <code>-o</code> option.</p>
<dt><code>-o</code>, <code>&#8211;other</code></p>
<dd> Search pattern in not only source files but also other files like &#8216;README&#8217;. This option is valid only with <code>-g</code> or <code>-P</code> command.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Quiet mode.</p>
<dt><code>-r</code>, <code>&#8211;reference</code>, <code>&#8211;rootdir</code></p>
<dd> Print the locations of object references. By default, print object definitions. With the <code>-p</code> option, print the root directory of source tree.</p>
<dt><code>&#8211;result</code> <i>format</i></p>
<dd> <i>format</i> may be &#8216;path&#8217;, `ctags&#8217;, `ctags-x&#8217;, `grep&#8217; or &#8216;cscope&#8217;. The <code>&#8211;result=ctags</code> and <code>&#8211;result=ctags-x</code> are equivalent to the <code>-t</code> and <code>-x</code> respectively. The <code>&#8211;result</code> option is given to priority more than the -t and -x option.</p>
<dt><code>-s</code>, <code>&#8211;symbol</code></p>
<dd> Print the locations of specified symbol other than definitions.</p>
<dt><code>-T</code>, <code>&#8211;through</code></p>
<dd> Go through all the tag files listed in <code>GTAGSLIBPATH</code>. By default, stop searching when tag is found. This option is ignored when either <code>-s</code>, <code>-r</code> or <code>-l</code> option is specified.</p>
<dt><code>-t</code>, <code>&#8211;tags</code></p>
<dd> Print with standard ctags format.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode.</p>
<dt><code>-x</code>, <code>&#8211;cxref</code></p>
<dd> In addition to the default output, produce the line number and the line contents.</dl>
<h2>EXAMPLES</h2>
<pre><code>
$ ls - F Makefile src / lib / $ gtags $ global main src / main.c $ global - x main main 10 src / main.c main(argc, argv)
{
    $ global - x '^[sg]et' set_num 20 lib / util.c set_num(values) get_num 30 lib / util.c get_num()
    {
        $ global - rx '^[sg]et' set_num 113 src / op.c set_num(32);
        set_num 225 src / opop.c if (set_num(0) &gt; 0)
        {
            get_num 90 src / op.c while (get_num() &gt; 0)
            {
                $ cd lib
                        $ global -
                    rx '^[sg]et' set_num 113../ src / op.c set_num(32);
                set_num 225../ src / opop.c if (set_num(0) &gt; 0)
                {
                    get_num 90../ src / op.c while (get_num() &gt; 0)
                    {
                        $ global strlen
                        $(cd / usr / src / sys; gtags)
                            $ export GTAGSLIBPATH = / usr / src / sys $ global strlen../../../ usr / src / sys / libkern / strlen.c $(cd / usr / src / lib; gtags) $ GTAGSLIBPATH = / usr / src / lib : / usr / src / sys $ global strlen../../../ usr / src / lib / libc / string / strlen.c
</code></pre>
<h2>FILES</h2>
<dl>
<dt>&#8216;GTAGS&#8217;</p>
<dd> Tag file for object definitions.</p>
<dt>&#8216;GRTAGS&#8217;</p>
<dd> Tag file for object references.</p>
<dt>&#8216;GSYMS&#8217;</p>
<dd> Tag file for other symbols.</p>
<dt>&#8216;GPATH&#8217;</p>
<dd> Tag file for path of source files.</p>
<dt>&#8216;GTAGSROOT&#8217;</p>
<dd> If environment variable <code>GTAGSROOT</code> is not set and &#8216;GTAGSROOT&#8217; exist in the same directory with &#8216;GTAGS&#8217; then use the value as <code>GTAGSROOT</code>.</p>
<dt>&#8216;/etc/gtags.conf&#8217;, &#8216;$HOME/.globalrc&#8217;</p>
<dd> Configuration file.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>global</code>:</p>
<dl>
<dt><code>GTAGSROOT</code></p>
<dd> The directory which is the root of source code.</p>
<dt><code>GTAGSDBPATH</code></p>
<dd> The directory on which gtags database exist. This value is ignored when <code>GTAGSROOT</code> is not defined.</p>
<dt><code>GTAGSLIBPATH</code></p>
<dd> If this variable is set, it is used as the path to search for library functions. If the specified object is not found in the source project, <code>global</code> also search in these paths. Since only &#8216;GTAGS&#8217; is targeted in the retrieval, this variable is ignored when the <code>-r</code> or <code>-s</code> is specified.</p>
<dt><code>GTAGSLABEL</code></p>
<dd> If this variable is set, its value is used as the label of configuration file. The default is default.</p>
<dt><code>MAKEOBJDIRPREFIX</code></p>
<dd> If this variable is set, &#8216;$MAKEOBJDIRPREFIX&lt;current directory&gt;&#8217; is used as the candidate directory for tag files. The default is &#8216;/usr/obj&#8217;.</dl>
<h2>CONFIGURATION</h2>
<p> The following configuration variables affect the execution of <code>global</code>:</p>
<dl>
<dt>icase_path(boolean)</p>
<dd> Ignore case distinctions in the <i>pattern</i>.</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>Global</code> exits with a non 0 value if an error occurred, 0 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gtags-parser/">gtags-parser</a></code>(1), <code><a href="/docs/linux/man/1-gtags/">gtags</a></code>(1), <code><a href="/docs/linux/man/1-htags/">htags</a></code>(1), <code><a href="/docs/linux/man/1-less/">less</a></code>(1). </p>
<p> GNU GLOBAL source code tag system<br />
 (<a rel="nofollow" href="http://www.gnu.org/software/global/">http://www.gnu.org/software/global/</a>).</p>
<h2>AUTHOR</h2>
<p> Tama Communications Corporation.</p>
<h2>HISTORY</h2>
<p> The <code>global</code> command appeared in FreeBSD 2.2.2. </p>
<h2>Index</h2>
