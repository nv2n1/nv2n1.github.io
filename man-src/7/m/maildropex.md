---
title: "maildropex(7)"
name: "maildropex"
section: "7"
letter: "m"
url: "/docs/linux/man/7-maildropex/"
description: "maildropex – maildrop filtering language examples"
---

<p>maildropex &#8211; maildrop filtering language examples</p>
<h2>Synopsis</h2>
<p>$HOME/.mailfilter, $HOME/.mailfilters/*</p>
<h2>Description</h2>
<p>If $HOME/.mailfilter exists, filtering instructions in this file will be carried out prior to delivering the message. The filtering instructions may instruct <code>maildrop</code> to discard the message, save the message in a different mailbox, or forward the message to another address. If $HOME/.mailfilter does not exist, or does not provide explicit delivery instructions, <code>maildrop</code> delivers the message to the user&#8217;s system mailbox. </p>
<p> The files in $HOME/.mailfilters are used when <code>maildrop</code> is invoked in embedded mode.</p>
<h2>Examples</h2>
<p>Take all mail that&#8217;s sent to the &#8216;auto&#8217; mailing list, and save it in Mail/auto. The &#8216;auto&#8217; mailing list software adds a &quot;Delivered-To: auto [at] domain.com&quot; header to all messages:</p>
<dl>
<dd>
<pre>if (/^Delivered-To: *auto [at] domain\.com$/)
 to Mail/auto</pre>
</dl>
<p> After the <code>to</code> command delivers the message, <code>maildrop</code> automatically stops filtering and terminates without executing the subsequent instructions in the filter file. Take all mail from &lt;boss [at] domain.com&gt; about the current project status, save it in Mail/project, then forward a copy to John: </p>
<pre><code>if (/ ^From
    : *boss[at] domain\.com /
          &amp;&amp; / ^Subject
    :.*[:wbreak:] project status
         [:wbreak:] /) {
    cc &quot;!john&quot; to Mail / project
}</code></pre>
<p> Note that it is necessary to use a backslash in order to continue the <code>if</code> statement on the next line. Keep copies of the last 50 messages that you received in the maildir directory &#8216;backup&#8217;. NOTE: &#8216;backup&#8217; must be a maildir directory, not a mailbox. You can create a maildir using the <code>maildirmake</code> command.</p>
<dl>
<dd>
<pre>cc backup
`cd backup/new &amp;&amp; rm -f dummy \`ls -t | sed -e 1,50d\``</pre>
</dl>
<p> Put this at the beginning of your filter file, before any other filtering instructions. This is a good idea to have when you are learning <code>maildrop</code>. If you make a mistake and accidentally delete a message, you can recover it from the backup/new subdirectory. Save messages that are at least 100 lines long (approximately) into Mail/IN.Large::</p>
<dl>
<dd>
<pre> if ( $LINES &gt; 100 )
 to Mail/IN.Large</pre>
</dl>
<p> Send messages from the auto mailing list to the program &#8216;archive&#8217;, using a lock file to make sure that only one instance of the archive program will be running at the same time: if (/ ^Delivered &#8211; To<br />
    : *auto [at] domain\.com$ /)<br />
    dotlock &quot;auto.lock&quot;<br />
    {</p>
<p>        to &quot;|archive&quot;<br />
    } Check if the Message-ID: header in the message is identical to the same header that was recently seen. Discard the message if it is, otherwise continue to filter the message:</p>
<dl>
<dd>
<pre>`reformail -D 8000 duplicate.cache`
if ( $RETURNCODE == 0 )
 exit</pre>
</dl>
<p> The m[blue]<code>reformail</code>m[]<font SIZE="-2">[1]</font> command maintains a list of recently seen Message-IDs in the file duplicate.cache.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Unlike a similar feature in the <code>formail</code> command, m[blue]<code>reformail</code>m[]<font SIZE="-2">[1]</font> takes care of locking the file, so it&#8217;s not necessary to implement your own locking mechanism for this option.  Here&#8217;s a more complicated example. This fragment is intended to go right after the message has been filtered according to your regular rules, and just before the message should be saved in your mailbox: cc $DEFAULT<br />
        xfilter &quot;reformail -r -t&quot; /<br />
    ^To :.*/<br />
    getaddr($MATCH) = ~ / ^ .*/<br />
    ;</p>
