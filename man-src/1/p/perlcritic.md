---
title: "perlcritic(1)"
name: "perlcritic"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlcritic/"
description: "\"perlcritic\" – Command-line interface to critique Perl source."
---

<h2 class="name">NAME</h2>
<p> &quot;perlcritic&quot; &#8211; Command-line interface to critique Perl source. </p>
<h2>SYNOPSIS</h2>
<pre><code>
perlcritic[-12345 | --brutal | --cruel | --harsh | --stern | --gentle]
          [--severity number | name][{-p | --profile} file | --noprofile]
          [--top[number]][--theme expression][--include pattern]
          [--exclude pattern][{-s | --single - policy} pattern]
          [--only | --noonly][--profile - strictness{warn | fatal | quiet}]
          [--force | --noforce][--statistics][--statistics - only]
          [--count | -C][--verbose{number | format}][--allow - unsafe]
          [--color | --nocolor][--pager pager][--quiet]
          [--color - severity - highest color_specification]
          [--color - severity - high color_specification]
          [--color - severity - medium color_specification]
          [--color - severity - low color_specification]
          [--color - severity - lowest color_specification]
          [--files - with - violations | -l]
          [--files - without - violations | -L]
          [--program - extensions file_name_extension]{FILE | DIRECTORY | STDIN} perlcritic-- profile -
    proto
        perlcritic{--list | --list - enabled | --list - themes | --doc pattern[...]} perlcritic
{
    --help | --options | --man | --version
}
</code></pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;perlcritic&quot;</tt> is a Perl source code analyzer. It is the executable front-end to the Perl::Critic engine, which attempts to identify awkward, hard to read, error-prone, or unconventional constructs in your code. Most of the rules are based on Damian Conway&#8217;s book <code>Perl Best Practices</code>. However, <tt>&quot;perlcritic&quot;</tt> is <code>not</code> limited to enforcing <font SIZE="-1">PBP,</font> and it will even support rules that contradict Conway. All rules can easily be configured or disabled to your liking. </p>
<p> This documentation only covers how to drive this command. For all other information, including how to persistently configure this command so that you don&#8217;t have to say so much on the command-line, see the documentation for Perl::Critic itself.</p>
<h2>USAGE EXAMPLES</h2>
<p> Before getting into all the gory details, here are some basic usage examples to help get you started. </p>
<p>#Report only most severe violations(severity = 5)<br />
perlcritic YourModule.pm<br />
#Same as above, but read input from STDIN<br />
            perlcritic<br />
#Recursively process all Perl files beneath directory<br />
                perlcritic /<br />
        some / directory<br />
#Report slightly less severe violations too(severity &gt;= 4)<br />
                   perlcritic &#8211;<br />
    4 YourModule.pm<br />
#Same as above, but using named severity level<br />
        perlcritic&#8211; stern YourModule.pm<br />
#Report all violations, regardless of severity(severity &gt;= 1)<br />
            perlcritic &#8211;<br />
    1 YourModule.pm<br />
#Same as above, but using named severity level<br />
            perlcritic&#8211; brutal YourModule.pm<br />
#Report only violations of things from &#8220;Perl Best Practices&#8221;<br />
                perlcritic&#8211; theme pbp YourModule.pm<br />
#Report top 20 most severe violations(severity &gt;= 1)<br />
                    perlcritic&#8211; top YourModule.pm<br />
#Report additional violations of Policies that match m / variables / xms<br />
                        perlcritic&#8211; include variables YourModule.pm<br />
#Use defaults from somewhere other than ~ /.perlcriticrc<br />
                            perlcriticrc&#8211; profile project /<br />
        specific / perlcriticrc YourModule.pm</p>
<h2>ARGUMENTS</h2>
<p> The arguments are paths to the files you wish to analyze. You may specify multiple files. If an argument is a directory, <tt>&quot;perlcritic&quot;</tt> will analyze all Perl files below the directory. If no arguments are specified, then input is read from <font SIZE="-1">STDIN.</font></p>
<h2>OPTIONS</h2>
<p> Option names can be abbreviated to uniqueness and can be stated with singe or double dashes, and option values can be separated from the option name by a space or &#8216;=&#8217; (as with Getopt::Long). Option names are also case-sensitive.</p>
<dl>
<dt>&quot;&#8211;profile FILE&quot; or &quot;-p FILE&quot;</p>
<dd> Directs <tt>&quot;perlcritic&quot;</tt> to use a profile named by <font SIZE="-1">FILE</font> rather than looking for the default <i>.perlcriticrc</i> file in the current directory or your home directory. See &#8220;<font SIZE="-1">CONFIGURATION&#8221;</font> in Perl::Critic for more information.</p>
<dt>&quot;&#8211;noprofile&quot;</p>
<dd> Directs <tt>&quot;perlcritic&quot;</tt> not to load any configuration file, thus reverting to the default configuration for all Policies.</p>
<dt>&quot;&#8211;severity N&quot;</p>
<dd> Directs <tt>&quot;perlcritic&quot;</tt> to only apply Policies with a severity greater than <tt>&quot;N&quot;</tt>. Severity values are integers ranging from 1 (least severe) to 5 (most severe). The default is 5. For a given <tt>&quot;--profile&quot;</tt>, decreasing the <tt>&quot;--severity&quot;</tt> will usually produce more violations. You can set the default value for this option in your <i>.perlcriticrc</i> file. You can also redefine the <tt>&quot;severity&quot;</tt> for any Policy in your <i>.perlcriticrc</i> file. See &#8220;<font SIZE="-1">CONFIGURATION&#8221;</font> for more information.</p>
<dt>&quot;-5 | -4 | -3 | -2 | -1&quot;</p>
<dd> These are numeric shortcuts for setting the <tt>&quot;--severity&quot;</tt> option. For example, <tt>&quot;-4&quot;</tt> is equivalent to <tt>&quot;--severity 4&quot;</tt>. If multiple shortcuts are specified, then the most restrictive one wins. If an explicit <tt>&quot;--severity&quot;</tt> option is also given, then all shortcut options are silently ignored. <font SIZE="-1">NOTE:</font> Be careful not to put one of the number severity shortcut options immediately after the <tt>&quot;--top&quot;</tt> flag or <tt>&quot;perlcritic&quot;</tt> will interpret it as the number of violations to report.</p>
<dt>&quot;&#8211;severity NAME&quot;</p>
<dd> If it is difficult for you to remember whether severity &#8220;5&#8221; is the most or least restrictive level, then you can use one of these named values: </p>
<p>SEVERITY NAME&#8230; is equivalent to&#8230; SEVERITY NUMBER&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;severity gentle&#8211; severity 5 &#8211;severity stern&#8211; severity 4 &#8211;severity harsh&#8211; severity 3 &#8211;severity cruel&#8211; severity 2 &#8211;severity brutal&#8211; severity 1</p>
<dt>&quot;&#8211;gentle | &#8211;stern | &#8211;harsh | &#8211;cruel | &#8211;brutal&quot;</p>
<dd> These are named shortcuts for setting the <tt>&quot;--severity&quot;</tt> option. For example, <tt>&quot;--cruel&quot;</tt> is equivalent to <tt>&quot;--severity 2&quot;</tt>. If multiple shortcuts are specified, then the most restrictive one wins. If an explicit <tt>&quot;--severity&quot;</tt> option is also given, then all shortcut options are silently ignored.</p>
<dt>&quot;&#8211;theme RULE&quot;</p>
<dd> Directs <tt>&quot;perlcritic&quot;</tt> to apply only Policies with themes that satisfy the <tt>&quot;RULE&quot;</tt>. Themes are arbitrary names for groups of related policies. You can combine theme names with boolean operators to create an arbitrarily complex <tt>&quot;RULE&quot;</tt>. For example, the following would apply only Policies that have a &#8216;bugs&#8217; <font SIZE="-1">AND </font>&#8216;pbp&#8217; theme: </p>
<pre>
    $&gt; perlcritic --theme='bugs &amp;&amp; pbp' MyModule.pm
