---
title: "pyreverse-3-4(1)"
name: "pyreverse-3-4"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pyreverse-3-4/"
description: "pyreverse – parse python sources files and extract diagrams from them."
---

<p>pyreverse &#8211; parse python sources files and extract diagrams from them. </p>
<h2>Synopsis</h2>
<p><code>pyreverse </code> <i>[options]</i> &lt;modules&gt; </p>
<h2>Description</h2>
<p><code>pyreverse</code> is a python source analyzer. It parses python packages and produces UML diagrams in different output formats. (dot, all formats available for dot, and vcg). With different options, you can have fine tuning on what and how modules, classes and attributes will be shown in the diagram. You can combine several modules in one project (except with <code>-c</code> ). </p>
<p> If no -c and no &#8211;diadefs option specified, <code>pyreverse </code> will create<br />
&nbsp;<wbr>&#8211; a diagram&nbsp;<wbr>&#8216;classes_&lt;name&gt;&#8217;&nbsp;<wbr>for the classes in&nbsp;<wbr>&lt;modules&gt;&nbsp;<wbr>and<br />
(&nbsp;<wbr>if there is more than one module in&nbsp;<wbr>&lt;projects&gt;&nbsp;<wbr>)<br />
&nbsp;<wbr>&#8211; a diagram&nbsp;<wbr>&#8216;packages_&lt;name&gt;&#8217;&nbsp;<wbr>for the package dependencies in&nbsp;<wbr>&lt;modules&gt;&nbsp;<wbr> </p>
<p> With -c &lt;class&gt;, <code>pyreverse </code> creates a diagram for that &lt;class&gt; with filename &lt;class&gt;.&lt;format&gt;. You can do -c &lt;class1&gt; , -c &lt;class2&gt;. </p>
<h2>Options</h2>
<dl COMPACT>
<dt>-h, &#8211;help</p>
<dd>show help message and exit</p>
<dt>-p&lt;name&gt;, &#8211;project=&lt;name&gt;</p>
<dd>set project name to &lt;name&gt; if not using -c option. (default:&#8217;No Name&#8217;)</p>
<dt>&#8211;ignore=&lt;file&gt;</p>
<dd>add &lt;file&gt; (may be a directory) to the black list (not parsed)</p>
<dt>-f&lt;mode&gt;, &#8211;filter-mode=&lt;mode&gt;</p>
<dd>filter attributes and functions according to &lt;mode&gt;. You can combine modes using &#8216;+&#8217; like &#8216;SPECIAL+OTHER&#8217;. Correct modes are :<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr>&#8216;PUB_ONLY&#8217;&nbsp;<wbr>: filter all non public attributes&nbsp;<wbr>(default)<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr>&#8216;ALL&#8217;&nbsp;<wbr>: no filter<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr>&#8216;SPECIAL&#8217;&nbsp;<wbr>: filter Python special functions except constructor<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr>&#8216;OTHER&#8217;&nbsp;<wbr>: filter protected and private attributes&nbsp;<wbr>[current: PUB_ONLY] </p>
<dt>-d&lt;file&gt;, &#8211;diadefs=&lt;file&gt;</p>
<dd>create diagram according to the diagram definitions in &lt;file&gt;</p>
<dt>-c &lt;class&gt;, &#8211;class=&lt;class&gt;</p>
<dd>create a class diagram with all classes related to &lt;class&gt; [current: none] the class must be in the file &lt;modules&gt;. By default, this will include all ancestors and associated classes of &lt;class&gt; and include module names (i.e. &#8216;-ASmy&#8217; ). </p>
<dt>-a &lt;ancestor&gt;, &#8211;show-ancestors=&lt;ancestor&gt;</p>
<dd>show &lt;ancestor&gt; generations of ancestor classes not in &lt;projects&gt;</p>
<dt>-A, &#8211;all-ancestors=[yn]</p>
<dd>show all ancestors off all classes in &lt;projects&gt; [current: none]</p>
<dt>-s &lt;ass_level&gt;, &#8211;show-associated=&lt;associated&gt;</p>
<dd>show &lt;ass_level&gt; associated classes. &lt;ass_level&gt;=1 will only take classes directly related to the classes in the project, while &lt;ass_level&gt;=2 will also take all classes related to those fetched by&lt;depth&gt;=1.</p>
<dt>-S, &#8211;all-associated=[yn]</p>
<dd>show recursively all associated off all associated classes [current: none] </p>
<dt>-b, &#8211;builtin</p>
<dd>include builtin objects in representation of classes [current: False]</p>
<dt>-m [yn], &#8211;module-names=[yn]</p>
<dd>include module name in representation of classes. This will include the full module path in the class name. [current: none] </p>
<dt>-k, &#8211;only-classnames</p>
<dd>don&#8217;t show attributes and methods in the class boxes; this disables -f values [current: False] </p>
<dt>-o &lt;format&gt;, &#8211;output=&lt;format&gt;</p>
<dd>create a *.&lt;format&gt; output file if format available. Available formats are all formats that dot can produce and <code>vcg.</code> [default: dot] </p>
</dl>
<h2>Examples</h2>
<p>Here are some examples for command line options: </p>
<dl COMPACT>
<dt>pyreverse &lt;project&gt; -a1 -s1 -m</p>
<dd>-a1 -s1 will include one level of ancestor and associated classes in the diagram of the &lt;project&gt; modules, while -m will show the full module path of each class. You can use the <code>-a, -s, -A, -S</code> options in the same way. Note that on class diagrams (using <code>-c</code> ) -a and -s will rather reduce than enlarge your diagram. </p>
<dt>pyreverse mod/foo.py mod/fee.py -k</p>
<dd>This is interesting if the diagram for &lt;project&gt;=mod is too complicated: you can show only the class names (no attributes or methods, option -k); or take only the modules you are interested in (here fee.py and foo.py). </p>
</dl>
<h2>Requires</h2>
<p>Python </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-pylint/">pylint</a>(1)</code> </p>
<p> <i><a rel="nofollow" href="http://www.logilab.org/pyreverse">http://www.logilab.org/pyreverse</a></i> </p>
<h2>Authors</h2>
<p>Sylvain Thenault, Emile Anclin </p>
<p> This manpage was written by Emile Anclin &lt;emile.anclin [at] logilab.fr&gt;</p>
