---
title: "twpolicy(4)"
name: "twpolicy"
section: "4"
letter: "t"
url: "/docs/linux/man/4-twpolicy/"
description: "twpolicy – Tripwire policy file reference"
---

<p>twpolicy &#8211; <i>Tripwire</i> policy file reference</p>
<h2>Description</h2>
<p>The policy file describes system objects to be monitored by <i>Tripwire</i>, and specifies what properties for each object should be collected and stored in the database file. Each object in the policy file is associated with a property mask, which describes what changes to the file or directory <i>Tripwire</i> should monitor, and which ones can safely be ignored. By customizing the various aspects of the policy file, the system administrator can very closely control how <i>Tripwire</i> checks the integrity of any system. </p>
<p> During installation, an encoded and signed policy file (<i>tw.pol</i>) will be created in the <i>/etc/tripwire</i> directory, and a plain text copy of this policy file (<i>twpol.txt</i>) will be generated in the same directory. An additional text file (<i>policyguide.txt</i>) illustrates all of the features of the policy language. Both of the text files are heavily commented and can be used as a reference during policy file creation. </p>
<p> A new policy file is first created using the <code>twadmin &#8211;create-polfile</code> command. With this command, the user can designate an existing plain text file as the current policy file. Using the current site key and passphrase, the new configuration file is encoded, signed and saved. </p>
<p> Once the initial policy file has been generated, any changes should be made with the <code>tripwire &#8211;update-policy</code> command, rather than by simply overwriting the policy file with the <code>twadmin &#8211;create-polfile</code> command. This is an important distinction&#8211;when a new policy file is created, the <i>Tripwire</i> database must be re-initialized. If an intruder has modified files since the last integrity check, these changes will not be detected, and will be included as part of the new &quot;baseline&quot; database.</p>
<h2>Components Of The Policy File</h2>
<p>The basic components of policy files are comments, rules, directives, and variables. Each of these components is described in greater detail below.</p>
<h3>Comments</h3>
<p>In a policy file, any text following a &#8216;#&#8217;, up to the next line break, is considered a comment. Example: </p>
<p> <font SIZE="-1"> </font></p>
<pre># This is a comment.
/bin -&gt; $(ReadOnly); # A comment can go here, too.</pre>
<h3>Rules</h3>
<p>Policy rules determine whether and to what extent <i>Tripwire</i> will check particular files and directories. There are two kinds of policy rules recognized by <i>Tripwire</i>: </p>
<p> 1) Normal rules define which properties of a particular file or directory tree <i>Tripwire</i> scans.<br />
 2) Stop points tell <i>Tripwire</i> not to scan a particular file or directory.</p>
<h3>Normal Rules</h3>
<p>The format for a normal rule is:<br />
 <i>object_name</i> -&gt; <i>property_mask</i>;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<p> where the <i>object_name</i> is the fully qualified pathname for a directory or file, and <i>property_mask</i> specifies what properties of an object to examine or ignore. The &#8216;-&gt;&#8217; token separates the pathname and the property mask. Whitespace must separate the object name and &#8216;-&gt;&#8217; token. A semicolon must terminate the rule. If the pathname specified is a directory, the directory and all of its descendants will be scanned with the indicated property mask. If the pathname refers to an individual file, only that file will be scanned with the specified property mask. Examples: </p>
