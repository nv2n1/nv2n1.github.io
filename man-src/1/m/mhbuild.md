---
title: "mhbuild(1)"
name: "mhbuild"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mhbuild/"
description: "mhbuild – translate MIME composition draft"
---

<h2 class="name">NAME</h2>
<p> mhbuild &#8211; translate MIME composition draft </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mhbuild</code> <i>file</i> [<code>-auto</code> | <code>-noauto</code>] [<code>-list</code> | <code>-nolist</code>] [<code>-realsize</code> | <code>-norealsize</code>] [<code>-headers</code> | <code>-noheaders</code>] [<code>-directives</code> | <code>-nodirectives</code>] [<code>-rfc934mode</code> | <code>-norfc934mode</code>] [<code>-contentid</code> | <code>-nocontentid</code>] [<code>-verbose</code> | <code>-noverbose</code>] [<code>-disposition</code> | <code>-nodisposition</code>] [<code>-check</code> | <code>-nocheck</code>] [<code>-headerencoding</code> <i>encoding-algorithm</i> | <code>-autoheaderencoding</code>] [<code>-maxunencoded</code> <i>line-length</i>] [<code>-dist</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mhbuild</code> command will translate a MIME composition draft into a valid MIME message. </p>
<p> <code>mhbuild</code> creates multi-media messages as specified in RFC 2045 to RFC 2049. This includes the encoding of message headers as specified by RFC 2047, and the encoding of MIME parameters as specified in RFC 2231. </p>
<p> If you specify the name of the composition file as &#8220;-&#8221;, then <code>mhbuild</code> will accept the composition draft on the standard input. If the translation of this input is successful, <code>mhbuild</code> will output the new MIME message to the standard output. This argument must be the last argument on the command line. </p>
<p> Otherwise if the file argument to <code>mhbuild</code> is the name of a valid composition file, and the translation is successful, <code>mhbuild</code> will replace the original file with the new MIME message. It will rename the original file to start with the &#8220;,&#8221; character and end with the string &#8220;.orig&#8221;, e.g., if you are editing the file &#8220;draft&#8221;, it will be renamed to &#8220;,draft.orig&#8221;. This allows you to easily recover the <code>mhbuild</code> input file.</p>
<h3>Listing the Contents</h3>
<p> The <code>-list</code> switch tells <code>mhbuild</code> to list the table of contents associated with the MIME message that is created. </p>
<p> The <code>-headers</code> switch indicates that a one-line banner should be displayed above the listing. The <code>-realsize</code> switch tells <code>mhbuild</code> to evaluate the &#8220;native&#8221; (decoded) format of each content prior to listing. This provides an accurate count at the expense of a small delay. If the <code>-verbose</code> switch is present, then the listing will show any &#8220;extra&#8221; information that is present in the message, such as comments in the &#8220;Content-Type&#8221; header. </p>
<p> If the <code>-disposition</code> switch is present, then the listing will show any relevant information from the &#8220;Content-Disposition&#8221; header.</p>
<h3>Simplified Attachment Interface</h3>
<p> For users who wish to simply attach files to text content, <code>mhbuild</code> will scan the composition file for &#8220;Attach&#8221; headers. An &#8220;Attach&#8221; header contains a filename that will be appended to the message using normal MIME encapsulation rules. One filename is allowed per &#8220;Attach&#8221; header, but multiple &#8220;Attach&#8221; headers are allowed ber composition file. </p>
<p> These files will be appended after any other MIME content, including any content specified by <code>mhbuild</code> directives (see below). See <i><a href="/docs/linux/man/1-send/">send</a></i>(1) for more details.</p>
<h3>Translating the Composition File</h3>
<p> <code>mhbuild</code> is essentially a filter to aid in the composition of MIME messages. <code>mhbuild</code> will convert an <code>mhbuild</code> &#8220;composition file&#8221; into a valid MIME message. A <code>mhbuild</code> &#8220;composition file&#8221; is just a file containing plain text that is interspersed with various <code>mhbuild</code> directives. When this file is processed by <code>mhbuild</code>, the various directives will be expanded to the appropriate content, and will be encoded according to the MIME standards. The resulting MIME message can then be sent by electronic mail. </p>
<p> The formal syntax for a <code>mhbuild</code> composition file is defined at the end of this document, but the ideas behind this format are not complex. Basically, the body contains one or more contents. A content consists of either a directive, indicated with a &#8220;#&#8221; as the first character of a line; or, plaintext (one or more lines of text). The continuation character, &#8220;\&#8220;, may be used to enter a single directive on more than one line, e.g., </p>
<dl>
<dt>
<dd>
<pre>
#image/png \
    /home/foobar/junk/picture.png
