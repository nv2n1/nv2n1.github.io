---
title: "procmailex(5)"
name: "procmailex"
section: "5"
letter: "p"
url: "/docs/linux/man/5-procmailex/"
description: "procmailex – procmail rcfile examples"
---

<p>procmailex &#8211; procmail rcfile examples</p>
<h2>Synopsis</h2>
<p><code>$HOME/.procmailrc examples</code></p>
<h2>Description</h2>
<p>For a description of the rcfile format see <code><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></code>(5). </p>
<p> The weighted scoring technique is described in detail in the <code><a href="/docs/linux/man/5-procmailsc/">procmailsc</a></code>(5) man page. </p>
<p> This man page shows several example recipes. For examples of complete rcfiles you can check the NOTES section in <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1), or look at the example rcfiles in /usr/share/doc/procmail/examples.</p>
<h2>Examples</h2>
<p>Sort out all mail coming from the scuba-dive mailing list into the mailfolder scubafile (uses the locallockfile scubafile.lock). </p>
<pre><dl><dt><dd>:0:
* ^TOscuba
scubafile
</dl></pre>
<p>Forward all mail from peter about compilers to william (and keep a copy of it here in petcompil). </p>
<pre><dl><dt><dd>:0
* ^From.*peter
* ^Subject:.*compilers
{
 :0 c
 ! william [at] somewhere.edu
 :0
 petcompil
}
</dl></pre>
<p>An equivalent solution that accomplishes the same: </p>
<pre><dl><dt><dd>:0 c
* ^From.*peter
* ^Subject:.*compilers
! william [at] somewhere.edu
 :0 A
 petcompil
