---
title: "prwdrc(5)"
name: "prwdrc"
section: "5"
letter: "p"
url: "/docs/linux/man/5-prwdrc/"
description: "prwdrc – prwd configuration file"
---

<p><code>prwdrc</code> &#8211; prwd configuration file</p>
<h2>Synopsis</h2>
<p><code>~/.prwdrc</code></p>
<h2>Description</h2>
<p>The <code>~/.prwdrc</code> file describes the template and various attributes affecting the behavior of <code>prwd.</code> The configuration file has the following format: Empty lines and lines starting with `#&#8217; are comments, otherwise a line is of the format &#8220;keyword arguments&#8230;&#8221;. Configuration arguments may be separated by whitespace. Arguments may optionally be enclosed in double quotes (&quot;) in order to represent arguments containing spaces. The possible keywords and their meanings are as follows:</p>
<dl>
<dt><code> alias</code> [<i>name</i> ] [<i>path</i> ]</p>
<dd>
<dd>Defines a new alias which could be used as a path shortener (see path in the TEMPLATE COMMANDS section) and as a shortcut (see <a href="/docs/linux/man/1-prwd/">prwd</a>(1) and its -a parameter). The <i>name</i> defines the short key used as replacement to the <i>path</i> See the ALIASES section below for a more complete description.</p>
<dt><code> set</code> [<i>key</i> ] [<i>value</i> ]</p>
<dd>
<dd>Sets the global configuration parameter <i>key</i> to <i>value</i> See the GLOBAL SETTINGS section below for a complete list of settings and their impact on <code>prwd</code></p>
<dt><code> template</code> [<i>value</i> ]</p>
<dd>
<dd>Defines your shell prompt template. See the section below.</dl>
<h2>Template Syntax</h2>
<p><code>~/.prwdrc</code> has a simple templating language with a few small commands providing basic information about your shell context. All the commands start with &#8220;${&#8220; and end with &#8220;}&#8221;, within these brackets the syntax uses flags and is very similar to standard UNIX tools. </p>
<p> Here is a simple template definition: </p>
<blockquote>
<pre>template &quot;${path -l 20}&gt; &quot;</pre>
</blockquote>
<p> This simple template returns your current path, up to 20 characters and a static &quot;&gt; &quot; suffix. </p></blockquote>
<h2>Template Commands</h2>
<p>The following commands available to customize your shell prompt:</p>
<dl>
<dt><code> path</code> [-<code>nc</code> ] [-<code>l </code><i>length</i> ] [-<code>f </code><i>filler</i> ]</p>
<dd>
<dd>Returns the current path (similar to the pwd command). The command-line options are as follows:</p>
<dl>
<dt><code>-n</code></p>
<dd>Return the current path using a USENET/newsgroup-style naming convention, i.e. only use the first letters of each path component.</p>
<dt><code>-c</code></p>
<dd>Attempt to keep all the path components intact (cut at the slash).</p>
<dt><code>-l </code><i>length</i></p>
<dd>Length of the final path output, including any possibly ellipsis/filler. Default: 24</p>
<dt><code>-f </code><i>filler</i></p>
<dd>String to use as ellipsis/filler on trimmed paths. Default: &quot;&#8230;&quot;</dl>
<dt><code> branch</code></p>
<dd>
<dd>Display the current branch if you happen to be in a mercurial or git repository.</p>
<dt><code> date</code> [<i>format</i> ]</p>
<dd>
<dd>Returns the current date/time using the provided format. See <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for more information on the format.</p>
<dt><code> hostname</code> [-<code>l</code> ]</p>
<dd>
<dd>Returns the current short hostname (up until the first dot). If the -l parameters is given, this command returns the long hostname.</p>
<dt><code> uid</code></p>
<dd>
<dd>Returns the &#8220;$&#8221; character if the user has UID != 0 and &#8220;#&#8221; otherwise. This is typically used at the end of a template, just before the trailing space.</p>
<dt><code> sep</code> [<i>value</i> ]</p>
<dd>
<dd>Define an optional separator. If the token immediately before the <i>sep</i> command is empty, the value of the separator is not returned. This is useful on prompts featuring some items that could be empty from time to time (e.g. branch).</dl>
<h2>Aliases</h2>
<p>If you use the <i>path</i> command in your prompt, defining aliases will allow <i>path</i> to shorten the paths using your own defined keywords. For example: </p>
<blockquote>
<pre>alias *prwd /home/tamentis/projects/prwd</pre>
</blockquote>
<p> If you are in &quot;/home/tamentis/projects/prwd/doc/html/&quot;, prwd would return &quot;*prwd/doc/html&quot;. If you have spaces in your directories, you can wrap your <i>path</i> parameters with double quotes: </p>
<blockquote>
<pre>alias windocs &quot;/mnt/Windows XP/My Documents/&quot;</pre>
</blockquote>
<p> You can define multiple values for a single alias, <code>prwd</code> will pick the one with an existing path. This allows you to share your configuration on different machines and use the same shortened alias, for example: </p>
<blockquote>
<pre>alias *prwd /home/tamentis/projects/prwd
alias *prwd /Users/tamentis/projects/prwd</pre>
</blockquote>
<p> Aliases can be nested one level deep if you have a complicated directory hierarchy. </p>
<blockquote>
<pre>alias *prwd /home/tamentis/projects/prwd
alias *prwddoc *prwd/doc</pre>
</blockquote>
<p> Since you already define your aliases in your <code>~/.prwdrc</code> file, you might want to use them in your shell. If you prefix your aliases with a &#8216;$&#8217; and add the following line to your .profile, you will be able to have your aliases available as environment variables. Add this to your profile or shell configuration file: </p>
<blockquote>
<pre>eval `prwd -a`</pre>
</blockquote>
<p> Then use your aliases like any environment variable: </p>
<blockquote>
<pre>cd $py3k</pre>
</blockquote>
<p> Note that ~ is a default alias for prwd.</p>
<h2>Global Settings</h2>
<p>Settings are defined with the <i>set</i> command, the first argument is the name of the setting, the second is the value:</p>
<dl>
<dt><code> set maxlength</code> [<i>length</i> ]</p>
<dd>
<dd>This setting is deprecated and was replaced by the -l parameter of the path command. If no template is defined, this will set the path length in the default template.</p>
<dt><code> set filler</code> [<i>value</i> ]</p>
<dd>
<dd>This setting is deprecated and was replaced by the -f parameter of the path command. If no template is defined, it sets the path filler/ellipsis in the default template.</p>
<dt><code> set cleancut</code> [<i>bool</i> ]</p>
<dd>
<dd>This setting is deprecated and was replaced by the -c parameter of the path command. If no template is defined, it sets the cleancut flag on in the default template, avoiding <code>prwd</code> from cutting path in the middle. For example &quot;&#8230;rwd/doc/html&quot; will be returned as &quot;&#8230;/doc/html&quot;.</p>
<dt><code> set newsgroup</code> [<i>bool</i> ]</p>
<dd>
<dd>This setting is deprecated and was replaced by the -n parameter of the path command. If no template is defined, it sets the newsgroup flag on in the default template, shortening the path by only displaying the first letter of each path components. For example &quot;/home/tamentis/projects/prwd/src/nowhere&quot; is turned into &quot;/h/t/p/s/nowhere&quot;.</p>
<dt><code> set mercurial</code> [<i>bool</i> ]</p>
<dd>
<dt><code> set git</code> [<i>bool</i> ]</p>
<dd>
<dd>This setting is deprecated and was replaced by the ${branch} command. If no template was defined, it will add the branch information between the hostname and the path in the default template.</p>
<dt><code> set hostname</code> [<i>bool</i> ]</p>
<dd>
<dd>This setting is deprecated and was replaced by the ${hostname} command. If no template was defined, it will add the hostname information at the beginning of the default template.</p>
<dt><code> set uid_indicator</code> [<i>bool</i> ]</p>
<dd>
<dd>This setting is deprecated and was replaced by the ${uid} command. If no template was defined, it will add the uid character at the end of the default template.</dl>
<h2>Example</h2>
<p>This example configuration defines two aliases and a template with the time: </p>
<blockquote>
<pre>alias $ports /usr/ports
alias $p /home/tamentis/projects
template &quot;${date} ${hostname}:${branch}${sep :}${path -l 24}${uid} &quot;</pre>
</blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-pwd/">pwd</a>(1), <a href="/docs/linux/man/1-csh/">csh</a>(1), <a href="/docs/linux/man/1-ksh/">ksh</a>(1), <a href="/docs/linux/man/1-sh/">sh</a>(1), <a href="/docs/linux/man/3-getcwd/">getcwd</a>(3)</p>
<h2>Authors</h2>
<p>prwd was written by Bertrand Janin &lt;b@janin.com&gt; and is distributed under an ISC license (BSD compatible, OSI compatible).</p>
