---

title: "gnubiff(1)"
name: "gnubiff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnubiff/"
description: "gnubiff – a mail notification program supporting GTK+ and GNOME"
---

<h2>NAME</h2>
<p> gnubiff &#8211; a mail notification program supporting GTK+ and GNOME</p>
<p> <code>gnubiff</code> [<i>options</i>]</p>
<p> gnubiff is a mail notification program that checks for mail, displays headers when new mail has arrived and allow to read first lines of new messages. It relies on the GNOME and GTK libraries but can be compiled and used with or without GNOME support. Supported protocols are pop3, apop, imap4, mh, qmail and mailfile. Furthermore, gnubiff is fully configurable with a lot of options like polltime, poptime, sounds, mail reader, mailbox names, etc. and can also filter spam. Note that gnubiff is not a mail reader even if it offers the possibility of reading very first lines of new messages. If you send some requests for specific features to be implemented, keep that in mind!</p>
<h2>OPTIONS</h2>
<p> gnubiff accepts the following command line options:</p>
<dl>
<dt><code>-c </code><i>filename,</i><code> &#8211;config </code><i>filename</i></dt>
<dd> Use the specified file as configuration file (default is ~/.gnubiffrc)</dd>
<dt><code>-n, &#8211;noconfigure</code></dt>
<dd> Skip the configure process</dd>
<dt><code>&#8211;nogui</code></dt>
<dd> Start gnubiff without GUI</dd>
<dt><code>&#8211;systemtray</code></dt>
<dd> Start gnubiff in the system tray</dd>
<dt><code>-?, &#8211;help</code></dt>
<dd> Show summary of options</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Print version information</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.gnubiffrc</i></dt>
<dd> user specific options file</dd></dl>
<h2>SEE ALSO</h2>
<p> More documentation about gnubiff can be found in the info pages with the command <code>info gnubiff</code></p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHORS</h2>
<p> gnubiff was developed by Nicolas Rougier &lt;Nicolas.Rougier [at] loria.fr&gt; and is currently maintained by Robert Sowada &lt;sowadart [at] gmx.de&gt;. This manpage was written by Roland Stigge &lt;stigge [at] antcom.de&gt; for Debian. It can be used elsewhere, of course. </p>
