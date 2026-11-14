---
title: "abook(1)"
name: "abook"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abook/"
description: "abook – text-based address book program"
---

<h2 class="name">NAME</h2>
<p> abook &#8211; text-based address book program </p>
<h2>SYNOPSIS</h2>
<p> <code>abook</code> [ <i>OPTION</i> ]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>abook</code> program. This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page. </p>
<p> <code>abook </code> is a text-based address book program. It contains Name, Email, Address and various Phone fields. It is designed for use with mutt, but can be equally useful on its own.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd> Show usage.</p>
<dt><code>-C &#8211;config</code> <i>&lt;filename&gt;</i></p>
<dd> Use an alternative configuration file (default is <i>$HOME/.abook/abookrc</i>).</p>
<dt><code>&#8211;datafile</code> <i>&lt;filename&gt;</i></p>
<dd> Use an alternative addressbook file (default is <i>$HOME/.abook/addressbook</i>).</p>
<dt><code>&#8211;mutt-query</code> <i>&lt;string&gt;</i></p>
<dd> Make a query for mutt (search the addressbook for <i>&lt;string&gt;</i>).<br />
 The <code>&#8211;datafile</code> option, as documented above, may be used <code>BEFORE</code> this option to search a different addressbook file.</p>
<dt><code>&#8211;convert</code> [ <code>&#8211;informat</code> <i>&lt;inputformat&gt;</i> ] [ <code>&#8211;infile</code> <i>&lt;inputfile&gt;</i> ] [ <code>&#8211;outformat</code> <i>&lt;outputformat&gt;</i> ] [ <code>&#8211;outfile</code> <i>&lt;outputfile&gt;</i> ]</p>
<dd> Converts <i>&lt;inputfile&gt;</i> in <i>&lt;inputformat&gt;</i> to <i>&lt;outputfile&gt;</i> in <i>&lt;outputformat&gt;</i> (defaults are <code>abook</code>, <code>stdin</code>, <code>text</code> and <code>stdout</code>). </p>
<p> The following <i>inputformats</i> are supported:<br />
 &#8211; <code>abook</code> abook native format<br />
 &#8211; <code>ldif</code> ldif / Netscape addressbook<br />
 &#8211; <code>mutt</code> mutt alias<br />
 &#8211; <code>pine</code> pine addressbook<br />
 &#8211; <code>csv</code> comma separated values<br />
 &#8211; <code>palmcsv</code> Palm comma separated values </p>
<p> The following <i>outputformats</i> are supported:<br />
 &#8211; <code>abook</code> abook native format<br />
 &#8211; <code>ldif</code> ldif / Netscape addressbook (.4ld)<br />
 &#8211; <code>mutt</code> mutt alias<br />
 &#8211; <code>html</code> html document<br />
 &#8211; <code>pine</code> pine addressbook<br />
 &#8211; <code>gcrd</code> GnomeCard (VCard) addressbook<br />
 &#8211; <code>csv</code> comma separated values<br />
 &#8211; <code>palmcsv</code> Palm comma separated values<br />
 &#8211; <code>elm</code> elm alias<br />
 &#8211; <code>text</code> plain text<br />
 &#8211; <code>spruce</code> Spruce address book<br />
 &#8211; <code>wl</code> Wanderlust address book<br />
 &#8211; <code>bsdcal</code> BSD calendar</p>
<dt><code>&#8211;add-email</code></p>
<dd> Read an e-mail message from stdin and add the sender to the addressbook.</p>
<dt><code>&#8211;add-email-quiet</code></p>
<dd> Same as &#8211;add-email but doesn&#8217;t confirm adding.</p>
<dt><code>&#8211;formats</code></p>
<dd> List available formats. </p>
</dl>
<h2>COMMANDS DURING USE</h2>
<p> Press &#8216;<code>?</code>&#8216; during use to get a list of commands.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), <code><a href="/docs/linux/man/5-abookrc/">abookrc</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Alan Ford &lt;alan [at] whirlnet.co.uk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<p> <code>abook</code> was written by Jaakko Heinonen &lt;jheinonen [at] users.sourceforge.net&gt; </p>
<h2>Index</h2>