<p> <font SIZE="-1"> </font></p>
<pre># Defines Tripwire behavior for entire /bin directory tree.
/bin -&gt; $(ReadOnly);
# Defines Tripwire behavior for a single file. In this case,
# Tripwire watches for all properties of hostname.hme0.
/etc/hostname.hme0 -&gt; $(IgnoreNone) -ar;
# Scan the entire /etc directory tree using mask1, except the
# file /etc/passwd, which should be scanned using mask2.
/etc -&gt; $(mask1);
/etc/passwd -&gt; $(mask2);</pre>
<p>Only one rule may be associated with any given object. If any object has more than one rule in a policy file, <i>Tripwire</i> will print an error message and exit without scanning any files. For example: </p>
<p> <font SIZE="-1"> </font></p>
<pre># This is an example of an illegal construct.
/usr/bin -&gt; $(mask3);
/usr/bin -&gt; $(mask4);</pre>
<h3>Object Names</h3>
<p>In this document, policy file objects are fully qualified pathnames of files and directories. Environment variables are not allowed for security reasons. Examples: </p>
<p> <font SIZE="-1"> </font></p>
<pre>/etc # valid object name.
/etc/passwd # valid object name.
$HOME # not valid.</pre>
<h3>Property Masks</h3>
<p>Property masks designate which <i>Tripwire</i> properties of a given object should be examined. A property mask consists of a series of single-character symbols, each of which may be preceded by an optional plus or minus sign. Each character symbol stands for a particular <i>Tripwire</i> property to be examined during integrity checking. If the character is preceded by a plus, checking is done for that property; if preceded by a minus, checking is not done for that property. For example: </p>
<p> <font SIZE="-1"> </font></p>
<pre>+p # compare permissions.
-p # ignore permissions.</pre>
<p>Each rule in the policy file must have a property mask. Examples: </p>
<p> <font SIZE="-1"> </font></p>
<pre>/etc -&gt; $(IgnoreAll); #valid property mask.
/etc -&gt; +p-p; #valid property mask.
/etc -&gt; ; #invalid property mask.</pre>
<p>Characters in a property mask without a preceding plus or minus sign are assumed to be plus. If a property is not specified in the property mask, it is ignored, which is equivalent to turning it off with the minus sign. Examples: </p>
<p> <font SIZE="-1"> </font></p>
<pre># Examine permissions and link count.
# All three of the following are equivalent.
+p+n
pn
pn-g</pre>
<p>Characters used in property masks, with descriptions: </p>
<p> <font SIZE="-1"> </font></p>
<pre>- Ignore the following properties 
+ Record and check the following properties
a Access timestamp 
b Number of blocks allocated
c Inode timestamp (create/modify)
d ID of device on which inode resides
g File owner's group ID
i Inode number
l File is increasing in size (a &quot;growing file&quot;)
m Modification timestamp
n Number of links (inode reference count)
p Permissions and file mode bits
r ID of device pointed to by inode&nbsp;<wbr> (valid only for device objects)s File size
t File type
u File owner's user ID
C CRC-32 hash value
H Haval hash value
M MD5 hash value
S SHA hash value</pre>
<h3>Stop Points</h3>
<p>Stop points are used to specify specific files or directories that <i>Tripwire</i> should not scan. The syntax for stop points is: </p>
<pre>! <i>object_name</i> ; </pre>
<p>For example: <font SIZE="-1"> </font></p>
<pre>!/etc/init.d; 
# The directory /etc/init.d will not be scanned.
/etc -&gt; $(ReadOnly);
!/etc/rc.d;
!/etc/mnttab;
# Scan all of /etc, but do not scan two particular 
# files in the /etc hierarchy.</pre>
<h3>Rule Attributes</h3>
<p>Rule attributes work with normal rules to modify their behavior or provide additional information. Multiple attributes can be assigned to each rule. Rule attributes are not case-sensitive. Rule attributes may be applied to a single rule using the following syntax:<br />
 <i>object_name</i> -&gt; <i>property_mask</i> (<i>rule attribute</i> = <i>value</i>); For example: <font SIZE="-1"> </font></p>
<pre>/usr/lib -&gt; $(ReadOnly) (emailto = admin [at] foo.com, severity = 80);
#This rule will notify the admin if any violations of the 
#rule occur and designate the severity as 80.</pre>
<p>Rule attributes can also be specified for a group of rules, using the format:<br />
 (<i>attribute list</i>)<br />
 { <i>rule list</i>; } For example: <font SIZE="-1"> </font></p>
<pre>(emailto = admin [at] foo.com, severity = 80)
{
 /usr/lib -&gt; $(ReadOnly);
}</pre>
<p>is equivalent to the attribute example above. </p>
<p> The following four rule attributes are supported by <i>Tripwire</i>:</p>
<dl>
<dt><tt>rulename</tt></p>
<dd>The <tt>rulename</tt> attribute is used to associate a rule or set of rules with a specific name. In a report file, this name will be associated with violations to the specified rule. This feature is useful if you want to track certain objects within a large <i>Tripwire</i> database. For instance, if you associate the rule name &quot;watchme&quot; with important files, you can sort through the <i>Tripwire</i> report using &quot;watchme&quot; as a sorting key.<br />
 Example: <font SIZE="-1"> </font></p>
