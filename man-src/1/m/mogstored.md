---
title: "mogstored(1)"
name: "mogstored"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mogstored/"
---

<h2 class="name">NAME</h2>
 

 mogstored -- MogileFS storage daemon 

<h2>USAGE</h2>

 This is the MogileFS storage daemon, which is just an <font SIZE="-1">HTTP</font> server that supports <font SIZE="-1">PUT</font>, <font SIZE="-1">DELETE</font>, etc. It's actually a wrapper around Perlbal, doing all the proper Perlbal config for you. 

 In addition, it monitors disk usage, I/O activity, etc, which are checked from the MogileFS tracker.

<h2>AUTHORS</h2>

 Brad Fitzpatrick &lt;brad [at] danga.com&gt; 

 Mark Smith &lt;junior [at] danga.com&gt; 

 Jonathan Steinert &lt;jsteinert [at] sixapart.com&gt;

<h2>ENVIRONMENT</h2>

<dl>
<dt><font SIZE="-1">PERLBAL_XS_HEADERS</font>
<dd> If defined and 0, Perlbal::XS::HTTPHeaders will not be used, if present. Otherwise, it will be enabled by default, if installed and loadable.</dl>

<h2>COPYRIGHT</h2>

 <pre>
 Copyright 2004, Danga Interactive
 Copyright 2005-2006, Six Apart Ltd.
</pre>

<h2>LICENSE</h2>

 Same terms as Perl itself. Artistic/GPLv2, at your choosing.

<h2>SEE ALSO</h2>

 MogileFS::Overview --- high level overview of MogileFS 

 mogilefsd --- MogileFS daemon 

 &lt;<a rel="nofollow" HREF="http://danga.com/mogilefs/">http://danga.com/mogilefs/</a>&gt; 

<h2>Index</h2>


