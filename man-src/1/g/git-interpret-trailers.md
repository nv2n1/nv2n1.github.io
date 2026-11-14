---
title: "git-interpret-trailers(1)"
name: "git-interpret-trailers"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-interpret-trailers/"
description: "git-interpret-trailers – Add or parse structured information in commit messages"
---

<h2 class="name">NAME</h2>
<p> git-interpret-trailers &#8211; Add or parse structured information in commit messages </p>
<h2>SYNOPSIS</h2>
<pre><code>
git interpret - trailers[&lt;options&gt;][(--trailer&lt;token&gt;[(= |
                                                       :) &lt; value &gt; ])...][&lt;file&gt;...] git interpret -
    trailers[&lt;options&gt;][--parse][&lt;file&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Help parsing or adding <i>trailers</i> lines, that look similar to RFC 822 e-mail headers, at the end of the otherwise free-form part of a commit message. </p>
<p> This command reads some patches or commit messages from either the &lt;file&gt; arguments or the standard input if no &lt;file&gt; is specified. If <code>&#8211;parse</code> is specified, the output consists of the parsed trailers. </p>
<p> Otherwise, this command applies the arguments passed using the <code>&#8211;trailer</code> option, if any, to the commit message part of each input file. The result is emitted on the standard output. </p>
<p> Some configuration variables control the way the <code>&#8211;trailer</code> arguments are applied to each commit message and the way any existing trailer in the commit message is changed. They also make it possible to automatically add some trailers. </p>
<p> By default, a <i>&lt;token&gt;=&lt;value&gt;</i> or <i>&lt;token&gt;:&lt;value&gt;</i> argument given using <code>&#8211;trailer</code> will be appended after the existing trailers only if the last trailer has a different (&lt;token&gt;, &lt;value&gt;) pair (or if there is no existing trailer). The &lt;token&gt; and &lt;value&gt; parts will be trimmed to remove starting and trailing whitespace, and the resulting trimmed &lt;token&gt; and &lt;value&gt; will appear in the message like this: </p>
<dl>
<dt>
<dd>
<pre>
token: value
</pre>
</dl>
<p> This means that the trimmed &lt;token&gt; and &lt;value&gt; will be separated by <code>&#8216;: &#8216;</code> (one colon followed by one space). </p>
<p> By default the new trailer will appear at the end of all the existing trailers. If there is no existing trailer, the new trailer will appear after the commit message part of the output, and, if there is no line with only spaces at the end of the commit message part, one blank line will be added before the new trailer. </p>
<p> Existing trailers are extracted from the input message by looking for a group of one or more lines that (i) is all trailers, or (ii) contains at least one Git-generated or user-configured trailer and consists of at least 25% trailers. The group must be preceded by one or more empty (or whitespace-only) lines. The group must either be at the end of the message or be the last non-whitespace lines before a line that starts with <i>&#8212;</i> (followed by a space or the end of the line). Such three minus signs start the patch part of the message. See also <code>&#8211;no-divider</code> below. </p>
<p> When reading trailers, there can be whitespaces after the token, the separator and the value. There can also be whitespaces inside the token and the value. The value may be split over multiple lines with each subsequent line starting with whitespace, like the &quot;folding&quot; in RFC 822. </p>
<p> Note that <i>trailers</i> do not follow and are not intended to follow many rules for RFC 822 headers. For example they do not follow the encoding rules and probably many other rules.</p>
<h2>OPTIONS</h2>
<p> &#8211;in-place</p>
<dl>
<dt>
<dd> Edit the files in place.</dl>
<p> &#8211;trim-empty</p>
<dl>
<dt>
<dd> If the &lt;value&gt; part of any trailer contains only whitespace, the whole trailer will be removed from the resulting message. This applies to existing trailers as well as new trailers.</dl>
<p> &#8211;trailer &lt;token&gt;[(=|:)&lt;value&gt;]</p>
<dl>
<dt>
<dd> Specify a (&lt;token&gt;, &lt;value&gt;) pair that should be applied as a trailer to the input messages. See the description of this command.</dl>
<p> &#8211;where &lt;placement&gt;, &#8211;no-where</p>
<dl>
<dt>
<dd> Specify where all new trailers will be added. A setting provided with <i>&#8211;where</i> overrides all configuration variables and applies to all <i>&#8211;trailer</i> options until the next occurrence of <i>&#8211;where</i> or <i>&#8211;no-where</i>. Possible values are <code>after</code>, <code>before</code>, <code>end</code> or <code>start</code>.</dl>
<p> &#8211;if-exists &lt;action&gt;, &#8211;no-if-exists</p>
<dl>
<dt>
<dd> Specify what action will be performed when there is already at least one trailer with the same &lt;token&gt; in the message. A setting provided with <i>&#8211;if-exists</i> overrides all configuration variables and applies to all <i>&#8211;trailer</i> options until the next occurrence of <i>&#8211;if-exists</i> or <i>&#8211;no-if-exists</i>. Possible actions are <code>addIfDifferent</code>, <code>addIfDifferentNeighbor</code>, <code>add</code>, <code>replace</code> and <code>doNothing</code>.</dl>
<p> &#8211;if-missing &lt;action&gt;, &#8211;no-if-missing</p>
<dl>
<dt>
<dd> Specify what action will be performed when there is no other trailer with the same &lt;token&gt; in the message. A setting provided with <i>&#8211;if-missing</i> overrides all configuration variables and applies to all <i>&#8211;trailer</i> options until the next occurrence of <i>&#8211;if-missing</i> or <i>&#8211;no-if-missing</i>. Possible actions are <code>doNothing</code> or <code>add</code>.</dl>
<p> &#8211;only-trailers</p>
<dl>
<dt>
<dd> Output only the trailers, not any other parts of the input.</dl>
<p> &#8211;only-input</p>
<dl>
<dt>
<dd> Output only trailers that exist in the input; do not add any from the command-line or by following configured <code>trailer.*</code> rules.</dl>
<p> &#8211;unfold</p>
<dl>
<dt>
<dd> Remove any whitespace-continuation in trailers, so that each trailer appears on a line by itself with its full content.</dl>
<p> &#8211;parse</p>
<dl>
<dt>
<dd> A convenience alias for <code>&#8211;only-trailers &#8211;only-input &#8211;unfold</code>.</dl>
<p> &#8211;no-divider</p>
<dl>
<dt>
<dd> Do not treat <code>&#8212;</code> as the end of the commit message. Use this when you know your input contains just the commit message itself (and not an email or the output of <code>git format-patch</code>).</dl>
<h2>CONFIGURATION VARIABLES</h2>
<p> trailer.separators</p>
<dl>
<dt>
<dd> This option tells which characters are recognized as trailer separators. By default only <i>:</i> is recognized as a trailer separator, except that <i>=</i> is always accepted on the command line for compatibility with other git commands. </p>
<p> The first character given by this option will be the default character used when another separator is not specified in the config for this trailer. </p>
<p> For example, if the value for this option is &quot;%=$&quot;, then only lines using the format <i>&lt;token&gt;&lt;sep&gt;&lt;value&gt;</i> with &lt;sep&gt; containing <i>%</i>, <i>=</i> or <i>$</i> and then spaces will be considered trailers. And <i>%</i> will be the default separator used, so by default trailers will appear like: <i>&lt;token&gt;% &lt;value&gt;</i> (one percent sign and one space will appear between the token and the value).</dl>
<p> trailer.where</p>
<dl>
<dt>
<dd> This option tells where a new trailer will be added. </p>
<p> This can be <code>end</code>, which is the default, <code>start</code>, <code>after</code> or <code>before</code>. </p>
<p> If it is <code>end</code>, then each new trailer will appear at the end of the existing trailers. </p>
<p> If it is <code>start</code>, then each new trailer will appear at the start, instead of the end, of the existing trailers. </p>
<p> If it is <code>after</code>, then each new trailer will appear just after the last trailer with the same &lt;token&gt;. </p>
<p> If it is <code>before</code>, then each new trailer will appear just before the first trailer with the same &lt;token&gt;.</dl>
<p> trailer.ifexists</p>
<dl>
<dt>
<dd> This option makes it possible to choose what action will be performed when there is already at least one trailer with the same &lt;token&gt; in the message. </p>
<p> The valid values for this option are: <code>addIfDifferentNeighbor</code> (this is the default), <code>addIfDifferent</code>, <code>add</code>, <code>replace</code> or <code>doNothing</code>. </p>
<p> With <code>addIfDifferentNeighbor</code>, a new trailer will be added only if no trailer with the same (&lt;token&gt;, &lt;value&gt;) pair is above or below the line where the new trailer will be added. </p>
<p> With <code>addIfDifferent</code>, a new trailer will be added only if no trailer with the same (&lt;token&gt;, &lt;value&gt;) pair is already in the message. </p>
<p> With <code>add</code>, a new trailer will be added, even if some trailers with the same (&lt;token&gt;, &lt;value&gt;) pair are already in the message. </p>
<p> With <code>replace</code>, an existing trailer with the same &lt;token&gt; will be deleted and the new trailer will be added. The deleted trailer will be the closest one (with the same &lt;token&gt;) to the place where the new one will be added. </p>
<p> With <code>doNothing</code>, nothing will be done; that is no new trailer will be added if there is already one with the same &lt;token&gt; in the message.</dl>
<p> trailer.ifmissing</p>
<dl>
<dt>
<dd> This option makes it possible to choose what action will be performed when there is not yet any trailer with the same &lt;token&gt; in the message. </p>
<p> The valid values for this option are: <code>add</code> (this is the default) and <code>doNothing</code>. </p>
<p> With <code>add</code>, a new trailer will be added. </p>
<p> With <code>doNothing</code>, nothing will be done.</dl>
<p> trailer.&lt;token&gt;.key</p>
<dl>
<dt>
<dd> This <code>key</code> will be used instead of &lt;token&gt; in the trailer. At the end of this key, a separator can appear and then some space characters. By default the only valid separator is <i>:</i>, but this can be changed using the <code>trailer.separators</code> config variable. </p>
<p> If there is a separator, then the key will be used instead of both the &lt;token&gt; and the default separator when adding the trailer.</dl>
<p> trailer.&lt;token&gt;.where</p>
<dl>
<dt>
<dd> This option takes the same values as the <i>trailer.where</i> configuration variable and it overrides what is specified by that option for trailers with the specified &lt;token&gt;.</dl>
<p> trailer.&lt;token&gt;.ifexists</p>
<dl>
<dt>
<dd> This option takes the same values as the <i>trailer.ifexists</i> configuration variable and it overrides what is specified by that option for trailers with the specified &lt;token&gt;.</dl>
<p> trailer.&lt;token&gt;.ifmissing</p>
<dl>
<dt>
<dd> This option takes the same values as the <i>trailer.ifmissing</i> configuration variable and it overrides what is specified by that option for trailers with the specified &lt;token&gt;.</dl>
<p> trailer.&lt;token&gt;.command</p>
<dl>
<dt>
<dd> This option behaves in the same way as <i>trailer.&lt;token&gt;.cmd</i>, except that it doesn&#8217;t pass anything as argument to the specified command. Instead the first occurrence of substring $ARG is replaced by the value that would be passed as argument. </p>
<p> The <i>trailer.&lt;token&gt;.command</i> option has been deprecated in favor of <i>trailer.&lt;token&gt;.cmd</i> due to the fact that $ARG in the user&#8217;s command is only replaced once and that the original way of replacing $ARG is not safe. </p>
<p> When both <i>trailer.&lt;token&gt;.cmd</i> and <i>trailer.&lt;token&gt;.command</i> are given for the same &lt;token&gt;, <i>trailer.&lt;token&gt;.cmd</i> is used and <i>trailer.&lt;token&gt;.command</i> is ignored.</dl>
<p> trailer.&lt;token&gt;.cmd</p>
<dl>
<dt>
<dd> This option can be used to specify a shell command that will be called: once to automatically add a trailer with the specified &lt;token&gt;, and then each time a <i>&#8211;trailer &lt;token&gt;=&lt;value&gt;</i> argument to modify the &lt;value&gt; of the trailer that this option would produce. </p>
<p> When the specified command is first called to add a trailer with the specified &lt;token&gt;, the behavior is as if a special <i>&#8211;trailer &lt;token&gt;=&lt;value&gt;</i> argument was added at the beginning of the &quot;git interpret-trailers&quot; command, where &lt;value&gt; is taken to be the standard output of the command with any leading and trailing whitespace trimmed off. </p>
<p> If some <i>&#8211;trailer &lt;token&gt;=&lt;value&gt;</i> arguments are also passed on the command line, the command is called again once for each of these arguments with the same &lt;token&gt;. And the &lt;value&gt; part of these arguments, if any, will be passed to the command as its first argument. This way the command can produce a &lt;value&gt; computed from the &lt;value&gt; passed in the <i>&#8211;trailer &lt;token&gt;=&lt;value&gt;</i> argument.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Configure a <i>sign</i> trailer with a <i>Signed-off-by</i> key, and then add two of these trailers to a message: </p>
<dl>
<dt>
<dd>
$ git config trailer.sign.key &#8220;Signed-off-by&#8221; $ cat msg.txt<br />
        subject<br />
            message<br />
                $ cat msg.txt |<br />
    git interpret &#8211; trailers&#8211; trailer &#8216;sign: Alice &lt;alice [at] example.com&gt;&#8217; &#8211;trailer &#8216;sign: Bob &lt;bob [at] example.com&gt;&#8217; subject message Signed &#8211; off &#8211; by : Alice&lt;alice[at] example.com&gt; Signed &#8211; off &#8211; by : Bob&lt;bob[at] example.com&gt;
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Use the <code>&#8211;in-place</code> option to edit a message file in place: </p>
<dl>
<dt>
<dd>
$ cat msg.txt<br />
        subject<br />
            message<br />
                Signed &#8211;<br />
    off &#8211; by : Bob&lt;bob[at] example.com&gt; $ git interpret &#8211; trailers&#8211; trailer &#8216;Acked-by: Alice &lt;alice [at] example.com&gt;&#8217; &#8211;in &#8211; place msg.txt $ cat msg.txt subject message Signed &#8211; off &#8211; by : Bob&lt;bob[at] example.com&gt; Acked &#8211; by : Alice&lt;alice[at] example.com&gt;
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Extract the last commit as a patch, and add a <i>Cc</i> and a <i>Reviewed-by</i> trailer to it: </p>
<dl>
<dt>
<dd>
$ git format &#8211; patch &#8211; 1 0001 &#8211; foo.patch $ git interpret &#8211; trailers&#8211; trailer &#8216;Cc: Alice &lt;alice [at] example.com&gt;&#8217; &#8211;trailer &#8216;Reviewed-by: Bob &lt;bob [at] example.com&gt;&#8217; 0001 &#8211; foo.patch &gt; 0001 &#8211; bar.patch
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Configure a <i>sign</i> trailer with a command to automatically add a &#8216;Signed-off-by: &#8216; with the author information only if there is no &#8216;Signed-off-by: &#8216; already, and show how it works: </p>
<dl>
<dt>
<dd>
$ git config trailer.sign.key &#8220;Signed-off-by: &#8221; $ git config trailer.sign.ifmissing add<br />
                $ git config trailer.sign.ifexists doNothing<br />
                    $ git config trailer.sign.command &#8216;echo &#8220;$(git config user.name) &lt;$(git config user.email)&gt;&#8221;&#8216; $ git interpret &#8211;<br />
            trailers<br />
        &lt;&lt; EOF &gt;<br />
    EOF<br />
                Signed &#8211;<br />
            off &#8211; by : Bob&lt;bob[at] example.com&gt; $ git interpret &#8211; trailers<br />
        &lt;&lt; EOF &gt;<br />
    Signed &#8211; off &#8211; by : Alice&lt;alice[at] example.com&gt; &gt; EOF<br />
                                                               Signed &#8211;<br />
                                                           off &#8211; by : Alice&lt;alice[at] example.com&gt;
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Configure a <i>fix</i> trailer with a key that contains a <i>#</i> and no space after this character, and show how it works: </p>
<dl>
<dt>
<dd>
<pre>
$ git config trailer.separators &quot;:#&quot;
$ git config trailer.fix.key &quot;Fix #&quot;
$ echo &quot;subject&quot; | git interpret-trailers --trailer fix=42
subject
Fix #42
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Configure a <i>help</i> trailer with a cmd use a script <code>glog-find-author</code> which search specified author identity from git log in git repository and show how it works: </p>
<dl>
<dt>
<dd>
$ cat ~ / bin / glog &#8211; find &#8211; author<br />
#!/ bin / sh<br />
                                  test &#8211;<br />
    n &#8220;$1&#8221; &amp;&amp;git log&#8211; author = &#8220;$1&#8221; &#8211;pretty = &#8220;%an &lt;%ae&gt;&#8221; &#8211; 1 || true $ git config trailer.help.key &#8220;Helped-by: &#8221; $ git config trailer.help.ifExists &#8220;addIfDifferentNeighbor&#8221; $ git config trailer.help.cmd &#8220;~/bin/glog-find-author&#8221; $ git interpret &#8211; trailers&#8211; trailer = &#8220;help:Junio&#8221; &#8211;trailer = &#8220;help:Couder&#8221; &lt;&lt; EOF &gt; subject &gt;&gt; message &gt;&gt; EOF<br />
                                                                                                                                                                                                                                                                                                                                                            subject<br />
                                                                                                                                                                                                                                                                                                                                                                message<br />
                                                                                                                                                                                                                                                                                                                                                                    Helped &#8211;<br />
                                                                                                                                                                                                                                                                                                                                                        by : Junio C Hamano&lt;gitster[at] pobox.com&gt;<br />
                                                                                                                                                                                                                                                                                                                                                                 Helped &#8211;<br />
                                                                                                                                                                                                                                                                                                                                                             by : Christian Couder&lt;christian.couder[at] gmail.com&gt;
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Configure a <i>ref</i> trailer with a cmd use a script <code>glog-grep</code> to grep last relevant commit from git log in the git repository and show how it works: </p>
<dl>
<dt>
<dd>
$ cat ~ / bin / glog &#8211; grep<br />
#!/ bin / sh<br />
                           test &#8211;<br />
    n &#8220;$1&#8221; &amp;&amp;git log&#8211; grep &#8220;$1&#8221; &#8211;pretty = reference &#8211; 1 || true $ git config trailer.ref.key &#8220;Reference-to: &#8221; $ git config trailer.ref.ifExists &#8220;replace&#8221; $ git config trailer.ref.cmd &#8220;~/bin/glog-grep&#8221; $ git interpret &#8211; trailers&#8211; trailer = &#8220;ref:Add copyright notices.&#8221; &lt;&lt; EOF &gt; subject &gt;&gt; message &gt;&gt; EOF<br />
                                                                                                                                                                                                                                                                                                                      subject<br />
                                                                                                                                                                                                                                                                                                                          message<br />
                                                                                                                                                                                                                                                                                                                              Reference &#8211;<br />
                                                                                                                                                                                                                                                                                                                  to : 8bc9a0c769(Add copyright notices., 2005 &#8211; 04 &#8211; 07)
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Configure a <i>see</i> trailer with a command to show the subject of a commit that is related, and show how it works: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git config trailer.see.key "See-also: " $ git config trailer.see.ifExists "replace" $ git config trailer.see.ifMissing "doNothing" $ git config trailer.see.command "git log -1 --oneline --format=\"%h (%s)\" --abbrev-commit --abbrev=14 \$ARG" $ git interpret - trailers &lt;&lt; EOF &gt; subject &gt;&gt; message &gt;&gt; see : HEAD ~2 &gt; EOF
                                                                                                                                                                                                                                                                                                                                      subject
                                                                                                                                                                                                                                                                                                                                          message
                                                                                                                                                                                                                                                                                                                                              See -
                                                                                                                                                                                                                                                                                                                                  also : fe3187489d69c4(subject of related commit)
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Configure a commit template with some trailers with empty values (using sed to show and keep the trailing spaces at the end of the trailers), then configure a commit-msg hook that uses <i>git interpret-trailers</i> to remove trailers with empty values and to add a <i>git-version</i> trailer: </p>
<dl>
<dt>
<dd>
<pre>
$ sed -e 's/ Z$/ /' &gt;commit_template.txt &lt;&lt;EOF
&gt; ***subject***
&gt;
&gt; ***message***
&gt;
&gt; Fixes: Z
&gt; Cc: Z
&gt; Reviewed-by: Z
&gt; Signed-off-by: Z
&gt; EOF
$ git config commit.template commit_template.txt
$ cat &gt;.git/hooks/commit-msg &lt;&lt;EOF
&gt; #!/bin/sh
&gt; git interpret-trailers --trim-empty --trailer &quot;git-version: \$(git describe)&quot; &quot;\$1&quot; &gt; &quot;\$1.new&quot;
&gt; mv &quot;\$1.new&quot; &quot;\$1&quot;
&gt; EOF
$ chmod +x .git/hooks/commit-msg
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1), <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1), <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
