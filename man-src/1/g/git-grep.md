---

title: "git-grep(1)"
name: "git-grep"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-grep/"
description: "git-grep – Print lines matching a pattern"
---

<pre><code>
 git grep  [-a | --text] [-I] [--textconv] [-i | --ignore-case] [-w | --word-regexp]
           [-v | --invert-match] [-h|-H] [--full-name]
           [-E | --extended-regexp] [-G | --basic-regexp]
           [-P | --perl-regexp]
           [-F | --fixed-strings] [-n | --line-number] [--column]
           [-l | --files-with-matches] [-L | --files-without-match]
           [(-O | --open-files-in-pager) [&lt;pager&gt;]]
           [-z | --null]
           [ -o | --only-matching ] [-c | --count] [--all-match] [-q | --quiet]
           [--max-depth &lt;depth&gt;] [--[no-]recursive]
           [--color[=&lt;when&gt;] | --no-color]
           [--break] [--heading] [-p | --show-function]
           [-A &lt;post-context&gt;] [-B &lt;pre-context&gt;] [-C &lt;context&gt;]
           [-W | --function-context]
           [--threads &lt;num&gt;]
           [-f &lt;file&gt;] [-e] &lt;pattern&gt;
           [--and|--or|--not|(|)|-e &lt;pattern&gt;...]
           [--recurse-submodules] [--parent-basename &lt;basename&gt;]
           [ [--[no-]exclude-standard] [--cached | --no-index | --untracked] | &lt;tree&gt;...]
           [--] [&lt;pathspec&gt;...]
</code></pre>
<p> Look for specified patterns in the tracked files in the work tree, blobs registered in the index file, or blobs in given tree objects. Patterns are lists of one or more search expressions separated by newline characters. An empty string as search expression matches all lines.  </p>
<h2>OPTIONS</h2>
<p> --cached </p>
<dl>
<dd> <p> Instead of searching tracked files in the working tree, search blobs registered in the index file. </p>
 </dd></dl>
<p> --no-index </p>
<dl>
<dd> <p> Search files in the current directory that is not managed by Git. </p>
 </dd></dl>
<p> --untracked </p>
<dl>
<dd> <p> In addition to searching in the tracked files in the working tree, search also in untracked files. </p>
 </dd></dl>
<p> --no-exclude-standard </p>
<dl>
<dd> <p> Also search in ignored files by not honoring the <code>.gitignore</code> mechanism. Only useful with <code>--untracked</code>. </p>
 </dd></dl>
<p> --exclude-standard </p>
<dl>
<dd> <p> Do not pay attention to ignored files specified via the <code>.gitignore</code> mechanism. Only useful when searching files in the current directory with <code>--no-index</code>. </p>
 </dd></dl>
<p> --recurse-submodules </p>
<dl>
<dd> <p> Recursively search in each submodule that is active and checked out in the repository. When used in combination with the &lt;tree&gt; option the prefix of all submodule output will be the name of the parent project&#8217;s &lt;tree&gt; object. This option has no effect if <code>--no-index</code> is given. </p>
 </dd></dl>
<p> -a, --text </p>
<dl>
<dd> <p> Process binary files as if they were text. </p>
 </dd></dl>
<p> --textconv </p>
<dl>
<dd> <p> Honor textconv filter settings. </p>
 </dd></dl>
<p> --no-textconv </p>
<dl>
<dd> <p> Do not honor textconv filter settings. This is the default. </p>
 </dd></dl>
<p> -i, --ignore-case </p>
<dl>
<dd> <p> Ignore case differences between the patterns and the files. </p>
 </dd></dl>
<p> -I </p>
<dl>
<dd> <p> Don&#8217;t match the pattern in binary files. </p>
 </dd></dl>
