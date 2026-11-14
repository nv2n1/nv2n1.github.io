---
title: "shellcheck(1)"
name: "shellcheck"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shellcheck/"
---

<h2 class="name">NAME</h2>
 

 

 shellcheck - Shell script analysis tool 

<h2>SYNOPSIS</h2>

 

 shellcheck [OPTIONS...] FILES...

<h2>DESCRIPTION</h2>

 

 ShellCheck is a static analysis and linting tool for sh/bash scripts. It's mainly focused on handling typical beginner and intermediate level syntax errors and pitfalls where the shell just gives a cryptic error message or strange behavior, but it also reports on a few more advanced issues where corner cases can cause delayed failures. 

 ShellCheck gives shell specific advice. Consider this line:
<dl>
<dt>
<dd> <pre>
(( area = 3.14*r*r ))
</pre>
<dt>&bull;
<dd> For scripts starting with #!/bin/sh (or when using -s sh), ShellCheck will warn that (( .. )) is not POSIX compliant (similar to checkbashisms).
<dt>&bull;
<dd> For scripts starting with #!/bin/bash (or using -s bash), ShellCheck will warn that decimals are not supported.
<dt>&bull;
<dd> For scripts starting with #!/bin/ksh (or using -s ksh), ShellCheck will not warn at all, as ksh supports decimals in arithmetic contexts.</dl>

<h2>OPTIONS</h2>

