---
title: "nntpsend(5)"
name: "nntpsend"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nntpsend/"
---

nntpsend.ctl - list of sites to feed via nntpsend

<h2>Description</h2>

The file <i>&lt;pathetc in inn.conf&gt;/nntpsend.ctl</i> specifies the default list of sites to be fed by <i><a HREF="/docs/linux/man/8-nntpsend/">nntpsend</a></i>(8). 

 Comments begin with a number sign (``#'') and continue through the end of the line. Blank lines and comments are ignored. All other lines should consist of four fields separated by a colon. 

 The first field is the name of the site as specified in the <i>newsfeeds</i> file. 

 The second field should be the hostname or IP address of the remote site. 

 The third field, if non-empty, specifies the default head truncation size of site's batchfile. If this field is empty, no truncation is performed. This field may be of the form ``maxsize-truncsize'', in which case it is passed to <i>shrinkfile</i> as ``-m maxsize -s truncsize''; otherwise it is of the form ``truncsize'', in which case it is passed as ``-s truncsize''. 

 The fourth field specifies some default flags passed to <i><a HREF="/docs/linux/man/8-innxmit/">innxmit</a></i>(8). The flag ``-a'' is always given to <i>innxmit</i> and need not appear here. If no ``-t timeout'' flag is given in this field or on the <i>nntpsend</i> command line, ``-t 180'' will be given to <i>innxmit</i>.

<h2>History</h2>

Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; for InterNetNews. This is revision 5909, dated 2002-12-03.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-innxmit/">innxmit</a>(8), <a HREF="/docs/linux/man/5-newsfeeds/">newsfeeds</a>(5), <a HREF="/docs/linux/man/8-nntpsend/">nntpsend</a>(8), <a HREF="/docs/linux/man/1-trunc/">trunc</a>(1). 
