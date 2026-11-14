---
title: "makedat(1)"
name: "makedat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makedat/"
description: "makedat – create GDBM/DB files for maildrop"
---

<h2 class="name">NAME</h2>
<p> makedat &#8211; create GDBM/DB files for maildrop </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>makedat</code> {-src=<i>textfile</i>} {-tmp=<i>tmpfile</i>} {-file=<i>gdbmfile</i>} [-cidr]</dl>
<h2>DESCRIPTION</h2>
<dd>The gdbm family of functions in <code>maildrop</code> provides access to GDBM/DB databases &#8211; simple database files. The gdbm family of functions provide a way of quickly storing and looking up key/data pairs. </p>
<p> You can use any program to create GDBM/DB database files. <code>makedat</code> is a quick utility to create GDBM or DB files from plain text files. </p>
<p> The system administrator selects whether <code>maildrop</code> uses GDBM or DB database files and whether <code>makedat</code> creates GDBM or DB database files as well. </p>
<p> The <code>makedat</code> command may not be available to you. GDBM/DB support in <code>maildrop</code> is optional, and the system administrator may choose not to install GDBM/DB support and the <code>makedat</code> command. </p>
<p> To see whether GDBM or DB support is being used, run the command &quot;<code>maildrop -v</code>&quot;. </p>
<p> The <i>textfile</i> argument to <code>makedat</code> is a plain text file containing key/value pairs. Each line in the text file contains a key value, followed by a tab and a data value. The data value may be omitted, which defaults to &quot;1&quot;. For example, the following three lines: </p>
<dl>
<dt>
<dd>
<pre>
example.com
domain.com&lt;tab&gt;ok
foo.domain.com&lt;tab&gt;bad
</pre>
</dl>
<p> Three key/value pairs are created: example.com, value &quot;1&quot;; domain.com, value &quot;ok&quot;, and &quot;foo.domain.com&quot;, value &quot;bad&quot;. </p>
<p> Empty lines in <i>textfile</i>, and lines starting with the # character, are ignored. </p>
<p> <i>textfile</i> can be &quot;-&quot;, in which case standard input is used. </p>
<p> <i>gdbmfile</i> is the GDBM/DB file to create. If this file exists, its existing contents are replaced. </p>
<p> <i>tmpfile</i> is a name of a temporary file in the same directory as <i>gdbmfile</i>. <i>tmpfile</i> is used by <code>makedat</code> to create the GDBM file, then <i>tmpfile</i> is renamed to <i>gdbmfile</i>. </p>
<p> This approach foregoes any need for locking in order to be able to dynamically update GDBM/DB files used by <code>maildrop</code>&#8216;s gdbm functions. However, <code>makedat</code> does not use any locks on <i>tmpfile</i>, so multiple instances of <code>makedat</code> using the same <i>tmpfile</i> are prohibited. </p>
<p> The <code>-cidr</code> flag specifies that the key is an IP netblock in CIDR notation. This flag requires the Net::CIDR Perl module to be installed separately. Download Net::CIDR from m[blue]<code><a rel="nofollow" href="http://www.cpan.org">http://www.cpan.org</a></code>m[].</p>
<h2>BUGS</h2>
<p> There are historical reasons why database functions in maildrop are called gdbm functions. The initial implementation used GDBM functions exclusively. The ability to use the DB library instead of the GDBM library has been added later.</p>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
makedat blacklist /etc/mail/blacklist.tmp /etc/mail/blacklist.dat
</pre>
</dl>
<p> Takes blacklist, and creates /etc/mail/blacklist.dat, using /etc/mail/blacklist.tmp as a temporary file.</p>
<h2>SEE ALSO</h2>
<p> m[blue]<code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)m[]<font SIZE="-2">[1]</font>, m[blue]<code><a href="/docs/linux/man/5-maildropgdbm/">maildropgdbm</a></code>(5)m[]<font SIZE="-2">[2]</font>.</p>
<h2>AUTHOR</h2>
<p> <code>Sam Varshavchik</code></p>
<dl>
<dt>
<dd> Author</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> <code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildrop.html">http://www.courier-mta.org/maildrop/maildrop.html</a></dl>
<dt> 2.</p>
<dd> <code><a href="/docs/linux/man/5-maildropgdbm/">maildropgdbm</a></code>(5)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropgdbm.html">http://www.courier-mta.org/maildrop/maildropgdbm.html</a></dl>
</dl>
<h2>Index</h2>
