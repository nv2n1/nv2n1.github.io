---
title: "did(1)"
name: "did"
section: "1"
letter: "d"
url: "/docs/linux/man/1-did/"
description: "did – What did you do last week, month, year?"
---

<h2>NAME</h2>
<p> did &#8211; What did you do last week, month, year?</p>
<h2>DESCRIPTION</h2>
<p> Comfortably gather status report data (e.g. list of committed changes) for given week, month, quarter, year or selected date range. By default all available stats for this week are reported.</p>
<h2>SYNOPSIS</h2>
<p> Usage is straightforward: </p>
<pre><code>
did[this | last][week | month | quarter | year][opts]
</code></pre>
<h2>EXAMPLES</h2>
<p> Gather all stats for current week: </p>
<pre>
did
</pre>
<p> Show me all stats for today/yesterday: </p>
<pre>
did today
did yesterday
</pre>
<p> Gather stats for the last month: </p>
<pre>
did last month
</pre>
<p> See <code>did &#8211;help</code> for complete list of available stats.</p>
<h2>OPTIONS</h2>
<p> The list of available options depends on which plugins are configured. Here&#8217;s the list of general options which are not related to any plugin:</p>
<h3>Select</h3>
<p> At least one email address needs to be provided on command line unless defined in the config file. Use the complete email address format <code>Name Surname &lt;email [at] example.org&gt;</code> to display full name in the report output. For date values <code>today</code> and <code>yesterday</code> can be used instead of the full date format.</p>
<dl>
<dt><code>&#8211;email=</code><i>EMAILS</i></p>
<dd> User email address(es)</p>
<dt><code>&#8211;since=</code><i>SINCE</i></p>
<dd> Start date in the YYYY-MM-DD format</p>
<dt><code>&#8211;until=</code><i>UNTIL</i></p>
<dd> End date in the YYYY-MM-DD format</dl>
<h3>Format</h3>
<p> The default output is plain text of maximum width 79 characters. This can adjusted using the <code>&#8211;width</code> parameter. To disable shortening altogether use <code>&#8211;width=0</code>. The default width value can be saved in the config file as well. Use <code>&#8211;format=wiki</code> to enable simple MoinMoin wiki syntax. For stats which support them, <code>&#8211;brief</code> and <code>&#8211;verbose</code> can be used to specify a different level of detail to be shown.</p>
<dl>
<dt><code>&#8211;format=</code><i>FMT</i></p>
<dd> Output style, possible values: text (default) or wiki</p>
<dt><code>&#8211;width=</code><i>WIDTH</i></p>
<dd> Maximum width of the report output (default: 79)</p>
<dt><code>&#8211;brief</code></p>
<dd> Show brief summary only, do not list individual items</p>
<dt><code>&#8211;verbose</code></p>
<dd> Include more details (like modified git directories)</dl>
<h3>Utils</h3>
<p> Multiple emails can be used to put together a team report or to gather stats for all of your email aliases. For this use case <code>&#8211;total</code> and <code>&#8211;merge</code> can be used to append the overall summary at the end or merge all results into a single report respectively. Use <code>&#8211;debug</code> or set the environment variable <code>DEBUG</code> to 1 through 5 to set the desired level of debugging.</p>
<dl>
<dt><code>&#8211;config=</code><i>FILE</i></p>
<dd> Use alternate configuration file (default: &#8216;config&#8217;)</p>
<dt><code>&#8211;total</code></p>
<dd> Append total stats after listing individual users</p>
<dt><code>&#8211;merge</code></p>
<dd> Merge stats of all users into a single report</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn on debugging output, do not catch exceptions </p>
<p> See <code>did &#8211;help</code> for complete list of available options.</dl>
<h2>INSTALL</h2>
<p> Install directly from Fedora/Copr repository: </p>
<pre>
yum install did
</pre>
<p> or use PIP (sudo required if not in a virtualenv): </p>
<pre>
pip install did
</pre>
<p> To build and execute in a docker container, run: </p>
<pre>
make run_docker
</pre>
<p> See documentation for more details about installation options.</p>
<h2>CONFIG</h2>
<p> The config file <code>~/.did/config</code> is used to store both general settings and configuration of individual reports: </p>
<pre><code>
[general] email = "Petr Šplíchal" &lt; psplicha[at] redhat.com &gt;
                  width = 79
                      [header] type = header
                          highlights = Highlights
                              joy = Joy of the week;-)
[tools]
type = git
did = /home/psss/git/did
[tests]
type = git
tests = /home/psss/git/tests/*
[trac]
type = trac
prefix = TT
url = https://some.trac.com/trac/project/rpc
[bz]
type = bugzilla
prefix = BZ
url = https://bugzilla.redhat.com/xmlrpc.cgi
[footer]
type = footer
next = Plans, thoughts, ideas...
status = Status: Green | Yellow | Orange | Red
</code></pre>
<p> See plugin documentation for more detailed description of options available for particular plugin. You can also check python module documentation directly, e.g. <code>pydoc did.plugins.git</code> or use the example config provided in the package and web documentation.</p>
<h2>LINKS</h2>
<p> Git: <i><a rel="nofollow" href="https://github.com/psss/did">https://github.com/psss/did</a></i> </p>
<p> Docs: <i><a rel="nofollow" href="http://did.readthedocs.org">http://did.readthedocs.org</a></i> </p>
<p> Issues: <i><a rel="nofollow" href="https://github.com/psss/did/issues">https://github.com/psss/did/issues</a></i> </p>
<p> Releases: <i><a rel="nofollow" href="https://github.com/psss/did/releases">https://github.com/psss/did/releases</a></i> </p>
<p> Copr: <i><a rel="nofollow" href="http://copr.fedoraproject.org/coprs/psss/did">http://copr.fedoraproject.org/coprs/psss/did</a></i> </p>
<p> PIP: <i><a rel="nofollow" href="https://pypi.python.org/pypi/did">https://pypi.python.org/pypi/did</a></i></p>
<h2>AUTHORS</h2>
<p> Petr Šplíchal, Karel Šrot, Lukáš Zachar, Matěj Cepl, Ondřej Pták, Chris Ward, Tomáš Hofman, Martin Mágr, Stanislav Kozina, Paul Belanger, Eduard Trott, Martin Frodl and Randy Barlow.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2015 Red Hat, Inc. All rights reserved. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
