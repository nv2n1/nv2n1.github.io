---
title: "mutt(1)"
name: "mutt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mutt/"
description: "mutt – The Mutt Mail User Agent"
---

<h2 class="name">NAME</h2>
<p> mutt &#8211; The Mutt Mail User Agent </p>
<h2>SYNOPSIS</h2>
<p> <code>mutt</code> [-nRyzZ] [-e <i>cmd</i>] [-F <i>file</i>] [-m <i>type</i>] [-f <i>file</i>] </p>
<p> <code>mutt </code> [-Enx] [-e <i>cmd</i>] [-F <i>file</i>] [-H <i>file</i>] [-i <i>file</i>] [-s <i>subj</i>] [-b <i>addr</i>] [-c <i>addr</i>] [-a <i>file</i> [&#8230;] &#8211;] <i>addr|mailto_url</i> [&#8230;] </p>
<p> <code>mutt </code> [-nx] [-e <i>cmd</i>] [-F <i>file</i>] [-s <i>subj</i>] [-b <i>addr</i>] [-c <i>addr</i>] [-a <i>file</i> [&#8230;] &#8211;] <i>addr|mailto_url</i> [&#8230;] &lt; message </p>
<p> <code>mutt</code> [-n] [-e <i>cmd</i>] [-F <i>file</i>] -p </p>
<p> <code>mutt</code> [-n] [-e <i>cmd</i>] [-F <i>file</i>] -A <i>alias</i> </p>
<p> <code>mutt</code> [-n] [-e <i>cmd</i>] [-F <i>file</i>] -Q <i>query</i> </p>
<p> <code>mutt </code> -v[v] </p>
<p> <code>mutt </code> -D</p>
<h2>DESCRIPTION</h2>
<p> Mutt is a small but very powerful text based program for reading and sending electronic mail under unix operating systems, including support for color terminals, MIME, OpenPGP, and a threaded sorting mode. </p>
<p> <i>Note:</i> This manual page gives a brief overview of mutt&#8217;s command line options. You should find a copy of the full manual in /usr/share/doc/mutt, in text, HTML, and/or PDF format.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-A <i>alias</i></p>
<dd> An expanded version of the given alias is passed to stdout.</p>
<dt>-a <i>file</i> [&#8230;]</p>
<dd> Attach a file to your message using MIME. When attaching single or multiple files, separating filenames and recipient addresses with &quot;&#8211;&quot; is mandatory, e.g. <code>mutt -a image.jpg &#8212; addr1</code> or <code>mutt -a img.jpg *.png &#8212; addr1 addr2</code>. The -a option must be placed at the end of command line options.</p>
<dt>-b <i>address</i></p>
<dd> Specify a blind-carbon-copy (BCC) recipient</p>
<dt>-c <i>address</i></p>
<dd> Specify a carbon-copy (CC) recipient</p>
<dt>-d <i>level</i></p>
<dd> If mutt was compiled with +DEBUG log debugging output to ~/.muttdebug0. <i>Level</i> can range from 1-5 and effects verbosity. A value of 2 is recommended.</p>
<dt>-D</p>
<dd> Print the value of all configuration options to stdout.</p>
<dt>-E</p>
<dd> Causes the draft file specified by -H or include file specified by -i to be edited during message composition.</p>
<dt>-e <i>command</i></p>
<dd> Specify a configuration command to be run after processing of initialization files.</p>
<dt>-f <i>mailbox</i></p>
<dd> Specify which mailbox to load.</p>
<dt>-F <i>muttrc</i></p>
<dd> Specify an initialization file to read instead of ~/.muttrc</p>
<dt>-h</p>
<dd> Display help.</p>
<dt>-H <i>draft</i></p>
<dd> Specify a draft file which contains header and body to use to send a message.</p>
<dt>-i <i>include</i></p>
<dd> Specify a file to include into the body of a message.</p>
<dt>-m <i>type</i></p>
<dd> specify a default mailbox type for newly created folders.</p>
<dt>-n</p>
<dd> Causes Mutt to bypass the system configuration file.</p>
<dt>-p</p>
<dd> Resume a postponed message.</p>
<dt>-Q <i>query</i></p>
<dd> Query a configuration variables value. The query is executed after all configuration files have been parsed, and any commands given on the command line have been executed.</p>
<dt>-R</p>
<dd> Open a mailbox in <i>read-only</i> mode.</p>
<dt>-s <i>subject</i></p>
<dd> Specify the subject of the message.</p>
<dt>-v</p>
<dd> Display the Mutt version number and compile-time definitions.</p>
<dt>-vv</p>
<dd> Display license and copyright information.</p>
<dt>-x</p>
<dd> Emulate the mailx compose mode.</p>
<dt>-y</p>
<dd> Start Mutt with a listing of all mailboxes specified by the <i>mailboxes</i> command.</p>
<dt>-z</p>
<dd> When used with -f, causes Mutt not to start if there are no messages in the mailbox.</p>
<dt>-Z</p>
<dd> Causes Mutt to open the first mailbox specified by the <i>mailboxes</i> command which contains new mail.</p>
<dt>&#8212;</p>
<dd> Treat remaining arguments as <i>addr</i> even if they start with a dash. See also &quot;-a&quot; above.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>EDITOR</p>
<dd> Specifies the editor to use if VISUAL is unset.</p>
<dt>EMAIL</p>
<dd> The user&#8217;s e-mail address.</p>
<dt>HOME</p>
<dd> Full path of the user&#8217;s home directory.</p>
<dt>MAIL</p>
<dd> Full path of the user&#8217;s spool mailbox.</p>
<dt>MAILDIR</p>
<dd> Full path of the user&#8217;s spool mailbox if MAIL is unset. Commonly used when the spool mailbox is a <code>maildir (5)</code> folder.</p>
<dt>MAILCAPS</p>
<dd> Path to search for mailcap files.</p>
<dt>MM_NOASK</p>
<dd> If this variable is set, mailcap are always used without prompting first.</p>
<dt>PGPPATH</p>
<dd> Directory in which the user&#8217;s PGP public keyring can be found. When used with the original PGP program, mutt and <code>mutt_pgpring (1)</code> rely on this being set.</p>
<dt>TMPDIR</p>
<dd> Directory in which temporary files are created.</p>
<dt>REPLYTO</p>
<dd> Default Reply-To address.</p>
<dt>VISUAL</p>
<dd> Specifies the editor to use when composing messages.</dl>
<h2>FILES</h2>
<dl>
<dt>~/.muttrc or ~/.mutt/muttrc</p>
<dd> User configuration file.</p>
<dt>/etc/Muttrc</p>
<dd> System-wide configuration file.</p>
<dt>/tmp/muttXXXXXX</p>
<dd> Temporary files created by Mutt.</p>
<dt>~/.mailcap</p>
<dd> User definition for handling non-text MIME types.</p>
<dt>/etc/mailcap</p>
<dd> System definition for handling non-text MIME types.</p>
<dt>~/.mime.types</p>
<dd> User&#8217;s personal mapping between MIME types and file extensions.</p>
<dt>/etc/mime.types</p>
<dd> System mapping between MIME types and file extensions.</p>
<dt>/usr/bin/mutt_dotlock</p>
<dd> The privileged dotlocking program.</p>
<dt>/usr/share/doc/mutt/manual.txt.gz</p>
<dd> The Mutt manual.</dl>
<h2>BUGS</h2>
<p> None. Mutts have fleas, not bugs.</p>
<h2>FLEAS</h2>
<p> Suspend/resume while editing a file with an external editor does not work under SunOS 4.x if you use the curses lib in /usr/5lib. It <i>does</i> work with the S-Lang library, however. </p>
<p> Resizing the screen while using an external pager causes Mutt to go haywire on some systems. </p>
<p> Suspend/resume does not work under Ultrix. </p>
<p> The help line for the index menu is not updated if you change the bindings for one of the functions listed while Mutt is running. </p>
<p> For a more up-to-date list of bugs, errm, fleas, please visit the mutt project&#8217;s bug tracking system under <a rel="nofollow" href="https://gitlab.com/muttmua/mutt/issues.">https://gitlab.com/muttmua/mutt/issues.</a></p>
<h2>NO WARRANTIES</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curses/">curses</a></code>(3), <code><a href="/docs/linux/man/5-mailcap/">mailcap</a></code>(5), <code><a href="/docs/linux/man/5-maildir/">maildir</a></code>(5), <code><a href="/docs/linux/man/5-mbox/">mbox</a></code>(5), <code><a href="/docs/linux/man/1-mutt_dotlock/">mutt_dotlock</a></code>(1), <code><a href="/docs/linux/man/5-muttrc/">muttrc</a></code>(5), <code><a href="/docs/linux/man/3-ncurses/">ncurses</a></code>(3), <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1), <code><a href="/docs/linux/man/1-smail/">smail</a></code>(1). </p>
<p> Mutt Home Page: <a rel="nofollow" href="http://www.mutt.org/">http://www.mutt.org/</a> </p>
<p> The Mutt manual</p>
<h2>AUTHOR</h2>
<p> Michael Elkins, and others. Use &lt;mutt-dev [at] mutt.org&gt; to contact the developers. </p>
<h2>Index</h2>
