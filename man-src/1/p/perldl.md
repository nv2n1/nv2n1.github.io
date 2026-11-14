---
title: "perldl(1)"
name: "perldl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldl/"
description: "perldl – Simple shell for PDL (see also pdl2)"
---

<h2 class="name">NAME</h2>
<p> perldl &#8211; Simple shell for PDL (see also pdl2) </p>
<h2>SYNOPSIS</h2>
<p> Use <font SIZE="-1">PDL</font> interactively: </p>
<pre>
  bash$ perldl
  pdl&gt; $a = sequence(10) # or any other perl or PDL command
  
  bash$ pdl
  pdl&gt; print &quot;Hello, world!
&quot;;
</pre>
<p> Run a script: </p>
<pre>
  bash$ cat &gt; pdlscript
  #!/usr/bin/pdl
  print &quot;Hello, world!
&quot;;
  ...
</pre>
<h2>DESCRIPTION</h2>
<p> The program <code>perldl</code> is a simple shell (written in perl) for interactive use of <font SIZE="-1">PDL. </font> It consists of a command-line interface that supports immediate interpretation of perl commands and expressions. Perl expressions, including <font SIZE="-1">PDL</font> constructs, can be entered directly at the keyboard and are compiled and executed immediately. The syntax is not exactly identical to Perl, in that under most circumstances ending a line causes immediate execution of the command entered so far (no trailing &#8216;;&#8217; is required). </p>
<p> The synonym <code>pdl</code> is a compiled executable that is useful as a script interpreter using <font SIZE="-1">UNIX</font> shebang (<tt>&quot;#!&quot;</tt>) syntax. This is useful for generating and re-executing command-journal files from <code>perldl</code>. </p>
<p> The <code>perldl</code> shell runs an initial startup file (<tt>&quot;~/.perldlrc&quot;</tt>) that can be used to pre-load perl modules or configure the global perl environment. It features a path mechanism for autoloading perl subroutines. There is a command-history mechanism, and several other useful features such as command preprocessing, shortcuts for commonly used commands such as &#8220;print&#8221;, and the ability to execute arbitrary code whenever a prompt is printed. </p>
<p> Depending on your configuration settings, <code>perldl</code> can be set to honor or ignore the ^D (end-of-file) character when sent from a terminal, or to attempt to do the Right Thing when a block construct spanning multiple lines is encountered. </p>
<p> <code>perldl</code> and <code>pdl</code> support several command-line options, which are discussed near the end of this document.</p>
<h3>Reference manual &amp; online help</h3>
<p> The <font SIZE="-1">PDL</font> reference manual and online help are available from within <code>perldl</code>, using the <code>help</code> and <code>apropos</code> commands (which may also be abbreviated <code>?</code> and <code>??</code>.) The <code>help</code> command alone prints a summary of help syntax, and <code>help &lt;module-name&gt;</code> will print <font SIZE="-1">POD</font> documentation from the module you mention (<font SIZE="-1">POD</font> is the Perl format for embedding documentation in your perl code; see perlpod for details). </p>
<p> If you include <font SIZE="-1">POD</font> documentation in your autoload subroutines (see <code>path mechanism</code> below), then both <code>help</code> and <code>apropos</code> will find it and be able to format and display it on demand.</p>
<h3>History mechanism</h3>
<p> If you have the perl modules ReadLines and ReadKeys installed, then <code>perldl</code> supports a history and line-editing mechanism using editing keys similar to emacs. The last 500 commands are always stored in the file <i>.perldl_hist</i> in your home directory between sessions. Set <tt>$PERLDL::HISTFILESIZE</tt> to change the number of lines saved. The command <tt>&quot;l [number]&quot;</tt> shows you the last <tt>&quot;number&quot;</tt> commands you typed where <tt>&quot;number&quot;</tt> defaults to 20. </p>
<p> e.g.: </p>
<pre>
   bash$ perldl
   ReadLines enabled
   pdl&gt; $a = rfits &quot;foo.fits&quot;
   BITPIX =  -32  size = 88504 pixels
   Reading  354016 bytes
   BSCALE =  &amp;&amp;  BZERO =
   pdl&gt; imag log($a+400)
   Displaying 299 x 296 image from 4.6939525604248 to 9.67116928100586 ...
</pre>
<h3>Command execution</h3>
<p> If you enter a simple command at the <code>perldl</code> command line, it is immediately executed in a Perl <tt>&quot;eval()&quot;</tt>. The environment is almost identical to that within a perl script, with some important exceptions:</p>
<dl>
<dt>&bull;</p>
<dd> <tt>$_</tt> is not preserved across lines </p>
<p> <tt>$_</tt> is used to hold the command line for initial processing, so at the beginning of processing of each command line, <tt>$_</tt> contains the command itself. Use variables other than <tt>$_</tt> to store values across lines.</p>
<dt>&bull;</p>
<dd> Scope is not preserved across lines </p>
<p> Each command line is executed in a separate <tt>&quot;eval&quot;</tt> block within perl, so scoping commands such as <tt>&quot;my&quot;</tt> and <tt>&quot;local&quot;</tt> may not perform exactly as expected &#8212; in particular, if you declare a variable with <tt>&quot;my&quot;</tt>, it is local to the particular command line on which you typed the <tt>&quot;my&quot;</tt> command, which means that it will evaporate before the next prompt is printed. (You can use <tt>&quot;my&quot;</tt> variables in a multi-line block or to isolate values within a single command line, of course). </p>
<pre>
  NOTE: pdl2 preserves lexical scope between lines.
</pre>
<dt>&bull;</p>
<dd> Execution is immediate </p>
<p> Under most circumstances, as soon as you end a line of input the line is parsed and executed. This breaks Perl&#8217;s normal dependence on semicolons as command delimiters. For example, the two-line expression </p>
<pre>
  print &quot;Hello &quot;,
     &quot;world&quot;;
</pre>
<p> prints the phrase <tt>&quot;Hello world&quot;</tt> in Perl, but (under most circumstances) <tt>&quot;Hello &quot;</tt> in <code>perldl</code>.</p>
<dt>&bull;</p>
<dd> Multi-line execution </p>
<p> In multiline mode (which is enabled by default, see <code>Shell variables</code>, below), <code>perldl</code> searches for searches for block-like constructs with curly braces, parentheses, quotes, and related delimiters. If you leave such a construct open, <code>perldl</code> accepts more lines of input until you close the construct or explictly end the multi-line expression with ^D. Following the example above, the phrase </p>
<pre>
  { print &quot;Hello &quot;,
       &quot;world&quot;; }
</pre>
<p> will print &#8220;Hello world&#8221; from either Perl or (in multi-line mode) <code>perldl</code>. </p>
<p> <code>Warning</code>: The multi-line parsing uses Damian Conway&#8217;s Text::Balanced module, which contains some flaws &#8212; so it can be fooled by quote-like operators such as <tt>&quot;q/.../&quot;</tt>, included <font SIZE="-1">POD</font> documentation, multi-line <tt>&quot;&lt;&lt;&quot;</tt> quotes, and some particularly bizarre-but-valid <tt>&quot;m/.../&quot;</tt> matches and <tt>&quot;s/.../.../&quot;</tt> substitutions. In such cases, use ^D to close out the multi-line construct and force compilation-and-execution.</dl>
<p> If you want to preserve this behavior in a script (for example to replay a command journal file; see below on how to create one), you can use <code>pdl</code> instead of <code>perl</code> as the interpreter in the script&#8217;s initial shebang line.</p>
<h3>Terminating perldl</h3>
<p> A <tt>&quot;perldl&quot;</tt> session can be terminated with any of the commands <tt>&quot;quit&quot;</tt>, <tt>&quot;exit&quot;</tt> or the shorthands <tt>&quot;x&quot;</tt> or <tt>&quot;q&quot;</tt>. If <font SIZE="-1">EOF</font> handling is switched on (the default) you can also type ^D at the command prompt. </p>
<p> If the command input is <font SIZE="-1">NOT</font> a terminal (for example if you are running from a command journal file), then <font SIZE="-1">EOF</font> will always terminate <code>perldl</code>.</p>
<h3>Terminating commands (Ctrl-C handling)</h3>
<p> Commands executed within <tt>&quot;perldl&quot;</tt> can be terminated prematurely using <tt>&quot;Ctrl-C&quot;</tt> (or whichever key sequence sends an <font SIZE="-1">INT</font> signal to the process on your terminal). Provided your <font SIZE="-1">PDL</font> code does not ignore <tt>&quot;sigint&quot;</tt>s this should throw you back at the <tt>&quot;perldl&quot;</tt> command prompt: </p>
<pre>
  pdl&gt; $result = start_lengthy_computation()
   &lt;Ctrl-C&gt;
 Ctrl-C detected
  pdl&gt;
</pre>
<h3>Shortcuts and aliases</h3>
<dl>
<dt>&bull;</p>
<dd> The shell aliases <tt>&quot;p&quot;</tt> to be a convenient short form of <tt>&quot;print&quot;</tt>, e.g. </p>
<pre><code>
pdl &gt; p ones 5, 3
                    [
                        [1 1 1 1 1]
                            [1 1 1 1 1]
                            [1 1 1 1 1]]
</code></pre>
<dt>&bull;</p>
<dd> <tt>&quot;q&quot;</tt> and <tt>&quot;x&quot;</tt> are short-hand for <tt>&quot;quit&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;l&quot;</tt> lists the history buffer </p>
<pre>
  pdl&gt; l # list last 20 commands
  pdl&gt; l 40 # list last 40 commands
</pre>
<dt>&bull;</p>
<dd> <tt>&quot;?&quot;</tt> is an alias for help </p>
<pre>
  pdl&gt; ? pdl2    # get help for new pdl2 shell
</pre>
<dt>&bull;</p>
<dd> <tt>&quot;??&quot;</tt> is an alias for apropos </p>
<pre>
  pdl&gt; ?? PDL::Doc
</pre>
<dt>&bull;</p>
<dd> help, apropos, usage and sig: all words after these commands are used verbatim and not evaluated by perl. So you can write, e.g., </p>
<pre>
  pdl&gt; help help
</pre>
<p> instead of </p>
<pre>
  pdl&gt; help 'help'
</pre>
</dl>
<h3>Command-line options</h3>
<p> <code>perldl</code> and <code>pdl</code> support several command-line options to adjust the behavior of the session. Most of them are equivalent to commands that can be entered at the <code>pdl&gt;</code> prompt. They are:</p>
<dl>
<dt>-glut</p>
<dd> Load OpenGL when starting the shell (the perl OpenGL module, which is available from <font SIZE="-1">CPAN</font> must be installed). This enables readline event loop processing. Don&#8217;t use with -tk.</p>
<dt>-tk</p>
<dd> Load Tk when starting the shell (the perl Tk module, which is available from <font SIZE="-1">CPAN</font> must be installed). This enables readline event loop processing. Don&#8217;t use with -glut.</p>
<dt>-f file</p>
<dd> Loads the file before processing any user input. Any errors during the execution of the file are fatal.</p>
<dt>-w</p>
<dd> Runs with warning messages (i.e. the normal perl <tt>&quot;-w&quot;</tt> warnings) turned-on.</p>
<dt>-M module</p>
<dd> Loads the module before processing any user input. Compare corresponding <tt>&quot;perl&quot;</tt> switch.</p>
<dt>-m module</p>
<dd> Unloads the module before processing any user input.</p>
<dt>-I directory</p>
<dd> Adds directory to the include path. (i.e. the <tt>@INC</tt> array) Compare corresponding <tt>&quot;perl&quot;</tt> switch.</p>
<dt>-V</p>
<dd> Prints a summary of <font SIZE="-1">PDL</font> config. This information should be included with any <font SIZE="-1">PDL</font> bug report. Compare corresponding <tt>&quot;perl&quot;</tt> switch.</dl>
<h3>The startup file <i>~/.perldlrc</i></h3>
<p> If the file <i>~/.perldlrc</i> is found it is sourced at start-up to load default modules, set shell variables, etc. If it is <font SIZE="-1">NOT</font> found the distribution file <i>PDL/default.perldlrc</i> is read instead. This loads various modules considered useful by default, and which ensure compatibility with v1.11. If you don&#8217;t like this and want a more streamlined set of your own favourite modules simple create your own <i>~/.perldlrc</i>. You may wish to start from the existing <i>PDL/default.perldlrc</i> as a template since it will not be sourced once you replace it with your own version. </p>
<p> To set even more local defaults the file <i>local.perldlrc</i> (in the current directory) is sourced if found. This lets you load modules and define subroutines for the project in the current directory. </p>
<p> The name is chosen specfically because it was found hidden files were <font SIZE="-1">NOT</font> wanted in these circumstances. </p>
<p> The startup file should normally include &#8220;use PDL::AutoLoader;&#8221;, as many of the nicer interactive features won&#8217;t work without it.</p>
<h3>Shell variables</h3>
<p> Shell variables: (<i>Note</i>: if you don&#8217;t like the defaults change them in <i>~/.perldlrc</i>)</p>
<dl>
<dt>&bull;</p>
<dd> <tt>$PERLDL::ESCAPE</tt> &#8211; default value &#8216;#&#8217; </p>
<p> Any line starting with this character is treated as a shell escape. The default value is chosen because it escapes the code from the standard perl interpreter.</p>
<dt>&bull;</p>
<dd> <tt>$PERLDL::HISTFILESIZE</tt> &#8211; default value 500 </p>
<p> This is the number of lines of perldl shell command history to keep.</p>
<dt>&bull;</p>
<dd> <tt>$PERLDL::PAGER</tt> &#8211; default value <tt>&quot;more&quot;</tt> </p>
<p> External program to filter the output of commands. Using <tt>&quot;more&quot;</tt> prints output one screenful at a time. On Unix, setting <tt><a href="/docs/linux/man/1-page/">page</a>(1)</tt> and <tt>$PERLDL::PAGER</tt> to <tt>&quot;tee -a outfile&quot;</tt> will keep a record of the output generated by subsequent perldl commands (without paging).</p>
<dt>&bull;</p>
<dd> <tt>$PERLDL::PROMPT</tt> &#8211; default value &#8216;pdl&gt; &#8216; </p>
<p> Enough said But can also be set to a subroutine reference, e.g. <tt>$PERLDL::PROMPT</tt> = sub {join(&#8216;:&#8217;,(gmtime)[2,1,0]).&#8217;&gt; &#8216;} puts the current time into the prompt.</p>
<dt>&bull;</p>
<dd> <tt>$PERLDL::MULTI</tt> &#8211; default value 1 </p>
<p> If this is set to a true value, then perldl will parse multi-line perl blocks: your input will not be executed until you finish a line with no outstanding group operators (such as quotes, blocks, parenthesis, or brackets) still active. Continuation lines have a different prompt that shows you what delimiters are still active. </p>
<p> Note that this is not (yet!) a complete perl parser. In particular, Text::Balanced appears to be able to ignore quoting operatores like <tt>&quot;q/ ... /&quot;</tt> within a line, but not to be able to extend them across lines. Likewise, there is no support for the &#8216;&lt;&lt;&#8216; operator. </p>
<p> Multiline conventional strings and {}, [], and () groupings are well supported.</p>
<dt>&bull;</p>
<dd> <tt>$PERLDL::NO_EOF</tt> &#8211; default value 0 / 1 on MSWin32 </p>
<p> Protects against accidental use of &#8220;^D&#8221; from the terminal. If this is set to a true value, then you can&#8217;t accidentally exit perldl by typing &#8220;^D&#8221;. If you set it to a value larger than 1 (and <font SIZE="-1">PERLDL::MULTI</font> is set), then you can&#8217;t use &#8220;^D&#8221; to exit multiline commands either. If you&#8217;re piping commands in from a file or pipe, this variable has no effect.</p>
<dt>&bull;</p>
<dd> <tt>$HOME</tt> </p>
<p> The user&#8217;s home directory</p>
<dt>&bull;</p>
<dd> <tt>$PERLDL::TERM</tt> </p>
<p> This is the Term::ReadLine object associated with the perldl shell. It can be used by routines called from perldl if your command is interactive.</p>
<dt>&bull;</p>
<dd> <tt>$PDL::toolongtoprint</tt> </p>
<p> The maximal size pdls to print (defaults to 10,000 elements). This is not just a <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt> variable but it is something that is usually needed in an interactive debugging session.</dl>
<h3>Executing scripts from the perldl prompt</h3>
<p> A useful idiom for developing perldl scripts or editing functions on-line is </p>
<pre>
  pdl&gt; # emacs script &amp;
    -- add perldl code to script and save the file
  
  pdl&gt; do 'script'
</pre>
<p> &#8212; substitute your favourite window-based editor for &#8217;emacs&#8217; (you may also need to change the &#8216;&amp;&#8217; on non-Unix systems). </p>
<p> Running &#8220;do &#8216;script&#8221;&#8217; again updates any variables and function definitions from the current version of &#8216;script&#8217;.</p>
<h3>Executing perldl scripts from the command line</h3>
<p> <font SIZE="-1">PDL</font> scripts are just perl scripts that happen to use <font SIZE="-1">PDL </font>(and possibly PDL::NiceSlice). But for the truly lazy, perldl can be invokes as a script interpreter. Because perldl is itself an interpreted perl script, most unices won&#8217;t allow you to say &#8220;#!/usr/bin/perldl&#8221; at the top of your script. </p>
<p> Instead, say &#8220;#!/usr/bin/pdl&#8221; and your script will be executed exactly as if you typed it, line-by-line, into the perldl shell.</p>
<h3>Command preprocessing</h3>
<p> <font SIZE="-1">NOTE:</font> This feature is used by default by PDL::NiceSlice. See below for more about slicing at the <tt>&quot;perldl&quot;</tt> prompt </p>
<p> In some cases, it is convenient to process commands before they are sent to perl for execution. For example, this is the case where the shell is being presented to people unfamiliar with perl but who wish to take advantage of commands added locally (eg by automatically quoting arguments to certain commands). </p>
<p> *<i></i><font SIZE="-1"><i>NOTE</i></font><i></i>*: The preprocessing interface has changed from earlier versions! The old way using <tt>$PERLDL::PREPROCESS</tt> will still work but is strongly deprecated and might go away in the future. </p>
<p> You can enable preprocessing by registering a filter with the <tt>&quot;preproc_add&quot;</tt> function. <tt>&quot;preproc_add&quot;</tt> takes one argument which is the filter to be installed. A filter is a Perl code reference (usually set in a local configuration file) that will be called, with the current command string as argument, just prior to the string being executed by the shell. The modified string should be returned. Note that you can make <tt>&quot;perldl&quot;</tt> completely unusable if you fail to return the modified string; quitting is then your only option. </p>
<p> Filters can be removed from the preprocessing pipeline by calling <tt>&quot;preproc_del&quot;</tt> with the filter to be removed as argument. To find out if a filter is currently installed in the preprocessing pipeline use <tt>&quot;preproc_registered&quot;</tt>: </p>
<pre>
  pdl&gt; preproc_add $myfilter unless preproc_registered $myfilter;
</pre>
<p> Previous versions of <tt>&quot;perldl&quot;</tt> used the variable <tt>$PERLDL::PREPROCESS</tt>. This will still work but should be avoided. Please change your scripts to use the <tt>&quot;preproc_add&quot;</tt> etc functions. </p>
<p> The following code would check for a call to function &#8216;mysub&#8217; and bracket arguments with qw. </p>
<p>$filter = preproc_add sub<br />
{<br />
    my $str = shift;<br />
    $str = ~s / ^\s + //;  # Strip leading space<br />
           if ($str = ~ / ^mysub /)<br />
    {<br />
        my($command, $arguments) = split(/\s + /, $str, 2);<br />
        $str = &#8220;$command qw( $arguments )&#8221; if (defined $arguments &amp;&amp; $arguments !~ / ^qw /);<br />
    };<br />
#Return the input string, modified as required<br />
    return $str;<br />
};</p>
<p> This would convert: </p>
<pre>
  pdl&gt; mysub arg1 arg2
</pre>
<p> to </p>
<pre>
  pdl&gt; mysub qw( arg1 arg2 )
</pre>
<p> which Perl will understand as a list. Obviously, a little more effort is required to check for cases where the caller has supplied a normal list (and so does not require automatic quoting) or variable interpolation is required. </p>
<p> You can remove this preprocessor using the <tt>&quot;preproc_del&quot;</tt> function which takes one argument (the filter to be removed, it must be the same coderef that was returned from a previous <tt>&quot;preproc_add&quot;</tt> call): </p>
<pre>
  pdl&gt; preproc_del $filter;
</pre>
<p> An example of actual usage can be found in the <tt>&quot;perldl&quot;</tt> script. Look at the function <tt>&quot;trans&quot;</tt> to see how the niceslicing preprocessor is enabled/disabled.</p>
<h3>perldl and PDL::NiceSlice</h3>
<p> PDL::NiceSlice introduces a more convenient slicing syntax for piddles. In current versions of <tt>&quot;perldl&quot;</tt> and <tt>&quot;pdl2&quot;</tt> niceslicing is enabled by default (if the required <font SIZE="-1">CPAN</font> modules are installed on your machine). </p>
<p> At startup <tt>&quot;perldl&quot;</tt> will let you know if niceslicing is enabled. The startup message will contain info to this end, something like this: </p>
<pre>
   perlDL shell v1.XX
    PDL comes with ABSOLUTELY NO WARRANTY. For details, see the file
    'COPYING' in the PDL distribution. This is free software and you
    are welcome to redistribute it under certain conditions, see
    the same file for details.
   ReadLines, NiceSlice  enabled
   Reading /home/csoelle/.perldlrc...
   Type 'demo' for online demos
   Loaded PDL v2.XX
</pre>
<p> When you get such a message that indicates <tt>&quot;NiceSlice&quot;</tt> is enabled you can use the enhanced slicing syntax: </p>
<pre>
  pdl&gt; $a = sequence 10;
  pdl&gt; p $a(3:8:2)
</pre>
<p> For details consult PDL::NiceSlice. </p>
<p> PDL::NiceSlice installs a filter in the preprocessing pipeline (see above) to enable the enhanced slicing syntax. You can use a few commands in the <tt>&quot;perldl&quot;</tt> shell to switch this preprocessing on or off and also explicitly check the substitutions that the NiceSlice filter makes. </p>
<p> You can switch the PDL::NiceSlice filter on and off by typing </p>
<pre>
  pdl&gt; trans # switch niceslicing on
</pre>
<p> and </p>
<pre>
  pdl&gt; notrans # switch niceslicing off
</pre>
<p> respectively. The filter is on by default. </p>
<p> To see how your commands are translated switch reporting on: </p>
<p>pdl &gt; report 1;<br />
pdl &gt; p $a(3 : 8 : 2)<br />
          processed p $a-&gt;nslice([ 3, 8, 2 ])<br />
              [3 5 7]</p>
<p> Similarly, switch reporting off as needed </p>
<pre>
  pdl&gt; report 0;
  pdl&gt;  p $a(3:8:2)
  [3 5 7]
</pre>
<p> Reporting is off by default.</p>
<h3>Automatically execute your own hooks</h3>
<p> The variable <tt>@PERLDL::AUTO</tt> is a simple list of perl code strings and/or code reference. It is used to define code to be executed automatically every time the user enters a new line. </p>
<p> A simple example would be to print the time of each command: </p>
<pre><code>
pdl &gt; push @PERLDL::AUTO, 'print scalar(gmtime),"
"'

                              pdl &gt; print zeroes(3, 3)
                                        Sun May 3 04 : 49 : 05 1998

                                            [
                                                [0 0 0]
                                                    [0 0 0]
                                                    [0 0 0]]

                              pdl
                              &gt; print "Boo" Sun May 3 04 : 49 : 18 1998 Boo
                              pdl
                              &gt;
</code></pre>
<p> Or to make sure any changes in the file &#8216;local.perldlrc&#8217; are always picked up :- </p>
<pre>
  pdl&gt; push @PERLDL::AUTO,&quot;do 'local.perldlrc'&quot;
</pre>
<p> This code can of course be put *in* &#8216;local.perldlrc&#8217;, but be careful :-) [Hint: add <tt>&quot;unless ($started++)&quot;</tt> to above to ensure it only gets done once!] </p>
<p> Another example application is as a hook for Autoloaders (e.g. PDL::AutoLoader) to add code too which allows them to automatically re-scan their files for changes. This is extremely convenient at the interactive command line. Since this hook is only in the shell it imposes no inefficiency on <font SIZE="-1">PDL</font> scripts. </p>
<p> Finally note this is a very powerful facility &#8211; which means it should be used with caution! </p>
<h2>Index</h2>
</dl>
