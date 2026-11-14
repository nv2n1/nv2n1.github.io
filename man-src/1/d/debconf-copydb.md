---
title: "debconf-copydb(1)"
name: "debconf-copydb"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-copydb/"
description: "debconf-copydb – copy a debconf database"
---

<h2 class="name">NAME</h2>
<p> debconf-copydb &#8211; copy a debconf database </p>
<h2>SYNOPSIS</h2>
<pre><code>
debconf - copydb sourcedb destdb[--pattern = pattern][--owner - pattern = pattern] [--config = Foo:bar]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>debconf-copydb</code> copies items from an existing debconf database into another, possibly new database. The two databases may have different formats; if so a conversion will automatically be done.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>sourcedb</i></p>
<dd> The name of the source database. Typically it will be defined in your debconf.conf (or .debconfrc) file.</p>
<dt><i>destdb</i></p>
<dd> The name of the destination database. It may be defined in debconf.conf or .debconfrc, or you might define it on the command line (see below).</p>
<dt><code>-p</code> <i>pattern</i>, <code>&#8211;pattern</code> <i>pattern</i></p>
<dd> If this is specified, only items in <i>sourcedb</i> whose names match the pattern will be copied.</p>
<dt><code>&#8211;owner-pattern</code> <i>pattern</i></p>
<dd> If this is specified, only items in <i>sourcedb</i> whose owners match the pattern will be copied.</p>
<dt><code>-c</code> <i>foo:bar</i>, <code>&#8211;config</code> <i>Foo:bar</i></p>
<dd> Set option Foo to bar. This is similar to writing: </p>
<pre>
  Foo: bar
</pre>
<p> In debconf.conf, except you probably want to leave off the space on the command line (or quote it: &#8220;Foo: bar&#8221;). Generally must be used multiple times, to build up a full configuration stanza. While blank lines are used to separate stanzas in debconf.conf, this program will assume that &#8220;Name:dbname&#8221; denotes the beginning of a new stanza.</dl>
<h2>EXAMPLES</h2>
<pre>
  debconf-copydb configdb backup
</pre>
<p> Copy all of configdb to backup, assuming you already have the backup database defined in debconf.conf. </p>
<p>debconf &#8211; copydb configdb newdb&#8211; pattern = &#8216;^slrn/&#8217; &#8211;config = Name : newdb&#8211; config = Driver : File&#8211; config = Filename : newdb.dat</p>
<p> Copy slrn&#8217;s data out of configdb, and into newdb. newdb is not defined in the rc file, so the &#8211;config switches set up the database on the fly. </p>
<pre>
  debconf-copydb configdb stdout -c Name:stdout -c Driver:Pipe \
        -c InFd:none --pattern='^foo/'
</pre>
<p> Spit out all the items in the debconf database related to package foo. </p>
<pre><code>
debconf - copydb configdb pipe-- config = Name : pipe-- config = Driver : Pipe-- config = InFd : none |
                                                                                                 ssh remotehost debconf - copydb pipe configdb-- config = Name : pipe-- config = Driver : Pipe
</code></pre>
<p> This uses the special purpose pipe driver to copy a database to a remote system.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-debconf-conf/">debconf.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