<p> --max-depth &lt;depth&gt; </p>
<dl>
<dd> <p> For each &lt;pathspec&gt; given on command line, descend at most &lt;depth&gt; levels of directories. A value of -1 means no limit. This option is ignored if &lt;pathspec&gt; contains active wildcards. In other words if &quot;a*&quot; matches a directory named &quot;a*&quot;, &quot;*&quot; is matched literally so --max-depth is still effective. </p>
 </dd></dl>
<p> -r, --recursive </p>
<dl>
<dd> <p> Same as <code>--max-depth=-1</code>; this is the default. </p>
 </dd></dl>
<p> --no-recursive </p>
<dl>
<dd> <p> Same as <code>--max-depth=0</code>. </p>
 </dd></dl>
<p> -w, --word-regexp </p>
<dl>
<dd> <p> Match the pattern only at word boundary (either begin at the beginning of a line, or preceded by a non-word character; end at the end of a line or followed by a non-word character). </p>
 </dd></dl>
<p> -v, --invert-match </p>
<dl>
<dd> <p> Select non-matching lines. </p>
 </dd></dl>
<p> -h, -H </p>
<dl>
<dd> <p> By default, the command shows the filename for each match. <code>-h</code> option is used to suppress this output. <code>-H</code> is there for completeness and does not do anything except it overrides <code>-h</code> given earlier on the command line. </p>
 </dd></dl>
<p> --full-name </p>
<dl>
<dd> <p> When run from a subdirectory, the command usually outputs paths relative to the current directory. This option forces paths to be output relative to the project top directory. </p>
 </dd></dl>
<p> -E, --extended-regexp, -G, --basic-regexp </p>
<dl>
<dd> <p> Use POSIX extended/basic regexp for patterns. Default is to use basic regexp. </p>
 </dd></dl>
<p> -P, --perl-regexp </p>
<dl>
<dd> <p> Use Perl-compatible regular expressions for patterns. </p>
<p> Support for these types of regular expressions is an optional compile-time dependency. If Git wasn&#8217;t compiled with support for them providing this option will cause it to die. </p>
 </dd></dl>
