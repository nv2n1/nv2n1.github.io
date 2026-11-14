---
title: "getopt(1)"
name: "getopt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getopt/"
description: "getopt – parse command options (enhanced)"
---

<h2 class="name">NAME</h2>
<p> getopt &#8211; parse command options (enhanced) </p>
<h2>SYNOPSIS</h2>
<p> <code>getopt</code> <i>optstring</i> <i>parameters</i> <code>getopt</code> [options] [<code>&#8212;</code>] <i>optstring</i> <i>parameters</i> <code>getopt</code> [options] <code>-o</code>|<code>&#8211;options</code> <i>optstring</i> [options] [<code>&#8212;</code>] <i>parameters</i></p>
<h2>DESCRIPTION</h2>
<p> <code>getopt</code> is used to break up (<i>parse</i>) options in command lines for easy parsing by shell procedures, and to check for valid options. It uses the GNU <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3) routines to do this. </p>
<p> The parameters <code>getopt</code> is called with can be divided into two parts: options which modify the way <code>getopt</code> will do the parsing (the <i>options</i> and the <i>optstring</i> in the <code>SYNOPSIS</code>), and the parameters which are to be parsed (<i>parameters</i> in the <code>SYNOPSIS</code>). The second part will start at the first non-option parameter that is not an option argument, or after the first occurrence of &#8216;<code>&#8212;</code>&#8216;. If no &#8216;<code>-o</code>&#8216; or &#8216;<code>&#8211;options</code>&#8216; option is found in the first part, the first parameter of the second part is used as the short options string. </p>
<p> If the environment variable <code>GETOPT_COMPATIBLE</code> is set, or if the first <i>parameter</i> is not an option (does not start with a &#8216;<code>&#8211;</code>&#8216;, the first format in the <code>SYNOPSIS</code>), <code>getopt</code> will generate output that is compatible with that of other versions of <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1). It will still do parameter shuffling and recognize optional arguments (see section <code>COMPATIBILITY</code> for more information). </p>
<p> Traditional implementations of <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) are unable to cope with whitespace and other (shell-specific) special characters in arguments and non-option parameters. To solve this problem, this implementation can generate quoted output which must once again be interpreted by the shell (usually by using the <code>eval</code> command). This has the effect of preserving those characters, but you must call <code>getopt</code> in a way that is no longer compatible with other versions (the second or third format in the <code>SYNOPSIS</code>). To determine whether this enhanced version of <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) is installed, a special test option (<code>-T</code>) can be used.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;alternative</code></p>
<dl>
<dt>
<dd> Allow long options to start with a single &#8216;<code>&#8211;</code>&#8216;.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit. No other output is generated.</dl>
<p> <code>-l</code>, <code>&#8211;longoptions</code> <i>longopts</i></p>
<dl>
<dt>
<dd> The long (multi-character) options to be recognized. More than one option name may be specified at once, by separating the names with commas. This option may be given more than once, the <i>longopts</i> are cumulative. Each long option name in <i>longopts</i> may be followed by one colon to indicate it has a required argument, and by two colons to indicate it has an optional argument.</dl>
<p> <code>-n</code>, <code>&#8211;name</code> <i>progname</i></p>
<dl>
<dt>
<dd> The name that will be used by the <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3) routines when it reports errors. Note that errors of <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) are still reported as coming from getopt.</dl>
<p> <code>-o</code>, <code>&#8211;options</code> <i>shortopts</i></p>
<dl>
<dt>
<dd> The short (one-character) options to be recognized. If this option is not found, the first parameter of <code>getopt</code> that does not start with a &#8216;<code>&#8211;</code>&#8216; (and is not an option argument) is used as the short options string. Each short option character in <i>shortopts</i> may be followed by one colon to indicate it has a required argument, and by two colons to indicate it has an optional argument. The first character of shortopts may be &#8216;<code>+</code>&#8216; or &#8216;<code>&#8211;</code>&#8216; to influence the way options are parsed and output is generated (see section <code>SCANNING MODES</code> for details).</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Disable error reporting by <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3).</dl>
<p> <code>-Q</code>, <code>&#8211;quiet-output</code></p>
<dl>
<dt>
<dd> Do not generate normal output. Errors are still reported by <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3), unless you also use <code>-q</code>.</dl>
<p> <code>-s</code>, <code>&#8211;shell</code> <i>shell</i></p>
<dl>
<dt>
<dd> Set quoting conventions to those of <i>shell</i>. If the <code>-s</code> option is not given, the BASH conventions are used. Valid arguments are currently &#8216;<code>sh</code>&#8216; &#8216;<code>bash</code>&#8216;, &#8216;<code>csh</code>&#8216;, and &#8216;<code>tcsh</code>&#8216;.</dl>
<p> <code>-T</code>, <code>&#8211;test</code></p>
<dl>
<dt>
<dd> Test if your <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) is this enhanced version or an old version. This generates no output, and sets the error status to 4. Other implementations of <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1), and this version if the environment variable <code>GETOPT_COMPATIBLE</code> is set, will return &#8216;<code>&#8212;</code>&#8216; and error status 0.</dl>
<p> <code>-u</code>, <code>&#8211;unquoted</code></p>
<dl>
<dt>
<dd> Do not quote the output. Note that whitespace and special (shell-dependent) characters can cause havoc in this mode (like they do with other <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) implementations).</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit. No other output is generated.</dl>
<h2>PARSING</h2>
<p> This section specifies the format of the second part of the parameters of <code>getopt</code> (the <i>parameters</i> in the <code>SYNOPSIS</code>). The next section (<code>OUTPUT</code>) describes the output that is generated. These parameters were typically the parameters a shell function was called with. Care must be taken that each parameter the shell function was called with corresponds to exactly one parameter in the parameter list of <code>getopt</code> (see the <code>EXAMPLES</code>). All parsing is done by the GNU <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3) routines. </p>
<p> The parameters are parsed from left to right. Each parameter is classified as a short option, a long option, an argument to an option, or a non-option parameter. </p>
<p> A simple short option is a &#8216;<code>&#8211;</code>&#8216; followed by a short option character. If the option has a required argument, it may be written directly after the option character or as the next parameter (i.e., separated by whitespace on the command line). If the option has an optional argument, it must be written directly after the option character if present. </p>
<p> It is possible to specify several short options after one &#8216;<code>&#8211;</code>&#8216;, as long as all (except possibly the last) do not have required or optional arguments. </p>
<p> A long option normally begins with &#8216;<code>&#8212;</code>&#8216; followed by the long option name. If the option has a required argument, it may be written directly after the long option name, separated by &#8216;<code>=</code>&#8216;, or as the next argument (i.e., separated by whitespace on the command line). If the option has an optional argument, it must be written directly after the long option name, separated by &#8216;<code>=</code>&#8216;, if present (if you add the &#8216;<code>=</code>&#8216; but nothing behind it, it is interpreted as if no argument was present; this is a slight bug, see the <code>BUGS</code>). Long options may be abbreviated, as long as the abbreviation is not ambiguous. </p>
<p> Each parameter not starting with a &#8216;<code>&#8211;</code>&#8216;, and not a required argument of a previous option, is a non-option parameter. Each parameter after a &#8216;<code>&#8212;</code>&#8216; parameter is always interpreted as a non-option parameter. If the environment variable <code>POSIXLY_CORRECT</code> is set, or if the short option string started with a &#8216;<code>+</code>&#8216;, all remaining parameters are interpreted as non-option parameters as soon as the first non-option parameter is found.</p>
<h2>OUTPUT</h2>
<p> Output is generated for each element described in the previous section. Output is done in the same order as the elements are specified in the input, except for non-option parameters. Output can be done in <i>compatible</i> (<i>unquoted</i>) mode, or in such way that whitespace and other special characters within arguments and non-option parameters are preserved (see <code>QUOTING</code>). When the output is processed in the shell script, it will seem to be composed of distinct elements that can be processed one by one (by using the shift command in most shell languages). This is imperfect in unquoted mode, as elements can be split at unexpected places if they contain whitespace or special characters. </p>
<p> If there are problems parsing the parameters, for example because a required argument is not found or an option is not recognized, an error will be reported on stderr, there will be no output for the offending element, and a non-zero error status is returned. </p>
<p> For a short option, a single &#8216;<code>&#8211;</code>&#8216; and the option character are generated as one parameter. If the option has an argument, the next parameter will be the argument. If the option takes an optional argument, but none was found, the next parameter will be generated but be empty in quoting mode, but no second parameter will be generated in unquoted (compatible) mode. Note that many other <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) implementations do not support optional arguments. </p>
<p> If several short options were specified after a single &#8216;<code>&#8211;</code>&#8216;, each will be present in the output as a separate parameter. </p>
<p> For a long option, &#8216;<code>&#8212;</code>&#8216; and the full option name are generated as one parameter. This is done regardless whether the option was abbreviated or specified with a single &#8216;<code>&#8211;</code>&#8216; in the input. Arguments are handled as with short options. </p>
<p> Normally, no non-option parameters output is generated until all options and their arguments have been generated. Then &#8216;<code>&#8212;</code>&#8216; is generated as a single parameter, and after it the non-option parameters in the order they were found, each as a separate parameter. Only if the first character of the short options string was a &#8216;<code>&#8211;</code>&#8216;, non-option parameter output is generated at the place they are found in the input (this is not supported if the first format of the <code>SYNOPSIS</code> is used; in that case all preceding occurrences of &#8216;<code>&#8211;</code>&#8216; and &#8216;<code>+</code>&#8216; are ignored).</p>
<h2>QUOTING</h2>
<p> In compatibility mode, whitespace or &#8216;special&#8217; characters in arguments or non-option parameters are not handled correctly. As the output is fed to the shell script, the script does not know how it is supposed to break the output into separate parameters. To circumvent this problem, this implementation offers quoting. The idea is that output is generated with quotes around each parameter. When this output is once again fed to the shell (usually by a shell <code>eval</code> command), it is split correctly into separate parameters. </p>
<p> Quoting is not enabled if the environment variable <code>GETOPT_COMPATIBLE</code> is set, if the first form of the <code>SYNOPSIS</code> is used, or if the option &#8216;<code>-u</code>&#8216; is found. </p>
<p> Different shells use different quoting conventions. You can use the &#8216;<code>-s</code>&#8216; option to select the shell you are using. The following shells are currently supported: &#8216;<code>sh</code>&#8216;, &#8216;<code>bash</code>&#8216;, &#8216;<code>csh</code>&#8216; and &#8216;<code>tcsh</code>&#8216;. Actually, only two &#8216;flavors&#8217; are distinguished: sh-like quoting conventions and csh-like quoting conventions. Chances are that if you use another shell script language, one of these flavors can still be used.</p>
<h2>SCANNING MODES</h2>
<p> The first character of the short options string may be a &#8216;<code>&#8211;</code>&#8216; or a &#8216;<code>+</code>&#8216; to indicate a special scanning mode. If the first calling form in the <code>SYNOPSIS</code> is used they are ignored; the environment variable <code>POSIXLY_CORRECT</code> is still examined, though. </p>
<p> If the first character is &#8216;<code>+</code>&#8216;, or if the environment variable <code>POSIXLY_CORRECT</code> is set, parsing stops as soon as the first non-option parameter (i.e., a parameter that does not start with a &#8216;<code>&#8211;</code>&#8216;) is found that is not an option argument. The remaining parameters are all interpreted as non-option parameters. </p>
<p> If the first character is a &#8216;<code>&#8211;</code>&#8216;, non-option parameters are outputted at the place where they are found; in normal operation, they are all collected at the end of output after a &#8216;<code>&#8212;</code>&#8216; parameter has been generated. Note that this &#8216;<code>&#8212;</code>&#8216; parameter is still generated, but it will always be the last parameter in this mode.</p>
<h2>COMPATIBILITY</h2>
<p> This version of <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) is written to be as compatible as possible to other versions. Usually you can just replace them with this version without any modifications, and with some advantages. </p>
<p> If the first character of the first parameter of getopt is not a &#8216;<code>&#8211;</code>&#8216;, <code>getopt</code> goes into compatibility mode. It will interpret its first parameter as the string of short options, and all other arguments will be parsed. It will still do parameter shuffling (i.e., all non-option parameters are output at the end), unless the environment variable <code>POSIXLY_CORRECT</code> is set, in which case, <code>getopt</code> will prepend a &#8216;<code>+</code>&#8216; before short options automatically. </p>
<p> The environment variable <code>GETOPT_COMPATIBLE</code> forces <code>getopt</code> into compatibility mode. Setting both this environment variable and <code>POSIXLY_CORRECT</code> offers 100% compatibility for &#8216;difficult&#8217; programs. Usually, though, neither is needed. </p>
<p> In compatibility mode, leading &#8216;<code>&#8211;</code>&#8216; and &#8216;<code>+</code>&#8216; characters in the short options string are ignored.</p>
<h2>RETURN CODES</h2>
<p> <code>getopt</code> returns error code <code>0</code> for successful parsing, <code>1</code> if <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3) returns errors, <code>2</code> if it does not understand its own parameters, <code>3</code> if an internal error occurs like out-of-memory, and <code>4</code> if it is called with <code>-T</code>.</p>
<h2>EXAMPLES</h2>
<p> Example scripts for (ba)sh and (t)csh are provided with the <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) distribution, and are installed in <i>/usr/share/doc/util-linux/examples/</i> directory.</p>
<h2>ENVIRONMENT</h2>
<p> <code>POSIXLY_CORRECT</code></p>
<dl>
<dt>
<dd> This environment variable is examined by the <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3) routines. If it is set, parsing stops as soon as a parameter is found that is not an option or an option argument. All remaining parameters are also interpreted as non-option parameters, regardless whether they start with a &#8216;<code>&#8211;</code>&#8216;.</dl>
<p> <code>GETOPT_COMPATIBLE</code></p>
<dl>
<dt>
<dd> Forces <code>getopt</code> to use the first calling format as specified in the <code>SYNOPSIS</code>.</dl>
<h2>BUGS</h2>
<p> <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3) can parse long options with optional arguments that are given an empty optional argument (but cannot do this for short options). This <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) treats optional arguments that are empty as if they were not present. </p>
<p> The syntax if you do not want any short option variables at all is not very intuitive (you have to set them explicitly to the empty string).</p>
<h2>AUTHOR</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-tcsh/">tcsh</a></code>(1), <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>getopt</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