</pre>
</dl>
<p> There are five kinds of directives: &#8220;type&#8221; directives, which name the type and subtype of the content; &#8220;external-type&#8221; directives, which also name the type and subtype of the content; the &#8220;message&#8221; directive (#forw), which is used to forward one or more messages; the &#8220;begin&#8221; directive (#begin), which is used to create a multipart content; and the &#8220;on/off/pop&#8221; directives (#on, #off, #pop) which control whether any other directives are honored at all. </p>
<p> The <code>-directives</code> switch allows control over whether mhbuild will honor any of the &#8220;#&#8221;-directives. This can also be affected with the #on or #off directives, and #pop, which restores the state of processing to that preceding the most recent #on or #off. (The #on, #off, and #pop directives are always honored, of course.) This allows inclusion of plain text which looks like mhbuild directives, without causing errors: </p>
<dl>
<dt>
<dd>
<pre><code>
#off
#include &lt;stdio.h&gt;
printf("Hello, World!);
#pop
</code></pre>
</dl>
<p> Currently the stack depth for the #on/off/pop directives is 32. </p>
<p> The &#8220;type&#8221; directive is used to directly specify the type and subtype of a content. You may only specify discrete types in this manner (can&#8217;t specify the types multipart or message with this directive). You may optionally specify the name of a file containing the contents in &#8220;native&#8221; (decoded) format. If this filename starts with the &#8220;|&#8221; character, then it represents a command to execute whose output is captured accordingly. For example, </p>
<dl>
<dt>
<dd>
<pre>
#audio/basic |raw2audio -F &lt; /usr/lib/sound/giggle.au
</pre>
</dl>
<p> If a filename is not given, <code>mhbuild</code> will look for information in the user&#8217;s profile to determine how the different contents should be composed. This is accomplished by consulting a composition string, and executing it under <code>/bin/sh</code>, with the standard output set to the content. If the <code>-verbose</code> switch is given, <code>mhbuild</code> will echo any commands that are used to create contents in this way. </p>
<p> The composition string may contain the following escapes: </p>
<dl>
<dt>
<dd>
<pre>
%a  Insert parameters from directive
%f  Insert filename containing content
%F  %f, and stdout is not re-directed
%s  Insert content subtype
%%  Insert character %
</pre>
</dl>
<p> First, <code>mhbuild</code> will look for an entry of the form: </p>
<dl>
<dt>
<dd> mhbuild-compose-&lt;type&gt;/&lt;subtype&gt;</dl>
<p> to determine the command to use to compose the content. If this isn&#8217;t found, <code>mhbuild</code> will look for an entry of the form: </p>
<dl>
<dt>
<dd> mhbuild-compose-&lt;type&gt;</dl>
<p> to determine the composition command. If this isn&#8217;t found, <code>mhbuild</code> will complain. </p>
<p> An example entry might be: </p>
<dl>
<dt>
<dd> mhbuild-compose-audio/basic: record | raw2audio -F</dl>
<p> Because commands like these will vary, depending on the display environment used for login, composition strings for different contents should probably be put in the file specified by the <code>$MHBUILD</code> environment variable, instead of directly in your user profile. </p>
<p> The &#8220;external-type&#8221; directives are used to provide a MIME reference to a content, rather than enclosing the contents itself (for instance, by specifying an ftp site). Hence, instead of providing a filename as with the type directives, external-parameters are supplied. These look like regular parameters, so they must be separated accordingly. For example, </p>
<dl>
<dt>
<dd>
#@ application / octet &#8211; stream;<br />
type = tar;<br />
conversions = compress<br />
    [this is the nmh distribution]<br />
{<br />
    attachment;<br />
    filename = &#8220;nmh.tar.gz&#8221;<br />
}<br />
name = &#8220;nmh.tar.gz&#8221;;<br />
directory = &#8220;/pub/nmh&#8221;;<br />
site = &#8220;ftp.math.gatech.edu&#8221;;<br />
access &#8211; type = anon &#8211; ftp;<br />
mode = &#8220;image&#8221;
</dl>
<p> You must give a description string to separate the content parameters from the external-parameters (although this string may be empty). This description string is specified by enclosing it within &#8220;[]&#8221;. A disposition string, to appear in a &#8220;Content-Disposition&#8221; header, may appear in the optional &#8220;{}&#8221;. </p>
<p> These parameters are of the form: </p>
<dl>
<dt>
<dd>
<pre>
access-type=  usually <i>anon-ftp</i>, <i>mail-server</i>, or <i>url</i>
name=         filename
permission=   read-only or read-write
site=         hostname
directory=    directoryname (optional)
mode=         usually <i>ascii</i> or <i>image</i> (optional)
size=         number of octets
server=       mailbox
subject=      subject to send
body=         command to send for retrieval
url=          URL of content
</pre>
</dl>
<p> A mimimum &#8220;external-type&#8221; directive for the <code>url</code> <i>access-type</i> would be as follows: </p>
<dl>
<dt>
<dd>
<pre>
#@application/octet-stream [] access-type=url; \
  url=&quot;<a rel="nofollow" href="http://download.savannah.gnu.org/releases/nmh/nmh-1.5.tar.gz">http://download.savannah.gnu.org/releases/nmh/nmh-1.5.tar.gz</a>&quot;
</pre>
</dl>
<p> Any long URLs will be wrapped according to RFC 2231 rules. </p>
<p> The &#8220;message&#8221; directive (#forw) is used to specify a message or group of messages to include. You may optionally specify the name of the folder and which messages are to be forwarded. If a folder is not given, it defaults to the current folder. Similarly, if a message is not given, it defaults to the current message. Hence, the message directive is similar to the <code>forw</code> command, except that the former uses the MIME rules for encapsulation rather than those specified in RFC 934. For example, </p>
<dl>
<dt>
<dd>
<pre>
#forw +inbox 42 43 99
</pre>
</dl>
<p> If you include a single message, it will be included directly as a content of type &#8220;message/rfc822&#8221;. If you include more than one message, then <code>mhbuild</code> will add a content of type &#8220;multipart/digest&#8221; and include each message as a subpart of this content. </p>
<p> If you are using this directive to include more than one message, you may use the <code>-rfc934mode</code> switch. This switch will indicate that <code>mhbuild</code> should attempt to utilize the MIME encapsulation rules in such a way that the &#8220;multipart/digest&#8221; that is created is (mostly) compatible with the encapsulation specified in RFC 934. If given, then RFC 934 compliant user-agents should be able to burst the message on reception &#8212; providing that the messages being encapsulated do not contain encapsulated messages themselves. The drawback of this approach is that the encapsulations are generated by placing an extra newline at the end of the body of each message. </p>
<p> The &#8220;begin&#8221; directive is used to create a multipart content. When using the &#8220;begin&#8221; directive, you must specify at least one content between the begin and end pairs. </p>
<dl>
<dt>
<dd>
<pre>
#begin
This will be a multipart with only one part.
#end
</pre>
</dl>
<p> If you use multiple directives in a composition draft, <code>mhbuild</code> will automatically encapsulate them inside a multipart content. Therefore the &#8220;begin&#8221; directive is only necessary if you wish to use nested multiparts, or create a multipart message containing only one part. </p>
<p> For all of these directives, the user may include a brief description of the content between the &#8220;[&#8221; character and the &#8220;]&#8221; character. This description will be copied into the &#8220;Content-Description&#8221; header when the directive is processed. </p>
<dl>
<dt>
<dd>
<pre>
#forw [important mail from Bob] +bob 1 2 3 4 5
</pre>
</dl>
<p> Similarly, a disposition string may optionally be provided between &#8220;{&#8221; and &#8220;}&#8221; characters; it will be copied into the &#8220;Content-Disposition&#8221; header when the directive is processed. If a disposition string is provided that does not contain a filename parameter, and a filename is provided in the directive, it will be added to the &#8220;Content-Disposition&#8221; header. For example, the following directive: </p>
<dl>
<dt>
<dd>
<pre>
#text/plain; charset=iso-8859-1 &lt;&gt;{attachment} /tmp/summary.txt
</pre>
</dl>
<p> creates these message part headers: </p>
<dl>
<dt>
<dd>
<pre>
Content-Type: text/plain; charset=&quot;iso-8859-1&quot;
Content-Disposition: attachment; filename=&quot;summary.txt&quot;
</pre>
</dl>
<p> By default, <code>mhbuild</code> will generate a unique &#8220;Content-ID:&#8221; for each directive, corresponding to each message part; however, the user may override this by defining the ID using the &#8220;&lt;&#8221; and &#8220;&gt;&#8221; characters. The <code>-nocontentid</code> switch suppresses creation of all &#8220;Content-ID:&#8221; headers, even in the top level of the message. </p>
<p> Normally <code>mhbuild</code> will choose an appropriate Content-Transfer-Encoding based on the content and the MIME Content-Type. However, you can override that in an <code>mhbuild</code> directive by specifying &#8220;*&#8221; and the encoding. Acceptable encoding values are &#8220;8bit&#8221;, &#8220;qp&rho;q (for quoted-printable), and &#8220;b64&#8221; (for base64 encoding). It should be noted that undesired results may occur if 8bit or quoted-printable is selected for binary content, due to the translation between Unix line endings and the line endings use by the mail transport system. </p>
<p> In addition to the various directives, plaintext can be present. Plaintext is gathered, until a directive is found or the draft is exhausted, and this is made to form a text content. If the plaintext must contain a &#8220;#&#8221; at the beginning of a line, simply double it, e.g., </p>
<dl>
<dt>
<dd> ##when sent, this line will start with only one #</dl>
<p> If you want to end the plaintext prior to a directive, e.g., to have two plaintext contents adjacent, simply insert a line containing a single &#8220;#&#8221; character, e.g., </p>
<dl>
<dt>
<dd>
<pre>
this is the first content
#
and this is the second
</pre>
</dl>
<p> Finally, if the plaintext starts with a line of the form: </p>
<dl>
<dt>
<dd> Content-Description: text</dl>
<p> then this will be used to describe the plaintext content. You MUST follow this line with a blank line before starting your text. </p>
<p> By default, plaintext is captured as a text/plain content. You can override this by starting the plaintext with &#8220;#&lt;&#8221; followed by a content-type specification. For example, e.g., </p>
<dl>
<dt>
<dd>
<pre>
#&lt;text/enriched
this content will be tagged as text/enriched
#
and this content will be tagged as text/plain
#
#&lt;application/x-patch [this is a patch]
and this content will be tagged as application/x-patch
</pre>
</dl>
<p> Note that if you use the &#8220;#&lt;&#8221; plaintext-form, then the content-description must be on the same line which identifies the content type of the plaintext. </p>
<p> When composing a text content, you may indicate the relevant character set by adding the &#8220;charset&#8221; parameter to the directive. </p>
<dl>
<dt>
<dd> #&lt;text/plain; charset=iso-8859-5</dl>
<p> If a text content contains any 8-bit characters (characters with the high bit set) and the character set is not specified as above, then <code>mhbuild</code> will assume the character set is of the type given by the standard <i><a href="/docs/linux/man/1-locale/">locale</a></i>(1) environment variables. If these environment variables are not set, then the character set will be labeled as &#8220;x-unknown&#8221;. </p>
<p> If a text content contains only 7-bit characters and the character set is not specified as above, then the character set will be labeled as &#8220;us-ascii&#8221;. </p>
<p> By default text content with the high bit set is encoded with a 8bit Content-Transfer-Encoding. If the text has lines longer than the value of <code>-maxunencoded</code> (which defaults to 78) then the text is encoded using the quoted-printable encoding. </p>
<p> The <code>-headerencoding</code> switch will indicate which algorithm to use when encoding any message headers that contain 8-bit characters. The valid arguments are <i>base64</i> for based-64 encoding and <i>quoted</i> for quoted-printable encoding. The <code>-autoheaderencoding</code> switch will instruct <code>mhbuild</code> to automatically pick the algorithm that results in a shorter encoded string. </p>
<p> Putting this all together, here is an example of a more complicated message draft. The following draft will expand into a multipart/mixed message containing five parts: </p>
<dl>
<dt>
<dd>
To : nobody[at] nowhere.org<br />
         cc : Subject : Look and listen to me !&#8211; &#8212; &#8212; &#8211;The first part will be text /<br />
    plain<br />
# &lt;text / enriched<br />
        The second part will be text /<br />
    enriched<br />
#<br />
        This third part will be text /<br />
    plain<br />
#audio / basic[silly giggle] | raw2audio &#8211; F &lt; / usr / lib / sounds / giggle.au<br />
#image / gif[photo of foobar] / home / foobar / lib / picture.gif
</dl>
<h3>Integrity Check</h3>
<p> If <code>mhbuild</code> is given the <code>-check</code> switch, then it will also associate an integrity check with each &#8220;leaf&#8221; content. This will add a Content-MD5 header field to the content, along with the md5 sum of the unencoded contents, per RFC 1864. This may be used by the receiver of the message to verify that the contents of the message were not changed in transport.</p>
<h3>Transfer Encodings</h3>
<p> After <code>mhbuild</code> constructs the new MIME message by parsing directives, including files, etc., it scans the contents of the message to determine which transfer encoding to use. It will check for 8bit data, long lines, spaces at the end of lines, and clashes with multipart boundaries. It will then choose a transfer encoding appropriate for each content type. </p>
<p> If an integrity check is being associated with each content by using the <code>-check</code> switch, then <code>mhbuild</code> will encode each content with a transfer encoding, even it the content contains only 7-bit data. This is to increase the likelihood that the content is not changed while in transport.</p>
<h3>Invoking mhbuild</h3>
<p> Typically, <code>mhbuild</code> is invoked by the <code>whatnow</code> program. This command will expect the body of the draft to be formatted as an <code>mhbuild</code> composition file. Once you have composed this input file using a command such as <code>comp</code>, <code>repl</code>, or <code>forw</code>, you invoke <code>mhbuild</code> at the &#8220;What now&#8221; prompt with </p>
<dl>
<dt>
<dd> What now? mime</dl>
<p> prior to sending the draft. This will cause <code>whatnow</code> to execute <code>mhbuild</code> to translate the composition file into MIME format. </p>
<p> Normally it is an error to invoke <code>mhbuild</code> on file that already in MIME format. The <code>-auto</code> switch will cause <code>mhbuild</code> to exit without error if the input file already has valid MIME headers. The use of <code>-auto</code> also enables the <code>-nodirectives</code> switch. </p>
<p> Finally, you should consider adding this line to your profile: </p>
<dl>
<dt>
<dd> lproc: show</dl>
<p> This way, if you decide to <code>list</code> after invoking <code>mime</code>, the command </p>
<dl>
<dt>
<dd> What now? list</dl>
<p> will work as you expect. </p>
<p> The <code>-dist</code> switch is intended to be used by <code>dist</code>. It will cause mhbuild to not generate any MIME headers in the composition file (such as &#8220;MIME-Version&#8221; or &#8220;Content-Type&#8221;), but it will still encode message headers according to RFC 2047.</p>
<h3>User Environment</h3>
<p> Because the environment in which <code>mhbuild</code> operates may vary for a user, <code>mhbuild</code> will look for the environment variable <code>$MHBUILD</code>. If present, this specifies the name of an additional user profile which should be read. Hence, when a user logs in on a particular machine, this environment variable should be set to refer to a file containing definitions useful for that machine. </p>
<p> Finally, <code>mhbuild</code> will attempt to consult </p>
<dl>
<dt>
<dd> /etc/nmh/mhn.defaults</dl>
<p> if it exists. </p>
<p> See &quot;Profile Lookup&quot; in <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5) for the profile search order, and for how duplicate entries are treated.</p>
<h3>Syntax of Composition Files</h3>
<p> The following is the formal syntax of a <code>mhbuild</code> &#8220;composition file&#8221;. </p>
<dl>
<dt>
<dd>
<pre><code>
body :: = 1 * (content | EOL)
                  content ::
              = directive | plaintext
                                directive ::
                    = "#" type "/" subtype 0 * (";" attribute "=" value)
                                                   ["(" comment ")"]
                                                   ["&lt;" id "&gt;"]
                                                   ["[" description "]"]
                                                   ["{" disposition "}"]
                                                   ["*8bit" | "*qp" | "*b64"]
                                                   [filename] EOL |
                      "#@" type "/" subtype 0 * (";" attribute "=" value)
                                                    ["(" comment ")"]
                                                    ["&lt;" id "&gt;"]
                                                    ["[" description "]"]
                                                    ["{" disposition "}"]
                                                    ["*8bit" | "*qp" | "*b64"] external -
                          parameters
                              EOL |
                      "#forw"
                          ["&lt;" id "&gt;"]
                          ["[" description "]"]
                          ["{" disposition "}"]
                          ["+" folder][0 * msg] EOL |
                      "#begin"
                          ["&lt;" id "&gt;"]
                          ["[" description "]"]
                          ["{" disposition "}"]
                          ["alternative" | "parallel" | something - else] EOL 1 *body
                      "#end" EOL
                          plaintext ::
                          = ["Content-Description:" description EOL EOL] 1 * line
                                                                                 ["#" EOL] |
                            "#&lt;" type "/" subtype 0 * (";" attribute "=" value)["(" comment ")"]["[" description "]"]["{" disposition "}"]["*8bit" | "*qp" | "*b64"] EOL 1 * line["#" EOL] line ::
                                = "##" text EOL-- interpreted as "#" text EOL | text EOL
</code></pre>
</dl>
<h2>FILES</h2>
<p> <code>mhbuild</code> looks for additional user profile files and mhn.defaults in multiple locations: absolute pathnames are accessed directly, tilde expansion is done on usernames, and files are searched for in the user&#8217;s <i>Mail</i> directory as specified in their profile. If not found there, the directory &#8220;<i>/etc/nmh</i>&#8221; is checked. </p>
<pre>
^$HOME/.mh_profile~^The user profile
^$MHBUILD~^Additional profile entries
^/etc/nmh/mhn.defaults~^System default MIME profile entries
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^mhbuild-compose-&lt;type&gt;*~^Template for composing contents
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mhlist/">mhlist</a></i>(1), <i><a href="/docs/linux/man/1-mhshow/">mhshow</a></i>(1), <i><a href="/docs/linux/man/1-mhstore/">mhstore</a></i>(1) </p>
<p> <i>Proposed Standard for Message Encapsulation</i> (RFC 934), </p>
<p> <i>The Content-MD5 Header Field</i> (RFC 1864), </p>
<p> <i>Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies</i> (RFC 2045), </p>
<p> <i>Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types</i> (RFC 2046), </p>
<p> <i>Multipurpose Internet Mail Extensions (MIME) Part Three: Message Header Extensions for Non-ASCII Text</i> (RFC 2047), </p>
<p> <i>Multipurpose Internet Mail Extensions (MIME) Part Four: Registration Procedures</i> (RFC 2048), </p>
<p> <i>Multipurpose Internet Mail Extensions (MIME) Part Five: Conformance Criteria and Examples</i> (RFC 2049), </p>
<p> <i>Definition of the URL MIME External-Body Access-Type</i> (RFC 2017), </p>
<p> <i>MIME Parameter Value and Encoded Word Extensions: Character Sets, Languages, and Continuations</i> (RFC 2231)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-headers</code>'
`<code>-realsize</code>'
`<code>-norfc934mode</code>'
`<code>-contentid</code>'
`<code>-nocheck</code>'
`<code>-noverbose</code>'
`<code>-nodisposition</code>'
`<code>-autoheaderencoding</code>'
`<code>-maxunencoded 78'</code>
</pre>
<h2>Index</h2>