</pre>
<p> Unless the <tt>&quot;--severity&quot;</tt> option is explicitly given, setting <tt>&quot;--theme&quot;</tt> silently causes the <tt>&quot;--severity&quot;</tt> to be set to 1. You can set the default value for this option in your <i>.perlcriticrc</i> file. See &#8220;<font SIZE="-1">POLICY THEMES&#8221;</font> in Perl::Critic for more information about themes.</p>
<dt>&quot;&#8211;include PATTERN&quot;</p>
<dd> Directs <tt>&quot;perlcritic&quot;</tt> to apply additional Policies that match the regex <tt>&quot;/PATTERN/imx&quot;</tt>. Use this option to temporarily override your profile and/or the severity settings at the command-line. For example: </p>
<pre>
    perlcritic --include=layout my_file.pl
</pre>
<p> This would cause <tt>&quot;perlcritic&quot;</tt> to apply all the <tt>&quot;CodeLayout::*&quot;</tt> policies even if they have a severity level that is less than the default level of 5, or have been disabled in your <i>.perlcriticrc</i> file. You can specify multiple <tt>&quot;--include&quot;</tt> options and you can use it in conjunction with the <tt>&quot;--exclude&quot;</tt> option. Note that <tt>&quot;--exclude&quot;</tt> takes precedence over <tt>&quot;--include&quot;</tt> when a Policy matches both patterns. You can set the default value for this option in your <i>.perlcriticrc</i> file.</p>
<dt>&quot;&#8211;exclude PATTERN&quot;</p>
<dd> Directs <tt>&quot;perlcritic&quot;</tt> to not apply any Policy that matches the regex <tt>&quot;/PATTERN/imx&quot;</tt>. Use this option to temporarily override your profile and/or the severity settings at the command-line. For example: </p>
<pre>
    perlcritic --exclude=strict my_file.pl
</pre>
<p> This would cause <tt>&quot;perlcritic&quot;</tt> to not apply the <tt>&quot;RequireUseStrict&quot;</tt> and <tt>&quot;ProhibitNoStrict&quot;</tt> Policies even though they have the highest severity level. You can specify multiple <tt>&quot;--exclude&quot;</tt> options and you can use it in conjunction with the <tt>&quot;--include&quot;</tt> option. Note that <tt>&quot;--exclude&quot;</tt> takes precedence over <tt>&quot;--include&quot;</tt> when a Policy matches both patterns. You can set the default value for this option in your <i>.perlcriticrc</i> file.</p>
<dt>&quot;&#8211;single-policy PATTERN&quot; or &quot;-s PATTERN&quot;</p>
<dd> Directs <tt>&quot;perlcritic&quot;</tt> to apply just one Policy module matching the regex <tt>&quot;/PATTERN/ixms&quot;</tt>, and exclude all other Policies. This option has precedence over the <tt>&quot;--severity&quot;</tt>, <tt>&quot;--theme&quot;</tt>, <tt>&quot;--include&quot;</tt>, <tt>&quot;--exclude&quot;</tt>, and <tt>&quot;--only&quot;</tt> options. For example: </p>
<pre>
    perlcritic --single-policy=nowarnings my_file.pl
</pre>
<p> This would cause <tt>&quot;perlcritic&quot;</tt> to apply just the <tt>&quot;ProhibitNoWarnings&quot;</tt> Policy, regardless of the severity level setting. No other Policies would be applied. </p>
<p> This is equivalent to what one might intend by&#8230; </p>
<pre>
    perlcritic --exclude=. --include=nowarnings my_file.pl
</pre>
<p> &#8230; but this won&#8217;t work because the <tt>&quot;--exclude&quot;</tt> option overrides the <tt>&quot;--include&quot;</tt> option. </p>
<p> The equivalent of this option can be accomplished by creating a custom profile containing only the desired policy and then running&#8230; </p>
<pre>
    perlcritic --profile=customprofile --only my_file.pl
