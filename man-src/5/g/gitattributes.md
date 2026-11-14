---
title: "gitattributes(5)"
name: "gitattributes"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gitattributes/"
description: "gitattributes – Defining attributes per path"
---

<p>gitattributes &#8211; Defining attributes per path</p>
<h2>Synopsis</h2>
<p>$GIT_DIR/info/attributes, .gitattributes</p>
<h2>Description</h2>
<p>A <code>gitattributes</code> file is a simple text file that gives <code>attributes</code> to pathnames. </p>
<p> Each line in <code>gitattributes</code> file is of form: </p>
<dl>
<dd>
<pre>pattern attr1 attr2 ...</pre>
</dl>
<p> That is, a pattern followed by an attributes list, separated by whitespaces. Leading and trailing whitespaces are ignored. Lines that begin with <i>#</i> are ignored. Patterns that begin with a double quote are quoted in C style. When the pattern matches the path in question, the attributes listed on the line are given to the path. </p>
<p> Each attribute can be in one of these states for a given path: </p>
<p> Set</p>
<dl>
<dd>The path has the attribute with special value &quot;true&quot;; this is specified by listing only the name of the attribute in the attribute list.</dl>
<p> Unset</p>
<dl>
<dd>The path has the attribute with special value &quot;false&quot;; this is specified by listing the name of the attribute prefixed with a dash <code>&#8211;</code> in the attribute list.</dl>
<p> Set to a value</p>
<dl>
<dd>The path has the attribute with specified string value; this is specified by listing the name of the attribute followed by an equal sign <code>=</code> and its value in the attribute list.</dl>
<p> Unspecified</p>
<dl>
<dd>No pattern matches the path, and nothing says if the path has or does not have the attribute, the attribute for the path is said to be Unspecified.</dl>
<p> When more than one pattern matches the path, a later line overrides an earlier line. This overriding is done per attribute. </p>
<p> The rules by which the pattern matches paths are the same as in <code>.gitignore</code> files (see <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)), with a few exceptions: </p>
<dl>
<dd>&bull; negative patterns are forbidden</dl>
<dl>
<dd>&bull; patterns that match a directory do not recursively match paths inside that directory (so using the trailing-slash <code>path/</code> syntax is pointless in an attributes file; use <code>path/**</code> instead)</dl>
<p> When deciding what attributes are assigned to a path, Git consults <code>$GIT_DIR/info/attributes</code> file (which has the highest precedence), <code>.gitattributes</code> file in the same directory as the path in question, and its parent directories up to the toplevel of the work tree (the further the directory that contains <code>.gitattributes</code> is from the path in question, the lower its precedence). Finally global and system-wide files are considered (they have the lowest precedence). </p>
<p> When the <code>.gitattributes</code> file is missing from the work tree, the path in the index is used as a fall-back. During checkout process, <code>.gitattributes</code> in the index is used and then the file in the working tree is used as a fall-back. </p>
<p> If you wish to affect only a single repository (i.e., to assign attributes to files that are particular to one user&#8217;s workflow for that repository), then attributes should be placed in the <code>$GIT_DIR/info/attributes</code> file. Attributes which should be version-controlled and distributed to other repositories (i.e., attributes of interest to all users) should go into <code>.gitattributes</code> files. Attributes that should affect all repositories for a single user should be placed in a file specified by the <code>core.attributesFile</code> configuration option (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). Its default value is $XDG_CONFIG_HOME/git/attributes. If $XDG_CONFIG_HOME is either not set or empty, $HOME/.config/git/attributes is used instead. Attributes for all users on a system should be placed in the <code>$(prefix)/etc/gitattributes</code> file. </p>
<p> Sometimes you would need to override a setting of an attribute for a path to <code>Unspecified</code> state. This can be done by listing the name of the attribute prefixed with an exclamation point <code>!</code>.</p>
<h2>Effects</h2>
<p>Certain operations by Git can be influenced by assigning particular attributes to a path. Currently, the following operations are attributes-aware.</p>
<h3>Checking-out and checking-in</h3>
<p>These attributes affect how the contents stored in the repository are copied to the working tree files when commands such as <i>git switch</i>, <i>git checkout</i> and <i>git merge</i> run. They also affect how Git stores the contents you prepare in the working tree in the repository upon <i>git add</i> and <i>git commit</i>. </p>
<p> <font SIZE="+1"> <code>text</code></p>
<dl>
<dd>This attribute enables and controls end-of-line normalization. When a text file is normalized, its line endings are converted to LF in the repository. To control what line ending style is used in the working directory, use the <code>eol</code> attribute for a single file and the <code>core.eol</code> configuration variable for all text files. Note that setting <code>core.autocrlf</code> to <code>true</code> or <code>input</code> overrides <code>core.eol</code> (see the definitions of those options in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> Set</p>
<dl>
<dd>Setting the <code>text</code> attribute on a path enables end-of-line normalization and marks the path as a text file. End-of-line conversion takes place without guessing the content type.</dl>
<p> Unset</p>
<dl>
<dd>Unsetting the <code>text</code> attribute on a path tells Git not to attempt any end-of-line conversion upon checkin or checkout.</dl>
<p> Set to string value &quot;auto&quot;</p>
<dl>
<dd>When <code>text</code> is set to &quot;auto&quot;, the path is marked for automatic end-of-line conversion. If Git decides that the content is text, its line endings are converted to LF on checkin. When the file has been committed with CRLF, no conversion is done.</dl>
<p> Unspecified</p>
<dl>
<dd>If the <code>text</code> attribute is unspecified, Git uses the <code>core.autocrlf</code> configuration variable to determine if the file should be converted.</dl>
<p> Any other value causes Git to act as if <code>text</code> has been left unspecified.</dl>
<p> </font><font SIZE="+2"> <code>eol</code></p>
<dl>
<dd>This attribute sets a specific line-ending style to be used in the working directory. It enables end-of-line conversion without any content checks, effectively setting the <code>text</code> attribute. Note that setting this attribute on paths which are in the index with CRLF line endings may make the paths to be considered dirty. Adding the path to the index again will normalize the line endings in the index. </p>
<p> Set to string value &quot;crlf&quot;</p>
<dl>
<dd>This setting forces Git to normalize line endings for this file on checkin and convert them to CRLF when the file is checked out.</dl>
<p> Set to string value &quot;lf&quot;</p>
<dl>
<dd>This setting forces Git to normalize line endings to LF on checkin and prevents conversion to CRLF when the file is checked out.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Backwards compatibility with crlf attribute</code></p>
<dl>
<dd>For backwards compatibility, the <code>crlf</code> attribute is interpreted as follows: </p>
<dl>
<dd></font></p>
<pre>crlf text
-crlf -text
crlf=input eol=lf</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>End-of-line conversion</code></p>
<dl>
<dd>While Git normally leaves file contents alone, it can be configured to normalize line endings to LF in the repository and, optionally, to convert them to CRLF when files are checked out. </p>
<p> If you simply want to have CRLF line endings in your working directory regardless of the repository you are working with, you can set the config variable &quot;core.autocrlf&quot; without using any attributes. </p>
<dl>
<dd></font></p>
<pre>[core]
 autocrlf = true</pre>
</dl>
<p> This does not force normalization of text files, but does ensure that text files that you introduce to the repository have their line endings normalized to LF when they are added, and that files that are already normalized in the repository stay normalized. </p>
<p> If you want to ensure that text files that any contributor introduces to the repository have their line endings normalized, you can set the <code>text</code> attribute to &quot;auto&quot; for <i>all</i> files. </p>
<dl>
<dd>
<pre>* text=auto</pre>
</dl>
<p> The attributes allow a fine-grained control, how the line endings are converted. Here is an example that will make Git normalize .txt, .vcproj and .sh files, ensure that .vcproj files have CRLF and .sh files have LF in the working directory, and prevent .jpg files from being normalized regardless of their content. </p>
<dl>
<dd>
<pre>* text=auto
*.txt text
*.vcproj text eol=crlf
*.sh text eol=lf
*.jpg -text</pre>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> When <code>text=auto</code> conversion is enabled in a cross-platform project using push and pull to a central repository the text files containing CRLFs should be normalized. </p>
</dl>
<p> From a clean working directory: </p>
<dl>
<dd>
<pre>$ echo &quot;* text=auto&quot; &gt;.gitattributes
$ git add --renormalize .
$ git status # Show files that will be normalized
$ git commit -m &quot;Introduce end-of-line normalization&quot;</pre>
</dl>
<p> If any files that should not be normalized show up in <i>git status</i>, unset their <code>text</code> attribute before running <i>git add -u</i>. </p>
<dl>
<dd>
<pre>manual.pdf -text</pre>
</dl>
<p> Conversely, text files that Git does not detect can have normalization enabled manually. </p>
<dl>
<dd>
<pre>weirdchars.txt text</pre>
</dl>
<p> If <code>core.safecrlf</code> is set to &quot;true&quot; or &quot;warn&quot;, Git verifies if the conversion is reversible for the current setting of <code>core.autocrlf</code>. For &quot;true&quot;, Git rejects irreversible conversions; for &quot;warn&quot;, Git only prints a warning but accepts an irreversible conversion. The safety triggers to prevent such a conversion done to the files in the work tree, but there are a few exceptions. Even though&#8230; </p>
<dl>
<dd>&bull; <i>git add</i> itself does not touch the files in the work tree, the next checkout would, so the safety triggers;</dl>
<dl>
<dd>&bull; <i>git apply</i> to update a text file with a patch does touch the files in the work tree, but the operation is about text files and CRLF conversion is about fixing the line ending inconsistencies, so the safety does not trigger;</dl>
<dl>
<dd>&bull; <i>git diff</i> itself does not touch the files in the work tree, it is often run to inspect the changes you intend to next <i>git add</i>. To catch potential problems early, safety triggers.</dl>
</dl>
<p> <font SIZE="+1"> <code>working-tree-encoding</code></p>
<dl>
<dd>Git recognizes files encoded in ASCII or one of its supersets (e.g. UTF-8, ISO-8859-1, &#8230;) as text files. Files encoded in certain other encodings (e.g. UTF-16) are interpreted as binary and consequently built-in Git text processing tools (e.g. <i>git diff</i>) as well as most Git web front ends do not visualize the contents of these files by default. </p>
<p> In these cases you can tell Git the encoding of a file in the working directory with the <code>working-tree-encoding</code> attribute. If a file with this attribute is added to Git, then Git re-encodes the content from the specified encoding to UTF-8. Finally, Git stores the UTF-8 encoded content in its internal data structure (called &quot;the index&quot;). On checkout the content is re-encoded back to the specified encoding. </p>
<p> Please note that using the <code>working-tree-encoding</code> attribute may have a number of pitfalls: </p>
<dl>
<dd>&bull; Alternative Git implementations (e.g. JGit or libgit2) and older Git versions (as of March 2018) do not support the <code>working-tree-encoding</code> attribute. If you decide to use the <code>working-tree-encoding</code> attribute in your repository, then it is strongly recommended to ensure that all clients working with the repository support it. </p>
<p> For example, Microsoft Visual Studio resources files (<code>*.rc</code>) or PowerShell script files (<code>*.ps1</code>) are sometimes encoded in UTF-16. If you declare <code>*.ps1</code> as files as UTF-16 and you add <code>foo.ps1</code> with a <code>working-tree-encoding</code> enabled Git client, then <code>foo.ps1</code> will be stored as UTF-8 internally. A client without <code>working-tree-encoding</code> support will checkout <code>foo.ps1</code> as UTF-8 encoded file. This will typically cause trouble for the users of this file. </p>
<p> If a Git client that does not support the <code>working-tree-encoding</code> attribute adds a new file <code>bar.ps1</code>, then <code>bar.ps1</code> will be stored &quot;as-is&quot; internally (in this example probably as UTF-16). A client with <code>working-tree-encoding</code> support will interpret the internal contents as UTF-8 and try to convert it to UTF-16 on checkout. That operation will fail and cause an error.</dl>
<dl>
<dd>&bull; Reencoding content to non-UTF encodings can cause errors as the conversion might not be UTF-8 round trip safe. If you suspect your encoding to not be round trip safe, then add it to <code>core.checkRoundtripEncoding</code> to make Git check the round trip encoding (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). SHIFT-JIS (Japanese character set) is known to have round trip issues with UTF-8 and is checked by default.</dl>
<dl>
<dd>&bull; Reencoding content requires resources that might slow down certain Git operations (e.g <i>git checkout</i> or <i>git add</i>).</dl>
<p> Use the <code>working-tree-encoding</code> attribute only if you cannot store a file in UTF-8 encoding and if you want Git to be able to process the content as text. </p>
<p> As an example, use the following attributes if your <i>*.ps1</i> files are UTF-16 encoded with byte order mark (BOM) and you want Git to perform automatic line ending conversion based on your platform. </p>
<dl>
<dd></font></p>
<pre>*.ps1 text working-tree-encoding=UTF-16</pre>
</dl>
<p> Use the following attributes if your <i>*.ps1</i> files are UTF-16 little endian encoded without BOM and you want Git to use Windows line endings in the working directory (use <code>UTF-16LE-BOM</code> instead of <code>UTF-16LE</code> if you want UTF-16 little endian with BOM). Please note, it is highly recommended to explicitly define the line endings with <code>eol</code> if the <code>working-tree-encoding</code> attribute is used to avoid ambiguity. </p>
<dl>
<dd>
<pre>*.ps1 text working-tree-encoding=UTF-16LE eol=CRLF</pre>
</dl>
<p> You can get a list of all available encodings on your platform with the following command: </p>
<dl>
<dd>
<pre>iconv --list</pre>
</dl>
<p> If you do not know the encoding of a file, then you can use the <code>file</code> command to guess the encoding: </p>
<dl>
<dd>
<pre>file foo.ps1</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>ident</code></p>
<dl>
<dd>When the attribute <code>ident</code> is set for a path, Git replaces <code>$Id$</code> in the blob object with <code>$Id:</code>, followed by the 40-character hexadecimal blob object name, followed by a dollar sign <code>$</code> upon checkout. Any byte sequence that begins with <code>$Id:</code> and ends with <code>$</code> in the worktree file is replaced with <code>$Id$</code> upon check-in.</dl>
<p> </font><font SIZE="+2"> <code>filter</code></p>
<dl>
<dd>A <code>filter</code> attribute can be set to a string value that names a filter driver specified in the configuration. </p>
<p> A filter driver consists of a <code>clean</code> command and a <code>smudge</code> command, either of which can be left unspecified. Upon checkout, when the <code>smudge</code> command is specified, the command is fed the blob object from its standard input, and its standard output is used to update the worktree file. Similarly, the <code>clean</code> command is used to convert the contents of worktree file upon checkin. By default these commands process only a single blob and terminate. If a long running <code>process</code> filter is used in place of <code>clean</code> and/or <code>smudge</code> filters, then Git can process all blobs with a single filter command invocation for the entire life of a single Git command, for example <code>git add &#8211;all</code>. If a long running <code>process</code> filter is configured then it always takes precedence over a configured single blob filter. See section below for the description of the protocol used to communicate with a <code>process</code> filter. </p>
<p> One use of the content filtering is to massage the content into a shape that is more convenient for the platform, filesystem, and the user to use. For this mode of operation, the key phrase here is &quot;more convenient&quot; and not &quot;turning something unusable into usable&quot;. In other words, the intent is that if someone unsets the filter driver definition, or does not have the appropriate filter program, the project should still be usable. </p>
<p> Another use of the content filtering is to store the content that cannot be directly used in the repository (e.g. a UUID that refers to the true content stored outside Git, or an encrypted content) and turn it into a usable form upon checkout (e.g. download the external content, or decrypt the encrypted content). </p>
<p> These two filters behave differently, and by default, a filter is taken as the former, massaging the contents into more convenient shape. A missing filter driver definition in the config, or a filter driver that exits with a non-zero status, is not an error but makes the filter a no-op passthru. </p>
<p> You can declare that a filter turns a content that by itself is unusable into a usable content by setting the filter.&lt;driver&gt;.required configuration variable to <code>true</code>. </p>
<p> Note: Whenever the clean filter is changed, the repo should be renormalized: $ git add &#8211;renormalize . </p>
<p> For example, in .gitattributes, you would assign the <code>filter</code> attribute for paths. </p>
<dl>
<dd></font></p>
<pre>*.c filter=indent</pre>
</dl>
<p> Then you would define a &quot;filter.indent.clean&quot; and &quot;filter.indent.smudge&quot; configuration in your .git/config to specify a pair of commands to modify the contents of C programs when the source files are checked in (&quot;clean&quot; is run) and checked out (no change is made because the command is &quot;cat&quot;). </p>
<dl>
<dd>
<pre>[filter &quot;indent&quot;]
 clean = indent
 smudge = cat</pre>
</dl>
<p> For best results, <code>clean</code> should not alter its output further if it is run twice (&quot;clean&rarr;clean&quot; should be equivalent to &quot;clean&quot;), and multiple <code>smudge</code> commands should not alter <code>clean</code>&#8216;s output (&quot;smudge&rarr;smudge&rarr;clean&quot; should be equivalent to &quot;clean&quot;). See the section on merging below. </p>
<p> The &quot;indent&quot; filter is well-behaved in this regard: it will not modify input that is already correctly indented. In this case, the lack of a smudge filter means that the clean filter <i>must</i> accept its own output without modifying it. </p>
<p> If a filter <i>must</i> succeed in order to make the stored contents usable, you can declare that the filter is <code>required</code>, in the configuration: </p>
<dl>
<dd>
<pre>[filter &quot;crypt&quot;]
 clean = openssl enc ...
 smudge = openssl enc -d ...
 required</pre>
</dl>
<p> Sequence &quot;%f&quot; on the filter command line is replaced with the name of the file the filter is working on. A filter might use this in keyword substitution. For example: </p>
<dl>
<dd>
<pre>[filter &quot;p4&quot;]
 clean = git-p4-filter --clean %f
 smudge = git-p4-filter --smudge %f</pre>
</dl>
<p> Note that &quot;%f&quot; is the name of the path that is being worked on. Depending on the version that is being filtered, the corresponding file on disk may not exist, or may have different contents. So, smudge and clean commands should not try to access the file on disk, but only act as filters on the content provided to them on standard input.</dl>
<p> <font SIZE="+1"> <code>Long Running Filter Process</code></p>
<dl>
<dd>If the filter command (a string value) is defined via <code>filter.&lt;driver&gt;.process</code> then Git can process all blobs with a single filter invocation for the entire life of a single Git command. This is achieved by using the long-running process protocol (described in technical/long-running-process-protocol.txt). </p>
<p> When Git encounters the first file that needs to be cleaned or smudged, it starts the filter and performs the handshake. In the handshake, the welcome message sent by Git is &quot;git-filter-client&quot;, only version 2 is supported, and the supported capabilities are &quot;clean&quot;, &quot;smudge&quot;, and &quot;delay&quot;. </p>
<p> Afterwards Git sends a list of &quot;key=value&quot; pairs terminated with a flush packet. The list will contain at least the filter command (based on the supported capabilities) and the pathname of the file to filter relative to the repository root. Right after the flush packet Git sends the content split in zero or more pkt-line packets and a flush packet to terminate content. Please note, that the filter must not send any response before it received the content and the final flush packet. Also note that the &quot;value&quot; of a &quot;key=value&quot; pair can contain the &quot;=&quot; character whereas the key would never contain that character. </p>
<dl>
<dd></font></p>
<pre>packet: git&gt; command=smudge
packet: git&gt; pathname=path/testfile.dat
packet: git&gt; 0000
packet: git&gt; CONTENT
packet: git&gt; 0000</pre>
</dl>
<p> The filter is expected to respond with a list of &quot;key=value&quot; pairs terminated with a flush packet. If the filter does not experience problems then the list must contain a &quot;success&quot; status. Right after these packets the filter is expected to send the content in zero or more pkt-line packets and a flush packet at the end. Finally, a second list of &quot;key=value&quot; pairs terminated with a flush packet is expected. The filter can change the status in the second list or keep the status as is with an empty list. Please note that the empty list must be terminated with a flush packet regardless. </p>
<dl>
<dd>
<pre>packet: git&lt; status=success
packet: git&lt; 0000
packet: git&lt; SMUDGED_CONTENT
packet: git&lt; 0000
packet: git&lt; 0000 # empty list, keep &quot;status=success&quot; unchanged!</pre>
</dl>
<p> If the result content is empty then the filter is expected to respond with a &quot;success&quot; status and a flush packet to signal the empty content. </p>
<dl>
<dd>
<pre>packet: git&lt; status=success
packet: git&lt; 0000
packet: git&lt; 0000 # empty content!
packet: git&lt; 0000 # empty list, keep &quot;status=success&quot; unchanged!</pre>
</dl>
<p> In case the filter cannot or does not want to process the content, it is expected to respond with an &quot;error&quot; status. </p>
<dl>
<dd>
<pre>packet: git&lt; status=error
packet: git&lt; 0000</pre>
</dl>
<p> If the filter experiences an error during processing, then it can send the status &quot;error&quot; after the content was (partially or completely) sent. </p>
<dl>
<dd>
<pre>packet: git&lt; status=success
packet: git&lt; 0000
packet: git&lt; HALF_WRITTEN_ERRONEOUS_CONTENT
packet: git&lt; 0000
packet: git&lt; status=error
packet: git&lt; 0000</pre>
</dl>
<p> In case the filter cannot or does not want to process the content as well as any future content for the lifetime of the Git process, then it is expected to respond with an &quot;abort&quot; status at any point in the protocol. </p>
<dl>
<dd>
<pre>packet: git&lt; status=abort
packet: git&lt; 0000</pre>
</dl>
<p> Git neither stops nor restarts the filter process in case the &quot;error&quot;/&quot;abort&quot; status is set. However, Git sets its exit code according to the <code>filter.&lt;driver&gt;.required</code> flag, mimicking the behavior of the <code>filter.&lt;driver&gt;.clean</code> / <code>filter.&lt;driver&gt;.smudge</code> mechanism. </p>
<p> If the filter dies during the communication or does not adhere to the protocol then Git will stop the filter process and restart it with the next file that needs to be processed. Depending on the <code>filter.&lt;driver&gt;.required</code> flag Git will interpret that as error.</dl>
<p> <font SIZE="+1"> <code>Delay</code></p>
<dl>
<dd>If the filter supports the &quot;delay&quot; capability, then Git can send the flag &quot;can-delay&quot; after the filter command and pathname. This flag denotes that the filter can delay filtering the current blob (e.g. to compensate network latencies) by responding with no content but with the status &quot;delayed&quot; and a flush packet. </p>
<dl>
<dd></font></p>
<pre>packet: git&gt; command=smudge
packet: git&gt; pathname=path/testfile.dat
packet: git&gt; can-delay=1
packet: git&gt; 0000
packet: git&gt; CONTENT
packet: git&gt; 0000
packet: git&lt; status=delayed
packet: git&lt; 0000</pre>
</dl>
<p> If the filter supports the &quot;delay&quot; capability then it must support the &quot;list_available_blobs&quot; command. If Git sends this command, then the filter is expected to return a list of pathnames representing blobs that have been delayed earlier and are now available. The list must be terminated with a flush packet followed by a &quot;success&quot; status that is also terminated with a flush packet. If no blobs for the delayed paths are available, yet, then the filter is expected to block the response until at least one blob becomes available. The filter can tell Git that it has no more delayed blobs by sending an empty list. As soon as the filter responds with an empty list, Git stops asking. All blobs that Git has not received at this point are considered missing and will result in an error. </p>
<dl>
<dd>
<pre>packet: git&gt; command=list_available_blobs
packet: git&gt; 0000
packet: git&lt; pathname=path/testfile.dat
packet: git&lt; pathname=path/otherfile.dat
packet: git&lt; 0000
packet: git&lt; status=success
packet: git&lt; 0000</pre>
</dl>
<p> After Git received the pathnames, it will request the corresponding blobs again. These requests contain a pathname and an empty content section. The filter is expected to respond with the smudged content in the usual way as explained above. </p>
<dl>
<dd>
<pre>packet: git&gt; command=smudge
packet: git&gt; pathname=path/testfile.dat
packet: git&gt; 0000
packet: git&gt; 0000 # empty content!
packet: git&lt; status=success
packet: git&lt; 0000
packet: git&lt; SMUDGED_CONTENT
packet: git&lt; 0000
packet: git&lt; 0000 # empty list, keep &quot;status=success&quot; unchanged!</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dd>A long running filter demo implementation can be found in <code>contrib/long-running-filter/example.pl</code> located in the Git core repository. If you develop your own long running filter process then the <code>GIT_TRACE_PACKET</code> environment variables can be very helpful for debugging (see <code><a href="/docs/linux/man/1-git/">git</a></code>(1)). </p>
<p> Please note that you cannot use an existing <code>filter.&lt;driver&gt;.clean</code> or <code>filter.&lt;driver&gt;.smudge</code> command with <code>filter.&lt;driver&gt;.process</code> because the former two use a different inter process communication protocol than the latter one.</dl>
<p> </font><font SIZE="+2"> <code>Interaction between checkin/checkout attributes</code></p>
<dl>
<dd>In the check-in codepath, the worktree file is first converted with <code>filter</code> driver (if specified and corresponding driver defined), then the result is processed with <code>ident</code> (if specified), and then finally with <code>text</code> (again, if specified and applicable). </p>
<p> In the check-out codepath, the blob content is first converted with <code>text</code>, and then <code>ident</code> and fed to <code>filter</code>.</dl>
<p> </font><font SIZE="+3"> <code>Merging branches with differing checkin/checkout attributes</code></p>
<dl>
<dd>If you have added attributes to a file that cause the canonical repository format for that file to change, such as adding a clean/smudge filter or text/eol/ident attributes, merging anything where the attribute is not in place would normally cause merge conflicts. </p>
<p> To prevent these unnecessary merge conflicts, Git can be told to run a virtual check-out and check-in of all three stages of a file when resolving a three-way merge by setting the <code>merge.renormalize</code> configuration variable. This prevents changes caused by check-in conversion from causing spurious merge conflicts when a converted file is merged with an unconverted file. </p>
<p> As long as a &quot;smudge&rarr;clean&quot; results in the same output as a &quot;clean&quot; even on files that are already smudged, this strategy will automatically resolve all filter-related conflicts. Filters that do not act in this way may cause additional merge conflicts that must be resolved manually.</dl>
<p> </font></p>
<h3>Generating diff text</h3>
<p><font SIZE="+1"> <code>diff</code></p>
<dl>
<dd>The attribute <code>diff</code> affects how Git generates diffs for particular files. It can tell Git whether to generate a textual patch for the path or to treat the path as a binary file. It can also affect what line is shown on the hunk header <code>@@ -k,l +n,m @@</code> line, tell Git to use an external command to generate the diff, or ask Git to convert binary files to a text format before generating the diff. </p>
<p> Set</p>
<dl>
<dd>A path to which the <code>diff</code> attribute is set is treated as text, even when they contain byte values that normally never appear in text files, such as NUL.</dl>
<p> Unset</p>
<dl>
<dd>A path to which the <code>diff</code> attribute is unset will generate <code>Binary files differ</code> (or a binary patch, if binary patches are enabled).</dl>
<p> Unspecified</p>
<dl>
<dd>A path to which the <code>diff</code> attribute is unspecified first gets its contents inspected, and if it looks like text and is smaller than core.bigFileThreshold, it is treated as text. Otherwise it would generate <code>Binary files differ</code>.</dl>
<p> String</p>
<dl>
<dd>Diff is shown using the specified diff driver. Each driver may specify one or more options, as described in the following section. The options for the diff driver &quot;foo&quot; are defined by the configuration variables in the &quot;diff.foo&quot; section of the Git config file.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Defining an external diff driver</code></p>
<dl>
<dd>The definition of a diff driver is done in <code>gitconfig</code>, not <code>gitattributes</code> file, so strictly speaking this manual page is a wrong place to talk about it. However&#8230; </p>
<p> To define an external diff driver <code>jcdiff</code>, add a section to your <code>$GIT_DIR/config</code> file (or <code>$HOME/.gitconfig</code> file) like this: </p>
<dl>
<dd></font></p>
<pre>[diff &quot;jcdiff&quot;]
 command = j-c-diff</pre>
</dl>
<p> When Git needs to show you a diff for the path with <code>diff</code> attribute set to <code>jcdiff</code>, it calls the command you specified with the above configuration, i.e. <code>j-c-diff</code>, with 7 parameters, just like <code>GIT_EXTERNAL_DIFF</code> program is called. See <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for details.</dl>
<p> <font SIZE="+1"> <code>Defining a custom hunk-header</code></p>
<dl>
<dd>Each group of changes (called a &quot;hunk&quot;) in the textual diff output is prefixed with a line of the form: </p>
<dl>
<dd></font></p>
<pre>@@ -k,l +n,m @@ TEXT</pre>
</dl>
<p> This is called a <i>hunk header</i>. The &quot;TEXT&quot; portion is by default a line that begins with an alphabet, an underscore or a dollar sign; this matches what GNU <i>diff -p</i> output uses. This default selection however is not suited for some contents, and you can use a customized pattern to make a selection. </p>
<p> First, in .gitattributes, you would assign the <code>diff</code> attribute for paths. </p>
<dl>
<dd>
<pre>*.tex diff=tex</pre>
</dl>
<p> Then, you would define a &quot;diff.tex.xfuncname&quot; configuration to specify a regular expression that matches a line that you would want to appear as the hunk header &quot;TEXT&quot;. Add a section to your <code>$GIT_DIR/config</code> file (or <code>$HOME/.gitconfig</code> file) like this: </p>
<dl>
<dd>
<pre>[diff &quot;tex&quot;]
 xfuncname = &quot;^(\\(sub)*section\{.*)$&quot;</pre>
</dl>
<p> Note. A single level of backslashes are eaten by the configuration file parser, so you would need to double the backslashes; the pattern above picks a line that begins with a backslash, and zero or more occurrences of <code>sub</code> followed by <code>section</code> followed by open brace, to the end of line. </p>
<p> There are a few built-in patterns to make this easier, and <code>tex</code> is one of them, so you do not have to write the above in your configuration file (you still need to enable this with the attribute mechanism, via <code>.gitattributes</code>). The following built in patterns are available: </p>
<dl>
<dd>&bull; <code>ada</code> suitable for source code in the Ada language.</dl>
<dl>
<dd>&bull; <code>bash</code> suitable for source code in the Bourne-Again SHell language. Covers a superset of POSIX shell function definitions.</dl>
<dl>
<dd>&bull; <code>bibtex</code> suitable for files with BibTeX coded references.</dl>
<dl>
<dd>&bull; <code>cpp</code> suitable for source code in the C and C++ languages.</dl>
<dl>
<dd>&bull; <code>csharp</code> suitable for source code in the C# language.</dl>
<dl>
<dd>&bull; <code>css</code> suitable for cascading style sheets.</dl>
<dl>
<dd>&bull; <code>dts</code> suitable for devicetree (DTS) files.</dl>
<dl>
<dd>&bull; <code>elixir</code> suitable for source code in the Elixir language.</dl>
<dl>
<dd>&bull; <code>fortran</code> suitable for source code in the Fortran language.</dl>
<dl>
<dd>&bull; <code>fountain</code> suitable for Fountain documents.</dl>
<dl>
<dd>&bull; <code>golang</code> suitable for source code in the Go language.</dl>
<dl>
<dd>&bull; <code>html</code> suitable for HTML/XHTML documents.</dl>
<dl>
<dd>&bull; <code>java</code> suitable for source code in the Java language.</dl>
<dl>
<dd>&bull; <code>markdown</code> suitable for Markdown documents.</dl>
<dl>
<dd>&bull; <code>matlab</code> suitable for source code in the MATLAB and Octave languages.</dl>
<dl>
<dd>&bull; <code>objc</code> suitable for source code in the Objective-C language.</dl>
<dl>
<dd>&bull; <code>pascal</code> suitable for source code in the Pascal/Delphi language.</dl>
<dl>
<dd>&bull; <code>perl</code> suitable for source code in the Perl language.</dl>
<dl>
<dd>&bull; <code>php</code> suitable for source code in the PHP language.</dl>
<dl>
<dd>&bull; <code>python</code> suitable for source code in the Python language.</dl>
<dl>
<dd>&bull; <code>ruby</code> suitable for source code in the Ruby language.</dl>
<dl>
<dd>&bull; <code>rust</code> suitable for source code in the Rust language.</dl>
<dl>
<dd>&bull; <code>scheme</code> suitable for source code in the Scheme language.</dl>
<dl>
<dd>&bull; <code>tex</code> suitable for source code for LaTeX documents.</dl>
</dl>
<p> <font SIZE="+1"> <code>Customizing word diff</code></p>
<dl>
<dd>You can customize the rules that <code>git diff &#8211;word-diff</code> uses to split words in a line, by specifying an appropriate regular expression in the &quot;diff.*.wordRegex&quot; configuration variable. For example, in TeX a backslash followed by a sequence of letters forms a command, but several such commands can be run together without intervening whitespace. To separate them, use a regular expression in your <code>$GIT_DIR/config</code> file (or <code>$HOME/.gitconfig</code> file) like this: </p>
<dl>
<dd></font></p>
<pre>[diff &quot;tex&quot;]
 wordRegex = &quot;\\[a-zA-Z]+|[{}]|\\.|[^\{}[:space:]]+&quot;</pre>
</dl>
<p> A built-in pattern is provided for all languages listed in the previous section.</dl>
<p> <font SIZE="+1"> <code>Performing text diffs of binary files</code></p>
<dl>
<dd>Sometimes it is desirable to see the diff of a text-converted version of some binary files. For example, a word processor document can be converted to an ASCII text representation, and the diff of the text shown. Even though this conversion loses some information, the resulting diff is useful for human viewing (but cannot be applied directly). </p>
<p> The <code>textconv</code> config option is used to define a program for performing such a conversion. The program should take a single argument, the name of a file to convert, and produce the resulting text on stdout. </p>
<p> For example, to show the diff of the exif information of a file instead of the binary information (assuming you have the exif tool installed), add the following section to your <code>$GIT_DIR/config</code> file (or <code>$HOME/.gitconfig</code> file): </p>
<dl>
<dd></font></p>
<pre>[diff &quot;jpg&quot;]
 textconv = exif</pre>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The text conversion is generally a one-way conversion; in this example, we lose the actual image contents and focus just on the text data. This means that diffs generated by textconv are <i>not</i> suitable for applying. For this reason, only <code>git diff</code> and the <code>git log</code> family of commands (i.e., log, whatchanged, show) will perform text conversion. <code>git format-patch</code> will never generate this output. If you want to send somebody a text-converted diff of a binary file (e.g., because it quickly conveys the changes you have made), you should generate it separately and send it as a comment <i>in addition to</i> the usual binary diff that you might send. </p>
</dl>
<p> Because text conversion can be slow, especially when doing a large number of them with <code>git log -p</code>, Git provides a mechanism to cache the output and use it in future diffs. To enable caching, set the &quot;cachetextconv&quot; variable in your diff driver&#8217;s config. For example: </p>
<dl>
<dd>
<pre>[diff &quot;jpg&quot;]
 textconv = exif
 cachetextconv = true</pre>
</dl>
<p> This will cache the result of running &quot;exif&quot; on each blob indefinitely. If you change the textconv config variable for a diff driver, Git will automatically invalidate the cache entries and re-run the textconv filter. If you want to invalidate the cache manually (e.g., because your version of &quot;exif&quot; was updated and now produces better output), you can remove the cache manually with <code>git update-ref -d refs/notes/textconv/jpg</code> (where &quot;jpg&quot; is the name of the diff driver, as in the example above).</dl>
<p> <font SIZE="+1"> <code>Choosing textconv versus external diff</code></p>
<dl>
<dd>If you want to show differences between binary or specially-formatted blobs in your repository, you can choose to use either an external diff command, or to use textconv to convert them to a diff-able text format. Which method you choose depends on your exact situation. </p>
<p> The advantage of using an external diff command is flexibility. You are not bound to find line-oriented changes, nor is it necessary for the output to resemble unified diff. You are free to locate and report changes in the most appropriate way for your data format. </p>
<p> A textconv, by comparison, is much more limiting. You provide a transformation of the data into a line-oriented text format, and Git uses its regular diff tools to generate the output. There are several advantages to choosing this method: </p>
<dl>
<dd>1. Ease of use. It is often much simpler to write a binary to text transformation than it is to perform your own diff. In many cases, existing programs can be used as textconv filters (e.g., exif, odt2txt).</dl>
<dl>
<dd>2. Git diff features. By performing only the transformation step yourself, you can still utilize many of Git&#8217;s diff features, including colorization, word-diff, and combined diffs for merges.</dl>
<dl>
<dd>3. Caching. Textconv caching can speed up repeated diffs, such as those you might trigger by running <code>git log -p</code>.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Marking files as binary</code></p>
<dl>
<dd>Git usually guesses correctly whether a blob contains text or binary data by examining the beginning of the contents. However, sometimes you may want to override its decision, either because a blob contains binary data later in the file, or because the content, while technically composed of text characters, is opaque to a human reader. For example, many postscript files contain only ASCII characters, but produce noisy and meaningless diffs. </p>
<p> The simplest way to mark a file as binary is to unset the diff attribute in the <code>.gitattributes</code> file: </p>
<dl>
<dd></font></p>
<pre>*.ps -diff</pre>
</dl>
<p> This will cause Git to generate <code>Binary files differ</code> (or a binary patch, if binary patches are enabled) instead of a regular diff. </p>
<p> However, one may also want to specify other diff driver attributes. For example, you might want to use <code>textconv</code> to convert postscript files to an ASCII representation for human viewing, but otherwise treat them as binary files. You cannot specify both <code>-diff</code> and <code>diff=ps</code> attributes. The solution is to use the <code>diff.*.binary</code> config option: </p>
<dl>
<dd>
<pre>[diff &quot;ps&quot;]
 textconv = ps2ascii
 binary = true</pre>
</dl>
</dl>
<h3>Performing a three-way merge</h3>
<p><font SIZE="+1"> <code>merge</code></p>
<dl>
<dd>The attribute <code>merge</code> affects how three versions of a file are merged when a file-level merge is necessary during <code>git merge</code>, and other commands such as <code>git revert</code> and <code>git cherry-pick</code>. </p>
<p> Set</p>
<dl>
<dd>Built-in 3-way merge driver is used to merge the contents in a way similar to <i>merge</i> command of <code>RCS</code> suite. This is suitable for ordinary text files.</dl>
<p> Unset</p>
<dl>
<dd>Take the version from the current branch as the tentative merge result, and declare that the merge has conflicts. This is suitable for binary files that do not have a well-defined merge semantics.</dl>
<p> Unspecified</p>
<dl>
<dd>By default, this uses the same built-in 3-way merge driver as is the case when the <code>merge</code> attribute is set. However, the <code>merge.default</code> configuration variable can name different merge driver to be used with paths for which the <code>merge</code> attribute is unspecified.</dl>
<p> String</p>
<dl>
<dd>3-way merge is performed using the specified custom merge driver. The built-in 3-way merge driver can be explicitly specified by asking for &quot;text&quot; driver; the built-in &quot;take the current branch&quot; driver can be requested with &quot;binary&quot;.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Built-in merge drivers</code></p>
<dl>
<dd>There are a few built-in low-level merge drivers defined that can be asked for via the <code>merge</code> attribute. </p>
<p> text</p>
<dl>
<dd>Usual 3-way file level merge for text files. Conflicted regions are marked with conflict markers <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code>, <code>=======</code> and <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code>. The version from your branch appears before the <code>=======</code> marker, and the version from the merged branch appears after the <code>=======</code> marker.</dl>
<p> binary</p>
<dl>
<dd>Keep the version from your branch in the work tree, but leave the path in the conflicted state for the user to sort out.</dl>
<p> union</p>
<dl>
<dd>Run 3-way file level merge for text files, but take lines from both versions, instead of leaving conflict markers. This tends to leave the added lines in the resulting file in random order and the user should verify the result. Do not use this if you do not understand the implications.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Defining a custom merge driver</code></p>
<dl>
<dd>The definition of a merge driver is done in the <code>.git/config</code> file, not in the <code>gitattributes</code> file, so strictly speaking this manual page is a wrong place to talk about it. However&#8230; </p>
<p> To define a custom merge driver <code>filfre</code>, add a section to your <code>$GIT_DIR/config</code> file (or <code>$HOME/.gitconfig</code> file) like this: </p>
<dl>
<dd></font></p>
<pre>[merge &quot;filfre&quot;]
 name = feel-free merge driver
 driver = filfre %O %A %B %L %P
 recursive = binary</pre>
</dl>
<p> The <code>merge.*.name</code> variable gives the driver a human-readable name. </p>
<p> The &#8216;merge.*.driver` variable&#8217;s value is used to construct a command to run to merge ancestor&#8217;s version (<code>%O</code>), current version (<code>%A</code>) and the other branches&#8217; version (<code>%B</code>). These three tokens are replaced with the names of temporary files that hold the contents of these versions when the command line is built. Additionally, %L will be replaced with the conflict marker size (see below). </p>
<p> The merge driver is expected to leave the result of the merge in the file named with <code>%A</code> by overwriting it, and exit with zero status if it managed to merge them cleanly, or non-zero if there were conflicts. </p>
<p> The <code>merge.*.recursive</code> variable specifies what other merge driver to use when the merge driver is called for an internal merge between common ancestors, when there are more than one. When left unspecified, the driver itself is used for both internal merge and the final merge. </p>
<p> The merge driver can learn the pathname in which the merged result will be stored via placeholder <code>%P</code>.</dl>
<p> <font SIZE="+1"> <code>conflict-marker-size</code></p>
<dl>
<dd>This attribute controls the length of conflict markers left in the work tree file during a conflicted merge. Only setting to the value to a positive integer has any meaningful effect. </p>
<p> For example, this line in <code>.gitattributes</code> can be used to tell the merge machinery to leave much longer (instead of the usual 7-character-long) conflict markers when merging the file <code>Documentation/git-merge.txt</code> results in a conflict. </p>
<dl>
<dd></font></p>
<pre>Documentation/git-merge.txt conflict-marker-size=32</pre>
</dl>
</dl>
<h3>Checking whitespace errors</h3>
<p><font SIZE="+1"> <code>whitespace</code></p>
<dl>
<dd>The <code>core.whitespace</code> configuration variable allows you to define what <i>diff</i> and <i>apply</i> should consider whitespace errors for all paths in the project (See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). This attribute gives you finer control per path. </p>
<p> Set</p>
<dl>
<dd>Notice all types of potential whitespace errors known to Git. The tab width is taken from the value of the <code>core.whitespace</code> configuration variable.</dl>
<p> Unset</p>
<dl>
<dd>Do not notice anything as error.</dl>
<p> Unspecified</p>
<dl>
<dd>Use the value of the <code>core.whitespace</code> configuration variable to decide what to notice as error.</dl>
<p> String</p>
<dl>
<dd>Specify a comma separate list of common whitespace problems to notice in the same format as the <code>core.whitespace</code> configuration variable.</dl>
</dl>
<p> </font></p>
<h3>Creating an archive</h3>
<p><font SIZE="+1"> <code>export-ignore</code></p>
<dl>
<dd>Files and directories with the attribute <code>export-ignore</code> won&#8217;t be added to archive files.</dl>
<p> </font><font SIZE="+2"> <code>export-subst</code></p>
<dl>
<dd>If the attribute <code>export-subst</code> is set for a file then Git will expand several placeholders when adding this file to an archive. The expansion depends on the availability of a commit ID, i.e., if <code><a href="/docs/linux/man/1-git-archive/">git-archive</a></code>(1) has been given a tree instead of a commit or a tag then no replacement will be done. The placeholders are the same as those for the option <code>&#8211;pretty=format:</code> of <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), except that they need to be wrapped like this: <code>$Format:PLACEHOLDERS$</code> in the file. E.g. the string <code>$Format:%H$</code> will be replaced by the commit hash. However, only one <code>%(describe)</code> placeholder is expanded per archive to avoid denial-of-service attacks.</dl>
<p> </font></p>
<h3>Packing objects</h3>
<p><font SIZE="+1"> <code>delta</code></p>
<dl>
<dd>Delta compression will not be attempted for blobs for paths with the attribute <code>delta</code> set to false.</dl>
<p> </font></p>
<h3>Viewing files in GUI tools</h3>
<p><font SIZE="+1"> <code>encoding</code></p>
<dl>
<dd>The value of this attribute specifies the character encoding that should be used by GUI tools (e.g. <code><a href="/docs/linux/man/1-gitk/">gitk</a></code>(1) and <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1)) to display the contents of the relevant file. Note that due to performance considerations <code><a href="/docs/linux/man/1-gitk/">gitk</a></code>(1) does not use this attribute unless you manually enable per-file encodings in its options. </p>
<p> If this attribute is not set or has an invalid value, the value of the <code>gui.encoding</code> configuration variable is used instead (See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> </font></p>
<h2>Using Macro Attributes</h2>
<p>You do not want any end-of-line conversions applied to, nor textual diffs produced for, any binary file you track. You would need to specify e.g. </p>
<dl>
<dd>
<pre>*.jpg -text -diff</pre>
</dl>
<p> but that may become cumbersome, when you have many attributes. Using macro attributes, you can define an attribute that, when set, also sets or unsets a number of other attributes at the same time. The system knows a built-in macro attribute, <code>binary</code>: </p>
<dl>
<dd>
<pre>*.jpg binary</pre>
</dl>
<p> Setting the &quot;binary&quot; attribute also unsets the &quot;text&quot; and &quot;diff&quot; attributes as above. Note that macro attributes can only be &quot;Set&quot;, though setting one might have the effect of setting or unsetting other attributes or even returning other attributes to the &quot;Unspecified&quot; state.</p>
<h2>Defining Macro Attributes</h2>
<p>Custom macro attributes can be defined only in top-level gitattributes files (<code>$GIT_DIR/info/attributes</code>, the <code>.gitattributes</code> file at the top level of the working tree, or the global or system-wide gitattributes files), not in <code>.gitattributes</code> files in working tree subdirectories. The built-in macro attribute &quot;binary&quot; is equivalent to: </p>
<dl>
<dd>
<pre>[attr]binary -diff -merge -text</pre>
</dl>
<h2>Notes</h2>
<p>Git does not follow symbolic links when accessing a <code>.gitattributes</code> file in the working tree. This keeps behavior consistent when the file is accessed from the index or a tree versus from the filesystem.</p>
<h2>Examples</h2>
<p>If you have these three <code>gitattributes</code> file:</p>
<dl>
<dd>
<pre>(in $GIT_DIR/info/attributes)
a* foo !bar -baz
(in .gitattributes)
abc foo bar baz
(in t/.gitattributes)
ab* merge=filfre
abc -foo -bar
*.c frotz</pre>
</dl>
<p> the attributes given to path <code>t/abc</code> are computed as follows:</p>
<dl>
<dd>1. By examining <code>t/.gitattributes</code> (which is in the same directory as the path in question), Git finds that the first line matches. <code>merge</code> attribute is set. It also finds that the second line matches, and attributes <code>foo</code> and <code>bar</code> are unset.</dl>
<dl>
<dd>2. Then it examines <code>.gitattributes</code> (which is in the parent directory), and finds that the first line matches, but <code>t/.gitattributes</code> file already decided how <code>merge</code>, <code>foo</code> and <code>bar</code> attributes should be given to this path, so it leaves <code>foo</code> and <code>bar</code> unset. Attribute <code>baz</code> is set.</dl>
<dl>
<dd>3. Finally it examines <code>$GIT_DIR/info/attributes</code>. This file is used to override the in-tree settings. The first line is a match, and <code>foo</code> is set, <code>bar</code> is reverted to unspecified state, and <code>baz</code> is unset.</dl>
<p> As the result, the attributes assignment to <code>t/abc</code> becomes:</p>
<dl>
<dd>
<pre>foo set to true
bar unspecified
baz set to false
merge set to string value &quot;filfre&quot;
frotz unspecified</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-git-check-attr/">git-check-attr</a></code>(1).</p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
