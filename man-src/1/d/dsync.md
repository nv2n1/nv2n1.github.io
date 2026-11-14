---
title: "dsync(1)"
name: "dsync"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dsync/"
description: "dsync – Dovecot’s mailbox synchronization utility"
---

<h2>NAME</h2>
<p> dsync &#8211; Dovecot&#8217;s mailbox synchronization utility</p>
<h2>SYNOPSIS</h2>
<p> <code>dsync</code> [<i>options</i>] <code>mirror&nbsp;<wbr></code><i>location2</i><br />
 <code>dsync</code> [<i>options</i>] <code>backup&nbsp;<wbr></code><i>location2</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dsync</code> is Dovecot&#8217;s mailbox synchronization utility. It can be used for several different use cases: Two-way synchronization of mailboxes in different servers (via <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1)), creating backups of mails to a remote server, and convert mailboxes from/to different mailbox formats. </p>
<p> The syncing is done as perfectly as possible: an IMAP or a POP3 client shouldn&#8217;t be able to notice any differences between the two mailboxes. Two-way syncing means that it&#8217;s safe to do any kind of modifications in both sides, and <code>dsync</code> will merge the changes without losing any changes done on either side. This is possible because <code>dsync</code> can access Dovecot&#8217;s index logs that keep track of changes. It&#8217;s of course possible to have conflicts during merging, these are resolved in a safe way. See the <code>dsync</code> design document for more information. </p>
<p> <code>dsync</code> uses the same configuration files as the rest of Dovecot (via doveconf binary). The entire configuration can be changed by giving -c parameter to another configuration file, or using -o parameter to override specific settings. When executing a remote <code>dsync</code> program it works the same way: it uses its own local configuration. </p>
<p> <code>dsync</code> can be run completely standalone. It doesn&#8217;t require any Dovecot server processes to be running, except when using -u parameter to do a userdb lookup from auth process. </p>
<p> <code>dsync</code> can currently sync only one user at a time. If you want to <code>dsync</code> all users, you&#8217;ll need to get a list of all users and execute <code>dsync</code> separately for each one. </p>
<p> Any errors are written to stderr.</p>
<h2>OPTIONS</h2>
<p> <code>dsync</code> recognizes the following command line options:</p>
<dl>
<dt><code>-c</code><i>&nbsp;<wbr>config-file</i></p>
<dd> read configuration from the given <i>config-file</i>. By default <i>/etc/dovecot/dovecot.conf</i> will be used. <code>-C&nbsp;<wbr></code><i>alt_char</i> Specifies an alternative mailbox name character. If source and destination mailbox formats are different, it&#8217;s possible that on one side there exists a mailbox name that isn&#8217;t valid for the other side. These invalid mailbox names are fixed by replacing such invalid characters with the given <i>alt_char</i>. The default is &#8216;<code>_</code>&#8216;.</p>
<dt><code>-D</code></p>
<dd> Activates debug messages and makes <code>dsync</code> more verbose.</p>
<dt><code>-f</code></p>
<dd> Makes <code>dsync</code> run in &quot;full sync&quot; mode rather than &quot;fast sync&quot; mode. In fast sync mode <code>dsync</code> might skip syncing a mailbox, if both locations had modified it equally many times (i.e. highest-modseqs were equal), but with different changes.</p>
<dt><code>-m&nbsp;<wbr></code><i>mailbox</i></p>
<dd> Specifies the <i>mailbox</i> that should be synchronized or from which mails should be converted. The default is to synchronize all respectively convert from all mailboxes.</p>
<dt><code>-o&nbsp;<wbr></code><i>setting</i><code>=</code><i>value</i></p>
<dd> Overrides the configuration <i>setting</i> from <i>/etc/dovecot/dovecot.conf</i> and from the userdb with the given <i>value</i>. In order to override multiple settings, the <code>-o</code> option may be specified multiple times.</p>
<dt><code>-R</code></p>
<dd> Reverse backup direction, so mails in <i>location2</i> are backed up to default mail location.</p>
<dt><code>-u&nbsp;<wbr></code><i>user</i></p>
<dd> Specifies that the userdb lookup for the given <i>user</i> should be done and used to set up the environment (uid, gid, home, etc.). By default the system user&#8217;s current environment will be used.</p>
<dt><code>-v</code></p>
<dd> Makes <code>dsync</code> more verbose.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>location2</i></p>
<dd> The first mail location is based on configuration (<i>mail_location</i> or <i>userdb</i> settings). It&#8217;s also possible to override it by giving <code>-o mail_location=</code><i>mail_location</i> setting. This parameter defines the other mail location that is used. </p>
<p> If the location is on local filesystem, you can use a regular mail_location, such as maildir:/backup/user/Maildir </p>
<p> If the location is on a remote server, <code>dsync</code> can ssh to it by giving <i>host</i> or <i>user [at] host</i> as the parameter. If user is specified, it&#8217;s given as <code>-u</code> parameter to <code>dsync</code>, not to ssh. The ssh username is always the default. </p>
<p> The final way to specify a location is to give a full command line or a path to a script that executes the <code>dsync</code>. For example: </p>
<pre>
ssh mailuser [at] host dsync -u user
</pre>
</dl>
<h2>COMMANDS</h2>
<p> <code>dsync</code> provides the following commands:</p>
<h3>mirror</h3>
<p> Does a two-way synchronization between two mail locations. Changes in both locations are synchronized to the other one, without losing any changes made by either of them. Any potential UID conflicts are resolved by giving them new UIDs.</p>
<h3>backup</h3>
<p> Backup mails from default mail location to <i>location2</i> (or vice versa, if <code>-R</code> parameter is given). No changes are ever done to the source location. Any changes done in destination are discarded.</p>
<h2>EXIT STATUS</h2>
<p> <code>dsync</code> will exit with one of the following values:</p>
<dl>
<dt><code>0</code></p>
<dd> Synchronization was done perfectly.</p>
<dt><code>2</code></p>
<dd> Synchronization was done without errors, but some changes couldn&#8217;t be done, so the mailboxes aren&#8217;t perfectly synchronized. Running dsync again usually fixes this. Typically this occurs for message modification sequences with newly created mailboxes. It can also occur if one of the mailboxes change during the syncing.</p>
<dt><code>1, &gt;2</code></p>
<dd> Synchronization failed.</dl>
<h2>EXAMPLE</h2>
<h3>MIRRORING</h3>
<p> Mirror mailboxes to a remote server. Any errors are written to stderr. </p>
<dl>
<dt>
<dd>
<pre>
<code>dsync -u username mirror username [at] example.com</code>
</pre>
</dl>
<p> If you need more complex parameters to ssh, you can use e.g.: </p>
<dl>
<dt>
<dd>
<pre>
<code>dsync -u username mirror ssh -i id_dsa.dovecot mailuser [at] example.com dsync -u username</code>
</pre>
</dl>
<h3>CONVERTING</h3>
<p> Assuming that the <i>mail_location</i> setting in <i>/etc/dovecot/conf.d/10-mail.conf</i> is set to: <code>mail_location = mdbox:~/mdbox</code>, a logged in system user may convert her/his mails from its Maildir in her/his home directory to the mdbox mailbox format. The user has to execute the command: </p>
<dl>
<dt>
<dd>
<pre>
<code>dsync mirror maildir:~/Maildir</code>
</pre>
</dl>
<p> If you want to do this without any downtime, you can do the conversion one user at a time. Initially:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Configuration uses <code>mail_location = maildir:~/Maildir</code></p>
<dt>&bull;</p>
<dd> Set up the possibility of doing per-user mail location using <i>userdb</i> extra fields.</dl>
</dl>
<p> Then for each user:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Run <i>dsync mirror</i> once to do the initial conversion.</p>
<dt>2.</p>
<dd> Run <i>dsync mirror</i> again, because the initial conversion could have taken a while and new changes could have occurred during it. This second time only applies changes, so it should be fast.</p>
<dt>3.</p>
<dd> Update mail extra field in userdb to <code>mdbox:~/mdbox</code>. If you&#8217;re using auth cache, you need to flush it.</p>
<dt>4.</p>
<dd> Wait for a few seconds and then kill the user&#8217;s all existing imap and pop3 sessions (that are still using maildir).</p>
<dt>5.</p>
<dd> Run <i>dsync mirror</i> once more to apply final changes that were possibly done. After this there should be no changes to Maildir, because the user&#8217;s mail location has been changed and all existing processes using it have been killed.</dl>
</dl>
<p> Once all users have been converted, you can set the default <i>mail_location</i> to mdbox and remove the per-user mail locations from <i>userdb</i>.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-kick/">doveadm-kick</a></code>(1), <code><a href="/docs/linux/man/1-doveconf/">doveconf</a></code>(1), <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1) </p>
<p> Additional resources:</p>
<dl>
<dt>dsync design</p>
<dd> <a rel="nofollow" href="http://wiki2.dovecot.org/Design/Dsync">http://wiki2.dovecot.org/Design/Dsync</a> </p>
</dl>
<h2>Index</h2>