</pre>
<dt>&quot;&#8211;top [ N ]&quot;</p>
<dd> Directs <tt>&quot;perlcritic&quot;</tt> to report only the top <tt>&quot;N&quot;</tt> Policy violations in each file, ranked by their severity. If <tt>&quot;N&quot;</tt> is not specified, it defaults to 20. If the <tt>&quot;--severity&quot;</tt> option (or one of the shortcuts) is not explicitly given, the <tt>&quot;--top&quot;</tt> option implies that the minimum severity level is &#8220;1&#8221; (i.e. &#8220;brutal&#8221;). Users can redefine the severity for any Policy in their <i>.perlcriticrc</i> file. See &#8220;<font SIZE="-1">CONFIGURATION&#8221;</font> for more information. You can set the default value for this option in your <i>.perlcriticrc</i> file. <font SIZE="-1">NOTE:</font> Be careful not to put one of the severity shortcut options immediately after the <tt>&quot;--top&quot;</tt> flag or <tt>&quot;perlcritic&quot;</tt> will interpret it as the number of violations to report.</p>
<dt>&quot;&#8211;force&quot;</p>
<dd> Directs <tt>&quot;perlcritic&quot;</tt> to ignore the magical <tt>&quot;## no critic&quot;</tt> annotations in the source code. See &#8220;<font SIZE="-1">BENDING THE RULES&#8221;</font> for more information. You can set the default value for this option in your <i>.perlcriticrc</i> file.</p>
<dt>&quot;&#8211;statistics&quot;</p>
<dd> Causes several statistics about the code being scanned and the violations found to be reported after any other output.</p>
<dt>&quot;&#8211;statistics-only&quot;</p>
<dd> Like the <tt>&quot;--statistics&quot;</tt> option, but suppresses normal output and only shows the statistics.</p>
<dt>&quot;&#8211;verbose N | FORMAT&quot;</p>
<dd> Sets the verbosity level or format for reporting violations. If given a number (<tt>&quot;N&quot;</tt>), <tt>&quot;perlcritic&quot;</tt> reports violations using one of the predefined formats described below. If given a string (<tt>&quot;FORMAT&quot;</tt>), it is interpreted to be an actual format specification. If the <tt>&quot;--verbose&quot;</tt> option is not specified, it defaults to either 4 or 5, depending on whether multiple files were given as arguments to <tt>&quot;perlcritic&quot;</tt>. You can set the default value for this option in your <i>.perlcriticrc</i> file. </p>
<p>Verbosity Format Specification&#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 &#8220;%f:%l:%c:%m
&#8221;,<br />
    2 &#8220;%f: (%l:%c) %m
&#8221;,<br />
    3 &#8220;%m at %f line %l
&#8221;,<br />
    4 &#8220;%m at line %l, column %c.  %e.  (Severity: %s)
&#8221;,<br />
    5 &#8220;%f: %m at line %l, column %c.  %e.  (Severity: %s)
&#8221;,<br />
    6 &#8220;%m at line %l, near &#8216;%r&#8217;.  (Severity: %s)
&#8221;,<br />
    7 &#8220;%f: %m at line %l near &#8216;%r&#8217;.  (Severity: %s)
&#8221;,<br />
    8 &#8220;[%p] %m at line %l, column %c.  (Severity: %s)
&#8221;,<br />
    9 &#8220;[%p] %m at line %l, near &#8216;%r&#8217;.  (Severity: %s)
&#8221;,<br />
    10 &#8220;%m at line %l, column %c.
  %p (Severity: %s)
%d
&#8221;,<br />
    11 &#8220;%m at line %l, near &#8216;%r&#8217;.
  %p (Severity: %s)
