---
title: "dpkgchangelogparse(3)"
name: "dpkgchangelogparse"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgchangelogparse/"
---

Dpkg::Changelog::Parse - generic changelog parser for dpkg-parsechangelog 

<h2>Description</h2>This module provides a single function <i>changelog_parse()</i> which reproduces all the features of dpkg-parsechangelog.
<h3><font SIZE="-1">FUNCTIONS</font></h3><dl COMPACT><dt>my $fields = changelog_parse(%opt)
<dd>This function will parse a changelog. In list context, it return as many Dpkg::Control object as the parser did output. In scalar context, it will return only the first one. If the parser didn't return any data, it will return an empty in list context or undef on scalar context. If the parser failed, it will die. 

 The parsing itself is done by an external program (searched in the following list of directories: <tt>$opt</tt>{libdir}, <i>/usr/local/lib/dpkg/parsechangelog</i>, <i>/usr/lib/dpkg/parsechangelog</i>) That program is named according to the format that it's able to parse. By default it's either ``debian'' or the format name lookep up in the 40 last lines of the changelog itself (extracted with this perl regular expression ``\schangelog-format:\s+([0-9a-z]+)\W''). But it can be overridden with <tt>$opt</tt>{changelogformat}. The program expects the content of the changelog file on its standard input. 

 The changelog file that is parsed is <i>debian/changelog</i> by default but it can be overridden with <tt>$opt</tt>{file}. 

 All the other keys in <tt>%opt</tt> are forwarded as parameter to the external parser. If the key starts with ``-'', it's passed as is. If not, it's passed as ``--&lt;key&gt;''. If the value of the corresponding hash entry is defined, then it's passed as the parameter that follows.</dl><h2>Changes</h2><h3>Version 1.00</h3>Mark the module as public.