<pre>/etc -&gt; +ug (rulename=watchme);</pre>
<dt><tt>emailto</tt></p>
<dd>The <tt>emailto</tt> attribute associates one or more email addresses with a rule or group of rules. When an integrity check is run with the <code>&#8211;email-report</code> option and a rule is violated, a report of that violation will be sent to the specified email address(es), using the report format specified by the <tt>EMAILREPORTLEVEL</tt> variable in the configuration file.<br />
 Example: <font SIZE="-1"> </font></p>
<pre>/etc -&gt; +ug (emailto=admin [at] domain.com);</pre>
<dd>To specify multiple email addresses, include them as a quoted, semicolon-delimited list. <font SIZE="-1"> </font></p>
<pre>/etc -&gt; +ug (emailto=&quot;admin [at] foo.com;admin2 [at] foo.com&quot;);</pre>
<dt><tt>severity</tt></p>
<dd>The <tt>severity</tt> attribute associates a numeric severity level with a rule. When <i>Tripwire</i> is run in Integrity Checking mode, it is possible to specify that only rules exceeding a certain severity level are used. The default severity level is 0, and values can range from 0 to 1,000,000.<br />
 Example: <font SIZE="-1"> </font></p>
<pre>/etc -&gt; +ug (severity=50);</pre>
<dt><tt>recurse</tt></p>
<dd>The <tt>recurse</tt> attribute specifies how a rule will scan directories. Valid values for <tt>recurse</tt> are <i>true</i>, <i>false</i>, or a number from -1 to 1,000,000. If <tt>recurse</tt> is set to <i>true</i> (or -1), tripwire will recursively scan the entire contents of the directory (both files and subdirectories). When <tt>recurse</tt> is set to <i>false</i> (or 0), and the rule refers to a directory, <i>Tripwire</i> will scan the inode of the directory but none of the files or subdirectories contained therein. For positive <tt>recurse</tt> value <i>n</i>, the rule will monitor all objects up to <i>n</i> levels below the start point. Stop points within the recursed directory still apply, and will prevent the specified file or directory from being scanned.</p>
<dd>When a rule refers to a file, specifying the <tt>recurse</tt> attribute has no effect&#8211;files will be scanned no matter what value is given for <tt>recurse</tt>. The default value for <tt>recurse</tt> is <i>true</i>.<br />
 Example: <font SIZE="-1"> </font></p>
<pre>/etc -&gt; +ug (recurse=2);</pre>
</dl>
<h3>Directives</h3>
<p><i>Tripwire</i> supports a small number of directives that allow conditional interpretation of the policy file and certain diagnostic and debugging operations. The primary purpose of directives is to support sharing of a policy file among multiple machines. Directives use the following syntax: </p>
<pre>@@ <i>directive_name</i> [<i>arguments</i>]</pre>
<p>Where the directive name is one of the directives listed below: </p>
<p> <font SIZE="-1"> </font></p>
<pre>@@section # Designates a section of the policy file.
@@ifhost # Allow conditional interpretation
@@else # of the policy file.
@@endif 
@@print # Print a message to standard output.
@@error # Print a message to standard output and then exit.
@@end # Marks the logical end-of-file.</pre>
<p>The @@section directive is used to designate sections of the policy file that are OS-specific. With <i>Tripwire 2.4</i>, valid arguments for the @@section directive are <tt>FS</tt> and <tt>GLOBAL</tt>. If no @@section directive is specified, <tt>FS</tt> will be assumed. If the argument to the @@section directive is either <tt>NTFS</tt> or <tt>NTREG</tt> (which have meaning only on Windows NT systems), <i>Tripwire</i> will skip all policy file text down to the next valid @@section directive. Any other argument will cause an error. </p>
<p> The @@ifhost, @@else, and @@endif directives are used to allow conditional interpretation of the policy file. With the @@ifhost directive, multiple hostnames can be expressed as arguments, but they must be separated by an &#8216;||&#8217;, interpreted as the logical &#8216;OR&#8217;. This example illustrates how one might employ directives to use one policy file with multiple hosts. </p>
<p> <font SIZE="-1"> </font></p>
<pre>@@ifhost spock || kirk
 /bin -&gt; $(ReadOnly);
