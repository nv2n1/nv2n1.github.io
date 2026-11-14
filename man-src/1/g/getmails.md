---
title: "getmails(1)"
name: "getmails"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getmails/"
description: "getmails – wrapper for getmail to access multiple mailboxes"
---

<h2 class="name">NAME</h2>
<p> getmails &#8211; wrapper for getmail to access multiple mailboxes </p>
<h2>SYNOPSIS</h2>
<p> <code>getmails</code> [<code>-p</code>] [<i>OPTION</i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>getmails</code> is a wrapper script for <code>getmail </code> to retrieve messages with multiple independent configuration files <i>~/.getmail/config/*</i> instead of a single <i>~/.getmailrc</i> file. </p>
<p> The configuration file name can be any arbitrary names. It&#8217;s good idea to use the corresponding email address as its name since it is the most intuitive choice. For example <i>~/.getmail/config/foo [at] example.org .</i> </p>
<p> To disable operation for an email account temporary, rename its configuration file to the hidden file such as <i>~/.getmail/config/.foo [at] example.org .</i> Then, it is ignored as the configuration file. </p>
<p> For the robust operation, the editor generated files such as <i>~/.getmail/config/foo~</i> , <i>~/.getmail/config/#foo#</i> , <i>~/.getmail/config/foo.swp</i> , and <i>~/.getmail/config/foo.bak</i> are also ignored as the configuration file. </p>
<p> When there are multiple email configuration files, <code>getmails</code> retrieves mails sequentially. But adding an optional option <code>-p</code> before other options makes <code>getmails</code> to invoke <code>getmail</code> with each configuration file in parallel to retrieve mails. </p>
<p> The option provided as <i>OPTION</i> is passed to <code>getmail</code> as is. The use of the <code>-r</code> option is not a good idea. </p>
<p> The existence of <i>~/.getmail/stop </i> can prevent this wrapper script to execute <code>getmail</code>. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the getmail debian package if bugs are in this wrapper script.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2011-2017 Osamu Aoki<br />
 This is free software; see the file COPYING for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