%d
&#8221;</p>
<p> Formats are a combination of literal and escape characters similar to the way <tt>&quot;sprintf&quot;</tt> works. See String::Format for a full explanation of the formatting capabilities. Valid escape characters are: </p>
<p>Escape Meaning&#8211; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; % c Column number where the violation occurred % d Full diagnostic discussion of the violation % e Explanation of violation or page numbers in PBP % F Just the name of the file where the violation occurred.% f Path to the file where the violation occurred.% l Line number where the violation occurred % m Brief description of the violation % P Full name of the Policy module that created the violation % p Name of the Policy without the Perl::Critic::Policy::prefix % r The string of source code that caused the violation % C The class of the PPI::Element that caused the violation % s The severity level of the violation</p>
<p> The purpose of these formats is to provide some compatibility with text editors that have an interface for parsing certain kinds of input. See &#8220;<font SIZE="-1">EDITOR INTEGRATION&#8221;</font> for more information about that.</p>
<dt>&quot;&#8211;list&quot;</p>
<dd> Displays a condensed listing of all the Perl::Critic::Policy modules that are found on this machine. This option lists <i>all</i> Policies, regardless of your <i>.perlcriticrc</i> or command line options. For each Policy, the name, default severity and default themes are shown.</p>
<dt>&quot;&#8211;list-enabled&quot;</p>
<dd> Displays a condensed listing of all the Perl::Critic::Policy modules that <i>would</i> be enforced, if you were actually going to critique a file with this command. This is useful when you&#8217;ve constructed a complicated command or modified your <i>.perlcriticrc</i> file and you want to see exactly which Policies are going to be enforced (or not enforced, as the case may be). For each Policy, the name, default severity and default themes are shown.</p>
<dt>&quot;&#8211;list-themes&quot;</p>
<dd> Displays a list of all the themes of the Perl::Critic::Policy modules that are found on this machine.</p>
<dt>&quot;&#8211;profile-proto&quot;</p>
<dd> Displays an expanded listing of all the Perl::Critic::Policy modules that are found on this machine. For each Policy, the name, default severity and default themes are shown, as well as the name of any additional parameters that the Policy supports. The format is suitable as a prototype for your <i>.perlcriticrc</i> file.</p>
<dt>&quot;&#8211;only&quot;</p>
<dd> Directs perlcritic to apply only Policies that are explicitly mentioned in your <i>.perlcriticrc</i> file. This is useful if you want to use just a small subset of Policies without having to disable all the others. You can set the default value for this option in your <i>.perlcriticrc</i> file.</p>
<dt>&quot;&#8211;profile-strictness {warn|fatal|quiet}&quot;</p>
<dd> Directs perlcritic how to treat certain recoverable problems found in a <i>.perlcriticrc</i> or file specified via the <tt>&quot;--profile&quot;</tt> option. Valid values are <tt>&quot;warn&quot;</tt> (the default), <tt>&quot;fatal&quot;</tt>, and <tt>&quot;quiet&quot;</tt>. For example, perlcritic normally only warns about profiles referring to non-existent Policies, but this option can make this situation fatal. You can set the default value for this option in your <i>.perlcriticrc</i> file.</p>
<dt>&quot;&#8211;count&quot;</p>
<dd>
<dt>&quot;-C&quot;</p>
<dd> Display only the number of violations for each file. Use this feature to get a quick handle on where a large pile of code might need the most attention.</p>
<dt>&quot;&#8211;Safari&quot;</p>
<dd> Report &#8220;Perl Best Practice&#8221; citations as section numbers from &lt;<a rel="nofollow" href="http://safari.oreilly.com">http://safari.oreilly.com</a>&gt; instead of page numbers from the actual book. <font SIZE="-1">NOTE:</font> This feature is not implemented yet.</p>
<dt>&quot;&#8211;color&quot;</p>
<dd> This option is on when outputting to a tty. When set, Severity 5 and 4 are colored red and yellow, respectively. Colorization only happens if Term::ANSIColor is installed and it only works on non-Windows environments. Negate this switch to disable color. You can set the default value for this option in your <i>.perlcriticrc</i> file. </p>
<p> Can also be specified as <tt>&quot;--colour&quot;</tt>.</p>
<dt>&quot;&#8211;pager PAGER_COMMAND_STRING&quot;</p>
<dd> If set, perlcritic will pipe it&#8217;s output to the given <font SIZE="-1">PAGER_COMMAND_STRING.</font> You can set the default value for this option in your <i>.perlcriticrc</i> file. </p>
<p> Setting a pager turns off color by default. You will have to turn color on explicitly. If you want color, you&#8217;ll probably also want to tell your pager to display raw characters. For <tt>&quot;less&quot;</tt> and <tt>&quot;more&quot;</tt>, use the -R switch.</p>
<dt>&quot;&#8211;color-severity-highest COLOR_SPECIFICATION&quot;</p>
<dd> Specifies the color to be used for highest severity violations, as a Term::ANSIColor color specification. Can also be specified as <tt>&quot;--colour-severity-highest&quot;</tt>, <tt>&quot;--color-severity-5&quot;</tt>, or <tt>&quot;--colour-severity-5&quot;</tt>.</p>
<dt>&quot;&#8211;color-severity-high COLOR_SPECIFICATION&quot;</p>
<dd> Specifies the color to be used for high severity violations, as a Term::ANSIColor color specification. Can also be specified as <tt>&quot;--colour-severity-high&quot;</tt>, <tt>&quot;--color-severity-4&quot;</tt>, or <tt>&quot;--colour-severity-4&quot;</tt>.</p>
<dt>&quot;&#8211;color-severity-medium COLOR_SPECIFICATION&quot;</p>
<dd> Specifies the color to be used for medium severity violations, as a Term::ANSIColor color specification. Can also be specified as <tt>&quot;--colour-severity-medium&quot;</tt>, <tt>&quot;--color-severity-3&quot;</tt>, or <tt>&quot;--colour-severity-3&quot;</tt>.</p>
<dt>&quot;&#8211;color-severity-low COLOR_SPECIFICATION&quot;</p>
<dd> Specifies the color to be used for low severity violations, as a Term::ANSIColor color specification. Can also be specified as <tt>&quot;--colour-severity-low&quot;</tt>, <tt>&quot;--color-severity-2&quot;</tt>, or <tt>&quot;--colour-severity-2&quot;</tt>.</p>
<dt>&quot;&#8211;color-severity-lowest COLOR_SPECIFICATION&quot;</p>
<dd> Specifies the color to be used for lowest severity violations, as a Term::ANSIColor color specification. Can also be specified as <tt>&quot;--colour-severity-lowest&quot;</tt>, <tt>&quot;--color-severity-1&quot;</tt>, or <tt>&quot;--colour-severity-1&quot;</tt>.</p>
<dt>&quot;&#8211;files-with-violations&quot;</p>
<dd> Display only the names of files with violations. Use this feature with &#8211;single-policy to find files that contain violations of a given policy. Can also be specified as <tt>&quot;--l&quot;</tt>.</p>
<dt>&quot;&#8211;files-without-violations&quot;</p>
<dd> Display only the names of files without violations. Use this feature with &#8211;single-policy to find files that do not contain violations of a given policy. Can also be specified as <tt>&quot;--L&quot;</tt>.</p>
<dt>&quot;&#8211;program-extensions file_name_extension&quot;</p>
<dd> Tell <tt>&quot;perlcritic&quot;</tt> to treat files whose names end in the given file name extension as programs, not as modules. If a leading &#8216;.&#8217; is desired it must be explicitly specified, e.g. </p>
<pre>
    --program-extensions .pl
</pre>
<p> The matching is case-sensitive, and the option may be specified as many times as desired, e.g. </p>
<pre>
    --program-extensions .pl --program-extensions .cgi
</pre>
<p> The above can also be done by quoting the file name extensions: </p>
<pre>
    --program-extensions '.pl .cgi'