<p> -F, --fixed-strings </p>
<dl>
<dd> <p> Use fixed strings for patterns (don&#8217;t interpret pattern as a regex). </p>
 </dd></dl>
<p> -n, --line-number </p>
<dl>
<dd> <p> Prefix the line number to matching lines. </p>
 </dd></dl>
<p> --column </p>
<dl>
<dd> <p> Prefix the 1-indexed byte-offset of the first match from the start of the matching line. </p>
 </dd></dl>
<p> -l, --files-with-matches, --name-only, -L, --files-without-match </p>
<dl>
<dd> <p> Instead of showing every matched line, show only the names of files that contain (or do not contain) matches. For better compatibility with <i>git diff</i>, <code>--name-only</code> is a synonym for <code>--files-with-matches</code>. </p>
 </dd></dl>
<p> -O[&lt;pager&gt;], --open-files-in-pager[=&lt;pager&gt;] </p>
<dl>
<dd> <p> Open the matching files in the pager (not the output of <i>grep</i>). If the pager happens to be &quot;less&quot; or &quot;vi&quot;, and the user specified only one pattern, the first file is positioned at the first match automatically. The <code>pager</code> argument is optional; if specified, it must be stuck to the option without a space. If <code>pager</code> is unspecified, the default pager will be used (see <code>core.pager</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
 </dd></dl>
<p> -z, --null </p>
<dl>
<dd> <p> Use \0 as the delimiter for pathnames in the output, and print them verbatim. Without this option, pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable core.quotePath (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
 </dd></dl>
<p> -o, --only-matching </p>
<dl>
<dd> <p> Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line. </p>
 </dd></dl>
<p> -c, --count </p>
<dl>
<dd> <p> Instead of showing every matched line, show the number of lines that match. </p>
 </dd></dl>
<p> --color[=&lt;when&gt;] </p>
<dl>
<dd> <p> Show colored matches. The value must be always (the default), never, or auto. </p>
 </dd></dl>
<p> --no-color </p>
<dl>
<dd> <p> Turn off match highlighting, even when the configuration file gives the default to color output. Same as <code>--color=never</code>. </p>
 </dd></dl>
<p> --break </p>
<dl>
<dd> <p> Print an empty line between matches from different files. </p>
 </dd></dl>
<p> --heading </p>
<dl>
<dd> <p> Show the filename above the matches in that file instead of at the start of each shown line. </p>
 </dd></dl>
<p> -p, --show-function </p>
<dl>
<dd> <p> Show the preceding line that contains the function name of the match, unless the matching line is a function name itself. The name is determined in the same way as <code>git diff</code> works out patch hunk headers (see <i>Defining a custom hunk-header</i> in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)). </p>
 </dd></dl>
<p> -&lt;num&gt;, -C &lt;num&gt;, --context &lt;num&gt; </p>
<dl>
<dd> <p> Show &lt;num&gt; leading and trailing lines, and place a line containing <code>--</code> between contiguous groups of matches. </p>
 </dd></dl>
<p> -A &lt;num&gt;, --after-context &lt;num&gt; </p>
<dl>
<dd> <p> Show &lt;num&gt; trailing lines, and place a line containing <code>--</code> between contiguous groups of matches. </p>
 </dd></dl>
<p> -B &lt;num&gt;, --before-context &lt;num&gt; </p>
<dl>
<dd> <p> Show &lt;num&gt; leading lines, and place a line containing <code>--</code> between contiguous groups of matches. </p>
 </dd></dl>
<p> -W, --function-context </p>
<dl>
<dd> <p> Show the surrounding text from the previous line containing a function name up to the one before the next function name, effectively showing the whole function in which the match was found. The function names are determined in the same way as <code>git diff</code> works out patch hunk headers (see <i>Defining a custom hunk-header</i> in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)). </p>
 </dd></dl>
<p> --threads &lt;num&gt; </p>
<dl>
<dd> <p> Number of grep worker threads to use. See <code>grep.threads</code> in <i>CONFIGURATION</i> for more information. </p>
 </dd></dl>
<p> -f &lt;file&gt; </p>
<dl>
<dd> <p> Read patterns from &lt;file&gt;, one per line. </p>
<p> Passing the pattern via &lt;file&gt; allows for providing a search pattern containing a \0. </p>
<p> Not all pattern types support patterns containing \0. Git will error out if a given pattern type can&#8217;t support such a pattern. The <code>--perl-regexp</code> pattern type when compiled against the PCRE v2 backend has the widest support for these types of patterns. </p>
<p> In versions of Git before 2.23.0 patterns containing \0 would be silently considered fixed. This was never documented, there were also odd and undocumented interactions between e.g. non-ASCII patterns containing \0 and <code>--ignore-case</code>. </p>
<p> In future versions we may learn to support patterns containing \0 for more search backends, until then we&#8217;ll die when the pattern type in question doesn&#8217;t support them. </p>
 </dd></dl>
<p> -e </p>
<dl>
<dd> <p> The next parameter is the pattern. This option has to be used for patterns starting with <code>-</code> and should be used in scripts passing user input to grep. Multiple patterns are combined by <i>or</i>. </p>
 </dd></dl>
<p> --and, --or, --not, ( ... ) </p>
<dl>
<dd> <p> Specify how multiple patterns are combined using Boolean expressions. <code>--or</code> is the default operator. <code>--and</code> has higher precedence than <code>--or</code>. <code>-e</code> has to be used for all patterns. </p>
 </dd></dl>
<p> --all-match </p>
<dl>
<dd> <p> When giving multiple pattern expressions combined with <code>--or</code>, this flag is specified to limit the match to files that have lines to match all of them. </p>
 </dd></dl>
<p> -q, --quiet </p>
<dl>
<dd> <p> Do not output matched lines; instead, exit with status 0 when there is a match and with non-zero status when there isn&#8217;t. </p>
 </dd></dl>
<p> &lt;tree&gt;... </p>
<dl>
<dd> <p> Instead of searching tracked files in the working tree, search blobs in the given trees. </p>
 </dd></dl>
<p> -- </p>
<dl>
<dd> <p> Signals the end of options; the rest of the parameters are &lt;pathspec&gt; limiters. </p>
 </dd></dl>
<p> &lt;pathspec&gt;... </p>
<dl>
<dd> <p> If given, limit the search to paths matching at least one pattern. Both leading paths match and <a href="/docs/linux/man/7-glob/">glob</a>(7) patterns are supported. </p>
<p> For more details about the &lt;pathspec&gt; syntax, see the <i>pathspec</i> entry in <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7). </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> <code>git grep &#8216;time_t&#8217; -- &#8216;*.[ch]&#8216;</code> </p>
<dl>
<dd> <p> Looks for <code>time_t</code> in all tracked .c and .h files in the working directory and its subdirectories. </p>
 </dd></dl>