<p>MATCH = tolower($MATCH)<br />
    flock &quot;vacation.lock&quot;<br />
{<br />
    `fgrep &#8211; iqx &quot;$MATCH&quot; vacation.lst 2 &gt; / dev / null ||<br />
    {<br />
        echo &quot;$MATCH&quot; &gt;&gt; vacation.lst;<br />
        exit 1;<br />
    }<br />
    `<br />
}<br />
if ($RETURNCODE == 0)<br />
exit<br />
    to &quot;| ( cat &#8211; ; echo &#8221;; cat vacation.msg) | $SENDMAIL&quot; This code maintains a list of everyone who sent you mail in the file called vacation.lst. When a message is received from anyone that is not already on the list, the address is added to the list, and the contents of the file vacation.msg are mailed back to the sender. This is intended to reply notify people that you will not be answering mail for a short period of time. The first statement saves the original message in your regular mailbox. Then, m[blue]<code>xfilter</code>m[]<font SIZE="-2">[2]</font> is used to generate an autoreply header to the sender. The To: header in the autoreply &#8211; which was the sender of the original message &#8211; is extracted, and the m[blue]<code>getaddr</code>m[]<font SIZE="-2">[3]</font> function is used to strip the person&#8217;s name, leaving the address only. The file vacation.lst is checked, using a lock file to guarantee atomic access and update (overkill, probably). Note that the backslashes are required. If the address is already in the file, <code>maildrop</code> exits, otherwise the contents of vacation.msg are appended to the autoreply header, and mailed out.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 An easier to make a vacation script is with m[blue]<code><a href="/docs/linux/man/1-mailbot/">mailbot</a></code>(1)m[]<font SIZE="-2">[4]</font>.  Here&#8217;s a version of the vacation script that uses a GDBM database file instead. The difference between this script and the previous script is that the previous script will send a vacation message to a given E-mail address only once. The following script will store the time that the vacation message was sent in the GDBM file. If it&#8217;s been at least a week since the vacation message has been sent to the given address, another vacation message will be sent. Even though a GDBM database file is used, locking is still necessary because the GDBM library does not allow more than one process to open the same database file for writing: </p>
<pre><code>cc $DEFAULT
        xfilter &quot;reformail -r -t&quot; /
    ^To :.*/
    getaddr($MATCH) = ~ / ^ .*/
    ;
MATCH = tolower($MATCH)
    flock &quot;vacation.lock&quot;
{
    current_time = time;
    if (gdbmopen(&quot;vacation.dat&quot;, &quot;C&quot;) == 0) {
        if ((prev_time = gdbmfetch($MATCH)) ne &quot;&quot; &amp;&amp;
            $prev_time &gt;= $current_time - 60 * 60 * 24 * 7) {
            exit
        }
        gdbmstore($MATCH, $current_time)
            gdbmclose
    }
}
to &quot;| ( cat - ; echo ''; cat vacation.msg) | $SENDMAIL&quot;</code></pre>
<p> This script requires that <code>maildrop</code> must be compiled with GDBM support enabled, which is done by default if GDBM libraries are present. After you return from vacation, you can use a simple Perl script to obtain a list of everyone who sent you mail (of course, that can also be determined by examining your mailbox).</p>
<h2>See Also</h2>
<p>m[blue]<code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)m[]<font SIZE="-2">[5]</font>, m[blue]<code><a href="/docs/linux/man/7-maildropfilter/">maildropfilter</a></code>(7)m[]<font SIZE="-2">[6]</font>, m[blue]<code><a href="/docs/linux/man/1-reformail/">reformail</a></code>(1)m[]<font SIZE="-2">[1]</font>, m[blue]<code><a href="/docs/linux/man/1-mailbot/">mailbot</a></code>(1)m[]<font SIZE="-2">[4]</font>, <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>reformail</p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org/maildrop/reformail.html">http://www.courier-mta.org/maildrop/reformail.html</a></dl>
<dt> 2.</p>
<dd><code>xfilter</code></p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#xfilter">http://www.courier-mta.org/maildrop/maildropfilter.html#xfilter</a></dl>
<dt> 3.</p>
<dd><code>getaddr</code></p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#getaddr">http://www.courier-mta.org/maildrop/maildropfilter.html#getaddr</a></dl>
<dt> 4.</p>
<dd><code><a href="/docs/linux/man/1-mailbot/">mailbot</a></code>(1)</p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org/maildrop/mailbot.html">http://www.courier-mta.org/maildrop/mailbot.html</a></dl>
<dt> 5.</p>
<dd><code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)</p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildrop.html">http://www.courier-mta.org/maildrop/maildrop.html</a></dl>
<dt> 6.</p>
<dd><code><a href="/docs/linux/man/7-maildropfilter/">maildropfilter</a></code>(7)</p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html">http://www.courier-mta.org/maildrop/maildropfilter.html</a></dl>
