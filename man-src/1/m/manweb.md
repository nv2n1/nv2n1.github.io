---
title: "manweb(1)"
name: "manweb"
section: "1"
letter: "m"
url: "/docs/linux/man/1-manweb/"
description: "manweb – browse netpbm (and other) documentation"
---

<h2 class="name">NAME</h2>
<p> manweb &#8211; browse netpbm (and other) documentation</p>
<h2>SYNOPSIS</h2>
<p> <code>manweb</code> <code>-help</code> </p>
<p> <code>manweb</code> [<code>-config=</code><i>configfile</i>] [<i>topic</i> [ <i>subtopic</i> &#8230; ] ] </p>
<h2>EXAMPLES</h2>
<pre>
manweb
</pre>
<p> This gets a master index of documentation. </p>
<pre>
manweb netpbm
</pre>
<p> This gets the main documentation page for the Netpbm package, with hyperlinks to the rest of the documentation. </p>
<pre>
manweb netpbm pngtopam
</pre>
<p> This goes directly to the documentation page for the Pngtopam program in the Netpbm package. </p>
<pre>
manweb pngtopam
</pre>
<p> This also goes directly to the documentation page for the Pngtopam program in the Netpbm package, if that&#8217;s what would run in response to a <code>pngtopam</code> shell command (your <code>PATH</code> environment variable is involved). </p>
<pre>
manweb 3 fopen
</pre>
<p> This gets the traditional man page for the fopen() subroutine using <code>man</code>. </p>
<pre>
manweb cp
</pre>
<p> This gets the GNU Info manual for the <code>cp</code> program, using <code>info</code>. </p>
<h2>DESCRIPTION</h2>
<p> <code>manweb</code> displays reference documentation via quick shell commands. It is a replacement for the well-known <code>man</code>. </p>
<h2>Differences Between Man and Manweb</h2>
<p> <code>manweb</code>&#8216;s advantages over <code>man</code> are: </p>
<dl>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>You can access documentation that is on the worldwide web instead of<br />
&nbsp;<wbr>having locally installed copies.&nbsp;<wbr>&nbsp;<wbr>This saves installation work and gets<br />
&nbsp;<wbr>you more current documentation. </p>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>Documentation can be in HTML, which is more widely known, more widely<br />
&nbsp;<wbr>useful, and more expressive than the nroff/troff format used by<br />
&nbsp;<wbr><code>man</code>. </p>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>puts your topics in a tree for multilevel documentation.<br />
&nbsp;<wbr><code>man</code>&nbsp;<wbr>is intended for a single level of documentation.&nbsp;<wbr>&nbsp;<wbr>For<br />
&nbsp;<wbr>example, you can have a man page for each shell command, but not for<br />
&nbsp;<wbr>the subcommands of a shell command.&nbsp;<wbr>&nbsp;<wbr>And you cannot properly have<br />
&nbsp;<wbr>man pages for the members of multiple subroutine libraries. </p>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>Documentation can be hyperlinked. </p>
</dl>
<p> Web servers need not be involved &#8212; the documentation can be in local files. Graphics need not be involved &#8212; the <code>lynx</code> browser works fine in the same kind of terminals in which <code>man</code> works. </p>
<p> <code>manweb</code> finds the documentation you specify and calls a web browser of your choice to display it. The documentation <code>manweb</code> finds can be either an HTML file on your system, in which case, <code>manweb</code> gives a <code>file:</code> URL to your browser, or an explicit URL. That explicit URL might be an <code>http:</code> URL referring to an HTML file on a web server somewhere, or anything else your browser understands. </p>
<p> If <code>manweb</code> finds neither an HTML file nor a URL, but your parameters look like they could mean something to <code>man</code>, <code>manweb</code> calls <code>man</code>. Therefore, you can use a single command to access the vast body of traditional man pages, plus any newer <code>manweb</code> documentation. You can make &quot;man&quot; a shell alias of &quot;manweb&quot;. </p>
<p> <code>manweb</code> finds Info documentation as well. It looks for the topic you specify as an Info topic after looking for HTML and URL documentation and before running <code>man</code>. If <code>manweb</code> finds a corresponding Info topic, it runs the program <code>info</code> on it. Info is the documentation system that the GNU project invented to, among other things, replace traditional Unix man pages. However, HTML and the Worldwide Web were invented shortly afterward, so Info fizzled. But there is still a lot of GNU software that is documented as Info topics. </p>
<h3>How Manweb Finds Documentation</h3>
<p> <code>manweb</code> passes a URL to a web browser. This section tells how your <code>manweb</code> invocation parameters turn into that URL. </p>
<p> <code>manweb</code>&#8216;s search starts in the &quot;web directory&quot; directory. That&#8217;s either the value of the <code>webdir</code> keyword in your <code>manweb</code> configuration file, or the default <code>/usr/man/web</code>. </p>
<p> Your invocation parameters form a &quot;topic chain.&quot; Going from left to right, the first parameter is the main topic, the 2nd is a subtopic of the main topic, and so on. </p>
<p> Let&#8217;s look at the simple case where you specify exactly one parameter &#8212; a main topic. We&#8217;ll call it <i>maintopic</i> and look at 4 ways <code>manweb</code> might find it: </p>
<dl>
<dt>&bull;</p>
<dd>
<p> If <code>manweb</code> finds a file named <i>maintopic</i><code>.html</code><br />
&nbsp;<wbr>in the web directory, the URL&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>passes to the<br />
&nbsp;<wbr>browser is just a&nbsp;<wbr><code>file:</code>&nbsp;<wbr>URL that specifies that .html<br />
&nbsp;<wbr>file. </p>
<dt>&bull;</p>
<dd>
<p> If there&#8217;s no .html file, but there is a file named<br />
&nbsp;<wbr><i>maintopic</i><code>.url</code>, the contents of the first line of<br />
&nbsp;<wbr>that .url file is what&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>passes to the browser.&nbsp;<wbr>&nbsp;<wbr>It<br />
&nbsp;<wbr>doesn&#8217;t interpret the contents at all.&nbsp;<wbr>&nbsp;<wbr>If it&#8217;s garbage, the<br />
&nbsp;<wbr>browser chokes on it. </p>
<dt>&bull;</p>
<dd>
<p> If there&#8217;s neither a .html nor a .url file, but there is a<br />
&nbsp;<wbr>directory named&nbsp;<wbr><i>maintopic</i>,&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>looks in the<br />
&nbsp;<wbr>directory for a file named&nbsp;<wbr><i>index.html</i>.&nbsp;<wbr>&nbsp;<wbr>If there is one,<br />
&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>passes a&nbsp;<wbr><code>file:</code>&nbsp;<wbr>URL specifying that<br />
&nbsp;<wbr>index.html file to the browser.&nbsp;<wbr>&nbsp;<wbr>If there&#8217;s no<br />
&nbsp;<wbr><i>index.html</i>,&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>uses a&nbsp;<wbr><code>file:</code>&nbsp;<wbr>URL that<br />
&nbsp;<wbr>specifies the directory itself. </p>
<dt>&bull;</p>
<dd>
<p> If <code>manweb</code> doesn&#8217;t find documentation in any of the<br />
&nbsp;<wbr>above ways, it searches your executable search path&nbsp;<wbr>(as defined<br />
&nbsp;<wbr>by your&nbsp;<wbr><code>PATH</code>&nbsp;<wbr>environment variable)&nbsp;<wbr>for a program named<br />
&nbsp;<wbr><i>maintopic</i>.&nbsp;<wbr>&nbsp;<wbr>If it finds one, it looks in the directory<br />
&nbsp;<wbr>that contains the program for a file named&nbsp;<wbr><code>doc.url</code>.&nbsp;<wbr>&nbsp;<wbr>If<br />
&nbsp;<wbr>it finds one, it appends&nbsp;<wbr><i>maintopic</i><code>.html</code>&nbsp;<wbr>to the<br />
&nbsp;<wbr>first line of the file and passes that to the browser.&nbsp;<wbr>&nbsp;<wbr>Unless&nbsp;<wbr><br />
&nbsp;<wbr>the first line does&nbsp;<wbr><i>not</i>&nbsp;<wbr>end with a slash &#8212; in that&nbsp;<wbr><br />
&nbsp;<wbr>case,&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>passes the first line of the file unmodified<br />
&nbsp;<wbr>to the browser.<br />
&nbsp;<wbr></dl>
<p> It gets a little more interesting when you have subtopics. Looking at each of the 4 cases above: </p>
<dl>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>Where&nbsp;<wbr><i>maintopic</i><code>.html</code>&nbsp;<wbr>exists, subtopics are invalid.<br />
&nbsp;<wbr>You get a warning message and the subtopics are ignored. </p>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>Where there&#8217;s no .html file but&nbsp;<wbr><i>maintopic</i><code>.url</code>&nbsp;<wbr>exists,<br />
&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>appends the subtopic chain to the URL it gets from the<br />
&nbsp;<wbr>.url file as in the following example:&nbsp;<wbr>&nbsp;<wbr>.url file contains<br />
&nbsp;<wbr><code><a rel="nofollow" href="http://acme.com/productxyz/">http://acme.com/productxyz/</a></code>&nbsp;<wbr>and subtopics are<br />
&nbsp;<wbr><code>create</code>&nbsp;<wbr>and<br />
&nbsp;<wbr><code>database</code>.&nbsp;<wbr>&nbsp;<wbr>The URL&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>passes to the browser is<br />
&nbsp;<wbr><code><a rel="nofollow" href="http://acme.com/productxyz/create/database.html">http://acme.com/productxyz/create/database.html</a></code>. </p>
<p> <code>manweb</code> doesn&#8217;t check that this kind of appendage makes<br />
&nbsp;<wbr>any sense for the URL in question, except that if the URL in the<br />
&nbsp;<wbr>.url file doesn&#8217;t end with a slash&nbsp;<wbr>(<code>/</code>),&nbsp;<wbr><code>manweb</code><br />
&nbsp;<wbr>issues a warning and doesn&#8217;t append anything&nbsp;<wbr>(ignores the subtopics).</p>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>Where there&#8217;s neither a .html file nor a .url file, but there&#8217;s a<br />
&nbsp;<wbr><i>maintopic</i>&nbsp;<wbr>directory,&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>recurses into that<br />
&nbsp;<wbr>directory and begins a whole new search using the first subtopic<br />
&nbsp;<wbr>as the main topic and the rest of the subtopics as subtopics of that.</p>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>When there are subtopics, the&nbsp;<wbr><code>PATH</code>&nbsp;<wbr>thing doesn&#8217;t make sense,<br />
&nbsp;<wbr>so&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>doesn&#8217;t do it. </p>
<p> If you give subtopics, the <code>PATH</code> thing described above for one topic doesn&#8217;t apply.</dl>
<p> If you give no parameters at all, <code>manweb</code> generates a URL for the web directory itself as described above for subdirectories. </p>
<p> The above is simplified by the assumption of a single web directory. In reality, the <code>webdir</code> keyword in the configuration file can specify a chain of web directories. <code>manweb</code> searches each one in turn, doing all the kinds of searches in each web directory before moving on to the next one. </p>
<h3>The Configuration File</h3>
<p> The default location of the <code>manweb</code> configuration file is <code>/etc/manweb.conf</code>. But you can override this with the environment variable <code>MANWEB_CONF_FILE</code>, and override that with the <code>-config</code> invocation option. </p>
<p> Lines starting with &quot;#&quot; are comments and are ignored, as are blank lines. </p>
<p> All other lines have the format <i>keyword</i>=<i>value</i>. The keywords defined are: </p>
<dl>
<dt>webdir</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>A colon-delimited sequence of directories to search for<br />
&nbsp;<wbr>documentation as described above.&nbsp;<wbr>&nbsp;<wbr>If you<br />
&nbsp;<wbr>don&#8217;t specify this, the default is&nbsp;<wbr><code>/usr/man/web</code>&nbsp;<wbr>alone.</p>
<dt>browser</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>The file specification&nbsp;<wbr><code>manweb</code>&nbsp;<wbr>of the web browser&nbsp;<wbr><code>manweb</code><br />
&nbsp;<wbr>is to invoke<br />
&nbsp;<wbr>to display documentation&nbsp;<wbr>(except when it uses&nbsp;<wbr><code>man</code>&nbsp;<wbr>to display<br />
&nbsp;<wbr>a conventional man page).<br />
&nbsp;<wbr>If the file specification does not include a slash,&nbsp;<wbr><code>manweb</code><br />
&nbsp;<wbr>searches for the file in the PATH search path. </p>
<p> If you don&#8217;t specify this, the default is the value of the<br />
&nbsp;<wbr><code>BROWSER</code>&nbsp;<wbr>environment variable, and if that is not set,<br />
&nbsp;<wbr><code>lynx</code>. </p>
<p> Example: </p>
<pre>
# Configuration file for Manweb
webdir=/usr/share/manweb
browser=netscape
</pre>
<p>&nbsp;<wbr> </p>
</dl>
<h2>Index</h2>
