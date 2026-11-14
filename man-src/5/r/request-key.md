---
title: "request-key(5)"
name: "request-key"
section: "5"
letter: "r"
url: "/docs/linux/man/5-request-key/"
description: "request-key.conf – Instantiation handler configuration file"
---

<p>request-key.conf &#8211; Instantiation handler configuration file</p>
<h2>Description</h2>
<p>This file and its associated key-type specific variants are used by the /sbin/request-key program to determine which program it should run to instantiate a key. </p>
<p> request-key looks first in /etc/request-key.d/ for a file of the key type name plus &quot;.conf&quot; that it can use. If that is not found, it will fall back to /etc/request-key.conf. </p>
<p> request-key scans through the chosen file one line at a time until it finds a match, which it will then use. If it doesn&#8217;t find a match, it&#8217;ll return an error and the kernel will automatically negate the key. </p>
<p> Any blank line or line beginning with a hash mark &#8216;#&#8217; is considered to be a comment and ignored. </p>
<p> All other lines are assumed to be command lines with a number of white space separated fields: </p>
<p> &lt;op&gt; &lt;type&gt; &lt;description&gt; &lt;callout-info&gt; &lt;prog&gt; &lt;arg1&gt; &lt;arg2&gt; &#8230; </p>
<p> The first four fields are used to match the parameters passed to request-key by the kernel. <i>op</i> is the operation type; currently the only supported operation is &quot;create&quot;. </p>
<p> <i>type</i>, <i>description</i> and <i>callout-info</i> match the three parameters passed to <code>keyctl request2</code> or the <code>request_key()</code> system call. Each of these may contain one or more asterisk &#8216;*&#8217; characters as wildcards anywhere within the string. </p>
<p> Should a match be made, the program specified by &lt;prog&gt; will be exec&#8217;d. This must have a fully qualified path name. argv[0] will be set from the part of the program name that follows the last slash &#8216;/&#8217; character. </p>
<p> If the program name is prefixed with a pipe bar character &#8216;|&#8217;, then the program will be forked and exec&#8217;d attached to three pipes. The callout information will be piped to it on it&#8217;s stdin and the intended payload data will be retrieved from its stdout. Anything sent to stderr will be posted in syslog. If the program exits 0, then /sbin/request-key will attempt to instantiate the key with the data read from stdout. If it fails in any other way, then request-key will attempt to execute the appropriate &#8216;negate&#8217; operation command. </p>
<p> The program arguments can be substituted with various macros. Only complete argument substitution is supported &#8211; macro substitutions can&#8217;t be embedded. All macros begin with a percent character &#8216;%&#8217;. An argument beginning with two percent characters will have one of them discarded. </p>
<p> The following macros are supported: </p>
<dl>
<dd>%o Operation type<br />
 %k Key ID<br />
 %t Key type<br />
 %d Key description<br />
 %c Callout information<br />
 %u Key UID<br />
 %g Key GID<br />
 %T Requestor&#8217;s thread keyring<br />
 %P Requestor&#8217;s process keyring<br />
 %S Requestor&#8217;s session keyring</dl>
<p> There&#8217;s another macro substitution too that permits the interpolation of the contents of a key: </p>
<dl>
<dd>%{&lt;type&gt;:&lt;description&gt;}</dl>
<p> This performs a lookup for a key of the given type and description on the requestor&#8217;s keyrings, and if found, substitutes the contents for the macro. If not found an error will be logged and the key under construction will be negated.</p>
<h2>Example</h2>
<p>A basic file will be installed in the /etc. This will contain two debugging lines that can be used to test the installation: </p>
<dl>
<dd>create user debug:* negate /bin/keyctl negate %k 30 %S<br />
 create user debug:loop:* * |/bin/cat<br />
 create user debug:* * /usr/share/keyutils/request-key-debug.sh %k %d %c %S<br />
 negate * * * /bin/keyctl negate %k 30 %S</dl>
<p> This is set up so that something like: </p>
<dl>
<dd>keyctl request2 user debug:xxxx negate</dl>
<p> will create a negative user-defined key, something like: </p>
<dl>
<dd>keyctl request2 user debug:yyyy spoon</dl>
<p> will create an instantiated user-defined key with &quot;Debug spoon&quot; as the payload, and something like: </p>
<dl>
<dd>keyctl request2 user debug:loop:zzzz abcdefghijkl</dl>
<p> will create an instantiated user-defined key with the callout information as the payload.</p>
<h2>Files</h2>
<p>/etc/request-key.conf<br />
 /etc/request-key.d/&lt;keytype&gt;.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5) </p>
