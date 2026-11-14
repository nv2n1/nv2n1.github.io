---
title: "mime-construct(1)"
name: "mime-construct"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mime-construct/"
description: "mime-construct – construct and optionally mail MIME messages"
---

<h2 class="name">NAME</h2>
<p> mime-construct &#8211; construct and optionally mail MIME messages </p>
<h2>SYNOPSIS</h2>
<p> <code>mime-construct</code> <i>switch</i>&#8230; </p>
<p> Sorry, it&#8217;s hard to provide a meaningful synopsis. See the examples.</p>
<h2>DESCRIPTION</h2>
<p> <code>mime-construct</code> constructs and (by default) mails <font SIZE="-1">MIME</font> messages. It is entirely driven from the command line, it is designed to be used by other programs, or people who act like programs.</p>
<h2>OPTIONS</h2>
<h3>Global Settings</h3>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> Turn debugging on.</p>
<dt><code>&#8211;help</code></p>
<dd> Show the usage message and die.</p>
<dt><code>&#8211;output</code></p>
<dd> Don&#8217;t mail the generated message, print it to stdout instead. This loses <code>&#8211;bcc</code> info.</p>
<dt><code>&#8211;subpart</code></p>
<dd> Generate a subpart which can be used in another <font SIZE="-1">MIME</font> message, rather than a top-level <font SIZE="-1">MIME</font> message itself. This turns on <code>&#8211;output</code> and changes some internal semantics a bit. See the examples.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version and exit successfully, if this is the only arg. Otherwise, print the version and die.</dl>
<h3>Main Header</h3>
<p> These arguments add text to the top-level header of the message, or control who it gets sent to.</p>
<dl>
<dt><code>&#8211;bcc</code> <i>address</i></p>
<dd> Add <i>address</i> to the recipient list. This doesn&#8217;t actually add anything to the header, of course. If you&#8217;re not actually mailing the message (if you use <code>&#8211;output</code> or <code>&#8211;subpart</code>) <code>&#8211;bcc</code> will have no effect.</p>
<dt><code>&#8211;cc</code> <i>address</i></p>
<dd> Add an address to the <code>Cc:</code> list.</p>
<dt><code>&#8211;embedded-to</code></p>
<dd> Send the message to the recipients already listed in the header, in addition to those given with <code>&#8211;to</code>, <code>&#8211;cc</code>, and <code>&#8211;bcc</code>. This makes sense if you use the <code>&#8211;header</code> switch to add your own <code>To:</code> or <code>Cc:</code>. In this case you probably don&#8217;t want to use <code>&#8211;to</code> or <code>&#8211;cc</code> because they would create new headers rather than adding to the ones already in the message. </p>
<p> This switch passes the <code>-t</code> switch to sendmail (<code>mime-construct</code> doesn&#8217;t try to parse the headers you provide), so it doesn&#8217;t really do anything if you&#8217;re not mailing the message.</p>
<dt><code>&#8211;header</code> <i>str</i></p>
<dd> Add arbitrary text to the header. The <i>str</i> can be anything you like, including multiple lines. You can create invalid messages this way. If you include a blank line in the <i>str</i> you&#8217;ll really screw up the message.</p>
<dt><code>&#8211;multipart</code> <i>str</i></p>
<dd> This specifies the multipart content type and options. The default is <tt>&quot;multipart/mixed&quot;</tt>. Don&#8217;t include a <tt>&quot;boundary&quot;</tt> setting, that&#8217;s supplied by <code>mime-construct</code>. </p>
<p> It&#8217;s okay if you specify the <code>&#8211;multipart</code> type but the message turns out to be a single part, the type you supply will just be ignored.</p>
<dt><code>&#8211;prelude</code> <i>str</i></p>
<dd> This adds <i>str</i> to the multipart prelude text. If you specify <code>&#8211;prelude</code> multiple times the <i>str</i>s will all be concatenated. </p>
<p> There isn&#8217;t any default for this text. It seems to me that nowadays adding an explanation of <font SIZE="-1">MIME</font> to the beginning of a message is like explaining how to use a seat buckle to people who are riding in an airplane. </p>
<p> It&#8217;s okay if you specify the <code>&#8211;prelude</code> but the message turns out to be a single part, the prelude you supply will just be ignored.</p>
<dt><code>&#8211;subject</code> <i>str</i></p>
<dd> Specify the subject for the message.</p>
<dt><code>&#8211;to</code> <i>address</i></p>
<dd> Add an address to the <code>To:</code> list.</dl>
<h3>Per-part Header</h3>
<p> These switches control the per-part headers. If the message turns out not to be multipart they actually add data to the top level header. </p>
<p> Each of these applies only to the next part output. After each part is output they are reset to their default values. It doesn&#8217;t make sense to use them without a following part, so <code>mime-construct</code> will sputter and die if you try to do that.</p>
<dl>
<dt><code>&#8211;attachment</code> <i>name</i></p>
<dd> This adds a <tt>&quot;Content-Disposition: attachment&quot;</tt> header with the given <i>name</i> as the value of the <tt>&quot;filename&quot;</tt> attribute. It&#8217;s just a convenience, since <code>mime-construct</code> is often used to send files as attachments. </p>
<p> Using <code>&#8211;attachment</code> <i>name</i> does not cause <code>mime-construct</code> to read any data from the file called <i>name</i>! It just uses that name in the header. The actual data which will go into this part of the message comes from one of the regular part output switches (given below). </p>
<p> You might prefer to use the <code>&#8211;file-attach</code> switch, which does read from the <i>name</i>d file.</p>
<dt><code>&#8211;encoding</code> <i>type</i></p>
<dd> This specifies the type of encoding you want this part to use. You normally shouldn&#8217;t use this switch, though. If this switch isn&#8217;t used <code>mime-construct</code> will choose an appropriate encoding. </p>
<p> The data you supply mustn&#8217;t be encoded already, <code>mime-construct</code> will encode it according to the <i>type</i> you specify here. Valid encodings are <code>7bit</code>, <code>8bit</code>, <code>binary</code>, <code>quoted-printable</code>, and <code>base64</code>. It&#8217;s easy to generate an illegal <font SIZE="-1">MIME</font> message by specifying the encoding yourself.</p>
<dt><code>&#8211;part-header</code> <i>str</i></p>
<dd> Add arbitrary text to the per-part header. The <i>str</i> can be anything you like, including multiple lines. You can create invalid messages this way. If you include a blank line in the <i>str</i> you&#8217;ll really screw up the message.</p>
<dt><code>&#8211;type</code> <i>type</i></p>
<dd> Specify the content type for this part. If you don&#8217;t specify a <code>&#8211;type</code> it defaults to <tt>&quot;text/plain&quot;</tt>. The <i>type</i> you supply can contain not only the type proper but also options. The whole thing will just be plopped onto the end of <tt>&quot;Content-Type:&quot;</tt> and stuck into the header. </p>
<p> You might prefer to use the <code>&#8211;file-auto</code> or <code>&#8211;file-attach</code> switches, which set the <code>&#8211;type</code> automatically based on a file&#8217;s name.</dl>
<h3>Part Output</h3>
<p> These switches add data to the body of the message. You use one of these for each for each part of a multipart message (or just one of them if the message isn&#8217;t to be multipart).</p>
<dl>
<dt><code>&#8211;file</code> <i>path</i></p>
<dd>
<dt><code>&#8211;file-auto</code> <i>path</i></p>
<dd>
<dt><code>&#8211;file-attach</code> <i>path</i></p>
<dd>
<dt><code>&#8211;attach</code> <i>path</i></p>
<dd>
<dt><code>&#8211;string</code> <i>str</i></p>
<dd>
<dt><code>&#8211;body</code> <i>str</i></p>
<dd> Use the contents of the file <i>path</i> or the literal string <i>str</i> as the body of this part. </p>
<p> <code>&#8211;file-auto</code> causes the Content-Type to be set based on the file&#8217;s name, if possible. </p>
<p> <code>&#8211;file-attach</code> does that and sets the <code>&#8211;attachment</code> name as well. </p>
<p> Be sure to include the trailing newline on <i>str</i> unless there really isn&#8217;t supposed to be one. If you leave the trailing newline off the part will have to be encoded in <tt>&quot;base64&quot;</tt> (because <tt>&quot;quoted-printable&quot;</tt> has an artificial limitation which prevents it from being able to encode such a data stream). </p>
<p> <code>&#8211;attach</code> is an alias for <code>&#8211;file-attach</code>, and <code>&#8211;body</code> is an alias for <code>&#8211;string</code>.</p>
<dt><code>&#8211;subpart-file</code> <i>path</i></p>
<dd>
<dt><code>&#8211;subpart-string</code> <i>str</i></p>
<dd> Use either the contents of <i>path</i> or <i>str</i> itself as the body of this part, but treat it as a subpart. This means that the data contains both some headers and some text. It also means that you can&#8217;t use <code>&#8211;type</code> or <code>&#8211;encoding</code> for this part. </p>
<p> Normally the <i>path</i> or <i>str</i> will have been generated by a different invocation of <code>mime-construct</code> which was given the <code>&#8211;subpart</code> switch.</dl>
<p> Arguments to switches which take a file name (such as <code>&#8211;file</code> and <code>&#8211;subpart-file</code>) can have some magic. If there is no file with the <i>path</i> supplied a regular Perl <i>open()</i> is done on it. See &#8220;<font SIZE="-1">EXAMPLES&#8221;</font>.</p>
<h2>EXAMPLES</h2>
<p> The examples assume that <tt>$nl</tt> contains a newline. The other variables used are I hope self-explanatory. </p>
<p> Send a simple message. </p>
<pre>
    mime-construct --to &quot;$recip&quot; --subject 'hi there' --string &quot;$body&quot;
</pre>
<p> Send a message which is read from stdin. </p>
<pre>
    fortune | mime-construct --to &quot;$recip&quot; --subject fortune --file -
</pre>
<p> Send a plain text part and attach a file, setting the file&#8217;s content type and <code>&#8211;attachment</code> name automatically. </p>
<pre><code>
mime - construct-- to "$recip" --subject "$file" --string "Here's the file I told you about.$nl" --file - attach "$file"
</code></pre>
<p> Most people think of attachments as multipart messages, but they don&#8217;t have to be. This generates a zip of all the files in the current directory and sends them as an attachment but as a single part message. </p>
<p>zip &#8211; q &#8211; * |<br />
    mime &#8211; construct&#8211; to &#8220;$recip&#8221; &#8211;subject &#8216;zipped directory&#8217; &#8211;attachment dir.zip&#8211; type application / zip&#8211; file &#8211;</p>
<p> You can use the full expressiveness of Perl&#8217;s <i>open()</i> when constructing file names. Eg, you can run processes <font SIZE="-1">XXX</font> bad examples, there&#8217;s no file names </p>
<p>mime &#8211; construct&#8211; to &#8220;$recip&#8221; &#8211;subject &#8220;$subject&#8221; &#8211;string &#8220;Here are those two files you wanted.$nl&#8221; &#8211;type application / x &#8211; gzip&#8211; attachment file1.gz&#8211; file &#8216;gzip -c file1 |&#8217; &#8211;type application / x &#8211; gzip&#8211; attachment file1.gz&#8211; file &#8216;gzip -c file2 |&#8217;</p>
<p> or read from alternate file descriptors (<tt>&quot;&lt;&amp;=4&quot;</tt> to read from file descriptor 4) or whatever. See perlopentut for a tutorial. </p>
<p> Here&#8217;s an example of using a separate invocation of <code>mime-construct</code> to create a subpart. This creates a message which has two parts at the top level. The first part is some text, the second part is a digest. The digest itself is a multipart message which contains a number of message/rfc822 parts. </p>
<p>    msg_args=<br />
    for msg in $msg_list<br />
    do<br />
        msg_args=&#8221;$msg_args &#8211;type message/rfc822 &#8211;file $msg&#8221;<br />
    done<br />
    set fnord<br />
    for recip in $recip_list<br />
    do<br />
        set &#8220;$@&#8221; &#8211;bcc $recip<br />
    done<br />
    shift<br />
    mime-construct &#8211;subpart &#8211;multipart multipart/digest $msg_args |<br />
        mime-construct \<br />
            &#8211;header &#8220;To: Digest recipients:;$nl&#8221; \<br />
            &#8211;subject &#8216;Foo digest&#8217; \<br />
            &#8220;$@&#8221; \<br />
            &#8211;file &#8220;$introduction&#8221; \<br />
            &#8211;subpart-file &#8211;</p>
<p> Here is how to send an encrypted messages (multipart/encrypted, as defined in <font SIZE="-1">RFC 1847</font>). You use <code>mime-construct</code> <tt>&quot;--subpart&quot;</tt> to generate the real message you want to send (which can be kind of <font SIZE="-1">MIME</font> message &#8212; non-text, multi-part, what have you), then encrypt that and use another <code>mime-construct</code> to contruct and send the multipart/encrypted message which contains it. </p>
<pre><code>
enc_type = application / pgp - encrypted
                                   enc_params = "Version: 1$nl" mime - construct-- subpart-- file body-- file - auto image.jpg |
                                                gpg-- encrypt-- armor - r "$recip" |
                                                mime - construct-- output-- to "$recip" --subject "$subject" --multipart "multipart/encrypted; protocol=\"$enc_type\"" --type "$enc_type" --string "$enc_params" --type application / octet - stream-- file -
</code></pre>
<h2>BUGS</h2>
<p> The body of the message is always held in memory, so you can expect problems if you work with bodies which are large compared to the amount of memory you&#8217;ve got.</p>
<h2>AVAILABILITY</h2>
<p> The code is licensed under the <font SIZE="-1">GNU GPL. </font> Check <a rel="nofollow" href="http://www.argon.org/~roderick/">http://www.argon.org/~roderick/</a> for updated versions.</p>
<h2>AUTHOR</h2>
<p> Roderick Schertler &lt;roderick [at] argon.org&gt; </p>
<h2>Index</h2>
