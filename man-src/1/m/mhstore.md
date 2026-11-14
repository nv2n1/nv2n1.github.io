---
title: "mhstore(1)"
name: "mhstore"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mhstore/"
description: "mhstore – store contents of MIME messages into files"
---

<h2 class="name">NAME</h2>
<p> mhstore &#8211; store contents of MIME messages into files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mhstore</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-file</code> <i>file</i>] [<code>-outfile</code> <i>outfile</i>] [<code>-part</code> <i>number</i>] &#8230; [<code>-type</code> <i>content</i>] &#8230; [<code>-auto</code> | <code>-noauto</code>] [<code>-clobber</code> <i>always</i> | <i>auto</i> | <i>suffix</i> | <i>ask</i> | <i>never</i>] [<code>-rcache</code> <i>policy</i>] [<code>-wcache</code> <i>policy</i>] [<code>-check</code> | <code>-nocheck</code>] [<code>-verbose</code> | <code>-noverbose</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mhstore</code> command allows you to store the contents of a collection of MIME (multi-media) messages into files or other messages. </p>
<p> <code>mhstore</code> manipulates multi-media messages as specified in RFC 2045 to RFC 2049. </p>
<p> By default, <code>mhstore</code> will store all the parts of each message. Each part will be store in a separate file. The header fields of the message are not stored. By using the <code>-part</code> and <code>-type</code> switches, you may limit the scope of <code>mhstore</code> to particular subparts (of a multipart content) and/or particular content types. </p>
<p> The <code>-file</code> <i>file</i> switch directs <code>mhstore</code> to use the specified file as the source message, rather than a message from a folder. If you specify this file as &#8220;-&#8221;, then <code>mhstore</code> will accept the source message on the standard input. Note that the file, or input from standard input should be a validly formatted message, just like any other <code>nmh</code> message. It should <code>NOT</code> be in mail drop format (to convert a file in mail drop format to a folder of <code>nmh</code> messages, see <i><a href="/docs/linux/man/1-inc/">inc</a></i>(1)). </p>
<p> A part specification consists of a series of numbers separated by dots. For example, in a multipart content containing three parts, these would be named as 1, 2, and 3, respectively. If part 2 was also a multipart content containing two parts, these would be named as 2.1 and 2.2, respectively. Note that the <code>-part</code> switch is effective for only messages containing a multipart content. If a message has some other kind of content, or if the part is itself another multipart content, the <code>-part</code> switch will not prevent the content from being acted upon. </p>
<p> A content specification consists of a content type and a subtype. The initial list of &#8220;standard&#8221; content types and subtypes can be found in RFC 2046. </p>
<p> A list of commonly used contents is briefly reproduced here: </p>
<dl>
<dt>
<dd>
<pre><code>
Type Subtypes-- -- -- -- -- --text plain, enriched multipart mixed, alternative, digest, parallel message rfc822, partial, external - body application octet - stream, postscript image jpeg, gif, png audio basic video mpeg
</code></pre>
</dl>
<p> A legal MIME message must contain a subtype specification. </p>
<p> To specify a content, regardless of its subtype, just use the name of the content, e.g., &#8220;audio&#8221;. To specify a specific subtype, separate the two with a slash, e.g., &#8220;audio/basic&#8221;. Note that regardless of the values given to the <code>-type</code> switch, a multipart content (of any subtype listed above) is always acted upon. Further note that if the <code>-type</code> switch is used, and it is desirable to act on a message/external-body content, then the <code>-type</code> switch must be used twice: once for message/external-body and once for the content externally referenced.</p>
<h3>Checking the Contents</h3>
<p> The <code>-check</code> switch tells <code>mhstore</code> to check each content for an integrity checksum. If a content has such a checksum (specified as a Content-MD5 header field), then <code>mhstore</code> will attempt to verify the integrity of the content.</p>
<h3>Storing the Contents</h3>
<p> The <code>mhstore</code> will store the contents of the named messages in &#8220;native&#8221; (decoded) format. Two things must be determined: the directory to store the content, and the filenames. Files are written in the directory given by the &#8220;nmh-storage&#8221; profile entry, e.g., </p>
<dl>
<dt>
<dd> nmh-storage: /tmp</dl>
<p> If this entry isn&#8217;t present, the current working directory is used. </p>
<p> If the <code>-outfile</code> switch is given, its argument is used for the filename to store all of the content, with &#8220;-&#8221; indicating standard output. If the <code>-auto</code> switch is given, then <code>mhstore</code> will check if the message contains information indicating the filename that should be used to store the content. This information should be specified as the &#8220;filename&#8221; attribute in the &#8220;Content-Disposition&#8221; header or as the &#8220;name&#8221; attribute in the &#8220;Content-Type&#8221; header for the content you are storing. For security reasons, this filename will be ignored if it begins with the character &#8216;/&#8217;, &#8216;.&#8217;, &#8216;|&#8217;, or &#8216;!&#8217;, or if it contains the character &#8216;%&#8217;. We also recommend using a &#8220;nmh-storage&#8221; profile entry or a <code>-clobber</code> switch setting other than the default of &#8220;always&#8221; to avoid overwriting existing files. </p>
<p> If the <code>-auto</code> switch is not given (or is being ignored for security reasons) then <code>mhstore</code> will look in the user&#8217;s profile for a &#8220;formatting string&#8221; to determine how the different contents should be stored. First, <code>mhstore</code> will look for an entry of the form: </p>
<dl>
<dt>
<dd> mhstore-store-&lt;type&gt;/&lt;subtype&gt;</dl>
<p> to determine the formatting string. If this isn&#8217;t found, <code>mhstore</code> will look for an entry of the form: </p>
<dl>
<dt>
<dd> mhstore-store-&lt;type&gt;</dl>
<p> to determine the formatting string. </p>
<p> If the formatting string starts with a &#8220;+&#8221; character, then content is stored in the named folder. A formatting string consisting solely of a &#8220;+&#8221; character is interpreted to be the current folder. </p>
<p> If the formatting string consists solely of a &#8220;-&#8221; character, then the content is sent to the standard output. </p>
<p> If the formatting string starts with a &#8216;|&#8217;, then it represents a command for <code>mhstore</code> to execute which should ultimately store the content. The content will be passed to the standard input of the command. Before the command is executed, <code>mhstore</code> will change to the appropriate directory, and any escapes (given below) in the formatting string will be expanded. The use of the &#8220;%a&#8221; sequence is not recommended because the user has no control over the Content-Type parameter data. </p>
<p> Otherwise the formatting string will represent a pathname in which to store the content. If the formatting string starts with a &#8216;/&#8217;, then the content will be stored in the full path given, else the file name will be relative to the value of &#8220;nmh-storage&#8221; or the current working directory. Any escapes (given below) will be expanded, except for the a-escape. Note that if &#8220;nmh-storage&#8221; is not an absolute path, it will be relative to the folder that contains the message(s). </p>
<p> A command or pathname formatting string may contain the following escapes. If the content isn&#8217;t part of a multipart (of any subtype listed above) content, the p-escapes are ignored. </p>
<dl>
<dt>
<dd>
<pre>
%a  Parameters from Content-Type  (only valid with command)
%m  Insert message number
%P  Insert part number with leading dot
%p  Insert part number without leading dot
%t  Insert content type
%s  Insert content subtype
%%  Insert character %
</pre>
</dl>
<p> If no formatting string is found, <code>mhstore</code> will check to see if the content is application/octet-stream with parameter &#8220;type=tar&#8221;. If so, <code>mhstore</code> will choose an appropriate filename. If the content is not application/octet-stream, then <code>mhstore</code> will check to see if the content is a message. If so, <code>mhstore</code> will use the value &#8220;+&#8221;. As a last resort, <code>mhstore</code> will use the value &#8220;%m%P.%s&#8221;. </p>
<p> Example profile entries might be: </p>
<dl>
<dt>
<dd>
<pre>
mhstore-store-text: %m%P.txt
mhstore-store-text: +inbox
mhstore-store-message/partial: +
mhstore-store-audio/basic: | raw2audio -e ulaw -s 8000 -c 1 &gt; %m%P.au
mhstore-store-image/jpeg: %m%P.jpg
mhstore-store-application/PostScript: %m%P.ps
</pre>
</dl>
<p> The <code>-verbose</code> switch directs <code>mhstore</code> to print out the names of files that it stores. For backward compatibility, it is the default. The <code>-noverbose</code> switch suppresses these printouts. </p>
<h3>Overwriting Existing Files</h3>
<p> The <code>-clobber</code> switch controls whether <code>mhstore</code> should overwrite existing files. The allowed values for this switch and corresponding behavior when <code>mhstore</code> encounters an existing file are: </p>
<dl>
<dt>
<dd>
<pre>
always    Overwrite existing file (default)
auto      Create new file of form name-n.extension
suffix    Create new file of form name.extension.n
ask       Prompt the user to specify whether or not to overwrite
          the existing file
