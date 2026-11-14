---
title: "update-mime(8)"
name: "update-mime"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-mime/"
description: "update-mime – create or update MIME information"
---

<p>update-mime &#8211; create or update MIME information</p>
<h2>Synopsis</h2>
<p><code>update-mime</code> [no parameters]</p>
<h2>Description</h2>
<p><code>update-mime</code> updates the <code>/etc/mailcap</code> file to reflect mime information changed by a Debian package during installation or removal.</p>
<h3>Options</h3>
<p><code>&#8211;local</code> Generate files in the current user&#8217;s home directory instead of the <i>/etc</i> directory. This allows users to create a custom ordering configuration and get a complete <i>~/.mailcap</i> file out of it. In this local mode, the order overriding file (see below) will be looked for in the <i>~/.mailcap.order</i> file. </p>
<h2>Overriding Order</h2>
<p>The order of entries in the <i>/etc/mailcap</i> file can be altered by editing the <i>/etc/mailcap.order</i> file. Please see the <code><a href="/docs/linux/man/5-mailcap-order/">mailcap.order</a>(5)</code> man page for more information.</p>
<h2>Creating Entries</h2>
<p>To create entries in the mailcap file, packages need to create a file in the <i>/usr/lib/mime/packages</i> directory. In this file goes the verbatim desired mailcap entries. In addition to the standard mailcap options (described below) is a new <i>priority</i> option. Specifying this will provide for simple ranking of programs within a given mime type. An animation viewer, for example, may be able to display a static picture, but probably wouldn&#8217;t be the best choice and so would give an option like &quot;priority=2&quot;. Priorities range from 0 to 9, with 0 being the lowest and 9 being the highest. If the <i>priority</i> option is omitted, a value of 5 is used. </p>
<p> The following are standard options that can be specified in the mailcap entry. Options are separated by semicolons (;) but must all be on the same line. Each line should look like: </p>
<p>&nbsp;<wbr>&nbsp;mime/type;&nbsp;viewer;&nbsp;option;&nbsp;another=val;&nbsp;etc;&nbsp;priority=5 </p>
<p> Mime types of the form &quot;class/*&quot; and even &quot;*/*&quot; are now acceptable (they were previously disallowed). When using &quot;class/*&quot;, it is probably a good idea to add a &quot;priority=[1-4]&quot; option so specific rules using the default priority will get chosen first. If using &quot;*/*&quot;, though, you probably want to add a &quot;priority=0&quot; option to make that rule a &quot;last resort&quot;.</p>
<h3>Commands</h3>
<dl>
<dt><code>&lt;program-string&gt;</code></p>
<dd>Specifies the program to run to view a file of the given content-type. <code>This option setting cannot be omitted.</code> An implicit &quot;view=&quot; can be considered before it. When writing an entry that has no viewer, use a value of <i>false</i> in this space.</p>
<dt><code>compose=&lt;program-string&gt;</code></p>
<dd>The &quot;compose&quot; command may be used to specify a program that can be used to compose a new body or body part in the given format. Its intended use is to support mail composing agents that support the composition of multiple types of mail using external composing agents. The result of the composing program may be data that is not yet suitable for mail transport &#8212; that is, a Content-Transfer-Encoding may need to be applied to the data.</p>
<dt><code>composetyped=&lt;program-string&gt;</code></p>
<dd>The &quot;composetyped&quot; command is similar to &quot;compose&quot;, but is to be used when the composing program needs to specify the Content-type header field to be applied to the composed data. The &quot;compose&quot; option is simpler, and is preferred for use with existing (non-mail-oriented) programs for composing data in a given format. The &quot;composetyped&quot; option is necessary when the Content-type information must include auxiliary parameters, and the composition program must then know enough about mail formats to produce output that includes the mail type information.</p>
<dt><code>edit=&lt;program-string&gt;</code></p>
<dd>The &quot;edit&quot; command may be used to specify a program that can be used to edit a body or body part in the given format. In many cases, it may be identical in content to the &quot;compose&quot; command.</p>
<dt><code>print=&lt;program-string&gt;</code></p>
<dd>The &quot;print&quot; command may be used to specify a program that can be used to print a message or body part in the given format.</dl>
<h3>Modifiers</h3>
<p>These options are modifiers to all the commands specified on the command line.</p>
<dl>
<dt><code>test=&lt;conditional&gt;</code></p>
<dd>The &quot;test&quot; option may be used to test some external condition (e.g., the machine architecture, or the window system in use) to determine whether or not the mailcap line applies. It specifies a program to be run to test some condition. If the test fails, a subsequent mailcap entry will be sought. Multiple test options are not permitted &#8212; since a test can call a program, it can already be arbitrarily complex. </p>
<p> <code>Note:</code> When testing for X by looking at the <i>DISPLAY</i> environment variable, please use one of: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;test=test -z&nbsp;&quot;$DISPLAY&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(no X)<br />
&nbsp;<wbr>&nbsp;or&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;test=test -n&nbsp;&quot;$DISPLAY&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(have X) </p>
<p> Many programs recognize these strings and optimize for them.</p>
<dt><code>needsterminal</code></p>
<dd>The &quot;needsterminal&quot; option, if given, indicates that the commands must be run on an interactive terminal. This is needed to inform window-oriented user agents that an interactive terminal is needed. (The decision is not left exclusively to the command because in some circumstances it may not be possible for such programs to tell whether or not they are on interactive terminals.) The needsterminal command applies to the view, compose and edit commands, if they exist. Note that this is NOT a test &#8212; it is a requirement for the environment in which the program will be executed, and will typically cause the creation of a terminal window when not executed on either a real terminal or a terminal window.</p>
<dt><code>copiousoutput</code></p>
<dd>The &quot;copiousoutput&quot; option, if given, indicates that the output from the view-command will be an extended stream of output and is to be interpreted as advice to the UA (User Agent mail-reading program) that the output should be either paged or made scrollable. Note that it is probably a mistake if needsterminal and copiousoutput are both specified.</dl>
<h3>Content-Type Info</h3>
<p>These options provide additional information about the given content-type.</p>
<dl>
<dt><code>description=&lt;string&gt;</code></p>
<dd>The &quot;description&quot; option simply provides a textual description that describes the type of data, to be used optionally by mail readers that wish to describe the data before offering to display it.</p>
<dt><code>textualnewlines</code></p>
<dd>The &quot;textualnewlines&quot; option, if given, indicates that this type of data is line-oriented and that, if encoded in a binary format, all newlines should be converted to canonical form (CRLF) before encoding, and will be in that form after decoding. In general, this is needed only if there is line-oriented data of some type other than text/* or non-line-oriented data that is a subtype of text.</p>
<dt><code>x11-bitmap=&lt;pathname&gt;</code></p>
<dd>The &quot;x11-bitmap&quot; option names a file, in X11 bitmap (xbm) format, which points to an appropriate icon to be used to visually denote the presence of this kind of data.</p>
<dt><code>nametemplate=&lt;string&gt;</code></p>
<dd>The &quot;nametemplate&quot; option gives a file name format, in which %s will be replaced by a short unique string to give the name of the temporary file to be passed to the viewing command. This is only expected to be relevant in environments where filename extensions are meaningful, e.g., one could specify that a GIF file being passed to a gif viewer should have a name ending in &quot;.gif&quot; by using &quot;nametemplate=%s.gif&quot;.</dl>
<h2>Dependencies</h2>
<p>Packages that wish to provide MIME access to themselves should <code>not</code> depend on, recommend, or suggest <code>mime-support,</code> as the the file they create in <i>/usr/lib/mime/packages</i> will cause <code>update-mime</code> to be automatically run via a Dpkg trigger.</p>
<h2>Desktop Entries</h2>
<p>In addition to the abovementioned mechanism <code>update-mime</code> also parses desktop entries in /usr/share/applications/ to generate mailcap entries. These entries are given a lower priority than those in /usr/lib/mime/packages.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-mailcap-order/">mailcap.order</a></code>(5), <a href="/docs/linux/man/1-deb-triggers/">deb-triggers</a><code>(1), RFC-2046, RFC-1524</code></p>
<h2>Author</h2>
<p><code>update-mime</code> was written by Brian White &lt;bcwhite [at] pobox.com&gt;</p>
<h2>Copyright</h2>
<p><code>update-mime</code> is in the public domain (the only true &quot;free&quot;).</p>