<p> <code>git grep -e &#8216;#define&#8217; --and \( -e MAX_PATH -e PATH_MAX \)</code> </p>
<dl>
<dd> <p> Looks for a line that has <code>#define</code> and either <code>MAX_PATH</code> or <code>PATH_MAX</code>. </p>
 </dd></dl>
<p> <code>git grep --all-match -e NODE -e Unexpected</code> </p>
<dl>
<dd> <p> Looks for a line that has <code>NODE</code> or <code>Unexpected</code> in files that have lines that match both. </p>
 </dd></dl>
<p> <code>git grep solution -- :^Documentation</code> </p>
<dl>
<dd> <p> Looks for <code>solution</code>, excluding files in <code>Documentation</code>. </p>
 </dd></dl>
<h2>NOTES ON THREADS</h2>
<p> The <code>--threads</code> option (and the grep.threads configuration) will be ignored when <code>--open-files-in-pager</code> is used, forcing a single-threaded execution. </p>
<p> When grepping the object store (with <code>--cached</code> or giving tree objects), running with multiple threads might perform slower than single threaded if <code>--textconv</code> is given and there&#8217;re too many text conversions. So if you experience low performance in this case, it might be desirable to use <code>--threads=1</code>.  </p>
<h2>CONFIGURATION</h2>
<p> grep.lineNumber </p>
<dl>
<dd> <p> If set to true, enable <code>-n</code> option by default. </p>
 </dd></dl>
<p> grep.column </p>
<dl>
<dd> <p> If set to true, enable the <code>--column</code> option by default. </p>
 </dd></dl>
<p> grep.patternType </p>
<dl>
<dd> <p> Set the default matching behavior. Using a value of <i>basic</i>, <i>extended</i>, <i>fixed</i>, or <i>perl</i> will enable the <code>--basic-regexp</code>, <code>--extended-regexp</code>, <code>--fixed-strings</code>, or <code>--perl-regexp</code> option accordingly, while the value <i>default</i> will return to the default matching behavior. </p>
 </dd></dl>
<p> grep.extendedRegexp </p>
<dl>
<dd> <p> If set to true, enable <code>--extended-regexp</code> option by default. This option is ignored when the <code>grep.patternType</code> option is set to a value other than <i>default</i>. </p>
 </dd></dl>
<p> grep.threads </p>
<dl>
<dd> <p> Number of grep worker threads to use. If unset (or set to 0), Git will use as many threads as the number of logical cores available. </p>
 </dd></dl>
<p> grep.fullName </p>
<dl>
<dd> <p> If set to true, enable <code>--full-name</code> option by default. </p>
 </dd></dl>
<p> grep.fallbackToNoIndex </p>
<dl>
<dd> <p> If set to true, fall back to git grep --no-index if git grep is executed outside of a git repository. Defaults to false. </p>
 </dd></dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
