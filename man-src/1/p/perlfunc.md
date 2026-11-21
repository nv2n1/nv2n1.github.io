---

title: "perlfunc(1)"
name: "perlfunc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfunc/"
description: "perlfunc – Perl builtin functions"
---

<p> perlfunc - Perl builtin functions </p>
<h2>DESCRIPTION</h2>
<p> The functions in this section can serve as terms in an expression. They fall into two major categories: list operators and named unary operators. These differ in their precedence relationship with a following comma. (See the precedence table in perlop.) List operators take more than one argument, while unary operators can never take more than one argument. Thus, a comma terminates the argument of a unary operator, but merely separates the arguments of a list operator. A unary operator generally provides scalar context to its argument, while a list operator may provide either scalar or list contexts for its arguments. If it does both, scalar arguments come first and list argument follow, and there can only ever be one such list argument. For instance, <code>&quot;splice&quot;</code> has three scalar arguments followed by a list, whereas <code>&quot;gethostbyname&quot;</code> has four scalar arguments. </p>
<p> In the syntax descriptions that follow, list operators that expect a list (and provide list context for elements of the list) are shown with <font SIZE="-1">LIST</font> as an argument. Such a list may consist of any combination of scalar arguments or list values; the list values will be included in the list as if each individual element were interpolated at that point in the list, forming a longer single-dimensional list value. Commas should separate literal elements of the <font SIZE="-1">LIST.</font> </p>
<p> Any function in the list below may be used either with or without parentheses around its arguments. (The syntax descriptions omit the parentheses.) If you use parentheses, the simple but occasionally surprising rule is this: It <i>looks</i> like a function, therefore it <i>is</i> a function, and precedence doesn&#8217;t matter. Otherwise it&#8217;s a list operator or unary operator, and precedence does matter. Whitespace between the function and left parenthesis doesn&#8217;t count, so sometimes you need to be careful: </p>
<pre><code>    print 1+2+4; # Prints 7.
    print(1+2) + 4; # Prints 3.
    print (1+2)+4; # Also prints 3!
    print +(1+2)+4; # Prints 7.
    print ((1+2)+4); # Prints 7.
</code></pre>
<p> If you run Perl with the <code>&quot;use warnings&quot;</code> pragma, it can warn you about this. For example, the third line above produces: </p>
<pre><code>    print (...) interpreted as function at - line 1.
    Useless use of integer addition in void context at - line 1.
</code></pre>
<p> A few functions take no arguments at all, and therefore work as neither unary nor list operators. These include such functions as <code>&quot;time&quot;</code> and <code>&quot;endpwent&quot;</code>. For example, <code>&quot;time+86_400&quot;</code> always means <code>&quot;time() + 86_400&quot;</code>. </p>
<p> For functions that can be used in either a scalar or list context, nonabortive failure is generally indicated in scalar context by returning the undefined value, and in list context by returning the empty list. </p>
<p> Remember the following important rule: There is <code>no rule</code> that relates the behavior of an expression in list context to its behavior in scalar context, or vice versa. It might do two totally different things. Each operator and function decides which sort of value would be most appropriate to return in scalar context. Some operators return the length of the list that would have been returned in list context. Some operators return the first value in the list. Some operators return the last value in the list. Some operators return a count of successful operations. In general, they do what you want, unless you want consistency. </p>
<p> A named array in scalar context is quite different from what would at first glance appear to be a list in scalar context. You can&#8217;t get a list like <code>&quot;(1,2,3)&quot;</code> into being in scalar context, because the compiler knows the context at compile time. It would generate the scalar comma operator there, not the list concatenation version of the comma. That means it was never a list to start with. </p>
<p> In general, functions in Perl that serve as wrappers for system calls (``syscalls&#8217;&#8216;) of the same name (like <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code>closedir</code>(2), etc.) return true when they succeed and <code>&quot;undef&quot;</code> otherwise, as is usually mentioned in the descriptions below. This is different from the C interfaces, which return <code>&quot;-1&quot;</code> on failure. Exceptions to this rule include <code>&quot;wait&quot;</code>, <code>&quot;waitpid&quot;</code>, and <code>&quot;syscall&quot;</code>. System calls also set the special <code>$!</code> variable on failure. Other functions do not, except accidentally. </p>
<p> Extension modules can also hook into the Perl parser to define new kinds of keyword-headed expression. These may look like functions, but may also look completely different. The syntax following the keyword is defined entirely by the extension. If you are an implementor, see ``PL_keyword_plugin&#8217;&#8216; in perlapi for the mechanism. If you are using such a module, see the module&#8217;s documentation for details of the syntax that it defines.  </p>
<h3>Perl Functions by Category</h3>
<p> Here are Perl&#8217;s functions (including things that look like functions, like some keywords and named operators) arranged by category. Some functions appear in more than one place. Any warnings, including those produced by keywords, are described in perldiag and warnings. </p>
<dl>
<dt>Functions for SCALARs or strings</dt>
<dd> <p> <code>&quot;chomp&quot;</code>, <code>&quot;chop&quot;</code>, <code>&quot;chr&quot;</code>, <code>&quot;crypt&quot;</code>, <code>&quot;fc&quot;</code>, <code>&quot;hex&quot;</code>, <code>&quot;index&quot;</code>, <code>&quot;lc&quot;</code>, <code>&quot;lcfirst&quot;</code>, <code>&quot;length&quot;</code>, <code>&quot;oct&quot;</code>, <code>&quot;ord&quot;</code>, <code>&quot;pack&quot;</code>, <code>&quot;q//&quot;</code>, <code>&quot;qq//&quot;</code>, <code>&quot;reverse&quot;</code>, <code>&quot;rindex&quot;</code>, <code>&quot;sprintf&quot;</code>, <code>&quot;substr&quot;</code>, <code>&quot;tr///&quot;</code>, <code>&quot;uc&quot;</code>, <code>&quot;ucfirst&quot;</code>, <code>&quot;y///&quot;</code> </p>
<p> <code>&quot;fc&quot;</code> is available only if the <code>&quot;fc&quot;</code> feature is enabled or if it is prefixed with <code>&quot;CORE::&quot;</code>. The <code>&quot;fc&quot;</code> feature is enabled automatically with a <code>&quot;use v5.16&quot;</code> (or higher) declaration in the current scope. </p>
 </dd>
<dt>Regular expressions and pattern matching</dt>
<dd> <p> <code>&quot;m//&quot;</code>, <code>&quot;pos&quot;</code>, <code>&quot;qr//&quot;</code>, <code>&quot;quotemeta&quot;</code>, <code>&quot;s///&quot;</code>, <code>&quot;split&quot;</code>, <code>&quot;study&quot;</code> </p>
 </dd>
<dt>Numeric functions</dt>
<dd> <p> <code>&quot;abs&quot;</code>, <code>&quot;atan2&quot;</code>, <code>&quot;cos&quot;</code>, <code>&quot;exp&quot;</code>, <code>&quot;hex&quot;</code>, <code>&quot;int&quot;</code>, <code>&quot;log&quot;</code>, <code>&quot;oct&quot;</code>, <code>&quot;rand&quot;</code>, <code>&quot;sin&quot;</code>, <code>&quot;sqrt&quot;</code>, <code>&quot;srand&quot;</code> </p>
 </dd>
<dt>Functions for real @ARRAYs</dt>
<dd> <p> <code>&quot;each&quot;</code>, <code>&quot;keys&quot;</code>, <code>&quot;pop&quot;</code>, <code>&quot;push&quot;</code>, <code>&quot;shift&quot;</code>, <code>&quot;splice&quot;</code>, <code>&quot;unshift&quot;</code>, <code>&quot;values&quot;</code> </p>
 </dd>
<dt>Functions for list data</dt>
<dd> <p> <code>&quot;grep&quot;</code>, <code>&quot;join&quot;</code>, <code>&quot;map&quot;</code>, <code>&quot;qw//&quot;</code>, <code>&quot;reverse&quot;</code>, <code>&quot;sort&quot;</code>, <code>&quot;unpack&quot;</code> </p>
 </dd>
<dt>Functions for real %HASHes</dt>
<dd> <p> <code>&quot;delete&quot;</code>, <code>&quot;each&quot;</code>, <code>&quot;exists&quot;</code>, <code>&quot;keys&quot;</code>, <code>&quot;values&quot;</code> </p>
 </dd>
<dt>Input and output functions</dt>
<dd> <p> <code>&quot;binmode&quot;</code>, <code>&quot;close&quot;</code>, <code>&quot;closedir&quot;</code>, <code>&quot;dbmclose&quot;</code>, <code>&quot;dbmopen&quot;</code>, <code>&quot;die&quot;</code>, <code>&quot;eof&quot;</code>, <code>&quot;fileno&quot;</code>, <code>&quot;flock&quot;</code>, <code>&quot;format&quot;</code>, <code>&quot;getc&quot;</code>, <code>&quot;print&quot;</code>, <code>&quot;printf&quot;</code>, <code>&quot;read&quot;</code>, <code>&quot;readdir&quot;</code>, <code>&quot;readline&quot;</code>, <code>&quot;rewinddir&quot;</code>, <code>&quot;say&quot;</code>, <code>&quot;seek&quot;</code>, <code>&quot;seekdir&quot;</code>, <code>&quot;select&quot;</code>, <code>&quot;syscall&quot;</code>, <code>&quot;sysread&quot;</code>, <code>&quot;sysseek&quot;</code>, <code>&quot;syswrite&quot;</code>, <code>&quot;tell&quot;</code>, <code>&quot;telldir&quot;</code>, <code>&quot;truncate&quot;</code>, <code>&quot;warn&quot;</code>, <code>&quot;write&quot;</code> </p>
<p> <code>&quot;say&quot;</code> is available only if the <code>&quot;say&quot;</code> feature is enabled or if it is prefixed with <code>&quot;CORE::&quot;</code>. The <code>&quot;say&quot;</code> feature is enabled automatically with a <code>&quot;use v5.10&quot;</code> (or higher) declaration in the current scope. </p>
 </dd>
<dt>Functions for fixed-length data or records</dt>
<dd> <p> <code>&quot;pack&quot;</code>, <code>&quot;read&quot;</code>, <code>&quot;syscall&quot;</code>, <code>&quot;sysread&quot;</code>, <code>&quot;sysseek&quot;</code>, <code>&quot;syswrite&quot;</code>, <code>&quot;unpack&quot;</code>, <code>&quot;vec&quot;</code> </p>
 </dd>
<dt>Functions for filehandles, files, or directories</dt>
<dd> <p> <code>&quot;-</code>X <code>&quot;</code>, <code>&quot;chdir&quot;</code>, <code>&quot;chmod&quot;</code>, <code>&quot;chown&quot;</code>, <code>&quot;chroot&quot;</code>, <code>&quot;fcntl&quot;</code>, <code>&quot;glob&quot;</code>, <code>&quot;ioctl&quot;</code>, <code>&quot;link&quot;</code>, <code>&quot;lstat&quot;</code>, <code>&quot;mkdir&quot;</code>, <code>&quot;open&quot;</code>, <code>&quot;opendir&quot;</code>, <code>&quot;readlink&quot;</code>, <code>&quot;rename&quot;</code>, <code>&quot;rmdir&quot;</code>, <code>&quot;select&quot;</code>, <code>&quot;stat&quot;</code>, <code>&quot;symlink&quot;</code>, <code>&quot;sysopen&quot;</code>, <code>&quot;umask&quot;</code>, <code>&quot;unlink&quot;</code>, <code>&quot;utime&quot;</code> </p>
 </dd>
<dt>Keywords related to the control flow of your Perl program</dt>
<dd> <p> <code>&quot;break&quot;</code>, <code>&quot;caller&quot;</code>, <code>&quot;continue&quot;</code>, <code>&quot;die&quot;</code>, <code>&quot;do&quot;</code>, <code>&quot;dump&quot;</code>, <code>&quot;eval&quot;</code>, <code>&quot;evalbytes&quot;</code>, <code>&quot;exit&quot;</code>, <code>&quot;__FILE__&quot;</code>, <code>&quot;goto&quot;</code>, <code>&quot;last&quot;</code>, <code>&quot;__LINE__&quot;</code>, <code>&quot;next&quot;</code>, <code>&quot;__PACKAGE__&quot;</code>, <code>&quot;redo&quot;</code>, <code>&quot;return&quot;</code>, <code>&quot;sub&quot;</code>, <code>&quot;__SUB__&quot;</code>, <code>&quot;wantarray&quot;</code> </p>
<p> <code>&quot;break&quot;</code> is available only if you enable the experimental <code>&quot;switch&quot;</code> feature or use the <code>&quot;CORE::&quot;</code> prefix. The <code>&quot;switch&quot;</code> feature also enables the <code>&quot;default&quot;</code>, <code>&quot;given&quot;</code> and <code>&quot;when&quot;</code> statements, which are documented in ``Switch Statements&#8217;&#8216; in perlsyn. The <code>&quot;switch&quot;</code> feature is enabled automatically with a <code>&quot;use v5.10&quot;</code> (or higher) declaration in the current scope. In Perl v5.14 and earlier, <code>&quot;continue&quot;</code> required the <code>&quot;switch&quot;</code> feature, like the other keywords. </p>
<p> <code>&quot;evalbytes&quot;</code> is only available with the <code>&quot;evalbytes&quot;</code> feature (see feature) or if prefixed with <code>&quot;CORE::&quot;</code>. <code>&quot;__SUB__&quot;</code> is only available with the <code>&quot;current_sub&quot;</code> feature or if prefixed with <code>&quot;CORE::&quot;</code>. Both the <code>&quot;evalbytes&quot;</code> and <code>&quot;current_sub&quot;</code> features are enabled automatically with a <code>&quot;use v5.16&quot;</code> (or higher) declaration in the current scope. </p>
 </dd>
<dt>Keywords related to scoping</dt>
<dd> <p> <code>&quot;caller&quot;</code>, <code>&quot;import&quot;</code>, <code>&quot;local&quot;</code>, <code>&quot;my&quot;</code>, <code>&quot;our&quot;</code>, <code>&quot;package&quot;</code>, <code>&quot;state&quot;</code>, <code>&quot;use&quot;</code> </p>
<p> <code>&quot;state&quot;</code> is available only if the <code>&quot;state&quot;</code> feature is enabled or if it is prefixed with <code>&quot;CORE::&quot;</code>. The <code>&quot;state&quot;</code> feature is enabled automatically with a <code>&quot;use v5.10&quot;</code> (or higher) declaration in the current scope. </p>
 </dd>
<dt>Miscellaneous functions</dt>
<dd> <p> <code>&quot;defined&quot;</code>, <code>&quot;formline&quot;</code>, <code>&quot;lock&quot;</code>, <code>&quot;prototype&quot;</code>, <code>&quot;reset&quot;</code>, <code>&quot;scalar&quot;</code>, <code>&quot;undef&quot;</code> </p>
 </dd>
<dt>Functions for processes and process groups</dt>
<dd> <p> <code>&quot;alarm&quot;</code>, <code>&quot;exec&quot;</code>, <code>&quot;fork&quot;</code>, <code>&quot;getpgrp&quot;</code>, <code>&quot;getppid&quot;</code>, <code>&quot;getpriority&quot;</code>, <code>&quot;kill&quot;</code>, <code>&quot;pipe&quot;</code>, <code>&quot;qx//&quot;</code>, <code>&quot;readpipe&quot;</code>, <code>&quot;setpgrp&quot;</code>, <code>&quot;setpriority&quot;</code>, <code>&quot;sleep&quot;</code>, <code>&quot;system&quot;</code>, <code>&quot;times&quot;</code>, <code>&quot;wait&quot;</code>, <code>&quot;waitpid&quot;</code> </p>
 </dd>
<dt>Keywords related to Perl modules</dt>
<dd> <p> <code>&quot;do&quot;</code>, <code>&quot;import&quot;</code>, <code>&quot;no&quot;</code>, <code>&quot;package&quot;</code>, <code>&quot;require&quot;</code>, <code>&quot;use&quot;</code> </p>
 </dd>
<dt>Keywords related to classes and object-orientation</dt>
<dd> <p> <code>&quot;bless&quot;</code>, <code>&quot;dbmclose&quot;</code>, <code>&quot;dbmopen&quot;</code>, <code>&quot;package&quot;</code>, <code>&quot;ref&quot;</code>, <code>&quot;tie&quot;</code>, <code>&quot;tied&quot;</code>, <code>&quot;untie&quot;</code>, <code>&quot;use&quot;</code> </p>
 </dd>
<dt>Low-level socket functions</dt>
<dd> <p> <code>&quot;accept&quot;</code>, <code>&quot;bind&quot;</code>, <code>&quot;connect&quot;</code>, <code>&quot;getpeername&quot;</code>, <code>&quot;getsockname&quot;</code>, <code>&quot;getsockopt&quot;</code>, <code>&quot;listen&quot;</code>, <code>&quot;recv&quot;</code>, <code>&quot;send&quot;</code>, <code>&quot;setsockopt&quot;</code>, <code>&quot;shutdown&quot;</code>, <code>&quot;socket&quot;</code>, <code>&quot;socketpair&quot;</code> </p>
 </dd>
<dt>System V interprocess communication functions</dt>
<dd> <p> <code>&quot;msgctl&quot;</code>, <code>&quot;msgget&quot;</code>, <code>&quot;msgrcv&quot;</code>, <code>&quot;msgsnd&quot;</code>, <code>&quot;semctl&quot;</code>, <code>&quot;semget&quot;</code>, <code>&quot;semop&quot;</code>, <code>&quot;shmctl&quot;</code>, <code>&quot;shmget&quot;</code>, <code>&quot;shmread&quot;</code>, <code>&quot;shmwrite&quot;</code> </p>
 </dd>
<dt>Fetching user and group info</dt>
<dd> <p> <code>&quot;endgrent&quot;</code>, <code>&quot;endhostent&quot;</code>, <code>&quot;endnetent&quot;</code>, <code>&quot;endpwent&quot;</code>, <code>&quot;getgrent&quot;</code>, <code>&quot;getgrgid&quot;</code>, <code>&quot;getgrnam&quot;</code>, <code>&quot;getlogin&quot;</code>, <code>&quot;getpwent&quot;</code>, <code>&quot;getpwnam&quot;</code>, <code>&quot;getpwuid&quot;</code>, <code>&quot;setgrent&quot;</code>, <code>&quot;setpwent&quot;</code> </p>
 </dd>
<dt>Fetching network info</dt>
<dd> <p> <code>&quot;endprotoent&quot;</code>, <code>&quot;endservent&quot;</code>, <code>&quot;gethostbyaddr&quot;</code>, <code>&quot;gethostbyname&quot;</code>, <code>&quot;gethostent&quot;</code>, <code>&quot;getnetbyaddr&quot;</code>, <code>&quot;getnetbyname&quot;</code>, <code>&quot;getnetent&quot;</code>, <code>&quot;getprotobyname&quot;</code>, <code>&quot;getprotobynumber&quot;</code>, <code>&quot;getprotoent&quot;</code>, <code>&quot;getservbyname&quot;</code>, <code>&quot;getservbyport&quot;</code>, <code>&quot;getservent&quot;</code>, <code>&quot;sethostent&quot;</code>, <code>&quot;setnetent&quot;</code>, <code>&quot;setprotoent&quot;</code>, <code>&quot;setservent&quot;</code> </p>
 </dd>
<dt>Time-related functions</dt>
<dd> <p> <code>&quot;gmtime&quot;</code>, <code>&quot;localtime&quot;</code>, <code>&quot;time&quot;</code>, <code>&quot;times&quot;</code> </p>
 </dd>
<dt>Non-function keywords</dt>
<dd> <p> <code>&quot;and&quot;</code>, <code>&quot;AUTOLOAD&quot;</code>, <code>&quot;BEGIN&quot;</code>, <code>&quot;CHECK&quot;</code>, <code>&quot;cmp&quot;</code>, <code>&quot;CORE&quot;</code>, <code>&quot;__DATA__&quot;</code>, <code>&quot;default&quot;</code>, <code>&quot;DESTROY&quot;</code>, <code>&quot;else&quot;</code>, <code>&quot;elseif&quot;</code>, <code>&quot;elsif&quot;</code>, <code>&quot;END&quot;</code>, <code>&quot;__END__&quot;</code>, <code>&quot;eq&quot;</code>, <code>&quot;for&quot;</code>, <code>&quot;foreach&quot;</code>, <code>&quot;ge&quot;</code>, <code>&quot;given&quot;</code>, <code>&quot;gt&quot;</code>, <code>&quot;if&quot;</code>, <code>&quot;INIT&quot;</code>, <code>&quot;le&quot;</code>, <code>&quot;lt&quot;</code>, <code>&quot;ne&quot;</code>, <code>&quot;not&quot;</code>, <code>&quot;or&quot;</code>, <code>&quot;UNITCHECK&quot;</code>, <code>&quot;unless&quot;</code>, <code>&quot;until&quot;</code>, <code>&quot;when&quot;</code>, <code>&quot;while&quot;</code>, <code>&quot;x&quot;</code>, <code>&quot;xor&quot;</code> </p>
 </dd></dl>
<h3>Portability</h3>
<p> Perl was born in Unix and can therefore access all common Unix system calls. In non-Unix environments, the functionality of some Unix system calls may not be available or details of the available functionality may differ slightly. The Perl functions affected by this are: </p>
<p> <code>&quot;-</code>X <code>&quot;</code>, <code>&quot;binmode&quot;</code>, <code>&quot;chmod&quot;</code>, <code>&quot;chown&quot;</code>, <code>&quot;chroot&quot;</code>, <code>&quot;crypt&quot;</code>, <code>&quot;dbmclose&quot;</code>, <code>&quot;dbmopen&quot;</code>, <code>&quot;dump&quot;</code>, <code>&quot;endgrent&quot;</code>, <code>&quot;endhostent&quot;</code>, <code>&quot;endnetent&quot;</code>, <code>&quot;endprotoent&quot;</code>, <code>&quot;endpwent&quot;</code>, <code>&quot;endservent&quot;</code>, <code>&quot;exec&quot;</code>, <code>&quot;fcntl&quot;</code>, <code>&quot;flock&quot;</code>, <code>&quot;fork&quot;</code>, <code>&quot;getgrent&quot;</code>, <code>&quot;getgrgid&quot;</code>, <code>&quot;gethostbyname&quot;</code>, <code>&quot;gethostent&quot;</code>, <code>&quot;getlogin&quot;</code>, <code>&quot;getnetbyaddr&quot;</code>, <code>&quot;getnetbyname&quot;</code>, <code>&quot;getnetent&quot;</code>, <code>&quot;getppid&quot;</code>, <code>&quot;getpgrp&quot;</code>, <code>&quot;getpriority&quot;</code>, <code>&quot;getprotobynumber&quot;</code>, <code>&quot;getprotoent&quot;</code>, <code>&quot;getpwent&quot;</code>, <code>&quot;getpwnam&quot;</code>, <code>&quot;getpwuid&quot;</code>, <code>&quot;getservbyport&quot;</code>, <code>&quot;getservent&quot;</code>, <code>&quot;getsockopt&quot;</code>, <code>&quot;glob&quot;</code>, <code>&quot;ioctl&quot;</code>, <code>&quot;kill&quot;</code>, <code>&quot;link&quot;</code>, <code>&quot;lstat&quot;</code>, <code>&quot;msgctl&quot;</code>, <code>&quot;msgget&quot;</code>, <code>&quot;msgrcv&quot;</code>, <code>&quot;msgsnd&quot;</code>, <code>&quot;open&quot;</code>, <code>&quot;pipe&quot;</code>, <code>&quot;readlink&quot;</code>, <code>&quot;rename&quot;</code>, <code>&quot;select&quot;</code>, <code>&quot;semctl&quot;</code>, <code>&quot;semget&quot;</code>, <code>&quot;semop&quot;</code>, <code>&quot;setgrent&quot;</code>, <code>&quot;sethostent&quot;</code>, <code>&quot;setnetent&quot;</code>, <code>&quot;setpgrp&quot;</code>, <code>&quot;setpriority&quot;</code>, <code>&quot;setprotoent&quot;</code>, <code>&quot;setpwent&quot;</code>, <code>&quot;setservent&quot;</code>, <code>&quot;setsockopt&quot;</code>, <code>&quot;shmctl&quot;</code>, <code>&quot;shmget&quot;</code>, <code>&quot;shmread&quot;</code>, <code>&quot;shmwrite&quot;</code>, <code>&quot;socket&quot;</code>, <code>&quot;socketpair&quot;</code>, <code>&quot;stat&quot;</code>, <code>&quot;symlink&quot;</code>, <code>&quot;syscall&quot;</code>, <code>&quot;sysopen&quot;</code>, <code>&quot;system&quot;</code>, <code>&quot;times&quot;</code>, <code>&quot;truncate&quot;</code>, <code>&quot;umask&quot;</code>, <code>&quot;unlink&quot;</code>, <code>&quot;utime&quot;</code>, <code>&quot;wait&quot;</code>, <code>&quot;waitpid&quot;</code> </p>
<p> For more information about the portability of these functions, see perlport and other available platform-specific documentation.  </p>
<h3>Alphabetical Listing of Perl Functions</h3>
<dl>
<dt>-X <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>-X <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>-X <font SIZE="-1">DIRHANDLE</font></dt>
<dd>  </dd>
<dt>-X</dt>
<dd> <p> A file test, where X is one of the letters listed below. This unary operator takes one argument, either a filename, a filehandle, or a dirhandle, and tests the associated file to see if something is true about it. If the argument is omitted, tests <code>$_</code>, except for <code>&quot;-t&quot;</code>, which tests <font SIZE="-1">STDIN.</font> Unless otherwise documented, it returns <code>1</code> for true and <code>&#8216;&#8216;</code> for false. If the file doesn&#8217;t exist or can&#8217;t be examined, it returns <code>&quot;undef&quot;</code> and sets <code>$!</code> (errno). With the exception of the <code>&quot;-l&quot;</code> test they all follow symbolic links because they use <code>&quot;stat()&quot;</code> and not <code>&quot;lstat()&quot;</code> (so dangling symlinks can&#8217;t be examined and will therefore report failure). </p>
<p> Despite the funny names, precedence is the same as any other named unary operator. The operator may be any of: </p>
<pre><code>    -r File is readable by effective uid/gid.
    -w File is writable by effective uid/gid.
    -x File is executable by effective uid/gid.
    -o File is owned by effective uid.
    -R File is readable by real uid/gid.
    -W File is writable by real uid/gid.
    -X File is executable by real uid/gid.
    -O File is owned by real uid.
    -e File exists.
    -z File has zero size (is empty).
    -s File has nonzero size (returns size in bytes).
    -f File is a plain file.
    -d File is a directory.
    -l File is a symbolic link (false if symlinks aren't
        supported by the file system).
    -p File is a named pipe (FIFO), or Filehandle is a pipe.
    -S File is a socket.
    -b File is a block special file.
    -c File is a character special file.
    -t Filehandle is opened to a tty.
    -u File has setuid bit set.
    -g File has setgid bit set.
    -k File has sticky bit set.
    -T File is an ASCII or UTF-8 text file (heuristic guess).
    -B File is a &quot;binary&quot; file (opposite of -T).
    -M Script start time minus file modification time, in days.
    -A Same for access time.
    -C Same for inode change time (Unix, may differ for other
        platforms)
</code></pre>
<p> Example: </p>
<pre><code>    while (&lt;&gt;) {
        chomp;
        next unless -f $_; # ignore specials
        #...
    }
</code></pre>
<p> Note that <code>&quot;-s/a/b/&quot;</code> does not do a negated substitution. Saying <code>&quot;-exp($foo)&quot;</code> still works as expected, however: only single letters following a minus are interpreted as file tests. </p>
<p> These operators are exempt from the ``looks like a function rule&#8217;&#8216; described above. That is, an opening parenthesis after the operator does not affect how much of the following code constitutes the argument. Put the opening parentheses before the operator to separate it from code that follows (this applies only to operators with higher precedence than unary operators, of course): </p>
<pre><code>    -s($file) + 1024 # probably wrong; same as -s($file + 1024)
    (-s $file) + 1024 # correct
</code></pre>
<p> The interpretation of the file permission operators <code>&quot;-r&quot;</code>, <code>&quot;-R&quot;</code>, <code>&quot;-w&quot;</code>, <code>&quot;-W&quot;</code>, <code>&quot;-x&quot;</code>, and <code>&quot;-X&quot;</code> is by default based solely on the mode of the file and the uids and gids of the user. There may be other reasons you can&#8217;t actually read, write, or execute the file: for example network filesystem access controls, ACLs (access control lists), read-only filesystems, and unrecognized executable formats. Note that the use of these six specific operators to verify if some operation is possible is usually a mistake, because it may be open to race conditions. </p>
<p> Also note that, for the superuser on the local filesystems, the <code>&quot;-r&quot;</code>, <code>&quot;-R&quot;</code>, <code>&quot;-w&quot;</code>, and <code>&quot;-W&quot;</code> tests always return 1, and <code>&quot;-x&quot;</code> and <code>&quot;-X&quot;</code> return 1 if any execute bit is set in the mode. Scripts run by the superuser may thus need to do a <code>&quot;stat&quot;</code> to determine the actual mode of the file, or temporarily set their effective uid to something else. </p>
<p> If you are using ACLs, there is a pragma called <code>&quot;filetest&quot;</code> that may produce more accurate results than the bare <code>&quot;stat&quot;</code> mode bits. When under <code>&quot;use filetest &#8216;access&#8217;&quot;</code>, the above-mentioned filetests test whether the permission can(not) be granted using the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) family of system calls. Also note that the <code>&quot;-x&quot;</code> and <code>&quot;-X&quot;</code> tests may under this pragma return true even if there are no execute permission bits set (nor any extra execute permission ACLs). This strangeness is due to the underlying system calls&#8217; definitions. Note also that, due to the implementation of <code>&quot;use filetest &#8216;access&#8217;&quot;</code>, the <code>&quot;_&quot;</code> special filehandle won&#8217;t cache the results of the file tests when this pragma is in effect. Read the documentation for the <code>&quot;filetest&quot;</code> pragma for more information. </p>
<p> The <code>&quot;-T&quot;</code> and <code>&quot;-B&quot;</code> tests work as follows. The first block or so of the file is examined to see if it is valid <font SIZE="-1">UTF-8</font> that includes non-ASCII characters. If so, it&#8217;s a <code>&quot;-T&quot;</code> file. Otherwise, that same portion of the file is examined for odd characters such as strange control codes or characters with the high bit set. If more than a third of the characters are strange, it&#8217;s a <code>&quot;-B&quot;</code> file; otherwise it&#8217;s a <code>&quot;-T&quot;</code> file. Also, any file containing a zero byte in the examined portion is considered a binary file. (If executed within the scope of a use locale which includes <code>&quot;LC_CTYPE&quot;</code>, odd characters are anything that isn&#8217;t a printable nor space in the current locale.) If <code>&quot;-T&quot;</code> or <code>&quot;-B&quot;</code> is used on a filehandle, the current <font SIZE="-1">IO</font> buffer is examined rather than the first block. Both <code>&quot;-T&quot;</code> and <code>&quot;-B&quot;</code> return true on an empty file, or a file at <font SIZE="-1">EOF</font> when testing a filehandle. Because you have to read a file to do the <code>&quot;-T&quot;</code> test, on most occasions you want to use a <code>&quot;-f&quot;</code> against the file first, as in <code>&quot;next unless -f $file &amp;&amp; -T $file&quot;</code>. </p>
<p> If any of the file tests (or either the <code>&quot;stat&quot;</code> or <code>&quot;lstat&quot;</code> operator) is given the special filehandle consisting of a solitary underline, then the stat structure of the previous file test (or <code>&quot;stat&quot;</code> operator) is used, saving a system call. (This doesn&#8217;t work with <code>&quot;-t&quot;</code>, and you need to remember that <code>&quot;lstat&quot;</code> and <code>&quot;-l&quot;</code> leave values in the stat structure for the symbolic link, not the real file.) (Also, if the stat buffer was filled by an <code>&quot;lstat&quot;</code> call, <code>&quot;-T&quot;</code> and <code>&quot;-B&quot;</code> will reset it with the results of <code>&quot;stat _&quot;</code>). Example: </p>
<pre><code>    print &quot;Can do.\n&quot; if -r $a || -w _ || -x _;
    stat($filename);
    print &quot;Readable\n&quot; if -r _;
    print &quot;Writable\n&quot; if -w _;
    print &quot;Executable\n&quot; if -x _;
    print &quot;Setuid\n&quot; if -u _;
    print &quot;Setgid\n&quot; if -g _;
    print &quot;Sticky\n&quot; if -k _;
    print &quot;Text\n&quot; if -T _;
    print &quot;Binary\n&quot; if -B _;
</code></pre>
<p> As of Perl 5.10.0, as a form of purely syntactic sugar, you can stack file test operators, in a way that <code>&quot;-f -w -x $file&quot;</code> is equivalent to <code>&quot;-x $file &amp;&amp; -w _ &amp;&amp; -f _&quot;</code>. (This is only fancy syntax: if you use the return value of <code>&quot;-f $file&quot;</code> as an argument to another filetest operator, no special magic will happen.) </p>
<p> Portability issues: ``-X&#8217;&#8216; in perlport. </p>
<p> To avoid confusing would-be users of your code with mysterious syntax errors, put something like this at the top of your script: </p>
<pre><code>    use 5.010; # so filetest ops can stack
</code></pre>
 </dd>
<dt>abs <font SIZE="-1">VALUE</font></dt>
<dd>  </dd>
<dt>abs</dt>
<dd> <p> Returns the absolute value of its argument. If <font SIZE="-1">VALUE</font> is omitted, uses <code>$_</code>. </p>
 </dd>
<dt>accept <font SIZE="-1">NEWSOCKET,GENERICSOCKET</font></dt>
<dd> <p> Accepts an incoming socket connect, just as <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2) does. Returns the packed address if it succeeded, false otherwise. See the example in ``Sockets: Client/Server Communication&#8217;&#8216; in perlipc. </p>
<p> On systems that support a close-on-exec flag on files, the flag will be set for the newly opened file descriptor, as determined by the value of <code>$^F</code>. See ``$^F&#8217;&#8216; in perlvar. </p>
 </dd>
<dt>alarm <font SIZE="-1">SECONDS</font></dt>
<dd>  </dd>
<dt>alarm</dt>
<dd> <p> Arranges to have a <font SIZE="-1">SIGALRM</font> delivered to this process after the specified number of wallclock seconds has elapsed. If <font SIZE="-1">SECONDS</font> is not specified, the value stored in <code>$_</code> is used. (On some machines, unfortunately, the elapsed time may be up to one second less or more than you specified because of how seconds are counted, and process scheduling may delay the delivery of the signal even further.) </p>
<p> Only one timer may be counting at once. Each call disables the previous timer, and an argument of <code>0</code> may be supplied to cancel the previous timer without starting a new one. The returned value is the amount of time remaining on the previous timer. </p>
<p> For delays of finer granularity than one second, the Time::HiRes module (from <font SIZE="-1">CPAN,</font> and starting from Perl 5.8 part of the standard distribution) provides <code>&quot;ualarm&quot;</code>. You may also use Perl&#8217;s four-argument version of <code>&quot;select&quot;</code> leaving the first three arguments undefined, or you might be able to use the <code>&quot;syscall&quot;</code> interface to access <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) if your system supports it. See perlfaq8 for details. </p>
<p> It is usually a mistake to intermix <code>&quot;alarm&quot;</code> and <code>&quot;sleep&quot;</code> calls, because <code>&quot;sleep&quot;</code> may be internally implemented on your system with <code>&quot;alarm&quot;</code>. </p>
<p> If you want to use <code>&quot;alarm&quot;</code> to time out a system call you need to use an <code>&quot;eval&quot;</code>/<code>&quot;die&quot;</code> pair. You can&#8217;t rely on the alarm causing the system call to fail with <code>$!</code> set to <code>&quot;EINTR&quot;</code> because Perl sets up signal handlers to restart system calls on some systems. Using <code>&quot;eval&quot;</code>/<code>&quot;die&quot;</code> always works, modulo the caveats given in ``Signals&#8217;&#8216; in perlipc. </p>
<pre><code>    eval {
        local $SIG{ALRM} = sub { die &quot;alarm\n&quot; }; # NB: \n required
        alarm $timeout;
        my $nread = sysread $socket, $buffer, $size;
        alarm 0;
    };
    if ($@) {
        die unless $@ eq &quot;alarm\n&quot;; # propagate unexpected errors
        # timed out
    }
    else {
        # didn't
    }
</code></pre>
<p> For more information see perlipc. </p>
<p> Portability issues: ``alarm&#8217;&#8216; in perlport. </p>
 </dd>
<dt>atan2 Y,X</dt>
<dd> <p> Returns the arctangent of Y/X in the range -PI to <font SIZE="-1">PI.</font> </p>
<p> For the tangent operation, you may use the <code>&quot;Math::Trig::tan&quot;</code> function, or use the familiar relation: </p>
<pre><code>    sub tan { sin($_[0]) / cos($_[0]) }
</code></pre>
<p> The return value for <code>&quot;atan2(0,0)&quot;</code> is implementation-defined; consult your <code><a href="/docs/linux/man/3-atan2/">atan2</a></code>(3) manpage for more information. </p>
<p> Portability issues: ``atan2&#8217;&#8216; in perlport. </p>
 </dd>
<dt>bind <font SIZE="-1">SOCKET,NAME</font></dt>
<dd> <p> Binds a network address to a socket, just as <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) does. Returns true if it succeeded, false otherwise. <font SIZE="-1">NAME</font> should be a packed address of the appropriate type for the socket. See the examples in ``Sockets: Client/Server Communication&#8217;&#8216; in perlipc. </p>
 </dd>
<dt>binmode <font SIZE="-1">FILEHANDLE, LAYER</font></dt>
<dd>  </dd>
<dt>binmode <font SIZE="-1">FILEHANDLE</font></dt>
<dd> <p> Arranges for <font SIZE="-1">FILEHANDLE</font> to be read or written in ``binary&#8217;&#8216; or ``text&#8217;&#8216; mode on systems where the run-time libraries distinguish between binary and text files. If <font SIZE="-1">FILEHANDLE</font> is an expression, the value is taken as the name of the filehandle. Returns true on success, otherwise it returns <code>&quot;undef&quot;</code> and sets <code>$!</code> (errno). </p>
<p> On some systems (in general, <font SIZE="-1">DOS-</font> and Windows-based systems) <code>&quot;binmode&quot;</code> is necessary when you&#8217;re not working with a text file. For the sake of portability it is a good idea always to use it when appropriate, and never to use it when it isn&#8217;t appropriate. Also, people can set their I/O to be by default UTF8-encoded Unicode, not bytes. </p>
<p> In other words: regardless of platform, use <code>&quot;binmode&quot;</code> on binary data, like images, for example. </p>
<p> If <font SIZE="-1">LAYER</font> is present it is a single string, but may contain multiple directives. The directives alter the behaviour of the filehandle. When <font SIZE="-1">LAYER</font> is present, using binmode on a text file makes sense. </p>
<p> If <font SIZE="-1">LAYER</font> is omitted or specified as <code>&quot;:raw&quot;</code> the filehandle is made suitable for passing binary data. This includes turning off possible <font SIZE="-1">CRLF</font> translation and marking it as bytes (as opposed to Unicode characters). Note that, despite what may be implied in <i>``Programming Perl&#8217;&#8216;</i> (the Camel, 3rd edition) or elsewhere, <code>&quot;:raw&quot;</code> is <i>not</i> simply the inverse of <code>&quot;:crlf&quot;</code>. Other layers that would affect the binary nature of the stream are <i>also</i> disabled. See PerlIO, perlrun, and the discussion about the <font SIZE="-1">PERLIO</font> environment variable. </p>
<p> The <code>&quot;:bytes&quot;</code>, <code>&quot;:crlf&quot;</code>, <code>&quot;:utf8&quot;</code>, and any other directives of the form <code>&quot;:...&quot;</code>, are called I/O <i>layers</i>. The open pragma can be used to establish default I/O layers. </p>
<p> <i>The </i><font SIZE="-1"><i>LAYER</i></font><i> parameter of the </i>&quot;binmode&quot;<i> function is described as ``</i><font SIZE="-1"><i>DISCIPLINE&#8217;&#8216;</i></font><i> in ``Programming Perl, 3rd Edition&#8217;&#8216;. However, since the publishing of this book, by many known as ``Camel </i><font SIZE="-1"><i>III&#8217;&#8216;,</i></font><i> the consensus of the naming of this functionality has moved from ``discipline&#8217;&#8216; to ``layer&#8217;&#8216;. All documentation of this version of Perl therefore refers to ``layers&#8217;&#8216; rather than to ``disciplines&#8217;&#8216;. Now back to the regularly scheduled documentation...</i> </p>
<p> To mark <font SIZE="-1">FILEHANDLE</font> as <font SIZE="-1">UTF-8,</font> use <code>&quot;:utf8&quot;</code> or <code>&quot;:encoding(UTF-8)&quot;</code>. <code>&quot;:utf8&quot;</code> just marks the data as <font SIZE="-1">UTF-8</font> without further checking, while <code>&quot;:encoding(UTF-8)&quot;</code> checks the data for actually being valid <font SIZE="-1">UTF-8.</font> More details can be found in PerlIO::encoding. </p>
<p> In general, <code>&quot;binmode&quot;</code> should be called after <code>&quot;open&quot;</code> but before any I/O is done on the filehandle. Calling <code>&quot;binmode&quot;</code> normally flushes any pending buffered output data (and perhaps pending input data) on the handle. An exception to this is the <code>&quot;:encoding&quot;</code> layer that changes the default character encoding of the handle. The <code>&quot;:encoding&quot;</code> layer sometimes needs to be called in mid-stream, and it doesn&#8217;t flush the stream. <code>&quot;:encoding&quot;</code> also implicitly pushes on top of itself the <code>&quot;:utf8&quot;</code> layer because internally Perl operates on UTF8-encoded Unicode characters. </p>
<p> The operating system, device drivers, C libraries, and Perl run-time system all conspire to let the programmer treat a single character (<code>&quot;\n&quot;</code>) as the line terminator, irrespective of external representation. On many operating systems, the native text file representation matches the internal representation, but on some platforms the external representation of <code>&quot;\n&quot;</code> is made up of more than one character. </p>
<p> All variants of Unix, Mac <font SIZE="-1">OS</font> (old and new), and Stream_LF files on <font SIZE="-1">VMS</font> use a single character to end each line in the external representation of text (even though that single character is <font SIZE="-1">CARRIAGE RETURN</font> on old, pre-Darwin flavors of Mac <font SIZE="-1">OS,</font> and is <font SIZE="-1">LINE FEED</font> on Unix and most <font SIZE="-1">VMS</font> files). In other systems like <font SIZE="-1">OS/2, DOS,</font> and the various flavors of MS-Windows, your program sees a <code>&quot;\n&quot;</code> as a simple <code>&quot;\cJ&quot;</code>, but what&#8217;s stored in text files are the two characters <code>&quot;\cM\cJ&quot;</code>. That means that if you don&#8217;t use <code>&quot;binmode&quot;</code> on these systems, <code>&quot;\cM\cJ&quot;</code> sequences on disk will be converted to <code>&quot;\n&quot;</code> on input, and any <code>&quot;\n&quot;</code> in your program will be converted back to <code>&quot;\cM\cJ&quot;</code> on output. This is what you want for text files, but it can be disastrous for binary files. </p>
<p> Another consequence of using <code>&quot;binmode&quot;</code> (on some systems) is that special end-of-file markers will be seen as part of the data stream. For systems from the Microsoft family this means that, if your binary data contain <code>&quot;\cZ&quot;</code>, the I/O subsystem will regard it as the end of the file, unless you use <code>&quot;binmode&quot;</code>. </p>
<p> <code>&quot;binmode&quot;</code> is important not only for <code>&quot;readline&quot;</code> and <code>&quot;print&quot;</code> operations, but also when using <code>&quot;read&quot;</code>, <code>&quot;seek&quot;</code>, <code>&quot;sysread&quot;</code>, <code>&quot;syswrite&quot;</code> and <code>&quot;tell&quot;</code> (see perlport for more details). See the <code>$/</code> and <code>&quot;$\&quot;</code> variables in perlvar for how to manually set your input and output line-termination sequences. </p>
<p> Portability issues: ``binmode&#8217;&#8216; in perlport. </p>
 </dd>
<dt>bless <font SIZE="-1">REF,CLASSNAME</font></dt>
<dd>  </dd>
<dt>bless <font SIZE="-1">REF</font></dt>
<dd> <p> This function tells the thingy referenced by <font SIZE="-1">REF</font> that it is now an object in the <font SIZE="-1">CLASSNAME</font> package. If <font SIZE="-1">CLASSNAME</font> is an empty string, it is interpreted as referring to the <code>&quot;main&quot;</code> package. If <font SIZE="-1">CLASSNAME</font> is omitted, the current package is used. Because a <code>&quot;bless&quot;</code> is often the last thing in a constructor, it returns the reference for convenience. Always use the two-argument version if a derived class might inherit the method doing the blessing. See perlobj for more about the blessing (and blessings) of objects. </p>
<p> Consider always blessing objects in CLASSNAMEs that are mixed case. Namespaces with all lowercase names are considered reserved for Perl pragmas. Builtin types have all uppercase names. To prevent confusion, you may wish to avoid such package names as well. It is advised to avoid the class name <code>0</code>, because much code erroneously uses the result of <code>&quot;ref&quot;</code> as a truth value. </p>
<p> See ``Perl Modules&#8217;&#8216; in perlmod. </p>
 </dd>
<dt>break</dt>
<dd> <p> Break out of a <code>&quot;given&quot;</code> block. </p>
<p> <code>&quot;break&quot;</code> is available only if the <code>&quot;switch&quot;</code> feature is enabled or if it is prefixed with <code>&quot;CORE::&quot;</code>. The <code>&quot;switch&quot;</code> feature is enabled automatically with a <code>&quot;use v5.10&quot;</code> (or higher) declaration in the current scope. </p>
 </dd>
<dt>caller <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>caller</dt>
<dd> <p> Returns the context of the current pure perl subroutine call. In scalar context, returns the caller&#8217;s package name if there <i>is</i> a caller (that is, if we&#8217;re in a subroutine or <code>&quot;eval&quot;</code> or <code>&quot;require&quot;</code>) and the undefined value otherwise. caller never returns <font SIZE="-1">XS</font> subs and they are skipped. The next pure perl sub will appear instead of the <font SIZE="-1">XS</font> sub in caller&#8217;s return values. In list context, caller returns </p>
<pre><code>       # 0 1 2
    my ($package, $filename, $line) = caller;
</code></pre>
<p> With <font SIZE="-1">EXPR,</font> it returns some extra information that the debugger uses to print a stack trace. The value of <font SIZE="-1">EXPR</font> indicates how many call frames to go back before the current one. </p>
<pre><code>    # 0 1 2 3 4
 my ($package, $filename, $line, $subroutine, $hasargs,
    # 5 6 7 8 9 10
    $wantarray, $evaltext, $is_require, $hints, $bitmask, $hinthash)
  = caller($i);
</code></pre>
<p> Here, <code>$subroutine</code> is the function that the caller called (rather than the function containing the caller). Note that <code>$subroutine</code> may be <code>&quot;(eval)&quot;</code> if the frame is not a subroutine call, but an <code>&quot;eval&quot;</code>. In such a case additional elements <code>$evaltext</code> and <code>$is_require</code> are set: <code>$is_require</code> is true if the frame is created by a <code>&quot;require&quot;</code> or <code>&quot;use&quot;</code> statement, <code>$evaltext</code> contains the text of the <code>&quot;eval EXPR&quot;</code> statement. In particular, for an <code>&quot;eval BLOCK&quot;</code> statement, <code>$subroutine</code> is <code>&quot;(eval)&quot;</code>, but <code>$evaltext</code> is undefined. (Note also that each <code>&quot;use&quot;</code> statement creates a <code>&quot;require&quot;</code> frame inside an <code>&quot;eval EXPR&quot;</code> frame.) <code>$subroutine</code> may also be <code>&quot;(unknown)&quot;</code> if this particular subroutine happens to have been deleted from the symbol table. <code>$hasargs</code> is true if a new instance of <code>@_</code> was set up for the frame. <code>$hints</code> and <code>$bitmask</code> contain pragmatic hints that the caller was compiled with. <code>$hints</code> corresponds to <code>$^H</code>, and <code>$bitmask</code> corresponds to <code>&quot;${^WARNING_BITS}&quot;</code>. The <code>$hints</code> and <code>$bitmask</code> values are subject to change between versions of Perl, and are not meant for external use. </p>
<p> <code>$hinthash</code> is a reference to a hash containing the value of <code>&quot;%^H&quot;</code> when the caller was compiled, or <code>&quot;undef&quot;</code> if <code>&quot;%^H&quot;</code> was empty. Do not modify the values of this hash, as they are the actual values stored in the optree. </p>
<p> Furthermore, when called from within the <font SIZE="-1">DB</font> package in list context, and with an argument, caller returns more detailed information: it sets the list variable <code>@DB::args</code> to be the arguments with which the subroutine was invoked. </p>
<p> Be aware that the optimizer might have optimized call frames away before <code>&quot;caller&quot;</code> had a chance to get the information. That means that <code>caller(N)</code> might not return information about the call frame you expect it to, for <code>&quot;N &gt; 1&quot;</code>. In particular, <code>@DB::args</code> might have information from the previous time <code>&quot;caller&quot;</code> was called. </p>
<p> Be aware that setting <code>@DB::args</code> is <i>best effort</i>, intended for debugging or generating backtraces, and should not be relied upon. In particular, as <code>@_</code> contains aliases to the caller&#8217;s arguments, Perl does not take a copy of <code>@_</code>, so <code>@DB::args</code> will contain modifications the subroutine makes to <code>@_</code> or its contents, not the original values at call time. <code>@DB::args</code>, like <code>@_</code>, does not hold explicit references to its elements, so under certain cases its elements may have become freed and reallocated for other variables or temporary values. Finally, a side effect of the current implementation is that the effects of <code>&quot;shift @_&quot;</code> can <i>normally</i> be undone (but not <code>&quot;pop @_&quot;</code> or other splicing, <i>and</i> not if a reference to <code>@_</code> has been taken, <i>and</i> subject to the caveat about reallocated elements), so <code>@DB::args</code> is actually a hybrid of the current state and initial state of <code>@_</code>. Buyer beware. </p>
 </dd>
<dt>chdir <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>chdir <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>chdir <font SIZE="-1">DIRHANDLE</font></dt>
<dd>  </dd>
<dt>chdir</dt>
<dd> <p> Changes the working directory to <font SIZE="-1">EXPR,</font> if possible. If <font SIZE="-1">EXPR</font> is omitted, changes to the directory specified by <code>$ENV{HOME}</code>, if set; if not, changes to the directory specified by <code>$ENV{LOGDIR}</code>. (Under <font SIZE="-1">VMS,</font> the variable <code>$ENV{&#8216;SYS$LOGIN&#8217;}</code> is also checked, and used if it is set.) If neither is set, <code>&quot;chdir&quot;</code> does nothing and fails. It returns true on success, false otherwise. See the example under <code>&quot;die&quot;</code>. </p>
<p> On systems that support <code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2), you may pass a filehandle or directory handle as the argument. On systems that don&#8217;t support <code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2), passing handles raises an exception. </p>
 </dd>
<dt>chmod <font SIZE="-1">LIST</font></dt>
<dd> <p> Changes the permissions of a list of files. The first element of the list must be the numeric mode, which should probably be an octal number, and which definitely should <i>not</i> be a string of octal digits: <code>0644</code> is okay, but <code>&quot;0644&quot;</code> is not. Returns the number of files successfully changed. See also <code>&quot;oct&quot;</code> if all you have is a string. </p>
<pre><code>    my $cnt = chmod 0755, &quot;foo&quot;, &quot;bar&quot;;
    chmod 0755, @executables;
    my $mode = &quot;0644&quot;; chmod $mode, &quot;foo&quot;; # !!! sets mode to
                                                # --w----r-T
    my $mode = &quot;0644&quot;; chmod oct($mode), &quot;foo&quot;; # this is better
    my $mode = 0644; chmod $mode, &quot;foo&quot;; # this is best
</code></pre>
<p> On systems that support <code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2), you may pass filehandles among the files. On systems that don&#8217;t support <code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2), passing filehandles raises an exception. Filehandles must be passed as globs or glob references to be recognized; barewords are considered filenames. </p>
<pre><code>    open(my $fh, &quot;&lt;&quot;, &quot;foo&quot;);
    my $perm = (stat $fh)[2] &amp; 07777;
    chmod($perm | 0600, $fh);
</code></pre>
<p> You can also import the symbolic <code>&quot;S_I*&quot;</code> constants from the <code>&quot;Fcntl&quot;</code> module: </p>
<pre><code>    use Fcntl qw( :mode );
    chmod S_IRWXU|S_IRGRP|S_IXGRP|S_IROTH|S_IXOTH, @executables;
    # Identical to the chmod 0755 of the example above.
</code></pre>
<p> Portability issues: ``chmod&#8217;&#8216; in perlport. </p>
 </dd>
<dt>chomp <font SIZE="-1">VARIABLE</font></dt>
<dd>  </dd>
<dt>chomp( <font SIZE="-1">LIST</font> )</dt>
<dd>  </dd>
<dt>chomp</dt>
<dd> <p> This safer version of <code>&quot;chop&quot;</code> removes any trailing string that corresponds to the current value of <code>$/</code> (also known as <code>$INPUT_RECORD_SEPARATOR</code> in the <code>&quot;English&quot;</code> module). It returns the total number of characters removed from all its arguments. It&#8217;s often used to remove the newline from the end of an input record when you&#8217;re worried that the final record may be missing its newline. When in paragraph mode (<code>&quot;$/ = &#8216;&#8216;&quot;</code>), it removes all trailing newlines from the string. When in slurp mode (<code>&quot;$/ = undef&quot;</code>) or fixed-length record mode (<code>$/</code> is a reference to an integer or the like; see perlvar), <code>&quot;chomp&quot;</code> won&#8217;t remove anything. If <font SIZE="-1">VARIABLE</font> is omitted, it chomps <code>$_</code>. Example: </p>
<pre><code>    while (&lt;&gt;) {
        chomp; # avoid \n on last field
        my @array = split(/:/);
        # ...
    }
</code></pre>
<p> If <font SIZE="-1">VARIABLE</font> is a hash, it chomps the hash&#8217;s values, but not its keys, resetting the <code>&quot;each&quot;</code> iterator in the process. </p>
<p> You can actually chomp anything that&#8217;s an lvalue, including an assignment: </p>
<pre><code>    chomp(my $cwd = `pwd`);
    chomp(my $answer = &lt;STDIN&gt;);
</code></pre>
<p> If you chomp a list, each element is chomped, and the total number of characters removed is returned. </p>
<p> Note that parentheses are necessary when you&#8217;re chomping anything that is not a simple variable. This is because <code>&quot;chomp $cwd = `pwd`;&quot;</code> is interpreted as <code>&quot;(chomp $cwd) = `pwd`;&quot;</code>, rather than as <code>&quot;chomp( $cwd = `pwd` )&quot;</code> which you might expect. Similarly, <code>&quot;chomp $a, $b&quot;</code> is interpreted as <code>&quot;chomp($a), $b&quot;</code> rather than as <code>&quot;chomp($a, $b)&quot;</code>. </p>
 </dd>
<dt>chop <font SIZE="-1">VARIABLE</font></dt>
<dd>  </dd>
<dt>chop( <font SIZE="-1">LIST</font> )</dt>
<dd>  </dd>
<dt>chop</dt>
<dd> <p> Chops off the last character of a string and returns the character chopped. It is much more efficient than <code>&quot;s/.$//s&quot;</code> because it neither scans nor copies the string. If <font SIZE="-1">VARIABLE</font> is omitted, chops <code>$_</code>. If <font SIZE="-1">VARIABLE</font> is a hash, it chops the hash&#8217;s values, but not its keys, resetting the <code>&quot;each&quot;</code> iterator in the process. </p>
<p> You can actually chop anything that&#8217;s an lvalue, including an assignment. </p>
<p> If you chop a list, each element is chopped. Only the value of the last <code>&quot;chop&quot;</code> is returned. </p>
<p> Note that <code>&quot;chop&quot;</code> returns the last character. To return all but the last character, use <code>&quot;substr($string, 0, -1)&quot;</code>. </p>
<p> See also <code>&quot;chomp&quot;</code>. </p>
 </dd>
<dt>chown <font SIZE="-1">LIST</font></dt>
<dd> <p> Changes the owner (and group) of a list of files. The first two elements of the list must be the <i>numeric</i> uid and gid, in that order. A value of -1 in either position is interpreted by most systems to leave that value unchanged. Returns the number of files successfully changed. </p>
<pre><code>    my $cnt = chown $uid, $gid, 'foo', 'bar';
    chown $uid, $gid, @filenames;
</code></pre>
<p> On systems that support <code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2), you may pass filehandles among the files. On systems that don&#8217;t support <code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2), passing filehandles raises an exception. Filehandles must be passed as globs or glob references to be recognized; barewords are considered filenames. </p>
<p> Here&#8217;s an example that looks up nonnumeric uids in the passwd file: </p>
<pre><code>    print &quot;User: &quot;;
    chomp(my $user = &lt;STDIN&gt;);
    print &quot;Files: &quot;;
    chomp(my $pattern = &lt;STDIN&gt;);
    my ($login,$pass,$uid,$gid) = getpwnam($user)
        or die &quot;$user not in passwd file&quot;;
    my @ary = glob($pattern); # expand filenames
    chown $uid, $gid, @ary;
</code></pre>
<p> On most systems, you are not allowed to change the ownership of the file unless you&#8217;re the superuser, although you should be able to change the group to any of your secondary groups. On insecure systems, these restrictions may be relaxed, but this is not a portable assumption. On <font SIZE="-1">POSIX</font> systems, you can detect this condition this way: </p>
<pre><code>    use POSIX qw(sysconf _PC_CHOWN_RESTRICTED);
    my $can_chown_giveaway = ! sysconf(_PC_CHOWN_RESTRICTED);
</code></pre>
<p> Portability issues: ``chown&#8217;&#8216; in perlport. </p>
 </dd>
<dt>chr <font SIZE="-1">NUMBER</font></dt>
<dd>  </dd>
<dt>chr</dt>
<dd> <p> Returns the character represented by that <font SIZE="-1">NUMBER</font> in the character set. For example, <code>&quot;chr(65)&quot;</code> is <code>&quot;A&quot;</code> in either <font SIZE="-1">ASCII</font> or Unicode, and chr(0x263a) is a Unicode smiley face. </p>
<p> Negative values give the Unicode replacement character (<code>chr</code>(0xfffd)), except under the bytes pragma, where the low eight bits of the value (truncated to an integer) are used. </p>
<p> If <font SIZE="-1">NUMBER</font> is omitted, uses <code>$_</code>. </p>
<p> For the reverse, use <code>&quot;ord&quot;</code>. </p>
<p> Note that characters from 128 to 255 (inclusive) are by default internally not encoded as <font SIZE="-1">UTF-8</font> for backward compatibility reasons. </p>
<p> See perlunicode for more about Unicode. </p>
 </dd>
<dt>chroot <font SIZE="-1">FILENAME</font></dt>
<dd>  </dd>
<dt>chroot</dt>
<dd> <p> This function works like the system call by the same name: it makes the named directory the new root directory for all further pathnames that begin with a <code>&quot;/&quot;</code> by your process and all its children. (It doesn&#8217;t change your current working directory, which is unaffected.) For security reasons, this call is restricted to the superuser. If <font SIZE="-1">FILENAME</font> is omitted, does a <code>&quot;chroot&quot;</code> to <code>$_</code>. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> It is good security practice to do <code>&quot;chdir(&quot;/&quot;)&quot;</code> (<code>&quot;chdir&quot;</code> to the root directory) immediately after a <code>&quot;chroot&quot;</code>. </p>
<p> Portability issues: ``chroot&#8217;&#8216; in perlport. </p>
 </dd>
<dt>close <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>close</dt>
<dd> <p> Closes the file or pipe associated with the filehandle, flushes the <font SIZE="-1">IO</font> buffers, and closes the system file descriptor. Returns true if those operations succeed and if no error was reported by any PerlIO layer. Closes the currently selected filehandle if the argument is omitted. </p>
<p> You don&#8217;t have to close <font SIZE="-1">FILEHANDLE</font> if you are immediately going to do another <code>&quot;open&quot;</code> on it, because <code>&quot;open&quot;</code> closes it for you. (See <code>&quot;open&quot;</code>.) However, an explicit <code>&quot;close&quot;</code> on an input file resets the line counter (<code>$.</code>), while the implicit close done by <code>&quot;open&quot;</code> does not. </p>
<p> If the filehandle came from a piped open, <code>&quot;close&quot;</code> returns false if one of the other syscalls involved fails or if its program exits with non-zero status. If the only problem was that the program exited non-zero, <code>$!</code> will be set to <code>0</code>. Closing a pipe also waits for the process executing on the pipe to exit---in case you wish to look at the output of the pipe afterwards---and implicitly puts the exit status value of that command into <code>$?</code> and <code>&quot;${^CHILD_ERROR_NATIVE}&quot;</code>. </p>
<p> If there are multiple threads running, <code>&quot;close&quot;</code> on a filehandle from a piped open returns true without waiting for the child process to terminate, if the filehandle is still open in another thread. </p>
<p> Closing the read end of a pipe before the process writing to it at the other end is done writing results in the writer receiving a <font SIZE="-1">SIGPIPE.</font> If the other end can&#8217;t handle that, be sure to read all the data before closing the pipe. </p>
<p> Example: </p>
<pre><code>    open(OUTPUT, '|sort &gt;foo') # pipe to sort
        or die &quot;Can't start sort: $!&quot;;
    #... # print stuff to output
    close OUTPUT # wait for sort to finish
        or warn $! ? &quot;Error closing sort pipe: $!&quot;
                   : &quot;Exit status $? from sort&quot;;
    open(INPUT, 'foo') # get sort's results
        or die &quot;Can't open 'foo' for input: $!&quot;;
</code></pre>
<p> <font SIZE="-1">FILEHANDLE</font> may be an expression whose value can be used as an indirect filehandle, usually the real filehandle name or an autovivified handle. </p>
 </dd>
<dt>closedir <font SIZE="-1">DIRHANDLE</font></dt>
<dd> <p> Closes a directory opened by <code>&quot;opendir&quot;</code> and returns the success of that system call. </p>
 </dd>
<dt>connect <font SIZE="-1">SOCKET,NAME</font></dt>
<dd> <p> Attempts to connect to a remote socket, just like <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2). Returns true if it succeeded, false otherwise. <font SIZE="-1">NAME</font> should be a packed address of the appropriate type for the socket. See the examples in ``Sockets: Client/Server Communication&#8217;&#8216; in perlipc. </p>
 </dd>
<dt>continue <font SIZE="-1">BLOCK</font></dt>
<dd>  </dd>
<dt>continue</dt>
<dd> <p> When followed by a <font SIZE="-1">BLOCK,</font> <code>&quot;continue&quot;</code> is actually a flow control statement rather than a function. If there is a <code>&quot;continue&quot;</code> <font SIZE="-1">BLOCK</font> attached to a <font SIZE="-1">BLOCK</font> (typically in a <code>&quot;while&quot;</code> or <code>&quot;foreach&quot;</code>), it is always executed just before the conditional is about to be evaluated again, just like the third part of a <code>&quot;for&quot;</code> loop in C. Thus it can be used to increment a loop variable, even when the loop has been continued via the <code>&quot;next&quot;</code> statement (which is similar to the C <code>&quot;continue&quot;</code> statement). </p>
<p> <code>&quot;last&quot;</code>, <code>&quot;next&quot;</code>, or <code>&quot;redo&quot;</code> may appear within a <code>&quot;continue&quot;</code> block; <code>&quot;last&quot;</code> and <code>&quot;redo&quot;</code> behave as if they had been executed within the main block. So will <code>&quot;next&quot;</code>, but since it will execute a <code>&quot;continue&quot;</code> block, it may be more entertaining. </p>
<pre><code>    while (EXPR) {
        ### redo always comes here
        do_something;
    } continue {
        ### next always comes here
        do_something_else;
        # then back the top to re-check EXPR
    }
    ### last always comes here
</code></pre>
<p> Omitting the <code>&quot;continue&quot;</code> section is equivalent to using an empty one, logically enough, so <code>&quot;next&quot;</code> goes directly back to check the condition at the top of the loop. </p>
<p> When there is no <font SIZE="-1">BLOCK,</font> <code>&quot;continue&quot;</code> is a function that falls through the current <code>&quot;when&quot;</code> or <code>&quot;default&quot;</code> block instead of iterating a dynamically enclosing <code>&quot;foreach&quot;</code> or exiting a lexically enclosing <code>&quot;given&quot;</code>. In Perl 5.14 and earlier, this form of <code>&quot;continue&quot;</code> was only available when the <code>&quot;switch&quot;</code> feature was enabled. See feature and ``Switch Statements&#8217;&#8216; in perlsyn for more information. </p>
 </dd>
<dt>cos <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>cos</dt>
<dd> <p> Returns the cosine of <font SIZE="-1">EXPR</font> (expressed in radians). If <font SIZE="-1">EXPR</font> is omitted, takes the cosine of <code>$_</code>. </p>
<p> For the inverse cosine operation, you may use the <code>&quot;Math::Trig::acos&quot;</code> function, or use this relation: </p>
<pre><code>    sub acos { atan2( sqrt(1 - $_[0] * $_[0]), $_[0] ) }
</code></pre>
 </dd>
<dt>crypt <font SIZE="-1">PLAINTEXT,SALT</font></dt>
<dd> <p> Creates a digest string exactly like the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) function in the C library (assuming that you actually have a version there that has not been extirpated as a potential munition). </p>
<p> <code>&quot;crypt&quot;</code> is a one-way hash function. The <font SIZE="-1">PLAINTEXT</font> and <font SIZE="-1">SALT</font> are turned into a short string, called a digest, which is returned. The same <font SIZE="-1">PLAINTEXT</font> and <font SIZE="-1">SALT</font> will always return the same string, but there is no (known) way to get the original <font SIZE="-1">PLAINTEXT</font> from the hash. Small changes in the <font SIZE="-1">PLAINTEXT</font> or <font SIZE="-1">SALT</font> will result in large changes in the digest. </p>
<p> There is no decrypt function. This function isn&#8217;t all that useful for cryptography (for that, look for <i>Crypt</i> modules on your nearby <font SIZE="-1">CPAN</font> mirror) and the name ``crypt&#8217;&#8216; is a bit of a misnomer. Instead it is primarily used to check if two pieces of text are the same without having to transmit or store the text itself. An example is checking if a correct password is given. The digest of the password is stored, not the password itself. The user types in a password that is <code>&quot;crypt&quot;</code>&#8216;d with the same salt as the stored digest. If the two digests match, the password is correct. </p>
<p> When verifying an existing digest string you should use the digest as the salt (like <code>&quot;crypt($plain, $digest) eq $digest&quot;</code>). The <font SIZE="-1">SALT</font> used to create the digest is visible as part of the digest. This ensures <code>&quot;crypt&quot;</code> will hash the new string with the same salt as the digest. This allows your code to work with the standard <code>&quot;crypt&quot;</code> and with more exotic implementations. In other words, assume nothing about the returned string itself nor about how many bytes of <font SIZE="-1">SALT</font> may matter. </p>
<p> Traditionally the result is a string of 13 bytes: two first bytes of the salt, followed by 11 bytes from the set <code>&quot;[./0-9A-Za-z]&quot;</code>, and only the first eight bytes of <font SIZE="-1">PLAINTEXT</font> mattered. But alternative hashing schemes (like <font SIZE="-1">MD5</font>), higher level security schemes (like C2), and implementations on non-Unix platforms may produce different strings. </p>
<p> When choosing a new salt create a random two character string whose characters come from the set <code>&quot;[./0-9A-Za-z]&quot;</code> (like <code>&quot;join &#8216;&#8216;, (&#8216;.&#8216;, &#8216;/&#8216;, 0..9, &#8216;A&#8217;..&#8216;Z&#8217;, &#8216;a&#8217;..&#8216;z&#8217;)[rand 64, rand 64]&quot;</code>). This set of characters is just a recommendation; the characters allowed in the salt depend solely on your system&#8217;s crypt library, and Perl can&#8217;t restrict what salts <code>&quot;crypt&quot;</code> accepts. </p>
<p> Here&#8217;s an example that makes sure that whoever runs this program knows their password: </p>
<pre><code>    my $pwd = (getpwuid($&lt;))[1];
    system &quot;stty -echo&quot;;
    print &quot;Password: &quot;;
    chomp(my $word = &lt;STDIN&gt;);
    print &quot;\n&quot;;
    system &quot;stty echo&quot;;
    if (crypt($word, $pwd) ne $pwd) {
        die &quot;Sorry...\n&quot;;
    } else {
        print &quot;ok\n&quot;;
    }
</code></pre>
<p> Of course, typing in your own password to whoever asks you for it is unwise. </p>
<p> The <code>&quot;crypt&quot;</code> function is unsuitable for hashing large quantities of data, not least of all because you can&#8217;t get the information back. Look at the Digest module for more robust algorithms. </p>
<p> If using <code>&quot;crypt&quot;</code> on a Unicode string (which <i>potentially</i> has characters with codepoints above 255), Perl tries to make sense of the situation by trying to downgrade (a copy of) the string back to an eight-bit byte string before calling <code>&quot;crypt&quot;</code> (on that copy). If that works, good. If not, <code>&quot;crypt&quot;</code> dies with <code>&quot;Wide character in crypt&quot;</code>. </p>
<p> Portability issues: ``crypt&#8217;&#8216; in perlport. </p>
 </dd>
<dt>dbmclose <font SIZE="-1">HASH</font></dt>
<dd> <p> [This function has been largely superseded by the <code>&quot;untie&quot;</code> function.] </p>
<p> Breaks the binding between a <font SIZE="-1">DBM</font> file and a hash. </p>
<p> Portability issues: ``dbmclose&#8217;&#8216; in perlport. </p>
 </dd>
<dt>dbmopen <font SIZE="-1">HASH,DBNAME,MASK</font></dt>
<dd> <p> [This function has been largely superseded by the <code>&quot;tie&quot;</code> function.] </p>
<p> This binds a <code>dbm</code>(3), <code>ndbm</code>(3), <code>sdbm</code>(3), <code><a href="/docs/linux/man/3-gdbm/">gdbm</a></code>(3), or Berkeley <font SIZE="-1">DB</font> file to a hash. <font SIZE="-1">HASH</font> is the name of the hash. (Unlike normal <code>&quot;open&quot;</code>, the first argument is <i>not</i> a filehandle, even though it looks like one). <font SIZE="-1">DBNAME</font> is the name of the database (without the <i>.dir</i> or <i>.pag</i> extension if any). If the database does not exist, it is created with protection specified by <font SIZE="-1">MASK</font> (as modified by the <code>&quot;umask&quot;</code>). To prevent creation of the database if it doesn&#8217;t exist, you may specify a <font SIZE="-1">MODE</font> of 0, and the function will return a false value if it can&#8217;t find an existing database. If your system supports only the older <font SIZE="-1">DBM</font> functions, you may make only one <code>&quot;dbmopen&quot;</code> call in your program. In older versions of Perl, if your system had neither <font SIZE="-1">DBM</font> nor ndbm, calling <code>&quot;dbmopen&quot;</code> produced a fatal error; it now falls back to <code>sdbm</code>(3). </p>
<p> If you don&#8217;t have write access to the <font SIZE="-1">DBM</font> file, you can only read hash variables, not set them. If you want to test whether you can write, either use file tests or try setting a dummy hash entry inside an <code>&quot;eval&quot;</code> to trap the error. </p>
<p> Note that functions such as <code>&quot;keys&quot;</code> and <code>&quot;values&quot;</code> may return huge lists when used on large <font SIZE="-1">DBM</font> files. You may prefer to use the <code>&quot;each&quot;</code> function to iterate over large <font SIZE="-1">DBM</font> files. Example: </p>
<pre><code>    # print out history file offsets
    dbmopen(%HIST,'/usr/lib/news/history',0666);
    while (($key,$val) = each %HIST) {
        print $key, ' = ', unpack('L',$val), &quot;\n&quot;;
    }
    dbmclose(%HIST);
</code></pre>
<p> See also AnyDBM_File for a more general description of the pros and cons of the various dbm approaches, as well as DB_File for a particularly rich implementation. </p>
<p> You can control which <font SIZE="-1">DBM</font> library you use by loading that library before you call <code>&quot;dbmopen&quot;</code>: </p>
<pre><code>    use DB_File;
    dbmopen(%NS_Hist, &quot;$ENV{HOME}/.netscape/history.db&quot;)
        or die &quot;Can't open netscape history file: $!&quot;;
</code></pre>
<p> Portability issues: ``dbmopen&#8217;&#8216; in perlport. </p>
 </dd>
<dt>defined <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>defined</dt>
<dd> <p> Returns a Boolean value telling whether <font SIZE="-1">EXPR</font> has a value other than the undefined value <code>&quot;undef&quot;</code>. If <font SIZE="-1">EXPR</font> is not present, <code>$_</code> is checked. </p>
<p> Many operations return <code>&quot;undef&quot;</code> to indicate failure, end of file, system error, uninitialized variable, and other exceptional conditions. This function allows you to distinguish <code>&quot;undef&quot;</code> from other values. (A simple Boolean test will not distinguish among <code>&quot;undef&quot;</code>, zero, the empty string, and <code>&quot;0&quot;</code>, which are all equally false.) Note that since <code>&quot;undef&quot;</code> is a valid scalar, its presence doesn&#8217;t <i>necessarily</i> indicate an exceptional condition: <code>&quot;pop&quot;</code> returns <code>&quot;undef&quot;</code> when its argument is an empty array, <i>or</i> when the element to return happens to be <code>&quot;undef&quot;</code>. </p>
<p> You may also use <code>&quot;defined(&amp;func)&quot;</code> to check whether subroutine <code>&quot;func&quot;</code> has ever been defined. The return value is unaffected by any forward declarations of <code>&quot;func&quot;</code>. A subroutine that is not defined may still be callable: its package may have an <code>&quot;AUTOLOAD&quot;</code> method that makes it spring into existence the first time that it is called; see perlsub. </p>
<p> Use of <code>&quot;defined&quot;</code> on aggregates (hashes and arrays) is no longer supported. It used to report whether memory for that aggregate had ever been allocated. You should instead use a simple test for size: </p>
<pre><code>    if (@an_array) { print &quot;has array elements\n&quot; }
    if (%a_hash) { print &quot;has hash members\n&quot; }
</code></pre>
<p> When used on a hash element, it tells you whether the value is defined, not whether the key exists in the hash. Use <code>&quot;exists&quot;</code> for the latter purpose. </p>
<p> Examples: </p>
<pre><code>    print if defined $switch{D};
    print &quot;$val\n&quot; while defined($val = pop(@ary));
    die &quot;Can't readlink $sym: $!&quot;
        unless defined($value = readlink $sym);
    sub foo { defined &amp;$bar ? $bar-&gt;(@_) : die &quot;No bar&quot;; }
    $debugging = 0 unless defined $debugging;
</code></pre>
<p> Note: Many folks tend to overuse <code>&quot;defined&quot;</code> and are then surprised to discover that the number <code>0</code> and <code>&quot;&quot;</code> (the zero-length string) are, in fact, defined values. For example, if you say </p>
<pre><code>    &quot;ab&quot; =~ /a(.*)b/;
</code></pre>
<p> The pattern match succeeds and <code>$1</code> is defined, although it matched ``nothing&#8217;&#8216;. It didn&#8217;t really fail to match anything. Rather, it matched something that happened to be zero characters long. This is all very above-board and honest. When a function returns an undefined value, it&#8217;s an admission that it couldn&#8217;t give you an honest answer. So you should use <code>&quot;defined&quot;</code> only when questioning the integrity of what you&#8217;re trying to do. At other times, a simple comparison to <code>0</code> or <code>&quot;&quot;</code> is what you want. </p>
<p> See also <code>&quot;undef&quot;</code>, <code>&quot;exists&quot;</code>, <code>&quot;ref&quot;</code>. </p>
 </dd>
<dt>delete <font SIZE="-1">EXPR</font></dt>
<dd> <p> Given an expression that specifies an element or slice of a hash, <code>&quot;delete&quot;</code> deletes the specified elements from that hash so that <code>&quot;exists&quot;</code> on that element no longer returns true. Setting a hash element to the undefined value does not remove its key, but deleting it does; see <code>&quot;exists&quot;</code>. </p>
<p> In list context, usually returns the value or values deleted, or the last such element in scalar context. The return list&#8217;s length corresponds to that of the argument list: deleting non-existent elements returns the undefined value in their corresponding positions. When a key/value hash slice is passed to <code>&quot;delete&quot;</code>, the return value is a list of key/value pairs (two elements for each item deleted from the hash). </p>
<p> <code>&quot;delete&quot;</code> may also be used on arrays and array slices, but its behavior is less straightforward. Although <code>&quot;exists&quot;</code> will return false for deleted entries, deleting array elements never changes indices of existing values; use <code>&quot;shift&quot;</code> or <code>&quot;splice&quot;</code> for that. However, if any deleted elements fall at the end of an array, the array&#8217;s size shrinks to the position of the highest element that still tests true for <code>&quot;exists&quot;</code>, or to 0 if none do. In other words, an array won&#8217;t have trailing nonexistent elements after a delete. </p>
<p> <font SIZE="-1"><code>WARNING:</code></font> Calling <code>&quot;delete&quot;</code> on array values is strongly discouraged. The notion of deleting or checking the existence of Perl array elements is not conceptually coherent, and can lead to surprising behavior. </p>
<p> Deleting from <code>%ENV</code> modifies the environment. Deleting from a hash tied to a <font SIZE="-1">DBM</font> file deletes the entry from the <font SIZE="-1">DBM</font> file. Deleting from a <code>&quot;tied&quot;</code> hash or array may not necessarily return anything; it depends on the implementation of the <code>&quot;tied&quot;</code> package&#8217;s <font SIZE="-1">DELETE</font> method, which may do whatever it pleases. </p>
<p> The <code>&quot;delete local EXPR&quot;</code> construct localizes the deletion to the current block at run time. Until the block exits, elements locally deleted temporarily no longer exist. See ``Localized deletion of elements of composite types&#8217;&#8216; in perlsub. </p>
<pre><code>    my %hash = (foo =&gt; 11, bar =&gt; 22, baz =&gt; 33);
    my $scalar = delete $hash{foo}; # $scalar is 11
    $scalar = delete @hash{qw(foo bar)}; # $scalar is 22
    my @array = delete @hash{qw(foo baz)}; # @array is (undef,33)
</code></pre>
<p> The following (inefficiently) deletes all the values of <code>%HASH</code> and <code>@ARRAY:</code> </p>
<pre><code>    foreach my $key (keys %HASH) {
        delete $HASH{$key};
    }
    foreach my $index (0 .. $#ARRAY) {
        delete $ARRAY[$index];
    }
</code></pre>
<p> And so do these: </p>
<pre><code>    delete @HASH{keys %HASH};
    delete @ARRAY[0 .. $#ARRAY];
</code></pre>
<p> But both are slower than assigning the empty list or undefining <code>%HASH</code> or <code>@ARRAY</code>, which is the customary way to empty out an aggregate: </p>
<pre><code>    %HASH = (); # completely empty %HASH
    undef %HASH; # forget %HASH ever existed
    @ARRAY = (); # completely empty @ARRAY
    undef @ARRAY; # forget @ARRAY ever existed
</code></pre>
<p> The <font SIZE="-1">EXPR</font> can be arbitrarily complicated provided its final operation is an element or slice of an aggregate: </p>
<pre><code>    delete $ref-&gt;[$x][$y]{$key};
    delete @{$ref-&gt;[$x][$y]}{$key1, $key2, @morekeys};
    delete $ref-&gt;[$x][$y][$index];
    delete @{$ref-&gt;[$x][$y]}[$index1, $index2, @moreindices];
</code></pre>
 </dd>
<dt>die <font SIZE="-1">LIST</font></dt>
<dd> <p> <code>&quot;die&quot;</code> raises an exception. Inside an <code>&quot;eval&quot;</code> the exception is stuffed into <code>$@</code> and the <code>&quot;eval&quot;</code> is terminated with the undefined value. If the exception is outside of all enclosing <code>&quot;eval&quot;</code>s, then the uncaught exception is printed to <code>&quot;STDERR&quot;</code> and perl exits with an exit code indicating failure. If you need to exit the process with a specific exit code, see <code>&quot;exit&quot;</code>. </p>
<p> Equivalent examples: </p>
<pre><code>    die &quot;Can't cd to spool: $!\n&quot; unless chdir '/usr/spool/news';
    chdir '/usr/spool/news' or die &quot;Can't cd to spool: $!\n&quot;
</code></pre>
<p> Most of the time, <code>&quot;die&quot;</code> is called with a string to use as the exception. You may either give a single non-reference operand to serve as the exception, or a list of two or more items, which will be stringified and concatenated to make the exception. </p>
<p> If the string exception does not end in a newline, the current script line number and input line number (if any) and a newline are appended to it. Note that the ``input line number&#8217;&#8216; (also known as ``chunk&#8217;&#8216;) is subject to whatever notion of ``line&#8217;&#8216; happens to be currently in effect, and is also available as the special variable <code>$.</code>. See ``$/&#8216;&#8216; in perlvar and ``$.&#8216;&#8216; in perlvar. </p>
<p> Hint: sometimes appending <code>&quot;, stopped&quot;</code> to your message will cause it to make better sense when the string <code>&quot;at foo line 123&quot;</code> is appended. Suppose you are running script ``canasta&#8217;&#8216;. </p>
<pre><code>    die &quot;/etc/games is no good&quot;;
    die &quot;/etc/games is no good, stopped&quot;;
</code></pre>
<p> produce, respectively </p>
<pre><code>    /etc/games is no good at canasta line 123.
    /etc/games is no good, stopped at canasta line 123.
</code></pre>
<p> If <font SIZE="-1">LIST</font> was empty or made an empty string, and <code>$@</code> already contains an exception value (typically from a previous <code>&quot;eval&quot;</code>), then that value is reused after appending <code>&quot;\t...propagated&quot;</code>. This is useful for propagating exceptions: </p>
<pre><code>    eval { ... };
    die unless $@ =~ /Expected exception/;
</code></pre>
<p> If <font SIZE="-1">LIST</font> was empty or made an empty string, and <code>$@</code> contains an object reference that has a <code>&quot;PROPAGATE&quot;</code> method, that method will be called with additional file and line number parameters. The return value replaces the value in <code>$@</code>; i.e., as if <code>&quot;$@ = eval { $@-&gt;PROPAGATE(__FILE__, __LINE__) };&quot;</code> were called. </p>
<p> If <font SIZE="-1">LIST</font> was empty or made an empty string, and <code>$@</code> is also empty, then the string <code>&quot;Died&quot;</code> is used. </p>
<p> You can also call <code>&quot;die&quot;</code> with a reference argument, and if this is trapped within an <code>&quot;eval&quot;</code>, <code>$@</code> contains that reference. This permits more elaborate exception handling using objects that maintain arbitrary state about the exception. Such a scheme is sometimes preferable to matching particular string values of <code>$@</code> with regular expressions. </p>
<p> Because Perl stringifies uncaught exception messages before display, you&#8217;ll probably want to overload stringification operations on exception objects. See overload for details about that. The stringified message should be non-empty, and should end in a newline, in order to fit in with the treatment of string exceptions. Also, because an exception object reference cannot be stringified without destroying it, Perl doesn&#8217;t attempt to append location or other information to a reference exception. If you want location information with a complex exception object, you&#8217;ll have to arrange to put the location information into the object yourself. </p>
<p> Because <code>$@</code> is a global variable, be careful that analyzing an exception caught by <code>&quot;eval&quot;</code> doesn&#8217;t replace the reference in the global variable. It&#8217;s easiest to make a local copy of the reference before any manipulations. Here&#8217;s an example: </p>
<pre><code>    use Scalar::Util &quot;blessed&quot;;
    eval { ... ; die Some::Module::Exception-&gt;new( FOO =&gt; &quot;bar&quot; ) };
    if (my $ev_err = $@) {
        if (blessed($ev_err)
            &amp;&amp; $ev_err-&gt;isa(&quot;Some::Module::Exception&quot;)) {
            # handle Some::Module::Exception
        }
        else {
            # handle all other possible exceptions
        }
    }
</code></pre>
<p> If an uncaught exception results in interpreter exit, the exit code is determined from the values of <code>$!</code> and <code>$?</code> with this pseudocode: </p>
<pre><code>    exit $! if $!; # errno
    exit $? &gt;&gt; 8 if $? &gt;&gt; 8; # child exit status
    exit 255; # last resort
</code></pre>
<p> As with <code>&quot;exit&quot;</code>, <code>$?</code> is set prior to unwinding the call stack; any <code>&quot;DESTROY&quot;</code> or <code>&quot;END&quot;</code> handlers can then alter this value, and thus Perl&#8217;s exit code. </p>
<p> The intent is to squeeze as much possible information about the likely cause into the limited space of the system exit code. However, as <code>$!</code> is the value of C&#8217;s <code>&quot;errno&quot;</code>, which can be set by any system call, this means that the value of the exit code used by <code>&quot;die&quot;</code> can be non-predictable, so should not be relied upon, other than to be non-zero. </p>
<p> You can arrange for a callback to be run just before the <code>&quot;die&quot;</code> does its deed, by setting the <code>$SIG{__DIE__}</code> hook. The associated handler is called with the exception as an argument, and can change the exception, if it sees fit, by calling <code>&quot;die&quot;</code> again. See ``%SIG&#8217;&#8216; in perlvar for details on setting <code>%SIG</code> entries, and <code>&quot;eval&quot;</code> for some examples. Although this feature was to be run only right before your program was to exit, this is not currently so: the <code>$SIG{__DIE__}</code> hook is currently called even inside <code>&quot;eval&quot;</code>ed blocks/strings! If one wants the hook to do nothing in such situations, put </p>
<pre><code>    die @_ if $^S;
</code></pre>
<p> as the first line of the handler (see ``$^S&#8217;&#8216; in perlvar). Because this promotes strange action at a distance, this counterintuitive behavior may be fixed in a future release. </p>
<p> See also <code>&quot;exit&quot;</code>, <code>&quot;warn&quot;</code>, and the Carp module. </p>
 </dd>
<dt>do <font SIZE="-1">BLOCK</font></dt>
<dd> <p> Not really a function. Returns the value of the last command in the sequence of commands indicated by <font SIZE="-1">BLOCK.</font> When modified by the <code>&quot;while&quot;</code> or <code>&quot;until&quot;</code> loop modifier, executes the <font SIZE="-1">BLOCK</font> once before testing the loop condition. (On other statements the loop modifiers test the conditional first.) </p>
<p> <code>&quot;do BLOCK&quot;</code> does <i>not</i> count as a loop, so the loop control statements <code>&quot;next&quot;</code>, <code>&quot;last&quot;</code>, or <code>&quot;redo&quot;</code> cannot be used to leave or restart the block. See perlsyn for alternative strategies. </p>
 </dd>
<dt>do <font SIZE="-1">EXPR</font></dt>
<dd> <p> Uses the value of <font SIZE="-1">EXPR</font> as a filename and executes the contents of the file as a Perl script: </p>
<pre><code>    # load the exact specified file (./ and ../ special-cased)
    do '/foo/stat.pl';
    do './stat.pl';
    do '../foo/stat.pl';
    # search for the named file within @INC
    do 'stat.pl';
    do 'foo/stat.pl';
</code></pre>
<p> <code>&quot;do &#8216;./stat.pl&#8217;&quot;</code> is largely like </p>
<pre><code>    eval `cat stat.pl`;
</code></pre>
<p> except that it&#8217;s more concise, runs no external processes, and keeps track of the current filename for error messages. It also differs in that code evaluated with <code>&quot;do FILE&quot;</code> cannot see lexicals in the enclosing scope; <code>&quot;eval STRING&quot;</code> does. It&#8217;s the same, however, in that it does reparse the file every time you call it, so you probably don&#8217;t want to do this inside a loop. </p>
<p> Using <code>&quot;do&quot;</code> with a relative path (except for <i>./</i> and <i>../</i>), like </p>
<pre><code>    do 'foo/stat.pl';
</code></pre>
<p> will search the <code>@INC</code> directories, and update <code>%INC</code> if the file is found. See ``@INC&#8217;&#8216; in perlvar and ``%INC&#8217;&#8216; in perlvar for these variables. In particular, note that whilst historically <code>@INC</code> contained &#8216;.&#8216; (the current directory) making these two cases equivalent, that is no longer necessarily the case, as &#8216;.&#8216; is not included in <code>@INC</code> by default in perl versions 5.26.0 onwards. Instead, perl will now warn: </p>
<pre><code>    do &quot;stat.pl&quot; failed, '.' is no longer in @INC;
    did you mean do &quot;./stat.pl&quot;?
</code></pre>
<p> If <code>&quot;do&quot;</code> can read the file but cannot compile it, it returns <code>&quot;undef&quot;</code> and sets an error message in <code>$@</code>. If <code>&quot;do&quot;</code> cannot read the file, it returns undef and sets <code>$!</code> to the error. Always check <code>$@</code> first, as compilation could fail in a way that also sets <code>$!</code>. If the file is successfully compiled, <code>&quot;do&quot;</code> returns the value of the last expression evaluated. </p>
<p> Inclusion of library modules is better done with the <code>&quot;use&quot;</code> and <code>&quot;require&quot;</code> operators, which also do automatic error checking and raise an exception if there&#8217;s a problem. </p>
<p> You might like to use <code>&quot;do&quot;</code> to read in a program configuration file. Manual error checking can be done this way: </p>
<pre><code>    # Read in config files: system first, then user.
    # Beware of using relative pathnames here.
    for $file (&quot;/share/prog/defaults.rc&quot;,
               &quot;$ENV{HOME}/.someprogrc&quot;)
    {
        unless ($return = do $file) {
            warn &quot;couldn't parse $file: $@&quot; if $@;
            warn &quot;couldn't do $file: $!&quot; unless defined $return;
            warn &quot;couldn't run $file&quot; unless $return;
        }
    }
</code></pre>
 </dd>
<dt>dump <font SIZE="-1">LABEL</font></dt>
<dd>  </dd>
<dt>dump <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>dump</dt>
<dd> <p> This function causes an immediate core dump. See also the <code>-u</code> command-line switch in perlrun, which does the same thing. Primarily this is so that you can use the <code>undump</code> program (not supplied) to turn your core dump into an executable binary after having initialized all your variables at the beginning of the program. When the new binary is executed it will begin by executing a <code>&quot;goto LABEL&quot;</code> (with all the restrictions that <code>&quot;goto&quot;</code> suffers). Think of it as a goto with an intervening core dump and reincarnation. If <code>&quot;LABEL&quot;</code> is omitted, restarts the program from the top. The <code>&quot;dump EXPR&quot;</code> form, available starting in Perl 5.18.0, allows a name to be computed at run time, being otherwise identical to <code>&quot;dump LABEL&quot;</code>. </p>
<p> <font SIZE="-1"><code>WARNING</code></font>: Any files opened at the time of the dump will <i>not</i> be open any more when the program is reincarnated, with possible resulting confusion by Perl. </p>
<p> This function is now largely obsolete, mostly because it&#8217;s very hard to convert a core file into an executable. As of Perl 5.30, it must be invoked as <code>&quot;CORE::dump()&quot;</code>. </p>
<p> Unlike most named operators, this has the same precedence as assignment. It is also exempt from the looks-like-a-function rule, so <code>&quot;dump (&quot;foo&quot;).&quot;bar&quot;&quot;</code> will cause ``bar&#8217;&#8216; to be part of the argument to <code>&quot;dump&quot;</code>. </p>
<p> Portability issues: ``dump&#8217;&#8216; in perlport. </p>
 </dd>
<dt>each <font SIZE="-1">HASH</font></dt>
<dd>  </dd>
<dt>each <font SIZE="-1">ARRAY</font></dt>
<dd> <p> When called on a hash in list context, returns a 2-element list consisting of the key and value for the next element of a hash. In Perl 5.12 and later only, it will also return the index and value for the next element of an array so that you can iterate over it; older Perls consider this a syntax error. When called in scalar context, returns only the key (not the value) in a hash, or the index in an array. </p>
<p> Hash entries are returned in an apparently random order. The actual random order is specific to a given hash; the exact same series of operations on two hashes may result in a different order for each hash. Any insertion into the hash may change the order, as will any deletion, with the exception that the most recent key returned by <code>&quot;each&quot;</code> or <code>&quot;keys&quot;</code> may be deleted without changing the order. So long as a given hash is unmodified you may rely on <code>&quot;keys&quot;</code>, <code>&quot;values&quot;</code> and <code>&quot;each&quot;</code> to repeatedly return the same order as each other. See ``Algorithmic Complexity Attacks&#8217;&#8216; in perlsec for details on why hash order is randomized. Aside from the guarantees provided here the exact details of Perl&#8217;s hash algorithm and the hash traversal order are subject to change in any release of Perl. </p>
<p> After <code>&quot;each&quot;</code> has returned all entries from the hash or array, the next call to <code>&quot;each&quot;</code> returns the empty list in list context and <code>&quot;undef&quot;</code> in scalar context; the next call following <i>that</i> one restarts iteration. Each hash or array has its own internal iterator, accessed by <code>&quot;each&quot;</code>, <code>&quot;keys&quot;</code>, and <code>&quot;values&quot;</code>. The iterator is implicitly reset when <code>&quot;each&quot;</code> has reached the end as just described; it can be explicitly reset by calling <code>&quot;keys&quot;</code> or <code>&quot;values&quot;</code> on the hash or array, or by referencing the hash (but not array) in list context. If you add or delete a hash&#8217;s elements while iterating over it, the effect on the iterator is unspecified; for example, entries may be skipped or duplicated---so don&#8217;t do that. Exception: It is always safe to delete the item most recently returned by <code>&quot;each&quot;</code>, so the following code works properly: </p>
<pre><code>    while (my ($key, $value) = each %hash) {
        print $key, &quot;\n&quot;;
        delete $hash{$key}; # This is safe
    }
</code></pre>
<p> Tied hashes may have a different ordering behaviour to perl&#8217;s hash implementation. </p>
<p> The iterator used by <code>&quot;each&quot;</code> is attached to the hash or array, and is shared between all iteration operations applied to the same hash or array. Thus all uses of <code>&quot;each&quot;</code> on a single hash or array advance the same iterator location. All uses of <code>&quot;each&quot;</code> are also subject to having the iterator reset by any use of <code>&quot;keys&quot;</code> or <code>&quot;values&quot;</code> on the same hash or array, or by the hash (but not array) being referenced in list context. This makes <code>&quot;each&quot;</code>-based loops quite fragile: it is easy to arrive at such a loop with the iterator already part way through the object, or to accidentally clobber the iterator state during execution of the loop body. It&#8217;s easy enough to explicitly reset the iterator before starting a loop, but there is no way to insulate the iterator state used by a loop from the iterator state used by anything else that might execute during the loop body. To avoid these problems, use a <code>&quot;foreach&quot;</code> loop rather than <code>&quot;while&quot;</code>-<code>&quot;each&quot;</code>. </p>
<p> This prints out your environment like the <code><a href="/docs/linux/man/1-printenv/">printenv</a></code>(1) program, but in a different order: </p>
<pre><code>    while (my ($key,$value) = each %ENV) {
        print &quot;$key=$value\n&quot;;
    }
</code></pre>
<p> Starting with Perl 5.14, an experimental feature allowed <code>&quot;each&quot;</code> to take a scalar expression. This experiment has been deemed unsuccessful, and was removed as of Perl 5.24. </p>
<p> As of Perl 5.18 you can use a bare <code>&quot;each&quot;</code> in a <code>&quot;while&quot;</code> loop, which will set <code>$_</code> on every iteration. If either an <code>&quot;each&quot;</code> expression or an explicit assignment of an <code>&quot;each&quot;</code> expression to a scalar is used as a <code>&quot;while&quot;</code>/<code>&quot;for&quot;</code> condition, then the condition actually tests for definedness of the expression&#8217;s value, not for its regular truth value. </p>
<pre><code>    while (each %ENV) {
        print &quot;$_=$ENV{$_}\n&quot;;
    }
</code></pre>
<p> To avoid confusing would-be users of your code who are running earlier versions of Perl with mysterious syntax errors, put this sort of thing at the top of your file to signal that your code will work <i>only</i> on Perls of a recent vintage: </p>
<pre><code>    use 5.012; # so keys/values/each work on arrays
    use 5.018; # so each assigns to $_ in a lone while test
</code></pre>
<p> See also <code>&quot;keys&quot;</code>, <code>&quot;values&quot;</code>, and <code>&quot;sort&quot;</code>. </p>
 </dd>
<dt>eof <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>eof ()</dt>
<dd>  </dd>
<dt>eof</dt>
<dd> <p> Returns 1 if the next read on <font SIZE="-1">FILEHANDLE</font> will return end of file <i>or</i> if <font SIZE="-1">FILEHANDLE</font> is not open. <font SIZE="-1">FILEHANDLE</font> may be an expression whose value gives the real filehandle. (Note that this function actually reads a character and then <code>&quot;ungetc&quot;</code>s it, so isn&#8217;t useful in an interactive context.) Do not read from a terminal file (or call <code>&quot;eof(FILEHANDLE)&quot;</code> on it) after end-of-file is reached. File types such as terminals may lose the end-of-file condition if you do. </p>
<p> An <code>&quot;eof&quot;</code> without an argument uses the last file read. Using <code>&quot;eof()&quot;</code> with empty parentheses is different. It refers to the pseudo file formed from the files listed on the command line and accessed via the <code>&quot;&lt;&gt;&quot;</code> operator. Since <code>&quot;&lt;&gt;&quot;</code> isn&#8217;t explicitly opened, as a normal filehandle is, an <code>&quot;eof()&quot;</code> before <code>&quot;&lt;&gt;&quot;</code> has been used will cause <code>@ARGV</code> to be examined to determine if input is available. Similarly, an <code>&quot;eof()&quot;</code> after <code>&quot;&lt;&gt;&quot;</code> has returned end-of-file will assume you are processing another <code>@ARGV</code> list, and if you haven&#8217;t set <code>@ARGV</code>, will read input from <code>&quot;STDIN&quot;</code>; see ``I/O Operators&#8217;&#8216; in perlop. </p>
<p> In a <code>&quot;while (&lt;&gt;)&quot;</code> loop, <code>&quot;eof&quot;</code> or <code>&quot;eof(ARGV)&quot;</code> can be used to detect the end of each file, whereas <code>&quot;eof()&quot;</code> will detect the end of the very last file only. Examples: </p>
<pre><code>    # reset line numbering on each input file
    while (&lt;&gt;) {
        next if /^\s*#/; # skip comments
        print &quot;$.\t$_&quot;;
    } continue {
        close ARGV if eof; # Not eof()!
    }
    # insert dashes just before last line of last file
    while (&lt;&gt;) {
        if (eof()) { # check for end of last file
            print &quot;--------------\n&quot;;
        }
        print;
        last if eof(); # needed if we're reading from a terminal
    }
</code></pre>
<p> Practical hint: you almost never need to use <code>&quot;eof&quot;</code> in Perl, because the input operators typically return <code>&quot;undef&quot;</code> when they run out of data or encounter an error. </p>
 </dd>
<dt>eval <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>eval <font SIZE="-1">BLOCK</font></dt>
<dd>  </dd>
<dt>eval</dt>
<dd> <p> <code>&quot;eval&quot;</code> in all its forms is used to execute a little Perl program, trapping any errors encountered so they don&#8217;t crash the calling program. </p>
<p> Plain <code>&quot;eval&quot;</code> with no argument is just <code>&quot;eval EXPR&quot;</code>, where the expression is understood to be contained in <code>$_</code>. Thus there are only two real <code>&quot;eval&quot;</code> forms; the one with an <font SIZE="-1">EXPR</font> is often called ``string eval&#8217;&#8216;. In a string eval, the value of the expression (which is itself determined within scalar context) is first parsed, and if there were no errors, executed as a block within the lexical context of the current Perl program. This form is typically used to delay parsing and subsequent execution of the text of <font SIZE="-1">EXPR</font> until run time. Note that the value is parsed every time the <code>&quot;eval&quot;</code> executes. </p>
<p> The other form is called ``block eval&#8217;&#8216;. It is less general than string eval, but the code within the <font SIZE="-1">BLOCK</font> is parsed only once (at the same time the code surrounding the <code>&quot;eval&quot;</code> itself was parsed) and executed within the context of the current Perl program. This form is typically used to trap exceptions more efficiently than the first, while also providing the benefit of checking the code within <font SIZE="-1">BLOCK</font> at compile time. <font SIZE="-1">BLOCK</font> is parsed and compiled just once. Since errors are trapped, it often is used to check if a given feature is available. </p>
<p> In both forms, the value returned is the value of the last expression evaluated inside the mini-program; a return statement may also be used, just as with subroutines. The expression providing the return value is evaluated in void, scalar, or list context, depending on the context of the <code>&quot;eval&quot;</code> itself. See <code>&quot;wantarray&quot;</code> for more on how the evaluation context can be determined. </p>
<p> If there is a syntax error or runtime error, or a <code>&quot;die&quot;</code> statement is executed, <code>&quot;eval&quot;</code> returns <code>&quot;undef&quot;</code> in scalar context, or an empty list in list context, and <code>$@</code> is set to the error message. (Prior to 5.16, a bug caused <code>&quot;undef&quot;</code> to be returned in list context for syntax errors, but not for runtime errors.) If there was no error, <code>$@</code> is set to the empty string. A control flow operator like <code>&quot;last&quot;</code> or <code>&quot;goto&quot;</code> can bypass the setting of <code>$@</code>. Beware that using <code>&quot;eval&quot;</code> neither silences Perl from printing warnings to <font SIZE="-1">STDERR,</font> nor does it stuff the text of warning messages into <code>$@</code>. To do either of those, you have to use the <code>$SIG{__WARN__}</code> facility, or turn off warnings inside the <font SIZE="-1">BLOCK</font> or <font SIZE="-1">EXPR</font> using <code>&quot;no warnings &#8216;all&#8217;&quot;</code>. See <code>&quot;warn&quot;</code>, perlvar, and warnings. </p>
<p> Note that, because <code>&quot;eval&quot;</code> traps otherwise-fatal errors, it is useful for determining whether a particular feature (such as <code>&quot;socket&quot;</code> or <code>&quot;symlink&quot;</code>) is implemented. It is also Perl&#8217;s exception-trapping mechanism, where the <code>&quot;die&quot;</code> operator is used to raise exceptions. </p>
<p> Before Perl 5.14, the assignment to <code>$@</code> occurred before restoration of localized variables, which means that for your code to run on older versions, a temporary is required if you want to mask some, but not all errors: </p>
<pre><code> # alter $@ on nefarious repugnancy only
 {
    my $e;
    {
      local $@; # protect existing $@
      eval { test_repugnancy() };
      # $@ =~ /nefarious/ and die $@; # Perl 5.14 and higher only
      $@ =~ /nefarious/ and $e = $@;
    }
    die $e if defined $e
 }
</code></pre>
<p> There are some different considerations for each form: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>String eval</dt>
<dd> <p> Since the return value of <font SIZE="-1">EXPR</font> is executed as a block within the lexical context of the current Perl program, any outer lexical variables are visible to it, and any package variable settings or subroutine and format definitions remain afterwards. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>Under the &quot;unicode_eval&quot; feature</dt>
<dd> <p> If this feature is enabled (which is the default under a <code>&quot;use 5.16&quot;</code> or higher declaration), <font SIZE="-1">EXPR</font> is considered to be in the same encoding as the surrounding program. Thus if <code>&quot;use utf8&quot;</code> is in effect, the string will be treated as being <font SIZE="-1">UTF-8</font> encoded. Otherwise, the string is considered to be a sequence of independent bytes. Bytes that correspond to ASCII-range code points will have their normal meanings for operators in the string. The treatment of the other bytes depends on if the <code>&quot;&#8216;unicode_strings&quot;&quot;</code> feature is in effect. </p>
<p> In a plain <code>&quot;eval&quot;</code> without an <font SIZE="-1">EXPR</font> argument, being in <code>&quot;use utf8&quot;</code> or not is irrelevant; the UTF-8ness of <code>$_</code> itself determines the behavior. </p>
<p> Any <code>&quot;use utf8&quot;</code> or <code>&quot;no utf8&quot;</code> declarations within the string have no effect, and source filters are forbidden. (<code>&quot;unicode_strings&quot;</code>, however, can appear within the string.) See also the <code>&quot;evalbytes&quot;</code> operator, which works properly with source filters. </p>
<p> Variables defined outside the <code>&quot;eval&quot;</code> and used inside it retain their original UTF-8ness. Everything inside the string follows the normal rules for a Perl program with the given state of <code>&quot;use utf8&quot;</code>. </p>
 </dd>
<dt>Outside the &quot;unicode_eval&quot; feature</dt>
<dd> <p> In this case, the behavior is problematic and is not so easily described. Here are two bugs that cannot easily be fixed without breaking existing programs: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> It can lose track of whether something should be encoded as <font SIZE="-1">UTF-8</font> or not. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Source filters activated within <code>&quot;eval&quot;</code> leak out into whichever file scope is currently being compiled. To give an example with the <font SIZE="-1">CPAN</font> module Semi::Semicolons: </p>
<pre><code> BEGIN { eval &quot;use Semi::Semicolons; # not filtered&quot; }
 # filtered here!
</code></pre>
<p> <code>&quot;evalbytes&quot;</code> fixes that to work the way one would expect: </p>
<pre><code> use feature &quot;evalbytes&quot;;
 BEGIN { evalbytes &quot;use Semi::Semicolons; # filtered&quot; }
 # not filtered
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
</dl>
<dl>
<dd> <p> Problems can arise if the string expands a scalar containing a floating point number. That scalar can expand to letters, such as <code>&quot;NaN&quot;</code> or <code>&quot;Infinity&quot;</code>; or, within the scope of a <code>&quot;use locale&quot;</code>, the decimal point character may be something other than a dot (such as a comma). None of these are likely to parse as you are likely expecting. </p>
<p> You should be especially careful to remember what&#8217;s being looked at when: </p>
<pre><code>    eval $x; # CASE 1
    eval &quot;$x&quot;; # CASE 2
    eval '$x'; # CASE 3
    eval { $x }; # CASE 4
    eval &quot;\$$x++&quot;; # CASE 5
    $$x++; # CASE 6
</code></pre>
<p> Cases 1 and 2 above behave identically: they run the code contained in the variable <code>$x</code>. (Although case 2 has misleading double quotes making the reader wonder what else might be happening (nothing is).) Cases 3 and 4 likewise behave in the same way: they run the code <code>&#8216;$x&#8217;</code>, which does nothing but return the value of <code>$x</code>. (Case 4 is preferred for purely visual reasons, but it also has the advantage of compiling at compile-time instead of at run-time.) Case 5 is a place where normally you <i>would</i> like to use double quotes, except that in this particular situation, you can just use symbolic references instead, as in case 6. </p>
<p> An <code>&quot;eval &#8216;&#8216;&quot;</code> executed within a subroutine defined in the <code>&quot;DB&quot;</code> package doesn&#8217;t see the usual surrounding lexical scope, but rather the scope of the first non-DB piece of code that called it. You don&#8217;t normally need to worry about this unless you are writing a Perl debugger. </p>
<p> The final semicolon, if any, may be omitted from the value of <font SIZE="-1">EXPR.</font> </p>
 </dd></dl>
<dt>Block eval</dt>
<dd> <p> If the code to be executed doesn&#8217;t vary, you may use the eval-BLOCK form to trap run-time errors without incurring the penalty of recompiling each time. The error, if any, is still returned in <code>$@</code>. Examples: </p>
<pre><code>    # make divide-by-zero nonfatal
    eval { $answer = $a / $b; }; warn $@ if $@;
    # same thing, but less efficient
    eval '$answer = $a / $b'; warn $@ if $@;
    # a compile-time error
    eval { $answer = }; # WRONG
    # a run-time error
    eval '$answer ='; # sets $@
</code></pre>
<p> If you want to trap errors when loading an <font SIZE="-1">XS</font> module, some problems with the binary interface (such as Perl version skew) may be fatal even with <code>&quot;eval&quot;</code> unless <code>$ENV{PERL_DL_NONLAZY}</code> is set. See perlrun. </p>
<p> Using the <code>&quot;eval {}&quot;</code> form as an exception trap in libraries does have some issues. Due to the current arguably broken state of <code>&quot;__DIE__&quot;</code> hooks, you may wish not to trigger any <code>&quot;__DIE__&quot;</code> hooks that user code may have installed. You can use the <code>&quot;local $SIG{__DIE__}&quot;</code> construct for this purpose, as this example shows: </p>
<pre><code>    # a private exception trap for divide-by-zero
    eval { local $SIG{'__DIE__'}; $answer = $a / $b; };
    warn $@ if $@;
</code></pre>
<p> This is especially significant, given that <code>&quot;__DIE__&quot;</code> hooks can call <code>&quot;die&quot;</code> again, which has the effect of changing their error messages: </p>
<pre><code>    # __DIE__ hooks may modify error messages
    {
       local $SIG{'__DIE__'} =
              sub { (my $x = $_[0]) =~ s/foo/bar/g; die $x };
       eval { die &quot;foo lives here&quot; };
       print $@ if $@; # prints &quot;bar lives here&quot;
    }
</code></pre>
<p> Because this promotes action at a distance, this counterintuitive behavior may be fixed in a future release. </p>
<p> <code>&quot;eval BLOCK&quot;</code> does <i>not</i> count as a loop, so the loop control statements <code>&quot;next&quot;</code>, <code>&quot;last&quot;</code>, or <code>&quot;redo&quot;</code> cannot be used to leave or restart the block. </p>
<p> The final semicolon, if any, may be omitted from within the <font SIZE="-1">BLOCK.</font> </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>evalbytes <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>evalbytes</dt>
<dd> <p> This function is similar to a string eval, except it always parses its argument (or <code>$_</code> if <font SIZE="-1">EXPR</font> is omitted) as a string of independent bytes. </p>
<p> If called when <code>&quot;use utf8&quot;</code> is in effect, the string will be assumed to be encoded in <font SIZE="-1">UTF-8,</font> and <code>&quot;evalbytes&quot;</code> will make a temporary copy to work from, downgraded to non-UTF-8. If this is not possible (because one or more characters in it require <font SIZE="-1">UTF-8</font>), the <code>&quot;evalbytes&quot;</code> will fail with the error stored in <code>$@</code>. </p>
<p> Bytes that correspond to ASCII-range code points will have their normal meanings for operators in the string. The treatment of the other bytes depends on if the <code>&quot;&#8216;unicode_strings&quot;&quot;</code> feature is in effect. </p>
<p> Of course, variables that are <font SIZE="-1">UTF-8</font> and are referred to in the string retain that: </p>
<pre><code> my $a = &quot;\x{100}&quot;;
 evalbytes 'print ord $a, &quot;\n&quot;';
</code></pre>
<p> prints </p>
<pre><code> 256
</code></pre>
<p> and <code>$@</code> is empty. </p>
<p> Source filters activated within the evaluated code apply to the code itself. </p>
<p> <code>&quot;evalbytes&quot;</code> is available starting in Perl v5.16. To access it, you must say <code>&quot;CORE::evalbytes&quot;</code>, but you can omit the <code>&quot;CORE::&quot;</code> if the <code>&quot;evalbytes&quot;</code> feature is enabled. This is enabled automatically with a <code>&quot;use v5.16&quot;</code> (or higher) declaration in the current scope. </p>
 </dd>
<dt>exec <font SIZE="-1">LIST</font></dt>
<dd>  </dd>
<dt>exec <font SIZE="-1">PROGRAM LIST</font></dt>
<dd> <p> The <code>&quot;exec&quot;</code> function executes a system command <i>and never returns</i>; use <code>&quot;system&quot;</code> instead of <code>&quot;exec&quot;</code> if you want it to return. It fails and returns false only if the command does not exist <i>and</i> it is executed directly instead of via your system&#8217;s command shell (see below). </p>
<p> Since it&#8217;s a common mistake to use <code>&quot;exec&quot;</code> instead of <code>&quot;system&quot;</code>, Perl warns you if <code>&quot;exec&quot;</code> is called in void context and if there is a following statement that isn&#8217;t <code>&quot;die&quot;</code>, <code>&quot;warn&quot;</code>, or <code>&quot;exit&quot;</code> (if warnings are enabled---but you always do that, right?). If you <i>really</i> want to follow an <code>&quot;exec&quot;</code> with some other statement, you can use one of these styles to avoid the warning: </p>
<pre><code>    exec ('foo') or print STDERR &quot;couldn't exec foo: $!&quot;;
    { exec ('foo') }; print STDERR &quot;couldn't exec foo: $!&quot;;
</code></pre>
<p> If there is more than one argument in <font SIZE="-1">LIST,</font> this calls <code><a href="/docs/linux/man/3-execvp/">execvp</a></code>(3) with the arguments in <font SIZE="-1">LIST.</font> If there is only one element in <font SIZE="-1">LIST,</font> the argument is checked for shell metacharacters, and if there are any, the entire argument is passed to the system&#8217;s command shell for parsing (this is <code>&quot;/bin/sh -c&quot;</code> on Unix platforms, but varies on other platforms). If there are no shell metacharacters in the argument, it is split into words and passed directly to <code>&quot;execvp&quot;</code>, which is more efficient. Examples: </p>
<pre><code>    exec '/bin/echo', 'Your arguments are: ', @ARGV;
    exec &quot;sort $outfile | uniq&quot;;
</code></pre>
<p> If you don&#8217;t really want to execute the first argument, but want to lie to the program you are executing about its own name, you can specify the program you actually want to run as an ``indirect object&#8217;&#8216; (without a comma) in front of the <font SIZE="-1">LIST,</font> as in <code>&quot;exec PROGRAM LIST&quot;</code>. (This always forces interpretation of the <font SIZE="-1">LIST</font> as a multivalued list, even if there is only a single scalar in the list.) Example: </p>
<pre><code>    my $shell = '/bin/csh';
    exec $shell '-sh'; # pretend it's a login shell
</code></pre>
<p> or, more directly, </p>
<pre><code>    exec {'/bin/csh'} '-sh'; # pretend it's a login shell
</code></pre>
<p> When the arguments get executed via the system shell, results are subject to its quirks and capabilities. See ```STRING`&#8216;&#8216; in perlop for details. </p>
<p> Using an indirect object with <code>&quot;exec&quot;</code> or <code>&quot;system&quot;</code> is also more secure. This usage (which also works fine with <code>&quot;system&quot;</code>) forces interpretation of the arguments as a multivalued list, even if the list had just one argument. That way you&#8217;re safe from the shell expanding wildcards or splitting up words with whitespace in them. </p>
<pre><code>    my @args = ( &quot;echo surprise&quot; );
    exec @args; # subject to shell escapes
                                # if @args == 1
    exec { $args[0] } @args; # safe even with one-arg list
</code></pre>
<p> The first version, the one without the indirect object, ran the <i>echo</i> program, passing it <code>&quot;surprise&quot;</code> an argument. The second version didn&#8217;t; it tried to run a program named <i>``echo surprise&#8217;&#8216;</i>, didn&#8217;t find it, and set <code>$?</code> to a non-zero value indicating failure. </p>
<p> On Windows, only the <code>&quot;exec PROGRAM LIST&quot;</code> indirect object syntax will reliably avoid using the shell; <code>&quot;exec LIST&quot;</code>, even with more than one element, will fall back to the shell if the first spawn fails. </p>
<p> Perl attempts to flush all files opened for output before the exec, but this may not be supported on some platforms (see perlport). To be safe, you may need to set <code>$|</code> (<code>$AUTOFLUSH</code> in English) or call the <code>&quot;autoflush&quot;</code> method of <code>&quot;IO::Handle&quot;</code> on any open handles to avoid lost output. </p>
<p> Note that <code>&quot;exec&quot;</code> will not call your <code>&quot;END&quot;</code> blocks, nor will it invoke <code>&quot;DESTROY&quot;</code> methods on your objects. </p>
<p> Portability issues: ``exec&#8217;&#8216; in perlport. </p>
 </dd>
<dt>exists <font SIZE="-1">EXPR</font></dt>
<dd> <p> Given an expression that specifies an element of a hash, returns true if the specified element in the hash has ever been initialized, even if the corresponding value is undefined. </p>
<pre><code>    print &quot;Exists\n&quot; if exists $hash{$key};
    print &quot;Defined\n&quot; if defined $hash{$key};
    print &quot;True\n&quot; if $hash{$key};
</code></pre>
<p> exists may also be called on array elements, but its behavior is much less obvious and is strongly tied to the use of <code>&quot;delete&quot;</code> on arrays. </p>
<p> <font SIZE="-1"><code>WARNING:</code></font> Calling <code>&quot;exists&quot;</code> on array values is strongly discouraged. The notion of deleting or checking the existence of Perl array elements is not conceptually coherent, and can lead to surprising behavior. </p>
<pre><code>    print &quot;Exists\n&quot; if exists $array[$index];
    print &quot;Defined\n&quot; if defined $array[$index];
    print &quot;True\n&quot; if $array[$index];
</code></pre>
<p> A hash or array element can be true only if it&#8217;s defined and defined only if it exists, but the reverse doesn&#8217;t necessarily hold true. </p>
<p> Given an expression that specifies the name of a subroutine, returns true if the specified subroutine has ever been declared, even if it is undefined. Mentioning a subroutine name for exists or defined does not count as declaring it. Note that a subroutine that does not exist may still be callable: its package may have an <code>&quot;AUTOLOAD&quot;</code> method that makes it spring into existence the first time that it is called; see perlsub. </p>
<pre><code>    print &quot;Exists\n&quot; if exists &amp;subroutine;
    print &quot;Defined\n&quot; if defined &amp;subroutine;
</code></pre>
<p> Note that the <font SIZE="-1">EXPR</font> can be arbitrarily complicated as long as the final operation is a hash or array key lookup or subroutine name: </p>
<pre><code>    if (exists $ref-&gt;{A}-&gt;{B}-&gt;{$key}) { }
    if (exists $hash{A}{B}{$key}) { }
    if (exists $ref-&gt;{A}-&gt;{B}-&gt;[$ix]) { }
    if (exists $hash{A}{B}[$ix]) { }
    if (exists &amp;{$ref-&gt;{A}{B}{$key}}) { }
</code></pre>
<p> Although the most deeply nested array or hash element will not spring into existence just because its existence was tested, any intervening ones will. Thus <code>&quot;$ref-&gt;{&quot;A&quot;}&quot;</code> and <code>&quot;$ref-&gt;{&quot;A&quot;}-&gt;{&quot;B&quot;}&quot;</code> will spring into existence due to the existence test for the <code>$key</code> element above. This happens anywhere the arrow operator is used, including even here: </p>
<pre><code>    undef $ref;
    if (exists $ref-&gt;{&quot;Some key&quot;}) { }
    print $ref; # prints HASH(0x80d3d5c)
</code></pre>
<p> Use of a subroutine call, rather than a subroutine name, as an argument to <code>&quot;exists&quot;</code> is an error. </p>
<pre><code>    exists &amp;sub; # OK
    exists &amp;sub(); # Error
</code></pre>
 </dd>
<dt>exit <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>exit</dt>
<dd> <p> Evaluates <font SIZE="-1">EXPR</font> and exits immediately with that value. Example: </p>
<pre><code>    my $ans = &lt;STDIN&gt;;
    exit 0 if $ans =~ /^[Xx]/;
</code></pre>
<p> See also <code>&quot;die&quot;</code>. If <font SIZE="-1">EXPR</font> is omitted, exits with <code>0</code> status. The only universally recognized values for <font SIZE="-1">EXPR</font> are <code>0</code> for success and <code>1</code> for error; other values are subject to interpretation depending on the environment in which the Perl program is running. For example, exiting 69 (<font SIZE="-1">EX_UNAVAILABLE</font>) from a <i>sendmail</i> incoming-mail filter will cause the mailer to return the item undelivered, but that&#8217;s not true everywhere. </p>
<p> Don&#8217;t use <code>&quot;exit&quot;</code> to abort a subroutine if there&#8217;s any chance that someone might want to trap whatever error happened. Use <code>&quot;die&quot;</code> instead, which can be trapped by an <code>&quot;eval&quot;</code>. </p>
<p> The <code>&quot;exit&quot;</code> function does not always exit immediately. It calls any defined <code>&quot;END&quot;</code> routines first, but these <code>&quot;END&quot;</code> routines may not themselves abort the exit. Likewise any object destructors that need to be called are called before the real exit. <code>&quot;END&quot;</code> routines and destructors can change the exit status by modifying <code>$?</code>. If this is a problem, you can call <code>&quot;POSIX::_exit($status)&quot;</code> to avoid <code>&quot;END&quot;</code> and destructor processing. See perlmod for details. </p>
<p> Portability issues: ``exit&#8217;&#8216; in perlport. </p>
 </dd>
<dt>exp <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>exp</dt>
<dd> <p> Returns <i>e</i> (the natural logarithm base) to the power of <font SIZE="-1">EXPR.</font> If <font SIZE="-1">EXPR</font> is omitted, gives <code>&quot;exp($_)&quot;</code>. </p>
 </dd>
<dt>fc <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>fc</dt>
<dd> <p> Returns the casefolded version of <font SIZE="-1">EXPR.</font> This is the internal function implementing the <code>&quot;\F&quot;</code> escape in double-quoted strings. </p>
<p> Casefolding is the process of mapping strings to a form where case differences are erased; comparing two strings in their casefolded form is effectively a way of asking if two strings are equal, regardless of case. </p>
<p> Roughly, if you ever found yourself writing this </p>
<pre><code>    lc($this) eq lc($that) # Wrong!
        # or
    uc($this) eq uc($that) # Also wrong!
        # or
    $this =~ /^\Q$that\E\z/i # Right!
</code></pre>
<p> Now you can write </p>
<pre><code>    fc($this) eq fc($that)
</code></pre>
<p> And get the correct results. </p>
<p> Perl only implements the full form of casefolding, but you can access the simple folds using &quot;<code>casefold()</code>&quot; in Unicode::UCD and &quot;<code>prop_invmap()</code>&quot; in Unicode::UCD. For further information on casefolding, refer to the Unicode Standard, specifically sections 3.13 <code>&quot;Default Case Operations&quot;</code>, 4.2 <code>&quot;Case-Normative&quot;</code>, and 5.18 <code>&quot;Case Mappings&quot;</code>, available at &lt;<a rel="nofollow" href="http://www.unicode.org/versions/latest/">http://www.unicode.org/versions/latest/</a>&gt;, as well as the Case Charts available at &lt;<a rel="nofollow" href="http://www.unicode.org/charts/case/">http://www.unicode.org/charts/case/</a>&gt;. </p>
<p> If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. </p>
<p> This function behaves the same way under various pragmas, such as within <code>&quot;use feature &#8216;unicode_strings&quot;</code>, as <code>&quot;lc&quot;</code> does, with the single exception of <code>&quot;fc&quot;</code> of <i></i><font SIZE="-1"><i>LATIN CAPITAL LETTER SHARP S</i></font><i></i> (U+1E9E) within the scope of <code>&quot;use locale&quot;</code>. The foldcase of this character would normally be <code>&quot;ss&quot;</code>, but as explained in the <code>&quot;lc&quot;</code> section, case changes that cross the 255/256 boundary are problematic under locales, and are hence prohibited. Therefore, this function under locale returns instead the string <code>&quot;\x{17F}\x{17F}&quot;</code>, which is the <i></i><font SIZE="-1"><i>LATIN SMALL LETTER LONG S</i></font><i></i>. Since that character itself folds to <code>&quot;s&quot;</code>, the string of two of them together should be equivalent to a single U+1E9E when foldcased. </p>
<p> While the Unicode Standard defines two additional forms of casefolding, one for Turkic languages and one that never maps one character into multiple characters, these are not provided by the Perl core. However, the <font SIZE="-1">CPAN</font> module <code>&quot;Unicode::Casing&quot;</code> may be used to provide an implementation. </p>
<p> <code>&quot;fc&quot;</code> is available only if the <code>&quot;fc&quot;</code> feature is enabled or if it is prefixed with <code>&quot;CORE::&quot;</code>. The <code>&quot;fc&quot;</code> feature is enabled automatically with a <code>&quot;use v5.16&quot;</code> (or higher) declaration in the current scope. </p>
 </dd>
<dt>fcntl <font SIZE="-1">FILEHANDLE,FUNCTION,SCALAR</font></dt>
<dd> <p> Implements the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) function. You&#8217;ll probably have to say </p>
<pre><code>    use Fcntl;
</code></pre>
<p> first to get the correct constant definitions. Argument processing and value returned work just like <code>&quot;ioctl&quot;</code> below. For example: </p>
<pre><code>    use Fcntl;
    my $flags = fcntl($filehandle, F_GETFL, 0)
        or die &quot;Can't fcntl F_GETFL: $!&quot;;
</code></pre>
<p> You don&#8217;t have to check for <code>&quot;defined&quot;</code> on the return from <code>&quot;fcntl&quot;</code>. Like <code>&quot;ioctl&quot;</code>, it maps a <code>0</code> return from the system call into <code>&quot;0 but true&quot;</code> in Perl. This string is true in boolean context and <code>0</code> in numeric context. It is also exempt from the normal <code>&quot;Argument &quot;...&quot; isn&#8217;t numeric&quot;</code> warnings on improper numeric conversions. </p>
<p> Note that <code>&quot;fcntl&quot;</code> raises an exception if used on a machine that doesn&#8217;t implement <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). See the Fcntl module or your <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) manpage to learn what functions are available on your system. </p>
<p> Here&#8217;s an example of setting a filehandle named <code>$REMOTE</code> to be non-blocking at the system level. You&#8217;ll have to negotiate <code>$|</code> on your own, though. </p>
<pre><code>    use Fcntl qw(F_GETFL F_SETFL O_NONBLOCK);
    my $flags = fcntl($REMOTE, F_GETFL, 0)
        or die &quot;Can't get flags for the socket: $!\n&quot;;
    fcntl($REMOTE, F_SETFL, $flags | O_NONBLOCK)
        or die &quot;Can't set flags for the socket: $!\n&quot;;
</code></pre>
<p> Portability issues: ``fcntl&#8217;&#8216; in perlport. </p>
 </dd>
<dt>__FILE__</dt>
<dd> <p> A special token that returns the name of the file in which it occurs. </p>
 </dd>
<dt>fileno <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>fileno <font SIZE="-1">DIRHANDLE</font></dt>
<dd> <p> Returns the file descriptor for a filehandle or directory handle, or undefined if the filehandle is not open. If there is no real file descriptor at the <font SIZE="-1">OS</font> level, as can happen with filehandles connected to memory objects via <code>&quot;open&quot;</code> with a reference for the third argument, -1 is returned. </p>
<p> This is mainly useful for constructing bitmaps for <code>&quot;select&quot;</code> and low-level <font SIZE="-1">POSIX</font> tty-handling operations. If <font SIZE="-1">FILEHANDLE</font> is an expression, the value is taken as an indirect filehandle, generally its name. </p>
<p> You can use this to find out whether two handles refer to the same underlying descriptor: </p>
<pre><code>    if (fileno($this) != -1 &amp;&amp; fileno($this) == fileno($that)) {
        print &quot;\$this and \$that are dups\n&quot;;
    } elsif (fileno($this) != -1 &amp;&amp; fileno($that) != -1) {
        print &quot;\$this and \$that have different &quot; .
            &quot;underlying file descriptors\n&quot;;
    } else {
        print &quot;At least one of \$this and \$that does &quot; .
            &quot;not have a real file descriptor\n&quot;;
    }
</code></pre>
<p> The behavior of <code>&quot;fileno&quot;</code> on a directory handle depends on the operating system. On a system with <code><a href="/docs/linux/man/3-dirfd/">dirfd</a></code>(3) or similar, <code>&quot;fileno&quot;</code> on a directory handle returns the underlying file descriptor associated with the handle; on systems with no such support, it returns the undefined value, and sets <code>$!</code> (errno). </p>
 </dd>
<dt>flock <font SIZE="-1">FILEHANDLE,OPERATION</font></dt>
<dd> <p> Calls <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2), or an emulation of it, on <font SIZE="-1">FILEHANDLE.</font> Returns true for success, false on failure. Produces a fatal error if used on a machine that doesn&#8217;t implement <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) locking, or <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3). <code>&quot;flock&quot;</code> is Perl&#8217;s portable file-locking interface, although it locks entire files only, not records. </p>
<p> Two potentially non-obvious but traditional <code>&quot;flock&quot;</code> semantics are that it waits indefinitely until the lock is granted, and that its locks are <code>merely advisory</code>. Such discretionary locks are more flexible, but offer fewer guarantees. This means that programs that do not also use <code>&quot;flock&quot;</code> may modify files locked with <code>&quot;flock&quot;</code>. See perlport, your port&#8217;s specific documentation, and your system-specific local manpages for details. It&#8217;s best to assume traditional behavior if you&#8217;re writing portable programs. (But if you&#8217;re not, you should as always feel perfectly free to write for your own system&#8217;s idiosyncrasies (sometimes called ``features&#8217;&#8216;). Slavish adherence to portability concerns shouldn&#8217;t get in the way of your getting your job done.) </p>
<p> <font SIZE="-1">OPERATION</font> is one of <font SIZE="-1">LOCK_SH, LOCK_EX,</font> or <font SIZE="-1">LOCK_UN,</font> possibly combined with <font SIZE="-1">LOCK_NB.</font> These constants are traditionally valued 1, 2, 8 and 4, but you can use the symbolic names if you import them from the Fcntl module, either individually, or as a group using the <code>&quot;:flock&quot;</code> tag. <font SIZE="-1">LOCK_SH</font> requests a shared lock, <font SIZE="-1">LOCK_EX</font> requests an exclusive lock, and <font SIZE="-1">LOCK_UN</font> releases a previously requested lock. If <font SIZE="-1">LOCK_NB</font> is bitwise-or&#8217;ed with <font SIZE="-1">LOCK_SH</font> or <font SIZE="-1">LOCK_EX,</font> then <code>&quot;flock&quot;</code> returns immediately rather than blocking waiting for the lock; check the return status to see if you got it. </p>
<p> To avoid the possibility of miscoordination, Perl now flushes <font SIZE="-1">FILEHANDLE</font> before locking or unlocking it. </p>
<p> Note that the emulation built with <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3) doesn&#8217;t provide shared locks, and it requires that <font SIZE="-1">FILEHANDLE</font> be open with write intent. These are the semantics that <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3) implements. Most if not all systems implement <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3) in terms of <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) locking, though, so the differing semantics shouldn&#8217;t bite too many people. </p>
<p> Note that the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) emulation of <code><a href="/docs/linux/man/3-flock/">flock</a></code>(3) requires that <font SIZE="-1">FILEHANDLE</font> be open with read intent to use <font SIZE="-1">LOCK_SH</font> and requires that it be open with write intent to use <font SIZE="-1">LOCK_EX.</font> </p>
<p> Note also that some versions of <code>&quot;flock&quot;</code> cannot lock things over the network; you would need to use the more system-specific <code>&quot;fcntl&quot;</code> for that. If you like you can force Perl to ignore your system&#8217;s <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) function, and so provide its own <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)-based emulation, by passing the switch <code>&quot;-Ud_flock&quot;</code> to the <i>Configure</i> program when you configure and build a new Perl. </p>
<p> Here&#8217;s a mailbox appender for <font SIZE="-1">BSD</font> systems. </p>
<pre><code>    # import LOCK_* and SEEK_END constants
    use Fcntl qw(:flock SEEK_END);
    sub lock {
        my ($fh) = @_;
        flock($fh, LOCK_EX) or die &quot;Cannot lock mailbox - $!\n&quot;;
        # and, in case we're running on a very old UNIX
        # variant without the modern O_APPEND semantics...
        seek($fh, 0, SEEK_END) or die &quot;Cannot seek - $!\n&quot;;
    }
    sub unlock {
        my ($fh) = @_;
        flock($fh, LOCK_UN) or die &quot;Cannot unlock mailbox - $!\n&quot;;
    }
    open(my $mbox, &quot;&gt;&gt;&quot;, &quot;/usr/spool/mail/$ENV{'USER'}&quot;)
        or die &quot;Can't open mailbox: $!&quot;;
    lock($mbox);
    print $mbox $msg,&quot;\n\n&quot;;
    unlock($mbox);
</code></pre>
<p> On systems that support a real <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2), locks are inherited across <code>&quot;fork&quot;</code> calls, whereas those that must resort to the more capricious <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) function lose their locks, making it seriously harder to write servers. </p>
<p> See also DB_File for other <code>&quot;flock&quot;</code> examples. </p>
<p> Portability issues: ``flock&#8217;&#8216; in perlport. </p>
 </dd>
<dt>fork</dt>
<dd> <p> Does a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) system call to create a new process running the same program at the same point. It returns the child pid to the parent process, <code>0</code> to the child process, or <code>&quot;undef&quot;</code> if the fork is unsuccessful. File descriptors (and sometimes locks on those descriptors) are shared, while everything else is copied. On most systems supporting <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), great care has gone into making it extremely efficient (for example, using copy-on-write technology on data pages), making it the dominant paradigm for multitasking over the last few decades. </p>
<p> Perl attempts to flush all files opened for output before forking the child process, but this may not be supported on some platforms (see perlport). To be safe, you may need to set <code>$|</code> (<code>$AUTOFLUSH</code> in English) or call the <code>&quot;autoflush&quot;</code> method of <code>&quot;IO::Handle&quot;</code> on any open handles to avoid duplicate output. </p>
<p> If you <code>&quot;fork&quot;</code> without ever waiting on your children, you will accumulate zombies. On some systems, you can avoid this by setting <code>$SIG{CHLD}</code> to <code>&quot;IGNORE&quot;</code>. See also perlipc for more examples of forking and reaping moribund children. </p>
<p> Note that if your forked child inherits system file descriptors like <font SIZE="-1">STDIN</font> and <font SIZE="-1">STDOUT</font> that are actually connected by a pipe or socket, even if you exit, then the remote server (such as, say, a <font SIZE="-1">CGI</font> script or a backgrounded job launched from a remote shell) won&#8217;t think you&#8217;re done. You should reopen those to <i>/dev/null</i> if it&#8217;s any issue. </p>
<p> On some platforms such as Windows, where the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) system call is not available, Perl can be built to emulate <code>&quot;fork&quot;</code> in the Perl interpreter. The emulation is designed, at the level of the Perl program, to be as compatible as possible with the ``Unix&#8217;&#8216; <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). However it has limitations that have to be considered in code intended to be portable. See perlfork for more details. </p>
<p> Portability issues: ``fork&#8217;&#8216; in perlport. </p>
 </dd>
<dt>format</dt>
<dd> <p> Declare a picture format for use by the <code>&quot;write&quot;</code> function. For example: </p>
<pre><code>    format Something =
        Test: @&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; @||||| @&gt;&gt;&gt;&gt;&gt;
              $str, $%, '$' . int($num)
    .
    $str = &quot;widget&quot;;
    $num = $cost/$quantity;
    $~ = 'Something';
    write;
</code></pre>
<p> See perlform for many details and examples. </p>
 </dd>
<dt>formline <font SIZE="-1">PICTURE,LIST</font></dt>
<dd> <p> This is an internal function used by <code>&quot;format&quot;</code>s, though you may call it, too. It formats (see perlform) a list of values according to the contents of <font SIZE="-1">PICTURE,</font> placing the output into the format output accumulator, <code>$^A</code> (or <code>$ACCUMULATOR</code> in English). Eventually, when a <code>&quot;write&quot;</code> is done, the contents of <code>$^A</code> are written to some filehandle. You could also read <code>$^A</code> and then set <code>$^A</code> back to <code>&quot;&quot;</code>. Note that a format typically does one <code>&quot;formline&quot;</code> per line of form, but the <code>&quot;formline&quot;</code> function itself doesn&#8217;t care how many newlines are embedded in the <font SIZE="-1">PICTURE.</font> This means that the <code>&quot;~&quot;</code> and <code>&quot;~~&quot;</code> tokens treat the entire <font SIZE="-1">PICTURE</font> as a single line. You may therefore need to use multiple formlines to implement a single record format, just like the <code>&quot;format&quot;</code> compiler. </p>
<p> Be careful if you put double quotes around the picture, because an <code>&quot;@&quot;</code> character may be taken to mean the beginning of an array name. <code>&quot;formline&quot;</code> always returns true. See perlform for other examples. </p>
<p> If you are trying to use this instead of <code>&quot;write&quot;</code> to capture the output, you may find it easier to open a filehandle to a scalar (<code>&quot;open my $fh, &quot;&gt;&quot;, \$output&quot;</code>) and write to that instead. </p>
 </dd>
<dt>getc <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>getc</dt>
<dd> <p> Returns the next character from the input file attached to <font SIZE="-1">FILEHANDLE,</font> or the undefined value at end of file or if there was an error (in the latter case <code>$!</code> is set). If <font SIZE="-1">FILEHANDLE</font> is omitted, reads from <font SIZE="-1">STDIN.</font> This is not particularly efficient. However, it cannot be used by itself to fetch single characters without waiting for the user to hit enter. For that, try something more like: </p>
<pre><code>    if ($BSD_STYLE) {
        system &quot;stty cbreak &lt;/dev/tty &gt;/dev/tty 2&gt;&amp;1&quot;;
    }
    else {
        system &quot;stty&quot;, '-icanon', 'eol', &quot;\001&quot;;
    }
    my $key = getc(STDIN);
    if ($BSD_STYLE) {
        system &quot;stty -cbreak &lt;/dev/tty &gt;/dev/tty 2&gt;&amp;1&quot;;
    }
    else {
        system 'stty', 'icanon', 'eol', '^@'; # ASCII NUL
    }
    print &quot;\n&quot;;
</code></pre>
<p> Determination of whether <code>$BSD_STYLE</code> should be set is left as an exercise to the reader. </p>
<p> The <code>&quot;POSIX::getattr&quot;</code> function can do this more portably on systems purporting <font SIZE="-1">POSIX</font> compliance. See also the <code>&quot;Term::ReadKey&quot;</code> module on <font SIZE="-1">CPAN.</font> </p>
 </dd>
<dt>getlogin</dt>
<dd> <p> This implements the C library function of the same name, which on most systems returns the current login from <i>/etc/utmp</i>, if any. If it returns the empty string, use <code>&quot;getpwuid&quot;</code>. </p>
<pre><code>    my $login = getlogin || getpwuid($&lt;) || &quot;Kilroy&quot;;
</code></pre>
<p> Do not consider <code>&quot;getlogin&quot;</code> for authentication: it is not as secure as <code>&quot;getpwuid&quot;</code>. </p>
<p> Portability issues: ``getlogin&#8217;&#8216; in perlport. </p>
 </dd>
<dt>getpeername <font SIZE="-1">SOCKET</font></dt>
<dd> <p> Returns the packed sockaddr address of the other end of the <font SIZE="-1">SOCKET</font> connection. </p>
<pre><code>    use Socket;
    my $hersockaddr = getpeername($sock);
    my ($port, $iaddr) = sockaddr_in($hersockaddr);
    my $herhostname = gethostbyaddr($iaddr, AF_INET);
    my $herstraddr = inet_ntoa($iaddr);
</code></pre>
 </dd>
<dt>getpgrp <font SIZE="-1">PID</font></dt>
<dd> <p> Returns the current process group for the specified <font SIZE="-1">PID.</font> Use a <font SIZE="-1">PID</font> of <code>0</code> to get the current process group for the current process. Will raise an exception if used on a machine that doesn&#8217;t implement <code><a href="/docs/linux/man/2-getpgrp/">getpgrp</a></code>(2). If <font SIZE="-1">PID</font> is omitted, returns the process group of the current process. Note that the <font SIZE="-1">POSIX</font> version of <code>&quot;getpgrp&quot;</code> does not accept a <font SIZE="-1">PID</font> argument, so only <code>&quot;PID==0&quot;</code> is truly portable. </p>
<p> Portability issues: ``getpgrp&#8217;&#8216; in perlport. </p>
 </dd>
<dt>getppid</dt>
<dd> <p> Returns the process id of the parent process. </p>
<p> Note for Linux users: Between v5.8.1 and v5.16.0 Perl would work around non-POSIX thread semantics the minority of Linux systems (and Debian GNU/kFreeBSD systems) that used LinuxThreads, this emulation has since been removed. See the documentation for $$ for details. </p>
<p> Portability issues: ``getppid&#8217;&#8216; in perlport. </p>
 </dd>
<dt>getpriority <font SIZE="-1">WHICH,WHO</font></dt>
<dd> <p> Returns the current priority for a process, a process group, or a user. (See <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2).) Will raise a fatal exception if used on a machine that doesn&#8217;t implement <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2). </p>
<p> <code>&quot;WHICH&quot;</code> can be any of <code>&quot;PRIO_PROCESS&quot;</code>, <code>&quot;PRIO_PGRP&quot;</code> or <code>&quot;PRIO_USER&quot;</code> imported from ``<font SIZE="-1">RESOURCE CONSTANTS&#8217;&#8216;</font> in <font SIZE="-1">POSIX</font>. </p>
<p> Portability issues: ``getpriority&#8217;&#8216; in perlport. </p>
 </dd>
<dt>getpwnam <font SIZE="-1">NAME</font></dt>
<dd>  </dd>
<dt>getgrnam <font SIZE="-1">NAME</font></dt>
<dd>  </dd>
<dt>gethostbyname <font SIZE="-1">NAME</font></dt>
<dd>  </dd>
<dt>getnetbyname <font SIZE="-1">NAME</font></dt>
<dd>  </dd>
<dt>getprotobyname <font SIZE="-1">NAME</font></dt>
<dd>  </dd>
<dt>getpwuid <font SIZE="-1">UID</font></dt>
<dd>  </dd>
<dt>getgrgid <font SIZE="-1">GID</font></dt>
<dd>  </dd>
<dt>getservbyname <font SIZE="-1">NAME,PROTO</font></dt>
<dd>  </dd>
<dt>gethostbyaddr <font SIZE="-1">ADDR,ADDRTYPE</font></dt>
<dd>  </dd>
<dt>getnetbyaddr <font SIZE="-1">ADDR,ADDRTYPE</font></dt>
<dd>  </dd>
<dt>getprotobynumber <font SIZE="-1">NUMBER</font></dt>
<dd>  </dd>
<dt>getservbyport <font SIZE="-1">PORT,PROTO</font></dt>
<dd>  </dd>
<dt>getpwent</dt>
<dd>  </dd>
<dt>getgrent</dt>
<dd>  </dd>
<dt>gethostent</dt>
<dd>  </dd>
<dt>getnetent</dt>
<dd>  </dd>
<dt>getprotoent</dt>
<dd>  </dd>
<dt>getservent</dt>
<dd>  </dd>
<dt>setpwent</dt>
<dd>  </dd>
<dt>setgrent</dt>
<dd>  </dd>
<dt>sethostent <font SIZE="-1">STAYOPEN</font></dt>
<dd>  </dd>
<dt>setnetent <font SIZE="-1">STAYOPEN</font></dt>
<dd>  </dd>
<dt>setprotoent <font SIZE="-1">STAYOPEN</font></dt>
<dd>  </dd>
<dt>setservent <font SIZE="-1">STAYOPEN</font></dt>
<dd>  </dd>
<dt>endpwent</dt>
<dd>  </dd>
<dt>endgrent</dt>
<dd>  </dd>
<dt>endhostent</dt>
<dd>  </dd>
<dt>endnetent</dt>
<dd>  </dd>
<dt>endprotoent</dt>
<dd>  </dd>
<dt>endservent</dt>
<dd> <p> These routines are the same as their counterparts in the system C library. In list context, the return values from the various get routines are as follows: </p>
<pre><code> # 0 1 2 3 4
 my ( $name, $passwd, $gid, $members ) = getgr*
 my ( $name, $aliases, $addrtype, $net ) = getnet*
 my ( $name, $aliases, $port, $proto ) = getserv*
 my ( $name, $aliases, $proto ) = getproto*
 my ( $name, $aliases, $addrtype, $length, @addrs ) = gethost*
 my ( $name, $passwd, $uid, $gid, $quota,
    $comment, $gcos, $dir, $shell, $expire ) = getpw*
 # 5 6 7 8 9
</code></pre>
<p> (If the entry doesn&#8217;t exist, the return value is a single meaningless true value.) </p>
<p> The exact meaning of the <code>$gcos</code> field varies but it usually contains the real name of the user (as opposed to the login name) and other information pertaining to the user. Beware, however, that in many system users are able to change this information and therefore it cannot be trusted and therefore the <code>$gcos</code> is tainted (see perlsec). The <code>$passwd</code> and <code>$shell</code>, user&#8217;s encrypted password and login shell, are also tainted, for the same reason. </p>
<p> In scalar context, you get the name, unless the function was a lookup by name, in which case you get the other thing, whatever it is. (If the entry doesn&#8217;t exist you get the undefined value.) For example: </p>
<pre><code>    my $uid = getpwnam($name);
    my $name = getpwuid($num);
    my $name = getpwent();
    my $gid = getgrnam($name);
    my $name = getgrgid($num);
    my $name = getgrent();
    # etc.
</code></pre>
<p> In <i>getpw*()</i> the fields <code>$quota</code>, <code>$comment</code>, and <code>$expire</code> are special in that they are unsupported on many systems. If the <code>$quota</code> is unsupported, it is an empty scalar. If it is supported, it usually encodes the disk quota. If the <code>$comment</code> field is unsupported, it is an empty scalar. If it is supported it usually encodes some administrative comment about the user. In some systems the <code>$quota</code> field may be <code>$change</code> or <code>$age</code>, fields that have to do with password aging. In some systems the <code>$comment</code> field may be <code>$class</code>. The <code>$expire</code> field, if present, encodes the expiration period of the account or the password. For the availability and the exact meaning of these fields in your system, please consult <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3) and your system&#8217;s <i>pwd.h</i> file. You can also find out from within Perl what your <code>$quota</code> and <code>$comment</code> fields mean and whether you have the <code>$expire</code> field by using the <code>&quot;Config&quot;</code> module and the values <code>&quot;d_pwquota&quot;</code>, <code>&quot;d_pwage&quot;</code>, <code>&quot;d_pwchange&quot;</code>, <code>&quot;d_pwcomment&quot;</code>, and <code>&quot;d_pwexpire&quot;</code>. Shadow password files are supported only if your vendor has implemented them in the intuitive fashion that calling the regular C library routines gets the shadow versions if you&#8217;re running under privilege or if there exists the <code><a href="/docs/linux/man/3-shadow/">shadow</a></code>(3) functions as found in System V (this includes Solaris and Linux). Those systems that implement a proprietary shadow password facility are unlikely to be supported. </p>
<p> The <code>$members</code> value returned by <i>getgr*()</i> is a space-separated list of the login names of the members of the group. </p>
<p> For the <i>gethost*()</i> functions, if the <code>&quot;h_errno&quot;</code> variable is supported in C, it will be returned to you via <code>$?</code> if the function call fails. The <code>@addrs</code> value returned by a successful call is a list of raw addresses returned by the corresponding library call. In the Internet domain, each address is four bytes long; you can unpack it by saying something like: </p>
<pre><code>    my ($w,$x,$y,$z) = unpack('W4',$addr[0]);
</code></pre>
<p> The Socket library makes this slightly easier: </p>
<pre><code>    use Socket;
    my $iaddr = inet_aton(&quot;127.1&quot;); # or whatever address
    my $name = gethostbyaddr($iaddr, AF_INET);
    # or going the other way
    my $straddr = inet_ntoa($iaddr);
</code></pre>
<p> In the opposite way, to resolve a hostname to the <font SIZE="-1">IP</font> address you can write this: </p>
<pre><code>    use Socket;
    my $packed_ip = gethostbyname(&quot;www.perl.org&quot;);
    my $ip_address;
    if (defined $packed_ip) {
        $ip_address = inet_ntoa($packed_ip);
    }
</code></pre>
<p> Make sure <code>&quot;gethostbyname&quot;</code> is called in <font SIZE="-1">SCALAR</font> context and that its return value is checked for definedness. </p>
<p> The <code>&quot;getprotobynumber&quot;</code> function, even though it only takes one argument, has the precedence of a list operator, so beware: </p>
<pre><code>    getprotobynumber $number eq 'icmp' # WRONG
    getprotobynumber($number eq 'icmp') # actually means this
    getprotobynumber($number) eq 'icmp' # better this way
</code></pre>
<p> If you get tired of remembering which element of the return list contains which return value, by-name interfaces are provided in standard modules: <code>&quot;File::stat&quot;</code>, <code>&quot;Net::hostent&quot;</code>, <code>&quot;Net::netent&quot;</code>, <code>&quot;Net::protoent&quot;</code>, <code>&quot;Net::servent&quot;</code>, <code>&quot;Time::gmtime&quot;</code>, <code>&quot;Time::localtime&quot;</code>, and <code>&quot;User::grent&quot;</code>. These override the normal built-ins, supplying versions that return objects with the appropriate names for each field. For example: </p>
<pre><code>   use File::stat;
   use User::pwent;
   my $is_his = (stat($filename)-&gt;uid == pwent($whoever)-&gt;uid);
</code></pre>
<p> Even though it looks as though they&#8217;re the same method calls (uid), they aren&#8217;t, because a <code>&quot;File::stat&quot;</code> object is different from a <code>&quot;User::pwent&quot;</code> object. </p>
<p> Many of these functions are not safe in a multi-threaded environment where more than one thread can be using them. In particular, functions like <code>&quot;getpwent()&quot;</code> iterate per-process and not per-thread, so if two threads are simultaneously iterating, neither will get all the records. </p>
<p> Some systems have thread-safe versions of some of the functions, such as <code>&quot;getpwnam_r()&quot;</code> instead of <code>&quot;getpwnam()&quot;</code>. There, Perl automatically and invisibly substitutes the thread-safe version, without notice. This means that code that safely runs on some systems can fail on others that lack the thread-safe versions. </p>
<p> Portability issues: ``getpwnam&#8217;&#8216; in perlport to ``endservent&#8217;&#8216; in perlport. </p>
 </dd>
<dt>getsockname <font SIZE="-1">SOCKET</font></dt>
<dd> <p> Returns the packed sockaddr address of this end of the <font SIZE="-1">SOCKET</font> connection, in case you don&#8217;t know the address because you have several different IPs that the connection might have come in on. </p>
<pre><code>    use Socket;
    my $mysockaddr = getsockname($sock);
    my ($port, $myaddr) = sockaddr_in($mysockaddr);
    printf &quot;Connect to %s [%s]\n&quot;,
       scalar gethostbyaddr($myaddr, AF_INET),
       inet_ntoa($myaddr);
</code></pre>
 </dd>
<dt>getsockopt <font SIZE="-1">SOCKET,LEVEL,OPTNAME</font></dt>
<dd> <p> Queries the option named <font SIZE="-1">OPTNAME</font> associated with <font SIZE="-1">SOCKET</font> at a given <font SIZE="-1">LEVEL.</font> Options may exist at multiple protocol levels depending on the socket type, but at least the uppermost socket level <font SIZE="-1">SOL_SOCKET</font> (defined in the <code>&quot;Socket&quot;</code> module) will exist. To query options at another level the protocol number of the appropriate protocol controlling the option should be supplied. For example, to indicate that an option is to be interpreted by the <font SIZE="-1">TCP</font> protocol, <font SIZE="-1">LEVEL</font> should be set to the protocol number of <font SIZE="-1">TCP,</font> which you can get using <code>&quot;getprotobyname&quot;</code>. </p>
<p> The function returns a packed string representing the requested socket option, or <code>&quot;undef&quot;</code> on error, with the reason for the error placed in <code>$!</code>. Just what is in the packed string depends on <font SIZE="-1">LEVEL</font> and <font SIZE="-1">OPTNAME</font>; consult <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) for details. A common case is that the option is an integer, in which case the result is a packed integer, which you can decode using <code>&quot;unpack&quot;</code> with the <code>&quot;i&quot;</code> (or <code>&quot;I&quot;</code>) format. </p>
<p> Here&#8217;s an example to test whether Nagle&#8217;s algorithm is enabled on a socket: </p>
<pre><code>    use Socket qw(:all);
    defined(my $tcp = getprotobyname(&quot;tcp&quot;))
        or die &quot;Could not determine the protocol number for tcp&quot;;
    # my $tcp = IPPROTO_TCP; # Alternative
    my $packed = getsockopt($socket, $tcp, TCP_NODELAY)
        or die &quot;getsockopt TCP_NODELAY: $!&quot;;
    my $nodelay = unpack(&quot;I&quot;, $packed);
    print &quot;Nagle's algorithm is turned &quot;,
           $nodelay ? &quot;off\n&quot; : &quot;on\n&quot;;
</code></pre>
<p> Portability issues: ``getsockopt&#8217;&#8216; in perlport. </p>
 </dd>
<dt>glob <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>glob</dt>
<dd> <p> In list context, returns a (possibly empty) list of filename expansions on the value of <font SIZE="-1">EXPR</font> such as the standard Unix shell <i>/bin/csh</i> would do. In scalar context, glob iterates through such filename expansions, returning undef when the list is exhausted. This is the internal function implementing the <code>&quot;&lt;*.c&gt;&quot;</code> operator, but you can use it directly. If <font SIZE="-1">EXPR</font> is omitted, <code>$_</code> is used. The <code>&quot;&lt;*.c&gt;&quot;</code> operator is discussed in more detail in ``I/O Operators&#8217;&#8216; in perlop. </p>
<p> Note that <code>&quot;glob&quot;</code> splits its arguments on whitespace and treats each segment as separate pattern. As such, <code>&quot;glob(&quot;*.c *.h&quot;)&quot;</code> matches all files with a <i>.c</i> or <i>.h</i> extension. The expression <code>&quot;glob(&quot;.* *&quot;)&quot;</code> matches all files in the current working directory. If you want to glob filenames that might contain whitespace, you&#8217;ll have to use extra quotes around the spacey filename to protect it. For example, to glob filenames that have an <code>&quot;e&quot;</code> followed by a space followed by an <code>&quot;f&quot;</code>, use one of: </p>
<pre><code>    my @spacies = &lt;&quot;*e f*&quot;&gt;;
    my @spacies = glob '&quot;*e f*&quot;';
    my @spacies = glob q(&quot;*e f*&quot;);
</code></pre>
<p> If you had to get a variable through, you could do this: </p>
<pre><code>    my @spacies = glob &quot;'*${var}e f*'&quot;;
    my @spacies = glob qq(&quot;*${var}e f*&quot;);
</code></pre>
<p> If non-empty braces are the only wildcard characters used in the <code>&quot;glob&quot;</code>, no filenames are matched, but potentially many strings are returned. For example, this produces nine strings, one for each pairing of fruits and colors: </p>
<pre><code>    my @many = glob &quot;{apple,tomato,cherry}={green,yellow,red}&quot;;
</code></pre>
<p> This operator is implemented using the standard <code>&quot;File::Glob&quot;</code> extension. See File::Glob for details, including <code>&quot;bsd_glob&quot;</code>, which does not treat whitespace as a pattern separator. </p>
<p> If a <code>&quot;glob&quot;</code> expression is used as the condition of a <code>&quot;while&quot;</code> or <code>&quot;for&quot;</code> loop, then it will be implicitly assigned to <code>$_</code>. If either a <code>&quot;glob&quot;</code> expression or an explicit assignment of a <code>&quot;glob&quot;</code> expression to a scalar is used as a <code>&quot;while&quot;</code>/<code>&quot;for&quot;</code> condition, then the condition actually tests for definedness of the expression&#8217;s value, not for its regular truth value. </p>
<p> Portability issues: ``glob&#8217;&#8216; in perlport. </p>
 </dd>
<dt>gmtime <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>gmtime</dt>
<dd> <p> Works just like <code>&quot;localtime&quot;</code> but the returned values are localized for the standard Greenwich time zone. </p>
<p> Note: When called in list context, <code>$isdst</code>, the last value returned by gmtime, is always <code>0</code>. There is no Daylight Saving Time in <font SIZE="-1">GMT.</font> </p>
<p> Portability issues: ``gmtime&#8217;&#8216; in perlport. </p>
 </dd>
<dt>goto <font SIZE="-1">LABEL</font></dt>
<dd>  </dd>
<dt>goto <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>goto &amp;NAME</dt>
<dd> <p> The <code>&quot;goto LABEL&quot;</code> form finds the statement labeled with <font SIZE="-1">LABEL</font> and resumes execution there. It can&#8217;t be used to get out of a block or subroutine given to <code>&quot;sort&quot;</code>. It can be used to go almost anywhere else within the dynamic scope, including out of subroutines, but it&#8217;s usually better to use some other construct such as <code>&quot;last&quot;</code> or <code>&quot;die&quot;</code>. The author of Perl has never felt the need to use this form of <code>&quot;goto&quot;</code> (in Perl, that is; C is another matter). (The difference is that C does not offer named loops combined with loop control. Perl does, and this replaces most structured uses of <code>&quot;goto&quot;</code> in other languages.) </p>
<p> The <code>&quot;goto EXPR&quot;</code> form expects to evaluate <code>&quot;EXPR&quot;</code> to a code reference or a label name. If it evaluates to a code reference, it will be handled like <code>&quot;goto &amp;NAME&quot;</code>, below. This is especially useful for implementing tail recursion via <code>&quot;goto __SUB__&quot;</code>. </p>
<p> If the expression evaluates to a label name, its scope will be resolved dynamically. This allows for computed <code>&quot;goto&quot;</code>s per <font SIZE="-1">FORTRAN,</font> but isn&#8217;t necessarily recommended if you&#8217;re optimizing for maintainability: </p>
<pre><code>    goto (&quot;FOO&quot;, &quot;BAR&quot;, &quot;GLARCH&quot;)[$i];
</code></pre>
<p> As shown in this example, <code>&quot;goto EXPR&quot;</code> is exempt from the ``looks like a function&#8217;&#8216; rule. A pair of parentheses following it does not (necessarily) delimit its argument. <code>&quot;goto(&quot;NE&quot;).&quot;XT&quot;&quot;</code> is equivalent to <code>&quot;goto NEXT&quot;</code>. Also, unlike most named operators, this has the same precedence as assignment. </p>
<p> Use of <code>&quot;goto LABEL&quot;</code> or <code>&quot;goto EXPR&quot;</code> to jump into a construct is deprecated and will issue a warning. Even then, it may not be used to go into any construct that requires initialization, such as a subroutine, a <code>&quot;foreach&quot;</code> loop, or a <code>&quot;given&quot;</code> block. In general, it may not be used to jump into the parameter of a binary or list operator, but it may be used to jump into the <i>first</i> parameter of a binary operator. (The <code>&quot;=&quot;</code> assignment operator&#8217;s ``first&#8217;&#8216; operand is its right-hand operand.) It also can&#8217;t be used to go into a construct that is optimized away. </p>
<p> The <code>&quot;goto &amp;NAME&quot;</code> form is quite different from the other forms of <code>&quot;goto&quot;</code>. In fact, it isn&#8217;t a goto in the normal sense at all, and doesn&#8217;t have the stigma associated with other gotos. Instead, it exits the current subroutine (losing any changes set by <code>&quot;local&quot;</code>) and immediately calls in its place the named subroutine using the current value of <code>@_</code>. This is used by <code>&quot;AUTOLOAD&quot;</code> subroutines that wish to load another subroutine and then pretend that the other subroutine had been called in the first place (except that any modifications to <code>@_</code> in the current subroutine are propagated to the other subroutine.) After the <code>&quot;goto&quot;</code>, not even <code>&quot;caller&quot;</code> will be able to tell that this routine was called first. </p>
<p> <font SIZE="-1">NAME</font> needn&#8217;t be the name of a subroutine; it can be a scalar variable containing a code reference or a block that evaluates to a code reference. </p>
 </dd>
<dt>grep <font SIZE="-1">BLOCK LIST</font></dt>
<dd>  </dd>
<dt>grep <font SIZE="-1">EXPR,LIST</font></dt>
<dd> <p> This is similar in spirit to, but not the same as, <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) and its relatives. In particular, it is not limited to using regular expressions. </p>
<p> Evaluates the <font SIZE="-1">BLOCK</font> or <font SIZE="-1">EXPR</font> for each element of <font SIZE="-1">LIST</font> (locally setting <code>$_</code> to each element) and returns the list value consisting of those elements for which the expression evaluated to true. In scalar context, returns the number of times the expression was true. </p>
<pre><code>    my @foo = grep(!/^#/, @bar); # weed out comments
</code></pre>
<p> or equivalently, </p>
<pre><code>    my @foo = grep {!/^#/} @bar; # weed out comments
</code></pre>
<p> Note that <code>$_</code> is an alias to the list value, so it can be used to modify the elements of the <font SIZE="-1">LIST.</font> While this is useful and supported, it can cause bizarre results if the elements of <font SIZE="-1">LIST</font> are not variables. Similarly, grep returns aliases into the original list, much as a for loop&#8217;s index variable aliases the list elements. That is, modifying an element of a list returned by grep (for example, in a <code>&quot;foreach&quot;</code>, <code>&quot;map&quot;</code> or another <code>&quot;grep&quot;</code>) actually modifies the element in the original list. This is usually something to be avoided when writing clear code. </p>
<p> See also <code>&quot;map&quot;</code> for a list composed of the results of the <font SIZE="-1">BLOCK</font> or <font SIZE="-1">EXPR.</font> </p>
 </dd>
<dt>hex <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>hex</dt>
<dd> <p> Interprets <font SIZE="-1">EXPR</font> as a hex string and returns the corresponding numeric value. If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. </p>
<pre><code>    print hex '0xAf'; # prints '175'
    print hex 'aF'; # same
    $valid_input =~ /\A(?:0?[xX])?(?:_?[0-9a-fA-F])*\z/
</code></pre>
<p> A hex string consists of hex digits and an optional <code>&quot;0x&quot;</code> or <code>&quot;x&quot;</code> prefix. Each hex digit may be preceded by a single underscore, which will be ignored. Any other character triggers a warning and causes the rest of the string to be ignored (even leading whitespace, unlike <code>&quot;oct&quot;</code>). Only integers can be represented, and integer overflow triggers a warning. </p>
<p> To convert strings that might start with any of <code>0</code>, <code>&quot;0x&quot;</code>, or <code>&quot;0b&quot;</code>, see <code>&quot;oct&quot;</code>. To present something as hex, look into <code>&quot;printf&quot;</code>, <code>&quot;sprintf&quot;</code>, and <code>&quot;unpack&quot;</code>. </p>
 </dd>
<dt>import <font SIZE="-1">LIST</font></dt>
<dd> <p> There is no builtin <code>&quot;import&quot;</code> function. It is just an ordinary method (subroutine) defined (or inherited) by modules that wish to export names to another module. The <code>&quot;use&quot;</code> function calls the <code>&quot;import&quot;</code> method for the package used. See also <code>&quot;use&quot;</code>, perlmod, and Exporter. </p>
 </dd>
<dt>index <font SIZE="-1">STR,SUBSTR,POSITION</font></dt>
<dd>  </dd>
<dt>index <font SIZE="-1">STR,SUBSTR</font></dt>
<dd> <p> The index function searches for one string within another, but without the wildcard-like behavior of a full regular-expression pattern match. It returns the position of the first occurrence of <font SIZE="-1">SUBSTR</font> in <font SIZE="-1">STR</font> at or after <font SIZE="-1">POSITION.</font> If <font SIZE="-1">POSITION</font> is omitted, starts searching from the beginning of the string. <font SIZE="-1">POSITION</font> before the beginning of the string or after its end is treated as if it were the beginning or the end, respectively. <font SIZE="-1">POSITION</font> and the return value are based at zero. If the substring is not found, <code>&quot;index&quot;</code> returns -1. </p>
 </dd>
<dt>int <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>int</dt>
<dd> <p> Returns the integer portion of <font SIZE="-1">EXPR.</font> If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. You should not use this function for rounding: one because it truncates towards <code>0</code>, and two because machine representations of floating-point numbers can sometimes produce counterintuitive results. For example, <code>&quot;int(-6.725/0.025)&quot;</code> produces -268 rather than the correct -269; that&#8217;s because it&#8217;s really more like -268.99999999999994315658 instead. Usually, the <code>&quot;sprintf&quot;</code>, <code>&quot;printf&quot;</code>, or the <code>&quot;POSIX::floor&quot;</code> and <code>&quot;POSIX::ceil&quot;</code> functions will serve you better than will <code>&quot;int&quot;</code>. </p>
 </dd>
<dt>ioctl <font SIZE="-1">FILEHANDLE,FUNCTION,SCALAR</font></dt>
<dd> <p> Implements the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) function. You&#8217;ll probably first have to say </p>
<pre><code>    require &quot;sys/ioctl.ph&quot;; # probably in
                             # $Config{archlib}/sys/ioctl.ph
</code></pre>
<p> to get the correct function definitions. If <i>sys/ioctl.ph</i> doesn&#8217;t exist or doesn&#8217;t have the correct definitions you&#8217;ll have to roll your own, based on your C header files such as <i>&lt;sys/ioctl.h&gt;</i>. (There is a Perl script called <code>h2ph</code> that comes with the Perl kit that may help you in this, but it&#8217;s nontrivial.) <font SIZE="-1">SCALAR</font> will be read and/or written depending on the <font SIZE="-1">FUNCTION</font>; a C pointer to the string value of <font SIZE="-1">SCALAR</font> will be passed as the third argument of the actual <code>&quot;ioctl&quot;</code> call. (If <font SIZE="-1">SCALAR</font> has no string value but does have a numeric value, that value will be passed rather than a pointer to the string value. To guarantee this to be true, add a <code>0</code> to the scalar before using it.) The <code>&quot;pack&quot;</code> and <code>&quot;unpack&quot;</code> functions may be needed to manipulate the values of structures used by <code>&quot;ioctl&quot;</code>. </p>
<p> The return value of <code>&quot;ioctl&quot;</code> (and <code>&quot;fcntl&quot;</code>) is as follows: </p>
<pre><code>    if OS returns: then Perl returns:
        -1 undefined value
         0 string &quot;0 but true&quot;
    anything else that number
</code></pre>
<p> Thus Perl returns true on success and false on failure, yet you can still easily determine the actual value returned by the operating system: </p>
<pre><code>    my $retval = ioctl(...) || -1;
    printf &quot;System returned %d\n&quot;, $retval;
</code></pre>
<p> The special string <code>&quot;0 but true&quot;</code> is exempt from <code>&quot;Argument &quot;...&quot; isn&#8217;t numeric&quot;</code> warnings on improper numeric conversions. </p>
<p> Portability issues: ``ioctl&#8217;&#8216; in perlport. </p>
 </dd>
<dt>join <font SIZE="-1">EXPR,LIST</font></dt>
<dd> <p> Joins the separate strings of <font SIZE="-1">LIST</font> into a single string with fields separated by the value of <font SIZE="-1">EXPR,</font> and returns that new string. Example: </p>
<pre><code>   my $rec = join(':', $login,$passwd,$uid,$gid,$gcos,$home,$shell);
</code></pre>
<p> Beware that unlike <code>&quot;split&quot;</code>, <code>&quot;join&quot;</code> doesn&#8217;t take a pattern as its first argument. Compare <code>&quot;split&quot;</code>. </p>
 </dd>
<dt>keys <font SIZE="-1">HASH</font></dt>
<dd>  </dd>
<dt>keys <font SIZE="-1">ARRAY</font></dt>
<dd> <p> Called in list context, returns a list consisting of all the keys of the named hash, or in Perl 5.12 or later only, the indices of an array. Perl releases prior to 5.12 will produce a syntax error if you try to use an array argument. In scalar context, returns the number of keys or indices. </p>
<p> Hash entries are returned in an apparently random order. The actual random order is specific to a given hash; the exact same series of operations on two hashes may result in a different order for each hash. Any insertion into the hash may change the order, as will any deletion, with the exception that the most recent key returned by <code>&quot;each&quot;</code> or <code>&quot;keys&quot;</code> may be deleted without changing the order. So long as a given hash is unmodified you may rely on <code>&quot;keys&quot;</code>, <code>&quot;values&quot;</code> and <code>&quot;each&quot;</code> to repeatedly return the same order as each other. See ``Algorithmic Complexity Attacks&#8217;&#8216; in perlsec for details on why hash order is randomized. Aside from the guarantees provided here the exact details of Perl&#8217;s hash algorithm and the hash traversal order are subject to change in any release of Perl. Tied hashes may behave differently to Perl&#8217;s hashes with respect to changes in order on insertion and deletion of items. </p>
<p> As a side effect, calling <code>&quot;keys&quot;</code> resets the internal iterator of the <font SIZE="-1">HASH</font> or <font SIZE="-1">ARRAY</font> (see <code>&quot;each&quot;</code>) before yielding the keys. In particular, calling <code>&quot;keys&quot;</code> in void context resets the iterator with no other overhead. </p>
<p> Here is yet another way to print your environment: </p>
<pre><code>    my @keys = keys %ENV;
    my @values = values %ENV;
    while (@keys) {
        print pop(@keys), '=', pop(@values), &quot;\n&quot;;
    }
</code></pre>
<p> or how about sorted by key: </p>
<pre><code>    foreach my $key (sort(keys %ENV)) {
        print $key, '=', $ENV{$key}, &quot;\n&quot;;
    }
</code></pre>
<p> The returned values are copies of the original keys in the hash, so modifying them will not affect the original hash. Compare <code>&quot;values&quot;</code>. </p>
<p> To sort a hash by value, you&#8217;ll need to use a <code>&quot;sort&quot;</code> function. Here&#8217;s a descending numeric sort of a hash by its values: </p>
<pre><code>    foreach my $key (sort { $hash{$b} &lt;=&gt; $hash{$a} } keys %hash) {
        printf &quot;%4d %s\n&quot;, $hash{$key}, $key;
    }
</code></pre>
<p> Used as an lvalue, <code>&quot;keys&quot;</code> allows you to increase the number of hash buckets allocated for the given hash. This can gain you a measure of efficiency if you know the hash is going to get big. (This is similar to pre-extending an array by assigning a larger number to $#array.) If you say </p>
<pre><code>    keys %hash = 200;
</code></pre>
<p> then <code>%hash</code> will have at least 200 buckets allocated for it--256 of them, in fact, since it rounds up to the next power of two. These buckets will be retained even if you do <code>&quot;%hash = ()&quot;</code>, use <code>&quot;undef %hash&quot;</code> if you want to free the storage while <code>%hash</code> is still in scope. You can&#8217;t shrink the number of buckets allocated for the hash using <code>&quot;keys&quot;</code> in this way (but you needn&#8217;t worry about doing this by accident, as trying has no effect). <code>&quot;keys @array&quot;</code> in an lvalue context is a syntax error. </p>
<p> Starting with Perl 5.14, an experimental feature allowed <code>&quot;keys&quot;</code> to take a scalar expression. This experiment has been deemed unsuccessful, and was removed as of Perl 5.24. </p>
<p> To avoid confusing would-be users of your code who are running earlier versions of Perl with mysterious syntax errors, put this sort of thing at the top of your file to signal that your code will work <i>only</i> on Perls of a recent vintage: </p>
<pre><code>    use 5.012; # so keys/values/each work on arrays
</code></pre>
<p> See also <code>&quot;each&quot;</code>, <code>&quot;values&quot;</code>, and <code>&quot;sort&quot;</code>. </p>
 </dd>
<dt>kill <font SIZE="-1">SIGNAL, LIST</font></dt>
<dd>  </dd>
<dt>kill <font SIZE="-1">SIGNAL</font></dt>
<dd> <p> Sends a signal to a list of processes. Returns the number of arguments that were successfully used to signal (which is not necessarily the same as the number of processes actually killed, e.g. where a process group is killed). </p>
<pre><code>    my $cnt = kill 'HUP', $child1, $child2;
    kill 'KILL', @goners;
</code></pre>
<p> <font SIZE="-1">SIGNAL</font> may be either a signal name (a string) or a signal number. A signal name may start with a <code>&quot;SIG&quot;</code> prefix, thus <code>&quot;FOO&quot;</code> and <code>&quot;SIGFOO&quot;</code> refer to the same signal. The string form of <font SIZE="-1">SIGNAL</font> is recommended for portability because the same signal may have different numbers in different operating systems. </p>
<p> A list of signal names supported by the current platform can be found in <code>$Config{sig_name}</code>, which is provided by the <code>&quot;Config&quot;</code> module. See Config for more details. </p>
<p> A negative signal name is the same as a negative signal number, killing process groups instead of processes. For example, <code>&quot;kill &#8216;-KILL&#8217;, $pgrp&quot;</code> and <code>&quot;kill -9, $pgrp&quot;</code> will send <code>&quot;SIGKILL&quot;</code> to the entire process group specified. That means you usually want to use positive not negative signals. </p>
<p> If <font SIZE="-1">SIGNAL</font> is either the number 0 or the string <code>&quot;ZERO&quot;</code> (or <code>&quot;SIGZERO&quot;</code>), no signal is sent to the process, but <code>&quot;kill&quot;</code> checks whether it&#8217;s <i>possible</i> to send a signal to it (that means, to be brief, that the process is owned by the same user, or we are the super-user). This is useful to check that a child process is still alive (even if only as a zombie) and hasn&#8217;t changed its <font SIZE="-1">UID.</font> See perlport for notes on the portability of this construct. </p>
<p> The behavior of kill when a <i></i><font SIZE="-1"><i>PROCESS</i></font><i></i> number is zero or negative depends on the operating system. For example, on POSIX-conforming systems, zero will signal the current process group, -1 will signal all processes, and any other negative <font SIZE="-1">PROCESS</font> number will act as a negative signal number and kill the entire process group specified. </p>
<p> If both the <font SIZE="-1">SIGNAL</font> and the <font SIZE="-1">PROCESS</font> are negative, the results are undefined. A warning may be produced in a future version. </p>
<p> See ``Signals&#8217;&#8216; in perlipc for more details. </p>
<p> On some platforms such as Windows where the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) system call is not available, Perl can be built to emulate <code>&quot;fork&quot;</code> at the interpreter level. This emulation has limitations related to kill that have to be considered, for code running on Windows and in code intended to be portable. </p>
<p> See perlfork for more details. </p>
<p> If there is no <i></i><font SIZE="-1"><i>LIST</i></font><i></i> of processes, no signal is sent, and the return value is 0. This form is sometimes used, however, because it causes tainting checks to be run. But see ``Laundering and Detecting Tainted Data&#8217;&#8216; in perlsec. </p>
<p> Portability issues: ``kill&#8217;&#8216; in perlport. </p>
 </dd>
<dt>last <font SIZE="-1">LABEL</font></dt>
<dd>  </dd>
<dt>last <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>last</dt>
<dd> <p> The <code>&quot;last&quot;</code> command is like the <code>&quot;break&quot;</code> statement in C (as used in loops); it immediately exits the loop in question. If the <font SIZE="-1">LABEL</font> is omitted, the command refers to the innermost enclosing loop. The <code>&quot;last EXPR&quot;</code> form, available starting in Perl 5.18.0, allows a label name to be computed at run time, and is otherwise identical to <code>&quot;last LABEL&quot;</code>. The <code>&quot;continue&quot;</code> block, if any, is not executed: </p>
<pre><code>    LINE: while (&lt;STDIN&gt;) {
        last LINE if /^$/; # exit when done with header
        #...
    }
</code></pre>
<p> <code>&quot;last&quot;</code> cannot return a value from a block that typically returns a value, such as <code>&quot;eval {}&quot;</code>, <code>&quot;sub {}&quot;</code>, or <code>&quot;do {}&quot;</code>. It will perform its flow control behavior, which precludes any return value. It should not be used to exit a <code>&quot;grep&quot;</code> or <code>&quot;map&quot;</code> operation. </p>
<p> Note that a block by itself is semantically identical to a loop that executes once. Thus <code>&quot;last&quot;</code> can be used to effect an early exit out of such a block. </p>
<p> See also <code>&quot;continue&quot;</code> for an illustration of how <code>&quot;last&quot;</code>, <code>&quot;next&quot;</code>, and <code>&quot;redo&quot;</code> work. </p>
<p> Unlike most named operators, this has the same precedence as assignment. It is also exempt from the looks-like-a-function rule, so <code>&quot;last (&quot;foo&quot;).&quot;bar&quot;&quot;</code> will cause ``bar&#8217;&#8216; to be part of the argument to <code>&quot;last&quot;</code>. </p>
 </dd>
<dt>lc <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>lc</dt>
<dd> <p> Returns a lowercased version of <font SIZE="-1">EXPR.</font> This is the internal function implementing the <code>&quot;\L&quot;</code> escape in double-quoted strings. </p>
<p> If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. </p>
<p> What gets returned depends on several factors: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>If &quot;use bytes&quot; is in effect:</dt>
<dd> <p> The results follow <font SIZE="-1">ASCII</font> rules. Only the characters <code>&quot;A-Z&quot;</code> change, to <code>&quot;a-z&quot;</code> respectively. </p>
 </dd>
<dt>Otherwise, if &quot;use locale&quot; for &quot;LC_CTYPE&quot; is in effect:</dt>
<dd> <p> Respects current <code>&quot;LC_CTYPE&quot;</code> locale for code points &lt; 256; and uses Unicode rules for the remaining code points (this last can only happen if the <font SIZE="-1">UTF8</font> flag is also set). See perllocale. </p>
<p> Starting in v5.20, Perl uses full Unicode rules if the locale is <font SIZE="-1">UTF-8.</font> Otherwise, there is a deficiency in this scheme, which is that case changes that cross the 255/256 boundary are not well-defined. For example, the lower case of <font SIZE="-1">LATIN CAPITAL LETTER SHARP S</font> (U+1E9E) in Unicode rules is U+00DF (on <font SIZE="-1">ASCII</font> platforms). But under <code>&quot;use locale&quot;</code> (prior to v5.20 or not a <font SIZE="-1">UTF-8</font> locale), the lower case of U+1E9E is itself, because 0xDF may not be <font SIZE="-1">LATIN SMALL LETTER SHARP S</font> in the current locale, and Perl has no way of knowing if that character even exists in the locale, much less what code point it is. Perl returns a result that is above 255 (almost always the input character unchanged), for all instances (and there aren&#8217;t many) where the 255/256 boundary would otherwise be crossed; and starting in v5.22, it raises a locale warning. </p>
 </dd>
<dt>Otherwise, If <font SIZE="-1">EXPR</font> has the <font SIZE="-1">UTF8</font> flag set:</dt>
<dd> <p> Unicode rules are used for the case change. </p>
 </dd>
<dt>Otherwise, if &quot;use feature &#8216;unicode_strings&#8217;&quot; or &quot;use locale &#8216;:not_characters&#8217;&quot; is in effect:</dt>
<dd> <p> Unicode rules are used for the case change. </p>
 </dd>
<dt>Otherwise:</dt>
<dd> <p> <font SIZE="-1">ASCII</font> rules are used for the case change. The lowercase of any character outside the <font SIZE="-1">ASCII</font> range is the character itself. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>lcfirst <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>lcfirst</dt>
<dd> <p> Returns the value of <font SIZE="-1">EXPR</font> with the first character lowercased. This is the internal function implementing the <code>&quot;\l&quot;</code> escape in double-quoted strings. </p>
<p> If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. </p>
<p> This function behaves the same way under various pragmas, such as in a locale, as <code>&quot;lc&quot;</code> does. </p>
 </dd>
<dt>length <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>length</dt>
<dd> <p> Returns the length in <i>characters</i> of the value of <font SIZE="-1">EXPR.</font> If <font SIZE="-1">EXPR</font> is omitted, returns the length of <code>$_</code>. If <font SIZE="-1">EXPR</font> is undefined, returns <code>&quot;undef&quot;</code>. </p>
<p> This function cannot be used on an entire array or hash to find out how many elements these have. For that, use <code>&quot;scalar @array&quot;</code> and <code>&quot;scalar keys %hash&quot;</code>, respectively. </p>
<p> Like all Perl character operations, <code>&quot;length&quot;</code> normally deals in logical characters, not physical bytes. For how many bytes a string encoded as <font SIZE="-1">UTF-8</font> would take up, use <code>&quot;length(Encode::encode(&#8216;UTF-8&#8217;, EXPR))&quot;</code> (you&#8217;ll have to <code>&quot;use Encode&quot;</code> first). See Encode and perlunicode. </p>
 </dd>
<dt>__LINE__</dt>
<dd> <p> A special token that compiles to the current line number. </p>
 </dd>
<dt>link <font SIZE="-1">OLDFILE,NEWFILE</font></dt>
<dd> <p> Creates a new filename linked to the old filename. Returns true for success, false otherwise. </p>
<p> Portability issues: ``link&#8217;&#8216; in perlport. </p>
 </dd>
<dt>listen <font SIZE="-1">SOCKET,QUEUESIZE</font></dt>
<dd> <p> Does the same thing that the <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) system call does. Returns true if it succeeded, false otherwise. See the example in ``Sockets: Client/Server Communication&#8217;&#8216; in perlipc. </p>
 </dd>
<dt>local <font SIZE="-1">EXPR</font></dt>
<dd> <p> You really probably want to be using <code>&quot;my&quot;</code> instead, because <code>&quot;local&quot;</code> isn&#8217;t what most people think of as ``local&#8217;&#8216;. See ``Private Variables via <code>my()</code>&#8216;&#8216; in perlsub for details. </p>
<p> A local modifies the listed variables to be local to the enclosing block, file, or eval. If more than one value is listed, the list must be placed in parentheses. See ``Temporary Values via <code>local()</code>&#8216;&#8216; in perlsub for details, including issues with tied arrays and hashes. </p>
<p> The <code>&quot;delete local EXPR&quot;</code> construct can also be used to localize the deletion of array/hash elements to the current block. See ``Localized deletion of elements of composite types&#8217;&#8216; in perlsub. </p>
 </dd>
<dt>localtime <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>localtime</dt>
<dd> <p> Converts a time as returned by the time function to a 9-element list with the time analyzed for the local time zone. Typically used as follows: </p>
<pre><code>    # 0 1 2 3 4 5 6 7 8
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) =
                                                localtime(time);
</code></pre>
<p> All list elements are numeric and come straight out of the C `struct tm&#8217;. <code>$sec</code>, <code>$min</code>, and <code>$hour</code> are the seconds, minutes, and hours of the specified time. </p>
<p> <code>$mday</code> is the day of the month and <code>$mon</code> the month in the range <code>0..11</code>, with 0 indicating January and 11 indicating December. This makes it easy to get a month name from a list: </p>
<pre><code>    my @abbr = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
    print &quot;$abbr[$mon] $mday&quot;;
    # $mon=9, $mday=18 gives &quot;Oct 18&quot;
</code></pre>
<p> <code>$year</code> contains the number of years since 1900. To get a 4-digit year write: </p>
<pre><code>    $year += 1900;
</code></pre>
<p> To get the last two digits of the year (e.g., ``01&#8217;&#8216; in 2001) do: </p>
<pre><code>    $year = sprintf(&quot;%02d&quot;, $year % 100);
</code></pre>
<p> <code>$wday</code> is the day of the week, with 0 indicating Sunday and 3 indicating Wednesday. <code>$yday</code> is the day of the year, in the range <code>0..364</code> (or <code>0..365</code> in leap years.) </p>
<p> <code>$isdst</code> is true if the specified time occurs during Daylight Saving Time, false otherwise. </p>
<p> If <font SIZE="-1">EXPR</font> is omitted, <code>&quot;localtime&quot;</code> uses the current time (as returned by <code>&quot;time&quot;</code>). </p>
<p> In scalar context, <code>&quot;localtime&quot;</code> returns the <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) value: </p>
<pre><code>    my $now_string = localtime; # e.g., &quot;Thu Oct 13 04:54:34 1994&quot;
</code></pre>
<p> The format of this scalar value is <code>not</code> locale-dependent but built into Perl. For <font SIZE="-1">GMT</font> instead of local time use the <code>&quot;gmtime&quot;</code> builtin. See also the <code>&quot;Time::Local&quot;</code> module (for converting seconds, minutes, hours, and such back to the integer value returned by <code>&quot;time&quot;</code>), and the <font SIZE="-1">POSIX</font> module&#8217;s <code>&quot;strftime&quot;</code> and <code>&quot;mktime&quot;</code> functions. </p>
<p> To get somewhat similar but locale-dependent date strings, set up your locale environment variables appropriately (please see perllocale) and try for example: </p>
<pre><code>    use POSIX qw(strftime);
    my $now_string = strftime &quot;%a %b %e %H:%M:%S %Y&quot;, localtime;
    # or for GMT formatted appropriately for your locale:
    my $now_string = strftime &quot;%a %b %e %H:%M:%S %Y&quot;, gmtime;
</code></pre>
<p> Note that <code>%a</code> and <code>%b</code>, the short forms of the day of the week and the month of the year, may not necessarily be three characters wide. </p>
<p> The Time::gmtime and Time::localtime modules provide a convenient, by-name access mechanism to the <code>&quot;gmtime&quot;</code> and <code>&quot;localtime&quot;</code> functions, respectively. </p>
<p> For a comprehensive date and time representation look at the DateTime module on <font SIZE="-1">CPAN.</font> </p>
<p> Portability issues: ``localtime&#8217;&#8216; in perlport. </p>
 </dd>
<dt>lock <font SIZE="-1">THING</font></dt>
<dd> <p> This function places an advisory lock on a shared variable or referenced object contained in <i></i><font SIZE="-1"><i>THING</i></font><i></i> until the lock goes out of scope. </p>
<p> The value returned is the scalar itself, if the argument is a scalar, or a reference, if the argument is a hash, array or subroutine. </p>
<p> <code>&quot;lock&quot;</code> is a ``weak keyword&#8217;&#8216;; this means that if you&#8217;ve defined a function by this name (before any calls to it), that function will be called instead. If you are not under <code>&quot;use threads::shared&quot;</code> this does nothing. See threads::shared. </p>
 </dd>
<dt>log <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>log</dt>
<dd> <p> Returns the natural logarithm (base <i>e</i>) of <font SIZE="-1">EXPR.</font> If <font SIZE="-1">EXPR</font> is omitted, returns the log of <code>$_</code>. To get the log of another base, use basic algebra: The base-N log of a number is equal to the natural log of that number divided by the natural log of N. For example: </p>
<pre><code>    sub log10 {
        my $n = shift;
        return log($n)/log(10);
    }
</code></pre>
<p> See also <code>&quot;exp&quot;</code> for the inverse operation. </p>
 </dd>
<dt>lstat <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>lstat <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>lstat <font SIZE="-1">DIRHANDLE</font></dt>
<dd>  </dd>
<dt>lstat</dt>
<dd> <p> Does the same thing as the <code>&quot;stat&quot;</code> function (including setting the special <code>&quot;_&quot;</code> filehandle) but stats a symbolic link instead of the file the symbolic link points to. If symbolic links are unimplemented on your system, a normal <code>&quot;stat&quot;</code> is done. For much more detailed information, please see the documentation for <code>&quot;stat&quot;</code>. </p>
<p> If <font SIZE="-1">EXPR</font> is omitted, stats <code>$_</code>. </p>
<p> Portability issues: ``lstat&#8217;&#8216; in perlport. </p>
 </dd>
<dt>m//</dt>
<dd> <p> The match operator. See ``Regexp Quote-Like Operators&#8217;&#8216; in perlop. </p>
 </dd>
<dt>map <font SIZE="-1">BLOCK LIST</font></dt>
<dd>  </dd>
<dt>map <font SIZE="-1">EXPR,LIST</font></dt>
<dd> <p> Evaluates the <font SIZE="-1">BLOCK</font> or <font SIZE="-1">EXPR</font> for each element of <font SIZE="-1">LIST</font> (locally setting <code>$_</code> to each element) and composes a list of the results of each such evaluation. Each element of <font SIZE="-1">LIST</font> may produce zero, one, or more elements in the generated list, so the number of elements in the generated list may differ from that in <font SIZE="-1">LIST.</font> In scalar context, returns the total number of elements so generated. In list context, returns the generated list. </p>
<pre><code>    my @chars = map(chr, @numbers);
</code></pre>
<p> translates a list of numbers to the corresponding characters. </p>
<pre><code>    my @squares = map { $_ * $_ } @numbers;
</code></pre>
<p> translates a list of numbers to their squared values. </p>
<pre><code>    my @squares = map { $_ &gt; 5 ? ($_ * $_) : () } @numbers;
</code></pre>
<p> shows that number of returned elements can differ from the number of input elements. To omit an element, return an empty list (). This could also be achieved by writing </p>
<pre><code>    my @squares = map { $_ * $_ } grep { $_ &gt; 5 } @numbers;
</code></pre>
<p> which makes the intention more clear. </p>
<p> Map always returns a list, which can be assigned to a hash such that the elements become key/value pairs. See perldata for more details. </p>
<pre><code>    my %hash = map { get_a_key_for($_) =&gt; $_ } @array;
</code></pre>
<p> is just a funny way to write </p>
<pre><code>    my %hash;
    foreach (@array) {
        $hash{get_a_key_for($_)} = $_;
    }
</code></pre>
<p> Note that <code>$_</code> is an alias to the list value, so it can be used to modify the elements of the <font SIZE="-1">LIST.</font> While this is useful and supported, it can cause bizarre results if the elements of <font SIZE="-1">LIST</font> are not variables. Using a regular <code>&quot;foreach&quot;</code> loop for this purpose would be clearer in most cases. See also <code>&quot;grep&quot;</code> for a list composed of those items of the original list for which the <font SIZE="-1">BLOCK</font> or <font SIZE="-1">EXPR</font> evaluates to true. </p>
<p> <code>&quot;{&quot;</code> starts both hash references and blocks, so <code>&quot;map { ...&quot;</code> could be either the start of map <font SIZE="-1">BLOCK LIST</font> or map <font SIZE="-1">EXPR, LIST.</font> Because Perl doesn&#8217;t look ahead for the closing <code>&quot;}&quot;</code> it has to take a guess at which it&#8217;s dealing with based on what it finds just after the <code>&quot;{&quot;</code>. Usually it gets it right, but if it doesn&#8217;t it won&#8217;t realize something is wrong until it gets to the <code>&quot;}&quot;</code> and encounters the missing (or unexpected) comma. The syntax error will be reported close to the <code>&quot;}&quot;</code>, but you&#8217;ll need to change something near the <code>&quot;{&quot;</code> such as using a unary <code>&quot;+&quot;</code> or semicolon to give Perl some help: </p>
<pre><code> my %hash = map { &quot;\L$_&quot; =&gt; 1 } @array # perl guesses EXPR. wrong
 my %hash = map { +&quot;\L$_&quot; =&gt; 1 } @array # perl guesses BLOCK. right
 my %hash = map {; &quot;\L$_&quot; =&gt; 1 } @array # this also works
 my %hash = map { (&quot;\L$_&quot; =&gt; 1) } @array # as does this
 my %hash = map { lc($_) =&gt; 1 } @array # and this.
 my %hash = map +( lc($_) =&gt; 1 ), @array # this is EXPR and works!
 my %hash = map ( lc($_), 1 ), @array # evaluates to (1, @array)
</code></pre>
<p> or to force an anon hash constructor use <code>&quot;+{&quot;</code>: </p>
<pre><code>    my @hashes = map +{ lc($_) =&gt; 1 }, @array # EXPR, so needs
                                              # comma at end
</code></pre>
<p> to get a list of anonymous hashes each with only one entry apiece. </p>
 </dd>
<dt>mkdir <font SIZE="-1">FILENAME,MODE</font></dt>
<dd>  </dd>
<dt>mkdir <font SIZE="-1">FILENAME</font></dt>
<dd>  </dd>
<dt>mkdir</dt>
<dd> <p> Creates the directory specified by <font SIZE="-1">FILENAME,</font> with permissions specified by <font SIZE="-1">MODE</font> (as modified by <code>&quot;umask&quot;</code>). If it succeeds it returns true; otherwise it returns false and sets <code>$!</code> (errno). <font SIZE="-1">MODE</font> defaults to 0777 if omitted, and <font SIZE="-1">FILENAME</font> defaults to <code>$_</code> if omitted. </p>
<p> In general, it is better to create directories with a permissive <font SIZE="-1">MODE</font> and let the user modify that with their <code>&quot;umask&quot;</code> than it is to supply a restrictive <font SIZE="-1">MODE</font> and give the user no way to be more permissive. The exceptions to this rule are when the file or directory should be kept private (mail files, for instance). The documentation for <code>&quot;umask&quot;</code> discusses the choice of <font SIZE="-1">MODE</font> in more detail. </p>
<p> Note that according to the <font SIZE="-1">POSIX 1003.1-1996</font> the <font SIZE="-1">FILENAME</font> may have any number of trailing slashes. Some operating and filesystems do not get this right, so Perl automatically removes all trailing slashes to keep everyone happy. </p>
<p> To recursively create a directory structure, look at the <code>&quot;make_path&quot;</code> function of the File::Path module. </p>
 </dd>
<dt>msgctl <font SIZE="-1">ID,CMD,ARG</font></dt>
<dd> <p> Calls the System V <font SIZE="-1">IPC</font> function <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2). You&#8217;ll probably have to say </p>
<pre><code>    use IPC::SysV;
</code></pre>
<p> first to get the correct constant definitions. If <font SIZE="-1">CMD</font> is <code>&quot;IPC_STAT&quot;</code>, then <font SIZE="-1">ARG</font> must be a variable that will hold the returned <code>&quot;msqid_ds&quot;</code> structure. Returns like <code>&quot;ioctl&quot;</code>: the undefined value for error, <code>&quot;0 but true&quot;</code> for zero, or the actual return value otherwise. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code> and <code>&quot;IPC::Semaphore&quot;</code>. </p>
<p> Portability issues: ``msgctl&#8217;&#8216; in perlport. </p>
 </dd>
<dt>msgget <font SIZE="-1">KEY,FLAGS</font></dt>
<dd> <p> Calls the System V <font SIZE="-1">IPC</font> function <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2). Returns the message queue id, or <code>&quot;undef&quot;</code> on error. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code> and <code>&quot;IPC::Msg&quot;</code>. </p>
<p> Portability issues: ``msgget&#8217;&#8216; in perlport. </p>
 </dd>
<dt>msgrcv <font SIZE="-1">ID,VAR,SIZE,TYPE,FLAGS</font></dt>
<dd> <p> Calls the System V <font SIZE="-1">IPC</font> function msgrcv to receive a message from message queue <font SIZE="-1">ID</font> into variable <font SIZE="-1">VAR</font> with a maximum message size of <font SIZE="-1">SIZE.</font> Note that when a message is received, the message type as a native long integer will be the first thing in <font SIZE="-1">VAR,</font> followed by the actual message. This packing may be opened with <code>&quot;unpack(&quot;l! a*&quot;)&quot;</code>. Taints the variable. Returns true if successful, false on error. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code> and <code>&quot;IPC::Msg&quot;</code>. </p>
<p> Portability issues: ``msgrcv&#8217;&#8216; in perlport. </p>
 </dd>
<dt>msgsnd <font SIZE="-1">ID,MSG,FLAGS</font></dt>
<dd> <p> Calls the System V <font SIZE="-1">IPC</font> function msgsnd to send the message <font SIZE="-1">MSG</font> to the message queue <font SIZE="-1">ID.</font> <font SIZE="-1">MSG</font> must begin with the native long integer message type, be followed by the length of the actual message, and then finally the message itself. This kind of packing can be achieved with <code>&quot;pack(&quot;l! a*&quot;, $type, $message)&quot;</code>. Returns true if successful, false on error. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code> and <code>&quot;IPC::Msg&quot;</code>. </p>
<p> Portability issues: ``msgsnd&#8217;&#8216; in perlport. </p>
 </dd>
<dt>my <font SIZE="-1">VARLIST</font></dt>
<dd>  </dd>
<dt>my <font SIZE="-1">TYPE VARLIST</font></dt>
<dd>  </dd>
<dt>my <font SIZE="-1">VARLIST : ATTRS</font></dt>
<dd>  </dd>
<dt>my <font SIZE="-1">TYPE VARLIST : ATTRS</font></dt>
<dd> <p> A <code>&quot;my&quot;</code> declares the listed variables to be local (lexically) to the enclosing block, file, or <code>&quot;eval&quot;</code>. If more than one variable is listed, the list must be placed in parentheses. </p>
<p> The exact semantics and interface of <font SIZE="-1">TYPE</font> and <font SIZE="-1">ATTRS</font> are still evolving. <font SIZE="-1">TYPE</font> may be a bareword, a constant declared with <code>&quot;use constant&quot;</code>, or <code>&quot;__PACKAGE__&quot;</code>. It is currently bound to the use of the fields pragma, and attributes are handled using the attributes pragma, or starting from Perl 5.8.0 also via the Attribute::Handlers module. See ``Private Variables via <code>my()</code>&#8216;&#8216; in perlsub for details. </p>
<p> Note that with a parenthesised list, <code>&quot;undef&quot;</code> can be used as a dummy placeholder, for example to skip assignment of initial values: </p>
<pre><code>    my ( undef, $min, $hour ) = localtime;
</code></pre>
 </dd>
<dt>next <font SIZE="-1">LABEL</font></dt>
<dd>  </dd>
<dt>next <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>next</dt>
<dd> <p> The <code>&quot;next&quot;</code> command is like the <code>&quot;continue&quot;</code> statement in C; it starts the next iteration of the loop: </p>
<pre><code>    LINE: while (&lt;STDIN&gt;) {
        next LINE if /^#/; # discard comments
        #...
    }
</code></pre>
<p> Note that if there were a <code>&quot;continue&quot;</code> block on the above, it would get executed even on discarded lines. If <font SIZE="-1">LABEL</font> is omitted, the command refers to the innermost enclosing loop. The <code>&quot;next EXPR&quot;</code> form, available as of Perl 5.18.0, allows a label name to be computed at run time, being otherwise identical to <code>&quot;next LABEL&quot;</code>. </p>
<p> <code>&quot;next&quot;</code> cannot return a value from a block that typically returns a value, such as <code>&quot;eval {}&quot;</code>, <code>&quot;sub {}&quot;</code>, or <code>&quot;do {}&quot;</code>. It will perform its flow control behavior, which precludes any return value. It should not be used to exit a <code>&quot;grep&quot;</code> or <code>&quot;map&quot;</code> operation. </p>
<p> Note that a block by itself is semantically identical to a loop that executes once. Thus <code>&quot;next&quot;</code> will exit such a block early. </p>
<p> See also <code>&quot;continue&quot;</code> for an illustration of how <code>&quot;last&quot;</code>, <code>&quot;next&quot;</code>, and <code>&quot;redo&quot;</code> work. </p>
<p> Unlike most named operators, this has the same precedence as assignment. It is also exempt from the looks-like-a-function rule, so <code>&quot;next (&quot;foo&quot;).&quot;bar&quot;&quot;</code> will cause ``bar&#8217;&#8216; to be part of the argument to <code>&quot;next&quot;</code>. </p>
 </dd>
<dt>no <font SIZE="-1">MODULE VERSION LIST</font></dt>
<dd>  </dd>
<dt>no <font SIZE="-1">MODULE VERSION</font></dt>
<dd>  </dd>
<dt>no <font SIZE="-1">MODULE LIST</font></dt>
<dd>  </dd>
<dt>no <font SIZE="-1">MODULE</font></dt>
<dd>  </dd>
<dt>no <font SIZE="-1">VERSION</font></dt>
<dd> <p> See the <code>&quot;use&quot;</code> function, of which <code>&quot;no&quot;</code> is the opposite. </p>
 </dd>
<dt>oct <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>oct</dt>
<dd> <p> Interprets <font SIZE="-1">EXPR</font> as an octal string and returns the corresponding value. (If <font SIZE="-1">EXPR</font> happens to start off with <code>&quot;0x&quot;</code>, interprets it as a hex string. If <font SIZE="-1">EXPR</font> starts off with <code>&quot;0b&quot;</code>, it is interpreted as a binary string. Leading whitespace is ignored in all three cases.) The following will handle decimal, binary, octal, and hex in standard Perl notation: </p>
<pre><code>    $val = oct($val) if $val =~ /^0/;
</code></pre>
<p> If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. To go the other way (produce a number in octal), use <code>&quot;sprintf&quot;</code> or <code>&quot;printf&quot;</code>: </p>
<pre><code>    my $dec_perms = (stat(&quot;filename&quot;))[2] &amp; 07777;
    my $oct_perm_str = sprintf &quot;%o&quot;, $perms;
</code></pre>
<p> The <code>&quot;oct&quot;</code> function is commonly used when a string such as <code>644</code> needs to be converted into a file mode, for example. Although Perl automatically converts strings into numbers as needed, this automatic conversion assumes base 10. </p>
<p> Leading white space is ignored without warning, as too are any trailing non-digits, such as a decimal point (<code>&quot;oct&quot;</code> only handles non-negative integers, not negative integers or floating point). </p>
 </dd>
<dt>open <font SIZE="-1">FILEHANDLE,EXPR</font></dt>
<dd>  </dd>
<dt>open <font SIZE="-1">FILEHANDLE,MODE,EXPR</font></dt>
<dd>  </dd>
<dt>open <font SIZE="-1">FILEHANDLE,MODE,EXPR,LIST</font></dt>
<dd>  </dd>
<dt>open <font SIZE="-1">FILEHANDLE,MODE,REFERENCE</font></dt>
<dd>  </dd>
<dt>open <font SIZE="-1">FILEHANDLE</font></dt>
<dd> <p> Opens the file whose filename is given by <font SIZE="-1">EXPR,</font> and associates it with <font SIZE="-1">FILEHANDLE.</font> </p>
<p> Simple examples to open a file for reading: </p>
<pre><code>    open(my $fh, &quot;&lt;&quot;, &quot;input.txt&quot;)
        or die &quot;Can't open &lt; input.txt: $!&quot;;
</code></pre>
<p> and for writing: </p>
<pre><code>    open(my $fh, &quot;&gt;&quot;, &quot;output.txt&quot;)
        or die &quot;Can't open &gt; output.txt: $!&quot;;
</code></pre>
<p> (The following is a comprehensive reference to <code>&quot;open&quot;</code>: for a gentler introduction you may consider perlopentut.) </p>
<p> If <font SIZE="-1">FILEHANDLE</font> is an undefined scalar variable (or array or hash element), a new filehandle is autovivified, meaning that the variable is assigned a reference to a newly allocated anonymous filehandle. Otherwise if <font SIZE="-1">FILEHANDLE</font> is an expression, its value is the real filehandle. (This is considered a symbolic reference, so <code>&quot;use strict &quot;refs&quot;&quot;</code> should <i>not</i> be in effect.) </p>
<p> If three (or more) arguments are specified, the open mode (including optional encoding) in the second argument are distinct from the filename in the third. If <font SIZE="-1">MODE</font> is <code>&quot;&lt;&quot;</code> or nothing, the file is opened for input. If <font SIZE="-1">MODE</font> is <code>&quot;&gt;&quot;</code>, the file is opened for output, with existing files first being truncated (``clobbered&#8217;&#8216;) and nonexisting files newly created. If <font SIZE="-1">MODE</font> is <code>&quot;&gt;&gt;&quot;</code>, the file is opened for appending, again being created if necessary. </p>
<p> You can put a <code>&quot;+&quot;</code> in front of the <code>&quot;&gt;&quot;</code> or <code>&quot;&lt;&quot;</code> to indicate that you want both read and write access to the file; thus <code>&quot;+&lt;&quot;</code> is almost always preferred for read/write updates---the <code>&quot;+&gt;&quot;</code> mode would clobber the file first. You can&#8217;t usually use either read-write mode for updating textfiles, since they have variable-length records. See the <code>-i</code> switch in perlrun for a better approach. The file is created with permissions of <code>0666</code> modified by the process&#8217;s <code>&quot;umask&quot;</code> value. </p>
<p> These various prefixes correspond to the <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3) modes of <code>&quot;r&quot;</code>, <code>&quot;r+&quot;</code>, <code>&quot;w&quot;</code>, <code>&quot;w+&quot;</code>, <code>&quot;a&quot;</code>, and <code>&quot;a+&quot;</code>. </p>
<p> In the one- and two-argument forms of the call, the mode and filename should be concatenated (in that order), preferably separated by white space. You can---but shouldn&#8217;t---omit the mode in these forms when that mode is <code>&quot;&lt;&quot;</code>. It is safe to use the two-argument form of <code>&quot;open&quot;</code> if the filename argument is a known literal. </p>
<p> For three or more arguments if <font SIZE="-1">MODE</font> is <code>&quot;|-&quot;</code>, the filename is interpreted as a command to which output is to be piped, and if <font SIZE="-1">MODE</font> is <code>&quot;-|&quot;</code>, the filename is interpreted as a command that pipes output to us. In the two-argument (and one-argument) form, one should replace dash (<code>&quot;-&quot;</code>) with the command. See ``Using <code>open()</code> for <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc for more examples of this. (You are not allowed to <code>&quot;open&quot;</code> to a command that pipes both in <i>and</i> out, but see IPC::Open2, IPC::Open3, and ``Bidirectional Communication with Another Process&#8217;&#8216; in perlipc for alternatives.) </p>
<p> In the form of pipe opens taking three or more arguments, if <font SIZE="-1">LIST</font> is specified (extra arguments after the command name) then <font SIZE="-1">LIST</font> becomes arguments to the command invoked if the platform supports it. The meaning of <code>&quot;open&quot;</code> with more than three arguments for non-pipe modes is not yet defined, but experimental ``layers&#8217;&#8216; may give extra <font SIZE="-1">LIST</font> arguments meaning. </p>
<p> In the two-argument (and one-argument) form, opening <code>&quot;&lt;-&quot;</code> or <code>&quot;-&quot;</code> opens <font SIZE="-1">STDIN</font> and opening <code>&quot;&gt;-&quot;</code> opens <font SIZE="-1">STDOUT.</font> </p>
<p> You may (and usually should) use the three-argument form of open to specify I/O layers (sometimes referred to as ``disciplines&#8217;&#8216;) to apply to the handle that affect how the input and output are processed (see open and PerlIO for more details). For example: </p>
<pre><code>  open(my $fh, &quot;&lt;:encoding(UTF-8)&quot;, $filename)
    || die &quot;Can't open UTF-8 encoded $filename: $!&quot;;
</code></pre>
<p> opens the UTF8-encoded file containing Unicode characters; see perluniintro. Note that if layers are specified in the three-argument form, then default layers stored in ${^OPEN} (see perlvar; usually set by the open pragma or the switch <code>&quot;-CioD&quot;</code>) are ignored. Those layers will also be ignored if you specify a colon with no name following it. In that case the default layer for the operating system (:raw on Unix, :crlf on Windows) is used. </p>
<p> Open returns nonzero on success, the undefined value otherwise. If the <code>&quot;open&quot;</code> involved a pipe, the return value happens to be the pid of the subprocess. </p>
<p> On some systems (in general, <font SIZE="-1">DOS-</font> and Windows-based systems) <code>&quot;binmode&quot;</code> is necessary when you&#8217;re not working with a text file. For the sake of portability it is a good idea always to use it when appropriate, and never to use it when it isn&#8217;t appropriate. Also, people can set their I/O to be by default UTF8-encoded Unicode, not bytes. </p>
<p> When opening a file, it&#8217;s seldom a good idea to continue if the request failed, so <code>&quot;open&quot;</code> is frequently used with <code>&quot;die&quot;</code>. Even if <code>&quot;die&quot;</code> won&#8217;t do what you want (say, in a <font SIZE="-1">CGI</font> script, where you want to format a suitable error message (but there are modules that can help with that problem)) always check the return value from opening a file. </p>
<p> The filehandle will be closed when its reference count reaches zero. If it is a lexically scoped variable declared with <code>&quot;my&quot;</code>, that usually means the end of the enclosing scope. However, this automatic close does not check for errors, so it is better to explicitly close filehandles, especially those used for writing: </p>
<pre><code>    close($handle)
       || warn &quot;close failed: $!&quot;;
</code></pre>
<p> An older style is to use a bareword as the filehandle, as </p>
<pre><code>    open(FH, &quot;&lt;&quot;, &quot;input.txt&quot;)
       or die &quot;Can't open &lt; input.txt: $!&quot;;
</code></pre>
<p> Then you can use <code>&quot;FH&quot;</code> as the filehandle, in <code>&quot;close FH&quot;</code> and <code>&quot;&lt;FH&gt;&quot;</code> and so on. Note that it&#8217;s a global variable, so this form is not recommended in new code. </p>
<p> As a shortcut a one-argument call takes the filename from the global scalar variable of the same name as the filehandle: </p>
<pre><code>    $ARTICLE = 100;
    open(ARTICLE) or die &quot;Can't find article $ARTICLE: $!\n&quot;;
</code></pre>
<p> Here <code>$ARTICLE</code> must be a global (package) scalar variable - not one declared with <code>&quot;my&quot;</code> or <code>&quot;state&quot;</code>. </p>
<p> As a special case the three-argument form with a read/write mode and the third argument being <code>&quot;undef&quot;</code>: </p>
<pre><code>    open(my $tmp, &quot;+&gt;&quot;, undef) or die ...
</code></pre>
<p> opens a filehandle to a newly created empty anonymous temporary file. (This happens under any mode, which makes <code>&quot;+&gt;&quot;</code> the only useful and sensible mode to use.) You will need to <code>&quot;seek&quot;</code> to do the reading. </p>
<p> Perl is built using PerlIO by default. Unless you&#8217;ve changed this (such as building Perl with <code>&quot;Configure -Uuseperlio&quot;</code>), you can open filehandles directly to Perl scalars via: </p>
<pre><code>    open(my $fh, &quot;&gt;&quot;, \$variable) || ..
</code></pre>
<p> To (re)open <code>&quot;STDOUT&quot;</code> or <code>&quot;STDERR&quot;</code> as an in-memory file, close it first: </p>
<pre><code>    close STDOUT;
    open(STDOUT, &quot;&gt;&quot;, \$variable)
        or die &quot;Can't open STDOUT: $!&quot;;
</code></pre>
<p> The scalars for in-memory files are treated as octet strings: unless the file is being opened with truncation the scalar may not contain any code points over 0xFF. </p>
<p> Opening in-memory files <i>can</i> fail for a variety of reasons. As with any other <code>&quot;open&quot;</code>, check the return value for success. </p>
<p> See perliol for detailed info on PerlIO. </p>
<p> General examples: </p>
<pre><code> open(my $log, &quot;&gt;&gt;&quot;, &quot;/usr/spool/news/twitlog&quot;);
 # if the open fails, output is discarded
 open(my $dbase, &quot;+&lt;&quot;, &quot;dbase.mine&quot;) # open for update
     or die &quot;Can't open 'dbase.mine' for update: $!&quot;;
 open(my $dbase, &quot;+&lt;dbase.mine&quot;) # ditto
     or die &quot;Can't open 'dbase.mine' for update: $!&quot;;
 open(my $article_fh, &quot;-|&quot;, &quot;caesar &lt;$article&quot;) # decrypt
                                                 # article
     or die &quot;Can't start caesar: $!&quot;;
 open(my $article_fh, &quot;caesar &lt;$article |&quot;) # ditto
     or die &quot;Can't start caesar: $!&quot;;
 open(my $out_fh, &quot;|-&quot;, &quot;sort &gt;Tmp$$&quot;) # $$ is our process id
     or die &quot;Can't start sort: $!&quot;;
 # in-memory files
 open(my $memory, &quot;&gt;&quot;, \$var)
     or die &quot;Can't open memory file: $!&quot;;
 print $memory &quot;foo!\n&quot;; # output will appear in $var
</code></pre>
<p> You may also, in the Bourne shell tradition, specify an <font SIZE="-1">EXPR</font> beginning with <code>&quot;&gt;&amp;&quot;</code>, in which case the rest of the string is interpreted as the name of a filehandle (or file descriptor, if numeric) to be duped (as in <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2)) and opened. You may use <code>&quot;&amp;&quot;</code> after <code>&quot;&gt;&quot;</code>, <code>&quot;&gt;&gt;&quot;</code>, <code>&quot;&lt;&quot;</code>, <code>&quot;+&gt;&quot;</code>, <code>&quot;+&gt;&gt;&quot;</code>, and <code>&quot;+&lt;&quot;</code>. The mode you specify should match the mode of the original filehandle. (Duping a filehandle does not take into account any existing contents of <font SIZE="-1">IO</font> buffers.) If you use the three-argument form, then you can pass either a number, the name of a filehandle, or the normal ``reference to a glob&#8217;&#8216;. </p>
<p> Here is a script that saves, redirects, and restores <code>&quot;STDOUT&quot;</code> and <code>&quot;STDERR&quot;</code> using various methods: </p>
<pre><code>    #!/usr/bin/perl
    open(my $oldout, &quot;&gt;&amp;STDOUT&quot;) or die &quot;Can't dup STDOUT: $!&quot;;
    open(OLDERR, &quot;&gt;&amp;&quot;, \*STDERR) or die &quot;Can't dup STDERR: $!&quot;;
    open(STDOUT, '&gt;', &quot;foo.out&quot;) or die &quot;Can't redirect STDOUT: $!&quot;;
    open(STDERR, &quot;&gt;&amp;STDOUT&quot;) or die &quot;Can't dup STDOUT: $!&quot;;
    select STDERR; $| = 1; # make unbuffered
    select STDOUT; $| = 1; # make unbuffered
    print STDOUT &quot;stdout 1\n&quot;; # this works for
    print STDERR &quot;stderr 1\n&quot;; # subprocesses too
    open(STDOUT, &quot;&gt;&amp;&quot;, $oldout) or die &quot;Can't dup \$oldout: $!&quot;;
    open(STDERR, &quot;&gt;&amp;OLDERR&quot;) or die &quot;Can't dup OLDERR: $!&quot;;
    print STDOUT &quot;stdout 2\n&quot;;
    print STDERR &quot;stderr 2\n&quot;;
</code></pre>
<p> If you specify <code>&#8216;&lt;&amp;=X&#8217;</code>, where <code>&quot;X&quot;</code> is a file descriptor number or a filehandle, then Perl will do an equivalent of C&#8217;s <code><a href="/docs/linux/man/3-fdopen/">fdopen</a></code>(3) of that file descriptor (and not call <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2)); this is more parsimonious of file descriptors. For example: </p>
<pre><code>    # open for input, reusing the fileno of $fd
    open(my $fh, &quot;&lt;&amp;=&quot;, $fd)
</code></pre>
<p> or </p>
<pre><code>    open(my $fh, &quot;&lt;&amp;=$fd&quot;)
</code></pre>
<p> or </p>
<pre><code>    # open for append, using the fileno of $oldfh
    open(my $fh, &quot;&gt;&gt;&amp;=&quot;, $oldfh)
</code></pre>
<p> Being parsimonious on filehandles is also useful (besides being parsimonious) for example when something is dependent on file descriptors, like for example locking using <code>&quot;flock&quot;</code>. If you do just <code>&quot;open(my $A, &quot;&gt;&gt;&amp;&quot;, $B)&quot;</code>, the filehandle <code>$A</code> will not have the same file descriptor as <code>$B</code>, and therefore <code>&quot;flock($A)&quot;</code> will not <code>&quot;flock($B)&quot;</code> nor vice versa. But with <code>&quot;open(my $A, &quot;&gt;&gt;&amp;=&quot;, $B)&quot;</code>, the filehandles will share the same underlying system file descriptor. </p>
<p> Note that under Perls older than 5.8.0, Perl uses the standard C library&#8217;s&#8217; <code><a href="/docs/linux/man/3-fdopen/">fdopen</a></code>(3) to implement the <code>&quot;=&quot;</code> functionality. On many Unix systems, <code><a href="/docs/linux/man/3-fdopen/">fdopen</a></code>(3) fails when file descriptors exceed a certain value, typically 255. For Perls 5.8.0 and later, PerlIO is (most often) the default. </p>
<p> You can see whether your Perl was built with PerlIO by running <code>&quot;perl -V:useperlio&quot;</code>. If it says <code>&#8216;define&#8217;</code>, you have PerlIO; otherwise you don&#8217;t. </p>
<p> If you open a pipe on the command <code>&quot;-&quot;</code> (that is, specify either <code>&quot;|-&quot;</code> or <code>&quot;-|&quot;</code> with the one- or two-argument forms of <code>&quot;open&quot;</code>), an implicit <code>&quot;fork&quot;</code> is done, so <code>&quot;open&quot;</code> returns twice: in the parent process it returns the pid of the child process, and in the child process it returns (a defined) <code>0</code>. Use <code>&quot;defined($pid)&quot;</code> or <code>&quot;//&quot;</code> to determine whether the open was successful. </p>
<p> For example, use either </p>
<pre><code>   my $child_pid = open(my $from_kid, &quot;-|&quot;) // die &quot;Can't fork: $!&quot;;
</code></pre>
<p> or </p>
<pre><code>   my $child_pid = open(my $to_kid, &quot;|-&quot;) // die &quot;Can't fork: $!&quot;;
</code></pre>
<p> followed by </p>
<pre><code>    if ($child_pid) {
        # am the parent:
        # either write $to_kid or else read $from_kid
        ...
       waitpid $child_pid, 0;
    } else {
        # am the child; use STDIN/STDOUT normally
        ...
        exit;
    }
</code></pre>
<p> The filehandle behaves normally for the parent, but I/O to that filehandle is piped from/to the <font SIZE="-1">STDOUT/STDIN</font> of the child process. In the child process, the filehandle isn&#8217;t opened---I/O happens from/to the new <font SIZE="-1">STDOUT/STDIN.</font> Typically this is used like the normal piped open when you want to exercise more control over just how the pipe command gets executed, such as when running setuid and you don&#8217;t want to have to scan shell commands for metacharacters. </p>
<p> The following blocks are more or less equivalent: </p>
<pre><code>    open(my $fh, &quot;|tr '[a-z]' '[A-Z]'&quot;);
    open(my $fh, &quot;|-&quot;, &quot;tr '[a-z]' '[A-Z]'&quot;);
    open(my $fh, &quot;|-&quot;) || exec 'tr', '[a-z]', '[A-Z]';
    open(my $fh, &quot;|-&quot;, &quot;tr&quot;, '[a-z]', '[A-Z]');
    open(my $fh, &quot;cat -n '$file'|&quot;);
    open(my $fh, &quot;-|&quot;, &quot;cat -n '$file'&quot;);
    open(my $fh, &quot;-|&quot;) || exec &quot;cat&quot;, &quot;-n&quot;, $file;
    open(my $fh, &quot;-|&quot;, &quot;cat&quot;, &quot;-n&quot;, $file);
</code></pre>
<p> The last two examples in each block show the pipe as ``list form&#8217;&#8216;, which is not yet supported on all platforms. A good rule of thumb is that if your platform has a real <code>&quot;fork&quot;</code> (in other words, if your platform is Unix, including Linux and MacOS X), you can use the list form. You would want to use the list form of the pipe so you can pass literal arguments to the command without risk of the shell interpreting any shell metacharacters in them. However, this also bars you from opening pipes to commands that intentionally contain shell metacharacters, such as: </p>
<pre><code>    open(my $fh, &quot;|cat -n | expand -4 | lpr&quot;)
        || die &quot;Can't open pipeline to lpr: $!&quot;;
</code></pre>
<p> See ``Safe Pipe Opens&#8217;&#8216; in perlipc for more examples of this. </p>
<p> Perl will attempt to flush all files opened for output before any operation that may do a fork, but this may not be supported on some platforms (see perlport). To be safe, you may need to set <code>$|</code> (<code>$AUTOFLUSH</code> in English) or call the <code>&quot;autoflush&quot;</code> method of <code>&quot;IO::Handle&quot;</code> on any open handles. </p>
<p> On systems that support a close-on-exec flag on files, the flag will be set for the newly opened file descriptor as determined by the value of <code>$^F</code>. See ``$^F&#8217;&#8216; in perlvar. </p>
<p> Closing any piped filehandle causes the parent process to wait for the child to finish, then returns the status value in <code>$?</code> and <code>&quot;${^CHILD_ERROR_NATIVE}&quot;</code>. </p>
<p> The filename passed to the one- and two-argument forms of <code>&quot;open&quot;</code> will have leading and trailing whitespace deleted and normal redirection characters honored. This property, known as ``magic open&#8217;&#8216;, can often be used to good effect. A user could specify a filename of <i>``rsh cat file |&#8216;&#8216;</i>, or you could change certain filenames as needed: </p>
<pre><code>    $filename =~ s/(.*\.gz)\s*$/gzip -dc &lt; $1|/;
    open(my $fh, $filename) or die &quot;Can't open $filename: $!&quot;;
</code></pre>
<p> Use the three-argument form to open a file with arbitrary weird characters in it, </p>
<pre><code>    open(my $fh, &quot;&lt;&quot;, $file)
        || die &quot;Can't open $file: $!&quot;;
</code></pre>
<p> otherwise it&#8217;s necessary to protect any leading and trailing whitespace: </p>
<pre><code>    $file =~ s#^(\s)#./$1#;
    open(my $fh, &quot;&lt; $file\0&quot;)
        || die &quot;Can't open $file: $!&quot;;
</code></pre>
<p> (this may not work on some bizarre filesystems). One should conscientiously choose between the <i>magic</i> and <i>three-argument</i> form of <code>&quot;open&quot;</code>: </p>
<pre><code>    open(my $in, $ARGV[0]) || die &quot;Can't open $ARGV[0]: $!&quot;;
</code></pre>
<p> will allow the user to specify an argument of the form <code>&quot;rsh cat file |&quot;</code>, but will not work on a filename that happens to have a trailing space, while </p>
<pre><code>    open(my $in, &quot;&lt;&quot;, $ARGV[0])
        || die &quot;Can't open $ARGV[0]: $!&quot;;
</code></pre>
<p> will have exactly the opposite restrictions. (However, some shells support the syntax <code>&quot;perl your_program.pl &lt;( rsh cat file )&quot;</code>, which produces a filename that can be opened normally.) </p>
<p> If you want a ``real&#8217;&#8216; C <code><a href="/docs/linux/man/2-open/">open</a></code>(2), then you should use the <code>&quot;sysopen&quot;</code> function, which involves no such magic (but uses different filemodes than Perl <code>&quot;open&quot;</code>, which corresponds to C <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3)). This is another way to protect your filenames from interpretation. For example: </p>
<pre><code>    use IO::Handle;
    sysopen(my $fh, $path, O_RDWR|O_CREAT|O_EXCL)
        or die &quot;Can't open $path: $!&quot;;
    $fh-&gt;autoflush(1);
    print $fh &quot;stuff $$\n&quot;;
    seek($fh, 0, 0);
    print &quot;File contains: &quot;, readline($fh);
</code></pre>
<p> See <code>&quot;seek&quot;</code> for some details about mixing reading and writing. </p>
<p> Portability issues: ``open&#8217;&#8216; in perlport. </p>
 </dd>
<dt>opendir <font SIZE="-1">DIRHANDLE,EXPR</font></dt>
<dd> <p> Opens a directory named <font SIZE="-1">EXPR</font> for processing by <code>&quot;readdir&quot;</code>, <code>&quot;telldir&quot;</code>, <code>&quot;seekdir&quot;</code>, <code>&quot;rewinddir&quot;</code>, and <code>&quot;closedir&quot;</code>. Returns true if successful. <font SIZE="-1">DIRHANDLE</font> may be an expression whose value can be used as an indirect dirhandle, usually the real dirhandle name. If <font SIZE="-1">DIRHANDLE</font> is an undefined scalar variable (or array or hash element), the variable is assigned a reference to a new anonymous dirhandle; that is, it&#8217;s autovivified. Dirhandles are the same objects as filehandles; an I/O object can only be open as one of these handle types at once. </p>
<p> See the example at <code>&quot;readdir&quot;</code>. </p>
 </dd>
<dt>ord <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>ord</dt>
<dd> <p> Returns the numeric value of the first character of <font SIZE="-1">EXPR.</font> If <font SIZE="-1">EXPR</font> is an empty string, returns 0. If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. (Note <i>character</i>, not byte.) </p>
<p> For the reverse, see <code>&quot;chr&quot;</code>. See perlunicode for more about Unicode. </p>
 </dd>
<dt>our <font SIZE="-1">VARLIST</font></dt>
<dd>  </dd>
<dt>our <font SIZE="-1">TYPE VARLIST</font></dt>
<dd>  </dd>
<dt>our <font SIZE="-1">VARLIST : ATTRS</font></dt>
<dd>  </dd>
<dt>our <font SIZE="-1">TYPE VARLIST : ATTRS</font></dt>
<dd> <p> <code>&quot;our&quot;</code> makes a lexical alias to a package (i.e. global) variable of the same name in the current package for use within the current lexical scope. </p>
<p> <code>&quot;our&quot;</code> has the same scoping rules as <code>&quot;my&quot;</code> or <code>&quot;state&quot;</code>, meaning that it is only valid within a lexical scope. Unlike <code>&quot;my&quot;</code> and <code>&quot;state&quot;</code>, which both declare new (lexical) variables, <code>&quot;our&quot;</code> only creates an alias to an existing variable: a package variable of the same name. </p>
<p> This means that when <code>&quot;use strict &#8216;vars&#8217;&quot;</code> is in effect, <code>&quot;our&quot;</code> lets you use a package variable without qualifying it with the package name, but only within the lexical scope of the <code>&quot;our&quot;</code> declaration. This applies immediately---even within the same statement. </p>
<pre><code>    package Foo;
    use strict;
    $Foo::foo = 23;
    {
        our $foo; # alias to $Foo::foo
        print $foo; # prints 23
    }
    print $Foo::foo; # prints 23
    print $foo; # ERROR: requires explicit package name
</code></pre>
<p> This works even if the package variable has not been used before, as package variables spring into existence when first used. </p>
<pre><code>    package Foo;
    use strict;
    our $foo = 23; # just like $Foo::foo = 23
    print $Foo::foo; # prints 23
</code></pre>
<p> Because the variable becomes legal immediately under <code>&quot;use strict &#8216;vars&#8217;&quot;</code>, so long as there is no variable with that name is already in scope, you can then reference the package variable again even within the same statement. </p>
<pre><code>    package Foo;
    use strict;
    my $foo = $foo; # error, undeclared $foo on right-hand side
    our $foo = $foo; # no errors
</code></pre>
<p> If more than one variable is listed, the list must be placed in parentheses. </p>
<pre><code>    our($bar, $baz);
</code></pre>
<p> An <code>&quot;our&quot;</code> declaration declares an alias for a package variable that will be visible across its entire lexical scope, even across package boundaries. The package in which the variable is entered is determined at the point of the declaration, not at the point of use. This means the following behavior holds: </p>
<pre><code>    package Foo;
    our $bar; # declares $Foo::bar for rest of lexical scope
    $bar = 20;
    package Bar;
    print $bar; # prints 20, as it refers to $Foo::bar
</code></pre>
<p> Multiple <code>&quot;our&quot;</code> declarations with the same name in the same lexical scope are allowed if they are in different packages. If they happen to be in the same package, Perl will emit warnings if you have asked for them, just like multiple <code>&quot;my&quot;</code> declarations. Unlike a second <code>&quot;my&quot;</code> declaration, which will bind the name to a fresh variable, a second <code>&quot;our&quot;</code> declaration in the same package, in the same scope, is merely redundant. </p>
<pre><code>    use warnings;
    package Foo;
    our $bar; # declares $Foo::bar for rest of lexical scope
    $bar = 20;
    package Bar;
    our $bar = 30; # declares $Bar::bar for rest of lexical scope
    print $bar; # prints 30
    our $bar; # emits warning but has no other effect
    print $bar; # still prints 30
</code></pre>
<p> An <code>&quot;our&quot;</code> declaration may also have a list of attributes associated with it. </p>
<p> The exact semantics and interface of <font SIZE="-1">TYPE</font> and <font SIZE="-1">ATTRS</font> are still evolving. <font SIZE="-1">TYPE</font> is currently bound to the use of the fields pragma, and attributes are handled using the attributes pragma, or, starting from Perl 5.8.0, also via the Attribute::Handlers module. See ``Private Variables via <code>my()</code>&#8216;&#8216; in perlsub for details. </p>
<p> Note that with a parenthesised list, <code>&quot;undef&quot;</code> can be used as a dummy placeholder, for example to skip assignment of initial values: </p>
<pre><code>    our ( undef, $min, $hour ) = localtime;
</code></pre>
<p> <code>&quot;our&quot;</code> differs from <code>&quot;use vars&quot;</code>, which allows use of an unqualified name <i>only</i> within the affected package, but across scopes. </p>
 </dd>
<dt>pack <font SIZE="-1">TEMPLATE,LIST</font></dt>
<dd> <p> Takes a <font SIZE="-1">LIST</font> of values and converts it into a string using the rules given by the <font SIZE="-1">TEMPLATE.</font> The resulting string is the concatenation of the converted values. Typically, each converted value looks like its machine-level representation. For example, on 32-bit machines an integer may be represented by a sequence of 4 bytes, which will in Perl be presented as a string that&#8217;s 4 characters long. </p>
<p> See perlpacktut for an introduction to this function. </p>
<p> The <font SIZE="-1">TEMPLATE</font> is a sequence of characters that give the order and type of values, as follows: </p>
<pre><code>    a A string with arbitrary binary data, will be null padded.
    A A text (ASCII) string, will be space padded.
    Z A null-terminated (ASCIZ) string, will be null padded.
    b A bit string (ascending bit order inside each byte,
       like vec()).
    B A bit string (descending bit order inside each byte).
    h A hex string (low nybble first).
    H A hex string (high nybble first).
    c A signed char (8-bit) value.
    C An unsigned char (octet) value.
    W An unsigned char value (can be greater than 255).
    s A signed short (16-bit) value.
    S An unsigned short value.
    l A signed long (32-bit) value.
    L An unsigned long value.
    q A signed quad (64-bit) value.
    Q An unsigned quad value.
         (Quads are available only if your system supports 64-bit
          integer values _and_ if Perl has been compiled to support
          those. Raises an exception otherwise.)
    i A signed integer value.
    I An unsigned integer value.
         (This 'integer' is _at_least_ 32 bits wide. Its exact
          size depends on what a local C compiler calls 'int'.)
    n An unsigned short (16-bit) in &quot;network&quot; (big-endian) order.
    N An unsigned long (32-bit) in &quot;network&quot; (big-endian) order.
    v An unsigned short (16-bit) in &quot;VAX&quot; (little-endian) order.
    V An unsigned long (32-bit) in &quot;VAX&quot; (little-endian) order.
    j A Perl internal signed integer value (IV).
    J A Perl internal unsigned integer value (UV).
    f A single-precision float in native format.
    d A double-precision float in native format.
    F A Perl internal floating-point value (NV) in native format
    D A float of long-double precision in native format.
         (Long doubles are available only if your system supports
          long double values _and_ if Perl has been compiled to
          support those. Raises an exception otherwise.
          Note that there are different long double formats.)
    p A pointer to a null-terminated string.
    P A pointer to a structure (fixed-length string).
    u A uuencoded string.
    U A Unicode character number. Encodes to a character in char-
       acter mode and UTF-8 (or UTF-EBCDIC in EBCDIC platforms) in
       byte mode.
    w A BER compressed integer (not an ASN.1 BER, see perlpacktut
       for details). Its bytes represent an unsigned integer in
       base 128, most significant digit first, with as few digits
       as possible. Bit eight (the high bit) is set on each byte
       except the last.
    x A null byte (a.k.a ASCII NUL, &quot;\000&quot;, chr(0))
    X Back up a byte.
    @ Null-fill or truncate to absolute position, counted from the
       start of the innermost ()-group.
    . Null-fill or truncate to absolute position specified by
       the value.
    ( Start of a ()-group.
</code></pre>
<p> One or more modifiers below may optionally follow certain letters in the <font SIZE="-1">TEMPLATE</font> (the second column lists letters for which the modifier is valid): </p>
<pre><code>    ! sSlLiI Forces native (short, long, int) sizes instead
                   of fixed (16-/32-bit) sizes.
    ! xX Make x and X act as alignment commands.
    ! nNvV Treat integers as signed instead of unsigned.
    ! @. Specify position as byte offset in the internal
                   representation of the packed string. Efficient
                   but dangerous.
    &gt; sSiIlLqQ Force big-endian byte-order on the type.
        jJfFdDpP (The &quot;big end&quot; touches the construct.)
    &lt; sSiIlLqQ Force little-endian byte-order on the type.
        jJfFdDpP (The &quot;little end&quot; touches the construct.)
</code></pre>
<p> The <code>&quot;&gt;&quot;</code> and <code>&quot;&lt;&quot;</code> modifiers can also be used on <code>&quot;()&quot;</code> groups to force a particular byte-order on all components in that group, including all its subgroups. </p>
<p> The following rules apply: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Each letter may optionally be followed by a number indicating the repeat count. A numeric repeat count may optionally be enclosed in brackets, as in <code>&quot;pack(&quot;C[80]&quot;, @arr)&quot;</code>. The repeat count gobbles that many values from the <font SIZE="-1">LIST</font> when used with all format types other than <code>&quot;a&quot;</code>, <code>&quot;A&quot;</code>, <code>&quot;Z&quot;</code>, <code>&quot;b&quot;</code>, <code>&quot;B&quot;</code>, <code>&quot;h&quot;</code>, <code>&quot;H&quot;</code>, <code>&quot;@&quot;</code>, <code>&quot;.&quot;</code>, <code>&quot;x&quot;</code>, <code>&quot;X&quot;</code>, and <code>&quot;P&quot;</code>, where it means something else, described below. Supplying a <code>&quot;*&quot;</code> for the repeat count instead of a number means to use however many items are left, except for: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;@&quot;</code>, <code>&quot;x&quot;</code>, and <code>&quot;X&quot;</code>, where it is equivalent to <code>0</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &lt;.&gt;, where it means relative to the start of the string. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;u&quot;</code>, where it is equivalent to 1 (or 45, which here is equivalent). </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> One can replace a numeric repeat count with a template letter enclosed in brackets to use the packed byte length of the bracketed template for the repeat count. </p>
<p> For example, the template <code>&quot;x[L]&quot;</code> skips as many bytes as in a packed long, and the template <code>&quot;$t X[$t] $t&quot;</code> unpacks twice whatever <code>$t</code> (when variable-expanded) unpacks. If the template in brackets contains alignment commands (such as <code>&quot;x![d]&quot;</code>), its packed length is calculated as if the start of the template had the maximal possible alignment. </p>
<p> When used with <code>&quot;Z&quot;</code>, a <code>&quot;*&quot;</code> as the repeat count is guaranteed to add a trailing null byte, so the resulting string is always one byte longer than the byte length of the item itself. </p>
<p> When used with <code>&quot;@&quot;</code>, the repeat count represents an offset from the start of the innermost <code>&quot;()&quot;</code> group. </p>
<p> When used with <code>&quot;.&quot;</code>, the repeat count determines the starting position to calculate the value offset as follows: </p>
 </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> If the repeat count is <code>0</code>, it&#8217;s relative to the current position. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If the repeat count is <code>&quot;*&quot;</code>, the offset is relative to the start of the packed string. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> And if it&#8217;s an integer <i>n</i>, the offset is relative to the start of the <i>n</i>th innermost <code>&quot;( )&quot;</code> group, or to the start of the string if <i>n</i> is bigger then the group level. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> The repeat count for <code>&quot;u&quot;</code> is interpreted as the maximal number of bytes to encode per line of output, with 0, 1 and 2 replaced by 45. The repeat count should not be more than 65. </p>
 </dd></dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;a&quot;</code>, <code>&quot;A&quot;</code>, and <code>&quot;Z&quot;</code> types gobble just one value, but pack it as a string of length count, padding with nulls or spaces as needed. When unpacking, <code>&quot;A&quot;</code> strips trailing whitespace and nulls, <code>&quot;Z&quot;</code> strips everything after the first null, and <code>&quot;a&quot;</code> returns data with no stripping at all. </p>
<p> If the value to pack is too long, the result is truncated. If it&#8217;s too long and an explicit count is provided, <code>&quot;Z&quot;</code> packs only <code>&quot;$count-1&quot;</code> bytes, followed by a null byte. Thus <code>&quot;Z&quot;</code> always packs a trailing null, except when the count is 0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Likewise, the <code>&quot;b&quot;</code> and <code>&quot;B&quot;</code> formats pack a string that&#8217;s that many bits long. Each such format generates 1 bit of the result. These are typically followed by a repeat count like <code>&quot;B8&quot;</code> or <code>&quot;B64&quot;</code>. </p>
<p> Each result bit is based on the least-significant bit of the corresponding input character, i.e., on <code>&quot;ord($char)%2&quot;</code>. In particular, characters <code>&quot;0&quot;</code> and <code>&quot;1&quot;</code> generate bits 0 and 1, as do characters <code>&quot;\000&quot;</code> and <code>&quot;\001&quot;</code>. </p>
<p> Starting from the beginning of the input string, each 8-tuple of characters is converted to 1 character of output. With format <code>&quot;b&quot;</code>, the first character of the 8-tuple determines the least-significant bit of a character; with format <code>&quot;B&quot;</code>, it determines the most-significant bit of a character. </p>
<p> If the length of the input string is not evenly divisible by 8, the remainder is packed as if the input string were padded by null characters at the end. Similarly during unpacking, ``extra&#8217;&#8216; bits are ignored. </p>
<p> If the input string is longer than needed, remaining characters are ignored. </p>
<p> A <code>&quot;*&quot;</code> for the repeat count uses all characters of the input field. On unpacking, bits are converted to a string of <code>0</code>s and <code>1</code>s. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;h&quot;</code> and <code>&quot;H&quot;</code> formats pack a string that many nybbles (4-bit groups, representable as hexadecimal digits, <code>&quot;0&quot;..&quot;9&quot;</code> <code>&quot;a&quot;..&quot;f&quot;</code>) long. </p>
<p> For each such format, <code>&quot;pack&quot;</code> generates 4 bits of result. With non-alphabetical characters, the result is based on the 4 least-significant bits of the input character, i.e., on <code>&quot;ord($char)%16&quot;</code>. In particular, characters <code>&quot;0&quot;</code> and <code>&quot;1&quot;</code> generate nybbles 0 and 1, as do bytes <code>&quot;\000&quot;</code> and <code>&quot;\001&quot;</code>. For characters <code>&quot;a&quot;..&quot;f&quot;</code> and <code>&quot;A&quot;..&quot;F&quot;</code>, the result is compatible with the usual hexadecimal digits, so that <code>&quot;a&quot;</code> and <code>&quot;A&quot;</code> both generate the nybble <code>&quot;0xA==10&quot;</code>. Use only these specific hex characters with this format. </p>
<p> Starting from the beginning of the template to <code>&quot;pack&quot;</code>, each pair of characters is converted to 1 character of output. With format <code>&quot;h&quot;</code>, the first character of the pair determines the least-significant nybble of the output character; with format <code>&quot;H&quot;</code>, it determines the most-significant nybble. </p>
<p> If the length of the input string is not even, it behaves as if padded by a null character at the end. Similarly, ``extra&#8217;&#8216; nybbles are ignored during unpacking. </p>
<p> If the input string is longer than needed, extra characters are ignored. </p>
<p> A <code>&quot;*&quot;</code> for the repeat count uses all characters of the input field. For <code>&quot;unpack&quot;</code>, nybbles are converted to a string of hexadecimal digits. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;p&quot;</code> format packs a pointer to a null-terminated string. You are responsible for ensuring that the string is not a temporary value, as that could potentially get deallocated before you got around to using the packed result. The <code>&quot;P&quot;</code> format packs a pointer to a structure of the size indicated by the length. A null pointer is created if the corresponding value for <code>&quot;p&quot;</code> or <code>&quot;P&quot;</code> is <code>&quot;undef&quot;</code>; similarly with <code>&quot;unpack&quot;</code>, where a null pointer unpacks into <code>&quot;undef&quot;</code>. </p>
<p> If your system has a strange pointer size---meaning a pointer is neither as big as an int nor as big as a long---it may not be possible to pack or unpack pointers in big- or little-endian byte order. Attempting to do so raises an exception. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;/&quot;</code> template character allows packing and unpacking of a sequence of items where the packed structure contains a packed item count followed by the packed items themselves. This is useful when the structure you&#8217;re unpacking has encoded the sizes or repeat counts for some of its fields within the structure itself as separate fields. </p>
<p> For <code>&quot;pack&quot;</code>, you write <i>length-item</i><code>&quot;/&quot;</code><i>sequence-item</i>, and the <i>length-item</i> describes how the length value is packed. Formats likely to be of most use are integer-packing ones like <code>&quot;n&quot;</code> for Java strings, <code>&quot;w&quot;</code> for <font SIZE="-1">ASN.1</font> or <font SIZE="-1">SNMP,</font> and <code>&quot;N&quot;</code> for Sun <font SIZE="-1">XDR.</font> </p>
<p> For <code>&quot;pack&quot;</code>, <i>sequence-item</i> may have a repeat count, in which case the minimum of that and the number of available items is used as the argument for <i>length-item</i>. If it has no repeat count or uses a &#8216;*&#8216;, the number of available items is used. </p>
<p> For <code>&quot;unpack&quot;</code>, an internal stack of integer arguments unpacked so far is used. You write <code>&quot;/&quot;</code><i>sequence-item</i> and the repeat count is obtained by popping off the last element from the stack. The <i>sequence-item</i> must not have a repeat count. </p>
<p> If <i>sequence-item</i> refers to a string type (<code>&quot;A&quot;</code>, <code>&quot;a&quot;</code>, or <code>&quot;Z&quot;</code>), the <i>length-item</i> is the string length, not the number of strings. With an explicit repeat count for pack, the packed string is adjusted to that length. For example: </p>
<pre><code> This code: gives this result:
 unpack(&quot;W/a&quot;, &quot;\004Gurusamy&quot;) (&quot;Guru&quot;)
 unpack(&quot;a3/A A*&quot;, &quot;007 Bond J &quot;) (&quot; Bond&quot;, &quot;J&quot;)
 unpack(&quot;a3 x2 /A A*&quot;, &quot;007: Bond, J.&quot;) (&quot;Bond, J&quot;, &quot;.&quot;)
 pack(&quot;n/a* w/a&quot;,&quot;hello,&quot;,&quot;world&quot;) &quot;\000\006hello,\005world&quot;
 pack(&quot;a/W2&quot;, ord(&quot;a&quot;) .. ord(&quot;z&quot;)) &quot;2ab&quot;
</code></pre>
<p> The <i>length-item</i> is not returned explicitly from <code>&quot;unpack&quot;</code>. </p>
<p> Supplying a count to the <i>length-item</i> format letter is only useful with <code>&quot;A&quot;</code>, <code>&quot;a&quot;</code>, or <code>&quot;Z&quot;</code>. Packing with a <i>length-item</i> of <code>&quot;a&quot;</code> or <code>&quot;Z&quot;</code> may introduce <code>&quot;\000&quot;</code> characters, which Perl does not regard as legal in numeric strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The integer types <code>&quot;s&quot;</code>, <code>&quot;S&quot;</code>, <code>&quot;l&quot;</code>, and <code>&quot;L&quot;</code> may be followed by a <code>&quot;!&quot;</code> modifier to specify native shorts or longs. As shown in the example above, a bare <code>&quot;l&quot;</code> means exactly 32 bits, although the native <code>&quot;long&quot;</code> as seen by the local C compiler may be larger. This is mainly an issue on 64-bit platforms. You can see whether using <code>&quot;!&quot;</code> makes any difference this way: </p>
<pre><code>    printf &quot;format s is %d, s! is %d\n&quot;,
        length pack(&quot;s&quot;), length pack(&quot;s!&quot;);
    printf &quot;format l is %d, l! is %d\n&quot;,
        length pack(&quot;l&quot;), length pack(&quot;l!&quot;);
</code></pre>
<p> <code>&quot;i!&quot;</code> and <code>&quot;I!&quot;</code> are also allowed, but only for completeness&#8217; sake: they are identical to <code>&quot;i&quot;</code> and <code>&quot;I&quot;</code>. </p>
<p> The actual sizes (in bytes) of native shorts, ints, longs, and long longs on the platform where Perl was built are also available from the command line: </p>
<pre><code>    $ perl -V:{short,int,long{,long}}size
    shortsize='2';
    intsize='4';
    longsize='4';
    longlongsize='8';
</code></pre>
<p> or programmatically via the <code>&quot;Config&quot;</code> module: </p>
<pre><code>       use Config;
       print $Config{shortsize}, &quot;\n&quot;;
       print $Config{intsize}, &quot;\n&quot;;
       print $Config{longsize}, &quot;\n&quot;;
       print $Config{longlongsize}, &quot;\n&quot;;
</code></pre>
<p> <code>$Config{longlongsize}</code> is undefined on systems without long long support. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The integer formats <code>&quot;s&quot;</code>, <code>&quot;S&quot;</code>, <code>&quot;i&quot;</code>, <code>&quot;I&quot;</code>, <code>&quot;l&quot;</code>, <code>&quot;L&quot;</code>, <code>&quot;j&quot;</code>, and <code>&quot;J&quot;</code> are inherently non-portable between processors and operating systems because they obey native byteorder and endianness. For example, a 4-byte integer 0x12345678 (305419896 decimal) would be ordered natively (arranged in and handled by the <font SIZE="-1">CPU</font> registers) into bytes as </p>
<pre><code>    0x12 0x34 0x56 0x78 # big-endian
    0x78 0x56 0x34 0x12 # little-endian
</code></pre>
<p> Basically, Intel and <font SIZE="-1">VAX</font> CPUs are little-endian, while everybody else, including Motorola m68k/88k, <font SIZE="-1">PPC,</font> Sparc, <font SIZE="-1">HP PA,</font> Power, and Cray, are big-endian. Alpha and <font SIZE="-1">MIPS</font> can be either: Digital/Compaq uses (well, used) them in little-endian mode, but SGI/Cray uses them in big-endian mode. </p>
<p> The names <i>big-endian</i> and <i>little-endian</i> are comic references to the egg-eating habits of the little-endian Lilliputians and the big-endian Blefuscudians from the classic Jonathan Swift satire, <i>Gulliver&#8217;s Travels</i>. This entered computer lingo via the paper ``On Holy Wars and a Plea for Peace&#8217;&#8216; by Danny Cohen, <font SIZE="-1">USC/ISI IEN 137,</font> April 1, 1980. </p>
<p> Some systems may have even weirder byte orders such as </p>
<pre><code>   0x56 0x78 0x12 0x34
   0x34 0x12 0x78 0x56
</code></pre>
<p> These are called mid-endian, middle-endian, mixed-endian, or just weird. </p>
<p> You can determine your system endianness with this incantation: </p>
<pre><code>   printf(&quot;%#02x &quot;, $_) for unpack(&quot;W*&quot;, pack L=&gt;0x12345678);
</code></pre>
<p> The byteorder on the platform where Perl was built is also available via Config: </p>
<pre><code>    use Config;
    print &quot;$Config{byteorder}\n&quot;;
</code></pre>
<p> or from the command line: </p>
<pre><code>    $ perl -V:byteorder
</code></pre>
<p> Byteorders <code>&quot;1234&quot;</code> and <code>&quot;12345678&quot;</code> are little-endian; <code>&quot;4321&quot;</code> and <code>&quot;87654321&quot;</code> are big-endian. Systems with multiarchitecture binaries will have <code>&quot;ffff&quot;</code>, signifying that static information doesn&#8217;t work, one must use runtime probing. </p>
<p> For portably packed integers, either use the formats <code>&quot;n&quot;</code>, <code>&quot;N&quot;</code>, <code>&quot;v&quot;</code>, and <code>&quot;V&quot;</code> or else use the <code>&quot;&gt;&quot;</code> and <code>&quot;&lt;&quot;</code> modifiers described immediately below. See also perlport. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Also floating point numbers have endianness. Usually (but not always) this agrees with the integer endianness. Even though most platforms these days use the <font SIZE="-1">IEEE 754</font> binary format, there are differences, especially if the long doubles are involved. You can see the <code>&quot;Config&quot;</code> variables <code>&quot;doublekind&quot;</code> and <code>&quot;longdblkind&quot;</code> (also <code>&quot;doublesize&quot;</code>, <code>&quot;longdblsize&quot;</code>): the ``kind&#8217;&#8216; values are enums, unlike <code>&quot;byteorder&quot;</code>. </p>
<p> Portability-wise the best option is probably to keep to the <font SIZE="-1">IEEE 754</font> 64-bit doubles, and of agreed-upon endianness. Another possibility is the <code>&quot;%a&quot;</code>) format of <code>&quot;printf&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Starting with Perl 5.10.0, integer and floating-point formats, along with the <code>&quot;p&quot;</code> and <code>&quot;P&quot;</code> formats and <code>&quot;()&quot;</code> groups, may all be followed by the <code>&quot;&gt;&quot;</code> or <code>&quot;&lt;&quot;</code> endianness modifiers to respectively enforce big- or little-endian byte-order. These modifiers are especially useful given how <code>&quot;n&quot;</code>, <code>&quot;N&quot;</code>, <code>&quot;v&quot;</code>, and <code>&quot;V&quot;</code> don&#8217;t cover signed integers, 64-bit integers, or floating-point values. </p>
<p> Here are some concerns to keep in mind when using an endianness modifier: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Exchanging signed integers between different platforms works only when all platforms store them in the same format. Most platforms store signed integers in two&#8217;s-complement notation, so usually this is not an issue. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;&gt;&quot;</code> or <code>&quot;&lt;&quot;</code> modifiers can only be used on floating-point formats on big- or little-endian machines. Otherwise, attempting to use them raises an exception. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Forcing big- or little-endian byte-order on floating-point values for data exchange can work only if all platforms use the same binary representation such as <font SIZE="-1">IEEE</font> floating-point. Even if all platforms are using <font SIZE="-1">IEEE,</font> there may still be subtle differences. Being able to use <code>&quot;&gt;&quot;</code> or <code>&quot;&lt;&quot;</code> on floating-point values can be useful, but also dangerous if you don&#8217;t know exactly what you&#8217;re doing. It is not a general way to portably store floating-point values. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When using <code>&quot;&gt;&quot;</code> or <code>&quot;&lt;&quot;</code> on a <code>&quot;()&quot;</code> group, this affects all types inside the group that accept byte-order modifiers, including all subgroups. It is silently ignored for all other types. You are not allowed to override the byte-order within a group that already has a byte-order modifier suffix. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Real numbers (floats and doubles) are in native machine format only. Due to the multiplicity of floating-point formats and the lack of a standard ``network&#8217;&#8216; representation for them, no facility for interchange has been made. This means that packed floating-point data written on one machine may not be readable on another, even if both use <font SIZE="-1">IEEE</font> floating-point arithmetic (because the endianness of the memory representation is not part of the <font SIZE="-1">IEEE</font> spec). See also perlport. </p>
<p> If you know <i>exactly</i> what you&#8217;re doing, you can use the <code>&quot;&gt;&quot;</code> or <code>&quot;&lt;&quot;</code> modifiers to force big- or little-endian byte-order on floating-point values. </p>
<p> Because Perl uses doubles (or long doubles, if configured) internally for all numeric calculation, converting from double into float and thence to double again loses precision, so <code>&quot;unpack(&quot;f&quot;, pack(&quot;f&quot;, $foo)&quot;</code>) will not in general equal <code>$foo</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pack and unpack can operate in two modes: character mode (<code>&quot;C0&quot;</code> mode) where the packed string is processed per character, and <font SIZE="-1">UTF-8</font> byte mode (<code>&quot;U0&quot;</code> mode) where the packed string is processed in its UTF-8-encoded Unicode form on a byte-by-byte basis. Character mode is the default unless the format string starts with <code>&quot;U&quot;</code>. You can always switch mode mid-format with an explicit <code>&quot;C0&quot;</code> or <code>&quot;U0&quot;</code> in the format. This mode remains in effect until the next mode change, or until the end of the <code>&quot;()&quot;</code> group it (directly) applies to. </p>
<p> Using <code>&quot;C0&quot;</code> to get Unicode characters while using <code>&quot;U0&quot;</code> to get <i>non</i>-Unicode bytes is not necessarily obvious. Probably only the first of these is what you want: </p>
<pre><code>    $ perl -CS -E 'say &quot;\x{3B1}\x{3C9}&quot;' |
      perl -CS -ne 'printf &quot;%v04X\n&quot;, $_ for unpack(&quot;C0A*&quot;, $_)'
    03B1.03C9
    $ perl -CS -E 'say &quot;\x{3B1}\x{3C9}&quot;' |
      perl -CS -ne 'printf &quot;%v02X\n&quot;, $_ for unpack(&quot;U0A*&quot;, $_)'
    CE.B1.CF.89
    $ perl -CS -E 'say &quot;\x{3B1}\x{3C9}&quot;' |
      perl -C0 -ne 'printf &quot;%v02X\n&quot;, $_ for unpack(&quot;C0A*&quot;, $_)'
    CE.B1.CF.89
    $ perl -CS -E 'say &quot;\x{3B1}\x{3C9}&quot;' |
      perl -C0 -ne 'printf &quot;%v02X\n&quot;, $_ for unpack(&quot;U0A*&quot;, $_)'
    C3.8E.C2.B1.C3.8F.C2.89
</code></pre>
<p> Those examples also illustrate that you should not try to use <code>&quot;pack&quot;</code>/<code>&quot;unpack&quot;</code> as a substitute for the Encode module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You must yourself do any alignment or padding by inserting, for example, enough <code>&quot;x&quot;</code>es while packing. There is no way for <code>&quot;pack&quot;</code> and <code>&quot;unpack&quot;</code> to know where characters are going to or coming from, so they handle their output and input as flat sequences of characters. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A <code>&quot;()&quot;</code> group is a sub-TEMPLATE enclosed in parentheses. A group may take a repeat count either as postfix, or for <code>&quot;unpack&quot;</code>, also via the <code>&quot;/&quot;</code> template character. Within each repetition of a group, positioning with <code>&quot;@&quot;</code> starts over at 0. Therefore, the result of </p>
<pre><code>    pack(&quot;@1A((@2A)@3A)&quot;, qw[X Y Z])
</code></pre>
<p> is the string <code>&quot;\0X\0\0YZ&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;x&quot;</code> and <code>&quot;X&quot;</code> accept the <code>&quot;!&quot;</code> modifier to act as alignment commands: they jump forward or back to the closest position aligned at a multiple of <code>&quot;count&quot;</code> characters. For example, to <code>&quot;pack&quot;</code> or <code>&quot;unpack&quot;</code> a C structure like </p>
<pre><code>    struct {
        char c; /* one signed, 8-bit character */
        double d;
        char cc[2];
    }
</code></pre>
<p> one may need to use the template <code>&quot;c x![d] d c[2]&quot;</code>. This assumes that doubles must be aligned to the size of double. </p>
<p> For alignment commands, a <code>&quot;count&quot;</code> of 0 is equivalent to a <code>&quot;count&quot;</code> of 1; both are no-ops. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;n&quot;</code>, <code>&quot;N&quot;</code>, <code>&quot;v&quot;</code> and <code>&quot;V&quot;</code> accept the <code>&quot;!&quot;</code> modifier to represent signed 16-/32-bit integers in big-/little-endian order. This is portable only when all platforms sharing packed data use the same binary representation for signed integers; for example, when all platforms use two&#8217;s-complement representation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Comments can be embedded in a <font SIZE="-1">TEMPLATE</font> using <code>&quot;#&quot;</code> through the end of line. White space can separate pack codes from each other, but modifiers and repeat counts must follow immediately. Breaking complex templates into individual line-by-line components, suitably annotated, can do as much to improve legibility and maintainability of pack/unpack formats as <code>&quot;/x&quot;</code> can for complicated pattern matches. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If <font SIZE="-1">TEMPLATE</font> requires more arguments than <code>&quot;pack&quot;</code> is given, <code>&quot;pack&quot;</code> assumes additional <code>&quot;&quot;</code> arguments. If <font SIZE="-1">TEMPLATE</font> requires fewer arguments than given, extra arguments are ignored. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attempting to pack the special floating point values <code>&quot;Inf&quot;</code> and <code>&quot;NaN&quot;</code> (infinity, also in negative, and not-a-number) into packed integer values (like <code>&quot;L&quot;</code>) is a fatal error. The reason for this is that there simply isn&#8217;t any sensible mapping for these special values into integers. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Examples: </p>
<pre><code>    $foo = pack(&quot;WWWW&quot;,65,66,67,68);
    # foo eq &quot;ABCD&quot;
    $foo = pack(&quot;W4&quot;,65,66,67,68);
    # same thing
    $foo = pack(&quot;W4&quot;,0x24b6,0x24b7,0x24b8,0x24b9);
    # same thing with Unicode circled letters.
    $foo = pack(&quot;U4&quot;,0x24b6,0x24b7,0x24b8,0x24b9);
    # same thing with Unicode circled letters. You don't get the
    # UTF-8 bytes because the U at the start of the format caused
    # a switch to U0-mode, so the UTF-8 bytes get joined into
    # characters
    $foo = pack(&quot;C0U4&quot;,0x24b6,0x24b7,0x24b8,0x24b9);
    # foo eq &quot;\xe2\x92\xb6\xe2\x92\xb7\xe2\x92\xb8\xe2\x92\xb9&quot;
    # This is the UTF-8 encoding of the string in the
    # previous example
    $foo = pack(&quot;ccxxcc&quot;,65,66,67,68);
    # foo eq &quot;AB\0\0CD&quot;
    # NOTE: The examples above featuring &quot;W&quot; and &quot;c&quot; are true
    # only on ASCII and ASCII-derived systems such as ISO Latin 1
    # and UTF-8. On EBCDIC systems, the first example would be
    # $foo = pack(&quot;WWWW&quot;,193,194,195,196);
    $foo = pack(&quot;s2&quot;,1,2);
    # &quot;\001\000\002\000&quot; on little-endian
    # &quot;\000\001\000\002&quot; on big-endian
    $foo = pack(&quot;a4&quot;,&quot;abcd&quot;,&quot;x&quot;,&quot;y&quot;,&quot;z&quot;);
    # &quot;abcd&quot;
    $foo = pack(&quot;aaaa&quot;,&quot;abcd&quot;,&quot;x&quot;,&quot;y&quot;,&quot;z&quot;);
    # &quot;axyz&quot;
    $foo = pack(&quot;a14&quot;,&quot;abcdefg&quot;);
    # &quot;abcdefg\0\0\0\0\0\0\0&quot;
    $foo = pack(&quot;i9pl&quot;, gmtime);
    # a real struct tm (on my system anyway)
    $utmp_template = &quot;Z8 Z8 Z16 L&quot;;
    $utmp = pack($utmp_template, @utmp1);
    # a struct utmp (BSDish)
    @utmp2 = unpack($utmp_template, $utmp);
    # &quot;@utmp1&quot; eq &quot;@utmp2&quot;
    sub bintodec {
        unpack(&quot;N&quot;, pack(&quot;B32&quot;, substr(&quot;0&quot; x 32 . shift, -32)));
    }
    $foo = pack('sx2l', 12, 34);
    # short 12, two zero bytes padding, long 34
    $bar = pack('s@4l', 12, 34);
    # short 12, zero fill to position 4, long 34
    # $foo eq $bar
    $baz = pack('s.l', 12, 4, 34);
    # short 12, zero fill to position 4, long 34
    $foo = pack('nN', 42, 4711);
    # pack big-endian 16- and 32-bit unsigned integers
    $foo = pack('S&gt;L&gt;', 42, 4711);
    # exactly the same
    $foo = pack('s&lt;l&lt;', -42, 4711);
    # pack little-endian 16- and 32-bit signed integers
    $foo = pack('(sl)&lt;', -42, 4711);
    # exactly the same
</code></pre>
<p> The same template may generally also be used in <code>&quot;unpack&quot;</code>. </p>
 </dd></dl>
<dt>package <font SIZE="-1">NAMESPACE</font></dt>
<dd>  </dd>
<dt>package <font SIZE="-1">NAMESPACE VERSION</font></dt>
<dd>  </dd>
<dt>package <font SIZE="-1">NAMESPACE BLOCK</font></dt>
<dd>  </dd>
<dt>package <font SIZE="-1">NAMESPACE VERSION BLOCK</font></dt>
<dd> <p> Declares the <font SIZE="-1">BLOCK</font> or the rest of the compilation unit as being in the given namespace. The scope of the package declaration is either the supplied code <font SIZE="-1">BLOCK</font> or, in the absence of a <font SIZE="-1">BLOCK,</font> from the declaration itself through the end of current scope (the enclosing block, file, or <code>&quot;eval&quot;</code>). That is, the forms without a <font SIZE="-1">BLOCK</font> are operative through the end of the current scope, just like the <code>&quot;my&quot;</code>, <code>&quot;state&quot;</code>, and <code>&quot;our&quot;</code> operators. All unqualified dynamic identifiers in this scope will be in the given namespace, except where overridden by another <code>&quot;package&quot;</code> declaration or when they&#8217;re one of the special identifiers that qualify into <code>&quot;main::&quot;</code>, like <code>&quot;STDOUT&quot;</code>, <code>&quot;ARGV&quot;</code>, <code>&quot;ENV&quot;</code>, and the punctuation variables. </p>
<p> A package statement affects dynamic variables only, including those you&#8217;ve used <code>&quot;local&quot;</code> on, but <i>not</i> lexically-scoped variables, which are created with <code>&quot;my&quot;</code>, <code>&quot;state&quot;</code>, or <code>&quot;our&quot;</code>. Typically it would be the first declaration in a file included by <code>&quot;require&quot;</code> or <code>&quot;use&quot;</code>. You can switch into a package in more than one place, since this only determines which default symbol table the compiler uses for the rest of that block. You can refer to identifiers in other packages than the current one by prefixing the identifier with the package name and a double colon, as in <code>$SomePack::var</code> or <code>&quot;ThatPack::INPUT_HANDLE&quot;</code>. If package name is omitted, the <code>&quot;main&quot;</code> package as assumed. That is, <code>$::sail</code> is equivalent to <code>$main::sail</code> (as well as to <code>&quot;$main&#8217;sail&quot;</code>, still seen in ancient code, mostly from Perl 4). </p>
<p> If <font SIZE="-1">VERSION</font> is provided, <code>&quot;package&quot;</code> sets the <code>$VERSION</code> variable in the given namespace to a version object with the <font SIZE="-1">VERSION</font> provided. <font SIZE="-1">VERSION</font> must be a ``strict&#8217;&#8216; style version number as defined by the version module: a positive decimal number (integer or decimal-fraction) without exponentiation or else a dotted-decimal v-string with a leading &#8216;v&#8217; character and at least three components. You should set <code>$VERSION</code> only once per package. </p>
<p> See ``Packages&#8217;&#8216; in perlmod for more information about packages, modules, and classes. See perlsub for other scoping issues. </p>
 </dd>
<dt>__PACKAGE__</dt>
<dd> <p> A special token that returns the name of the package in which it occurs. </p>
 </dd>
<dt>pipe <font SIZE="-1">READHANDLE,WRITEHANDLE</font></dt>
<dd> <p> Opens a pair of connected pipes like the corresponding system call. Note that if you set up a loop of piped processes, deadlock can occur unless you are very careful. In addition, note that Perl&#8217;s pipes use <font SIZE="-1">IO</font> buffering, so you may need to set <code>$|</code> to flush your <font SIZE="-1">WRITEHANDLE</font> after each command, depending on the application. </p>
<p> Returns true on success. </p>
<p> See IPC::Open2, IPC::Open3, and ``Bidirectional Communication with Another Process&#8217;&#8216; in perlipc for examples of such things. </p>
<p> On systems that support a close-on-exec flag on files, that flag is set on all newly opened file descriptors whose <code>&quot;fileno&quot;</code>s are <i>higher</i> than the current value of <code>$^F</code> (by default 2 for <code>&quot;STDERR&quot;</code>). See ``$^F&#8217;&#8216; in perlvar. </p>
 </dd>
<dt>pop <font SIZE="-1">ARRAY</font></dt>
<dd>  </dd>
<dt>pop</dt>
<dd> <p> Pops and returns the last value of the array, shortening the array by one element. </p>
<p> Returns the undefined value if the array is empty, although this may also happen at other times. If <font SIZE="-1">ARRAY</font> is omitted, pops the <code>@ARGV</code> array in the main program, but the <code>@_</code> array in subroutines, just like <code>&quot;shift&quot;</code>. </p>
<p> Starting with Perl 5.14, an experimental feature allowed <code>&quot;pop&quot;</code> to take a scalar expression. This experiment has been deemed unsuccessful, and was removed as of Perl 5.24. </p>
 </dd>
<dt>pos <font SIZE="-1">SCALAR</font></dt>
<dd>  </dd>
<dt>pos</dt>
<dd> <p> Returns the offset of where the last <code>&quot;m//g&quot;</code> search left off for the variable in question (<code>$_</code> is used when the variable is not specified). This offset is in characters unless the (no-longer-recommended) <code>&quot;use bytes&quot;</code> pragma is in effect, in which case the offset is in bytes. Note that 0 is a valid match offset. <code>&quot;undef&quot;</code> indicates that the search position is reset (usually due to match failure, but can also be because no match has yet been run on the scalar). </p>
<p> <code>&quot;pos&quot;</code> directly accesses the location used by the regexp engine to store the offset, so assigning to <code>&quot;pos&quot;</code> will change that offset, and so will also influence the <code>&quot;\G&quot;</code> zero-width assertion in regular expressions. Both of these effects take place for the next match, so you can&#8217;t affect the position with <code>&quot;pos&quot;</code> during the current match, such as in <code>&quot;(?{pos() = 5})&quot;</code> or <code>&quot;s//pos() = 5/e&quot;</code>. </p>
<p> Setting <code>&quot;pos&quot;</code> also resets the <i>matched with zero-length</i> flag, described under ``Repeated Patterns Matching a Zero-length Substring&#8217;&#8216; in perlre. </p>
<p> Because a failed <code>&quot;m//gc&quot;</code> match doesn&#8217;t reset the offset, the return from <code>&quot;pos&quot;</code> won&#8217;t change either in this case. See perlre and perlop. </p>
 </dd>
<dt>print <font SIZE="-1">FILEHANDLE LIST</font></dt>
<dd>  </dd>
<dt>print <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>print <font SIZE="-1">LIST</font></dt>
<dd>  </dd>
<dt>print</dt>
<dd> <p> Prints a string or a list of strings. Returns true if successful. <font SIZE="-1">FILEHANDLE</font> may be a scalar variable containing the name of or a reference to the filehandle, thus introducing one level of indirection. (<font SIZE="-1">NOTE:</font> If <font SIZE="-1">FILEHANDLE</font> is a variable and the next token is a term, it may be misinterpreted as an operator unless you interpose a <code>&quot;+&quot;</code> or put parentheses around the arguments.) If <font SIZE="-1">FILEHANDLE</font> is omitted, prints to the last selected (see <code>&quot;select&quot;</code>) output handle. If <font SIZE="-1">LIST</font> is omitted, prints <code>$_</code> to the currently selected output handle. To use <font SIZE="-1">FILEHANDLE</font> alone to print the content of <code>$_</code> to it, you must use a bareword filehandle like <code>&quot;FH&quot;</code>, not an indirect one like <code>$fh</code>. To set the default output handle to something other than <font SIZE="-1">STDOUT,</font> use the select operation. </p>
<p> The current value of <code>$,</code> (if any) is printed between each <font SIZE="-1">LIST</font> item. The current value of <code>&quot;$\&quot;</code> (if any) is printed after the entire <font SIZE="-1">LIST</font> has been printed. Because print takes a <font SIZE="-1">LIST,</font> anything in the <font SIZE="-1">LIST</font> is evaluated in list context, including any subroutines whose return lists you pass to <code>&quot;print&quot;</code>. Be careful not to follow the print keyword with a left parenthesis unless you want the corresponding right parenthesis to terminate the arguments to the print; put parentheses around all arguments (or interpose a <code>&quot;+&quot;</code>, but that doesn&#8217;t look as good). </p>
<p> If you&#8217;re storing handles in an array or hash, or in general whenever you&#8217;re using any expression more complex than a bareword handle or a plain, unsubscripted scalar variable to retrieve it, you will have to use a block returning the filehandle value instead, in which case the <font SIZE="-1">LIST</font> may not be omitted: </p>
<pre><code>    print { $files[$i] } &quot;stuff\n&quot;;
    print { $OK ? *STDOUT : *STDERR } &quot;stuff\n&quot;;
</code></pre>
<p> Printing to a closed pipe or socket will generate a <font SIZE="-1">SIGPIPE</font> signal. See perlipc for more on signal handling. </p>
 </dd>
<dt>printf <font SIZE="-1">FILEHANDLE FORMAT, LIST</font></dt>
<dd>  </dd>
<dt>printf <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>printf <font SIZE="-1">FORMAT, LIST</font></dt>
<dd>  </dd>
<dt>printf</dt>
<dd> <p> Equivalent to <code>&quot;print FILEHANDLE sprintf(FORMAT, LIST)&quot;</code>, except that <code>&quot;$\&quot;</code> (the output record separator) is not appended. The <font SIZE="-1">FORMAT</font> and the <font SIZE="-1">LIST</font> are actually parsed as a single list. The first argument of the list will be interpreted as the <code>&quot;printf&quot;</code> format. This means that <code>&quot;printf(@_)&quot;</code> will use <code>$_[0]</code> as the format. See sprintf for an explanation of the format argument. If <code>&quot;use locale&quot;</code> (including <code>&quot;use locale &#8216;:not_characters&#8217;&quot;</code>) is in effect and <code>&quot;POSIX::setlocale&quot;</code> has been called, the character used for the decimal separator in formatted floating-point numbers is affected by the <code>&quot;LC_NUMERIC&quot;</code> locale setting. See perllocale and <font SIZE="-1">POSIX</font>. </p>
<p> For historical reasons, if you omit the list, <code>$_</code> is used as the format; to use <font SIZE="-1">FILEHANDLE</font> without a list, you must use a bareword filehandle like <code>&quot;FH&quot;</code>, not an indirect one like <code>$fh</code>. However, this will rarely do what you want; if <code>$_</code> contains formatting codes, they will be replaced with the empty string and a warning will be emitted if warnings are enabled. Just use <code>&quot;print&quot;</code> if you want to print the contents of <code>$_</code>. </p>
<p> Don&#8217;t fall into the trap of using a <code>&quot;printf&quot;</code> when a simple <code>&quot;print&quot;</code> would do. The <code>&quot;print&quot;</code> is more efficient and less error prone. </p>
 </dd>
<dt>prototype <font SIZE="-1">FUNCTION</font></dt>
<dd>  </dd>
<dt>prototype</dt>
<dd> <p> Returns the prototype of a function as a string (or <code>&quot;undef&quot;</code> if the function has no prototype). <font SIZE="-1">FUNCTION</font> is a reference to, or the name of, the function whose prototype you want to retrieve. If <font SIZE="-1">FUNCTION</font> is omitted, <code>$_</code> is used. </p>
<p> If <font SIZE="-1">FUNCTION</font> is a string starting with <code>&quot;CORE::&quot;</code>, the rest is taken as a name for a Perl builtin. If the builtin&#8217;s arguments cannot be adequately expressed by a prototype (such as <code>&quot;system&quot;</code>), <code>&quot;prototype&quot;</code> returns <code>&quot;undef&quot;</code>, because the builtin does not really behave like a Perl function. Otherwise, the string describing the equivalent prototype is returned. </p>
 </dd>
<dt>push <font SIZE="-1">ARRAY,LIST</font></dt>
<dd> <p> Treats <font SIZE="-1">ARRAY</font> as a stack by appending the values of <font SIZE="-1">LIST</font> to the end of <font SIZE="-1">ARRAY.</font> The length of <font SIZE="-1">ARRAY</font> increases by the length of <font SIZE="-1">LIST.</font> Has the same effect as </p>
<pre><code>    for my $value (LIST) {
        $ARRAY[++$#ARRAY] = $value;
    }
</code></pre>
<p> but is more efficient. Returns the number of elements in the array following the completed <code>&quot;push&quot;</code>. </p>
<p> Starting with Perl 5.14, an experimental feature allowed <code>&quot;push&quot;</code> to take a scalar expression. This experiment has been deemed unsuccessful, and was removed as of Perl 5.24. </p>
 </dd>
<dt>q/STRING/</dt>
<dd>  </dd>
<dt>qq/STRING/</dt>
<dd>  </dd>
<dt>qw/STRING/</dt>
<dd>  </dd>
<dt>qx/STRING/</dt>
<dd> <p> Generalized quotes. See ``Quote-Like Operators&#8217;&#8216; in perlop. </p>
 </dd>
<dt>qr/STRING/</dt>
<dd> <p> Regexp-like quote. See ``Regexp Quote-Like Operators&#8217;&#8216; in perlop. </p>
 </dd>
<dt>quotemeta <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>quotemeta</dt>
<dd> <p> Returns the value of <font SIZE="-1">EXPR</font> with all the <font SIZE="-1">ASCII</font> non-``word&#8217;&#8216; characters backslashed. (That is, all <font SIZE="-1">ASCII</font> characters not matching <code>&quot;/[A-Za-z_0-9]/&quot;</code> will be preceded by a backslash in the returned string, regardless of any locale settings.) This is the internal function implementing the <code>&quot;\Q&quot;</code> escape in double-quoted strings. (See below for the behavior on non-ASCII code points.) </p>
<p> If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. </p>
<p> quotemeta (and <code>&quot;\Q&quot;</code> ... <code>&quot;\E&quot;</code>) are useful when interpolating strings into regular expressions, because by default an interpolated variable will be considered a mini-regular expression. For example: </p>
<pre><code>    my $sentence = 'The quick brown fox jumped over the lazy dog';
    my $substring = 'quick.*?fox';
    $sentence =~ s{$substring}{big bad wolf};
</code></pre>
<p> Will cause <code>$sentence</code> to become <code>&#8216;The big bad wolf jumped over...&#8216;</code>. </p>
<p> On the other hand: </p>
<pre><code>    my $sentence = 'The quick brown fox jumped over the lazy dog';
    my $substring = 'quick.*?fox';
    $sentence =~ s{\Q$substring\E}{big bad wolf};
</code></pre>
<p> Or: </p>
<pre><code>    my $sentence = 'The quick brown fox jumped over the lazy dog';
    my $substring = 'quick.*?fox';
    my $quoted_substring = quotemeta($substring);
    $sentence =~ s{$quoted_substring}{big bad wolf};
</code></pre>
<p> Will both leave the sentence as is. Normally, when accepting literal string input from the user, <code>&quot;quotemeta&quot;</code> or <code>&quot;\Q&quot;</code> must be used. </p>
<p> In Perl v5.14, all non-ASCII characters are quoted in non-UTF-8-encoded strings, but not quoted in <font SIZE="-1">UTF-8</font> strings. </p>
<p> Starting in Perl v5.16, Perl adopted a Unicode-defined strategy for quoting non-ASCII characters; the quoting of <font SIZE="-1">ASCII</font> characters is unchanged. </p>
<p> Also unchanged is the quoting of non-UTF-8 strings when outside the scope of a <code>&quot;use feature &#8216;unicode_strings&#8217;&quot;</code>, which is to quote all characters in the upper Latin1 range. This provides complete backwards compatibility for old programs which do not use Unicode. (Note that <code>&quot;unicode_strings&quot;</code> is automatically enabled within the scope of a <code>&quot;use v5.12&quot;</code> or greater.) </p>
<p> Within the scope of <code>&quot;use locale&quot;</code>, all non-ASCII Latin1 code points are quoted whether the string is encoded as <font SIZE="-1">UTF-8</font> or not. As mentioned above, locale does not affect the quoting of ASCII-range characters. This protects against those locales where characters such as <code>&quot;|&quot;</code> are considered to be word characters. </p>
<p> Otherwise, Perl quotes non-ASCII characters using an adaptation from Unicode (see &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr31/">http://www.unicode.org/reports/tr31/</a>&gt;). The only code points that are quoted are those that have any of the Unicode properties: Pattern_Syntax, Pattern_White_Space, White_Space, Default_Ignorable_Code_Point, or General_Category=Control. </p>
<p> Of these properties, the two important ones are Pattern_Syntax and Pattern_White_Space. They have been set up by Unicode for exactly this purpose of deciding which characters in a regular expression pattern should be quoted. No character that can be in an identifier has these properties. </p>
<p> Perl promises, that if we ever add regular expression pattern metacharacters to the dozen already defined (<code>&quot;\ | ( ) [ { ^ $ * + ? .&quot;</code>), that we will only use ones that have the Pattern_Syntax property. Perl also promises, that if we ever add characters that are considered to be white space in regular expressions (currently mostly affected by <code>&quot;/x&quot;</code>), they will all have the Pattern_White_Space property. </p>
<p> Unicode promises that the set of code points that have these two properties will never change, so something that is not quoted in v5.16 will never need to be quoted in any future Perl release. (Not all the code points that match Pattern_Syntax have actually had characters assigned to them; so there is room to grow, but they are quoted whether assigned or not. Perl, of course, would never use an unassigned code point as an actual metacharacter.) </p>
<p> Quoting characters that have the other 3 properties is done to enhance the readability of the regular expression and not because they actually need to be quoted for regular expression purposes (characters with the White_Space property are likely to be indistinguishable on the page or screen from those with the Pattern_White_Space property; and the other two properties contain non-printing characters). </p>
 </dd>
<dt>rand <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>rand</dt>
<dd> <p> Returns a random fractional number greater than or equal to <code>0</code> and less than the value of <font SIZE="-1">EXPR.</font> (<font SIZE="-1">EXPR</font> should be positive.) If <font SIZE="-1">EXPR</font> is omitted, the value <code>1</code> is used. Currently <font SIZE="-1">EXPR</font> with the value <code>0</code> is also special-cased as <code>1</code> (this was undocumented before Perl 5.8.0 and is subject to change in future versions of Perl). Automatically calls <code>&quot;srand&quot;</code> unless <code>&quot;srand&quot;</code> has already been called. See also <code>&quot;srand&quot;</code>. </p>
<p> Apply <code>&quot;int&quot;</code> to the value returned by <code>&quot;rand&quot;</code> if you want random integers instead of random fractional numbers. For example, </p>
<pre><code>    int(rand(10))
</code></pre>
<p> returns a random integer between <code>0</code> and <code>9</code>, inclusive. </p>
<p> (Note: If your rand function consistently returns numbers that are too large or too small, then your version of Perl was probably compiled with the wrong number of <font SIZE="-1">RANDBITS.</font>) </p>
<p> &quot;rand&quot;<code> is not cryptographically secure. You should not rely on it in security-sensitive situations.</code> As of this writing, a number of third-party <font SIZE="-1">CPAN</font> modules offer random number generators intended by their authors to be cryptographically secure, including: Data::Entropy, Crypt::Random, Math::Random::Secure, and Math::TrulyRandom. </p>
 </dd>
<dt>read <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH,OFFSET</font></dt>
<dd>  </dd>
<dt>read <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH</font></dt>
<dd> <p> Attempts to read <font SIZE="-1">LENGTH</font> <i>characters</i> of data into variable <font SIZE="-1">SCALAR</font> from the specified <font SIZE="-1">FILEHANDLE.</font> Returns the number of characters actually read, <code>0</code> at end of file, or undef if there was an error (in the latter case <code>$!</code> is also set). <font SIZE="-1">SCALAR</font> will be grown or shrunk so that the last character actually read is the last character of the scalar after the read. </p>
<p> An <font SIZE="-1">OFFSET</font> may be specified to place the read data at some place in the string other than the beginning. A negative <font SIZE="-1">OFFSET</font> specifies placement at that many characters counting backwards from the end of the string. A positive <font SIZE="-1">OFFSET</font> greater than the length of <font SIZE="-1">SCALAR</font> results in the string being padded to the required size with <code>&quot;\0&quot;</code> bytes before the result of the read is appended. </p>
<p> The call is implemented in terms of either Perl&#8217;s or your system&#8217;s native <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3) library function. To get a true <code><a href="/docs/linux/man/2-read/">read</a></code>(2) system call, see sysread. </p>
<p> Note the <i>characters</i>: depending on the status of the filehandle, either (8-bit) bytes or characters are read. By default, all filehandles operate on bytes, but for example if the filehandle has been opened with the <code>&quot;:utf8&quot;</code> I/O layer (see <code>&quot;open&quot;</code>, and the open pragma), the I/O will operate on UTF8-encoded Unicode characters, not bytes. Similarly for the <code>&quot;:encoding&quot;</code> layer: in that case pretty much any characters can be read. </p>
 </dd>
<dt>readdir <font SIZE="-1">DIRHANDLE</font></dt>
<dd> <p> Returns the next directory entry for a directory opened by <code>&quot;opendir&quot;</code>. If used in list context, returns all the rest of the entries in the directory. If there are no more entries, returns the undefined value in scalar context and the empty list in list context. </p>
<p> If you&#8217;re planning to filetest the return values out of a <code>&quot;readdir&quot;</code>, you&#8217;d better prepend the directory in question. Otherwise, because we didn&#8217;t <code>&quot;chdir&quot;</code> there, it would have been testing the wrong file. </p>
<pre><code>    opendir(my $dh, $some_dir) || die &quot;Can't opendir $some_dir: $!&quot;;
    my @dots = grep { /^\./ &amp;&amp; -f &quot;$some_dir/$_&quot; } readdir($dh);
    closedir $dh;
</code></pre>
<p> As of Perl 5.12 you can use a bare <code>&quot;readdir&quot;</code> in a <code>&quot;while&quot;</code> loop, which will set <code>$_</code> on every iteration. If either a <code>&quot;readdir&quot;</code> expression or an explicit assignment of a <code>&quot;readdir&quot;</code> expression to a scalar is used as a <code>&quot;while&quot;</code>/<code>&quot;for&quot;</code> condition, then the condition actually tests for definedness of the expression&#8217;s value, not for its regular truth value. </p>
<pre><code>    opendir(my $dh, $some_dir) || die &quot;Can't open $some_dir: $!&quot;;
    while (readdir $dh) {
        print &quot;$some_dir/$_\n&quot;;
    }
    closedir $dh;
</code></pre>
<p> To avoid confusing would-be users of your code who are running earlier versions of Perl with mysterious failures, put this sort of thing at the top of your file to signal that your code will work <i>only</i> on Perls of a recent vintage: </p>
<pre><code>    use 5.012; # so readdir assigns to $_ in a lone while test
</code></pre>
 </dd>
<dt>readline <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>readline</dt>
<dd> <p> Reads from the filehandle whose typeglob is contained in <font SIZE="-1">EXPR</font> (or from <code>*ARGV</code> if <font SIZE="-1">EXPR</font> is not provided). In scalar context, each call reads and returns the next line until end-of-file is reached, whereupon the subsequent call returns <code>&quot;undef&quot;</code>. In list context, reads until end-of-file is reached and returns a list of lines. Note that the notion of ``line&#8217;&#8216; used here is whatever you may have defined with <code>$/</code> (or <code>$INPUT_RECORD_SEPARATOR</code> in English). See ``$/&#8216;&#8216; in perlvar. </p>
<p> When <code>$/</code> is set to <code>&quot;undef&quot;</code>, when <code>&quot;readline&quot;</code> is in scalar context (i.e., file slurp mode), and when an empty file is read, it returns <code>&#8216;&#8216;</code> the first time, followed by <code>&quot;undef&quot;</code> subsequently. </p>
<p> This is the internal function implementing the <code>&quot;&lt;EXPR&gt;&quot;</code> operator, but you can use it directly. The <code>&quot;&lt;EXPR&gt;&quot;</code> operator is discussed in more detail in ``I/O Operators&#8217;&#8216; in perlop. </p>
<pre><code>    my $line = &lt;STDIN&gt;;
    my $line = readline(STDIN); # same thing
</code></pre>
<p> If <code>&quot;readline&quot;</code> encounters an operating system error, <code>$!</code> will be set with the corresponding error message. It can be helpful to check <code>$!</code> when you are reading from filehandles you don&#8217;t trust, such as a tty or a socket. The following example uses the operator form of <code>&quot;readline&quot;</code> and dies if the result is not defined. </p>
<pre><code>    while ( ! eof($fh) ) {
        defined( $_ = readline $fh ) or die &quot;readline failed: $!&quot;;
        ...
    }
</code></pre>
<p> Note that you have can&#8217;t handle <code>&quot;readline&quot;</code> errors that way with the <code>&quot;ARGV&quot;</code> filehandle. In that case, you have to open each element of <code>@ARGV</code> yourself since <code>&quot;eof&quot;</code> handles <code>&quot;ARGV&quot;</code> differently. </p>
<pre><code>    foreach my $arg (@ARGV) {
        open(my $fh, $arg) or warn &quot;Can't open $arg: $!&quot;;
        while ( ! eof($fh) ) {
            defined( $_ = readline $fh )
                or die &quot;readline failed for $arg: $!&quot;;
            ...
        }
    }
</code></pre>
<p> Like the <code>&quot;&lt;EXPR&gt;&quot;</code> operator, if a <code>&quot;readline&quot;</code> expression is used as the condition of a <code>&quot;while&quot;</code> or <code>&quot;for&quot;</code> loop, then it will be implicitly assigned to <code>$_</code>. If either a <code>&quot;readline&quot;</code> expression or an explicit assignment of a <code>&quot;readline&quot;</code> expression to a scalar is used as a <code>&quot;while&quot;</code>/<code>&quot;for&quot;</code> condition, then the condition actually tests for definedness of the expression&#8217;s value, not for its regular truth value. </p>
 </dd>
<dt>readlink <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>readlink</dt>
<dd> <p> Returns the value of a symbolic link, if symbolic links are implemented. If not, raises an exception. If there is a system error, returns the undefined value and sets <code>$!</code> (errno). If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. </p>
<p> Portability issues: ``readlink&#8217;&#8216; in perlport. </p>
 </dd>
<dt>readpipe <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>readpipe</dt>
<dd> <p> <font SIZE="-1">EXPR</font> is executed as a system command. The collected standard output of the command is returned. In scalar context, it comes back as a single (potentially multi-line) string. In list context, returns a list of lines (however you&#8217;ve defined lines with <code>$/</code> (or <code>$INPUT_RECORD_SEPARATOR</code> in English)). This is the internal function implementing the <code>&quot;qx/EXPR/&quot;</code> operator, but you can use it directly. The <code>&quot;qx/EXPR/&quot;</code> operator is discussed in more detail in ``I/O Operators&#8217;&#8216; in perlop. If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. </p>
 </dd>
<dt>recv <font SIZE="-1">SOCKET,SCALAR,LENGTH,FLAGS</font></dt>
<dd> <p> Receives a message on a socket. Attempts to receive <font SIZE="-1">LENGTH</font> characters of data into variable <font SIZE="-1">SCALAR</font> from the specified <font SIZE="-1">SOCKET</font> filehandle. <font SIZE="-1">SCALAR</font> will be grown or shrunk to the length actually read. Takes the same flags as the system call of the same name. Returns the address of the sender if <font SIZE="-1">SOCKET</font>&#8216;s protocol supports this; returns an empty string otherwise. If there&#8217;s an error, returns the undefined value. This call is actually implemented in terms of the <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2) system call. See ``<font SIZE="-1">UDP:</font> Message Passing&#8217;&#8216; in perlipc for examples. </p>
<p> Note that if the socket has been marked as <code>&quot;:utf8&quot;</code>, <code>&quot;recv&quot;</code> will throw an exception. The <code>&quot;:encoding(...)&quot;</code> layer implicitly introduces the <code>&quot;:utf8&quot;</code> layer. See <code>&quot;binmode&quot;</code>. </p>
 </dd>
<dt>redo <font SIZE="-1">LABEL</font></dt>
<dd>  </dd>
<dt>redo <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>redo</dt>
<dd> <p> The <code>&quot;redo&quot;</code> command restarts the loop block without evaluating the conditional again. The <code>&quot;continue&quot;</code> block, if any, is not executed. If the <font SIZE="-1">LABEL</font> is omitted, the command refers to the innermost enclosing loop. The <code>&quot;redo EXPR&quot;</code> form, available starting in Perl 5.18.0, allows a label name to be computed at run time, and is otherwise identical to <code>&quot;redo LABEL&quot;</code>. Programs that want to lie to themselves about what was just input normally use this command: </p>
<pre><code>    # a simpleminded Pascal comment stripper
    # (warning: assumes no { or } in strings)
    LINE: while (&lt;STDIN&gt;) {
        while (s|({.*}.*){.*}|$1 |) {}
        s|{.*}| |;
        if (s|{.*| |) {
            my $front = $_;
            while (&lt;STDIN&gt;) {
                if (/}/) { # end of comment?
                    s|^|$front\{|;
                    redo LINE;
                }
            }
        }
        print;
    }
</code></pre>
<p> <code>&quot;redo&quot;</code> cannot return a value from a block that typically returns a value, such as <code>&quot;eval {}&quot;</code>, <code>&quot;sub {}&quot;</code>, or <code>&quot;do {}&quot;</code>. It will perform its flow control behavior, which precludes any return value. It should not be used to exit a <code>&quot;grep&quot;</code> or <code>&quot;map&quot;</code> operation. </p>
<p> Note that a block by itself is semantically identical to a loop that executes once. Thus <code>&quot;redo&quot;</code> inside such a block will effectively turn it into a looping construct. </p>
<p> See also <code>&quot;continue&quot;</code> for an illustration of how <code>&quot;last&quot;</code>, <code>&quot;next&quot;</code>, and <code>&quot;redo&quot;</code> work. </p>
<p> Unlike most named operators, this has the same precedence as assignment. It is also exempt from the looks-like-a-function rule, so <code>&quot;redo (&quot;foo&quot;).&quot;bar&quot;&quot;</code> will cause ``bar&#8217;&#8216; to be part of the argument to <code>&quot;redo&quot;</code>. </p>
 </dd>
<dt>ref <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>ref</dt>
<dd> <p> Examines the value of <font SIZE="-1">EXPR,</font> expecting it to be a reference, and returns a string giving information about the reference and the type of referent. If <font SIZE="-1">EXPR</font> is not specified, <code>$_</code> will be used. </p>
<p> If the operand is not a reference, then the empty string will be returned. An empty string will only be returned in this situation. <code>&quot;ref&quot;</code> is often useful to just test whether a value is a reference, which can be done by comparing the result to the empty string. It is a common mistake to use the result of <code>&quot;ref&quot;</code> directly as a truth value: this goes wrong because <code>0</code> (which is false) can be returned for a reference. </p>
<p> If the operand is a reference to a blessed object, then the name of the class into which the referent is blessed will be returned. <code>&quot;ref&quot;</code> doesn&#8217;t care what the physical type of the referent is; blessing takes precedence over such concerns. Beware that exact comparison of <code>&quot;ref&quot;</code> results against a class name doesn&#8217;t perform a class membership test: a class&#8217;s members also include objects blessed into subclasses, for which <code>&quot;ref&quot;</code> will return the name of the subclass. Also beware that class names can clash with the built-in type names (described below). </p>
<p> If the operand is a reference to an unblessed object, then the return value indicates the type of object. If the unblessed referent is not a scalar, then the return value will be one of the strings <code>&quot;ARRAY&quot;</code>, <code>&quot;HASH&quot;</code>, <code>&quot;CODE&quot;</code>, <code>&quot;FORMAT&quot;</code>, or <code>&quot;IO&quot;</code>, indicating only which kind of object it is. If the unblessed referent is a scalar, then the return value will be one of the strings <code>&quot;SCALAR&quot;</code>, <code>&quot;VSTRING&quot;</code>, <code>&quot;REF&quot;</code>, <code>&quot;GLOB&quot;</code>, <code>&quot;LVALUE&quot;</code>, or <code>&quot;REGEXP&quot;</code>, depending on the kind of value the scalar currently has. But note that <code>&quot;qr//&quot;</code> scalars are created already blessed, so <code>&quot;ref qr/.../&quot;</code> will likely return <code>&quot;Regexp&quot;</code>. Beware that these built-in type names can also be used as class names, so <code>&quot;ref&quot;</code> returning one of these names doesn&#8217;t unambiguously indicate that the referent is of the kind to which the name refers. </p>
<p> The ambiguity between built-in type names and class names significantly limits the utility of <code>&quot;ref&quot;</code>. For unambiguous information, use <code>&quot;Scalar::Util::blessed()&quot;</code> for information about blessing, and <code>&quot;Scalar::Util::reftype()&quot;</code> for information about physical types. Use the <code>&quot;isa&quot;</code> method for class membership tests, though one must be sure of blessedness before attempting a method call. </p>
<p> See also perlref and perlobj. </p>
 </dd>
<dt>rename <font SIZE="-1">OLDNAME,NEWNAME</font></dt>
<dd> <p> Changes the name of a file; an existing file <font SIZE="-1">NEWNAME</font> will be clobbered. Returns true for success, false otherwise. </p>
<p> Behavior of this function varies wildly depending on your system implementation. For example, it will usually not work across file system boundaries, even though the system <i>mv</i> command sometimes compensates for this. Other restrictions include whether it works on directories, open files, or pre-existing files. Check perlport and either the <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2) manpage or equivalent system documentation for details. </p>
<p> For a platform independent <code>&quot;move&quot;</code> function look at the File::Copy module. </p>
<p> Portability issues: ``rename&#8217;&#8216; in perlport. </p>
 </dd>
<dt>require <font SIZE="-1">VERSION</font></dt>
<dd>  </dd>
<dt>require <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>require</dt>
<dd> <p> Demands a version of Perl specified by <font SIZE="-1">VERSION,</font> or demands some semantics specified by <font SIZE="-1">EXPR</font> or by <code>$_</code> if <font SIZE="-1">EXPR</font> is not supplied. </p>
<p> <font SIZE="-1">VERSION</font> may be either a literal such as v5.24.1, which will be compared to <code>$^V</code> (or <code>$PERL_VERSION</code> in English), or a numeric argument of the form 5.024001, which will be compared to <code>$]</code>. An exception is raised if <font SIZE="-1">VERSION</font> is greater than the version of the current Perl interpreter. Compare with <code>&quot;use&quot;</code>, which can do a similar check at compile time. </p>
<p> Specifying <font SIZE="-1">VERSION</font> as a numeric argument of the form 5.024001 should generally be avoided as older less readable syntax compared to v5.24.1. Before perl 5.8.0 (released in 2002), the more verbose numeric form was the only supported syntax, which is why you might see it in older code. </p>
<pre><code>    require v5.24.1; # run time version check
    require 5.24.1; # ditto
    require 5.024_001; # ditto; older syntax compatible
                          with perl 5.6
</code></pre>
<p> Otherwise, <code>&quot;require&quot;</code> demands that a library file be included if it hasn&#8217;t already been included. The file is included via the do-FILE mechanism, which is essentially just a variety of <code>&quot;eval&quot;</code> with the caveat that lexical variables in the invoking script will be invisible to the included code. If it were implemented in pure Perl, it would have semantics similar to the following: </p>
<pre><code>    use Carp 'croak';
    use version;
    sub require {
        my ($filename) = @_;
        if ( my $version = eval { version-&gt;parse($filename) } ) {
            if ( $version &gt; $^V ) {
               my $vn = $version-&gt;normal;
               croak &quot;Perl $vn required--this is only $^V, stopped&quot;;
            }
            return 1;
        }
        if (exists $INC{$filename}) {
            return 1 if $INC{$filename};
            croak &quot;Compilation failed in require&quot;;
        }
        foreach $prefix (@INC) {
            if (ref($prefix)) {
                #... do other stuff - see text below ....
            }
            # (see text below about possible appending of .pmc
            # suffix to $filename)
            my $realfilename = &quot;$prefix/$filename&quot;;
            next if ! -e $realfilename || -d _ || -b _;
            $INC{$filename} = $realfilename;
            my $result = do($realfilename);
                         # but run in caller's namespace
            if (!defined $result) {
                $INC{$filename} = undef;
                croak $@ ? &quot;$@Compilation failed in require&quot;
                         : &quot;Can't locate $filename: $!\n&quot;;
            }
            if (!$result) {
                delete $INC{$filename};
                croak &quot;$filename did not return true value&quot;;
            }
            $! = 0;
            return $result;
        }
        croak &quot;Can't locate $filename in \@INC ...&quot;;
    }
</code></pre>
<p> Note that the file will not be included twice under the same specified name. </p>
<p> The file must return true as the last statement to indicate successful execution of any initialization code, so it&#8217;s customary to end such a file with <code>&quot;1;&quot;</code> unless you&#8217;re sure it&#8217;ll return true otherwise. But it&#8217;s better just to put the <code>&quot;1;&quot;</code>, in case you add more statements. </p>
<p> If <font SIZE="-1">EXPR</font> is a bareword, <code>&quot;require&quot;</code> assumes a <i>.pm</i> extension and replaces <code>&quot;::&quot;</code> with <code>&quot;/&quot;</code> in the filename for you, to make it easy to load standard modules. This form of loading of modules does not risk altering your namespace, however it will autovivify the stash for the required module. </p>
<p> In other words, if you try this: </p>
<pre><code>        require Foo::Bar; # a splendid bareword
</code></pre>
<p> The require function will actually look for the <i>Foo/Bar.pm</i> file in the directories specified in the <code>@INC</code> array, and it will autovivify the <code>&quot;Foo::Bar::&quot;</code> stash at compile time. </p>
<p> But if you try this: </p>
<pre><code>        my $class = 'Foo::Bar';
        require $class; # $class is not a bareword
    #or
        require &quot;Foo::Bar&quot;; # not a bareword because of the &quot;&quot;
</code></pre>
<p> The require function will look for the <i>Foo::Bar</i> file in the <code>@INC</code> array and will complain about not finding <i>Foo::Bar</i> there. In this case you can do: </p>
<pre><code>        eval &quot;require $class&quot;;
</code></pre>
<p> or you could do </p>
<pre><code>        require &quot;Foo/Bar.pm&quot;;
</code></pre>
<p> Neither of these forms will autovivify any stashes at compile time and only have run time effects. </p>
<p> Now that you understand how <code>&quot;require&quot;</code> looks for files with a bareword argument, there is a little extra functionality going on behind the scenes. Before <code>&quot;require&quot;</code> looks for a <i>.pm</i> extension, it will first look for a similar filename with a <i>.pmc</i> extension. If this file is found, it will be loaded in place of any file ending in a <i>.pm</i> extension. This applies to both the explicit <code>&quot;require &quot;Foo/Bar.pm&quot;;&quot;</code> form and the <code>&quot;require Foo::Bar;&quot;</code> form. </p>
<p> You can also insert hooks into the import facility by putting Perl code directly into the <code>@INC</code> array. There are three forms of hooks: subroutine references, array references, and blessed objects. </p>
<p> Subroutine references are the simplest case. When the inclusion system walks through <code>@INC</code> and encounters a subroutine, this subroutine gets called with two parameters, the first a reference to itself, and the second the name of the file to be included (e.g., <i>Foo/Bar.pm</i>). The subroutine should return either nothing or else a list of up to four values in the following order: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>1.</dt>
<dd> <p> A reference to a scalar, containing any initial source code to prepend to the file or generator output. </p>
 </dd>
<dt>2.</dt>
<dd> <p> A filehandle, from which the file will be read. </p>
 </dd>
<dt>3.</dt>
<dd> <p> A reference to a subroutine. If there is no filehandle (previous item), then this subroutine is expected to generate one line of source code per call, writing the line into <code>$_</code> and returning 1, then finally at end of file returning 0. If there is a filehandle, then the subroutine will be called to act as a simple source filter, with the line as read in <code>$_</code>. Again, return 1 for each valid line, and 0 after all lines have been returned. For historical reasons the subroutine will receive a meaningless argument (in fact always the numeric value zero) as <code>$_[0]</code>. </p>
 </dd>
<dt>4.</dt>
<dd> <p> Optional state for the subroutine. The state is passed in as <code>$_[1]</code>. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> If an empty list, <code>&quot;undef&quot;</code>, or nothing that matches the first 3 values above is returned, then <code>&quot;require&quot;</code> looks at the remaining elements of <code>@INC</code>. Note that this filehandle must be a real filehandle (strictly a typeglob or reference to a typeglob, whether blessed or unblessed); tied filehandles will be ignored and processing will stop there. </p>
<p> If the hook is an array reference, its first element must be a subroutine reference. This subroutine is called as above, but the first parameter is the array reference. This lets you indirectly pass arguments to the subroutine. </p>
<p> In other words, you can write: </p>
<pre><code>    push @INC, \&amp;my_sub;
    sub my_sub {
        my ($coderef, $filename) = @_; # $coderef is \&amp;my_sub
        ...
    }
</code></pre>
<p> or: </p>
<pre><code>    push @INC, [ \&amp;my_sub, $x, $y, ... ];
    sub my_sub {
        my ($arrayref, $filename) = @_;
        # Retrieve $x, $y, ...
        my (undef, @parameters) = @$arrayref;
        ...
    }
</code></pre>
<p> If the hook is an object, it must provide an <code>&quot;INC&quot;</code> method that will be called as above, the first parameter being the object itself. (Note that you must fully qualify the sub&#8217;s name, as unqualified <code>&quot;INC&quot;</code> is always forced into package <code>&quot;main&quot;</code>.) Here is a typical code layout: </p>
<pre><code>    # In Foo.pm
    package Foo;
    sub new { ... }
    sub Foo::INC {
        my ($self, $filename) = @_;
        ...
    }
    # In the main program
    push @INC, Foo-&gt;new(...);
</code></pre>
<p> These hooks are also permitted to set the <code>%INC</code> entry corresponding to the files they have loaded. See ``%INC&#8217;&#8216; in perlvar. </p>
<p> For a yet-more-powerful import facility, see <code>&quot;use&quot;</code> and perlmod. </p>
 </dd></dl>
<dt>reset <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>reset</dt>
<dd> <p> Generally used in a <code>&quot;continue&quot;</code> block at the end of a loop to clear variables and reset <code>&quot;m?pattern?&quot;</code> searches so that they work again. The expression is interpreted as a list of single characters (hyphens allowed for ranges). All variables (scalars, arrays, and hashes) in the current package beginning with one of those letters are reset to their pristine state. If the expression is omitted, one-match searches (<code>&quot;m?pattern?&quot;</code>) are reset to match again. Only resets variables or searches in the current package. Always returns 1. Examples: </p>
<pre><code>    reset 'X'; # reset all X variables
    reset 'a-z'; # reset lower case variables
    reset; # just reset m?one-time? searches
</code></pre>
<p> Resetting <code>&quot;A-Z&quot;</code> is not recommended because you&#8217;ll wipe out your <code>@ARGV</code> and <code>@INC</code> arrays and your <code>%ENV</code> hash. </p>
<p> Resets only package variables; lexical variables are unaffected, but they clean themselves up on scope exit anyway, so you&#8217;ll probably want to use them instead. See <code>&quot;my&quot;</code>. </p>
 </dd>
<dt>return <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>return</dt>
<dd> <p> Returns from a subroutine, <code>&quot;eval&quot;</code>, <code>&quot;do FILE&quot;</code>, <code>&quot;sort&quot;</code> block or regex eval block (but not a <code>&quot;grep&quot;</code> or <code>&quot;map&quot;</code> block) with the value given in <font SIZE="-1">EXPR.</font> Evaluation of <font SIZE="-1">EXPR</font> may be in list, scalar, or void context, depending on how the return value will be used, and the context may vary from one execution to the next (see <code>&quot;wantarray&quot;</code>). If no <font SIZE="-1">EXPR</font> is given, returns an empty list in list context, the undefined value in scalar context, and (of course) nothing at all in void context. </p>
<p> (In the absence of an explicit <code>&quot;return&quot;</code>, a subroutine, <code>&quot;eval&quot;</code>, or <code>&quot;do FILE&quot;</code> automatically returns the value of the last expression evaluated.) </p>
<p> Unlike most named operators, this is also exempt from the looks-like-a-function rule, so <code>&quot;return (&quot;foo&quot;).&quot;bar&quot;&quot;</code> will cause <code>&quot;bar&quot;</code> to be part of the argument to <code>&quot;return&quot;</code>. </p>
 </dd>
<dt>reverse <font SIZE="-1">LIST</font></dt>
<dd> <p> In list context, returns a list value consisting of the elements of <font SIZE="-1">LIST</font> in the opposite order. In scalar context, concatenates the elements of <font SIZE="-1">LIST</font> and returns a string value with all characters in the opposite order. </p>
<pre><code>    print join(&quot;, &quot;, reverse &quot;world&quot;, &quot;Hello&quot;); # Hello, world
    print scalar reverse &quot;dlrow ,&quot;, &quot;olleH&quot;; # Hello, world
</code></pre>
<p> Used without arguments in scalar context, <code>&quot;reverse&quot;</code> reverses <code>$_</code>. </p>
<pre><code>    $_ = &quot;dlrow ,olleH&quot;;
    print reverse; # No output, list context
    print scalar reverse; # Hello, world
</code></pre>
<p> Note that reversing an array to itself (as in <code>&quot;@a = reverse @a&quot;</code>) will preserve non-existent elements whenever possible; i.e., for non-magical arrays or for tied arrays with <code>&quot;EXISTS&quot;</code> and <code>&quot;DELETE&quot;</code> methods. </p>
<p> This operator is also handy for inverting a hash, although there are some caveats. If a value is duplicated in the original hash, only one of those can be represented as a key in the inverted hash. Also, this has to unwind one hash and build a whole new one, which may take some time on a large hash, such as from a <font SIZE="-1">DBM</font> file. </p>
<pre><code>    my %by_name = reverse %by_address; # Invert the hash
</code></pre>
 </dd>
<dt>rewinddir <font SIZE="-1">DIRHANDLE</font></dt>
<dd> <p> Sets the current position to the beginning of the directory for the <code>&quot;readdir&quot;</code> routine on <font SIZE="-1">DIRHANDLE.</font> </p>
<p> Portability issues: ``rewinddir&#8217;&#8216; in perlport. </p>
 </dd>
<dt>rindex <font SIZE="-1">STR,SUBSTR,POSITION</font></dt>
<dd>  </dd>
<dt>rindex <font SIZE="-1">STR,SUBSTR</font></dt>
<dd> <p> Works just like <code>&quot;index&quot;</code> except that it returns the position of the <i>last</i> occurrence of <font SIZE="-1">SUBSTR</font> in <font SIZE="-1">STR.</font> If <font SIZE="-1">POSITION</font> is specified, returns the last occurrence beginning at or before that position. </p>
 </dd>
<dt>rmdir <font SIZE="-1">FILENAME</font></dt>
<dd>  </dd>
<dt>rmdir</dt>
<dd> <p> Deletes the directory specified by <font SIZE="-1">FILENAME</font> if that directory is empty. If it succeeds it returns true; otherwise it returns false and sets <code>$!</code> (errno). If <font SIZE="-1">FILENAME</font> is omitted, uses <code>$_</code>. </p>
<p> To remove a directory tree recursively (<code>&quot;rm -rf&quot;</code> on Unix) look at the <code>&quot;rmtree&quot;</code> function of the File::Path module. </p>
 </dd>
<dt>s///</dt>
<dd> <p> The substitution operator. See ``Regexp Quote-Like Operators&#8217;&#8216; in perlop. </p>
 </dd>
<dt>say <font SIZE="-1">FILEHANDLE LIST</font></dt>
<dd>  </dd>
<dt>say <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>say <font SIZE="-1">LIST</font></dt>
<dd>  </dd>
<dt>say</dt>
<dd> <p> Just like <code>&quot;print&quot;</code>, but implicitly appends a newline. <code>&quot;say LIST&quot;</code> is simply an abbreviation for <code>&quot;{ local $\ = &quot;\n&quot;; print LIST }&quot;</code>. To use <font SIZE="-1">FILEHANDLE</font> without a <font SIZE="-1">LIST</font> to print the contents of <code>$_</code> to it, you must use a bareword filehandle like <code>&quot;FH&quot;</code>, not an indirect one like <code>$fh</code>. </p>
<p> <code>&quot;say&quot;</code> is available only if the <code>&quot;say&quot;</code> feature is enabled or if it is prefixed with <code>&quot;CORE::&quot;</code>. The <code>&quot;say&quot;</code> feature is enabled automatically with a <code>&quot;use v5.10&quot;</code> (or higher) declaration in the current scope. </p>
 </dd>
<dt>scalar <font SIZE="-1">EXPR</font></dt>
<dd> <p> Forces <font SIZE="-1">EXPR</font> to be interpreted in scalar context and returns the value of <font SIZE="-1">EXPR.</font> </p>
<pre><code>    my @counts = ( scalar @a, scalar @b, scalar @c );
</code></pre>
<p> There is no equivalent operator to force an expression to be interpolated in list context because in practice, this is never needed. If you really wanted to do so, however, you could use the construction <code>&quot;@{[ (some expression) ]}&quot;</code>, but usually a simple <code>&quot;(some expression)&quot;</code> suffices. </p>
<p> Because <code>&quot;scalar&quot;</code> is a unary operator, if you accidentally use a parenthesized list for the <font SIZE="-1">EXPR,</font> this behaves as a scalar comma expression, evaluating all but the last element in void context and returning the final element evaluated in scalar context. This is seldom what you want. </p>
<p> The following single statement: </p>
<pre><code>    print uc(scalar(foo(), $bar)), $baz;
</code></pre>
<p> is the moral equivalent of these two: </p>
<pre><code>    foo();
    print(uc($bar), $baz);
</code></pre>
<p> See perlop for more details on unary operators and the comma operator, and perldata for details on evaluating a hash in scalar contex. </p>
 </dd>
<dt>seek <font SIZE="-1">FILEHANDLE,POSITION,WHENCE</font></dt>
<dd> <p> Sets <font SIZE="-1">FILEHANDLE</font>&#8216;s position, just like the <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3) call of C <code>&quot;stdio&quot;</code>. <font SIZE="-1">FILEHANDLE</font> may be an expression whose value gives the name of the filehandle. The values for <font SIZE="-1">WHENCE</font> are <code>0</code> to set the new position <i>in bytes</i> to <font SIZE="-1">POSITION</font>; <code>1</code> to set it to the current position plus <font SIZE="-1">POSITION</font>; and <code>2</code> to set it to <font SIZE="-1">EOF</font> plus <font SIZE="-1">POSITION,</font> typically negative. For <font SIZE="-1">WHENCE</font> you may use the constants <code>&quot;SEEK_SET&quot;</code>, <code>&quot;SEEK_CUR&quot;</code>, and <code>&quot;SEEK_END&quot;</code> (start of the file, current position, end of the file) from the Fcntl module. Returns <code>1</code> on success, false otherwise. </p>
<p> Note the emphasis on bytes: even if the filehandle has been set to operate on characters (for example using the <code>&quot;:encoding(UTF-8)&quot;</code> I/O layer), the <code>&quot;seek&quot;</code>, <code>&quot;tell&quot;</code>, and <code>&quot;sysseek&quot;</code> family of functions use byte offsets, not character offsets, because seeking to a character offset would be very slow in a <font SIZE="-1">UTF-8</font> file. </p>
<p> If you want to position the file for <code>&quot;sysread&quot;</code> or <code>&quot;syswrite&quot;</code>, don&#8217;t use <code>&quot;seek&quot;</code>, because buffering makes its effect on the file&#8217;s read-write position unpredictable and non-portable. Use <code>&quot;sysseek&quot;</code> instead. </p>
<p> Due to the rules and rigors of <font SIZE="-1">ANSI C,</font> on some systems you have to do a seek whenever you switch between reading and writing. Amongst other things, this may have the effect of calling stdio&#8217;s <code><a href="/docs/linux/man/3-clearerr/">clearerr</a></code>(3). A <font SIZE="-1">WHENCE</font> of <code>1</code> (<code>&quot;SEEK_CUR&quot;</code>) is useful for not moving the file position: </p>
<pre><code>    seek($fh, 0, 1);
</code></pre>
<p> This is also useful for applications emulating <code>&quot;tail -f&quot;</code>. Once you hit <font SIZE="-1">EOF</font> on your read and then sleep for a while, you (probably) have to stick in a dummy <code>&quot;seek&quot;</code> to reset things. The <code>&quot;seek&quot;</code> doesn&#8217;t change the position, but it <i>does</i> clear the end-of-file condition on the handle, so that the next <code>&quot;readline FILE&quot;</code> makes Perl try again to read something. (We hope.) </p>
<p> If that doesn&#8217;t work (some I/O implementations are particularly cantankerous), you might need something like this: </p>
<pre><code>    for (;;) {
        for ($curpos = tell($fh); $_ = readline($fh);
             $curpos = tell($fh)) {
            # search for some stuff and put it into files
        }
        sleep($for_a_while);
        seek($fh, $curpos, 0);
    }
</code></pre>
 </dd>
<dt>seekdir <font SIZE="-1">DIRHANDLE,POS</font></dt>
<dd> <p> Sets the current position for the <code>&quot;readdir&quot;</code> routine on <font SIZE="-1">DIRHANDLE.</font> <font SIZE="-1">POS</font> must be a value returned by <code>&quot;telldir&quot;</code>. <code>&quot;seekdir&quot;</code> also has the same caveats about possible directory compaction as the corresponding system library routine. </p>
 </dd>
<dt>select <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>select</dt>
<dd> <p> Returns the currently selected filehandle. If <font SIZE="-1">FILEHANDLE</font> is supplied, sets the new current default filehandle for output. This has two effects: first, a <code>&quot;write&quot;</code> or a <code>&quot;print&quot;</code> without a filehandle default to this <font SIZE="-1">FILEHANDLE.</font> Second, references to variables related to output will refer to this output channel. </p>
<p> For example, to set the top-of-form format for more than one output channel, you might do the following: </p>
<pre><code>    select(REPORT1);
    $^ = 'report1_top';
    select(REPORT2);
    $^ = 'report2_top';
</code></pre>
<p> <font SIZE="-1">FILEHANDLE</font> may be an expression whose value gives the name of the actual filehandle. Thus: </p>
<pre><code>    my $oldfh = select(STDERR); $| = 1; select($oldfh);
</code></pre>
<p> Some programmers may prefer to think of filehandles as objects with methods, preferring to write the last example as: </p>
<pre><code>    STDERR-&gt;autoflush(1);
</code></pre>
<p> (Prior to Perl version 5.14, you have to <code>&quot;use IO::Handle;&quot;</code> explicitly first.) </p>
<p> Portability issues: ``select&#8217;&#8216; in perlport. </p>
 </dd>
<dt>select <font SIZE="-1">RBITS,WBITS,EBITS,TIMEOUT</font></dt>
<dd> <p> This calls the <code><a href="/docs/linux/man/2-select/">select</a></code>(2) syscall with the bit masks specified, which can be constructed using <code>&quot;fileno&quot;</code> and <code>&quot;vec&quot;</code>, along these lines: </p>
<pre><code>    my $rin = my $win = my $ein = '';
    vec($rin, fileno(STDIN), 1) = 1;
    vec($win, fileno(STDOUT), 1) = 1;
    $ein = $rin | $win;
</code></pre>
<p> If you want to select on many filehandles, you may wish to write a subroutine like this: </p>
<pre><code>    sub fhbits {
        my @fhlist = @_;
        my $bits = &quot;&quot;;
        for my $fh (@fhlist) {
            vec($bits, fileno($fh), 1) = 1;
        }
        return $bits;
    }
    my $rin = fhbits(\*STDIN, $tty, $mysock);
</code></pre>
<p> The usual idiom is: </p>
<pre><code> my ($nfound, $timeleft) =
   select(my $rout = $rin, my $wout = $win, my $eout = $ein,
                                                          $timeout);
</code></pre>
<p> or to block until something becomes ready just do this </p>
<pre><code> my $nfound =
   select(my $rout = $rin, my $wout = $win, my $eout = $ein, undef);
</code></pre>
<p> Most systems do not bother to return anything useful in <code>$timeleft</code>, so calling <code>&quot;select&quot;</code> in scalar context just returns <code>$nfound</code>. </p>
<p> Any of the bit masks can also be <code>&quot;undef&quot;</code>. The timeout, if specified, is in seconds, which may be fractional. Note: not all implementations are capable of returning the <code>$timeleft</code>. If not, they always return <code>$timeleft</code> equal to the supplied <code>$timeout</code>. </p>
<p> You can effect a sleep of 250 milliseconds this way: </p>
<pre><code>    select(undef, undef, undef, 0.25);
</code></pre>
<p> Note that whether <code>&quot;select&quot;</code> gets restarted after signals (say, <font SIZE="-1">SIGALRM</font>) is implementation-dependent. See also perlport for notes on the portability of <code>&quot;select&quot;</code>. </p>
<p> On error, <code>&quot;select&quot;</code> behaves just like <code><a href="/docs/linux/man/2-select/">select</a></code>(2): it returns <code>&quot;-1&quot;</code> and sets <code>$!</code>. </p>
<p> On some Unixes, <code><a href="/docs/linux/man/2-select/">select</a></code>(2) may report a socket file descriptor as ``ready for reading&#8217;&#8216; even when no data is available, and thus any subsequent <code>&quot;read&quot;</code> would block. This can be avoided if you always use <code>&quot;O_NONBLOCK&quot;</code> on the socket. See <code><a href="/docs/linux/man/2-select/">select</a></code>(2) and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for further details. </p>
<p> The standard <code>&quot;IO::Select&quot;</code> module provides a user-friendlier interface to <code>&quot;select&quot;</code>, mostly because it does all the bit-mask work for you. </p>
<p> <font SIZE="-1"><code>WARNING</code></font>: One should not attempt to mix buffered I/O (like <code>&quot;read&quot;</code> or <code>&quot;readline&quot;</code>) with <code>&quot;select&quot;</code>, except as permitted by <font SIZE="-1">POSIX,</font> and even then only on <font SIZE="-1">POSIX</font> systems. You have to use <code>&quot;sysread&quot;</code> instead. </p>
<p> Portability issues: ``select&#8217;&#8216; in perlport. </p>
 </dd>
<dt>semctl <font SIZE="-1">ID,SEMNUM,CMD,ARG</font></dt>
<dd> <p> Calls the System V <font SIZE="-1">IPC</font> function <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2). You&#8217;ll probably have to say </p>
<pre><code>    use IPC::SysV;
</code></pre>
<p> first to get the correct constant definitions. If <font SIZE="-1">CMD</font> is <font SIZE="-1">IPC_STAT</font> or <font SIZE="-1">GETALL,</font> then <font SIZE="-1">ARG</font> must be a variable that will hold the returned semid_ds structure or semaphore value array. Returns like <code>&quot;ioctl&quot;</code>: the undefined value for error, &quot;<code>&quot;0 but true&quot;</code>&quot; for zero, or the actual return value otherwise. The <font SIZE="-1">ARG</font> must consist of a vector of native short integers, which may be created with <code>&quot;pack(&quot;s!&quot;,(0)x$nsem)&quot;</code>. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code> and <code>&quot;IPC::Semaphore&quot;</code>. </p>
<p> Portability issues: ``semctl&#8217;&#8216; in perlport. </p>
 </dd>
<dt>semget <font SIZE="-1">KEY,NSEMS,FLAGS</font></dt>
<dd> <p> Calls the System V <font SIZE="-1">IPC</font> function <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2). Returns the semaphore id, or the undefined value on error. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code> and <code>&quot;IPC::Semaphore&quot;</code>. </p>
<p> Portability issues: ``semget&#8217;&#8216; in perlport. </p>
 </dd>
<dt>semop <font SIZE="-1">KEY,OPSTRING</font></dt>
<dd> <p> Calls the System V <font SIZE="-1">IPC</font> function <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) for semaphore operations such as signalling and waiting. <font SIZE="-1">OPSTRING</font> must be a packed array of semop structures. Each semop structure can be generated with <code>&quot;pack(&quot;s!3&quot;, $semnum, $semop, $semflag)&quot;</code>. The length of <font SIZE="-1">OPSTRING</font> implies the number of semaphore operations. Returns true if successful, false on error. As an example, the following code waits on semaphore <code>$semnum</code> of semaphore id <code>$semid:</code> </p>
<pre><code>    my $semop = pack(&quot;s!3&quot;, $semnum, -1, 0);
    die &quot;Semaphore trouble: $!\n&quot; unless semop($semid, $semop);
</code></pre>
<p> To signal the semaphore, replace <code>&quot;-1&quot;</code> with <code>1</code>. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code> and <code>&quot;IPC::Semaphore&quot;</code>. </p>
<p> Portability issues: ``semop&#8217;&#8216; in perlport. </p>
 </dd>
<dt>send <font SIZE="-1">SOCKET,MSG,FLAGS,TO</font></dt>
<dd>  </dd>
<dt>send <font SIZE="-1">SOCKET,MSG,FLAGS</font></dt>
<dd> <p> Sends a message on a socket. Attempts to send the scalar <font SIZE="-1">MSG</font> to the <font SIZE="-1">SOCKET</font> filehandle. Takes the same flags as the system call of the same name. On unconnected sockets, you must specify a destination to <i>send to</i>, in which case it does a <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2) syscall. Returns the number of characters sent, or the undefined value on error. The <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) syscall is currently unimplemented. See ``<font SIZE="-1">UDP:</font> Message Passing&#8217;&#8216; in perlipc for examples. </p>
<p> Note that if the socket has been marked as <code>&quot;:utf8&quot;</code>, <code>&quot;send&quot;</code> will throw an exception. The <code>&quot;:encoding(...)&quot;</code> layer implicitly introduces the <code>&quot;:utf8&quot;</code> layer. See <code>&quot;binmode&quot;</code>. </p>
 </dd>
<dt>setpgrp <font SIZE="-1">PID,PGRP</font></dt>
<dd> <p> Sets the current process group for the specified <font SIZE="-1">PID,</font> <code>0</code> for the current process. Raises an exception when used on a machine that doesn&#8217;t implement <font SIZE="-1">POSIX</font> <code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2) or <font SIZE="-1">BSD</font> <code><a href="/docs/linux/man/2-setpgrp/">setpgrp</a></code>(2). If the arguments are omitted, it defaults to <code>&quot;0,0&quot;</code>. Note that the <font SIZE="-1">BSD 4.2</font> version of <code>&quot;setpgrp&quot;</code> does not accept any arguments, so only <code>&quot;setpgrp(0,0)&quot;</code> is portable. See also <code>&quot;POSIX::setsid()&quot;</code>. </p>
<p> Portability issues: ``setpgrp&#8217;&#8216; in perlport. </p>
 </dd>
<dt>setpriority <font SIZE="-1">WHICH,WHO,PRIORITY</font></dt>
<dd> <p> Sets the current priority for a process, a process group, or a user. (See <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2).) Raises an exception when used on a machine that doesn&#8217;t implement <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2). </p>
<p> <code>&quot;WHICH&quot;</code> can be any of <code>&quot;PRIO_PROCESS&quot;</code>, <code>&quot;PRIO_PGRP&quot;</code> or <code>&quot;PRIO_USER&quot;</code> imported from ``<font SIZE="-1">RESOURCE CONSTANTS&#8217;&#8216;</font> in <font SIZE="-1">POSIX</font>. </p>
<p> Portability issues: ``setpriority&#8217;&#8216; in perlport. </p>
 </dd>
<dt>setsockopt <font SIZE="-1">SOCKET,LEVEL,OPTNAME,OPTVAL</font></dt>
<dd> <p> Sets the socket option requested. Returns <code>&quot;undef&quot;</code> on error. Use integer constants provided by the <code>&quot;Socket&quot;</code> module for <font SIZE="-1">LEVEL</font> and <font SIZE="-1">OPNAME.</font> Values for <font SIZE="-1">LEVEL</font> can also be obtained from getprotobyname. <font SIZE="-1">OPTVAL</font> might either be a packed string or an integer. An integer <font SIZE="-1">OPTVAL</font> is shorthand for pack(``i&#8217;&#8216;, <font SIZE="-1">OPTVAL</font>). </p>
<p> An example disabling Nagle&#8217;s algorithm on a socket: </p>
<pre><code>    use Socket qw(IPPROTO_TCP TCP_NODELAY);
    setsockopt($socket, IPPROTO_TCP, TCP_NODELAY, 1);
</code></pre>
<p> Portability issues: ``setsockopt&#8217;&#8216; in perlport. </p>
 </dd>
<dt>shift <font SIZE="-1">ARRAY</font></dt>
<dd>  </dd>
<dt>shift</dt>
<dd> <p> Shifts the first value of the array off and returns it, shortening the array by 1 and moving everything down. If there are no elements in the array, returns the undefined value. If <font SIZE="-1">ARRAY</font> is omitted, shifts the <code>@_</code> array within the lexical scope of subroutines and formats, and the <code>@ARGV</code> array outside a subroutine and also within the lexical scopes established by the <code>&quot;eval STRING&quot;</code>, <code>&quot;BEGIN {}&quot;</code>, <code>&quot;INIT {}&quot;</code>, <code>&quot;CHECK {}&quot;</code>, <code>&quot;UNITCHECK {}&quot;</code>, and <code>&quot;END {}&quot;</code> constructs. </p>
<p> Starting with Perl 5.14, an experimental feature allowed <code>&quot;shift&quot;</code> to take a scalar expression. This experiment has been deemed unsuccessful, and was removed as of Perl 5.24. </p>
<p> See also <code>&quot;unshift&quot;</code>, <code>&quot;push&quot;</code>, and <code>&quot;pop&quot;</code>. <code>&quot;shift&quot;</code> and <code>&quot;unshift&quot;</code> do the same thing to the left end of an array that <code>&quot;pop&quot;</code> and <code>&quot;push&quot;</code> do to the right end. </p>
 </dd>
<dt>shmctl <font SIZE="-1">ID,CMD,ARG</font></dt>
<dd> <p> Calls the System V <font SIZE="-1">IPC</font> function shmctl. You&#8217;ll probably have to say </p>
<pre><code>    use IPC::SysV;
</code></pre>
<p> first to get the correct constant definitions. If <font SIZE="-1">CMD</font> is <code>&quot;IPC_STAT&quot;</code>, then <font SIZE="-1">ARG</font> must be a variable that will hold the returned <code>&quot;shmid_ds&quot;</code> structure. Returns like ioctl: <code>&quot;undef&quot;</code> for error; &quot;<code>0</code> but true&quot; for zero; and the actual return value otherwise. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code>. </p>
<p> Portability issues: ``shmctl&#8217;&#8216; in perlport. </p>
 </dd>
<dt>shmget <font SIZE="-1">KEY,SIZE,FLAGS</font></dt>
<dd> <p> Calls the System V <font SIZE="-1">IPC</font> function shmget. Returns the shared memory segment id, or <code>&quot;undef&quot;</code> on error. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code>. </p>
<p> Portability issues: ``shmget&#8217;&#8216; in perlport. </p>
 </dd>
<dt>shmread <font SIZE="-1">ID,VAR,POS,SIZE</font></dt>
<dd>  </dd>
<dt>shmwrite <font SIZE="-1">ID,STRING,POS,SIZE</font></dt>
<dd> <p> Reads or writes the System V shared memory segment <font SIZE="-1">ID</font> starting at position <font SIZE="-1">POS</font> for size <font SIZE="-1">SIZE</font> by attaching to it, copying in/out, and detaching from it. When reading, <font SIZE="-1">VAR</font> must be a variable that will hold the data read. When writing, if <font SIZE="-1">STRING</font> is too long, only <font SIZE="-1">SIZE</font> bytes are used; if <font SIZE="-1">STRING</font> is too short, nulls are written to fill out <font SIZE="-1">SIZE</font> bytes. Return true if successful, false on error. <code>&quot;shmread&quot;</code> taints the variable. See also ``SysV <font SIZE="-1">IPC&#8217;&#8216;</font> in perlipc and the documentation for <code>&quot;IPC::SysV&quot;</code> and the <code>&quot;IPC::Shareable&quot;</code> module from <font SIZE="-1">CPAN.</font> </p>
<p> Portability issues: ``shmread&#8217;&#8216; in perlport and ``shmwrite&#8217;&#8216; in perlport. </p>
 </dd>
<dt>shutdown <font SIZE="-1">SOCKET,HOW</font></dt>
<dd> <p> Shuts down a socket connection in the manner indicated by <font SIZE="-1">HOW,</font> which has the same interpretation as in the syscall of the same name. </p>
<pre><code>    shutdown($socket, 0); # I/we have stopped reading data
    shutdown($socket, 1); # I/we have stopped writing data
    shutdown($socket, 2); # I/we have stopped using this socket
</code></pre>
<p> This is useful with sockets when you want to tell the other side you&#8217;re done writing but not done reading, or vice versa. It&#8217;s also a more insistent form of close because it also disables the file descriptor in any forked copies in other processes. </p>
<p> Returns <code>1</code> for success; on error, returns <code>&quot;undef&quot;</code> if the first argument is not a valid filehandle, or returns <code>0</code> and sets <code>$!</code> for any other failure. </p>
 </dd>
<dt>sin <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>sin</dt>
<dd> <p> Returns the sine of <font SIZE="-1">EXPR</font> (expressed in radians). If <font SIZE="-1">EXPR</font> is omitted, returns sine of <code>$_</code>. </p>
<p> For the inverse sine operation, you may use the <code>&quot;Math::Trig::asin&quot;</code> function, or use this relation: </p>
<pre><code>    sub asin { atan2($_[0], sqrt(1 - $_[0] * $_[0])) }
</code></pre>
 </dd>
<dt>sleep <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>sleep</dt>
<dd> <p> Causes the script to sleep for (integer) <font SIZE="-1">EXPR</font> seconds, or forever if no argument is given. Returns the integer number of seconds actually slept. </p>
<p> May be interrupted if the process receives a signal such as <code>&quot;SIGALRM&quot;</code>. </p>
<pre><code>    eval {
        local $SIG{ALRM} = sub { die &quot;Alarm!\n&quot; };
        sleep;
    };
    die $@ unless $@ eq &quot;Alarm!\n&quot;;
</code></pre>
<p> You probably cannot mix <code>&quot;alarm&quot;</code> and <code>&quot;sleep&quot;</code> calls, because <code>&quot;sleep&quot;</code> is often implemented using <code>&quot;alarm&quot;</code>. </p>
<p> On some older systems, it may sleep up to a full second less than what you requested, depending on how it counts seconds. Most modern systems always sleep the full amount. They may appear to sleep longer than that, however, because your process might not be scheduled right away in a busy multitasking system. </p>
<p> For delays of finer granularity than one second, the Time::HiRes module (from <font SIZE="-1">CPAN,</font> and starting from Perl 5.8 part of the standard distribution) provides <code>&quot;usleep&quot;</code>. You may also use Perl&#8217;s four-argument version of <code>&quot;select&quot;</code> leaving the first three arguments undefined, or you might be able to use the <code>&quot;syscall&quot;</code> interface to access <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) if your system supports it. See perlfaq8 for details. </p>
<p> See also the <font SIZE="-1">POSIX</font> module&#8217;s <code>&quot;pause&quot;</code> function. </p>
 </dd>
<dt>socket <font SIZE="-1">SOCKET,DOMAIN,TYPE,PROTOCOL</font></dt>
<dd> <p> Opens a socket of the specified kind and attaches it to filehandle <font SIZE="-1">SOCKET.</font> <font SIZE="-1">DOMAIN, TYPE,</font> and <font SIZE="-1">PROTOCOL</font> are specified the same as for the syscall of the same name. You should <code>&quot;use Socket&quot;</code> first to get the proper definitions imported. See the examples in ``Sockets: Client/Server Communication&#8217;&#8216; in perlipc. </p>
<p> On systems that support a close-on-exec flag on files, the flag will be set for the newly opened file descriptor, as determined by the value of <code>$^F</code>. See ``$^F&#8217;&#8216; in perlvar. </p>
 </dd>
<dt>socketpair <font SIZE="-1">SOCKET1,SOCKET2,DOMAIN,TYPE,PROTOCOL</font></dt>
<dd> <p> Creates an unnamed pair of sockets in the specified domain, of the specified type. <font SIZE="-1">DOMAIN, TYPE,</font> and <font SIZE="-1">PROTOCOL</font> are specified the same as for the syscall of the same name. If unimplemented, raises an exception. Returns true if successful. </p>
<p> On systems that support a close-on-exec flag on files, the flag will be set for the newly opened file descriptors, as determined by the value of <code>$^F</code>. See ``$^F&#8217;&#8216; in perlvar. </p>
<p> Some systems define <code>&quot;pipe&quot;</code> in terms of <code>&quot;socketpair&quot;</code>, in which a call to <code>&quot;pipe($rdr, $wtr)&quot;</code> is essentially: </p>
<pre><code>    use Socket;
    socketpair(my $rdr, my $wtr, AF_UNIX, SOCK_STREAM, PF_UNSPEC);
    shutdown($rdr, 1); # no more writing for reader
    shutdown($wtr, 0); # no more reading for writer
</code></pre>
<p> See perlipc for an example of socketpair use. Perl 5.8 and later will emulate socketpair using <font SIZE="-1">IP</font> sockets to localhost if your system implements sockets but not socketpair. </p>
<p> Portability issues: ``socketpair&#8217;&#8216; in perlport. </p>
 </dd>
<dt>sort <font SIZE="-1">SUBNAME LIST</font></dt>
<dd>  </dd>
<dt>sort <font SIZE="-1">BLOCK LIST</font></dt>
<dd>  </dd>
<dt>sort <font SIZE="-1">LIST</font></dt>
<dd> <p> In list context, this sorts the <font SIZE="-1">LIST</font> and returns the sorted list value. In scalar context, the behaviour of <code>&quot;sort&quot;</code> is undefined. </p>
<p> If <font SIZE="-1">SUBNAME</font> or <font SIZE="-1">BLOCK</font> is omitted, <code>&quot;sort&quot;</code>s in standard string comparison order. If <font SIZE="-1">SUBNAME</font> is specified, it gives the name of a subroutine that returns an integer less than, equal to, or greater than <code>0</code>, depending on how the elements of the list are to be ordered. (The <code>&quot;&lt;=&gt;&quot;</code> and <code>&quot;cmp&quot;</code> operators are extremely useful in such routines.) <font SIZE="-1">SUBNAME</font> may be a scalar variable name (unsubscripted), in which case the value provides the name of (or a reference to) the actual subroutine to use. In place of a <font SIZE="-1">SUBNAME,</font> you can provide a <font SIZE="-1">BLOCK</font> as an anonymous, in-line sort subroutine. </p>
<p> If the subroutine&#8217;s prototype is <code>&quot;($$)&quot;</code>, the elements to be compared are passed by reference in <code>@_</code>, as for a normal subroutine. This is slower than unprototyped subroutines, where the elements to be compared are passed into the subroutine as the package global variables <code>$a</code> and <code>$b</code> (see example below). </p>
<p> If the subroutine is an <font SIZE="-1">XSUB,</font> the elements to be compared are pushed on to the stack, the way arguments are usually passed to XSUBs. <code>$a</code> and <code>$b</code> are not set. </p>
<p> The values to be compared are always passed by reference and should not be modified. </p>
<p> You also cannot exit out of the sort block or subroutine using any of the loop control operators described in perlsyn or with <code>&quot;goto&quot;</code>. </p>
<p> When <code>&quot;use locale&quot;</code> (but not <code>&quot;use locale &#8216;:not_characters&#8217;&quot;</code>) is in effect, <code>&quot;sort LIST&quot;</code> sorts <font SIZE="-1">LIST</font> according to the current collation locale. See perllocale. </p>
<p> <code>&quot;sort&quot;</code> returns aliases into the original list, much as a for loop&#8217;s index variable aliases the list elements. That is, modifying an element of a list returned by <code>&quot;sort&quot;</code> (for example, in a <code>&quot;foreach&quot;</code>, <code>&quot;map&quot;</code> or <code>&quot;grep&quot;</code>) actually modifies the element in the original list. This is usually something to be avoided when writing clear code. </p>
<p> Historically Perl has varied in whether sorting is stable by default. If stability matters, it can be controlled explicitly by using the sort pragma. </p>
<p> Examples: </p>
<pre><code>    # sort lexically
    my @articles = sort @files;
    # same thing, but with explicit sort routine
    my @articles = sort {$a cmp $b} @files;
    # now case-insensitively
    my @articles = sort {fc($a) cmp fc($b)} @files;
    # same thing in reversed order
    my @articles = sort {$b cmp $a} @files;
    # sort numerically ascending
    my @articles = sort {$a &lt;=&gt; $b} @files;
    # sort numerically descending
    my @articles = sort {$b &lt;=&gt; $a} @files;
    # this sorts the %age hash by value instead of key
    # using an in-line function
    my @eldest = sort { $age{$b} &lt;=&gt; $age{$a} } keys %age;
    # sort using explicit subroutine name
    sub byage {
        $age{$a} &lt;=&gt; $age{$b}; # presuming numeric
    }
    my @sortedclass = sort byage @class;
    sub backwards { $b cmp $a }
    my @harry = qw(dog cat x Cain Abel);
    my @george = qw(gone chased yz Punished Axed);
    print sort @harry;
        # prints AbelCaincatdogx
    print sort backwards @harry;
        # prints xdogcatCainAbel
    print sort @george, 'to', @harry;
        # prints AbelAxedCainPunishedcatchaseddoggonetoxyz
    # inefficiently sort by descending numeric compare using
    # the first integer after the first = sign, or the
    # whole record case-insensitively otherwise
    my @new = sort {
        ($b =~ /=(\d+)/)[0] &lt;=&gt; ($a =~ /=(\d+)/)[0]
                            ||
                    fc($a) cmp fc($b)
    } @old;
    # same thing, but much more efficiently;
    # we'll build auxiliary indices instead
    # for speed
    my (@nums, @caps);
    for (@old) {
        push @nums, ( /=(\d+)/ ? $1 : undef );
        push @caps, fc($_);
    }
    my @new = @old[ sort {
                           $nums[$b] &lt;=&gt; $nums[$a]
                                    ||
                           $caps[$a] cmp $caps[$b]
                         } 0..$#old
                  ];
    # same thing, but without any temps
    my @new = map { $_-&gt;[0] }
           sort { $b-&gt;[1] &lt;=&gt; $a-&gt;[1]
                           ||
                  $a-&gt;[2] cmp $b-&gt;[2]
           } map { [$_, /=(\d+)/, fc($_)] } @old;
    # using a prototype allows you to use any comparison subroutine
    # as a sort subroutine (including other package's subroutines)
    package Other;
    sub backwards ($$) { $_[1] cmp $_[0]; } # $a and $b are
                                             # not set here
    package main;
    my @new = sort Other::backwards @old;
    # guarantee stability
    use sort 'stable';
    my @new = sort { substr($a, 3, 5) cmp substr($b, 3, 5) } @old;
</code></pre>
<p> Warning: syntactical care is required when sorting the list returned from a function. If you want to sort the list returned by the function call <code>&quot;find_records(@key)&quot;</code>, you can use: </p>
<pre><code>    my @contact = sort { $a cmp $b } find_records @key;
    my @contact = sort +find_records(@key);
    my @contact = sort &amp;find_records(@key);
    my @contact = sort(find_records(@key));
</code></pre>
<p> If instead you want to sort the array <code>@key</code> with the comparison routine <code>&quot;find_records()&quot;</code> then you can use: </p>
<pre><code>    my @contact = sort { find_records() } @key;
    my @contact = sort find_records(@key);
    my @contact = sort(find_records @key);
    my @contact = sort(find_records (@key));
</code></pre>
<p> <code>$a</code> and <code>$b</code> are set as package globals in the package the <code>sort()</code> is called from. That means <code>$main::a</code> and <code>$main::b</code> (or <code>$::a</code> and <code>$::b</code>) in the <code>&quot;main&quot;</code> package, <code>$FooPack::a</code> and <code>$FooPack::b</code> in the <code>&quot;FooPack&quot;</code> package, etc. If the sort block is in scope of a <code>&quot;my&quot;</code> or <code>&quot;state&quot;</code> declaration of <code>$a</code> and/or <code>$b</code>, you <i>must</i> spell out the full name of the variables in the sort block : </p>
<pre><code>   package main;
   my $a = &quot;C&quot;; # DANGER, Will Robinson, DANGER !!!
   print sort { $a cmp $b } qw(A C E G B D F H);
                                          # WRONG
   sub badlexi { $a cmp $b }
   print sort badlexi qw(A C E G B D F H);
                                          # WRONG
   # the above prints BACFEDGH or some other incorrect ordering
   print sort { $::a cmp $::b } qw(A C E G B D F H);
                                          # OK
   print sort { our $a cmp our $b } qw(A C E G B D F H);
                                          # also OK
   print sort { our ($a, $b); $a cmp $b } qw(A C E G B D F H);
                                          # also OK
   sub lexi { our $a cmp our $b }
   print sort lexi qw(A C E G B D F H);
                                          # also OK
   # the above print ABCDEFGH
</code></pre>
<p> With proper care you may mix package and my (or state) <code>$a</code> and/or <code>$b</code>: </p>
<pre><code>   my $a = {
      tiny =&gt; -2,
      small =&gt; -1,
      normal =&gt; 0,
      big =&gt; 1,
      huge =&gt; 2
   };
   say sort { $a-&gt;{our $a} &lt;=&gt; $a-&gt;{our $b} }
       qw{ huge normal tiny small big};
   # prints tinysmallnormalbighuge
</code></pre>
<p> <code>$a</code> and <code>$b</code> are implicitly local to the <code>sort()</code> execution and regain their former values upon completing the sort. </p>
<p> Sort subroutines written using <code>$a</code> and <code>$b</code> are bound to their calling package. It is possible, but of limited interest, to define them in a different package, since the subroutine must still refer to the calling package&#8217;s <code>$a</code> and <code>$b</code> : </p>
<pre><code>   package Foo;
   sub lexi { $Bar::a cmp $Bar::b }
   package Bar;
   ... sort Foo::lexi ...
</code></pre>
<p> Use the prototyped versions (see above) for a more generic alternative. </p>
<p> The comparison function is required to behave. If it returns inconsistent results (sometimes saying <code>$x[1]</code> is less than <code>$x[2]</code> and sometimes saying the opposite, for example) the results are not well-defined. </p>
<p> Because <code>&quot;&lt;=&gt;&quot;</code> returns <code>&quot;undef&quot;</code> when either operand is <code>&quot;NaN&quot;</code> (not-a-number), be careful when sorting with a comparison function like <code>&quot;$a &lt;=&gt; $b&quot;</code> any lists that might contain a <code>&quot;NaN&quot;</code>. The following example takes advantage that <code>&quot;NaN != NaN&quot;</code> to eliminate any <code>&quot;NaN&quot;</code>s from the input list. </p>
<pre><code>    my @result = sort { $a &lt;=&gt; $b } grep { $_ == $_ } @input;
</code></pre>
 </dd>
<dt>splice <font SIZE="-1">ARRAY,OFFSET,LENGTH,LIST</font></dt>
<dd>  </dd>
<dt>splice <font SIZE="-1">ARRAY,OFFSET,LENGTH</font></dt>
<dd>  </dd>
<dt>splice <font SIZE="-1">ARRAY,OFFSET</font></dt>
<dd>  </dd>
<dt>splice <font SIZE="-1">ARRAY</font></dt>
<dd> <p> Removes the elements designated by <font SIZE="-1">OFFSET</font> and <font SIZE="-1">LENGTH</font> from an array, and replaces them with the elements of <font SIZE="-1">LIST,</font> if any. In list context, returns the elements removed from the array. In scalar context, returns the last element removed, or <code>&quot;undef&quot;</code> if no elements are removed. The array grows or shrinks as necessary. If <font SIZE="-1">OFFSET</font> is negative then it starts that far from the end of the array. If <font SIZE="-1">LENGTH</font> is omitted, removes everything from <font SIZE="-1">OFFSET</font> onward. If <font SIZE="-1">LENGTH</font> is negative, removes the elements from <font SIZE="-1">OFFSET</font> onward except for -LENGTH elements at the end of the array. If both <font SIZE="-1">OFFSET</font> and <font SIZE="-1">LENGTH</font> are omitted, removes everything. If <font SIZE="-1">OFFSET</font> is past the end of the array and a <font SIZE="-1">LENGTH</font> was provided, Perl issues a warning, and splices at the end of the array. </p>
<p> The following equivalences hold (assuming <code>&quot;$#a &gt;= $i&quot;</code> ) </p>
<pre><code>    push(@a,$x,$y) splice(@a,@a,0,$x,$y)
    pop(@a) splice(@a,-1)
    shift(@a) splice(@a,0,1)
    unshift(@a,$x,$y) splice(@a,0,0,$x,$y)
    $a[$i] = $y splice(@a,$i,1,$y)
</code></pre>
<p> <code>&quot;splice&quot;</code> can be used, for example, to implement n-ary queue processing: </p>
<pre><code>    sub nary_print {
      my $n = shift;
      while (my @next_n = splice @_, 0, $n) {
        say join q{ -- }, @next_n;
      }
    }
    nary_print(3, qw(a b c d e f g h));
    # prints:
    # a -- b -- c
    # d -- e -- f
    # g -- h
</code></pre>
<p> Starting with Perl 5.14, an experimental feature allowed <code>&quot;splice&quot;</code> to take a scalar expression. This experiment has been deemed unsuccessful, and was removed as of Perl 5.24. </p>
 </dd>
<dt>split /PATTERN/,EXPR,LIMIT</dt>
<dd>  </dd>
<dt>split /PATTERN/,EXPR</dt>
<dd>  </dd>
<dt>split /PATTERN/</dt>
<dd>  </dd>
<dt>split</dt>
<dd> <p> Splits the string <font SIZE="-1">EXPR</font> into a list of strings and returns the list in list context, or the size of the list in scalar context. (Prior to Perl 5.11, it also overwrote <code>@_</code> with the list in void and scalar context. If you target old perls, beware.) </p>
<p> If only <font SIZE="-1">PATTERN</font> is given, <font SIZE="-1">EXPR</font> defaults to <code>$_</code>. </p>
<p> Anything in <font SIZE="-1">EXPR</font> that matches <font SIZE="-1">PATTERN</font> is taken to be a separator that separates the <font SIZE="-1">EXPR</font> into substrings (called &quot;<i>fields</i>&quot;) that do <code>not</code> include the separator. Note that a separator may be longer than one character or even have no characters at all (the empty string, which is a zero-width match). </p>
<p> The <font SIZE="-1">PATTERN</font> need not be constant; an expression may be used to specify a pattern that varies at runtime. </p>
<p> If <font SIZE="-1">PATTERN</font> matches the empty string, the <font SIZE="-1">EXPR</font> is split at the match position (between characters). As an example, the following: </p>
<pre><code>    print join(':', split(/b/, 'abc')), &quot;\n&quot;;
</code></pre>
<p> uses the <code>&quot;b&quot;</code> in <code>&#8216;abc&#8217;</code> as a separator to produce the output <code>&quot;a:c&quot;</code>. However, this: </p>
<pre><code>    print join(':', split(//, 'abc')), &quot;\n&quot;;
</code></pre>
<p> uses empty string matches as separators to produce the output <code>&quot;a:b:c&quot;</code>; thus, the empty string may be used to split <font SIZE="-1">EXPR</font> into a list of its component characters. </p>
<p> As a special case for <code>&quot;split&quot;</code>, the empty pattern given in match operator syntax (<code>&quot;//&quot;</code>) specifically matches the empty string, which is contrary to its usual interpretation as the last successful match. </p>
<p> If <font SIZE="-1">PATTERN</font> is <code>&quot;/^/&quot;</code>, then it is treated as if it used the multiline modifier (<code>&quot;/^/m&quot;</code>), since it isn&#8217;t much use otherwise. </p>
<p> <code>&quot;/m&quot;</code> and any of the other pattern modifiers valid for <code>&quot;qr&quot;</code> (summarized in ``qr/STRING/msixpodualn&#8217;&#8216; in perlop) may be specified explicitly. </p>
<p> As another special case, <code>&quot;split&quot;</code> emulates the default behavior of the command line tool <code>awk</code> when the <font SIZE="-1">PATTERN</font> is either omitted or a string composed of a single space character (such as <code>&#8216; &#8216;</code> or <code>&quot;\x20&quot;</code>, but not e.g. <code>&quot;/ /&quot;</code>). In this case, any leading whitespace in <font SIZE="-1">EXPR</font> is removed before splitting occurs, and the <font SIZE="-1">PATTERN</font> is instead treated as if it were <code>&quot;/\s+/&quot;</code>; in particular, this means that <i>any</i> contiguous whitespace (not just a single space character) is used as a separator. However, this special treatment can be avoided by specifying the pattern <code>&quot;/ /&quot;</code> instead of the string <code>&quot; &quot;</code>, thereby allowing only a single space character to be a separator. In earlier Perls this special case was restricted to the use of a plain <code>&quot; &quot;</code> as the pattern argument to split; in Perl 5.18.0 and later this special case is triggered by any expression which evaluates to the simple string <code>&quot; &quot;</code>. </p>
<p> As of Perl 5.28, this special-cased whitespace splitting works as expected in the scope of <code>&quot;use feature &#8216;unicode_strings&quot;</code>. In previous versions, and outside the scope of that feature, it exhibits ``The &#8216;&#8216;Unicode Bug&quot;&quot; in perlunicode: characters that are whitespace according to Unicode rules but not according to <font SIZE="-1">ASCII</font> rules can be treated as part of fields rather than as field separators, depending on the string&#8217;s internal encoding. </p>
<p> If omitted, <font SIZE="-1">PATTERN</font> defaults to a single space, <code>&quot; &quot;</code>, triggering the previously described <i>awk</i> emulation. </p>
<p> If <font SIZE="-1">LIMIT</font> is specified and positive, it represents the maximum number of fields into which the <font SIZE="-1">EXPR</font> may be split; in other words, <font SIZE="-1">LIMIT</font> is one greater than the maximum number of times <font SIZE="-1">EXPR</font> may be split. Thus, the <font SIZE="-1">LIMIT</font> value <code>1</code> means that <font SIZE="-1">EXPR</font> may be split a maximum of zero times, producing a maximum of one field (namely, the entire value of <font SIZE="-1">EXPR</font>). For instance: </p>
<pre><code>    print join(':', split(//, 'abc', 1)), &quot;\n&quot;;
</code></pre>
<p> produces the output <code>&quot;abc&quot;</code>, and this: </p>
<pre><code>    print join(':', split(//, 'abc', 2)), &quot;\n&quot;;
</code></pre>
<p> produces the output <code>&quot;a:bc&quot;</code>, and each of these: </p>
<pre><code>    print join(':', split(//, 'abc', 3)), &quot;\n&quot;;
    print join(':', split(//, 'abc', 4)), &quot;\n&quot;;
</code></pre>
<p> produces the output <code>&quot;a:b:c&quot;</code>. </p>
<p> If <font SIZE="-1">LIMIT</font> is negative, it is treated as if it were instead arbitrarily large; as many fields as possible are produced. </p>
<p> If <font SIZE="-1">LIMIT</font> is omitted (or, equivalently, zero), then it is usually treated as if it were instead negative but with the exception that trailing empty fields are stripped (empty leading fields are always preserved); if all fields are empty, then all fields are considered to be trailing (and are thus stripped in this case). Thus, the following: </p>
<pre><code>    print join(':', split(/,/, 'a,b,c,,,')), &quot;\n&quot;;
</code></pre>
<p> produces the output <code>&quot;a:b:c&quot;</code>, but the following: </p>
<pre><code>    print join(':', split(/,/, 'a,b,c,,,', -1)), &quot;\n&quot;;
</code></pre>
<p> produces the output <code>&quot;a:b:c:::&quot;</code>. </p>
<p> In time-critical applications, it is worthwhile to avoid splitting into more fields than necessary. Thus, when assigning to a list, if <font SIZE="-1">LIMIT</font> is omitted (or zero), then <font SIZE="-1">LIMIT</font> is treated as though it were one larger than the number of variables in the list; for the following, <font SIZE="-1">LIMIT</font> is implicitly 3: </p>
<pre><code>    my ($login, $passwd) = split(/:/);
</code></pre>
<p> Note that splitting an <font SIZE="-1">EXPR</font> that evaluates to the empty string always produces zero fields, regardless of the <font SIZE="-1">LIMIT</font> specified. </p>
<p> An empty leading field is produced when there is a positive-width match at the beginning of <font SIZE="-1">EXPR.</font> For instance: </p>
<pre><code>    print join(':', split(/ /, ' abc')), &quot;\n&quot;;
</code></pre>
<p> produces the output <code>&quot;:abc&quot;</code>. However, a zero-width match at the beginning of <font SIZE="-1">EXPR</font> never produces an empty field, so that: </p>
<pre><code>    print join(':', split(//, ' abc'));
</code></pre>
<p> produces the output <code>&quot; :a:b:c&quot;</code> (rather than <code>&quot;: :a:b:c&quot;</code>). </p>
<p> An empty trailing field, on the other hand, is produced when there is a match at the end of <font SIZE="-1">EXPR,</font> regardless of the length of the match (of course, unless a non-zero <font SIZE="-1">LIMIT</font> is given explicitly, such fields are removed, as in the last example). Thus: </p>
<pre><code>    print join(':', split(//, ' abc', -1)), &quot;\n&quot;;
</code></pre>
<p> produces the output <code>&quot; :a:b:c:&quot;</code>. </p>
<p> If the <font SIZE="-1">PATTERN</font> contains capturing groups, then for each separator, an additional field is produced for each substring captured by a group (in the order in which the groups are specified, as per backreferences); if any group does not match, then it captures the <code>&quot;undef&quot;</code> value instead of a substring. Also, note that any such additional field is produced whenever there is a separator (that is, whenever a split occurs), and such an additional field does <code>not</code> count towards the <font SIZE="-1">LIMIT.</font> Consider the following expressions evaluated in list context (each returned list is provided in the associated comment): </p>
<pre><code>    split(/-|,/, &quot;1-10,20&quot;, 3)
    # ('1', '10', '20')
    split(/(-|,)/, &quot;1-10,20&quot;, 3)
    # ('1', '-', '10', ',', '20')
    split(/-|(,)/, &quot;1-10,20&quot;, 3)
    # ('1', undef, '10', ',', '20')
    split(/(-)|,/, &quot;1-10,20&quot;, 3)
    # ('1', '-', '10', undef, '20')
    split(/(-)|(,)/, &quot;1-10,20&quot;, 3)
    # ('1', '-', undef, '10', undef, ',', '20')
</code></pre>
 </dd>
<dt>sprintf <font SIZE="-1">FORMAT, LIST</font></dt>
<dd> <p> Returns a string formatted by the usual <code>&quot;printf&quot;</code> conventions of the C library function <code>&quot;sprintf&quot;</code>. See below for more details and see <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) or <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) on your system for an explanation of the general principles. </p>
<p> For example: </p>
<pre><code>        # Format number with up to 8 leading zeroes
        my $result = sprintf(&quot;%08d&quot;, $number);
        # Round number to 3 digits after decimal point
        my $rounded = sprintf(&quot;%.3f&quot;, $number);
</code></pre>
<p> Perl does its own <code>&quot;sprintf&quot;</code> formatting: it emulates the C function <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), but doesn&#8217;t use it except for floating-point numbers, and even then only standard modifiers are allowed. Non-standard extensions in your local <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) are therefore unavailable from Perl. </p>
<p> Unlike <code>&quot;printf&quot;</code>, <code>&quot;sprintf&quot;</code> does not do what you probably mean when you pass it an array as your first argument. The array is given scalar context, and instead of using the 0th element of the array as the format, Perl will use the count of elements in the array as the format, which is almost never useful. </p>
<p> Perl&#8217;s <code>&quot;sprintf&quot;</code> permits the following universally-known conversions: </p>
<pre><code>   %% a percent sign
   %c a character with the given number
   %s a string
   %d a signed integer, in decimal
   %u an unsigned integer, in decimal
   %o an unsigned integer, in octal
   %x an unsigned integer, in hexadecimal
   %e a floating-point number, in scientific notation
   %f a floating-point number, in fixed decimal notation
   %g a floating-point number, in %e or %f notation
</code></pre>
<p> In addition, Perl permits the following widely-supported conversions: </p>
<pre><code>   %X like %x, but using upper-case letters
   %E like %e, but using an upper-case &quot;E&quot;
   %G like %g, but with an upper-case &quot;E&quot; (if applicable)
   %b an unsigned integer, in binary
   %B like %b, but using an upper-case &quot;B&quot; with the # flag
   %p a pointer (outputs the Perl value's address in hexadecimal)
   %n special: *stores* the number of characters output so far
         into the next argument in the parameter list
   %a hexadecimal floating point
   %A like %a, but using upper-case letters
</code></pre>
<p> Finally, for backward (and we do mean ``backward&#8217;&#8216;) compatibility, Perl permits these unnecessary but widely-supported conversions: </p>
<pre><code>   %i a synonym for %d
   %D a synonym for %ld
   %U a synonym for %lu
   %O a synonym for %lo
   %F a synonym for %f
</code></pre>
<p> Note that the number of exponent digits in the scientific notation produced by <code>%e</code>, <code>%E</code>, <code>%g</code> and <code>%G</code> for numbers with the modulus of the exponent less than 100 is system-dependent: it may be three or less (zero-padded as necessary). In other words, 1.23 times ten to the 99th may be either ``1.23e99&#8217;&#8216; or ``1.23e099&#8217;&#8216;. Similarly for <code>%a</code> and <code>%A</code>: the exponent or the hexadecimal digits may float: especially the ``long doubles&#8217;&#8216; Perl configuration option may cause surprises. </p>
<p> Between the <code>&quot;%&quot;</code> and the format letter, you may specify several additional attributes controlling the interpretation of the format. In order, these are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>format parameter index</dt>
<dd> <p> An explicit format parameter index, such as <code>&quot;2$&quot;</code>. By default sprintf will format the next unused argument in the list, but this allows you to take the arguments out of order: </p>
<pre><code>  printf '%2$d %1$d', 12, 34; # prints &quot;34 12&quot;
  printf '%3$d %d %1$d', 1, 2, 3; # prints &quot;3 1 1&quot;
</code></pre>
 </dd>
<dt>flags</dt>
<dd> <p> one or more of: </p>
<pre><code>   space prefix non-negative number with a space
   + prefix non-negative number with a plus sign
   - left-justify within the field
   0 use zeros, not spaces, to right-justify
   # ensure the leading &quot;0&quot; for any octal,
           prefix non-zero hexadecimal with &quot;0x&quot; or &quot;0X&quot;,
           prefix non-zero binary with &quot;0b&quot; or &quot;0B&quot;
</code></pre>
<p> For example: </p>
<pre><code>  printf '&lt;% d&gt;', 12; # prints &quot;&lt; 12&gt;&quot;
  printf '&lt;% d&gt;', 0; # prints &quot;&lt; 0&gt;&quot;
  printf '&lt;% d&gt;', -12; # prints &quot;&lt;-12&gt;&quot;
  printf '&lt;%+d&gt;', 12; # prints &quot;&lt;+12&gt;&quot;
  printf '&lt;%+d&gt;', 0; # prints &quot;&lt;+0&gt;&quot;
  printf '&lt;%+d&gt;', -12; # prints &quot;&lt;-12&gt;&quot;
  printf '&lt;%6s&gt;', 12; # prints &quot;&lt; 12&gt;&quot;
  printf '&lt;%-6s&gt;', 12; # prints &quot;&lt;12 &gt;&quot;
  printf '&lt;%06s&gt;', 12; # prints &quot;&lt;000012&gt;&quot;
  printf '&lt;%#o&gt;', 12; # prints &quot;&lt;014&gt;&quot;
  printf '&lt;%#x&gt;', 12; # prints &quot;&lt;0xc&gt;&quot;
  printf '&lt;%#X&gt;', 12; # prints &quot;&lt;0XC&gt;&quot;
  printf '&lt;%#b&gt;', 12; # prints &quot;&lt;0b1100&gt;&quot;
  printf '&lt;%#B&gt;', 12; # prints &quot;&lt;0B1100&gt;&quot;
</code></pre>
<p> When a space and a plus sign are given as the flags at once, the space is ignored. </p>
<pre><code>  printf '&lt;%+ d&gt;', 12; # prints &quot;&lt;+12&gt;&quot;
  printf '&lt;% +d&gt;', 12; # prints &quot;&lt;+12&gt;&quot;
</code></pre>
<p> When the # flag and a precision are given in the <code>%o</code> conversion, the precision is incremented if it&#8217;s necessary for the leading ``0&#8217;&#8216;. </p>
<pre><code>  printf '&lt;%#.5o&gt;', 012; # prints &quot;&lt;00012&gt;&quot;
  printf '&lt;%#.5o&gt;', 012345; # prints &quot;&lt;012345&gt;&quot;
  printf '&lt;%#.0o&gt;', 0; # prints &quot;&lt;0&gt;&quot;
</code></pre>
 </dd>
<dt>vector flag</dt>
<dd> <p> This flag tells Perl to interpret the supplied string as a vector of integers, one for each character in the string. Perl applies the format to each integer in turn, then joins the resulting strings with a separator (a dot <code>&quot;.&quot;</code> by default). This can be useful for displaying ordinal values of characters in arbitrary strings: </p>
<pre><code>  printf &quot;%vd&quot;, &quot;AB\x{100}&quot;; # prints &quot;65.66.256&quot;
  printf &quot;version is v%vd\n&quot;, $^V; # Perl's version
</code></pre>
<p> Put an asterisk <code>&quot;*&quot;</code> before the <code>&quot;v&quot;</code> to override the string to use to separate the numbers: </p>
<pre><code>  printf &quot;address is %*vX\n&quot;, &quot;:&quot;, $addr; # IPv6 address
  printf &quot;bits are %0*v8b\n&quot;, &quot; &quot;, $bits; # random bitstring
</code></pre>
<p> You can also explicitly specify the argument number to use for the join string using something like <code>&quot;*2$v&quot;</code>; for example: </p>
<pre><code>  printf '%*4$vX %*4$vX %*4$vX', # 3 IPv6 addresses
          @addr[1..3], &quot;:&quot;;
</code></pre>
 </dd>
<dt>(minimum) width</dt>
<dd> <p> Arguments are usually formatted to be only as wide as required to display the given value. You can override the width by putting a number here, or get the width from the next argument (with <code>&quot;*&quot;</code>) or from a specified argument (e.g., with <code>&quot;*2$&quot;</code>): </p>
<pre><code> printf &quot;&lt;%s&gt;&quot;, &quot;a&quot;; # prints &quot;&lt;a&gt;&quot;
 printf &quot;&lt;%6s&gt;&quot;, &quot;a&quot;; # prints &quot;&lt; a&gt;&quot;
 printf &quot;&lt;%*s&gt;&quot;, 6, &quot;a&quot;; # prints &quot;&lt; a&gt;&quot;
 printf '&lt;%*2$s&gt;', &quot;a&quot;, 6; # prints &quot;&lt; a&gt;&quot;
 printf &quot;&lt;%2s&gt;&quot;, &quot;long&quot;; # prints &quot;&lt;long&gt;&quot; (does not truncate)
</code></pre>
<p> If a field width obtained through <code>&quot;*&quot;</code> is negative, it has the same effect as the <code>&quot;-&quot;</code> flag: left-justification. </p>
 </dd>
<dt>precision, or maximum width</dt>
<dd> <p> You can specify a precision (for numeric conversions) or a maximum width (for string conversions) by specifying a <code>&quot;.&quot;</code> followed by a number. For floating-point formats except <code>&quot;g&quot;</code> and <code>&quot;G&quot;</code>, this specifies how many places right of the decimal point to show (the default being 6). For example: </p>
<pre><code>  # these examples are subject to system-specific variation
  printf '&lt;%f&gt;', 1; # prints &quot;&lt;1.000000&gt;&quot;
  printf '&lt;%.1f&gt;', 1; # prints &quot;&lt;1.0&gt;&quot;
  printf '&lt;%.0f&gt;', 1; # prints &quot;&lt;1&gt;&quot;
  printf '&lt;%e&gt;', 10; # prints &quot;&lt;1.000000e+01&gt;&quot;
  printf '&lt;%.1e&gt;', 10; # prints &quot;&lt;1.0e+01&gt;&quot;
</code></pre>
<p> For ``g&#8217;&#8216; and ``G&#8217;&#8216;, this specifies the maximum number of significant digits to show; for example: </p>
<pre><code>  # These examples are subject to system-specific variation.
  printf '&lt;%g&gt;', 1; # prints &quot;&lt;1&gt;&quot;
  printf '&lt;%.10g&gt;', 1; # prints &quot;&lt;1&gt;&quot;
  printf '&lt;%g&gt;', 100; # prints &quot;&lt;100&gt;&quot;
  printf '&lt;%.1g&gt;', 100; # prints &quot;&lt;1e+02&gt;&quot;
  printf '&lt;%.2g&gt;', 100.01; # prints &quot;&lt;1e+02&gt;&quot;
  printf '&lt;%.5g&gt;', 100.01; # prints &quot;&lt;100.01&gt;&quot;
  printf '&lt;%.4g&gt;', 100.01; # prints &quot;&lt;100&gt;&quot;
  printf '&lt;%.1g&gt;', 0.0111; # prints &quot;&lt;0.01&gt;&quot;
  printf '&lt;%.2g&gt;', 0.0111; # prints &quot;&lt;0.011&gt;&quot;
  printf '&lt;%.3g&gt;', 0.0111; # prints &quot;&lt;0.0111&gt;&quot;
</code></pre>
<p> For integer conversions, specifying a precision implies that the output of the number itself should be zero-padded to this width, where the 0 flag is ignored: </p>
<pre><code>  printf '&lt;%.6d&gt;', 1; # prints &quot;&lt;000001&gt;&quot;
  printf '&lt;%+.6d&gt;', 1; # prints &quot;&lt;+000001&gt;&quot;
  printf '&lt;%-10.6d&gt;', 1; # prints &quot;&lt;000001 &gt;&quot;
  printf '&lt;%10.6d&gt;', 1; # prints &quot;&lt; 000001&gt;&quot;
  printf '&lt;%010.6d&gt;', 1; # prints &quot;&lt; 000001&gt;&quot;
  printf '&lt;%+10.6d&gt;', 1; # prints &quot;&lt; +000001&gt;&quot;
  printf '&lt;%.6x&gt;', 1; # prints &quot;&lt;000001&gt;&quot;
  printf '&lt;%#.6x&gt;', 1; # prints &quot;&lt;0x000001&gt;&quot;
  printf '&lt;%-10.6x&gt;', 1; # prints &quot;&lt;000001 &gt;&quot;
  printf '&lt;%10.6x&gt;', 1; # prints &quot;&lt; 000001&gt;&quot;
  printf '&lt;%010.6x&gt;', 1; # prints &quot;&lt; 000001&gt;&quot;
  printf '&lt;%#10.6x&gt;', 1; # prints &quot;&lt; 0x000001&gt;&quot;
</code></pre>
<p> For string conversions, specifying a precision truncates the string to fit the specified width: </p>
<pre><code>  printf '&lt;%.5s&gt;', &quot;truncated&quot;; # prints &quot;&lt;trunc&gt;&quot;
  printf '&lt;%10.5s&gt;', &quot;truncated&quot;; # prints &quot;&lt; trunc&gt;&quot;
</code></pre>
<p> You can also get the precision from the next argument using <code>&quot;.*&quot;</code>, or from a specified argument (e.g., with <code>&quot;.*2$&quot;</code>): </p>
<pre><code>  printf '&lt;%.6x&gt;', 1; # prints &quot;&lt;000001&gt;&quot;
  printf '&lt;%.*x&gt;', 6, 1; # prints &quot;&lt;000001&gt;&quot;
  printf '&lt;%.*2$x&gt;', 1, 6; # prints &quot;&lt;000001&gt;&quot;
  printf '&lt;%6.*2$x&gt;', 1, 4; # prints &quot;&lt; 0001&gt;&quot;
</code></pre>
<p> If a precision obtained through <code>&quot;*&quot;</code> is negative, it counts as having no precision at all. </p>
<pre><code>  printf '&lt;%.*s&gt;', 7, &quot;string&quot;; # prints &quot;&lt;string&gt;&quot;
  printf '&lt;%.*s&gt;', 3, &quot;string&quot;; # prints &quot;&lt;str&gt;&quot;
  printf '&lt;%.*s&gt;', 0, &quot;string&quot;; # prints &quot;&lt;&gt;&quot;
  printf '&lt;%.*s&gt;', -1, &quot;string&quot;; # prints &quot;&lt;string&gt;&quot;
  printf '&lt;%.*d&gt;', 1, 0; # prints &quot;&lt;0&gt;&quot;
  printf '&lt;%.*d&gt;', 0, 0; # prints &quot;&lt;&gt;&quot;
  printf '&lt;%.*d&gt;', -1, 0; # prints &quot;&lt;0&gt;&quot;
</code></pre>
 </dd>
<dt>size</dt>
<dd> <p> For numeric conversions, you can specify the size to interpret the number as using <code>&quot;l&quot;</code>, <code>&quot;h&quot;</code>, <code>&quot;V&quot;</code>, <code>&quot;q&quot;</code>, <code>&quot;L&quot;</code>, or <code>&quot;ll&quot;</code>. For integer conversions (<code>&quot;d u o x X b i D U O&quot;</code>), numbers are usually assumed to be whatever the default integer size is on your platform (usually 32 or 64 bits), but you can override this to use instead one of the standard C types, as supported by the compiler used to build Perl: </p>
<pre><code>   hh interpret integer as C type &quot;char&quot; or &quot;unsigned
               char&quot; on Perl 5.14 or later
   h interpret integer as C type &quot;short&quot; or
               &quot;unsigned short&quot;
   j interpret integer as C type &quot;intmax_t&quot; on Perl
               5.14 or later; and prior to Perl 5.30, only with
               a C99 compiler (unportable)
   l interpret integer as C type &quot;long&quot; or
               &quot;unsigned long&quot;
   q, L, or ll interpret integer as C type &quot;long long&quot;,
               &quot;unsigned long long&quot;, or &quot;quad&quot; (typically
               64-bit integers)
   t interpret integer as C type &quot;ptrdiff_t&quot; on Perl
               5.14 or later
   z interpret integer as C type &quot;size_t&quot; on Perl 5.14
               or later
</code></pre>
<p> As of 5.14, none of these raises an exception if they are not supported on your platform. However, if warnings are enabled, a warning of the <code>&quot;printf&quot;</code> warning class is issued on an unsupported conversion flag. Should you instead prefer an exception, do this: </p>
<pre><code>    use warnings FATAL =&gt; &quot;printf&quot;;
</code></pre>
<p> If you would like to know about a version dependency before you start running the program, put something like this at its top: </p>
<pre><code>    use 5.014; # for hh/j/t/z/ printf modifiers
</code></pre>
<p> You can find out whether your Perl supports quads via Config: </p>
<pre><code>    use Config;
    if ($Config{use64bitint} eq &quot;define&quot;
        || $Config{longsize} &gt;= 8) {
        print &quot;Nice quads!\n&quot;;
    }
</code></pre>
<p> For floating-point conversions (<code>&quot;e f g E F G&quot;</code>), numbers are usually assumed to be the default floating-point size on your platform (double or long double), but you can force ``long double&#8217;&#8216; with <code>&quot;q&quot;</code>, <code>&quot;L&quot;</code>, or <code>&quot;ll&quot;</code> if your platform supports them. You can find out whether your Perl supports long doubles via Config: </p>
<pre><code>    use Config;
    print &quot;long doubles\n&quot; if $Config{d_longdbl} eq &quot;define&quot;;
</code></pre>
<p> You can find out whether Perl considers ``long double&#8217;&#8216; to be the default floating-point size to use on your platform via Config: </p>
<pre><code>    use Config;
    if ($Config{uselongdouble} eq &quot;define&quot;) {
        print &quot;long doubles by default\n&quot;;
    }
</code></pre>
<p> It can also be that long doubles and doubles are the same thing: </p>
<pre><code>        use Config;
        ($Config{doublesize} == $Config{longdblsize}) &amp;&amp;
                print &quot;doubles are long doubles\n&quot;;
</code></pre>
<p> The size specifier <code>&quot;V&quot;</code> has no effect for Perl code, but is supported for compatibility with <font SIZE="-1">XS</font> code. It means ``use the standard size for a Perl integer or floating-point number&#8217;&#8216;, which is the default. </p>
 </dd>
<dt>order of arguments</dt>
<dd> <p> Normally, <code>&quot;sprintf&quot;</code> takes the next unused argument as the value to format for each format specification. If the format specification uses <code>&quot;*&quot;</code> to require additional arguments, these are consumed from the argument list in the order they appear in the format specification <i>before</i> the value to format. Where an argument is specified by an explicit index, this does not affect the normal order for the arguments, even when the explicitly specified index would have been the next argument. </p>
<p> So: </p>
<pre><code>    printf &quot;&lt;%*.*s&gt;&quot;, $a, $b, $c;
</code></pre>
<p> uses <code>$a</code> for the width, <code>$b</code> for the precision, and <code>$c</code> as the value to format; while: </p>
<pre><code>  printf '&lt;%*1$.*s&gt;', $a, $b;
</code></pre>
<p> would use <code>$a</code> for the width and precision, and <code>$b</code> as the value to format. </p>
<p> Here are some more examples; be aware that when using an explicit index, the <code>&quot;$&quot;</code> may need escaping: </p>
<pre><code> printf &quot;%2\$d %d\n&quot;, 12, 34; # will print &quot;34 12\n&quot;
 printf &quot;%2\$d %d %d\n&quot;, 12, 34; # will print &quot;34 12 34\n&quot;
 printf &quot;%3\$d %d %d\n&quot;, 12, 34, 56; # will print &quot;56 12 34\n&quot;
 printf &quot;%2\$*3\$d %d\n&quot;, 12, 34, 3; # will print &quot; 34 12\n&quot;
 printf &quot;%*1\$.*f\n&quot;, 4, 5, 10; # will print &quot;5.0000\n&quot;
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> If <code>&quot;use locale&quot;</code> (including <code>&quot;use locale &#8216;:not_characters&#8217;&quot;</code>) is in effect and <code>&quot;POSIX::setlocale&quot;</code> has been called, the character used for the decimal separator in formatted floating-point numbers is affected by the <code>&quot;LC_NUMERIC&quot;</code> locale. See perllocale and <font SIZE="-1">POSIX</font>. </p>
 </dd></dl>
<dt>sqrt <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>sqrt</dt>
<dd> <p> Return the positive square root of <font SIZE="-1">EXPR.</font> If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. Works only for non-negative operands unless you&#8217;ve loaded the <code>&quot;Math::Complex&quot;</code> module. </p>
<pre><code>    use Math::Complex;
    print sqrt(-4); # prints 2i
</code></pre>
 </dd>
<dt>srand <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>srand</dt>
<dd> <p> Sets and returns the random number seed for the <code>&quot;rand&quot;</code> operator. </p>
<p> The point of the function is to ``seed&#8217;&#8216; the <code>&quot;rand&quot;</code> function so that <code>&quot;rand&quot;</code> can produce a different sequence each time you run your program. When called with a parameter, <code>&quot;srand&quot;</code> uses that for the seed; otherwise it (semi-)randomly chooses a seed. In either case, starting with Perl 5.14, it returns the seed. To signal that your code will work <i>only</i> on Perls of a recent vintage: </p>
<pre><code>    use 5.014; # so srand returns the seed
</code></pre>
<p> If <code>&quot;srand&quot;</code> is not called explicitly, it is called implicitly without a parameter at the first use of the <code>&quot;rand&quot;</code> operator. However, there are a few situations where programs are likely to want to call <code>&quot;srand&quot;</code>. One is for generating predictable results, generally for testing or debugging. There, you use <code>&quot;srand($seed)&quot;</code>, with the same <code>$seed</code> each time. Another case is that you may want to call <code>&quot;srand&quot;</code> after a <code>&quot;fork&quot;</code> to avoid child processes sharing the same seed value as the parent (and consequently each other). </p>
<p> Do <code>not</code> call <code>&quot;srand()&quot;</code> (i.e., without an argument) more than once per process. The internal state of the random number generator should contain more entropy than can be provided by any seed, so calling <code>&quot;srand&quot;</code> again actually <i>loses</i> randomness. </p>
<p> Most implementations of <code>&quot;srand&quot;</code> take an integer and will silently truncate decimal numbers. This means <code>&quot;srand(42)&quot;</code> will usually produce the same results as <code>&quot;srand(42.1)&quot;</code>. To be safe, always pass <code>&quot;srand&quot;</code> an integer. </p>
<p> A typical use of the returned seed is for a test program which has too many combinations to test comprehensively in the time available to it each run. It can test a random subset each time, and should there be a failure, log the seed used for that run so that it can later be used to reproduce the same results. </p>
<p> &quot;rand&quot;<code> is not cryptographically secure. You should not rely on it in security-sensitive situations.</code> As of this writing, a number of third-party <font SIZE="-1">CPAN</font> modules offer random number generators intended by their authors to be cryptographically secure, including: Data::Entropy, Crypt::Random, Math::Random::Secure, and Math::TrulyRandom. </p>
 </dd>
<dt>stat <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>stat <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>stat <font SIZE="-1">DIRHANDLE</font></dt>
<dd>  </dd>
<dt>stat</dt>
<dd> <p> Returns a 13-element list giving the status info for a file, either the file opened via <font SIZE="-1">FILEHANDLE</font> or <font SIZE="-1">DIRHANDLE,</font> or named by <font SIZE="-1">EXPR.</font> If <font SIZE="-1">EXPR</font> is omitted, it stats <code>$_</code> (not <code>&quot;_&quot;</code>!). Returns the empty list if <code>&quot;stat&quot;</code> fails. Typically used as follows: </p>
<pre><code>    my ($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,
        $atime,$mtime,$ctime,$blksize,$blocks)
           = stat($filename);
</code></pre>
<p> Not all fields are supported on all filesystem types. Here are the meanings of the fields: </p>
<pre><code>  0 dev device number of filesystem
  1 ino inode number
  2 mode file mode (type and permissions)
  3 nlink number of (hard) links to the file
  4 uid numeric user ID of file's owner
  5 gid numeric group ID of file's owner
  6 rdev the device identifier (special files only)
  7 size total size of file, in bytes
  8 atime last access time in seconds since the epoch
  9 mtime last modify time in seconds since the epoch
 10 ctime inode change time in seconds since the epoch (*)
 11 blksize preferred I/O size in bytes for interacting with the
             file (may vary from file to file)
 12 blocks actual number of system-specific blocks allocated
             on disk (often, but not always, 512 bytes each)
</code></pre>
<p> (The epoch was at 00:00 January 1, 1970 <font SIZE="-1">GMT.</font>) </p>
<p> (*) Not all fields are supported on all filesystem types. Notably, the ctime field is non-portable. In particular, you cannot expect it to be a ``creation time&#8217;&#8216;; see ``Files and Filesystems&#8217;&#8216; in perlport for details. </p>
<p> If <code>&quot;stat&quot;</code> is passed the special filehandle consisting of an underline, no stat is done, but the current contents of the stat structure from the last <code>&quot;stat&quot;</code>, <code>&quot;lstat&quot;</code>, or filetest are returned. Example: </p>
<pre><code>    if (-x $file &amp;&amp; (($d) = stat(_)) &amp;&amp; $d &lt; 0) {
        print &quot;$file is executable NFS file\n&quot;;
    }
</code></pre>
<p> (This works on machines only for which the device number is negative under <font SIZE="-1">NFS.</font>) </p>
<p> On some platforms inode numbers are of a type larger than perl knows how to handle as integer numerical values. If necessary, an inode number will be returned as a decimal string in order to preserve the entire value. If used in a numeric context, this will be converted to a floating-point numerical value, with rounding, a fate that is best avoided. Therefore, you should prefer to compare inode numbers using <code>&quot;eq&quot;</code> rather than <code>&quot;==&quot;</code>. <code>&quot;eq&quot;</code> will work fine on inode numbers that are represented numerically, as well as those represented as strings. </p>
<p> Because the mode contains both the file type and its permissions, you should mask off the file type portion and (s)printf using a <code>&quot;%o&quot;</code> if you want to see the real permissions. </p>
<pre><code>    my $mode = (stat($filename))[2];
    printf &quot;Permissions are %04o\n&quot;, $mode &amp; 07777;
</code></pre>
<p> In scalar context, <code>&quot;stat&quot;</code> returns a boolean value indicating success or failure, and, if successful, sets the information associated with the special filehandle <code>&quot;_&quot;</code>. </p>
<p> The File::stat module provides a convenient, by-name access mechanism: </p>
<pre><code>    use File::stat;
    my $sb = stat($filename);
    printf &quot;File is %s, size is %s, perm %04o, mtime %s\n&quot;,
           $filename, $sb-&gt;size, $sb-&gt;mode &amp; 07777,
           scalar localtime $sb-&gt;mtime;
</code></pre>
<p> You can import symbolic mode constants (<code>&quot;S_IF*&quot;</code>) and functions (<code>&quot;S_IS*&quot;</code>) from the Fcntl module: </p>
<pre><code>    use Fcntl ':mode';
    my $mode = (stat($filename))[2];
    my $user_rwx = ($mode &amp; S_IRWXU) &gt;&gt; 6;
    my $group_read = ($mode &amp; S_IRGRP) &gt;&gt; 3;
    my $other_execute = $mode &amp; S_IXOTH;
    printf &quot;Permissions are %04o\n&quot;, S_IMODE($mode), &quot;\n&quot;;
    my $is_setuid = $mode &amp; S_ISUID;
    my $is_directory = S_ISDIR($mode);
</code></pre>
<p> You could write the last two using the <code>&quot;-u&quot;</code> and <code>&quot;-d&quot;</code> operators. Commonly available <code>&quot;S_IF*&quot;</code> constants are: </p>
<pre><code>    # Permissions: read, write, execute, for user, group, others.
    S_IRWXU S_IRUSR S_IWUSR S_IXUSR
    S_IRWXG S_IRGRP S_IWGRP S_IXGRP
    S_IRWXO S_IROTH S_IWOTH S_IXOTH
    # Setuid/Setgid/Stickiness/SaveText.
    # Note that the exact meaning of these is system-dependent.
    S_ISUID S_ISGID S_ISVTX S_ISTXT
    # File types. Not all are necessarily available on
    # your system.
    S_IFREG S_IFDIR S_IFLNK S_IFBLK S_IFCHR
    S_IFIFO S_IFSOCK S_IFWHT S_ENFMT
    # The following are compatibility aliases for S_IRUSR,
    # S_IWUSR, and S_IXUSR.
    S_IREAD S_IWRITE S_IEXEC
</code></pre>
<p> and the <code>&quot;S_IF*&quot;</code> functions are </p>
<pre><code>    S_IMODE($mode) the part of $mode containing the permission
                      bits and the setuid/setgid/sticky bits
    S_IFMT($mode) the part of $mode containing the file type
                      which can be bit-anded with (for example)
                      S_IFREG or with the following functions
    # The operators -f, -d, -l, -b, -c, -p, and -S.
    S_ISREG($mode) S_ISDIR($mode) S_ISLNK($mode)
    S_ISBLK($mode) S_ISCHR($mode) S_ISFIFO($mode) S_ISSOCK($mode)
    # No direct -X operator counterpart, but for the first one
    # the -g operator is often equivalent. The ENFMT stands for
    # record flocking enforcement, a platform-dependent feature.
    S_ISENFMT($mode) S_ISWHT($mode)
</code></pre>
<p> See your native <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2) and <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) documentation for more details about the <code>&quot;S_*&quot;</code> constants. To get status info for a symbolic link instead of the target file behind the link, use the <code>&quot;lstat&quot;</code> function. </p>
<p> Portability issues: ``stat&#8217;&#8216; in perlport. </p>
 </dd>
<dt>state <font SIZE="-1">VARLIST</font></dt>
<dd>  </dd>
<dt>state <font SIZE="-1">TYPE VARLIST</font></dt>
<dd>  </dd>
<dt>state <font SIZE="-1">VARLIST : ATTRS</font></dt>
<dd>  </dd>
<dt>state <font SIZE="-1">TYPE VARLIST : ATTRS</font></dt>
<dd> <p> <code>&quot;state&quot;</code> declares a lexically scoped variable, just like <code>&quot;my&quot;</code>. However, those variables will never be reinitialized, contrary to lexical variables that are reinitialized each time their enclosing block is entered. See ``Persistent Private Variables&#8217;&#8216; in perlsub for details. </p>
<p> If more than one variable is listed, the list must be placed in parentheses. With a parenthesised list, <code>&quot;undef&quot;</code> can be used as a dummy placeholder. However, since initialization of state variables in such lists is currently not possible this would serve no purpose. </p>
<p> <code>&quot;state&quot;</code> is available only if the <code>&quot;state&quot;</code> feature is enabled or if it is prefixed with <code>&quot;CORE::&quot;</code>. The <code>&quot;state&quot;</code> feature is enabled automatically with a <code>&quot;use v5.10&quot;</code> (or higher) declaration in the current scope. </p>
 </dd>
<dt>study <font SIZE="-1">SCALAR</font></dt>
<dd>  </dd>
<dt>study</dt>
<dd> <p> At this time, <code>&quot;study&quot;</code> does nothing. This may change in the future. </p>
<p> Prior to Perl version 5.16, it would create an inverted index of all characters that occurred in the given <font SIZE="-1">SCALAR</font> (or <code>$_</code> if unspecified). When matching a pattern, the rarest character from the pattern would be looked up in this index. Rarity was based on some static frequency tables constructed from some C programs and English text. </p>
 </dd>
<dt>sub <font SIZE="-1">NAME BLOCK</font></dt>
<dd>  </dd>
<dt>sub <font SIZE="-1">NAME</font> (<font SIZE="-1">PROTO</font>) <font SIZE="-1">BLOCK</font></dt>
<dd>  </dd>
<dt>sub <font SIZE="-1">NAME : ATTRS BLOCK</font></dt>
<dd>  </dd>
<dt>sub <font SIZE="-1">NAME</font> (<font SIZE="-1">PROTO</font>) : <font SIZE="-1">ATTRS BLOCK</font></dt>
<dd> <p> This is subroutine definition, not a real function <i>per se</i>. Without a <font SIZE="-1">BLOCK</font> it&#8217;s just a forward declaration. Without a <font SIZE="-1">NAME,</font> it&#8217;s an anonymous function declaration, so does return a value: the <font SIZE="-1">CODE</font> ref of the closure just created. </p>
<p> See perlsub and perlref for details about subroutines and references; see attributes and Attribute::Handlers for more information about attributes. </p>
 </dd>
<dt>__SUB__</dt>
<dd> <p> A special token that returns a reference to the current subroutine, or <code>&quot;undef&quot;</code> outside of a subroutine. </p>
<p> The behaviour of <code>&quot;__SUB__&quot;</code> within a regex code block (such as <code>&quot;/(?{...})/&quot;</code>) is subject to change. </p>
<p> This token is only available under <code>&quot;use v5.16&quot;</code> or the <code>&quot;current_sub&quot;</code> feature. See feature. </p>
 </dd>
<dt>substr <font SIZE="-1">EXPR,OFFSET,LENGTH,REPLACEMENT</font></dt>
<dd>  </dd>
<dt>substr <font SIZE="-1">EXPR,OFFSET,LENGTH</font></dt>
<dd>  </dd>
<dt>substr <font SIZE="-1">EXPR,OFFSET</font></dt>
<dd> <p> Extracts a substring out of <font SIZE="-1">EXPR</font> and returns it. First character is at offset zero. If <font SIZE="-1">OFFSET</font> is negative, starts that far back from the end of the string. If <font SIZE="-1">LENGTH</font> is omitted, returns everything through the end of the string. If <font SIZE="-1">LENGTH</font> is negative, leaves that many characters off the end of the string. </p>
<pre><code>    my $s = &quot;The black cat climbed the green tree&quot;;
    my $color = substr $s, 4, 5; # black
    my $middle = substr $s, 4, -11; # black cat climbed the
    my $end = substr $s, 14; # climbed the green tree
    my $tail = substr $s, -4; # tree
    my $z = substr $s, -4, 2; # tr
</code></pre>
<p> You can use the <code>&quot;substr&quot;</code> function as an lvalue, in which case <font SIZE="-1">EXPR</font> must itself be an lvalue. If you assign something shorter than <font SIZE="-1">LENGTH,</font> the string will shrink, and if you assign something longer than <font SIZE="-1">LENGTH,</font> the string will grow to accommodate it. To keep the string the same length, you may need to pad or chop your value using <code>&quot;sprintf&quot;</code>. </p>
<p> If <font SIZE="-1">OFFSET</font> and <font SIZE="-1">LENGTH</font> specify a substring that is partly outside the string, only the part within the string is returned. If the substring is beyond either end of the string, <code>&quot;substr&quot;</code> returns the undefined value and produces a warning. When used as an lvalue, specifying a substring that is entirely outside the string raises an exception. Here&#8217;s an example showing the behavior for boundary cases: </p>
<pre><code>    my $name = 'fred';
    substr($name, 4) = 'dy'; # $name is now 'freddy'
    my $null = substr $name, 6, 2; # returns &quot;&quot; (no warning)
    my $oops = substr $name, 7; # returns undef, with warning
    substr($name, 7) = 'gap'; # raises an exception
</code></pre>
<p> An alternative to using <code>&quot;substr&quot;</code> as an lvalue is to specify the replacement string as the 4th argument. This allows you to replace parts of the <font SIZE="-1">EXPR</font> and return what was there before in one operation, just as you can with <code>&quot;splice&quot;</code>. </p>
<pre><code>    my $s = &quot;The black cat climbed the green tree&quot;;
    my $z = substr $s, 14, 7, &quot;jumped from&quot;; # climbed
    # $s is now &quot;The black cat jumped from the green tree&quot;
</code></pre>
<p> Note that the lvalue returned by the three-argument version of <code>&quot;substr&quot;</code> acts as a &#8216;magic bullet&#8217;; each time it is assigned to, it remembers which part of the original string is being modified; for example: </p>
<pre><code>    my $x = '1234';
    for (substr($x,1,2)) {
        $_ = 'a'; print $x,&quot;\n&quot;; # prints 1a4
        $_ = 'xyz'; print $x,&quot;\n&quot;; # prints 1xyz4
        $x = '56789';
        $_ = 'pq'; print $x,&quot;\n&quot;; # prints 5pq9
    }
</code></pre>
<p> With negative offsets, it remembers its position from the end of the string when the target string is modified: </p>
<pre><code>    my $x = '1234';
    for (substr($x, -3, 2)) {
        $_ = 'a'; print $x,&quot;\n&quot;; # prints 1a4, as above
        $x = 'abcdefg';
        print $_,&quot;\n&quot;; # prints f
    }
</code></pre>
<p> Prior to Perl version 5.10, the result of using an lvalue multiple times was unspecified. Prior to 5.16, the result with negative offsets was unspecified. </p>
 </dd>
<dt>symlink <font SIZE="-1">OLDFILE,NEWFILE</font></dt>
<dd> <p> Creates a new filename symbolically linked to the old filename. Returns <code>1</code> for success, <code>0</code> otherwise. On systems that don&#8217;t support symbolic links, raises an exception. To check for that, use eval: </p>
<pre><code>    my $symlink_exists = eval { symlink(&quot;&quot;,&quot;&quot;); 1 };
</code></pre>
<p> Portability issues: ``symlink&#8217;&#8216; in perlport. </p>
 </dd>
<dt>syscall <font SIZE="-1">NUMBER, LIST</font></dt>
<dd> <p> Calls the system call specified as the first element of the list, passing the remaining elements as arguments to the system call. If unimplemented, raises an exception. The arguments are interpreted as follows: if a given argument is numeric, the argument is passed as an int. If not, the pointer to the string value is passed. You are responsible to make sure a string is pre-extended long enough to receive any result that might be written into a string. You can&#8217;t use a string literal (or other read-only string) as an argument to <code>&quot;syscall&quot;</code> because Perl has to assume that any string pointer might be written through. If your integer arguments are not literals and have never been interpreted in a numeric context, you may need to add <code>0</code> to them to force them to look like numbers. This emulates the <code>&quot;syswrite&quot;</code> function (or vice versa): </p>
<pre><code>    require 'syscall.ph'; # may need to run h2ph
    my $s = &quot;hi there\n&quot;;
    syscall(SYS_write(), fileno(STDOUT), $s, length $s);
</code></pre>
<p> Note that Perl supports passing of up to only 14 arguments to your syscall, which in practice should (usually) suffice. </p>
<p> Syscall returns whatever value returned by the system call it calls. If the system call fails, <code>&quot;syscall&quot;</code> returns <code>&quot;-1&quot;</code> and sets <code>$!</code> (errno). Note that some system calls <i>can</i> legitimately return <code>&quot;-1&quot;</code>. The proper way to handle such calls is to assign <code>&quot;$! = 0&quot;</code> before the call, then check the value of <code>$!</code> if <code>&quot;syscall&quot;</code> returns <code>&quot;-1&quot;</code>. </p>
<p> There&#8217;s a problem with <code>&quot;syscall(SYS_pipe())&quot;</code>: it returns the file number of the read end of the pipe it creates, but there is no way to retrieve the file number of the other end. You can avoid this problem by using <code>&quot;pipe&quot;</code> instead. </p>
<p> Portability issues: ``syscall&#8217;&#8216; in perlport. </p>
 </dd>
<dt>sysopen <font SIZE="-1">FILEHANDLE,FILENAME,MODE</font></dt>
<dd>  </dd>
<dt>sysopen <font SIZE="-1">FILEHANDLE,FILENAME,MODE,PERMS</font></dt>
<dd> <p> Opens the file whose filename is given by <font SIZE="-1">FILENAME,</font> and associates it with <font SIZE="-1">FILEHANDLE.</font> If <font SIZE="-1">FILEHANDLE</font> is an expression, its value is used as the real filehandle wanted; an undefined scalar will be suitably autovivified. This function calls the underlying operating system&#8217;s <code><a href="/docs/linux/man/2-open/">open</a></code>(2) function with the parameters <font SIZE="-1">FILENAME, MODE,</font> and <font SIZE="-1">PERMS.</font> </p>
<p> Returns true on success and <code>&quot;undef&quot;</code> otherwise. </p>
<p> The possible values and flag bits of the <font SIZE="-1">MODE</font> parameter are system-dependent; they are available via the standard module <code>&quot;Fcntl&quot;</code>. See the documentation of your operating system&#8217;s <code><a href="/docs/linux/man/2-open/">open</a></code>(2) syscall to see which values and flag bits are available. You may combine several flags using the <code>&quot;|&quot;</code>-operator. </p>
<p> Some of the most common values are <code>&quot;O_RDONLY&quot;</code> for opening the file in read-only mode, <code>&quot;O_WRONLY&quot;</code> for opening the file in write-only mode, and <code>&quot;O_RDWR&quot;</code> for opening the file in read-write mode. </p>
<p> For historical reasons, some values work on almost every system supported by Perl: 0 means read-only, 1 means write-only, and 2 means read/write. We know that these values do <i>not</i> work under <font SIZE="-1">OS/390</font> and on the Macintosh; you probably don&#8217;t want to use them in new code. </p>
<p> If the file named by <font SIZE="-1">FILENAME</font> does not exist and the <code>&quot;open&quot;</code> call creates it (typically because <font SIZE="-1">MODE</font> includes the <code>&quot;O_CREAT&quot;</code> flag), then the value of <font SIZE="-1">PERMS</font> specifies the permissions of the newly created file. If you omit the <font SIZE="-1">PERMS</font> argument to <code>&quot;sysopen&quot;</code>, Perl uses the octal value <code>0666</code>. These permission values need to be in octal, and are modified by your process&#8217;s current <code>&quot;umask&quot;</code>. </p>
<p> In many systems the <code>&quot;O_EXCL&quot;</code> flag is available for opening files in exclusive mode. This is <code>not</code> locking: exclusiveness means here that if the file already exists, <code>&quot;sysopen&quot;</code> fails. <code>&quot;O_EXCL&quot;</code> may not work on network filesystems, and has no effect unless the <code>&quot;O_CREAT&quot;</code> flag is set as well. Setting <code>&quot;O_CREAT|O_EXCL&quot;</code> prevents the file from being opened if it is a symbolic link. It does not protect against symbolic links in the file&#8217;s path. </p>
<p> Sometimes you may want to truncate an already-existing file. This can be done using the <code>&quot;O_TRUNC&quot;</code> flag. The behavior of <code>&quot;O_TRUNC&quot;</code> with <code>&quot;O_RDONLY&quot;</code> is undefined. </p>
<p> You should seldom if ever use <code>0644</code> as argument to <code>&quot;sysopen&quot;</code>, because that takes away the user&#8217;s option to have a more permissive umask. Better to omit it. See <code>&quot;umask&quot;</code> for more on this. </p>
<p> Note that under Perls older than 5.8.0, <code>&quot;sysopen&quot;</code> depends on the <code><a href="/docs/linux/man/3-fdopen/">fdopen</a></code>(3) C library function. On many Unix systems, <code><a href="/docs/linux/man/3-fdopen/">fdopen</a></code>(3) is known to fail when file descriptors exceed a certain value, typically 255. If you need more file descriptors than that, consider using the <code>&quot;POSIX::open&quot;</code> function. For Perls 5.8.0 and later, PerlIO is (most often) the default. </p>
<p> See perlopentut for a kinder, gentler explanation of opening files. </p>
<p> Portability issues: ``sysopen&#8217;&#8216; in perlport. </p>
 </dd>
<dt>sysread <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH,OFFSET</font></dt>
<dd>  </dd>
<dt>sysread <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH</font></dt>
<dd> <p> Attempts to read <font SIZE="-1">LENGTH</font> bytes of data into variable <font SIZE="-1">SCALAR</font> from the specified <font SIZE="-1">FILEHANDLE,</font> using <code><a href="/docs/linux/man/2-read/">read</a></code>(2). It bypasses buffered <font SIZE="-1">IO,</font> so mixing this with other kinds of reads, <code>&quot;print&quot;</code>, <code>&quot;write&quot;</code>, <code>&quot;seek&quot;</code>, <code>&quot;tell&quot;</code>, or <code>&quot;eof&quot;</code> can cause confusion because the perlio or stdio layers usually buffer data. Returns the number of bytes actually read, <code>0</code> at end of file, or undef if there was an error (in the latter case <code>$!</code> is also set). <font SIZE="-1">SCALAR</font> will be grown or shrunk so that the last byte actually read is the last byte of the scalar after the read. </p>
<p> An <font SIZE="-1">OFFSET</font> may be specified to place the read data at some place in the string other than the beginning. A negative <font SIZE="-1">OFFSET</font> specifies placement at that many characters counting backwards from the end of the string. A positive <font SIZE="-1">OFFSET</font> greater than the length of <font SIZE="-1">SCALAR</font> results in the string being padded to the required size with <code>&quot;\0&quot;</code> bytes before the result of the read is appended. </p>
<p> There is no <code>syseof()</code> function, which is ok, since <code>&quot;eof&quot;</code> doesn&#8217;t work well on device files (like ttys) anyway. Use <code>&quot;sysread&quot;</code> and check for a return value of 0 to decide whether you&#8217;re done. </p>
<p> Note that if the filehandle has been marked as <code>&quot;:utf8&quot;</code>, <code>&quot;sysread&quot;</code> will throw an exception. The <code>&quot;:encoding(...)&quot;</code> layer implicitly introduces the <code>&quot;:utf8&quot;</code> layer. See <code>&quot;binmode&quot;</code>, <code>&quot;open&quot;</code>, and the open pragma. </p>
 </dd>
<dt>sysseek <font SIZE="-1">FILEHANDLE,POSITION,WHENCE</font></dt>
<dd> <p> Sets <font SIZE="-1">FILEHANDLE</font>&#8216;s system position <i>in bytes</i> using <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2). <font SIZE="-1">FILEHANDLE</font> may be an expression whose value gives the name of the filehandle. The values for <font SIZE="-1">WHENCE</font> are <code>0</code> to set the new position to <font SIZE="-1">POSITION</font>; <code>1</code> to set it to the current position plus <font SIZE="-1">POSITION</font>; and <code>2</code> to set it to <font SIZE="-1">EOF</font> plus <font SIZE="-1">POSITION,</font> typically negative. </p>
<p> Note the emphasis on bytes: even if the filehandle has been set to operate on characters (for example using the <code>&quot;:encoding(UTF-8)&quot;</code> I/O layer), the <code>&quot;seek&quot;</code>, <code>&quot;tell&quot;</code>, and <code>&quot;sysseek&quot;</code> family of functions use byte offsets, not character offsets, because seeking to a character offset would be very slow in a <font SIZE="-1">UTF-8</font> file. </p>
<p> <code>&quot;sysseek&quot;</code> bypasses normal buffered <font SIZE="-1">IO,</font> so mixing it with reads other than <code>&quot;sysread&quot;</code> (for example <code>&quot;readline&quot;</code> or <code>&quot;read&quot;</code>), <code>&quot;print&quot;</code>, <code>&quot;write&quot;</code>, <code>&quot;seek&quot;</code>, <code>&quot;tell&quot;</code>, or <code>&quot;eof&quot;</code> may cause confusion. </p>
<p> For <font SIZE="-1">WHENCE,</font> you may also use the constants <code>&quot;SEEK_SET&quot;</code>, <code>&quot;SEEK_CUR&quot;</code>, and <code>&quot;SEEK_END&quot;</code> (start of the file, current position, end of the file) from the Fcntl module. Use of the constants is also more portable than relying on 0, 1, and 2. For example to define a ``systell&#8217;&#8216; function: </p>
<pre><code>    use Fcntl 'SEEK_CUR';
    sub systell { sysseek($_[0], 0, SEEK_CUR) }
</code></pre>
<p> Returns the new position, or the undefined value on failure. A position of zero is returned as the string <code>&quot;0 but true&quot;</code>; thus <code>&quot;sysseek&quot;</code> returns true on success and false on failure, yet you can still easily determine the new position. </p>
 </dd>
<dt>system <font SIZE="-1">LIST</font></dt>
<dd>  </dd>
<dt>system <font SIZE="-1">PROGRAM LIST</font></dt>
<dd> <p> Does exactly the same thing as <code>&quot;exec&quot;</code>, except that a fork is done first and the parent process waits for the child process to exit. Note that argument processing varies depending on the number of arguments. If there is more than one argument in <font SIZE="-1">LIST,</font> or if <font SIZE="-1">LIST</font> is an array with more than one value, starts the program given by the first element of the list with arguments given by the rest of the list. If there is only one scalar argument, the argument is checked for shell metacharacters, and if there are any, the entire argument is passed to the system&#8217;s command shell for parsing (this is <code>&quot;/bin/sh -c&quot;</code> on Unix platforms, but varies on other platforms). If there are no shell metacharacters in the argument, it is split into words and passed directly to <code>&quot;execvp&quot;</code>, which is more efficient. On Windows, only the <code>&quot;system PROGRAM LIST&quot;</code> syntax will reliably avoid using the shell; <code>&quot;system LIST&quot;</code>, even with more than one element, will fall back to the shell if the first spawn fails. </p>
<p> Perl will attempt to flush all files opened for output before any operation that may do a fork, but this may not be supported on some platforms (see perlport). To be safe, you may need to set <code>$|</code> (<code>$AUTOFLUSH</code> in English) or call the <code>&quot;autoflush&quot;</code> method of <code>&quot;IO::Handle&quot;</code> on any open handles. </p>
<p> The return value is the exit status of the program as returned by the <code>&quot;wait&quot;</code> call. To get the actual exit value, shift right by eight (see below). See also <code>&quot;exec&quot;</code>. This is <i>not</i> what you want to use to capture the output from a command; for that you should use merely backticks or <code>&quot;qx//&quot;</code>, as described in ```STRING`&#8216;&#8216; in perlop. Return value of -1 indicates a failure to start the program or an error of the <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) system call (inspect <code>$!</code> for the reason). </p>
<p> If you&#8217;d like to make <code>&quot;system&quot;</code> (and many other bits of Perl) die on error, have a look at the autodie pragma. </p>
<p> Like <code>&quot;exec&quot;</code>, <code>&quot;system&quot;</code> allows you to lie to a program about its name if you use the <code>&quot;system PROGRAM LIST&quot;</code> syntax. Again, see <code>&quot;exec&quot;</code>. </p>
<p> Since <code>&quot;SIGINT&quot;</code> and <code>&quot;SIGQUIT&quot;</code> are ignored during the execution of <code>&quot;system&quot;</code>, if you expect your program to terminate on receipt of these signals you will need to arrange to do so yourself based on the return value. </p>
<pre><code>    my @args = (&quot;command&quot;, &quot;arg1&quot;, &quot;arg2&quot;);
    system(@args) == 0
        or die &quot;system @args failed: $?&quot;;
</code></pre>
<p> If you&#8217;d like to manually inspect <code>&quot;system&quot;</code>&#8216;s failure, you can check all possible failure modes by inspecting <code>$?</code> like this: </p>
<pre><code>    if ($? == -1) {
        print &quot;failed to execute: $!\n&quot;;
    }
    elsif ($? &amp; 127) {
        printf &quot;child died with signal %d, %s coredump\n&quot;,
            ($? &amp; 127), ($? &amp; 128) ? 'with' : 'without';
    }
    else {
        printf &quot;child exited with value %d\n&quot;, $? &gt;&gt; 8;
    }
</code></pre>
<p> Alternatively, you may inspect the value of <code>&quot;${^CHILD_ERROR_NATIVE}&quot;</code> with the <code>&quot;W*()&quot;</code> calls from the <font SIZE="-1">POSIX</font> module. </p>
<p> When <code>&quot;system&quot;</code>&#8216;s arguments are executed indirectly by the shell, results and return codes are subject to its quirks. See ```STRING`&#8216;&#8216; in perlop and <code>&quot;exec&quot;</code> for details. </p>
<p> Since <code>&quot;system&quot;</code> does a <code>&quot;fork&quot;</code> and <code>&quot;wait&quot;</code> it may affect a <code>&quot;SIGCHLD&quot;</code> handler. See perlipc for details. </p>
<p> Portability issues: ``system&#8217;&#8216; in perlport. </p>
 </dd>
<dt>syswrite <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH,OFFSET</font></dt>
<dd>  </dd>
<dt>syswrite <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH</font></dt>
<dd>  </dd>
<dt>syswrite <font SIZE="-1">FILEHANDLE,SCALAR</font></dt>
<dd> <p> Attempts to write <font SIZE="-1">LENGTH</font> bytes of data from variable <font SIZE="-1">SCALAR</font> to the specified <font SIZE="-1">FILEHANDLE,</font> using <code><a href="/docs/linux/man/2-write/">write</a></code>(2). If <font SIZE="-1">LENGTH</font> is not specified, writes whole <font SIZE="-1">SCALAR.</font> It bypasses buffered <font SIZE="-1">IO,</font> so mixing this with reads (other than <code>&quot;sysread)&quot;</code>), <code>&quot;print&quot;</code>, <code>&quot;write&quot;</code>, <code>&quot;seek&quot;</code>, <code>&quot;tell&quot;</code>, or <code>&quot;eof&quot;</code> may cause confusion because the perlio and stdio layers usually buffer data. Returns the number of bytes actually written, or <code>&quot;undef&quot;</code> if there was an error (in this case the errno variable <code>$!</code> is also set). If the <font SIZE="-1">LENGTH</font> is greater than the data available in the <font SIZE="-1">SCALAR</font> after the <font SIZE="-1">OFFSET,</font> only as much data as is available will be written. </p>
<p> An <font SIZE="-1">OFFSET</font> may be specified to write the data from some part of the string other than the beginning. A negative <font SIZE="-1">OFFSET</font> specifies writing that many characters counting backwards from the end of the string. If <font SIZE="-1">SCALAR</font> is of length zero, you can only use an <font SIZE="-1">OFFSET</font> of 0. </p>
<p> <font SIZE="-1"><code>WARNING</code></font>: If the filehandle is marked <code>&quot;:utf8&quot;</code>, <code>&quot;syswrite&quot;</code> will raise an exception. The <code>&quot;:encoding(...)&quot;</code> layer implicitly introduces the <code>&quot;:utf8&quot;</code> layer. Alternately, if the handle is not marked with an encoding but you attempt to write characters with code points over 255, raises an exception. See <code>&quot;binmode&quot;</code>, <code>&quot;open&quot;</code>, and the open pragma. </p>
 </dd>
<dt>tell <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>tell</dt>
<dd> <p> Returns the current position <i>in bytes</i> for <font SIZE="-1">FILEHANDLE,</font> or -1 on error. <font SIZE="-1">FILEHANDLE</font> may be an expression whose value gives the name of the actual filehandle. If <font SIZE="-1">FILEHANDLE</font> is omitted, assumes the file last read. </p>
<p> Note the emphasis on bytes: even if the filehandle has been set to operate on characters (for example using the <code>&quot;:encoding(UTF-8)&quot;</code> I/O layer), the <code>&quot;seek&quot;</code>, <code>&quot;tell&quot;</code>, and <code>&quot;sysseek&quot;</code> family of functions use byte offsets, not character offsets, because seeking to a character offset would be very slow in a <font SIZE="-1">UTF-8</font> file. </p>
<p> The return value of <code>&quot;tell&quot;</code> for the standard streams like the <font SIZE="-1">STDIN</font> depends on the operating system: it may return -1 or something else. <code>&quot;tell&quot;</code> on pipes, fifos, and sockets usually returns -1. </p>
<p> There is no <code>&quot;systell&quot;</code> function. Use <code>&quot;sysseek($fh, 0, 1)&quot;</code> for that. </p>
<p> Do not use <code>&quot;tell&quot;</code> (or other buffered I/O operations) on a filehandle that has been manipulated by <code>&quot;sysread&quot;</code>, <code>&quot;syswrite&quot;</code>, or <code>&quot;sysseek&quot;</code>. Those functions ignore the buffering, while <code>&quot;tell&quot;</code> does not. </p>
 </dd>
<dt>telldir <font SIZE="-1">DIRHANDLE</font></dt>
<dd> <p> Returns the current position of the <code>&quot;readdir&quot;</code> routines on <font SIZE="-1">DIRHANDLE.</font> Value may be given to <code>&quot;seekdir&quot;</code> to access a particular location in a directory. <code>&quot;telldir&quot;</code> has the same caveats about possible directory compaction as the corresponding system library routine. </p>
 </dd>
<dt>tie <font SIZE="-1">VARIABLE,CLASSNAME,LIST</font></dt>
<dd> <p> This function binds a variable to a package class that will provide the implementation for the variable. <font SIZE="-1">VARIABLE</font> is the name of the variable to be enchanted. <font SIZE="-1">CLASSNAME</font> is the name of a class implementing objects of correct type. Any additional arguments are passed to the appropriate constructor method of the class (meaning <code>&quot;TIESCALAR&quot;</code>, <code>&quot;TIEHANDLE&quot;</code>, <code>&quot;TIEARRAY&quot;</code>, or <code>&quot;TIEHASH&quot;</code>). Typically these are arguments such as might be passed to the <code>dbm_open</code>(3) function of C. The object returned by the constructor is also returned by the <code>&quot;tie&quot;</code> function, which would be useful if you want to access other methods in <font SIZE="-1">CLASSNAME.</font> </p>
<p> Note that functions such as <code>&quot;keys&quot;</code> and <code>&quot;values&quot;</code> may return huge lists when used on large objects, like <font SIZE="-1">DBM</font> files. You may prefer to use the <code>&quot;each&quot;</code> function to iterate over such. Example: </p>
<pre><code>    # print out history file offsets
    use NDBM_File;
    tie(my %HIST, 'NDBM_File', '/usr/lib/news/history', 1, 0);
    while (my ($key,$val) = each %HIST) {
        print $key, ' = ', unpack('L', $val), &quot;\n&quot;;
    }
</code></pre>
<p> A class implementing a hash should have the following methods: </p>
<pre><code>    TIEHASH classname, LIST
    FETCH this, key
    STORE this, key, value
    DELETE this, key
    CLEAR this
    EXISTS this, key
    FIRSTKEY this
    NEXTKEY this, lastkey
    SCALAR this
    DESTROY this
    UNTIE this
</code></pre>
<p> A class implementing an ordinary array should have the following methods: </p>
<pre><code>    TIEARRAY classname, LIST
    FETCH this, key
    STORE this, key, value
    FETCHSIZE this
    STORESIZE this, count
    CLEAR this
    PUSH this, LIST
    POP this
    SHIFT this
    UNSHIFT this, LIST
    SPLICE this, offset, length, LIST
    EXTEND this, count
    DELETE this, key
    EXISTS this, key
    DESTROY this
    UNTIE this
</code></pre>
<p> A class implementing a filehandle should have the following methods: </p>
<pre><code>    TIEHANDLE classname, LIST
    READ this, scalar, length, offset
    READLINE this
    GETC this
    WRITE this, scalar, length, offset
    PRINT this, LIST
    PRINTF this, format, LIST
    BINMODE this
    EOF this
    FILENO this
    SEEK this, position, whence
    TELL this
    OPEN this, mode, LIST
    CLOSE this
    DESTROY this
    UNTIE this
</code></pre>
<p> A class implementing a scalar should have the following methods: </p>
<pre><code>    TIESCALAR classname, LIST
    FETCH this,
    STORE this, value
    DESTROY this
    UNTIE this
</code></pre>
<p> Not all methods indicated above need be implemented. See perltie, Tie::Hash, Tie::Array, Tie::Scalar, and Tie::Handle. </p>
<p> Unlike <code>&quot;dbmopen&quot;</code>, the <code>&quot;tie&quot;</code> function will not <code>&quot;use&quot;</code> or <code>&quot;require&quot;</code> a module for you; you need to do that explicitly yourself. See DB_File or the Config module for interesting <code>&quot;tie&quot;</code> implementations. </p>
<p> For further details see perltie, <code>&quot;tied&quot;</code>. </p>
 </dd>
<dt>tied <font SIZE="-1">VARIABLE</font></dt>
<dd> <p> Returns a reference to the object underlying <font SIZE="-1">VARIABLE</font> (the same value that was originally returned by the <code>&quot;tie&quot;</code> call that bound the variable to a package.) Returns the undefined value if <font SIZE="-1">VARIABLE</font> isn&#8217;t tied to a package. </p>
 </dd>
<dt>time</dt>
<dd> <p> Returns the number of non-leap seconds since whatever time the system considers to be the epoch, suitable for feeding to <code>&quot;gmtime&quot;</code> and <code>&quot;localtime&quot;</code>. On most systems the epoch is 00:00:00 <font SIZE="-1">UTC,</font> January 1, 1970; a prominent exception being Mac <font SIZE="-1">OS</font> Classic which uses 00:00:00, January 1, 1904 in the current local time zone for its epoch. </p>
<p> For measuring time in better granularity than one second, use the Time::HiRes module from Perl 5.8 onwards (or from <font SIZE="-1">CPAN</font> before then), or, if you have <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), you may be able to use the <code>&quot;syscall&quot;</code> interface of Perl. See perlfaq8 for details. </p>
<p> For date and time processing look at the many related modules on <font SIZE="-1">CPAN.</font> For a comprehensive date and time representation look at the DateTime module. </p>
 </dd>
<dt>times</dt>
<dd> <p> Returns a four-element list giving the user and system times in seconds for this process and any exited children of this process. </p>
<pre><code>    my ($user,$system,$cuser,$csystem) = times;
</code></pre>
<p> In scalar context, <code>&quot;times&quot;</code> returns <code>$user</code>. </p>
<p> Children&#8217;s times are only included for terminated children. </p>
<p> Portability issues: ``times&#8217;&#8216; in perlport. </p>
 </dd>
<dt>tr///</dt>
<dd> <p> The transliteration operator. Same as <code>&quot;y///&quot;</code>. See ``Quote-Like Operators&#8217;&#8216; in perlop. </p>
 </dd>
<dt>truncate <font SIZE="-1">FILEHANDLE,LENGTH</font></dt>
<dd>  </dd>
<dt>truncate <font SIZE="-1">EXPR,LENGTH</font></dt>
<dd> <p> Truncates the file opened on <font SIZE="-1">FILEHANDLE,</font> or named by <font SIZE="-1">EXPR,</font> to the specified length. Raises an exception if truncate isn&#8217;t implemented on your system. Returns true if successful, <code>&quot;undef&quot;</code> on error. </p>
<p> The behavior is undefined if <font SIZE="-1">LENGTH</font> is greater than the length of the file. </p>
<p> The position in the file of <font SIZE="-1">FILEHANDLE</font> is left unchanged. You may want to call seek before writing to the file. </p>
<p> Portability issues: ``truncate&#8217;&#8216; in perlport. </p>
 </dd>
<dt>uc <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>uc</dt>
<dd> <p> Returns an uppercased version of <font SIZE="-1">EXPR.</font> This is the internal function implementing the <code>&quot;\U&quot;</code> escape in double-quoted strings. It does not attempt to do titlecase mapping on initial letters. See <code>&quot;ucfirst&quot;</code> for that. </p>
<p> If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. </p>
<p> This function behaves the same way under various pragmas, such as in a locale, as <code>&quot;lc&quot;</code> does. </p>
 </dd>
<dt>ucfirst <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>ucfirst</dt>
<dd> <p> Returns the value of <font SIZE="-1">EXPR</font> with the first character in uppercase (titlecase in Unicode). This is the internal function implementing the <code>&quot;\u&quot;</code> escape in double-quoted strings. </p>
<p> If <font SIZE="-1">EXPR</font> is omitted, uses <code>$_</code>. </p>
<p> This function behaves the same way under various pragmas, such as in a locale, as <code>&quot;lc&quot;</code> does. </p>
 </dd>
<dt>umask <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>umask</dt>
<dd> <p> Sets the umask for the process to <font SIZE="-1">EXPR</font> and returns the previous value. If <font SIZE="-1">EXPR</font> is omitted, merely returns the current umask. </p>
<p> The Unix permission <code>&quot;rwxr-x---&quot;</code> is represented as three sets of three bits, or three octal digits: <code>0750</code> (the leading 0 indicates octal and isn&#8217;t one of the digits). The <code>&quot;umask&quot;</code> value is such a number representing disabled permissions bits. The permission (or ``mode&#8217;&#8216;) values you pass <code>&quot;mkdir&quot;</code> or <code>&quot;sysopen&quot;</code> are modified by your umask, so even if you tell <code>&quot;sysopen&quot;</code> to create a file with permissions <code>0777</code>, if your umask is <code>0022</code>, then the file will actually be created with permissions <code>0755</code>. If your <code>&quot;umask&quot;</code> were <code>0027</code> (group can&#8217;t write; others can&#8217;t read, write, or execute), then passing <code>&quot;sysopen&quot;</code> <code>0666</code> would create a file with mode <code>0640</code> (because <code>&quot;0666 &amp;~ 027&quot;</code> is <code>0640</code>). </p>
<p> Here&#8217;s some advice: supply a creation mode of <code>0666</code> for regular files (in <code>&quot;sysopen&quot;</code>) and one of <code>0777</code> for directories (in <code>&quot;mkdir&quot;</code>) and executable files. This gives users the freedom of choice: if they want protected files, they might choose process umasks of <code>022</code>, <code>027</code>, or even the particularly antisocial mask of <code>077</code>. Programs should rarely if ever make policy decisions better left to the user. The exception to this is when writing files that should be kept private: mail files, web browser cookies, <i>.rhosts</i> files, and so on. </p>
<p> If <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) is not implemented on your system and you are trying to restrict access for <i>yourself</i> (i.e., <code>&quot;(EXPR &amp; 0700) &gt; 0&quot;</code>), raises an exception. If <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) is not implemented and you are not trying to restrict access for yourself, returns <code>&quot;undef&quot;</code>. </p>
<p> Remember that a umask is a number, usually given in octal; it is <i>not</i> a string of octal digits. See also <code>&quot;oct&quot;</code>, if all you have is a string. </p>
<p> Portability issues: ``umask&#8217;&#8216; in perlport. </p>
 </dd>
<dt>undef <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>undef</dt>
<dd> <p> Undefines the value of <font SIZE="-1">EXPR,</font> which must be an lvalue. Use only on a scalar value, an array (using <code>&quot;@&quot;</code>), a hash (using <code>&quot;%&quot;</code>), a subroutine (using <code>&quot;&amp;&quot;</code>), or a typeglob (using <code>&quot;*&quot;</code>). Saying <code>&quot;undef $hash{$key}&quot;</code> will probably not do what you expect on most predefined variables or <font SIZE="-1">DBM</font> list values, so don&#8217;t do that; see <code>&quot;delete&quot;</code>. Always returns the undefined value. You can omit the <font SIZE="-1">EXPR,</font> in which case nothing is undefined, but you still get an undefined value that you could, for instance, return from a subroutine, assign to a variable, or pass as a parameter. Examples: </p>
<pre><code>    undef $foo;
    undef $bar{'blurfl'}; # Compare to: delete $bar{'blurfl'};
    undef @ary;
    undef %hash;
    undef &amp;mysub;
    undef *xyz; # destroys $xyz, @xyz, %xyz, &amp;xyz, etc.
    return (wantarray ? (undef, $errmsg) : undef) if $they_blew_it;
    select undef, undef, undef, 0.25;
    my ($x, $y, undef, $z) = foo(); # Ignore third value returned
</code></pre>
<p> Note that this is a unary operator, not a list operator. </p>
 </dd>
<dt>unlink <font SIZE="-1">LIST</font></dt>
<dd>  </dd>
<dt>unlink</dt>
<dd> <p> Deletes a list of files. On success, it returns the number of files it successfully deleted. On failure, it returns false and sets <code>$!</code> (errno): </p>
<pre><code>    my $unlinked = unlink 'a', 'b', 'c';
    unlink @goners;
    unlink glob &quot;*.bak&quot;;
</code></pre>
<p> On error, <code>&quot;unlink&quot;</code> will not tell you which files it could not remove. If you want to know which files you could not remove, try them one at a time: </p>
<pre><code>     foreach my $file ( @goners ) {
         unlink $file or warn &quot;Could not unlink $file: $!&quot;;
     }
</code></pre>
<p> Note: <code>&quot;unlink&quot;</code> will not attempt to delete directories unless you are superuser and the <code>-U</code> flag is supplied to Perl. Even if these conditions are met, be warned that unlinking a directory can inflict damage on your filesystem. Finally, using <code>&quot;unlink&quot;</code> on directories is not supported on many operating systems. Use <code>&quot;rmdir&quot;</code> instead. </p>
<p> If <font SIZE="-1">LIST</font> is omitted, <code>&quot;unlink&quot;</code> uses <code>$_</code>. </p>
 </dd>
<dt>unpack <font SIZE="-1">TEMPLATE,EXPR</font></dt>
<dd>  </dd>
<dt>unpack <font SIZE="-1">TEMPLATE</font></dt>
<dd> <p> <code>&quot;unpack&quot;</code> does the reverse of <code>&quot;pack&quot;</code>: it takes a string and expands it out into a list of values. (In scalar context, it returns merely the first value produced.) </p>
<p> If <font SIZE="-1">EXPR</font> is omitted, unpacks the <code>$_</code> string. See perlpacktut for an introduction to this function. </p>
<p> The string is broken into chunks described by the <font SIZE="-1">TEMPLATE.</font> Each chunk is converted separately to a value. Typically, either the string is a result of <code>&quot;pack&quot;</code>, or the characters of the string represent a C structure of some kind. </p>
<p> The <font SIZE="-1">TEMPLATE</font> has the same format as in the <code>&quot;pack&quot;</code> function. Here&#8217;s a subroutine that does substring: </p>
<pre><code>    sub substr {
        my ($what, $where, $howmuch) = @_;
        unpack(&quot;x$where a$howmuch&quot;, $what);
    }
</code></pre>
<p> and then there&#8217;s </p>
<pre><code>    sub ordinal { unpack(&quot;W&quot;,$_[0]); } # same as ord()
</code></pre>
<p> In addition to fields allowed in <code>&quot;pack&quot;</code>, you may prefix a field with a %&lt;number&gt; to indicate that you want a &lt;number&gt;-bit checksum of the items instead of the items themselves. Default is a 16-bit checksum. The checksum is calculated by summing numeric values of expanded values (for string fields the sum of <code>&quot;ord($char)&quot;</code> is taken; for bit fields the sum of zeroes and ones). </p>
<p> For example, the following computes the same number as the System V sum program: </p>
<pre><code>    my $checksum = do {
        local $/; # slurp!
        unpack(&quot;%32W*&quot;, readline) % 65535;
    };
</code></pre>
<p> The following efficiently counts the number of set bits in a bit vector: </p>
<pre><code>    my $setbits = unpack(&quot;%32b*&quot;, $selectmask);
</code></pre>
<p> The <code>&quot;p&quot;</code> and <code>&quot;P&quot;</code> formats should be used with care. Since Perl has no way of checking whether the value passed to <code>&quot;unpack&quot;</code> corresponds to a valid memory location, passing a pointer value that&#8217;s not known to be valid is likely to have disastrous consequences. </p>
<p> If there are more pack codes or if the repeat count of a field or a group is larger than what the remainder of the input string allows, the result is not well defined: the repeat count may be decreased, or <code>&quot;unpack&quot;</code> may produce empty strings or zeros, or it may raise an exception. If the input string is longer than one described by the <font SIZE="-1">TEMPLATE,</font> the remainder of that input string is ignored. </p>
<p> See <code>&quot;pack&quot;</code> for more examples and notes. </p>
 </dd>
<dt>unshift <font SIZE="-1">ARRAY,LIST</font></dt>
<dd> <p> Does the opposite of a <code>&quot;shift&quot;</code>. Or the opposite of a <code>&quot;push&quot;</code>, depending on how you look at it. Prepends list to the front of the array and returns the new number of elements in the array. </p>
<pre><code>    unshift(@ARGV, '-e') unless $ARGV[0] =~ /^-/;
</code></pre>
<p> Note the <font SIZE="-1">LIST</font> is prepended whole, not one element at a time, so the prepended elements stay in the same order. Use <code>&quot;reverse&quot;</code> to do the reverse. </p>
<p> Starting with Perl 5.14, an experimental feature allowed <code>&quot;unshift&quot;</code> to take a scalar expression. This experiment has been deemed unsuccessful, and was removed as of Perl 5.24. </p>
 </dd>
<dt>untie <font SIZE="-1">VARIABLE</font></dt>
<dd> <p> Breaks the binding between a variable and a package. (See tie.) Has no effect if the variable is not tied. </p>
 </dd>
<dt>use Module <font SIZE="-1">VERSION LIST</font></dt>
<dd>  </dd>
<dt>use Module <font SIZE="-1">VERSION</font></dt>
<dd>  </dd>
<dt>use Module <font SIZE="-1">LIST</font></dt>
<dd>  </dd>
<dt>use Module</dt>
<dd>  </dd>
<dt>use <font SIZE="-1">VERSION</font></dt>
<dd> <p> Imports some semantics into the current package from the named module, generally by aliasing certain subroutine or variable names into your package. It is exactly equivalent to </p>
<pre><code>    BEGIN { require Module; Module-&gt;import( LIST ); }
</code></pre>
<p> except that Module <i>must</i> be a bareword. The importation can be made conditional by using the if module. </p>
<p> In the <code>&quot;use VERSION&quot;</code> form, <font SIZE="-1">VERSION</font> may be either a v-string such as v5.24.1, which will be compared to <code>$^V</code> (aka <code>$PERL_VERSION</code>), or a numeric argument of the form 5.024001, which will be compared to <code>$]</code>. An exception is raised if <font SIZE="-1">VERSION</font> is greater than the version of the current Perl interpreter; Perl will not attempt to parse the rest of the file. Compare with <code>&quot;require&quot;</code>, which can do a similar check at run time. Symmetrically, <code>&quot;no VERSION&quot;</code> allows you to specify that you want a version of Perl older than the specified one. </p>
<p> Specifying <font SIZE="-1">VERSION</font> as a numeric argument of the form 5.024001 should generally be avoided as older less readable syntax compared to v5.24.1. Before perl 5.8.0 released in 2002 the more verbose numeric form was the only supported syntax, which is why you might see it in </p>
<pre><code>    use v5.24.1; # compile time version check
    use 5.24.1; # ditto
    use 5.024_001; # ditto; older syntax compatible with perl 5.6
</code></pre>
<p> This is often useful if you need to check the current Perl version before <code>&quot;use&quot;</code>ing library modules that won&#8217;t work with older versions of Perl. (We try not to do this more than we have to.) </p>
<p> <code>&quot;use VERSION&quot;</code> also lexically enables all features available in the requested version as defined by the feature pragma, disabling any features not in the requested version&#8217;s feature bundle. See feature. Similarly, if the specified Perl version is greater than or equal to 5.12.0, strictures are enabled lexically as with <code>&quot;use strict&quot;</code>. Any explicit use of <code>&quot;use strict&quot;</code> or <code>&quot;no strict&quot;</code> overrides <code>&quot;use VERSION&quot;</code>, even if it comes before it. Later use of <code>&quot;use VERSION&quot;</code> will override all behavior of a previous <code>&quot;use VERSION&quot;</code>, possibly removing the <code>&quot;strict&quot;</code> and <code>&quot;feature&quot;</code> added by <code>&quot;use VERSION&quot;</code>. <code>&quot;use VERSION&quot;</code> does not load the <i>feature.pm</i> or <i>strict.pm</i> files. </p>
<p> The <code>&quot;BEGIN&quot;</code> forces the <code>&quot;require&quot;</code> and <code>&quot;import&quot;</code> to happen at compile time. The <code>&quot;require&quot;</code> makes sure the module is loaded into memory if it hasn&#8217;t been yet. The <code>&quot;import&quot;</code> is not a builtin; it&#8217;s just an ordinary static method call into the <code>&quot;Module&quot;</code> package to tell the module to import the list of features back into the current package. The module can implement its <code>&quot;import&quot;</code> method any way it likes, though most modules just choose to derive their <code>&quot;import&quot;</code> method via inheritance from the <code>&quot;Exporter&quot;</code> class that is defined in the <code>&quot;Exporter&quot;</code> module. See Exporter. If no <code>&quot;import&quot;</code> method can be found, then the call is skipped, even if there is an <font SIZE="-1">AUTOLOAD</font> method. </p>
<p> If you do not want to call the package&#8217;s <code>&quot;import&quot;</code> method (for instance, to stop your namespace from being altered), explicitly supply the empty list: </p>
<pre><code>    use Module ();
</code></pre>
<p> That is exactly equivalent to </p>
<pre><code>    BEGIN { require Module }
</code></pre>
<p> If the <font SIZE="-1">VERSION</font> argument is present between Module and <font SIZE="-1">LIST,</font> then the <code>&quot;use&quot;</code> will call the <code>&quot;VERSION&quot;</code> method in class Module with the given version as an argument: </p>
<pre><code>    use Module 12.34;
</code></pre>
<p> is equivalent to: </p>
<pre><code>    BEGIN { require Module; Module-&gt;VERSION(12.34) }
</code></pre>
<p> The default <code>&quot;VERSION&quot;</code> method, inherited from the <code>&quot;UNIVERSAL&quot;</code> class, croaks if the given version is larger than the value of the variable <code>$Module::VERSION</code>. </p>
<p> The <font SIZE="-1">VERSION</font> argument cannot be an arbitrary expression. It only counts as a <font SIZE="-1">VERSION</font> argument if it is a version number literal, starting with either a digit or <code>&quot;v&quot;</code> followed by a digit. Anything that doesn&#8217;t look like a version literal will be parsed as the start of the <font SIZE="-1">LIST.</font> Nevertheless, many attempts to use an arbitrary expression as a <font SIZE="-1">VERSION</font> argument will appear to work, because Exporter&#8217;s <code>&quot;import&quot;</code> method handles numeric arguments specially, performing version checks rather than treating them as things to export. </p>
<p> Again, there is a distinction between omitting <font SIZE="-1">LIST</font> (<code>&quot;import&quot;</code> called with no arguments) and an explicit empty <font SIZE="-1">LIST</font> <code>&quot;()&quot;</code> (<code>&quot;import&quot;</code> not called). Note that there is no comma after <font SIZE="-1">VERSION</font>! </p>
<p> Because this is a wide-open interface, pragmas (compiler directives) are also implemented this way. Some of the currently implemented pragmas are: </p>
<pre><code>    use constant;
    use diagnostics;
    use integer;
    use sigtrap qw(SEGV BUS);
    use strict qw(subs vars refs);
    use subs qw(afunc blurfl);
    use warnings qw(all);
    use sort qw(stable);
</code></pre>
<p> Some of these pseudo-modules import semantics into the current block scope (like <code>&quot;strict&quot;</code> or <code>&quot;integer&quot;</code>, unlike ordinary modules, which import symbols into the current package (which are effective through the end of the file). </p>
<p> Because <code>&quot;use&quot;</code> takes effect at compile time, it doesn&#8217;t respect the ordinary flow control of the code being compiled. In particular, putting a <code>&quot;use&quot;</code> inside the false branch of a conditional doesn&#8217;t prevent it from being processed. If a module or pragma only needs to be loaded conditionally, this can be done using the if pragma: </p>
<pre><code>    use if $] &lt; 5.008, &quot;utf8&quot;;
    use if WANT_WARNINGS, warnings =&gt; qw(all);
</code></pre>
<p> There&#8217;s a corresponding <code>&quot;no&quot;</code> declaration that unimports meanings imported by <code>&quot;use&quot;</code>, i.e., it calls <code>&quot;Module-&gt;unimport(LIST)&quot;</code> instead of <code>&quot;import&quot;</code>. It behaves just as <code>&quot;import&quot;</code> does with <font SIZE="-1">VERSION,</font> an omitted or empty <font SIZE="-1">LIST,</font> or no unimport method being found. </p>
<pre><code>    no integer;
    no strict 'refs';
    no warnings;
</code></pre>
<p> Care should be taken when using the <code>&quot;no VERSION&quot;</code> form of <code>&quot;no&quot;</code>. It is <i>only</i> meant to be used to assert that the running Perl is of a earlier version than its argument and <i>not</i> to undo the feature-enabling side effects of <code>&quot;use VERSION&quot;</code>. </p>
<p> See perlmodlib for a list of standard modules and pragmas. See perlrun for the <code>&quot;-M&quot;</code> and <code>&quot;-m&quot;</code> command-line options to Perl that give <code>&quot;use&quot;</code> functionality from the command-line. </p>
 </dd>
<dt>utime <font SIZE="-1">LIST</font></dt>
<dd> <p> Changes the access and modification times on each file of a list of files. The first two elements of the list must be the <font SIZE="-1">NUMERIC</font> access and modification times, in that order. Returns the number of files successfully changed. The inode change time of each file is set to the current time. For example, this code has the same effect as the Unix <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) command when the files <i>already exist</i> and belong to the user running the program: </p>
<pre><code>    #!/usr/bin/perl
    my $atime = my $mtime = time;
    utime $atime, $mtime, @ARGV;
</code></pre>
<p> Since Perl 5.8.0, if the first two elements of the list are <code>&quot;undef&quot;</code>, the <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2) syscall from your C library is called with a null second argument. On most systems, this will set the file&#8217;s access and modification times to the current time (i.e., equivalent to the example above) and will work even on files you don&#8217;t own provided you have write permission: </p>
<pre><code>    for my $file (@ARGV) {
        utime(undef, undef, $file)
            || warn &quot;Couldn't touch $file: $!&quot;;
    }
</code></pre>
<p> Under <font SIZE="-1">NFS</font> this will use the time of the <font SIZE="-1">NFS</font> server, not the time of the local machine. If there is a time synchronization problem, the <font SIZE="-1">NFS</font> server and local machine will have different times. The Unix <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) command will in fact normally use this form instead of the one shown in the first example. </p>
<p> Passing only one of the first two elements as <code>&quot;undef&quot;</code> is equivalent to passing a 0 and will not have the effect described when both are <code>&quot;undef&quot;</code>. This also triggers an uninitialized warning. </p>
<p> On systems that support <code>futimes</code>(2), you may pass filehandles among the files. On systems that don&#8217;t support <code>futimes</code>(2), passing filehandles raises an exception. Filehandles must be passed as globs or glob references to be recognized; barewords are considered filenames. </p>
<p> Portability issues: ``utime&#8217;&#8216; in perlport. </p>
 </dd>
<dt>values <font SIZE="-1">HASH</font></dt>
<dd>  </dd>
<dt>values <font SIZE="-1">ARRAY</font></dt>
<dd> <p> In list context, returns a list consisting of all the values of the named hash. In Perl 5.12 or later only, will also return a list of the values of an array; prior to that release, attempting to use an array argument will produce a syntax error. In scalar context, returns the number of values. </p>
<p> Hash entries are returned in an apparently random order. The actual random order is specific to a given hash; the exact same series of operations on two hashes may result in a different order for each hash. Any insertion into the hash may change the order, as will any deletion, with the exception that the most recent key returned by <code>&quot;each&quot;</code> or <code>&quot;keys&quot;</code> may be deleted without changing the order. So long as a given hash is unmodified you may rely on <code>&quot;keys&quot;</code>, <code>&quot;values&quot;</code> and <code>&quot;each&quot;</code> to repeatedly return the same order as each other. See ``Algorithmic Complexity Attacks&#8217;&#8216; in perlsec for details on why hash order is randomized. Aside from the guarantees provided here the exact details of Perl&#8217;s hash algorithm and the hash traversal order are subject to change in any release of Perl. Tied hashes may behave differently to Perl&#8217;s hashes with respect to changes in order on insertion and deletion of items. </p>
<p> As a side effect, calling <code>&quot;values&quot;</code> resets the <font SIZE="-1">HASH</font> or <font SIZE="-1">ARRAY</font>&#8216;s internal iterator (see <code>&quot;each&quot;</code>) before yielding the values. In particular, calling <code>&quot;values&quot;</code> in void context resets the iterator with no other overhead. </p>
<p> Apart from resetting the iterator, <code>&quot;values @array&quot;</code> in list context is the same as plain <code>@array</code>. (We recommend that you use void context <code>&quot;keys @array&quot;</code> for this, but reasoned that taking <code>&quot;values @array&quot;</code> out would require more documentation than leaving it in.) </p>
<p> Note that the values are not copied, which means modifying them will modify the contents of the hash: </p>
<pre><code>    for (values %hash) { s/foo/bar/g } # modifies %hash values
    for (@hash{keys %hash}) { s/foo/bar/g } # same
</code></pre>
<p> Starting with Perl 5.14, an experimental feature allowed <code>&quot;values&quot;</code> to take a scalar expression. This experiment has been deemed unsuccessful, and was removed as of Perl 5.24. </p>
<p> To avoid confusing would-be users of your code who are running earlier versions of Perl with mysterious syntax errors, put this sort of thing at the top of your file to signal that your code will work <i>only</i> on Perls of a recent vintage: </p>
<pre><code>    use 5.012; # so keys/values/each work on arrays
</code></pre>
<p> See also <code>&quot;keys&quot;</code>, <code>&quot;each&quot;</code>, and <code>&quot;sort&quot;</code>. </p>
 </dd>
<dt>vec <font SIZE="-1">EXPR,OFFSET,BITS</font></dt>
<dd> <p> Treats the string in <font SIZE="-1">EXPR</font> as a bit vector made up of elements of width <font SIZE="-1">BITS</font> and returns the value of the element specified by <font SIZE="-1">OFFSET</font> as an unsigned integer. <font SIZE="-1">BITS</font> therefore specifies the number of bits that are reserved for each element in the bit vector. This must be a power of two from 1 to 32 (or 64, if your platform supports that). </p>
<p> If <font SIZE="-1">BITS</font> is 8, ``elements&#8217;&#8216; coincide with bytes of the input string. </p>
<p> If <font SIZE="-1">BITS</font> is 16 or more, bytes of the input string are grouped into chunks of size <font SIZE="-1">BITS/8,</font> and each group is converted to a number as with <code>&quot;pack&quot;</code>/<code>&quot;unpack&quot;</code> with big-endian formats <code>&quot;n&quot;</code>/<code>&quot;N&quot;</code> (and analogously for BITS==64). See <code>&quot;pack&quot;</code> for details. </p>
<p> If bits is 4 or less, the string is broken into bytes, then the bits of each byte are broken into 8/BITS groups. Bits of a byte are numbered in a little-endian-ish way, as in <code>0x01</code>, <code>0x02</code>, <code>0x04</code>, <code>0x08</code>, <code>0x10</code>, <code>0x20</code>, <code>0x40</code>, <code>0x80</code>. For example, breaking the single input byte <code>&quot;chr(0x36)&quot;</code> into two groups gives a list <code>&quot;(0x6, 0x3)&quot;</code>; breaking it into 4 groups gives <code>&quot;(0x2, 0x1, 0x3, 0x0)&quot;</code>. </p>
<p> <code>&quot;vec&quot;</code> may also be assigned to, in which case parentheses are needed to give the expression the correct precedence as in </p>
<pre><code>    vec($image, $max_x * $x + $y, 8) = 3;
</code></pre>
<p> If the selected element is outside the string, the value 0 is returned. If an element off the end of the string is written to, Perl will first extend the string with sufficiently many zero bytes. It is an error to try to write off the beginning of the string (i.e., negative <font SIZE="-1">OFFSET</font>). </p>
<p> If the string happens to be encoded as <font SIZE="-1">UTF-8</font> internally (and thus has the <font SIZE="-1">UTF8</font> flag set), <code>&quot;vec&quot;</code> tries to convert it to use a one-byte-per-character internal representation. However, if the string contains characters with values of 256 or higher, that conversion will fail, and a deprecation message will be raised. In that situation, <code>&quot;vec&quot;</code> will operate on the underlying buffer regardless, in its internal <font SIZE="-1">UTF-8</font> representation. In Perl 5.32, this will be a fatal error. </p>
<p> Strings created with <code>&quot;vec&quot;</code> can also be manipulated with the logical operators <code>&quot;|&quot;</code>, <code>&quot;&amp;&quot;</code>, <code>&quot;^&quot;</code>, and <code>&quot;~&quot;</code>. These operators will assume a bit vector operation is desired when both operands are strings. See ``Bitwise String Operators&#8217;&#8216; in perlop. </p>
<p> The following code will build up an <font SIZE="-1">ASCII</font> string saying <code>&#8216;PerlPerlPerl&#8217;</code>. The comments show the string after each step. Note that this code works in the same way on big-endian or little-endian machines. </p>
<pre><code>    my $foo = '';
    vec($foo, 0, 32) = 0x5065726C; # 'Perl'
    # $foo eq &quot;Perl&quot; eq &quot;\x50\x65\x72\x6C&quot;, 32 bits
    print vec($foo, 0, 8); # prints 80 == 0x50 == ord('P')
    vec($foo, 2, 16) = 0x5065; # 'PerlPe'
    vec($foo, 3, 16) = 0x726C; # 'PerlPerl'
    vec($foo, 8, 8) = 0x50; # 'PerlPerlP'
    vec($foo, 9, 8) = 0x65; # 'PerlPerlPe'
    vec($foo, 20, 4) = 2; # 'PerlPerlPe' . &quot;\x02&quot;
    vec($foo, 21, 4) = 7; # 'PerlPerlPer'
                                   # 'r' is &quot;\x72&quot;
    vec($foo, 45, 2) = 3; # 'PerlPerlPer' . &quot;\x0c&quot;
    vec($foo, 93, 1) = 1; # 'PerlPerlPer' . &quot;\x2c&quot;
    vec($foo, 94, 1) = 1; # 'PerlPerlPerl'
                                   # 'l' is &quot;\x6c&quot;
</code></pre>
<p> To transform a bit vector into a string or list of 0&#8217;s and 1&#8217;s, use these: </p>
<pre><code>    my $bits = unpack(&quot;b*&quot;, $vector);
    my @bits = split(//, unpack(&quot;b*&quot;, $vector));
</code></pre>
<p> If you know the exact length in bits, it can be used in place of the <code>&quot;*&quot;</code>. </p>
<p> Here is an example to illustrate how the bits actually fall in place: </p>
<pre><code>  #!/usr/bin/perl -wl
  print &lt;&lt;'EOT';
                                    0 1 2 3
                     unpack(&quot;V&quot;,$_) 01234567890123456789012345678901
  ------------------------------------------------------------------
  EOT
  for $w (0..3) {
      $width = 2**$w;
      for ($shift=0; $shift &lt; $width; ++$shift) {
          for ($off=0; $off &lt; 32/$width; ++$off) {
              $str = pack(&quot;B*&quot;, &quot;0&quot;x32);
              $bits = (1&lt;&lt;$shift);
              vec($str, $off, $width) = $bits;
              $res = unpack(&quot;b*&quot;,$str);
              $val = unpack(&quot;V&quot;, $str);
              write;
          }
      }
  }
  format STDOUT =
  vec($_,@#,@#) = @&lt;&lt; == @######### @&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;
  $off, $width, $bits, $val, $res
  .
  __END__
</code></pre>
<p> Regardless of the machine architecture on which it runs, the example above should print the following table: </p>
<pre><code>                                    0 1 2 3
                     unpack(&quot;V&quot;,$_) 01234567890123456789012345678901
  ------------------------------------------------------------------
  vec($_, 0, 1) = 1 == 1 10000000000000000000000000000000
  vec($_, 1, 1) = 1 == 2 01000000000000000000000000000000
  vec($_, 2, 1) = 1 == 4 00100000000000000000000000000000
  vec($_, 3, 1) = 1 == 8 00010000000000000000000000000000
  vec($_, 4, 1) = 1 == 16 00001000000000000000000000000000
  vec($_, 5, 1) = 1 == 32 00000100000000000000000000000000
  vec($_, 6, 1) = 1 == 64 00000010000000000000000000000000
  vec($_, 7, 1) = 1 == 128 00000001000000000000000000000000
  vec($_, 8, 1) = 1 == 256 00000000100000000000000000000000
  vec($_, 9, 1) = 1 == 512 00000000010000000000000000000000
  vec($_,10, 1) = 1 == 1024 00000000001000000000000000000000
  vec($_,11, 1) = 1 == 2048 00000000000100000000000000000000
  vec($_,12, 1) = 1 == 4096 00000000000010000000000000000000
  vec($_,13, 1) = 1 == 8192 00000000000001000000000000000000
  vec($_,14, 1) = 1 == 16384 00000000000000100000000000000000
  vec($_,15, 1) = 1 == 32768 00000000000000010000000000000000
  vec($_,16, 1) = 1 == 65536 00000000000000001000000000000000
  vec($_,17, 1) = 1 == 131072 00000000000000000100000000000000
  vec($_,18, 1) = 1 == 262144 00000000000000000010000000000000
  vec($_,19, 1) = 1 == 524288 00000000000000000001000000000000
  vec($_,20, 1) = 1 == 1048576 00000000000000000000100000000000
  vec($_,21, 1) = 1 == 2097152 00000000000000000000010000000000
  vec($_,22, 1) = 1 == 4194304 00000000000000000000001000000000
  vec($_,23, 1) = 1 == 8388608 00000000000000000000000100000000
  vec($_,24, 1) = 1 == 16777216 00000000000000000000000010000000
  vec($_,25, 1) = 1 == 33554432 00000000000000000000000001000000
  vec($_,26, 1) = 1 == 67108864 00000000000000000000000000100000
  vec($_,27, 1) = 1 == 134217728 00000000000000000000000000010000
  vec($_,28, 1) = 1 == 268435456 00000000000000000000000000001000
  vec($_,29, 1) = 1 == 536870912 00000000000000000000000000000100
  vec($_,30, 1) = 1 == 1073741824 00000000000000000000000000000010
  vec($_,31, 1) = 1 == 2147483648 00000000000000000000000000000001
  vec($_, 0, 2) = 1 == 1 10000000000000000000000000000000
  vec($_, 1, 2) = 1 == 4 00100000000000000000000000000000
  vec($_, 2, 2) = 1 == 16 00001000000000000000000000000000
  vec($_, 3, 2) = 1 == 64 00000010000000000000000000000000
  vec($_, 4, 2) = 1 == 256 00000000100000000000000000000000
  vec($_, 5, 2) = 1 == 1024 00000000001000000000000000000000
  vec($_, 6, 2) = 1 == 4096 00000000000010000000000000000000
  vec($_, 7, 2) = 1 == 16384 00000000000000100000000000000000
  vec($_, 8, 2) = 1 == 65536 00000000000000001000000000000000
  vec($_, 9, 2) = 1 == 262144 00000000000000000010000000000000
  vec($_,10, 2) = 1 == 1048576 00000000000000000000100000000000
  vec($_,11, 2) = 1 == 4194304 00000000000000000000001000000000
  vec($_,12, 2) = 1 == 16777216 00000000000000000000000010000000
  vec($_,13, 2) = 1 == 67108864 00000000000000000000000000100000
  vec($_,14, 2) = 1 == 268435456 00000000000000000000000000001000
  vec($_,15, 2) = 1 == 1073741824 00000000000000000000000000000010
  vec($_, 0, 2) = 2 == 2 01000000000000000000000000000000
  vec($_, 1, 2) = 2 == 8 00010000000000000000000000000000
  vec($_, 2, 2) = 2 == 32 00000100000000000000000000000000
  vec($_, 3, 2) = 2 == 128 00000001000000000000000000000000
  vec($_, 4, 2) = 2 == 512 00000000010000000000000000000000
  vec($_, 5, 2) = 2 == 2048 00000000000100000000000000000000
  vec($_, 6, 2) = 2 == 8192 00000000000001000000000000000000
  vec($_, 7, 2) = 2 == 32768 00000000000000010000000000000000
  vec($_, 8, 2) = 2 == 131072 00000000000000000100000000000000
  vec($_, 9, 2) = 2 == 524288 00000000000000000001000000000000
  vec($_,10, 2) = 2 == 2097152 00000000000000000000010000000000
  vec($_,11, 2) = 2 == 8388608 00000000000000000000000100000000
  vec($_,12, 2) = 2 == 33554432 00000000000000000000000001000000
  vec($_,13, 2) = 2 == 134217728 00000000000000000000000000010000
  vec($_,14, 2) = 2 == 536870912 00000000000000000000000000000100
  vec($_,15, 2) = 2 == 2147483648 00000000000000000000000000000001
  vec($_, 0, 4) = 1 == 1 10000000000000000000000000000000
  vec($_, 1, 4) = 1 == 16 00001000000000000000000000000000
  vec($_, 2, 4) = 1 == 256 00000000100000000000000000000000
  vec($_, 3, 4) = 1 == 4096 00000000000010000000000000000000
  vec($_, 4, 4) = 1 == 65536 00000000000000001000000000000000
  vec($_, 5, 4) = 1 == 1048576 00000000000000000000100000000000
  vec($_, 6, 4) = 1 == 16777216 00000000000000000000000010000000
  vec($_, 7, 4) = 1 == 268435456 00000000000000000000000000001000
  vec($_, 0, 4) = 2 == 2 01000000000000000000000000000000
  vec($_, 1, 4) = 2 == 32 00000100000000000000000000000000
  vec($_, 2, 4) = 2 == 512 00000000010000000000000000000000
  vec($_, 3, 4) = 2 == 8192 00000000000001000000000000000000
  vec($_, 4, 4) = 2 == 131072 00000000000000000100000000000000
  vec($_, 5, 4) = 2 == 2097152 00000000000000000000010000000000
  vec($_, 6, 4) = 2 == 33554432 00000000000000000000000001000000
  vec($_, 7, 4) = 2 == 536870912 00000000000000000000000000000100
  vec($_, 0, 4) = 4 == 4 00100000000000000000000000000000
  vec($_, 1, 4) = 4 == 64 00000010000000000000000000000000
  vec($_, 2, 4) = 4 == 1024 00000000001000000000000000000000
  vec($_, 3, 4) = 4 == 16384 00000000000000100000000000000000
  vec($_, 4, 4) = 4 == 262144 00000000000000000010000000000000
  vec($_, 5, 4) = 4 == 4194304 00000000000000000000001000000000
  vec($_, 6, 4) = 4 == 67108864 00000000000000000000000000100000
  vec($_, 7, 4) = 4 == 1073741824 00000000000000000000000000000010
  vec($_, 0, 4) = 8 == 8 00010000000000000000000000000000
  vec($_, 1, 4) = 8 == 128 00000001000000000000000000000000
  vec($_, 2, 4) = 8 == 2048 00000000000100000000000000000000
  vec($_, 3, 4) = 8 == 32768 00000000000000010000000000000000
  vec($_, 4, 4) = 8 == 524288 00000000000000000001000000000000
  vec($_, 5, 4) = 8 == 8388608 00000000000000000000000100000000
  vec($_, 6, 4) = 8 == 134217728 00000000000000000000000000010000
  vec($_, 7, 4) = 8 == 2147483648 00000000000000000000000000000001
  vec($_, 0, 8) = 1 == 1 10000000000000000000000000000000
  vec($_, 1, 8) = 1 == 256 00000000100000000000000000000000
  vec($_, 2, 8) = 1 == 65536 00000000000000001000000000000000
  vec($_, 3, 8) = 1 == 16777216 00000000000000000000000010000000
  vec($_, 0, 8) = 2 == 2 01000000000000000000000000000000
  vec($_, 1, 8) = 2 == 512 00000000010000000000000000000000
  vec($_, 2, 8) = 2 == 131072 00000000000000000100000000000000
  vec($_, 3, 8) = 2 == 33554432 00000000000000000000000001000000
  vec($_, 0, 8) = 4 == 4 00100000000000000000000000000000
  vec($_, 1, 8) = 4 == 1024 00000000001000000000000000000000
  vec($_, 2, 8) = 4 == 262144 00000000000000000010000000000000
  vec($_, 3, 8) = 4 == 67108864 00000000000000000000000000100000
  vec($_, 0, 8) = 8 == 8 00010000000000000000000000000000
  vec($_, 1, 8) = 8 == 2048 00000000000100000000000000000000
  vec($_, 2, 8) = 8 == 524288 00000000000000000001000000000000
  vec($_, 3, 8) = 8 == 134217728 00000000000000000000000000010000
  vec($_, 0, 8) = 16 == 16 00001000000000000000000000000000
  vec($_, 1, 8) = 16 == 4096 00000000000010000000000000000000
  vec($_, 2, 8) = 16 == 1048576 00000000000000000000100000000000
  vec($_, 3, 8) = 16 == 268435456 00000000000000000000000000001000
  vec($_, 0, 8) = 32 == 32 00000100000000000000000000000000
  vec($_, 1, 8) = 32 == 8192 00000000000001000000000000000000
  vec($_, 2, 8) = 32 == 2097152 00000000000000000000010000000000
  vec($_, 3, 8) = 32 == 536870912 00000000000000000000000000000100
  vec($_, 0, 8) = 64 == 64 00000010000000000000000000000000
  vec($_, 1, 8) = 64 == 16384 00000000000000100000000000000000
  vec($_, 2, 8) = 64 == 4194304 00000000000000000000001000000000
  vec($_, 3, 8) = 64 == 1073741824 00000000000000000000000000000010
  vec($_, 0, 8) = 128 == 128 00000001000000000000000000000000
  vec($_, 1, 8) = 128 == 32768 00000000000000010000000000000000
  vec($_, 2, 8) = 128 == 8388608 00000000000000000000000100000000
  vec($_, 3, 8) = 128 == 2147483648 00000000000000000000000000000001
</code></pre>
 </dd>
<dt>wait</dt>
<dd> <p> Behaves like <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) on your system: it waits for a child process to terminate and returns the pid of the deceased process, or <code>&quot;-1&quot;</code> if there are no child processes. The status is returned in <code>$?</code> and <code>&quot;${^CHILD_ERROR_NATIVE}&quot;</code>. Note that a return value of <code>&quot;-1&quot;</code> could mean that child processes are being automatically reaped, as described in perlipc. </p>
<p> If you use <code>&quot;wait&quot;</code> in your handler for <code>$SIG{CHLD}</code>, it may accidentally wait for the child created by <code>&quot;qx&quot;</code> or <code>&quot;system&quot;</code>. See perlipc for details. </p>
<p> Portability issues: ``wait&#8217;&#8216; in perlport. </p>
 </dd>
<dt>waitpid <font SIZE="-1">PID,FLAGS</font></dt>
<dd> <p> Waits for a particular child process to terminate and returns the pid of the deceased process, or <code>&quot;-1&quot;</code> if there is no such child process. A non-blocking wait (with <font SIZE="-1">WNOHANG</font> in <font SIZE="-1">FLAGS</font>) can return 0 if there are child processes matching <font SIZE="-1">PID</font> but none have terminated yet. The status is returned in <code>$?</code> and <code>&quot;${^CHILD_ERROR_NATIVE}&quot;</code>. </p>
<p> A <font SIZE="-1">PID</font> of <code>0</code> indicates to wait for any child process whose process group <font SIZE="-1">ID</font> is equal to that of the current process. A <font SIZE="-1">PID</font> of less than <code>&quot;-1&quot;</code> indicates to wait for any child process whose process group <font SIZE="-1">ID</font> is equal to -PID. A <font SIZE="-1">PID</font> of <code>&quot;-1&quot;</code> indicates to wait for any child process. </p>
<p> If you say </p>
<pre><code>    use POSIX &quot;:sys_wait_h&quot;;
    my $kid;
    do {
        $kid = waitpid(-1, WNOHANG);
    } while $kid &gt; 0;
</code></pre>
<p> or </p>
<pre><code>    1 while waitpid(-1, WNOHANG) &gt; 0;
</code></pre>
<p> then you can do a non-blocking wait for all pending zombie processes (see ``<font SIZE="-1">WAIT&#8217;&#8216;</font> in <font SIZE="-1">POSIX</font>). Non-blocking wait is available on machines supporting either the <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) or <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2) syscalls. However, waiting for a particular pid with <font SIZE="-1">FLAGS</font> of <code>0</code> is implemented everywhere. (Perl emulates the system call by remembering the status values of processes that have exited but have not been harvested by the Perl script yet.) </p>
<p> Note that on some systems, a return value of <code>&quot;-1&quot;</code> could mean that child processes are being automatically reaped. See perlipc for details, and for other examples. </p>
<p> Portability issues: ``waitpid&#8217;&#8216; in perlport. </p>
 </dd>
<dt>wantarray</dt>
<dd> <p> Returns true if the context of the currently executing subroutine or <code>&quot;eval&quot;</code> is looking for a list value. Returns false if the context is looking for a scalar. Returns the undefined value if the context is looking for no value (void context). </p>
<pre><code>    return unless defined wantarray; # don't bother doing more
    my @a = complex_calculation();
    return wantarray ? @a : &quot;@a&quot;;
</code></pre>
<p> <code>&quot;wantarray&quot;</code>&#8216;s result is unspecified in the top level of a file, in a <code>&quot;BEGIN&quot;</code>, <code>&quot;UNITCHECK&quot;</code>, <code>&quot;CHECK&quot;</code>, <code>&quot;INIT&quot;</code> or <code>&quot;END&quot;</code> block, or in a <code>&quot;DESTROY&quot;</code> method. </p>
<p> This function should have been named <code>wantlist()</code> instead. </p>
 </dd>
<dt>warn <font SIZE="-1">LIST</font></dt>
<dd> <p> Emits a warning, usually by printing it to <code>&quot;STDERR&quot;</code>. <code>&quot;warn&quot;</code> interprets its operand <font SIZE="-1">LIST</font> in the same way as <code>&quot;die&quot;</code>, but is slightly different in what it defaults to when <font SIZE="-1">LIST</font> is empty or makes an empty string. If it is empty and <code>$@</code> already contains an exception value then that value is used after appending <code>&quot;\t...caught&quot;</code>. If it is empty and <code>$@</code> is also empty then the string <code>&quot;Warning: Something&#8217;s wrong&quot;</code> is used. </p>
<p> By default, the exception derived from the operand <font SIZE="-1">LIST</font> is stringified and printed to <code>&quot;STDERR&quot;</code>. This behaviour can be altered by installing a <code>$SIG{__WARN__}</code> handler. If there is such a handler then no message is automatically printed; it is the handler&#8217;s responsibility to deal with the exception as it sees fit (like, for instance, converting it into a <code>&quot;die&quot;</code>). Most handlers must therefore arrange to actually display the warnings that they are not prepared to deal with, by calling <code>&quot;warn&quot;</code> again in the handler. Note that this is quite safe and will not produce an endless loop, since <code>&quot;__WARN__&quot;</code> hooks are not called from inside one. </p>
<p> You will find this behavior is slightly different from that of <code>$SIG{__DIE__}</code> handlers (which don&#8217;t suppress the error text, but can instead call <code>&quot;die&quot;</code> again to change it). </p>
<p> Using a <code>&quot;__WARN__&quot;</code> handler provides a powerful way to silence all warnings (even the so-called mandatory ones). An example: </p>
<pre><code>    # wipe out *all* compile-time warnings
    BEGIN { $SIG{'__WARN__'} = sub { warn $_[0] if $DOWARN } }
    my $foo = 10;
    my $foo = 20; # no warning about duplicate my $foo,
                           # but hey, you asked for it!
    # no compile-time or run-time warnings before here
    $DOWARN = 1;
    # run-time warnings enabled after here
    warn &quot;\$foo is alive and $foo!&quot;; # does show up
</code></pre>
<p> See perlvar for details on setting <code>%SIG</code> entries and for more examples. See the Carp module for other kinds of warnings using its <code>&quot;carp&quot;</code> and <code>&quot;cluck&quot;</code> functions. </p>
 </dd>
<dt>write <font SIZE="-1">FILEHANDLE</font></dt>
<dd>  </dd>
<dt>write <font SIZE="-1">EXPR</font></dt>
<dd>  </dd>
<dt>write</dt>
<dd> <p> Writes a formatted record (possibly multi-line) to the specified <font SIZE="-1">FILEHANDLE,</font> using the format associated with that file. By default the format for a file is the one having the same name as the filehandle, but the format for the current output channel (see the <code>&quot;select&quot;</code> function) may be set explicitly by assigning the name of the format to the <code>$~</code> variable. </p>
<p> Top of form processing is handled automatically: if there is insufficient room on the current page for the formatted record, the page is advanced by writing a form feed and a special top-of-page format is used to format the new page header before the record is written. By default, the top-of-page format is the name of the filehandle with <code>&quot;_TOP&quot;</code> appended, or <code>&quot;top&quot;</code> in the current package if the former does not exist. This would be a problem with autovivified filehandles, but it may be dynamically set to the format of your choice by assigning the name to the <code>$^</code> variable while that filehandle is selected. The number of lines remaining on the current page is in variable <code>&quot;$-&quot;</code>, which can be set to <code>0</code> to force a new page. </p>
<p> If <font SIZE="-1">FILEHANDLE</font> is unspecified, output goes to the current default output channel, which starts out as <font SIZE="-1">STDOUT</font> but may be changed by the <code>&quot;select&quot;</code> operator. If the <font SIZE="-1">FILEHANDLE</font> is an <font SIZE="-1">EXPR,</font> then the expression is evaluated and the resulting string is used to look up the name of the <font SIZE="-1">FILEHANDLE</font> at run time. For more on formats, see perlform. </p>
<p> Note that write is <i>not</i> the opposite of <code>&quot;read&quot;</code>. Unfortunately. </p>
 </dd>
<dt>y///</dt>
<dd> <p> The transliteration operator. Same as <code>&quot;tr///&quot;</code>. See ``Quote-Like Operators&#8217;&#8216; in perlop. </p>
 </dd></dl>
<h3>Non-function Keywords by Cross-reference</h3>
<p> <i>perldata</i> </p>
<dl>
<dt>__DATA__</dt>
<dd>  </dd>
<dt>__END__</dt>
<dd> <p> These keywords are documented in ``Special Literals&#8217;&#8216; in perldata. </p>
 </dd></dl>
<p> <i>perlmod</i> </p>
<dl>
<dt><font SIZE="-1">BEGIN</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">CHECK</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">END</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">INIT</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">UNITCHECK</font></dt>
<dd> <p> These compile phase keywords are documented in ``<font SIZE="-1">BEGIN, UNITCHECK, CHECK, INIT</font> and <font SIZE="-1">END&#8217;&#8216;</font> in perlmod. </p>
 </dd></dl>
<p> <i>perlobj</i> </p>
<dl>
<dt><font SIZE="-1">DESTROY</font></dt>
<dd> <p> This method keyword is documented in ``Destructors&#8217;&#8216; in perlobj. </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>and</dt>
<dd>  </dd>
<dt>cmp</dt>
<dd>  </dd>
<dt>eq</dt>
<dd>  </dd>
<dt>ge</dt>
<dd>  </dd>
<dt>gt</dt>
<dd>  </dd>
<dt>le</dt>
<dd>  </dd>
<dt>lt</dt>
<dd>  </dd>
<dt>ne</dt>
<dd>  </dd>
<dt>not</dt>
<dd>  </dd>
<dt>or</dt>
<dd>  </dd>
<dt>x</dt>
<dd>  </dd>
<dt>xor</dt>
<dd> <p> These operators are documented in perlop. </p>
 </dd></dl>
<p> <i>perlsub</i> </p>
<dl>
<dt><font SIZE="-1">AUTOLOAD</font></dt>
<dd> <p> This keyword is documented in ``Autoloading&#8217;&#8216; in perlsub. </p>
 </dd></dl>
<p> <i>perlsyn</i> </p>
<dl>
<dt>else</dt>
<dd>  </dd>
<dt>elsif</dt>
<dd>  </dd>
<dt>for</dt>
<dd>  </dd>
<dt>foreach</dt>
<dd>  </dd>
<dt>if</dt>
<dd>  </dd>
<dt>unless</dt>
<dd>  </dd>
<dt>until</dt>
<dd>  </dd>
<dt>while</dt>
<dd> <p> These flow-control keywords are documented in ``Compound Statements&#8217;&#8216; in perlsyn. </p>
 </dd>
<dt>elseif</dt>
<dd> <p> The ``else if&#8217;&#8216; keyword is spelled <code>&quot;elsif&quot;</code> in Perl. There&#8217;s no <code>&quot;elif&quot;</code> or <code>&quot;else if&quot;</code> either. It does parse <code>&quot;elseif&quot;</code>, but only to warn you about not using it. </p>
<p> See the documentation for flow-control keywords in ``Compound Statements&#8217;&#8216; in perlsyn. </p>
 </dd>
<dt>default</dt>
<dd>  </dd>
<dt>given</dt>
<dd>  </dd>
<dt>when</dt>
<dd> <p> These flow-control keywords related to the experimental switch feature are documented in ``Switch Statements&#8217;&#8216; in perlsyn. </p>
 </dd></dl>