</pre>
<p> Files whose name ends in &#8216;.PL&#8217; will always be considered programs.</p>
<dt>&quot;&#8211;doc PATTERN&quot;</p>
<dd> Displays the perldoc for all Perl::Critic::Policy modules that match <tt>&quot;m/PATTERN/ixms&quot;</tt>. Since Policy modules tend to have rather long names, this just provides a more convenient way to say something like: <tt>&quot;perldoc Perl::Critic::Policy::ValuesAndExpressions::RequireUpperCaseHeredocTerminator&quot;</tt> at the command prompt.</p>
<dt>&quot;&#8211;allow-unsafe&quot;</p>
<dd> This option directs <tt>&quot;perlcritic&quot;</tt> to allow the use of Policies that have been marked as &#8220;unsafe&#8221;. Unsafe Policies may result in risky operations by compiling and executing the code they analyze. All the Policies that ship in the core Perl::Critic distribution are safe. However, third-party Policies, such as those in the Perl::Critic::Dynamic distribution are not safe. Note that &#8220;safety&#8221; is honorary &#8212; if a Policy author marks a Policy as safe, it is not a guarantee that it won&#8217;t do nasty things. <code>If you don&#8217;t trust your Policies and the code you are analyzing, then do not use this switch</code>.</p>
<dt>&quot;&#8211;quiet&quot;</p>
<dd> Suppress the &#8220;source <font SIZE="-1">OK&#8221;</font> message when no violations are found.</p>
<dt>&quot;&#8211;help&quot;</p>
<dd>
<dt>&quot;-?&quot;</p>
<dd>
<dt>&quot;-H&quot;</p>
<dd> Displays a brief summary of options and exits.</p>
<dt>&quot;&#8211;options&quot;</p>
<dd> Displays the descriptions of the options and exits. While this output is long, it it nowhere near the length of the output of <tt>&quot;--man&quot;</tt>.</p>
<dt>&quot;&#8211;man&quot;</p>
<dd> Displays the complete <tt>&quot;perlcritic&quot;</tt> manual and exits.</p>
<dt>&quot;&#8211;version&quot;</p>
<dd>
<dt>&quot;-V&quot;</p>
<dd> Displays the version number of <tt>&quot;perlcritic&quot;</tt> and exits.</dl>
<h2>CONFIGURATION</h2>
<p> Most of the settings for Perl::Critic and each of the Policy modules can be controlled by a configuration file. The default configuration file is called <i>.perlcriticrc</i>. <tt>&quot;perlcritic&quot;</tt> will look for this file in the current directory first, and then in your home directory. Alternatively, you can set the <tt>&quot;PERLCRITIC&quot;</tt> environment variable to explicitly point to a different file in another location. If none of these files exist, and the <tt>&quot;--profile&quot;</tt> option is not given on the command-line, then all Policies will be loaded with their default configuration. </p>
<p> The format of the configuration file is a series of INI-style blocks that contain key-value pairs separated by &#8220;=&#8221;. Comments should start with &#8220;#&#8221; and can be placed on a separate line or after the name-value pairs if you desire. </p>
<p> Default settings for perlcritic itself can be set <code>before the first named block.</code> For example, putting any or all of these at the top of your <i>.perlcriticrc</i> file will set the default value for the corresponding command-line argument. </p>
<pre>
    severity  = 3                                     #Integer or named level
    only      = 1                                     #Zero or One
    force     = 0                                     #Zero or One
    verbose   = 4                                     #Integer or format spec
    top       = 50                                    #A positive integer
    theme     = (pbp + security) * bugs               #A theme expression
    include   = NamingConventions ClassHierarchies    #Space-delimited list
    exclude   = Variables  Modules::RequirePackage    #Space-delimited list
</pre>
<p> The remainder of the configuration file is a series of blocks like this: </p>
<pre>
    [Perl::Critic::Policy::Category::PolicyName]
    severity = 1
    set_themes = foo bar
    add_themes = baz
    arg1 = value1
    arg2 = value2
</pre>
<p> <tt>&quot;Perl::Critic::Policy::Category::PolicyName&quot;</tt> is the full name of a module that implements the policy. The Policy modules distributed with Perl::Critic have been grouped into categories according to the table of contents in Damian Conway&#8217;s book <code>Perl Best Practices</code>. For brevity, you can omit the <tt>'Perl::Critic::Policy'</tt> part of the module name. </p>
<p> <tt>&quot;severity&quot;</tt> is the level of importance you wish to assign to the Policy. All Policy modules are defined with a default severity value ranging from 1 (least severe) to 5 (most severe). However, you may disagree with the default severity and choose to give it a higher or lower severity, based on your own coding philosophy. You can set the <tt>&quot;severity&quot;</tt> to an integer from 1 to 5, or use one of the equivalent names: </p>
<p>SEVERITY NAME&#8230; is equivalent to&#8230; SEVERITY NUMBER&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;gentle 5 stern 4 harsh 3 cruel 2 brutal 1</p>
<p> <tt>&quot;set_themes&quot;</tt> sets the theme for the Policy and overrides its default theme. The argument is a string of one or more whitespace-delimited alphanumeric words. Themes are case-insensitive. See &#8220;<font SIZE="-1">POLICY THEMES&#8221;</font> for more information. </p>
<p> <tt>&quot;add_themes&quot;</tt> appends to the default themes for this Policy. The argument is a string of one or more whitespace-delimited words. Themes are case-insensitive. See &#8220;<font SIZE="-1">POLICY THEMES&#8221;</font> for more information. </p>
<p> The remaining key-value pairs are configuration parameters that will be passed into the constructor of that Policy. The constructors for most Policy modules do not support arguments, and those that do should have reasonable defaults. See the documentation on the appropriate Policy module for more details. </p>
<p> Instead of redefining the severity for a given Policy, you can completely disable a Policy by prepending a &#8216;-&#8216; to the name of the module in your configuration file. In this manner, the Policy will never be loaded, regardless of the <tt>&quot;--severity&quot;</tt> given on the command line. </p>
<p> A simple configuration might look like this: </p>
<p>#&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;<br />
#I think these are really important, so always load them<br />
[TestingAndDebugging::RequireUseStrict] severity = 5<br />
    [TestingAndDebugging::RequireUseWarnings] severity = 5<br />
#&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;<br />
#I think these are less important, so only load when asked<br />
        [Variables::ProhibitPackageVars] severity = 2<br />
            [ControlStructures::ProhibitPostfixControls] allow = if unless #My custom configuration<br />
                severity = cruel #Same as &#8220;severity = 2&#8221;<br />
#&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;<br />
#Give these policies a custom theme.I can activate just<br />
#these policies by saying &#8220;perlcritic &#8211;theme &#8216;larry || curly'&#8221;<br />
                    [Modules::RequireFilenameMatchesPackage] add_themes = larry<br />
                        [TestingAndDebugging::RequireTestLabels] add_themes = curly moe<br />
#&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;<br />
#I do not agree with these at all, so never load them<br />
                            [-NamingConventions::Capitalization]<br />
                            [-ValuesAndExpressions::ProhibitMagicNumbers]<br />