@@endif
@@ifhost chekov || uhura
 /usr/bin -&gt; +pinug;
@@else
 /usr/bin -&gt; +pinugsmC;
@@endif</pre>
<p>The @@print and @@error directives are intended for debugging and remote diagnostics. The syntax for these commands is: </p>
<pre>@@print &quot;<i>string</i>&quot;
@@error &quot;<i>string</i>&quot;</pre>
<p>The @@print directive prints <i>string</i> to <i>stdout</i>, while the @@error directive prints <i>string</i> to <i>stdout</i> and causes the calling program to exit with a non-zero status. </p>
<p> The @@end directive marks the end of the policy file. Any text appearing after this directive will be ignored by <i>Tripwire</i>.</p>
<h3>Variables</h3>
<p>For user convenience, <i>Tripwire</i>&#8216;s policy file supports variables for string substitution. Variables can be defined anywhere between rules. The syntax for variable definition is: </p>
<pre><i>variable</i> = <i>value</i>;</pre>
<p>Variable substitution is legal anywhere that a string could appear. The syntax for variable substitution is: </p>
<pre>$( <i>variable</i> )</pre>
<p>Examples of variable definition and variable substitution on the left, right, and both sides of rules. Note that variable names are case sensitive. </p>
<p> <font SIZE="-1"> </font></p>
<pre>param1 = +SMCH; # Set variable param1.
dir1 = /etc/inet; # Set variable dir1.
DIR1 = /etc/init.d; # Variables are case sensitive.
$(dir1) -&gt; +tbamc; # Left hand substitution.
/etc/inet -&gt; $(param1); # Right hand substitution.
$(DIR1) -&gt; $(param1); # Double substitution.</pre>
<p>A number of variables are predefined by <i>Tripwire</i> and may not be changed. These variables represent different ways that files can change, and can be used on the right side of rules to design a policy file quickly.</p>
<dl>
<dt>ReadOnly</p>
<dd>ReadOnly is good for files that are widely available but are intended to be read-only.<br />
 Value: <font SIZE="-1"> +pinugtsdbmCM-rlacSH </font></p>
<dt>Dynamic</p>
<dd>Dynamic is good for monitoring user directories and files that tend to be dynamic in behavior.<br />
 Value: <font SIZE="-1"> +pinugtd-srlbamcCMSH </font></p>
<dt>Growing</p>
<dd>The Growing variable is intended for files that should only get larger.<br />
 Value: <font SIZE="-1"> +pinugtdl-srbamcCMSH </font></p>
<dt>Device</p>
<dd>Device is good for devices or other files that <i>Tripwire</i> should not attempt to open.<br />
 Value: <font SIZE="-1"> +pugsdr-intlbamcCMSH </font></p>
<dt>IgnoreAll</p>
<dd>IgnoreAll tracks a file&#8217;s presence or absence, but doesn&#8217;t check any other properties.<br />
 Value: <font SIZE="-1"> -pinugtsdrlbamcCMSH </font></p>
<dt>IgnoreNone</p>
<dd>IgnoreNone turns on all properties and provides a convenient starting point for defining your own property masks. (For example,&nbsp;<wbr><tt>mymask&nbsp;<wbr>=&nbsp;<wbr>$(IgnoreNone)&nbsp;<wbr>-ar;</tt>)<br />
 Value: <font SIZE="-1"> +pinugtsdrbamcCMSH-l </font></dl>
<h2>Version Information</h2>
<p>This man page describes <i>Tripwire 2.4</i>.</p>
<h2>Authors</h2>
<p>Tripwire, Inc.</p>
<h2>Copying Permissions</h2>
<p>Permission is granted to make and distribute verbatim copies of this man page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this man page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this man page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by Tripwire, Inc. </p>
<p> Copyright 2000-2017 Tripwire, Inc. Tripwire is a registered trademark of Tripwire, Inc. in the United States and other countries. All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-twintro/">twintro</a></code>(8), <code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8), <code><a href="/docs/linux/man/8-twadmin/">twadmin</a></code>(8), <code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8), <code><a href="/docs/linux/man/8-siggen/">siggen</a></code>(8), <code><a href="/docs/linux/man/4-twconfig/">twconfig</a></code>(4), <code><a href="/docs/linux/man/5-twfiles/">twfiles</a></code>(5) </p>