<dl>
<dt>-a, -check-sourced
<dd> Emit warnings in sourced files. Normally, shellcheck will only warn about issues in the specified files. With this option, any issues in sourced files will also be reported.
<dt>-C[WHEN], -color[=WHEN]
<dd> For TTY output, enable colors always, never or auto. The default is auto. -color without an argument is equivalent to -color=always.
<dt>-i CODE1[,CODE2...], -include=CODE1[,CODE2...]
<dd> Explicitly include only the specified codes in the report. Subsequent -i options are cumulative, but all the codes can be specified at once, comma-separated as a single argument. Include options override any provided exclude options.
<dt>-e CODE1[,CODE2...], -exclude=CODE1[,CODE2...]
<dd> Explicitly exclude the specified codes from the report. Subsequent -e options are cumulative, but all the codes can be specified at once, comma-separated as a single argument.
<dt>-f FORMAT, -format=FORMAT
<dd> Specify the output format of shellcheck, which prints its results in the standard output. Subsequent -f options are ignored, see FORMATS below for more information.
<dt>-list-optional
<dd> Output a list of known optional checks. These can be enabled with -o flags or enable directives.
<dt>-norc
<dd> Don't try to look for .shellcheckrc configuration files.
<dt>-o NAME1[,NAME2...], -enable=NAME1[,NAME2...]
<dd> Enable optional checks. The special name all enables all of them. Subsequent -o options accumulate. This is equivalent to specifying enable directives.
<dt>-P SOURCEPATH, -source-path=SOURCEPATH
<dd> Specify paths to search for sourced files, separated by : on Unix and ; on Windows. This is equivalent to specifying search-path directives.
<dt>-s shell, -shell=shell
<dd> Specify Bourne shell dialect. Valid values are sh, bash, dash and ksh. The default is to deduce the shell from the file's shell directive, shebang, or .bash/.bats/.dash/.ksh extension, in that order. sh refers to POSIX sh (not the system's), and will warn of portability issues.
<dt>-S SEVERITY, -severity=severity
<dd> Specify minimum severity of errors to consider. Valid values in order of severity are error, warning, info and style. The default is style.
<dt>-V, -version
<dd> Print version information and exit.
<dt>-W NUM, -wiki-link-count=NUM
<dd> For TTY output, show NUM wiki links to more information about mentioned warnings. Set to 0 to disable them entirely.
<dt>-x, -external-sources
<dd> Follow `source' statements even when the file is not specified as input. By default, shellcheck will only follow files specified on the command line (plus /dev/null). This option allows following any file the script may source.
<dt>FILES...
<dd> One or more script files to check, or "-" for standard input.</dl>

<h2>FORMATS</h2>

<dl>
<dt>tty
<dd> Plain text, human readable output. This is the default.
<dt>gcc
<dd> GCC compatible output. Useful for editors that support compiling and showing syntax errors.
<dl>
<dt>
<dd> 

 For example, in Vim, :set makeprg=shellcheck\ -f\ gcc\ % will allow using :make to check the script, and :cnext to jump to the next error.
<dl>
<dt>
<dd> <pre>
&lt;file&gt;:&lt;line&gt;:&lt;column&gt;: &lt;type&gt;: &lt;message&gt;
</pre></dl>
</dl>

<dt>checkstyle
<dd> Checkstyle compatible XML output. Supported directly or through plugins by many IDEs and build monitoring systems.
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
&lt;checkstyle version='4.3'&gt;
  &lt;file name='file'&gt;
    &lt;error
      line='line'
      column='column'
      severity='severity'
      message='message'
      source='ShellCheck.SC####' /&gt;
    ...
  &lt;/file&gt;
  ...
&lt;/checkstyle&gt;
</pre></dl>
</dl>

<dt>diff
<dd> Auto-fixes in unified diff format. Can be piped to git apply or patch -p1 to automatically apply fixes.
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre><code>
--- a/test.sh
+++ b/test.sh
@@ -2,6 +2,6 @@
 ## Example of a broken script.
 for f in $(ls *.m3u)
 do
-  grep -qi hq.*mp3 $f \
+  grep -qi hq.*mp3 "$f" \
     &amp;&amp; echo -e 'Playlist $f contains a HQ file in mp3 format'
 done
</code></pre></dl>
</dl>

<dt>json1
<dd> Json is a popular serialization format that is more suitable for web applications. ShellCheck's json is compact and contains only the bare minimum. Tabs are counted as 1 character.
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
{
comments:
    [{
        "file" : "filename",
        "line" : lineNumber,
        "column" : columnNumber,
        "level" : "severitylevel",
        "code" : errorCode,
        "message" : "warning message"
    },
     ...]
}
</dl>
</dl>

<dt>json
<dd> This is a legacy version of the json1 format. It's a raw array of comments, and all offsets have a tab stop of 8.
<dt>quiet
<dd> Suppress all normal output. Exit with zero if no issues are found, otherwise exit with one. Stops processing after the first issue.</dl>

<h2>DIRECTIVES</h2>

 

 ShellCheck directives can be specified as comments in the shell script. If they appear before the first command, they are considered file-wide. Otherwise, they apply to the immediately following command or block:
<dl>
<dt>
<dd> <pre>
# shellcheck key=value key=value
command-or-structure
</pre></dl>
 

 For example, to suppress SC2035 about using ./*.jpg:
<dl>
<dt>
<dd> <pre>
# shellcheck disable=SC2035
echo &quot;Files: &quot; *.jpg
</pre></dl>
 

 To tell ShellCheck where to look for an otherwise dynamically determined file:
<dl>
<dt>
<dd> <pre>
# shellcheck source=./lib.sh
source &quot;$(find_install_dir)/lib.sh&quot;
</pre></dl>
 

 Here a shell brace group is used to suppress a warning on multiple lines:
<dl>
<dt>
<dd> <pre>
# shellcheck disable=SC2016
{
  echo 'Modifying $PATH'
  echo 'PATH=foo:$PATH' &gt;&gt; ~/.bashrc
}
</pre></dl>
 

 Valid keys are:
<dl>
<dt>disable
<dd> Disables a comma separated list of error codes for the following command. The command can be a simple command like echo foo, or a compound command like a function definition, subshell block or loop.
<dt>enable
<dd> Enable an optional check by name, as listed with -list-optional. Only file-wide enable directives are considered.
<dt>source
<dd> Overrides the filename included by a source/. statement. This can be used to tell shellcheck where to look for a file whose name is determined at runtime, or to skip a source by telling it to use /dev/null.
<dt>source-path
<dd> Add a directory to the search path for source/. statements (by default, only ShellCheck's working directory is included). Absolute paths will also be rooted in these paths. The special path SCRIPTDIR can be used to specify the currently checked script's directory, as in source-path=SCRIPTDIR or source-path=SCRIPTDIR/../libs. Multiple paths accumulate, and -P takes precedence over them.
<dt>shell
<dd> Overrides the shell detected from the shebang. This is useful for files meant to be included (and thus lacking a shebang), or possibly as a more targeted alternative to `disable=2039'.</dl>