#&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;<br />
#For all other Policies, I accept the default severity,<br />
#so no additional configuration is required for them.</p>
<p> Note that all policies included with the Perl::Critic distribution that have integer parameters accept underscores (&#8220;_&#8221;) in their values, as with Perl numeric literals. For example, </p>
<pre>
    [ValuesAndExpressions::RequireNumberSeparators]
    min_value = 1_000
</pre>
<p> For additional configuration examples, see the <i>perlcriticrc</i> file that is included in this <i>examples</i> directory of this distribution. </p>
<p> Damian Conway&#8217;s own Perl::Critic configuration is also included in this distribution as <i>examples/perlcriticrc-conway</i>.</p>
<h2>THE POLICIES</h2>
<p> A large number of Policy modules are distributed with Perl::Critic. They are described briefly in the companion document Perl::Critic::PolicySummary and in more detail in the individual modules themselves. Say <tt>&quot;perlcritic --doc PATTERN&quot;</tt> to see the perldoc for all Policy modules that match the regex <tt>&quot;m/PATTERN/ixms&quot;</tt> </p>
<p> There are a number of distributions of additional policies on <font SIZE="-1">CPAN.</font> If Perl::Critic doesn&#8217;t contain a policy that you want, some one may have already written it. See &#8220;<font SIZE="-1">SEE ALSO&#8221;</font> in Perl::Critic for a list of some of these distributions.</p>
<h2>POLICY THEMES</h2>
<p> Each Policy is defined with one or more &#8220;themes&#8221;. Themes can be used to create arbitrary groups of Policies. They are intended to provide an alternative mechanism for selecting your preferred set of Policies. For example, you may wish disable a certain set of Policies when analyzing test programs. Conversely, you may wish to enable only a specific subset of Policies when analyzing modules. </p>
<p> The Policies that ship with Perl::Critic are have been divided into the following themes. This is just our attempt to provide some basic logical groupings. You are free to invent new themes that suit your needs. </p>
<p>THEME DESCRIPTION&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;core All policies that ship with Perl::Critic<br />
        pbp Policies that come directly from &#8220;Perl Best Practices&#8221; bugs Policies that that prevent or<br />
    reveal bugs<br />
            maintenance Policies that affect the long &#8211;<br />
        term health of the code<br />
            cosmetic Policies that only have a superficial effect<br />
                complexity Policies that specificaly relate to code complexity<br />
                    security Policies that relate to security issues<br />
                        tests Policies that are specific to test programs</p>
<p> Say <tt>&quot;perlcritic --list&quot;</tt> to get a listing of all available policies and the themes that are associated with each one. You can also change the theme for any Policy in your <i>.perlcriticrc</i> file. See the &#8220;<font SIZE="-1">CONFIGURATION&#8221;</font> section for more information about that. </p>
<p> Using the <tt>&quot;--theme&quot;</tt> command-line option, you can create an arbitrarily complex rule that determines which Policies to apply. Precedence is the same as regular Perl code, and you can use parentheses to enforce precedence as well. Supported operators are: </p>
<p>Operator Altertative Example&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -&amp;&amp;and&#8217;pbp &amp;&amp; core&#8217; || or &#8216;pbp || (bugs &amp;&amp; security)&#8217; !not &#8216;pbp &amp;&amp; ! (portability || complexity)&#8217;</p>
<p> Theme names are case-insensitive. If the <tt>&quot;--theme&quot;</tt> is set to an empty string, then it evaluates as true all Policies.</p>
<h2>BENDING THE RULES</h2>
<p> Perl::Critic takes a hard-line approach to your code: either you comply or you don&#8217;t. In the real world, it is not always practical (or even possible) to fully comply with coding standards. In such cases, it is wise to show that you are knowingly violating the standards and that you have a Damn Good Reason (<font SIZE="-1">DGR</font>) for doing so. </p>
<p> To help with those situations, you can direct Perl::Critic to ignore certain lines or blocks of code by using annotations: </p>
<p>require &#8216;LegacyLibaray1.pl&#8217;;<br />
##no critic<br />
    require &#8216;LegacyLibrary2.pl&#8217;;  ## no critic<br />
  for my $element (@list)<br />
{<br />
    ##no critic<br />
        $foo = &#8220;&#8221;;<br />
#Violates &#8216;ProhibitEmptyQuotes&#8217; $barf = bar() if $foo;<br />
#Violates &#8216;ProhibitPostfixControls&#8217;<br />
#Some more evil code&#8230;<br />
        ##use critic<br />
#Some good code&#8230;<br />
            do_something($_);<br />
}</p>
<p> The <tt>&quot;## no critic&quot;</tt> annotations direct Perl::Critic to ignore the remaining lines of code until a <tt>&quot;## use critic&quot;</tt> annotation is found. If the <tt>&quot;## no critic&quot;</tt> annotation is on the same line as a code statement, then only that line of code is overlooked. To direct perlcritic to ignore the <tt>&quot;## no critic&quot;</tt> annotations, use the <tt>&quot;--force&quot;</tt> option. </p>
<p> A bare <tt>&quot;## no critic&quot;</tt> annotation disables all the active Policies. If you wish to disable only specific Policies, add a list of Policy names as arguments just as you would for the <tt>&quot;no strict&quot;</tt> or <tt>&quot;no warnings&quot;</tt> pragma. For example, this would disable the <tt>&quot;ProhibitEmptyQuotes&quot;</tt> and <tt>&quot;ProhibitPostfixControls&quot;</tt> policies until the end of the block or until the next <tt>&quot;## use critic&quot;</tt> annotation (whichever comes first): </p>
<pre><code>
##no critic(EmptyQuotes, PostfixControls);
#Now exempt from ValuesAndExpressions::ProhibitEmptyQuotes
$foo = "";
#Now exempt ControlStructures::ProhibitPostfixControls
$barf = bar() if $foo;
#Still subject to ValuesAndExpression::RequireNumberSeparators
$long_int = 10000000000;
</code></pre>
<p> Since the Policy names are matched against the <tt>&quot;## no critic&quot;</tt> arguments as regular expressions, you can abbreviate the Policy names or disable an entire family of Policies in one shot like this: </p>
<pre>
    ## no critic (NamingConventions)
    # Now exempt from NamingConventions::Capitalization
    my $camelHumpVar = 'foo';
    # Now exempt from NamingConventions::Capitalization
    sub camelHumpSub {}
</pre>
<p> The argument list must be enclosed in parentheses and must contain one or more comma-separated barewords (i.e. don&#8217;t use quotes). The <tt>&quot;## no critic&quot;</tt> annotations can be nested, and Policies named by an inner annotation will be disabled along with those already disabled an outer annotation. </p>
<p> Some Policies like <tt>&quot;Subroutines::ProhibitExcessComplexity&quot;</tt> apply to an entire block of code. In those cases, <tt>&quot;## no critic&quot;</tt> must appear on the line where the violation is reported. For example: </p>
<pre>
    sub complicated_function {  ## no critic (ProhibitExcessComplexity)
        # Your code here...
    }
</pre>
<p> Some Policies like <tt>&quot;Documentation::RequirePodSections&quot;</tt> apply to the entire document, in which case violations are reported at line 1. But if the file requires a shebang line, it is impossible to put <tt>&quot;## no critic&quot;</tt> on the first line of the file. This is a known limitation and it will be addressed in a future release. As a workaround, you can disable the affected policies at the command-line or in your <i>.perlcriticrc</i> file. But beware that this will affect the analysis of <code>all</code> files. </p>
<p> Use this feature wisely. <tt>&quot;## no critic&quot;</tt> should be used in the smallest possible scope, or only on individual lines of code. And you should always be as specific as possible about which policies you want to disable (i.e. never use a bare <tt>&quot;## no critic&quot;</tt>). If Perl::Critic complains about your code, try and find a compliant solution before resorting to this feature.</p>
<h2>EDITOR INTEGRATION</h2>
<p> For ease-of-use, <tt>&quot;perlcritic&quot;</tt> can be integrated with your favorite text editor. The output-formatting capabilities of <tt>&quot;perlcritic&quot;</tt> are specifically intended for use with the &#8220;grep&#8221; or &#8220;compile&#8221; modes available in editors like <tt>&quot;emacs&quot;</tt> and <tt>&quot;vim&quot;</tt>. In these modes, you can run an arbitrary command and the editor will parse the output into an interactive buffer that you can click on and jump to the relevant line of code. </p>
<p> The Perl::Critic team thanks everyone who has helped integrate Perl-Critic with their favorite editor. Your contributions in particular have made Perl-Critic a convenient and user-friendly tool for Perl developers of all stripes. We sincerely appreciate your hard work.</p>
<h3><font SIZE="-1">EMACS</font></h3>
<p> Joshua ben Jore has authored a minor-mode for emacs that allows you to run perlcritic on the current region or buffer. You can run it on demand, or configure it to run automatically when you save the buffer. The output appears in a hot-linked compiler buffer. The code and installation instructions can be found in the <i>extras</i> directory inside this distribution.</p>
<h3><font SIZE="-1">VIM</font></h3>
<p> Scott Peshak has published <i>perlchecker.vim</i>, which is available at &lt;<a rel="nofollow" href="http://www.vim.org/scripts/script.php?script_id=1731">http://www.vim.org/scripts/script.php?script_id=1731</a>&gt;.</p>
<h3>gVIM</h3>
<p> Fritz Mehner recently added support for <tt>&quot;perlcritic&quot;</tt> to his fantastic gVIM plugin. In addition to providing a very Perlish <font SIZE="-1">IDE,</font> Fritz&#8217;s plugin enables one-click access to <tt>&quot;perlcritic&quot;</tt> and many other very useful utilities. And all is seamlessly integrated into the editor. See &lt;<a rel="nofollow" href="http://lug.fh-swf.de/vim/vim-perl/screenshots-en.html">http://lug.fh-swf.de/vim/vim-perl/screenshots-en.html</a>&gt; for complete details.</p>
<h3><font SIZE="-1">EPIC</font></h3>
<p> <font SIZE="-1">EPIC</font> is an open source Perl <font SIZE="-1">IDE</font> based on the Eclipse platform. Features include syntax highlighting, on-the-fly syntax check, content assist, code completion, perldoc support, source formatting with Perl::Tidy, code templates, a regular expression editing tool, and integration with the Perl debugger. Recent versions of <font SIZE="-1">EPIC</font> also have built-in support for Perl::Critic. At least one Perl::Critic contributor swears by <font SIZE="-1">EPIC. </font> Go to &lt;<a rel="nofollow" href="http://e-p-i-c.sourceforge.net">http://e-p-i-c.sourceforge.net</a>&gt; for more information about <font SIZE="-1">EPIC.</font></p>
<h3>BBEdit</h3>
<p> Josh Clark has produced an excellent Perl-Critic plugin for BBEdit. See &lt;<a rel="nofollow" href="http://globalmoxie.com/projects/bbedit-perl-critic/index.shtml">http://globalmoxie.com/projects/bbedit-perl-critic/index.shtml</a>&gt; for download, installation, and usage instructions. Apple users rejoice!</p>
<h3>Komodo</h3>
<p> Komodo is a proprietary <font SIZE="-1">IDE</font> for Perl and several other dynamic languages. Starting in version 5.1.1, Komodo has built-in support for Perl-Critic, if you have the Perl::Critic and criticism modules installed. Free trial copies of Komodo can be obtained from the ActiveState website at &lt;<a rel="nofollow" href="http://www.activestate.com">http://www.activestate.com</a>&gt;.</p>
<h3>ActivePerl</h3>
<p> ActivePerl includes a very slick graphical interface for configuring and running Perl-Critic called <tt>&quot;perlcritic-gui&quot;</tt>. A free community edition of ActivePerl can be obtained from the ActiveState website at &lt;<a rel="nofollow" href="http://www.activestate.com">http://www.activestate.com</a>&gt;.</p>
<h2>EXIT STATUS</h2>
<p> If <tt>&quot;perlcritic&quot;</tt> has any errors itself, exits with status == 1. If there are no errors, but <tt>&quot;perlcritic&quot;</tt> finds Policy violations in your source code, exits with status == 2. If there were no errors and no violations were found, exits with status == 0.</p>
<h2>THE Perl::Critic PHILOSOPHY</h2>
<dl>
<dt>
<dd> Coding standards are deeply personal and highly subjective. The goal of Perl::Critic is to help you write code that conforms with a set of best practices. Our primary goal is not to dictate what those practices are, but rather, to implement the practices discovered by others. Ultimately, you make the rules &#8212; Perl::Critic is merely a tool for encouraging consistency. If there is a policy that you think is important or that we have overlooked, we would be very grateful for contributions, or you can simply load your own private set of policies into Perl::Critic.</dl>
<h2>EXTENDING THE CRITIC</h2>
<p> The modular design of Perl::Critic is intended to facilitate the addition of new Policies. You&#8217;ll need to have some understanding of <font SIZE="-1">PPI</font>, but most Policy modules are pretty straightforward and only require about 20 lines of code, and half of those lines are simple use statements and simple declarations.. Please see the Perl::Critic::DEVELOPER file included in this distribution for a step-by-step demonstration of how to create new Policy modules. </p>
<p> If you develop any new Policy modules, feel free to send them to <tt>&quot;&lt;jeff [at] imaginative-software.com&gt;&quot;</tt> and I&#8217;ll be happy to put them into the Perl::Critic distribution. Or if you would like to work on the Perl::Critic project directly, check out our repository at &lt;<a rel="nofollow" href="http://perlcritic.tigris.org">http://perlcritic.tigris.org</a>&gt;. To subscribe to our mailing list, send a message to &lt;mailto:dev-subscribe [at] perlcritic.tigris.org&gt;. </p>
<p> The Perl::Critic team is also available for hire. If your organization has its own coding standards, we can create custom Policies to enforce your local guidelines. Or if your code base is prone to a particular defect pattern, we can design Policies that will help you catch those costly defects <code>before</code> they go into production. To discuss your needs with the Perl::Critic team, just contact <tt>&quot;&lt;jeff [at] imaginative-software.com&gt;&quot;</tt>.</p>
<h2>CONTACTING THE DEVELOPMENT TEAM</h2>
<p> You are encouraged to subscribe to the mailing list; send a message to &lt;mailto:users-subscribe [at] perlcritic.tigris.org&gt;. See also the archives at &lt;<a rel="nofollow" href="http://perlcritic.tigris.org/servlets/SummarizeList?listName=users">http://perlcritic.tigris.org/servlets/SummarizeList?listName=users</a>&gt;. You can also contact the author at <tt>&quot;&lt;jeff [at] imaginative-software.com&gt;&quot;</tt>. </p>
<p> At least one member of the development team has started hanging around in &lt;<a href="irc://irc.perl.org/#perlcritic">irc://irc.perl.org/#perlcritic</a>&gt;. </p>
<p> You can also follow Perl::Critic on Twitter, at &lt;<a rel="nofollow" href="https://twitter.com/perlcritic">https://twitter.com/perlcritic</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> There are a number of distributions of additional Policies available. A few are listed here: </p>
<p> Perl::Critic::More Perl::Critic::Bangs Perl::Critic::Lax Perl::Critic::StricterSubs Perl::Critic::Swift </p>
<p> These distributions enable you to use Perl::Critic in your unit tests: </p>
<p> Test::Perl::Critic Test::Perl::Critic::Progressive </p>
<p> There is also a distribution that will install all the Perl::Critic related modules known to the development team: </p>
<p> Task::Perl::Critic </p>
<p> Also, ActivePerl includes a very slick graphical interface to Perl-Critic called <tt>&quot;perlcritic-gui&quot;</tt>. You can get a free community edition of ActivePerl from &lt;<a rel="nofollow" href="http://www.activestate.com">http://www.activestate.com</a>&gt;.</p>
<h2>BUGS</h2>
<p> Scrutinizing Perl code is hard for humans, let alone machines. If you find any bugs, particularly false-positives or false-negatives from a Perl::Critic::Policy, please submit them to &lt;<a rel="nofollow" href="http://rt.cpan.org/NoAuth/Bugs.html?Dist=Perl-Critic">http://rt.cpan.org/NoAuth/Bugs.html?Dist=Perl-Critic</a>&gt;. Thanks. </p>
<p> Most policies will produce false-negatives if they cannot understand a particular block of code.</p>
<h2>CREDITS</h2>
<p> Adam Kennedy &#8211; For creating <font SIZE="-1">PPI</font>, the heart and soul of Perl::Critic. </p>
<p> Damian Conway &#8211; For writing <code>Perl Best Practices</code>, finally :) </p>
<p> Chris Dolan &#8211; For contributing the best features and Policy modules. </p>
<p> Andy Lester &#8211; Wise sage and master of all-things-testing. </p>
<p> Elliot Shank &#8211; The self-proclaimed quality freak. </p>
<p> Giuseppe Maxia &#8211; For all the great ideas and positive encouragement. </p>
<p> and Sharon, my wife &#8211; For putting up with my all-night code sessions.</p>
<h2>AUTHOR</h2>
<p> Jeffrey Ryan Thalhammer &lt;jeff [at] imaginative-software.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2005-2011 Imaginative Software Systems. All rights reserved. </p>
<p> This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. The full text of this license can be found in the <font SIZE="-1">LICENSE</font> file included with this module. </p>
<h2>Index</h2>
<dt><a href="#lbAT">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAU">THE Perl::Critic PHILOSOPHY</a></p>
<dd>
<dt><a href="#lbAV">EXTENDING THE CRITIC</a></p>
<dd>
<dt><a href="#lbAW">CONTACTING THE DEVELOPMENT TEAM</a></p>
<dd>
<dt><a href="#lbAX">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAY">BUGS</a></p>
<dd>
<dt><a href="#lbAZ">CREDITS</a></p>
<dd>
<dt><a href="#lbBA">AUTHOR</a></p>
<dd>
<dt><a href="#lbBB">COPYRIGHT</a></p>
<dd></dl>
