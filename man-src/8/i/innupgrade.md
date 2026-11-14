---
title: "innupgrade(8)"
name: "innupgrade"
section: "8"
letter: "i"
url: "/docs/linux/man/8-innupgrade/"
description: "innupgrade – Upgrade INN configuration files"
---

<p>innupgrade &#8211; Upgrade INN configuration files</p>
<h2>Synopsis</h2>
<p><code>innupgrade</code> <i>directory</i> </p>
<p> <code>innupgrade</code> [<code>-t</code> <i>type</i>] <code>-f</code> <i>file</i></p>
<h2>Description</h2>
<p><code>innupgrade</code> is intended to be run during a major upgrade of <font SIZE="-1">INN</font> to fix the configuration files with any required changes. If given a directory, it will scan that directory for any files that it has updates defined for, try to perform those updates, and replace the files with updated versions if applying the updates resulted in any changes. The old versions of the files will be saved with a <tt>&quot;.OLD&quot;</tt> extension. </p>
<p> If the <code>-f</code> flag is used, only that file will be updated. If the file name doesn&#8217;t match the standard file name of an <font SIZE="-1">INN</font> configuration file, the optional <code>-t</code> flag may be given to specify the type. See &#8220;<font SIZE="-1">EXAMPLES</font>&#8221; for an example of this. </p>
<p> Currently, <code>innupgrade</code> knows how to apply the following updates:</p>
<dl>
<dt><i>inn.conf</i></p>
<dd>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Quote values with whitespace and comment out keys with no values, required for the change in configuration parsers introduced in <font SIZE="-1">INN</font>&nbsp;<wbr>2.4. The new format is not backward compatible with the previous parser, since the previous parser will include the double-quotes in the value of the parameter.</p>
<dt>&bull;</p>
<dd>Add the <i>hismethod</i> parameter if not found (introduced in <font SIZE="-1">INN</font>&nbsp;<wbr>2.4, with the default value <tt>&quot;hisv6&quot;</tt>) and rename <i>nntpactsync</i> to <i>incominglogfrequency</i> (since <font SIZE="-1">INN</font>&nbsp;<wbr>2.5).</p>
<dt>&bull;</p>
<dd>If the <i>overview.fmt</i> file exists, its content is merged in the <i>extraoverviewadvertised</i> and <i>extraoverviewhidden</i> parameters introduced in <font SIZE="-1">INN</font>&nbsp;<wbr>2.5. The file is then renamed to <i>overview.fmt.OLD</i>.</p>
<dt>&bull;</p>
<dd>If the <i>sasl.conf</i> file exists, its content is merged in the <i>tlscapath</i>, <i>tlscafile</i>, <i>tlscertfile</i> and <i>tlskeyfile</i> parameters introduced in <font SIZE="-1">INN</font>&nbsp;<wbr>2.5. The file is then renamed to <i>sasl.conf.OLD</i>.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>newsfeeds</i></p>
<dd>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Replace the use of <code>startinnfeed</code> with the appropriate direct invocation of <code>innfeed</code> or <code>imapfeed</code>.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<p> A few obsolete programs or configuration files are renamed with a <tt>&quot;.OLD&quot;</tt> extension by <code>innupgrade</code>. Obsolete man pages are directly removed. </p>
<p> Normally, <code>innupgrade</code> should be run at least on the <i>pathetc</i> directory after any upgrade of <font SIZE="-1">INN</font> other than a patch release (any upgrade that changes the first or second version numbers). This may occur automatically during the upgrade process.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code> <i>file</i></p>
<dd>Only act on <i>file</i> rather than working on an entire directory.</p>
<dt><code>-t</code> <i>type</i></p>
<dd>For a file specified with <code>-f</code>, parse it and upgrade it as if it were named <i>type</i>. Used for upgrading files with the same syntax as normal <font SIZE="-1">INN</font> configuration files but with different names. Only makes sense in combination with <code>-f</code>.</dl>
<h2>Examples</h2>
<p>Upgrade any configuration files found in <i>pathetc</i> and append a <tt>&quot;.OLD&quot;</tt> extension to obsolete files in <i>pathetc</i>: </p>
<pre> innupgrade &lt;pathetc in inn.conf&gt;</pre>
<p>Upgrade only <i>/news/etc/inn.conf</i>: </p>
<pre> innupgrade -f /news/etc/inn.conf</pre>
<p>Upgrade a file named <i>inn-special.conf</i> that should have the same syntax as <i>inn.conf</i>: </p>
<pre> innupgrade -t inn.conf -f inn-special.conf</pre>
<p>Any upgrade rules that apply to <i>inn.conf</i> will be applied to the alternate file.</p>
<h2>History</h2>
<p>Written by Russ Allbery &lt;eagle [at] eyrie.org&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> innupgrade.pod 9768 2014-12-07 21:22:57Z iulius $</p>