</dl></pre>
<p>An equivalent, but slightly slower solution that accomplishes the same: </p>
<pre><dl><dt><dd>:0 c
* ^From.*peter
* ^Subject:.*compilers
! william [at] somewhere.edu
:0
* ^From.*peter
* ^Subject:.*compilers
petcompil
</dl></pre>
<p>If you are fairly new to procmail and plan to experiment a little bit it often helps to have a <i>safety net</i> of some sort. Inserting the following two recipes above all other recipes will make sure that of all arriving mail always the last 32 messages will be preserved. In order for it to work as intended, you have to create a directory named `backup&#8217; in $MAILDIR prior to inserting these two recipes. </p>
<pre><dl><dt><dd>:0 c
backup
:0 ic
| cd backup &amp;&amp; rm -f dummy `ls -t msg.* | sed -e 1,32d`
</dl></pre>
<p>If your system doesn&#8217;t generate or generates incorrect leading `From &#8216; lines on every mail, you can fix this by calling up procmail with the -f- option. To fix the same problem by different means, you could have inserted the following two recipes above all other recipes in your rcfile. They will filter the header of any mail through formail which will strip any leading `From &#8216;, and automatically regenerates it subsequently. </p>
<pre><dl><dt><dd>:0 fhw
| formail -I &quot;From &quot; -a &quot;From &quot;
</dl></pre>
<p>Add the headers of all messages that didn&#8217;t come from the postmaster to your private header collection (for statistics or mail debugging); and use the lockfile `headc.lock&#8217;. In order to make sure the lockfile is not removed until the pipe has finished, you have to specify option `w&#8217;; otherwise the lockfile would be removed as soon as the pipe has accepted the mail. </p>
<pre><dl><dt><dd>:0 hwc:
* !^FROM_MAILER
| uncompress headc.Z; cat &gt;&gt;headc; compress headc
</dl></pre>
<p>Or, if you would use the more efficient gzip instead of compress: </p>
<pre><dl><dt><dd>:0 hwc:
* !^FROM_MAILER
| gzip &gt;&gt;headc.gz
</dl></pre>
<p>Forward all mails shorter than 1000 bytes to my home address (no lockfile needed on this recipe). </p>
<pre><dl><dt><dd>:0
* &lt; 1000
! myname [at] home
</dl></pre>
<p>Split up incoming digests from the surfing mailing list into their individual messages, and store them into surfing, using surfing.lock as the locallockfile. </p>
<pre><dl><dt><dd>:0:
* ^Subject:.*surfing.*Digest
| formail +1 -ds &gt;&gt;surfing
</dl></pre>
<p>Store everything coming from the postmaster or mailer-daemon (like bounced mail) into the file postm, using postm.lock as the locallockfile. </p>
<pre><dl><dt><dd>:0:
* ^FROM_MAILER
postm
</dl></pre>
<p>A simple autoreply recipe. It makes sure that neither mail from any daemon (like bouncing mail or mail from mailing-lists), nor autoreplies coming from yourself will be autoreplied to. If this precaution would not be taken, disaster could result (`ringing&#8217; mail). In order for this recipe to autoreply to all the incoming mail, you should of course insert it before all other recipes in your rcfile. However, it is advisable to put it <i>after</i> any recipes that process the mails from subscribed mailinglists; it generally is not a good idea to generate autoreplies to mailinglists (yes, the !^FROM_DAEMON regexp should already catch those, but if the mailinglist doesn&#8217;t follow accepted conventions, this might <i>not</i> be <i>enough</i>). </p>
<pre><dl><dt><dd>:0 h c
* !^FROM_DAEMON
* !^X-Loop: your [at] own.mail.address
| (formail -r -I&quot;Precedence: junk&quot; \
 -A&quot;X-Loop: your [at] own.mail.address&quot; ; \
 echo &quot;Mail received.&quot;) | $SENDMAIL -t
</dl></pre>
<p>A more complicated autoreply recipe that implements the functional equivalent of the well known <code><a href="/docs/linux/man/1-vacation/">vacation</a></code>(1) program. This recipe is based on the same principles as the last one (prevent `ringing&#8217; mail). In addition to that however, it maintains a vacation database by extracting the name of the sender and inserting it in the vacation.cache file if the name was new (the vacation.cache file is maintained by formail which will make sure that it always contains the most recent names, the size of the file is limited to a maximum of approximately 8192 bytes). If the name was new, an autoreply will be sent. As you can see, the following recipe has comments <code>between</code> the conditions. This is allowed. Do <code>not</code> put comments on the same line as a condition though. </p>
<pre><dl><dt><dd>SHELL=/bin/sh # for other shells, this might need adjustment
:0 Whc: vacation.lock
 # Perform a quick check to see if the mail was addressed to us
* $^To:.*\&lt;$\LOGNAME\&gt;
 # Don't reply to daemons and mailinglists
* !^FROM_DAEMON
 # Mail loops are evil
* !^X-Loop: your [at] own.mail.address
| formail -rD 8192 vacation.cache
 :0 ehc # if the name was not in the cache
 | (formail -rI&quot;Precedence: junk&quot; \
 -A&quot;X-Loop: your [at] own.mail.address&quot; ; \
 echo &quot;I received your mail,&quot;; \
 echo &quot;but I won't be back until Monday.&quot;; \
 echo &quot;-- &quot;; cat $HOME/.signature \
 ) | $SENDMAIL -oi -t
</dl></pre>
<p>Store all messages concerning TeX in separate, unique filenames, in a directory named texmail (this directory has to exist); there is no need to use lockfiles in this case, so we won&#8217;t. </p>
<pre><dl><dt><dd>:0
* (^TO|^Subject:.*)TeX[^t]
texmail
</dl></pre>
<p>The same as above, except now we store the mails in numbered files (MH mail folder). </p>
<pre><dl><dt><dd>:0
* (^TO|^Subject:.*)TeX[^t]
texmail/.
</dl></pre>
<p>Or you could file the mail in several directory folders at the same time. The following recipe will deliver the mail to two MH-folders and one directory folder. It is actually only one file with two extra hardlinks. </p>
<pre><dl><dt><dd>:0
* (^TO|^Subject:.*)TeX[^t]
texmail/. wordprocessing dtp/.
</dl></pre>
<p>Store all the messages about meetings in a folder that is in a directory that changes every month. E.g. if it were January 1994, the folder would have the name `94-01/meeting&#8217; and the locallockfile would be `94-01/meeting.lock&#8217;. </p>
<pre><dl><dt><dd>:0:
* meeting
`date +%y-%m`/meeting
</dl></pre>
<p>The same as above, but, if the `94-01&#8242; directory wouldn&#8217;t have existed, it is created automatically: </p>
<pre><dl><dt><dd>MONTHFOLDER=`date +%y-%m`
:0 Wic
* ? test ! -d $MONTHFOLDER
| mkdir $MONTHFOLDER
:0:
* meeting
${MONTHFOLDER}/meeting
</dl></pre>
<p>The same as above, but now by slightly different means: </p>
<pre><dl><dt><dd>MONTHFOLDER=`date +%y-%m`
DUMMY=`test -d $MONTHFOLDER || mkdir $MONTHFOLDER`
:0:
* meeting
${MONTHFOLDER}/meeting
</dl></pre>
<p>If you are subscribed to several mailinglists and people cross-post to some of them, you usually receive several duplicate mails (one from every list). The following simple recipe eliminates duplicate mails. It tells formail to keep an 8KB cache file in which it will store the Message-IDs of the most recent mails you received. Since Message-IDs are guaranteed to be unique for every new mail, they are ideally suited to weed out duplicate mails. Simply put the following recipe at the top of your rcfile, and no duplicate mail will get past it. </p>
<pre><dl><dt><dd>:0 Wh: msgid.lock
| formail -D 8192 msgid.cache
</dl></pre>
<p><code>Beware</code> if you have delivery problems in recipes below this one and procmail tries to requeue the mail, then on the next queue run, this mail will be considered a duplicate and will be thrown away. For those not quite so confident in their own scripting capabilities, you can use the following recipe instead. It puts duplicates in a separate folder instead of throwing them away. It is up to you to periodically empty the folder of course. </p>
<pre><dl><dt><dd>:0 Whc: msgid.lock
| formail -D 8192 msgid.cache
:0 a:
duplicates
</dl></pre>
<p>Procmail can deliver to MH folders directly, but, it does not update the unseen sequences the real MH manages. If you want procmail to update those as well, use a recipe like the following which will file everything that contains the word spam in the body of the mail into an MH folder called spamfold. Note the local lockfile, which is needed because MH programs do not lock the sequences file. Asynchronous invocations of MH programs that change the sequences file may therefore corrupt it or silently lose changes. Unfortunately, the lockfile doesn&#8217;t completely solve the problem as rcvstore could be invoked while `show&#8217; or `mark&#8217; or some other MH program is running. This problem is expected to be fixed in some future version of MH, but until then, you&#8217;ll have to balance the risk of lost or corrupt sequences against the benefits of the unseen sequence. </p>
<pre><dl><dt><dd>:0 :spamfold/$LOCKEXT
* B ?? spam
| rcvstore +spamfold
</dl></pre>
<p>When delivering to emacs folders (i.e., mailfolders managed by any emacs mail package, e.g., RMAIL or VM) directly, you should use emacs-compatible lockfiles. The emacs mailers are a bit braindamaged in that respect, they get very upset if someone delivers to mailfolders which they already have in their internal buffers. The following recipe assumes that $HOME equals /home/john. </p>
<pre><dl><dt><dd>MAILDIR=Mail
:0:/usr/local/lib/emacs/lock/!home!john!Mail!mailbox
* ^Subject:.*whatever
mailbox
</dl></pre>
<p>Alternatively, you can have procmail deliver into its own set of mailboxes, which you then periodically empty and copy over to your emacs files using <code>movemail</code>. Movemail uses mailbox.lock local lockfiles per mailbox. This actually is the preferred mode of operation in conjunction with procmail. To extract certain headers from a mail and put them into environment variables you can use any of the following constructs: </p>
<pre><dl><dt><dd>SUBJECT=`formail -xSubject:` # regular field
FROM=`formail -rt -xTo:` # special case
:0 h # alternate method
KEYWORDS=| formail -xKeywords:
</dl></pre>
<p>If you are using temporary files in a procmailrc file, and want to make sure that they are removed just before procmail exits, you could use something along the lines of: </p>
<pre><code>TEMPORARY=$HOME/tmp/pmail.$$
TRAP=&quot;/bin/rm -f $TEMPORARY&quot;</code></pre>
<p> The TRAP keyword can also be used to change the exitcode of procmail. I.e. if you want procmail to return an exitcode of `1&#8242; instead of its regular exitcodes, you could use: </p>
<pre><dl><dt><dd>EXITCODE=&quot;&quot;
TRAP=&quot;exit 1;&quot; # The trailing semi-colon is important
 # since exit is not a standalone program
</dl></pre>
<p>Or, if the exitcode does not need to depend on the programs run from the TRAP, you can use a mere: </p>
<pre><dl><dt><dd>EXITCODE=1
</dl></pre>
<p>The following recipe prints every incoming mail that looks like a postscript file. </p>
<pre><dl><dt><dd>:0 Bb
* ^^%!
| lpr
</dl></pre>
<p>The following recipe does the same, but is a bit more selective. It only prints the postscript file if it comes from the print-server. The first condition matches only if it is found in the header. The second condition only matches at the start of the body. </p>
<pre><dl><dt><dd>:0 b
* ^From[ :].*print-server
* B ?? ^^%!
| lpr
</dl></pre>
<p>The same as above, but now by slightly different means: </p>
<pre><dl><dt><dd>:0
* ^From[ :].*print-server
{
 :0 B b
 * ^^%!
 | lpr
}
</dl></pre>
<p>Likewise: </p>
<pre><dl><dt><dd>:0 HB b
* ^^(.+$)*From[ :].*print-server
* ^^(.+$)*^%!
| lpr
</dl></pre>
<p>Suppose you have two accounts, you use both accounts regularly, but they are in very distinct places (i.e., you can only read mail that arrived at either one of the accounts). You would like to forward mail arriving at account one to account two, and the other way around. The first thing that comes to mind is using .forward files at both sites; this won&#8217;t work of course, since you will be creating a mail loop. This mail loop can be avoided by inserting the following recipe in front of all other recipes in the $HOME/.procmailrc files on both sites. If you make sure that you add the same X-Loop: field at both sites, mail can now safely be forwarded to the other account from either of them. </p>
<pre><dl><dt><dd>:0 c
* !^X-Loop: yourname [at] your.main.mail.address
| formail -A &quot;X-Loop: yourname [at] your.main.mail.address&quot; | \
 $SENDMAIL -oi yourname [at] the.other.account
</dl></pre>
<p>If someone sends you a mail with the word `retrieve&#8217; in the subject, the following will automatically send back the contents of info_file to the sender. Like in all recipes where we send mail, we watch out for mail loops. </p>
<pre><dl><dt><dd>:0
* !^From +YOUR_USERNAME
* !^Subject:.*Re:
* !^FROM_DAEMON
* ^Subject:.*retrieve
| (formail -r ; cat info_file) | $SENDMAIL -oi -t
</dl></pre>
<p>Now follows an example for a very simple fileserver accessible by mail. For more demanding applications, I suggest you take a look at <code>SmartList</code> (available from the same place as the procmail distribution). As listed, this fileserver sends back at most one file per request, it ignores the body of incoming mails, the Subject: line has to look like &quot;Subject: send file the_file_you_want&quot; (the blanks are significant), it does not return files that have names starting with a dot, nor does it allow files to be retrieved that are outside the fileserver directory tree (if you decide to munge this example, make sure you do not inadvertently loosen this last restriction). </p>
<pre><code>:0
* ^Subject: send file [0-9a-z]
* !^X-Loop: yourname [at] your.main.mail.address
* !^Subject:.*Re:
* !^FROM_DAEMON
* !^Subject: send file .*[/.]\.
{
    MAILDIR=$HOME/fileserver # chdir to the fileserver directory

    :0 fhw                   # reverse mailheader and extract name
    * ^Subject: send file \/[^ ]*
    | formail -rA &quot;X-Loop: yourname [at] your.main.mail.address&quot;

    FILE=&quot;$MATCH&quot;            # the requested filename

    :0 ah
    | cat - ./$FILE 2&gt;&amp;1 | $SENDMAIL -oi -t
}</code></pre>
<p> The following example preconverts all plain-text mail arriving in certain encoded MIME formats into a more compact 8-bit format which can be used and displayed more easily by most programs. The <code><a href="/docs/linux/man/1-mimencode/">mimencode</a></code>(1) program is part of Nathaniel Borenstein&#8217;s metamail package. </p>
<pre><dl><dt><dd>:0
* ^Content-Type: *text/plain
{
 :0 fbw
 * ^Content-Transfer-Encoding: *quoted-printable
 | mimencode -u -q
 :0 Afhw
 | formail -I &quot;Content-Transfer-Encoding: 8bit&quot;
 :0 fbw
 * ^Content-Transfer-Encoding: *base64
 | mimencode -u -b
 :0 Afhw
 | formail -I &quot;Content-Transfer-Encoding: 8bit&quot;
}
</dl></pre>
<p>The following one is rather exotic, but it only serves to demonstrate a feature. Suppose you have a file in your HOME directory called &quot;.urgent&quot;, and the (one) person named in that file is the sender of an incoming mail, you&#8217;d like that mail to be stored in $MAILDIR/urgent instead of in any of the normal mailfolders it would have been sorted in. Then this is what you could do (beware, the filelength of $HOME/.urgent should be well below $LINEBUF, increase LINEBUF if necessary): </p>
<pre><dl><dt><dd>URGMATCH=`cat $HOME/.urgent`
:0:
* $^From.*${URGMATCH}
urgent
</dl></pre>
<p>An entirely different application for procmail would be to conditionally apply filters to a certain (outgoing) text or mail. A typical example would be a filter through which you pipe all outgoing mail, in order to make sure that it will be MIME encoded only if it needs to be. I.e. in this case you could start procmail in the middle of a pipe like: </p>
<pre><dl><dt><dd>cat newtext | procmail ./mimeconvert | mail chris [at] where.ever
</dl></pre>
<p>The <code>mimeconvert</code> rcfile could contain something like (the =0x80= and =0xff= should be substituted with the real 8-bit characters): </p>
<pre><dl><dt><dd>DEFAULT=| # pipe to stdout instead of
 # delivering mail as usual
:0 Bfbw
* [=0x80=-=0xff=]
| mimencode -q
 :0 Afhw
 | formail -I 'MIME-Version: 1.0' \
 -I 'Content-Type: text/plain; charset=ISO-8859-1' \
 -I 'Content-Transfer-Encoding: quoted-printable'
</dl></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1), <code><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></code>(5), <code><a href="/docs/linux/man/5-procmailsc/">procmailsc</a></code>(5), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/1-mailx/">mailx</a></code>(1), <code><a href="/docs/linux/man/1-uucp/">uucp</a></code>(1), <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/1-biff/">biff</a></code>(1), <code><a href="/docs/linux/man/8-comsat/">comsat</a></code>(8), <code><a href="/docs/linux/man/1-mimencode/">mimencode</a></code>(1), <code><a href="/docs/linux/man/1-lockfile/">lockfile</a></code>(1), <code><a href="/docs/linux/man/1-formail/">formail</a></code>(1)</p>
<h2>Authors</h2>
<p>Stephen R. van den Berg </p>
<pre><dl><dt><dd>&lt;srb [at] cuci.nl&gt;
</dl></pre>
<p>Philip A. Guenther </p>
<pre><dl><dt><dd>&lt;guenther [at] sendmail.com&gt;
</dl></pre>
