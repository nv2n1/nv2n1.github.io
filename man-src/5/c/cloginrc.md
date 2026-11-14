---
title: "cloginrc(5)"
name: "cloginrc"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cloginrc/"
description: ".cloginrc – clogin configuration file"
---

<p>&nbsp;<wbr>.cloginrc &#8211; clogin configuration file</p>
<h2>Description</h2>
<p><code>.cloginrc</code> contains configuration information for <code><a href="/docs/linux/man/1-alogin/">alogin</a></code>(1), <code><a href="/docs/linux/man/1-blogin/">blogin</a></code>(1), <code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1), <code><a href="/docs/linux/man/1-elogin/">elogin</a></code>(1), <code><a href="/docs/linux/man/1-flogin/">flogin</a></code>(1), <code><a href="/docs/linux/man/1-hlogin/">hlogin</a></code>(1), <code><a href="/docs/linux/man/1-htlogin/">htlogin</a></code>(1), <code><a href="/docs/linux/man/1-jlogin/">jlogin</a></code>(1), <code><a href="/docs/linux/man/1-nlogin/">nlogin</a></code>(1), <code><a href="/docs/linux/man/1-nslogin/">nslogin</a></code>(1), <code><a href="/docs/linux/man/1-rivlogin/">rivlogin</a></code>(1), and <code><a href="/docs/linux/man/1-wlogin/">wlogin</a></code>(1), such as usernames, passwords, ssh encryption type, etc., and is read at run-time. </p>
<p> Each line contains either white-space (blank line), a comment which begins with the comment character &#8216;#&#8217; and may be preceded by white-space, or one of the directives listed below. </p>
<p> Each line containing a directive is of the form: </p>
<pre>add &lt;directive&gt; &lt;hostname glob&gt; {&lt;value&gt;} [{&lt;value&gt;} ...]
or
include {&lt;file&gt;}</pre>
<p>Note: the braces ({}) surrounding the values is significant when the values include TCL meta-characters. Best common practice is to always enclose the values in braces. If a value includes a (left or right) brace or space character, it must be backslash-escaped, as in: </p>
<pre>add user &lt;hostname glob&gt; {foo\}bar}
add user &lt;hostname glob&gt; {foo\ bar}</pre>
<p>As <code>.cloginrc</code> is searched for a directive matching a hostname, it is always the first matching instance of a directive, one whose hostname glob expression matches the hostname, which is used. For example; looking up the &quot;password&quot; directive for hostname foo in a <code>.cloginrc</code> file containing </p>
<pre>add password * {bar} {table}
add password foo {bar} {table}</pre>
<p>would return the first line, even though the second is an exact match. </p>
<p> <code>.cloginrc</code> is expected to exist in the user&#8217;s home directory and must not be readable, writable, or executable by &quot;others&quot;. <code>.cloginrc</code> should be mode 0600, or 0640 if it is to be shared with other users who are members of the same unix group. See <code><a href="/docs/linux/man/1-chgrp/">chgrp</a></code>(1) and <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) for more information on ownership and file modes.</p>
<h2>Directives</h2>
<p>The accepted directives are (alphabetically): </p>
<dl>
<dt><code>add autoenable &lt;router name glob&gt; {[01]}</code></p>
<dd>When using locally defined usernames or AAA, it is possible to have a login which is automatically enabled. This is, that user has enable privileges without the need to execute the enable command. The router&#8217;s prompt is different for enabled mode, ending with a # rather than a &gt;. </p>
<p> Example: add autoenable * {1} </p>
<p> Default: 0 </p>
<p> zero, meaning that the user is not automatically enabled and <i>clogin</i> should execute the enable command to gain enable privileges, unless negated by the noenable directive or -noenable command-line option. </p>
<p> Also see the <code>noenable</code> directive.</p>
<dt><code>add cyphertype &lt;router name glob&gt; {&lt;ssh encryption type&gt;}</code></p>
<dd>cyphertype defines which encryption algorithm is used with ssh. A device may not support the type ssh uses by default. See <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1)&#8217;s<br />
&nbsp;<wbr>-c option for details. </p>
<p> Default: {3des}</p>
<dt><code>add enableprompt &lt;router name glob&gt; {&lt;enable prompt&gt;}</code></p>
<dd>When using AAA with a Cisco router or switch, it is possible to redefine the prompt the device presents to the user for the enable password. enableprompt may be used to adjust the prompt that <i>clogin</i> should look for when trying to login. Note that enableprompt can be a Tcl style regular expression. </p>
<p> Example: add enableprompt rc*.example.net {&quot;\[Ee]nter\ the\ enable\ password:&quot;} </p>
<p> Default: &quot;\[Pp]assword:&quot;</p>
<dt><code>add enablecmd &lt;router name glob&gt; {&lt;enable command&gt;}</code></p>
<dd>This defines the command on the device used to enter enabled or super-user mode. For example, in Cisco IOS the command is &quot;enable&quot;.</p>
<dt><code>add enauser &lt;router name glob&gt; {&lt;username&gt;}</code></p>
<dd>This is only needed if a device prompts for a username when gaining enable privileges and where this username is different from that defined by or the default of the user directive.</p>
<dt><code>add identity &lt;router name glob&gt; {&lt;ssh identity file path&gt;}</code></p>
<dd>May be used to specify an alternate identity file for use with <a href="/docs/linux/man/1-ssh/">ssh</a>(1). See ssh&#8217;s -i option for details. </p>
<p> Default: your default identity file. see <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>add method &lt;router name glob&gt; {ssh} [{&#8230;}]</code></p>
<dd>Defines, in order, the connection methods to use for a device from the set {ssh, telnet, rsh}. Method ssh and telnet may have a suffix, indicating an alternate TCP port, of the form &quot;:port&quot;. </p>
<p> Note: Different versions of telnet treat the specification of a port differently. In particular, BSD derived telnets do not do option negotiation when a port is given. Some devices, Extreme switches for example, have undesirable telnet default options such as linemode. In the BSD case, to enable option negotiation when specifying a port the method should be &quot;{telnet:-23}&quot; or, better, add &quot;mode character&quot; to .telnetrc. See <code><a href="/docs/linux/man/1-telnet/">telnet</a></code>(1) for more information on telnet command-line syntax, telnet options, and .telnetrc. </p>
<p> Example: add method * {ssh} {telnet:3000} {rsh} </p>
<p> Which would cause <i>clogin</i> to first attempt an ssh connection to the device and if that were to fail with connection refused, a telnet connection to port 3000 would be tried, and then a rsh connection. </p>
<p> Note that not all platforms support all of these connection methods. </p>
<p> Default: {telnet} {ssh}</p>
<dt><code>add noenable &lt;router name glob&gt; {1}</code></p>
<dd><i>clogin</i> will not try to gain enable privileges when noenable is matched for a device. This is equivalent to <i>clogin</i>&#8216;s -noenable command-line option. </p>
<p> Note that this directive is meaningless for <code><a href="/docs/linux/man/1-jlogin/">jlogin</a></code>(1), <code><a href="/docs/linux/man/1-nlogin/">nlogin</a></code>(1) and <code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1) [for Extreme] which do not have the concept of &quot;enabled&quot; and/or no way to elevate privleges once logged in; a user either has the necessary privleges or doesn&#8217;t.</p>
<dt><code>add passphrase &lt;router name glob&gt; {&lt;SSH passphrase&gt;}</code></p>
<dd>Specify the SSH passphrase. Note that this may be particular to an <code>identity</code> directive. The passphrase will default to the <code>password</code> for the given router. </p>
<p> Example: add passphrase rc*.example.net {the\ bird\ goes\ tweet}</p>
<dt><code>add passprompt &lt;router name glob&gt; {&lt;password prompt&gt;}</code></p>
<dd>When using AAA with a Cisco router or switch, it is possible to redefine the prompt the device presents to the user for the password. passprompt may be used to adjust the prompt that <i>clogin</i> should look for when trying to login. Note that passprompt can be a Tcl style regular expression. </p>
<p> Example: add passprompt rc*.example.net {&quot;\[Ee]nter\ the\ password:&quot;} </p>
<p> Default: &quot;(\[Pp]assword|passwd):&quot;</p>
<dt><code>add password &lt;router name glob&gt; {&lt;vty passwd&gt;} [{&lt;enable passwd&gt;}]</code></p>
<dd>Specifies a vty password, that which is prompted for upon the connection to the router. The last argument is the enable password and need not be specified if the device also has a matching noenable or autoenable directive or the corresponding command-line options are used.</p>
<dt><code>add prompt &lt;router name glob&gt; {&lt;regex&gt;}</code></p>
<dd>Match login prompt, or initial login prompt in the case of some of the login scripts. This is provided only as a work-around for login banners that contain forbidden characters that conflict with CLI prompt markers. </p>
<p> Note that not all login scripts support this.</p>
<dt><code>add sshcmd &lt;router name glob&gt; {&lt;ssh&gt;}</code></p>
<dd>&lt;ssh&gt; is the name of the ssh executable. OpenSSH uses a command-line option to specify the protocol version, but other implementations use a separate binary such as &quot;ssh1&quot;. <code>sshcmd</code> allows this to be adjusted as necessary for the local environment. </p>
<p> Default: ssh</p>
<dt><code>add timeout &lt;router name glob&gt; {&lt;seconds&gt;}</code></p>
<dd>Time in seconds that the login script will wait for input from the device before timeout. </p>
<p> Default: device dependent</p>
<dt><code>add user &lt;router name glob&gt; {&lt;username&gt;}</code></p>
<dd>Specifies a username <i>clogin</i> should use if or when prompted for one. </p>
<p> Default: $USER (or $LOGNAME), i.e.: your Unix username.</p>
<dt><code>add userpassword &lt;router name glob&gt; {&lt;user password&gt;}</code></p>
<dd>Specifies a password to be associated with a user, if different from that defined with the password directive.</p>
<dt><code>add userprompt &lt;router name glob&gt; {&lt;username prompt&gt;}</code></p>
<dd>When using AAA with a Cisco router or switch, it is possible to redefine the prompt the device presents to the user for the username. userprompt may be used to adjust the prompt that <i>clogin</i> should look for when trying to login. Note that userprompt can be a Tcl style regular expression. </p>
<p> Example: add userprompt rc*.example.net {&quot;\[Ee]nter\ your\ username:&quot;} </p>
<p> Default: &quot;(Username|login|user name):&quot;</p>
<dt><code>include {&lt;file&gt;}</code></p>
<dd>&lt;file&gt; is the pathname of an additional <code>.cloginrc</code> file to include at that point. It is evaluated immediately. That is important with regard to the order of matching hostnames for a given directive, as mentioned above. This is useful if you have your own <code>.cloginrc</code> plus an additional <code>.cloginrc</code> file that is shared among a group of folks. </p>
<p> If &lt;file&gt; is not a full pathname, $HOME/ will be prepended. </p>
<p> Example: include {.cloginrc.group} </p>
</dl>
<h2>Files</h2>
<pre><i>$HOME/.cloginrc</i> Configuration file described here.
<i>share/rancid/cloginrc.sample</i> A sample <code>.cloginrc</code>.</pre>
<h2>Errors</h2>
<p><code>.cloginrc</code> is interpreted directly by Tcl, so its syntax follows that of Tcl. Errors may produce quite unexpected results.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1), <code><a href="/docs/linux/man/3-glob/">glob</a></code>(3), <code><a href="/docs/linux/man/1-tclsh/">tclsh</a></code>(1) </p>
