---
title: "webcheckout(1)"
name: "webcheckout"
section: "1"
letter: "w"
url: "/docs/linux/man/1-webcheckout/"
description: "webcheckout – check out repositories referenced on a web page"
---

<h2 class="name">NAME</h2>
<p> webcheckout &#8211; check out repositories referenced on a web page </p>
<h2>SYNOPSIS</h2>
<p> <code>webcheckout</code> [options] url [destdir]</p>
<h2>DESCRIPTION</h2>
<p> <code>webcheckout</code> downloads an url and parses it, looking for version control repositories referenced by the page. It checks out each repository into a subdirectory of the current directory, using whatever <font SIZE="-1">VCS</font> program is appropriate for that repository (git, svn, etc). </p>
<p> The information about the repositories is embedded in the web page using the rel=vcs-* microformat, which is documented at &lt;<a rel="nofollow" href="http://kitenet.net/~joey/rfc/rel-vcs/">http://kitenet.net/~joey/rfc/rel-vcs/</a>&gt;. </p>
<p> If the optional destdir parameter is specified, <font SIZE="-1">VCS</font> programs will be asked to check out repositories into that directory. If there are multiple repositories to check out, each will be checked out into a separate subdirectory of the destdir.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-a, &#8211;auth</p>
<dd> Prefer authenticated repositories. By default, webcheckout will use anonymous repositories when possible. If you have an account that allows you to use authenticated repositories, you might want to use this option.</p>
<dt>&#8211;no-act, -n</p>
<dd> Do not actually check anything out, just print out the commands that would be run to check out the repositories.</p>
<dt>&#8211;quiet, -q</p>
<dd> Quiet mode. Do not print out the commands being run. (The <font SIZE="-1">VCS</font> commands may still be noisy however.)</dl>
<h2>PREREQUISITES</h2>
<p> To use this program you will need lots of <font SIZE="-1">VCS</font> programs installed, obviously. It also depends on the perl <font SIZE="-1">LWP</font> and HTML::Parser modules. </p>
<p> If the perl <font SIZE="-1">URI</font> module is installed, webcheckout can heuristically guess what you mean by partial URLs, such as &#8220;kitenet.net/~joey&#8221;&#8217;</p>
<h2>AUTHOR</h2>
<p> Copyright 2009 Joey Hess &lt;joey [at] kitenet.net&gt; </p>
<p> Licensed under the <font SIZE="-1">GNU GPL</font> version 2 or higher. </p>
<p> This program is included in myrepos &lt;<a rel="nofollow" href="http://myrepos.branchable.com/">http://myrepos.branchable.com/</a>&gt; </p>
<h2>Index</h2>
