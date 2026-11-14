---
title: "update-perl-sax-parsers(8)"
name: "update-perl-sax-parsers"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-perl-sax-parsers/"
description: "update-perl-sax-parsers – (de)register Perl SAX parser modules"
---

<p>update-perl-sax-parsers &#8211; (de)register Perl SAX parser modules</p>
<h2>Synopsis</h2>
<p><code>update-perl-sax-parsers</code> [<i>options</i>] <code>&#8211;add</code> <i>parser_module</i> </p>
<p> <code>update-perl-sax-parsers</code> [<i>options</i>] <code>&#8211;remove</code> <i>parser_module</i> </p>
<p> <code>update-perl-sax-parsers</code> [<i>options</i>] <code>&#8211;update</code></p>
<h2>Description</h2>
<p><code>update-perl-sax-parsers</code> inserts, updates and removes individual Perl SAX parser module info files in the directory <i>/var/lib/libxml-sax-perl/ParserDetails.d</i> and the overall Perl SAX parser modules info file <i>/etc/perl/XML/SAX/ParserDetails.ini</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;add</code></p>
<dd>Adds the per-module info file for the indicated Perl SAX parser module to the directory <i>/var/lib/libxml-sax-perl/ParserDetails.d</i>.</p>
<dt><code>&#8211;remove</code></p>
<dd>Removes the per-module info file for Perl SAX parser module from the directory <i>/var/lib/libxml-sax-perl/ParserDetails.d</i>.</p>
<dt><code>&#8211;update</code></p>
<dd>updates the overall Perl SAX parser modules info file <i>/etc/perl/XML/SAX/ParserDetails.ini</i>. The modules will be listed in an order of ascending priority. See the PARSER PRIORITIES section below. </p>
<p> The file will be managed with <code><a href="/docs/linux/man/1-ucf/">ucf</a>(1) ,</code> unless the <code>&#8211;file</code> option is used. See also the <code>&#8211;ucf</code> option below.</p>
<dt><code>&#8211;directory</code></p>
<dd>When used with <code>&#8211;add</code> or with <code>&#8211;remove</code> indicates the ParserDetails.d directory to use for storing the per-module Perl SAX parser module info file. When used one or more times with <code>&#8211;update</code> indicates the ParserDetails.d directories to be used as source for generating the ParserDetails.ini file. Default is <i>/var/lib/libxml-sax-perl/ParserDetails.d</i>.</p>
<dt><code>&#8211;file</code></p>
<dd>Indicates the ParserDetails.ini file up be updated. Default is <i>/etc/perl/XML/SAX/ParserDetails.ini</i>.</p>
<dt><code>&#8211;priority XX</code></p>
<dd>Specifies the priority of the SAX parser module to be added removed. The priority will be encoded to the filename of the ParserDetails.d entry. See the PARSER PRIORITIES section below. </p>
<p> This option was added in version 0.3 of <code>update-perl-sax-parsers .</code> Use the value &quot;0&quot; to disable the encoding and match the behaviour of earlier versions of the script. </p>
<p> The default priority value is 50, unless <code>&#8211;directory</code> was specified, in which case the default is 0 (disabled.)</p>
<dt><code>&#8211;ucf X</code></p>
<dd>Forcibly enable (X != 0) or disable (X = 0) of <code><a href="/docs/linux/man/1-ucf/">ucf</a>(1) .</code> By default, <code><a href="/docs/linux/man/1-ucf/">ucf</a>(1)</code> will be used to manage the ParserDetails.ini file when <code>&#8211;file</code> is <i>not</i> specified.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Prevents any diagnostic output.</p>
<dt><code>&#8211;test</code></p>
<dd>Prevents the modification of any files and enables debugging mode.</p>
<dt><code>&#8211;version</code></p>
<dd>Displays the version information and exits.</p>
<dt><code>&#8211;help</code></p>
<dd>Display the usage information and exits.</dl>
<h2>Parser Priorities</h2>
<p>Starting with version 0.3 of <code>update-perl-sax-parsers ,</code> the parsers are assigned a priority value that is encoded into the names of the files in the ParserDetails.d directory. Specifically, the file name will be &quot;XX-Some::Module&quot;, where XX denotes the priority and Some::Module is the name of the parser module. </p>
<p> When <code>&#8211;update</code> is called, the parsers are listed in an order of ascending priority into the <i>ParserDetails.ini</i> file. The last parser in the file, ie. the one with the highest priority, is the <code>default</code> XML::SAX parser. </p>
<p> Parsers with the same priority are sorted alphabetically by their name. This is contrary to the behaviour of earlier versions, where the sort order was undefined and depended on the underlying file system.</p>
<h2>Note</h2>
<p>Installing the original package from CPAN into /usr/local breaks the Debian package, since the former is in Perl&#8217;s @INC before the latter. So, please don&#8217;t do this. </p>
<p> If there&#8217;s a new version of XML::SAX simply file a wishlist against the Debian package and wait for the update.</p>
<h2>See Also</h2>
<dl>
<dt>/usr/share/doc/libxml-sax-perl/README.Debian</p>
<dd></dl>
<h2>Authors</h2>
<p>Ardo van Rangelrooij &lt;ardo [at] debian.org&gt; </p>
<p> Niko Tyni &lt;ntyni [at] iki.fi&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2001-2003 Ardo van Rangelrooij </p>
<p> Copyright &#169; 2007 Niko Tyni </p>
<p> This is free software; see the GNU General Public Licence version 2 or later for copying conditions. There is <i>no</i> warranty.</p>
