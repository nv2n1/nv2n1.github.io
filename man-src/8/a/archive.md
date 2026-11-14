---
title: "archive(8)"
name: "archive"
section: "8"
letter: "a"
url: "/docs/linux/man/8-archive/"
description: "archive – Usenet article archiver"
---

<p>archive &#8211; Usenet article archiver</p>
<h2>Synopsis</h2>
<p><code>archive</code> [<code>-cfr</code>] [<code>-a</code> <i>archive</i>] [<code>-i</code> <i>index</i>] [<code>-p</code> <i>pattern</i>] [<i>input</i>]</p>
<h2>Description</h2>
<p><code>archive</code> makes copies of files specified on its standard input. It is normally run either as a channel feed under <code>innd</code> or by a script before <code>news.daily</code> is run. </p>
<p> <code>archive</code> reads the named <i>input</i> file, or standard input if no file is given. The input is taken as a sequence of lines; blank lines and lines starting with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines should specify the token of an article to archive. Every article is retrieved from a token, and the Xref: header is used to determine the target file in the archive directory. You can limit the targets taken from the Xref: header with the <code>-p</code> option. </p>
<p> Files are copied to a directory within the archive directory, <i>patharchive</i> in <i>inn.conf</i> (or some other directory given with <code>-a</code>). The default is to create a hierarchy that mimics a traditional news spool storage of the given articles; intermediate directories will be created as needed. For example, if the input token represents article 2211 in the newsgroup comp.sources.unix, <code>archive</code> will by default store the article as: </p>
<pre> comp/sources/unix/2211</pre>
<p>in the archive area. This can be modified with the <code>-c</code> and <code>-f</code> options.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>archive</i></p>
<dd>If the <code>-a</code> flag is given, its argument specifies the root of the archive area, instead of <i>patharchive</i> in <i>inn.conf</i>.</p>
<dt><code>-c</code></p>
<dd>If the <code>-c</code> flag is given, directory names will be flattened as described under the <code>-f</code> option. Then, additionally, all posts will be concatenated into a single file, appending to that file if it already exists. The file name will be <tt>&quot;YYYYMM&quot;</tt>, formed from the current time when <code>archive</code> is run. In other words, if given an article in comp.sources.unix on December 14th, 1998, the article would be appended to the file: </p>
<pre> comp.sources.unix/199812</pre>
<p>in the archive area. </p>
<p> Articles will be separated by a line containing only <tt>&quot;-----------&quot;</tt>.</p>
<dt><code>-f</code></p>
<dd>If the <code>-f</code> flag is used, directory names will be flattened, replacing the slashes with the periods. In other words, article 2211 in comp.sources.unix will be written to: </p>
<pre> comp.sources.unix/2211</pre>
<p>in the archive area.</p>
<dt><code>-i</code> <i>index</i></p>
<dd>If the <code>-i</code> flag is used, <code>archive</code> will append one line to the file <i>index</i> for each article that it archives. This line will contain the destination file name, the Message-ID: header, and the Subject: header of the message, separated by spaces. If either header is missing (normally not possible if the article was accepted by <code>innd</code>), it will be replaced by <tt>&quot;&lt;none&gt;&quot;</tt>. The headers will be transformed using the same rules as are used to generate overview data (unfolded and then with tabs, <font SIZE="-1">CR</font>, and <font SIZE="-1">LF</font> replaced by spaces).</p>
<dt><code>-p</code> <i>pattern</i></p>
<dd>Limits the targets taken from the Xref: header to the groups specified in <i>pattern</i>. <i>pattern</i> is a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) pattern matching newsgroups that you wish to have <code>archive</code> handle.</p>
<dt><code>-r</code></p>
<dd>By default, <code>archive</code> sets its standard error to <i>pathlog</i>/errlog. To suppress this redirection, use the <code>-r</code> flag.</dl>
<h2>Return Value</h2>
<p>If the input is exhausted, <code>archive</code> will exit with a zero status. If an I/O error occurs, it will try to spool its input, copying it to a file. If there was no input filename, the standard input will be copied to <i>pathoutgoing</i>/archive and the program will exit. If an input filename was given, a temporary file named <i>input</i>.bch (if <i>input</i> is an absolute pathname) or <i>pathoutgoing</i>/<i>input</i>.bch (if the filename does not begin with a slash) is created. Once the input is copied, <code>archive</code> will try to rename this temporary file to be the name of the input file, and then exit.</p>
<h2>Examples</h2>
<p>A typical <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5) entry to archive most source newsgroups is as follows: </p>
<pre> source-archive!\
 :!*,*sources*,!*wanted*,!*.d\
 :Tc,Wn\
 :&lt;pathbin&gt;/archive -f -i &lt;patharchive&gt;/INDEX</pre>
<p>Replace &lt;pathbin&gt; and &lt;patharchive&gt; with the appropriate paths.</p>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> archive.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5). </p>
