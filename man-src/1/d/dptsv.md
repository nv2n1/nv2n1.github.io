---
title: "dptsv(1)"
name: "dptsv"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dptsv/"
description: "dptsv – mutual converter between TSV and QDBM Depot database"
---

<h2 class="name">NAME</h2>
<p> dptsv &#8211; mutual converter between TSV and QDBM Depot database </p>
<h2>SYNOPSIS</h2>
<p> <code>dptsv import</code> [-bnum <i>num</i>] [-bin] <i>name</i><br />
 <code>dptsv export</code> [-bin] <i>name</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>dptsv</code> commands. </p>
<p> The command <i>dptsv</i> features mutual conversion between a database of Depot and a TSV text. This command is useful when data exchange with another version of QDBM or another DBM, or when data exchange between systems which have different byte orders. This command is used in the above format. <i>name</i> specifies a database name. </p>
<p> The subcommand <code>export</code> reads TSV data from the standard input. If a key overlaps, the latter is adopted. <code>-bnum</code> specifies the number of the elements of the bucket array. The subcommand <code>import</code> writes TSV data to the standard output.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the file:///usr/share/doc/qdbm-doc/spex.html#depotcli.</p>
<dl>
<dt><code>-bnum num</code></p>
<dd> specify the number of the elements of the bucket array.</p>
<dt><code>-bin</code></p>
<dd> treat records as Base64 format.</dl>
<h2>EXAMPLES</h2>
<p> For example, to make a database to search `/etc/password&#8217; by a user name, perform the following command.<br />
 <code> cat /etc/passwd | tr &#8216;:&#8217; &#8216; &#8216; | dptsv import casket</code> </p>
<p> Thus, to retrieve the information of a user `mikio&#8217;, perform the following command.<br />
 <code> dpmgr get casket mikio</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-qdbm/">qdbm</a></code>(3), <code><a href="/docs/linux/man/1-dpmgr/">dpmgr</a></code>(1), <code><a href="/docs/linux/man/3-dpopen/">dpopen</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