never     Do not overwrite existing file
</pre>
</dl>
<p> With <i>auto</i> and <i>suffix</i>, <i>n</i> is the lowest unused number, starting from one, in the same form. If a filename does not have an extension (following a &#8216;.&#8217;), then <i>auto</i> and <i>suffix</i> create a new file of the form <i>name-n</i> and <i>name.n</i>, respectively. With <i>never</i> and <i>ask</i>, the exit status of <code>mhstore</code> will be the number of files that were requested but not stored. </p>
<p> With <i>ask</i>, if standard input is connected to a terminal, the user is prompted to respond <i>yes</i>, <i>no</i>, or <i>rename</i> to whether the file should be overwritten. The responses can be abbreviated. If the user responds with <i>rename</i>, then <code>mhstore</code> prompts the user for the name of the new file to be created. If it is a relative path name (does not begin with &#8216;/&#8217;), then it is relative to the current directory. If it is an absolute or relative path to a directory that does not exist, the user will be prompted whether to create the directory. If standard input is not connected to a terminal, <i>ask</i> behaves the same as <i>always</i>.</p>
<h3>Reassembling Messages of Type message/partial</h3>
<p> <code>mhstore</code> is also able to reassemble messages that have been split into multiple messages of type &#8220;message/partial&#8221;. </p>
<p> When asked to store a content containing a partial message, <code>mhstore</code> will try to locate all of the portions and combine them accordingly. The default is to store the combined parts as a new message in the current folder, although this can be changed using formatting strings as discussed above. Thus, if someone has sent you a message in several parts (such as the output from <code>sendfiles</code>), you can easily reassemble them all into a single message in the following fashion: </p>
<dl>
<dt>
<dd>
<pre>
% mhlist 5-8
 msg part  type/subtype             size description
   5       message/partial           47K part 1 of 4
   6       message/partial           47K part 2 of 4
   7       message/partial           47K part 3 of 4
   8       message/partial           18K part 4 of 4
% mhstore 5-8
reassembling partials 5,6,7,8 to folder inbox as message 9
% mhlist -verbose 9
 msg part  type/subtype             size description
   9       application/octet-stream 118K
             (extract with uncompress | tar xvpf -)
             type=tar
             conversions=compress
</pre>
</dl>
<p> This will store exactly one message, containing the sum of the parts. It doesn&#8217;t matter whether the partials are specified in order, since <code>mhstore</code> will sort the partials, so that they are combined in the correct order. But if <code>mhstore</code> can not locate every partial necessary to reassemble the message, it will not store anything.</p>
<h3>External Access</h3>
<p> For contents of type message/external-body, <i>mhstore</i> supports these access-types: </p>
<dl>
<dt>&bull;</p>
<dd> afs</p>
<dt>&bull;</p>
<dd> anon-ftp</p>
<dt>&bull;</p>
<dd> ftp</p>
<dt>&bull;</p>
<dd> local-file</p>
<dt>&bull;</p>
<dd> mail-server</p>
<dt>&bull;</p>
<dd> url</dl>
<p> For the &#8220;anon-ftp&#8221; and &#8220;ftp&#8221; access types, <code>mhstore</code> will look for the &#8220;nmh-access-ftp&#8221; profile entry, e.g., </p>
<dl>
<dt>
<dd> nmh-access-ftp: my<a href="ftp://ftp.sh">ftp.sh</a></dl>
<p> to determine the pathname of a program to perform the FTP retrieval. This program is invoked with these arguments: </p>
<dl>
<dt>
<dd>
<pre>
domain name of FTP-site
username
password
remote directory
remote filename
local filename
``ascii'' or ``binary''
</pre>
</dl>
<p> The program should terminate with an exit status of zero if the retrieval is successful, and a non-zero exit status otherwise. </p>
<p> For the &#8220;url&#8221; access types, <code>mhstore</code> will look for the &#8220;nmh-access-url&#8221; profile entry, e.g., </p>
<dl>
<dt>
<dd> nmh-access-url: curl -L</dl>
<p> to determine the program to use to perform the HTTP retrieval. This program is invoked with one argument: the URL of the content to retrieve. The program should write the content to standard out, and should terminate with a status of zero if the retrieval is successful and a non-zero exit status otherwise. </p>
<h3>The Content Cache</h3>
<p> When <code>mhstore</code> encounters an external content containing a &#8220;Content-ID:&#8221; field, and if the content allows caching, then depending on the caching behavior of <code>mhstore</code>, the content might be read from or written to a cache. </p>
<p> The caching behavior of <code>mhstore</code> is controlled with the <code>-rcache</code> and <code>-wcache</code> switches, which define the policy for reading from, and writing to, the cache, respectively. One of four policies may be specified: &#8220;public&#8221;, indicating that <code>mhstore</code> should make use of a publically-accessible content cache; &#8220;private&#8221;, indicating that <code>mhstore</code> should make use of the user&#8217;s private content cache; &#8220;never&#8221;, indicating that <code>mhstore</code> should never make use of caching; and, &#8220;ask&#8221;, indicating that <code>mhstore</code> should ask the user. </p>
<p> There are two directories where contents may be cached: the profile entry &#8220;nmh-cache&#8221; names a directory containing world-readable contents, and, the profile entry &#8220;nmh-private-cache&#8221; names a directory containing private contents. The former should be an absolute (rooted) directory name. </p>
<p> For example, </p>
<dl>
<dt>
<dd> nmh-cache: /tmp</dl>
<p> might be used if you didn&#8217;t care that the cache got wiped after each reboot of the system. The latter is interpreted relative to the user&#8217;s nmh directory, if not rooted, e.g., </p>
<dl>
<dt>
<dd> nmh-private-cache: .cache</dl>
<p> (which is the default value).</p>
<h3>User Environment</h3>
<p> Because the environment in which <code>mhstore</code> operates may vary for different machines, <code>mhstore</code> will look for the environment variable <code>$MHSTORE</code>. If present, this specifies the name of an additional user profile which should be read. Hence, when a user logs in on a particular machine, this environment variable should be set to refer to a file containing definitions useful for that machine. Finally, <code>mhstore</code> will attempt to consult </p>
<dl>
<dt>
<dd> /etc/nmh/mhn.defaults</dl>
<p> which is created automatically during <code>nmh</code> installation. </p>
<p> See &quot;Profile Lookup&quot; in <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5) for the profile search order, and for how duplicate entries are treated.</p>
<h2>FILES</h2>
<p> <code>mhstore</code> looks for additional profile files in multiple locations: absolute pathnames are accessed directly, tilde expansion is done on usernames, and files are searched for in the user&#8217;s <i>Mail</i> directory as specified in their profile. If not found there, the directory &#8220;<i>/etc/nmh</i>&#8221; is checked. </p>
<pre>
^$HOME/.mh_profile~^The user profile
^$MHSTORE~^Additional profile entries
^/etc/nmh/mhn.defaults~^System default MIME profile entries
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^nmh-access-ftp:~^Program to retrieve contents via FTP
^nmh-access-url:~^Program to retrieve contents via HTTP
^nmh-cache~^Public directory to store cached external contents
^nmh-private-cache~^Personal directory to store cached external contents
^nmh-storage~^Directory to store contents
^mhstore-store-&lt;type&gt;*~^Template for storing contents
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1), <i><a href="/docs/linux/man/1-mhlist/">mhlist</a></i>(1), <i><a href="/docs/linux/man/1-mhshow/">mhshow</a></i>(1), <i><a href="/docs/linux/man/1-sendfiles/">sendfiles</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to cur
`<code>-noauto</code>'
`<code>-clobber always</code>'
`<code>-nocheck</code>'
`<code>-rcache ask</code>'
`<code>-wcache ask</code>'
`<code>-verbose</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The last message selected will become the current message.</p>
<h2>BUGS</h2>
<p> Partial messages contained within a multipart content are not reassembled. </p>
<h2>Index</h2>
