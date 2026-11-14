---
title: "rdoc3-0(1)"
name: "rdoc3-0"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdoc3-0/"
description: "rdoc3.0 – Generate documentation from Ruby script files"
---

<p>rdoc3.0 &#8211; Generate documentation from Ruby script files </p>
<h2>Synopsis</h2>
<p>rdoc3.0 [options] [names&#8230;]</p>
<h2>Description</h2>
<p>Files are parsed, and the information they contain collected, before any output is produced. This allows cross references between all files to be resolved. If a name is a directory, it is traversed. If no names are specified, all Ruby files in the current directory (and subdirectories) are processed. </p>
<p> Available output formatters: chm, html, ri, xml </p>
<p> For information on where the output goes, use: </p>
<pre> rdoc --help-output</pre>
<h2>Options</h2>
<dl COMPACT>
<dd><code>&#8211;accessor, -A accessorname[,..]</code> comma separated list of additional class methods that should be treated like &#8216;attr_reader&#8217; and friends. Option may be repeated. Each accessorname may have &#8216;=text&#8217; appended, in which case that text appears where the r/w/rw appears for normal accessors.</p>
<dd><code>&#8211;all, -a</code> include all methods (not just public) in the output.</p>
<dd><code>&#8211;charset, -c charset</code> specifies HTML character-set</p>
<dd><code>&#8211;debug, -D</code> displays lots on internal stuff</p>
<dd><code>&#8211;diagram, -d</code> generate diagrams showing modules and classes. You need dot V1.8.6 or later to use the &#8211;diagram option correctly. Dot is available from &lt;URL:<a rel="nofollow" href="http://www.research.att.com/sw/tools/graphviz/">http://www.research.att.com/sw/tools/graphviz/</a>&gt;.</p>
<dd><code>&#8211;exclude, -x pattern</code> do not process files or directories matching pattern. Files given explicitly on the command line will never be excluded.</p>
<dd><code>&#8211;extension, -E new = old</code> treat files ending with .new as if they ended with .old. Using &#8216;-E cgi=rb&#8217; will cause xxx.cgi to be parsed as a Ruby file</p>
<dd><code>&#8211;fileboxes, -F</code> classes are put in boxes which represents files, where these classes reside. Classes shared between more than one file are shown with list of files that sharing them. Silently discarded if &#8211;diagram is not given Experimental.</p>
<dd><code>&#8211;fmt, -f formatname</code> set the output formatter (see below).</p>
<dd><code>&#8211;help, -h</code> print usage.</p>
<dd><code>&#8211;help-output, -O</code> explain the various output options.</p>
<dd><code>&#8211;image-format, -I gif|png|jpg|jpeg</code> sets output image format for diagrams. Can be png, gif, jpeg, jpg. If this option is omitted, png is used. Requires &#8211;diagram.</p>
<dd><code>&#8211;include, -i dir[,dir&#8230;]</code> set (or add to) the list of directories to be searched when satisfying :include: requests. Can be used more than once.</p>
<dd><code>&#8211;inline-source, -S</code> show method source code inline, rather than via a popup link.</p>
<dd><code>&#8211;line-numbers, -N</code> include line numbers in the source code</p>
<dd><code>&#8211;main, -m name</code> name will be the initial page displayed.</p>
<dd><code>&#8211;merge, -M</code> when creating ri output, merge processed classes into previously documented classes of the name name.</p>
<dd><code>&#8211;one-file, -1</code> put all the output into a single file.</p>
<dd><code>&#8211;op, -o dir</code> set the output directory.</p>
<dd><code>&#8211;opname, -n name</code> set the name of the output. Has no effect for HTML.</p>
<dd><code>&#8211;promiscuous, -p</code> When documenting a file that contains a module or class also defined in other files, show all stuff for that module/class in each files page. By default, only show stuff defined in that particular file.</p>
<dd><code>&#8211;quiet, -q</code> don&#8217;t show progress as we parse.</p>
<dd><code>&#8211;ri, -r</code> generate output for use by &#8216;ri.&#8217; The files are stored in the &#8216;.rdoc&#8217; directory under your home directory unless overridden by a subsequent &#8211;op parameter, so no special privileges are needed.</p>
<dd><code>&#8211;ri-site, -R</code> generate output for use by &#8216;ri.&#8217; The files are stored in a site-wide directory, making them accessible to others, so special privileges are needed.</p>
<dd><code>&#8211;ri-system, -Y</code> generate output for use by &#8216;ri.&#8217; The files are stored in a system-level directory, making them accessible to others, so special privileges are needed. This option is intended to be used during Ruby installations.</p>
<dd><code>&#8211;show-hash, -H</code> a name of the form #name in a comment is a possible hyperlink to an instance method name. When displayed, the &#8216;#&#8217; is removed unless this option is specified.</p>
<dd><code>&#8211;style, -s stylesheet-url</code> specifies the URL of a separate stylesheet.</p>
<dd><code>&#8211;tab-width, -w n</code> set the width of tab characters (default 8).</p>
<dd><code>&#8211;template, -T template-name</code> set the template used when generating output.</p>
<dd><code>&#8211;title, -t text</code> set text as the title for the output.</p>
<dd><code>&#8211;version, -v</code> display RDoc&#8217;s version.</p>
<dd><code>&#8211;webcvs, -W url</code> specify a URL for linking to a web frontend to CVS. If the URL contains a contain a &#8216;%s&#8217;, the filename will be appended to it. </p>
</dl>
