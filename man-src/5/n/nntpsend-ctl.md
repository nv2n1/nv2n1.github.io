---
title: "nntpsend-ctl(5)"
name: "nntpsend-ctl"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nntpsend-ctl/"
description: "nntpsend.ctl – List of sites to feed via nntpsend"
---

<p>nntpsend.ctl &#8211; List of sites to feed via nntpsend</p>
<h2>Description</h2>
<p>The file <i>pathetc</i>/nntpsend.ctl specifies the default list of sites to be fed by <code>nntpsend</code>. Comments begin with a number sign (<tt>&quot;#&quot;</tt>) and continue through the end of the line. Blank lines and comments are ignored. All other lines should consist of four fields separated by a colon. </p>
<p> The first field is the name of the site as specified in the <i>newsfeeds</i> file. </p>
<p> The second field should be the hostname or <font SIZE="-1">IP</font> address of the remote site. </p>
<p> The third field, if non-empty, specifies the default head truncation size of the batch file. If this field is empty, no truncation is performed. This field may be of the form <tt>&quot;</tt>maxsize<tt>-</tt>truncsize<tt>&quot;</tt>, in which case it is passed to <code>shrinkfile</code> as <tt>&quot;-m </tt>maxsize<tt> -s </tt>truncsize<tt>&quot;</tt>; otherwise it is of the form <tt>&quot;</tt>truncsize<tt>&quot;</tt>, in which case it is passed as <tt>&quot;-s </tt>truncsize<tt>&quot;</tt>. </p>
<p> The fourth field specifies some default flags passed to <code>innxmit</code>. Note that the flag <code>-a</code> is always given to <code>innxmit</code> and need not appear here. If no <code>-t</code> flag is given in this field or on the <code>nntpsend</code> command line, <tt>&quot;-t 180&quot;</tt> will be given to <code>innxmit</code>. </p>
<p> See <i><a href="/docs/linux/man/8-nntpsend/">nntpsend</a></i>(8) for an example of <i>nntpsend.ctl</i> config file.</p>
<h2>History</h2>
<p>Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> nntpsend.ctl.pod 9072 2010-05-31 17:42:04Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-innxmit/">innxmit</a></i>(1), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-nntpsend/">nntpsend</a></i>(8), <i><a href="/docs/linux/man/1-shrinkfile/">shrinkfile</a></i>(1). </p>