<h2>RC FILES</h2>

 

 Unless --norc is used, ShellCheck will look for a file .shellcheckrc or shellcheckrc in the script's directory and each parent directory. If found, it will read key=value pairs from it and treat them as file-wide directives. 

 Here is an example .shellcheckrc:
<dl>
<dt>
<dd> <pre><code>
#Look for 'source' d files relative to the checked script,
#and also look for absolute paths in / mnt / chroot
source - path = SCRIPTDIR
                    source -
                path = / mnt / chroot
#Turn on warnings for unquoted variables with safe values
                                   enable = quote - safe - variables
#Turn on warnings for unassigned uppercase variables
                                                               enable = check - unassigned - uppercase
#Allow using `which` since it gives full paths and is common enough
                                                                                                 disable = SC2230
</code></pre></dl>
 

 If no .shellcheckrc is found in any of the parent directories, ShellCheck will look in ~/.shellcheckrc followed by the XDG config directory (usually ~/.config/shellcheckrc) on Unix, or %APPDATA%/shellcheckrc on Windows. Only the first file found will be used. 

 Note for Snap users: the Snap sandbox disallows access to hidden files. Use shellcheckrc without the dot instead. 

 Note for Docker users: ShellCheck will only be able to look for files that are mounted in the container, so ~/.shellcheckrc will not be read.

<h2>ENVIRONMENT VARIABLES</h2>

 

 The environment variable SHELLCHECK_OPTS can be set with default flags:
<dl>
<dt>
<dd> <pre>
export SHELLCHECK_OPTS='--shell=bash --exclude=SC2016'
</pre></dl>
 

 Its value will be split on spaces and prepended to the command line on each invocation.

<h2>RETURN VALUES</h2>

 

 ShellCheck uses the follow exit codes:
<dl>
<dt>&bull;
<dd> 0: All files successfully scanned with no issues.
<dt>&bull;
<dd> 1: All files successfully scanned with some issues.
<dt>&bull;
<dd> 2: Some files could not be processed (e.g. file not found).
<dt>&bull;
<dd> 3: ShellCheck was invoked with bad syntax (e.g. unknown flag).
<dt>&bull;
<dd> 4: ShellCheck was invoked with bad options (e.g. unknown formatter).</dl>

<h2>LOCALE</h2>

 

 This version of ShellCheck is only available in English. All files are leniently decoded as UTF-8, with a fallback of ISO-8859-1 for invalid sequences. LC_CTYPE is respected for output, and defaults to UTF-8 for locales where encoding is unspecified (such as the C locale). 

 Windows users seeing commitBuffer: invalid argument (invalid character) should set their terminal to use UTF-8 with chcp 65001.

<h2>AUTHORS</h2>

 

 ShellCheck is developed and maintained by Vidar Holen, with assistance from a long list of wonderful contributors.

<h2>REPORTING BUGS</h2>

 

 Bugs and issues can be reported on GitHub: 

 <a rel="nofollow" HREF="https://github.com/koalaman/shellcheck/issues">https://github.com/koalaman/shellcheck/issues</a>

<h2>COPYRIGHT</h2>

 

 Copyright 2012-2019, Vidar Holen and contributors. Licensed under the GNU General Public License version 3 or later, see <a rel="nofollow" HREF="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-sh/">sh</a>(1) <a HREF="/docs/linux/man/1-bash/">bash</a>(1) 

<h2>Index</h2>


