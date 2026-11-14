---
title: "clide(1)"
name: "clide"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clide/"
description: "clide – color and style highlighting program for text"
---

<h2 class="name">NAME</h2>
<p> clide &#8211; color and style highlighting program for text </p>
<h2>SYNOPSIS</h2>
<p> <code>clide</code> [options] [file1] [file2] [&#8230;fileN] </p>
<p> <code>| clide</code> [options] (<font SIZE="-1">STDIN</font> through pipe) </p>
<p> <code>clide</code> [options] (<font SIZE="-1">STDIN.</font> Use Ctrl-D to finish input)</p>
<h2>DESCRIPTION</h2>
<p> clide is a program that allows you to colorize and add various display altering attributes to text based on search patterns and expressions. Currently the focus is on creating <font SIZE="-1">ANSI</font> color and style escape codes for use in terminal displays.</p>
<h2>OPTIONS</h2>
<pre><code>
  -h, --help - Show some terse help for the program
  -e, --expression &lt;expression&gt;,&lt;attributes&gt;
      Examples:
         -e /searchpattern/,fg=red,bold
         -e HTMLTAG,fg=blue,bg=yellow
  -d, --definitionfile &lt;file&gt;
  -f, --expressionfile &lt;file&gt;
  --listcolors - Show a list of foreground and background colors
                 that can be used.
  --liststyles - Show a list of styles that can be used (not all
                 of which may work on your display)
  --listdefinitions - Show a list of predefined search expressions
  --reverseprecedence, -r - Reverse the precedence order in which
                 expressions are run through.
  --wf, --warmfuzzy "&lt;message&gt;" -
                Send the developer a short message to let him know that you like this program.
</code></pre>
<h2>EXAMPLES</h2>
<h3><font SIZE="-1">FILE ARGUMENTS</font></h3>
<p> One way to utilize clide is to process the contents of a file or multiple files. This is done simply by passing the files as arguments after the other options you wish to specify for matching expressions: </p>
<pre>
 clide -e HTMLTAG,fg=yellow index.html
</pre>
<h3><font SIZE="-1">PIPELINES</font></h3>
<p> Another way to use clide is by passing the output of one program into it. You are sending the standard output (<font SIZE="-1">STDOUT</font>) of one program to the standard input (<font SIZE="-1">STDIN</font>) of clide. Like this command that sends the output of ls through clide, which colors lines that are directory entries: </p>
<pre>
 ls -l | clide -e /^d.*/,fg=blue,bold
</pre>
<h3><font SIZE="-1">SHELL ESCAPING</font></h3>
<p> If you are creating more complex search patterns, you are probably going to need to put quotes around the whole argument that is passed to a -e option. This is because your shell will interpret certain characters like (, ), $, &amp;, [, ], etc. For example, this command uses an expression that will change the percentage display of a filesystem to red if it is 94% or more: </p>
<pre>
 df -h | clide -e &quot;/(100|9[4-9])%/,fg=red,bold&quot;
</pre>
<p> But because ( ) is used in most shells as a subshell sequence, you have to put quotes around the whole expression so that its not processed by your shell.</p>
<h2>EXPRESSIONS</h2>
<p> Expressions can be specified on the command line using one or more -e options. You can also use the -f option one or more times to specify premade expression files.</p>
<h3><font SIZE="-1">PERL REGULAR EXPRESSIONS</font></h3>
<p> clide works by passing the expression that you specify into a <font SIZE="-1">PERL</font> matching operator. This means that you can pass almost any valid <font SIZE="-1">PERL</font> regular expression to clide and it should work as expected. </p>
<p> The only limitation is in what flags you can pass to the search. Currently, you can only pass a &#8216;i&#8217; (case insensitive) and/or a &#8216;g&#8217; (global search) flag to the search expression. The multiline flag &#8216;m&#8217; is not supported. </p>
<p> For more information about perl regular expressions, see the <i><a href="/docs/linux/man/1-pcre/">pcre</a></i>(1) man page.</p>
<h3><font SIZE="-1">REGULAR EXPRESSION SEARCH</font></h3>
<p> The basic way to tell clide what text you want to affect is to use the regular expression search operator. This is passed to the -e option along with a command seperated list of attributes to set. </p>
<pre>
 clide -e /failed/i,fg=yellow,bg=red,bold
</pre>
<p> The above expression searches for the word failed (using the i option after the second / means make the search case insensitive). It will change the word failed to have a foreground color of bold yellow (bright) and a background color of red.</p>
<h3><font SIZE="-1">PREDEFINED SEARCH PATTERNS</font></h3>
<p> A list of helpful predefined search patterns is included with clide to make pattern matching easier for the user. A list of the patterns is available by running clide with the &#8211;listdefinitions option. You can also put your own definitions in files and use the -f option to include them. </p>
<p> Using a predefined search expression is simply a matter of using its name for the first part of the -e argument, like this: </p>
<pre>
 clide -e HOSTNAME,bold logfile.txt
</pre>
<p> <font SIZE="-1">WARNING:</font> Predefined search patterns <font SIZE="-1">MUST</font> use all uppercase names. In the future clide may have other expression functions that start with lower case letters and there needs to be a way to differentiate between a pattern definition and an operation.</p>
<h2>FILE FORMATS</h2>
<p> <font SIZE="-1">NOTE:</font> The author would like to encourage you to put your expression and definition files in a directory called .clide in your home directory. Future versions of clide may make it easier to use these files if you have them located in such a named directory.</p>
<h3><font SIZE="-1">EXPRESSION FILE</font></h3>
<p> The expression file is pretty simple, you put each expression one per line in exactly the same way that you would pass it to the -e option. expression definitions can be used as the expressions themselves are parsed after all the predefined expressions are read in. You can include these files using the -f option. </p>
<p> So an expression file called microblogging might look like this: </p>
<pre>
 HTMLTAG,fg=red,bg=black
 URL,fg=yellow,bold,underline
 TWITTERGROUP,fg=blue,bold
 # Highlight some of my MB account names
 /@(mkrenz|climagic|suso)/,fg=yellow,bg=blue,bold
 TWITTERMENTION,fg=cyan
 IDENTICAGROUP,fg=blue,bold
</pre>
<p> Then you&#8217;d use it like this: </p>
<pre>
 twidge lsrecent | clide -f ~/.clide/microblogging
</pre>
<p> Comments can be made using a # character at the beginning of the line.</p>
<h3><font SIZE="-1">DEFINITION FILE</font></h3>
<p> The definition file has a bit more of a format to it. Each line has two columns seperated by whitespace. The first column is the name of the definition in all uppercase letters. The second column is the search expression starting with a forward slash and terminated by a forward slash and one or more pcre flags (i or g) </p>
<pre><code>
#These are IPs I'm watching out for.
INTERESTINGIPS /(
    3\.14\.159\.26 | 206\.97\.64\.[29] | 10\.[0 - 9] { 1, 3 }\.[0 - 9] { 1, 3 }\.[0 - 9] { 1, 3 })
    / g
#Words I care about.
    LOGINWORDS
    / (error | failed | failure | success | successful) / gi
</code></pre>
<p> Then just include the file using -d for each file you want to include. </p>
<p> Note that you don&#8217;t need to escape or backslash as much in the searches when you put them in a file as compared with when you specify the pattern on the command line. Keep this in mind if you copy and paste your expressions into a file.</p>
<h2>BUGS AND LIMITATIONS</h2>
<p> Because one expression matching will actually alter the line in order to add the escape sequences, matching expressions that are run later may not match what the user expects them to match because the string has changed. This is going to be fixed in a future release. </p>
<p> Currently clide can only work on 7-bit <font SIZE="-1">ASCII</font> text. If it encounters a line with upper 8-bit (binary) characters, it will simply print the line with out doing any processing on it. If you&#8217;re really curious as to why, you can read the comments in the code or ask the author. A future version of clide may not have this limitation. </p>
<p> Most terminal emulators and the console itself have some limitations as to what they can display. Most of them don&#8217;t support blinking text, only some support dark mode, etc. This is not a limitation of clide, it is your terminal software. </p>
<p> clide doesn&#8217;t support multiline matching at this time.</p>
<h2>SEE ALSO</h2>
<p> pcre</p>
<h2>WARMFUZZY</h2>
<p> If you like clide, you should let the author know by sending a short message using the &#8211;warmfuzzy option, like this: </p>
<pre>
 clide --warmfuzzy &quot;I like clide&quot;
</pre>
<p> This option makes an <font SIZE="-1">HTTP</font> request to a website that will in turn let the author know what you thought. </p>
<p> I included this option because I think that open source projects need an easier way for users to give the developers a little reward for their efforts.</p>
<h2>COPYRIGHT</h2>
<p> This code is copyright 2010 by Mark Krenz under the terms of the <font SIZE="-1">GNU GPL</font> version 3. See the file <font SIZE="-1">COPYING</font> that comes with clide for more details.</p>
<h2>MORE INFO</h2>
<p> You can find more information about clide at its website at </p>
<pre>
 L&lt;<a rel="nofollow" href="http://suso.suso.org/xulu/clide">http://suso.suso.org/xulu/clide</a>&gt;
</pre>
<p> If you&#8217;d like to get involved with development in any way, please feel free to contact the author.</p>
<h2>AUTHOR</h2>
<p> clide was written by Mark Krenz &lt;mark [at] suso.com&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAJ">EXPRESSIONS</a></p>
<dd>
<dt><a href="#lbAN">FILE FORMATS</a></p>
<dd>
<dt><a href="#lbAQ">BUGS AND LIMITATIONS</a></p>
<dd>
<dt><a href="#lbAR">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAS">WARMFUZZY</a></p>
<dd>
<dt><a href="#lbAT">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAU">MORE INFO</a></p>
<dd>
<dt><a href="#lbAV">AUTHOR</a></p>
<dd></dl>
