---
title: "perlfunc(1)"
name: "perlfunc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfunc/"
description: "perlfunc – Perl builtin functions"
---

<h2 class="name">NAME</h2>
<p> perlfunc &#8211; Perl builtin functions </p>
<h2>DESCRIPTION</h2>
<p> The functions in this section can serve as terms in an expression. They fall into two major categories: list operators and named unary operators. These differ in their precedence relationship with a following comma. (See the precedence table in perlop.) List operators take more than one argument, while unary operators can never take more than one argument. Thus, a comma terminates the argument of a unary operator, but merely separates the arguments of a list operator. A unary operator generally provides scalar context to its argument, while a list operator may provide either scalar or list contexts for its arguments. If it does both, scalar arguments come first and list argument follow, and there can only ever be one such list argument. For instance, <tt>&quot;splice&quot;</tt> has three scalar arguments followed by a list, whereas <tt>&quot;gethostbyname&quot;</tt> has four scalar arguments. </p>
<p> In the syntax descriptions that follow, list operators that expect a list (and provide list context for elements of the list) are shown with <font SIZE="-1">LIST</font> as an argument. Such a list may consist of any combination of scalar arguments or list values; the list values will be included in the list as if each individual element were interpolated at that point in the list, forming a longer single-dimensional list value. Commas should separate literal elements of the <font SIZE="-1">LIST.</font> </p>
<p> Any function in the list below may be used either with or without parentheses around its arguments. (The syntax descriptions omit the parentheses.) If you use parentheses, the simple but occasionally surprising rule is this: It <i>looks</i> like a function, therefore it <i>is</i> a function, and precedence doesn&#8217;t matter. Otherwise it&#8217;s a list operator or unary operator, and precedence does matter. Whitespace between the function and left parenthesis doesn&#8217;t count, so sometimes you need to be careful: </p>
<pre><code>
print 1 + 2 + 4;
#Prints 7. print(1 + 2) + 4;
#Prints 3. print(1 + 2) + 4;
#Also prints 3 !print + (1 + 2) + 4;
#Prints 7. print((1 + 2) + 4);
#Prints 7.
</code></pre>
<p> If you run Perl with the <tt>&quot;use warnings&quot;</tt> pragma, it can warn you about this. For example, the third line above produces: </p>
<pre>
    print (...) interpreted as function at - line 1.
    Useless use of integer addition in void context at - line 1.
</pre>
<p> A few functions take no arguments at all, and therefore work as neither unary nor list operators. These include such functions as <tt>&quot;time&quot;</tt> and <tt>&quot;endpwent&quot;</tt>. For example, <tt>&quot;time+86_400&quot;</tt> always means <tt>&quot;time() + 86_400&quot;</tt>. </p>
<p> For functions that can be used in either a scalar or list context, nonabortive failure is generally indicated in scalar context by returning the undefined value, and in list context by returning the empty list. </p>
<p> Remember the following important rule: There is <code>no rule</code> that relates the behavior of an expression in list context to its behavior in scalar context, or vice versa. It might do two totally different things. Each operator and function decides which sort of value would be most appropriate to return in scalar context. Some operators return the length of the list that would have been returned in list context. Some operators return the first value in the list. Some operators return the last value in the list. Some operators return a count of successful operations. In general, they do what you want, unless you want consistency. </p>
<p> A named array in scalar context is quite different from what would at first glance appear to be a list in scalar context. You can&#8217;t get a list like <tt>&quot;(1,2,3)&quot;</tt> into being in scalar context, because the compiler knows the context at compile time. It would generate the scalar comma operator there, not the list concatenation version of the comma. That means it was never a list to start with. </p>
<p> In general, functions in Perl that serve as wrappers for system calls (&#8220;syscalls&#8221;) of the same name (like <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-closedir/">closedir</a></code>(2), etc.) return true when they succeed and <tt>&quot;undef&quot;</tt> otherwise, as is usually mentioned in the descriptions below. This is different from the C interfaces, which return <tt>&quot;-1&quot;</tt> on failure. Exceptions to this rule include <tt>&quot;wait&quot;</tt>, <tt>&quot;waitpid&quot;</tt>, and <tt>&quot;syscall&quot;</tt>. System calls also set the special <tt>$!</tt> variable on failure. Other functions do not, except accidentally. </p>
<p> Extension modules can also hook into the Perl parser to define new kinds of keyword-headed expression. These may look like functions, but may also look completely different. The syntax following the keyword is defined entirely by the extension. If you are an implementor, see &#8220;PL_keyword_plugin&#8221; in perlapi for the mechanism. If you are using such a module, see the module&#8217;s documentation for details of the syntax that it defines.</p>
<h3>Perl Functions by Category</h3>
<p> Here are Perl&#8217;s functions (including things that look like functions, like some keywords and named operators) arranged by category. Some functions appear in more than one place. Any warnings, including those produced by keywords, are described in perldiag and warnings.</p>
<dl>
<dt>Functions for SCALARs or strings</p>
<dd> <tt>&quot;chomp&quot;</tt>, <tt>&quot;chop&quot;</tt>, <tt>&quot;chr&quot;</tt>, <tt>&quot;crypt&quot;</tt>, <tt>&quot;fc&quot;</tt>, <tt>&quot;hex&quot;</tt>, <tt>&quot;index&quot;</tt>, <tt>&quot;lc&quot;</tt>, <tt>&quot;lcfirst&quot;</tt>, <tt>&quot;length&quot;</tt>, <tt>&quot;oct&quot;</tt>, <tt>&quot;ord&quot;</tt>, <tt>&quot;pack&quot;</tt>, <tt>&quot;q//&quot;</tt>, <tt>&quot;qq//&quot;</tt>, <tt>&quot;reverse&quot;</tt>, <tt>&quot;rindex&quot;</tt>, <tt>&quot;sprintf&quot;</tt>, <tt>&quot;substr&quot;</tt>, <tt>&quot;tr///&quot;</tt>, <tt>&quot;uc&quot;</tt>, <tt>&quot;ucfirst&quot;</tt>, <tt>&quot;y///&quot;</tt> </p>
<p> <tt>&quot;fc&quot;</tt> is available only if the <tt>&quot;fc&quot;</tt> feature is enabled or if it is prefixed with <tt>&quot;CORE::&quot;</tt>. The <tt>&quot;fc&quot;</tt> feature is enabled automatically with a <tt>&quot;use v5.16&quot;</tt> (or higher) declaration in the current scope.</p>
<dt>Regular expressions and pattern matching</p>
<dd> <tt>&quot;m//&quot;</tt>, <tt>&quot;pos&quot;</tt>, <tt>&quot;qr//&quot;</tt>, <tt>&quot;quotemeta&quot;</tt>, <tt>&quot;s///&quot;</tt>, <tt>&quot;split&quot;</tt>, <tt>&quot;study&quot;</tt></p>
<dt>Numeric functions</p>
<dd> <tt>&quot;abs&quot;</tt>, <tt>&quot;atan2&quot;</tt>, <tt>&quot;cos&quot;</tt>, <tt>&quot;exp&quot;</tt>, <tt>&quot;hex&quot;</tt>, <tt>&quot;int&quot;</tt>, <tt>&quot;log&quot;</tt>, <tt>&quot;oct&quot;</tt>, <tt>&quot;rand&quot;</tt>, <tt>&quot;sin&quot;</tt>, <tt>&quot;sqrt&quot;</tt>, <tt>&quot;srand&quot;</tt></p>
<dt>Functions for real @ARRAYs</p>
<dd> <tt>&quot;each&quot;</tt>, <tt>&quot;keys&quot;</tt>, <tt>&quot;pop&quot;</tt>, <tt>&quot;push&quot;</tt>, <tt>&quot;shift&quot;</tt>, <tt>&quot;splice&quot;</tt>, <tt>&quot;unshift&quot;</tt>, <tt>&quot;values&quot;</tt></p>
<dt>Functions for list data</p>
<dd> <tt>&quot;grep&quot;</tt>, <tt>&quot;join&quot;</tt>, <tt>&quot;map&quot;</tt>, <tt>&quot;qw//&quot;</tt>, <tt>&quot;reverse&quot;</tt>, <tt>&quot;sort&quot;</tt>, <tt>&quot;unpack&quot;</tt></p>
<dt>Functions for real %HASHes</p>
<dd> <tt>&quot;delete&quot;</tt>, <tt>&quot;each&quot;</tt>, <tt>&quot;exists&quot;</tt>, <tt>&quot;keys&quot;</tt>, <tt>&quot;values&quot;</tt></p>
<dt>Input and output functions</p>
<dd> <tt>&quot;binmode&quot;</tt>, <tt>&quot;close&quot;</tt>, <tt>&quot;closedir&quot;</tt>, <tt>&quot;dbmclose&quot;</tt>, <tt>&quot;dbmopen&quot;</tt>, <tt>&quot;die&quot;</tt>, <tt>&quot;eof&quot;</tt>, <tt>&quot;fileno&quot;</tt>, <tt>&quot;flock&quot;</tt>, <tt>&quot;format&quot;</tt>, <tt>&quot;getc&quot;</tt>, <tt>&quot;print&quot;</tt>, <tt>&quot;printf&quot;</tt>, <tt>&quot;read&quot;</tt>, <tt>&quot;readdir&quot;</tt>, <tt>&quot;readline&quot;</tt>, <tt>&quot;rewinddir&quot;</tt>, <tt>&quot;say&quot;</tt>, <tt>&quot;seek&quot;</tt>, <tt>&quot;seekdir&quot;</tt>, <tt>&quot;select&quot;</tt>, <tt>&quot;syscall&quot;</tt>, <tt>&quot;sysread&quot;</tt>, <tt>&quot;sysseek&quot;</tt>, <tt>&quot;syswrite&quot;</tt>, <tt>&quot;tell&quot;</tt>, <tt>&quot;telldir&quot;</tt>, <tt>&quot;truncate&quot;</tt>, <tt>&quot;warn&quot;</tt>, <tt>&quot;write&quot;</tt> </p>
<p> <tt>&quot;say&quot;</tt> is available only if the <tt>&quot;say&quot;</tt> feature is enabled or if it is prefixed with <tt>&quot;CORE::&quot;</tt>. The <tt>&quot;say&quot;</tt> feature is enabled automatically with a <tt>&quot;use v5.10&quot;</tt> (or higher) declaration in the current scope.</p>
<dt>Functions for fixed-length data or records</p>
<dd> <tt>&quot;pack&quot;</tt>, <tt>&quot;read&quot;</tt>, <tt>&quot;syscall&quot;</tt>, <tt>&quot;sysread&quot;</tt>, <tt>&quot;sysseek&quot;</tt>, <tt>&quot;syswrite&quot;</tt>, <tt>&quot;unpack&quot;</tt>, <tt>&quot;vec&quot;</tt></p>
<dt>Functions for filehandles, files, or directories</p>
<dd> <tt>&quot;-</tt>X<tt>&quot;</tt>, <tt>&quot;chdir&quot;</tt>, <tt>&quot;chmod&quot;</tt>, <tt>&quot;chown&quot;</tt>, <tt>&quot;chroot&quot;</tt>, <tt>&quot;fcntl&quot;</tt>, <tt>&quot;glob&quot;</tt>, <tt>&quot;ioctl&quot;</tt>, <tt>&quot;link&quot;</tt>, <tt>&quot;lstat&quot;</tt>, <tt>&quot;mkdir&quot;</tt>, <tt>&quot;open&quot;</tt>, <tt>&quot;opendir&quot;</tt>, <tt>&quot;readlink&quot;</tt>, <tt>&quot;rename&quot;</tt>, <tt>&quot;rmdir&quot;</tt>, <tt>&quot;select&quot;</tt>, <tt>&quot;stat&quot;</tt>, <tt>&quot;symlink&quot;</tt>, <tt>&quot;sysopen&quot;</tt>, <tt>&quot;umask&quot;</tt>, <tt>&quot;unlink&quot;</tt>, <tt>&quot;utime&quot;</tt></p>
<dt>Keywords related to the control flow of your Perl program</p>
<dd> <tt>&quot;break&quot;</tt>, <tt>&quot;caller&quot;</tt>, <tt>&quot;continue&quot;</tt>, <tt>&quot;die&quot;</tt>, <tt>&quot;do&quot;</tt>, <tt>&quot;dump&quot;</tt>, <tt>&quot;eval&quot;</tt>, <tt>&quot;evalbytes&quot;</tt>, <tt>&quot;exit&quot;</tt>, <tt>&quot;__FILE__&quot;</tt>, <tt>&quot;goto&quot;</tt>, <tt>&quot;last&quot;</tt>, <tt>&quot;__LINE__&quot;</tt>, <tt>&quot;next&quot;</tt>, <tt>&quot;__PACKAGE__&quot;</tt>, <tt>&quot;redo&quot;</tt>, <tt>&quot;return&quot;</tt>, <tt>&quot;sub&quot;</tt>, <tt>&quot;__SUB__&quot;</tt>, <tt>&quot;wantarray&quot;</tt> </p>
<p> <tt>&quot;break&quot;</tt> is available only if you enable the experimental <tt>&quot;switch&quot;</tt> feature or use the <tt>&quot;CORE::&quot;</tt> prefix. The <tt>&quot;switch&quot;</tt> feature also enables the <tt>&quot;default&quot;</tt>, <tt>&quot;given&quot;</tt> and <tt>&quot;when&quot;</tt> statements, which are documented in &#8220;Switch Statements&#8221; in perlsyn. The <tt>&quot;switch&quot;</tt> feature is enabled automatically with a <tt>&quot;use v5.10&quot;</tt> (or higher) declaration in the current scope. In Perl v5.14 and earlier, <tt>&quot;continue&quot;</tt> required the <tt>&quot;switch&quot;</tt> feature, like the other keywords. </p>
<p> <tt>&quot;evalbytes&quot;</tt> is only available with the <tt>&quot;evalbytes&quot;</tt> feature (see feature) or if prefixed with <tt>&quot;CORE::&quot;</tt>. <tt>&quot;__SUB__&quot;</tt> is only available with the <tt>&quot;current_sub&quot;</tt> feature or if prefixed with <tt>&quot;CORE::&quot;</tt>. Both the <tt>&quot;evalbytes&quot;</tt> and <tt>&quot;current_sub&quot;</tt> features are enabled automatically with a <tt>&quot;use v5.16&quot;</tt> (or higher) declaration in the current scope.</p>
<dt>Keywords related to scoping</p>
<dd> <tt>&quot;caller&quot;</tt>, <tt>&quot;import&quot;</tt>, <tt>&quot;local&quot;</tt>, <tt>&quot;my&quot;</tt>, <tt>&quot;our&quot;</tt>, <tt>&quot;package&quot;</tt>, <tt>&quot;state&quot;</tt>, <tt>&quot;use&quot;</tt> </p>
<p> <tt>&quot;state&quot;</tt> is available only if the <tt>&quot;state&quot;</tt> feature is enabled or if it is prefixed with <tt>&quot;CORE::&quot;</tt>. The <tt>&quot;state&quot;</tt> feature is enabled automatically with a <tt>&quot;use v5.10&quot;</tt> (or higher) declaration in the current scope.</p>
<dt>Miscellaneous functions</p>
<dd> <tt>&quot;defined&quot;</tt>, <tt>&quot;formline&quot;</tt>, <tt>&quot;lock&quot;</tt>, <tt>&quot;prototype&quot;</tt>, <tt>&quot;reset&quot;</tt>, <tt>&quot;scalar&quot;</tt>, <tt>&quot;undef&quot;</tt></p>
<dt>Functions for processes and process groups</p>
<dd> <tt>&quot;alarm&quot;</tt>, <tt>&quot;exec&quot;</tt>, <tt>&quot;fork&quot;</tt>, <tt>&quot;getpgrp&quot;</tt>, <tt>&quot;getppid&quot;</tt>, <tt>&quot;getpriority&quot;</tt>, <tt>&quot;kill&quot;</tt>, <tt>&quot;pipe&quot;</tt>, <tt>&quot;qx//&quot;</tt>, <tt>&quot;readpipe&quot;</tt>, <tt>&quot;setpgrp&quot;</tt>, <tt>&quot;setpriority&quot;</tt>, <tt>&quot;sleep&quot;</tt>, <tt>&quot;system&quot;</tt>, <tt>&quot;times&quot;</tt>, <tt>&quot;wait&quot;</tt>, <tt>&quot;waitpid&quot;</tt></p>
<dt>Keywords related to Perl modules</p>
<dd> <tt>&quot;do&quot;</tt>, <tt>&quot;import&quot;</tt>, <tt>&quot;no&quot;</tt>, <tt>&quot;package&quot;</tt>, <tt>&quot;require&quot;</tt>, <tt>&quot;use&quot;</tt></p>
<dt>Keywords related to classes and object-orientation</p>
<dd> <tt>&quot;bless&quot;</tt>, <tt>&quot;dbmclose&quot;</tt>, <tt>&quot;dbmopen&quot;</tt>, <tt>&quot;package&quot;</tt>, <tt>&quot;ref&quot;</tt>, <tt>&quot;tie&quot;</tt>, <tt>&quot;tied&quot;</tt>, <tt>&quot;untie&quot;</tt>, <tt>&quot;use&quot;</tt></p>
<dt>Low-level socket functions</p>
<dd> <tt>&quot;accept&quot;</tt>, <tt>&quot;bind&quot;</tt>, <tt>&quot;connect&quot;</tt>, <tt>&quot;getpeername&quot;</tt>, <tt>&quot;getsockname&quot;</tt>, <tt>&quot;getsockopt&quot;</tt>, <tt>&quot;listen&quot;</tt>, <tt>&quot;recv&quot;</tt>, <tt>&quot;send&quot;</tt>, <tt>&quot;setsockopt&quot;</tt>, <tt>&quot;shutdown&quot;</tt>, <tt>&quot;socket&quot;</tt>, <tt>&quot;socketpair&quot;</tt></p>
<dt>System V interprocess communication functions</p>
<dd> <tt>&quot;msgctl&quot;</tt>, <tt>&quot;msgget&quot;</tt>, <tt>&quot;msgrcv&quot;</tt>, <tt>&quot;msgsnd&quot;</tt>, <tt>&quot;semctl&quot;</tt>, <tt>&quot;semget&quot;</tt>, <tt>&quot;semop&quot;</tt>, <tt>&quot;shmctl&quot;</tt>, <tt>&quot;shmget&quot;</tt>, <tt>&quot;shmread&quot;</tt>, <tt>&quot;shmwrite&quot;</tt></p>
<dt>Fetching user and group info</p>
<dd> <tt>&quot;endgrent&quot;</tt>, <tt>&quot;endhostent&quot;</tt>, <tt>&quot;endnetent&quot;</tt>, <tt>&quot;endpwent&quot;</tt>, <tt>&quot;getgrent&quot;</tt>, <tt>&quot;getgrgid&quot;</tt>, <tt>&quot;getgrnam&quot;</tt>, <tt>&quot;getlogin&quot;</tt>, <tt>&quot;getpwent&quot;</tt>, <tt>&quot;getpwnam&quot;</tt>, <tt>&quot;getpwuid&quot;</tt>, <tt>&quot;setgrent&quot;</tt>, <tt>&quot;setpwent&quot;</tt></p>
<dt>Fetching network info</p>
<dd> <tt>&quot;endprotoent&quot;</tt>, <tt>&quot;endservent&quot;</tt>, <tt>&quot;gethostbyaddr&quot;</tt>, <tt>&quot;gethostbyname&quot;</tt>, <tt>&quot;gethostent&quot;</tt>, <tt>&quot;getnetbyaddr&quot;</tt>, <tt>&quot;getnetbyname&quot;</tt>, <tt>&quot;getnetent&quot;</tt>, <tt>&quot;getprotobyname&quot;</tt>, <tt>&quot;getprotobynumber&quot;</tt>, <tt>&quot;getprotoent&quot;</tt>, <tt>&quot;getservbyname&quot;</tt>, <tt>&quot;getservbyport&quot;</tt>, <tt>&quot;getservent&quot;</tt>, <tt>&quot;sethostent&quot;</tt>, <tt>&quot;setnetent&quot;</tt>, <tt>&quot;setprotoent&quot;</tt>, <tt>&quot;setservent&quot;</tt></p>
<dt>Time-related functions</p>
<dd> <tt>&quot;gmtime&quot;</tt>, <tt>&quot;localtime&quot;</tt>, <tt>&quot;time&quot;</tt>, <tt>&quot;times&quot;</tt></p>
<dt>Non-function keywords</p>
<dd> <tt>&quot;and&quot;</tt>, <tt>&quot;AUTOLOAD&quot;</tt>, <tt>&quot;BEGIN&quot;</tt>, <tt>&quot;CHECK&quot;</tt>, <tt>&quot;cmp&quot;</tt>, <tt>&quot;CORE&quot;</tt>, <tt>&quot;__DATA__&quot;</tt>, <tt>&quot;default&quot;</tt>, <tt>&quot;DESTROY&quot;</tt>, <tt>&quot;else&quot;</tt>, <tt>&quot;elseif&quot;</tt>, <tt>&quot;elsif&quot;</tt>, <tt>&quot;END&quot;</tt>, <tt>&quot;__END__&quot;</tt>, <tt>&quot;eq&quot;</tt>, <tt>&quot;for&quot;</tt>, <tt>&quot;foreach&quot;</tt>, <tt>&quot;ge&quot;</tt>, <tt>&quot;given&quot;</tt>, <tt>&quot;gt&quot;</tt>, <tt>&quot;if&quot;</tt>, <tt>&quot;INIT&quot;</tt>, <tt>&quot;le&quot;</tt>, <tt>&quot;lt&quot;</tt>, <tt>&quot;ne&quot;</tt>, <tt>&quot;not&quot;</tt>, <tt>&quot;or&quot;</tt>, <tt>&quot;UNITCHECK&quot;</tt>, <tt>&quot;unless&quot;</tt>, <tt>&quot;until&quot;</tt>, <tt>&quot;when&quot;</tt>, <tt>&quot;while&quot;</tt>, <tt>&quot;x&quot;</tt>, <tt>&quot;xor&quot;</tt></dl>
<h3>Portability</h3>
<p> Perl was born in Unix and can therefore access all common Unix system calls. In non-Unix environments, the functionality of some Unix system calls may not be available or details of the available functionality may differ slightly. The Perl functions affected by this are: </p>
<p> <tt>&quot;-</tt>X<tt>&quot;</tt>, <tt>&quot;binmode&quot;</tt>, <tt>&quot;chmod&quot;</tt>, <tt>&quot;chown&quot;</tt>, <tt>&quot;chroot&quot;</tt>, <tt>&quot;crypt&quot;</tt>, <tt>&quot;dbmclose&quot;</tt>, <tt>&quot;dbmopen&quot;</tt>, <tt>&quot;dump&quot;</tt>, <tt>&quot;endgrent&quot;</tt>, <tt>&quot;endhostent&quot;</tt>, <tt>&quot;endnetent&quot;</tt>, <tt>&quot;endprotoent&quot;</tt>, <tt>&quot;endpwent&quot;</tt>, <tt>&quot;endservent&quot;</tt>, <tt>&quot;exec&quot;</tt>, <tt>&quot;fcntl&quot;</tt>, <tt>&quot;flock&quot;</tt>, <tt>&quot;fork&quot;</tt>, <tt>&quot;getgrent&quot;</tt>, <tt>&quot;getgrgid&quot;</tt>, <tt>&quot;gethostbyname&quot;</tt>, <tt>&quot;gethostent&quot;</tt>, <tt>&quot;getlogin&quot;</tt>, <tt>&quot;getnetbyaddr&quot;</tt>, <tt>&quot;getnetbyname&quot;</tt>, <tt>&quot;getnetent&quot;</tt>, <tt>&quot;getppid&quot;</tt>, <tt>&quot;getpgrp&quot;</tt>, <tt>&quot;getpriority&quot;</tt>, <tt>&quot;getprotobynumber&quot;</tt>, <tt>&quot;getprotoent&quot;</tt>, <tt>&quot;getpwent&quot;</tt>, <tt>&quot;getpwnam&quot;</tt>, <tt>&quot;getpwuid&quot;</tt>, <tt>&quot;getservbyport&quot;</tt>, <tt>&quot;getservent&quot;</tt>, <tt>&quot;getsockopt&quot;</tt>, <tt>&quot;glob&quot;</tt>, <tt>&quot;ioctl&quot;</tt>, <tt>&quot;kill&quot;</tt>, <tt>&quot;link&quot;</tt>, <tt>&quot;lstat&quot;</tt>, <tt>&quot;msgctl&quot;</tt>, <tt>&quot;msgget&quot;</tt>, <tt>&quot;msgrcv&quot;</tt>, <tt>&quot;msgsnd&quot;</tt>, <tt>&quot;open&quot;</tt>, <tt>&quot;pipe&quot;</tt>, <tt>&quot;readlink&quot;</tt>, <tt>&quot;rename&quot;</tt>, <tt>&quot;select&quot;</tt>, <tt>&quot;semctl&quot;</tt>, <tt>&quot;semget&quot;</tt>, <tt>&quot;semop&quot;</tt>, <tt>&quot;setgrent&quot;</tt>, <tt>&quot;sethostent&quot;</tt>, <tt>&quot;setnetent&quot;</tt>, <tt>&quot;setpgrp&quot;</tt>, <tt>&quot;setpriority&quot;</tt>, <tt>&quot;setprotoent&quot;</tt>, <tt>&quot;setpwent&quot;</tt>, <tt>&quot;setservent&quot;</tt>, <tt>&quot;setsockopt&quot;</tt>, <tt>&quot;shmctl&quot;</tt>, <tt>&quot;shmget&quot;</tt>, <tt>&quot;shmread&quot;</tt>, <tt>&quot;shmwrite&quot;</tt>, <tt>&quot;socket&quot;</tt>, <tt>&quot;socketpair&quot;</tt>, <tt>&quot;stat&quot;</tt>, <tt>&quot;symlink&quot;</tt>, <tt>&quot;syscall&quot;</tt>, <tt>&quot;sysopen&quot;</tt>, <tt>&quot;system&quot;</tt>, <tt>&quot;times&quot;</tt>, <tt>&quot;truncate&quot;</tt>, <tt>&quot;umask&quot;</tt>, <tt>&quot;unlink&quot;</tt>, <tt>&quot;utime&quot;</tt>, <tt>&quot;wait&quot;</tt>, <tt>&quot;waitpid&quot;</tt> </p>
<p> For more information about the portability of these functions, see perlport and other available platform-specific documentation.</p>
<h3>Alphabetical Listing of Perl Functions</h3>
<dl>
<dt>-X <font SIZE="-1">FILEHANDLE</font></p>
<dd>
<dt>-X <font SIZE="-1">EXPR</font></p>
<dd>
<dt>-X <font SIZE="-1">DIRHANDLE</font></p>
<dd>
<dt>-X</p>
<dd> A file test, where X is one of the letters listed below. This unary operator takes one argument, either a filename, a filehandle, or a dirhandle, and tests the associated file to see if something is true about it. If the argument is omitted, tests <tt>$_</tt>, except for <tt>&quot;-t&quot;</tt>, which tests <font SIZE="-1">STDIN.</font> Unless otherwise documented, it returns <tt>1</tt> for true and <tt>''</tt> for false. If the file doesn&#8217;t exist or can&#8217;t be examined, it returns <tt>&quot;undef&quot;</tt> and sets <tt>$!</tt> (errno). With the exception of the <tt>&quot;-l&quot;</tt> test they all follow symbolic links because they use <tt>&quot;stat()&quot;</tt> and not <tt>&quot;lstat()&quot;</tt> (so dangling symlinks can&#8217;t be examined and will therefore report failure). </p>
<p> Despite the funny names, precedence is the same as any other named unary operator. The operator may be any of: </p>
<p>    -r  File is readable by effective uid/gid.<br />
    -w  File is writable by effective uid/gid.<br />
    -x  File is executable by effective uid/gid.<br />
    -o  File is owned by effective uid.<br />
    -R  File is readable by real uid/gid.<br />
    -W  File is writable by real uid/gid.<br />
    -X  File is executable by real uid/gid.<br />
    -O  File is owned by real uid.<br />
    -e  File exists.<br />
    -z  File has zero size (is empty).<br />
    -s  File has nonzero size (returns size in bytes).<br />
    -f  File is a plain file.<br />
    -d  File is a directory.<br />
    -l  File is a symbolic link (false if symlinks aren&#8217;t<br />
        supported by the file system).<br />
    -p  File is a named pipe (FIFO), or Filehandle is a pipe.<br />
    -S  File is a socket.<br />
    -b  File is a block special file.<br />
    -c  File is a character special file.<br />
    -t  Filehandle is opened to a tty.<br />
    -u  File has setuid bit set.<br />
    -g  File has setgid bit set.<br />
    -k  File has sticky bit set.<br />
    -T  File is an ASCII or UTF-8 text file (heuristic guess).<br />
    -B  File is a &#8220;binary&#8221; file (opposite of -T).<br />
    -M  Script start time minus file modification time, in days.<br />
    -A  Same for access time.<br />
    -C  Same for inode change time (Unix, may differ for other<br />
        platforms)</p>
<p> Example: </p>
<p>while (&lt;&gt;) {<br />
    chomp;<br />
    next unless &#8211; f $_;<br />
#ignore specials<br />
#&#8230;<br />
}</p>
<p> Note that <tt>&quot;-s/a/b/&quot;</tt> does not do a negated substitution. Saying <tt>&quot;-exp($foo)&quot;</tt> still works as expected, however: only single letters following a minus are interpreted as file tests. </p>
<p> These operators are exempt from the &#8220;looks like a function rule&#8221; described above. That is, an opening parenthesis after the operator does not affect how much of the following code constitutes the argument. Put the opening parentheses before the operator to separate it from code that follows (this applies only to operators with higher precedence than unary operators, of course): </p>
<pre>
    -s($file) + 1024   # probably wrong; same as -s($file + 1024)
    (-s $file) + 1024  # correct
</pre>
<p> The interpretation of the file permission operators <tt>&quot;-r&quot;</tt>, <tt>&quot;-R&quot;</tt>, <tt>&quot;-w&quot;</tt>, <tt>&quot;-W&quot;</tt>, <tt>&quot;-x&quot;</tt>, and <tt>&quot;-X&quot;</tt> is by default based solely on the mode of the file and the uids and gids of the user. There may be other reasons you can&#8217;t actually read, write, or execute the file: for example network filesystem access controls, ACLs (access control lists), read-only filesystems, and unrecognized executable formats. Note that the use of these six specific operators to verify if some operation is possible is usually a mistake, because it may be open to race conditions. </p>
<p> Also note that, for the superuser on the local filesystems, the <tt>&quot;-r&quot;</tt>, <tt>&quot;-R&quot;</tt>, <tt>&quot;-w&quot;</tt>, and <tt>&quot;-W&quot;</tt> tests always return 1, and <tt>&quot;-x&quot;</tt> and <tt>&quot;-X&quot;</tt> return 1 if any execute bit is set in the mode. Scripts run by the superuser may thus need to do a <tt>&quot;stat&quot;</tt> to determine the actual mode of the file, or temporarily set their effective uid to something else. </p>
<p> If you are using ACLs, there is a pragma called <tt>&quot;filetest&quot;</tt> that may produce more accurate results than the bare <tt>&quot;stat&quot;</tt> mode bits. When under <tt>&quot;use filetest 'access'&quot;</tt>, the above-mentioned filetests test whether the permission can(not) be granted using the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) family of system calls. Also note that the <tt>&quot;-x&quot;</tt> and <tt>&quot;-X&quot;</tt> tests may under this pragma return true even if there are no execute permission bits set (nor any extra execute permission ACLs). This strangeness is due to the underlying system calls&#8217; definitions. Note also that, due to the implementation of <tt>&quot;use filetest 'access'&quot;</tt>, the <tt>&quot;_&quot;</tt> special filehandle won&#8217;t cache the results of the file tests when this pragma is in effect. Read the documentation for the <tt>&quot;filetest&quot;</tt> pragma for more information. </p>
<p> The <tt>&quot;-T&quot;</tt> and <tt>&quot;-B&quot;</tt> tests work as follows. The first block or so of the file is examined to see if it is valid <font SIZE="-1">UTF-8</font> that includes non-ASCII characters. If so, it&#8217;s a <tt>&quot;-T&quot;</tt> file. Otherwise, that same portion of the file is examined for odd characters such as strange control codes or characters with the high bit set. If more than a third of the characters are strange, it&#8217;s a <tt>&quot;-B&quot;</tt> file; otherwise it&#8217;s a <tt>&quot;-T&quot;</tt> file. Also, any file containing a zero byte in the examined portion is considered a binary file. (If executed within the scope of a use locale which includes <tt>&quot;LC_CTYPE&quot;</tt>, odd characters are anything that isn&#8217;t a printable nor space in the current locale.) If <tt>&quot;-T&quot;</tt> or <tt>&quot;-B&quot;</tt> is used on a filehandle, the current <font SIZE="-1">IO</font> buffer is examined rather than the first block. Both <tt>&quot;-T&quot;</tt> and <tt>&quot;-B&quot;</tt> return true on an empty file, or a file at <font SIZE="-1">EOF</font> when testing a filehandle. Because you have to read a file to do the <tt>&quot;-T&quot;</tt> test, on most occasions you want to use a <tt>&quot;-f&quot;</tt> against the file first, as in <tt>&quot;next unless -f $file &amp;&amp; -T $file&quot;</tt>. </p>
<p> If any of the file tests (or either the <tt>&quot;stat&quot;</tt> or <tt>&quot;lstat&quot;</tt> operator) is given the special filehandle consisting of a solitary underline, then the stat structure of the previous file test (or <tt>&quot;stat&quot;</tt> operator) is used, saving a system call. (This doesn&#8217;t work with <tt>&quot;-t&quot;</tt>, and you need to remember that <tt>&quot;lstat&quot;</tt> and <tt>&quot;-l&quot;</tt> leave values in the stat structure for the symbolic link, not the real file.) (Also, if the stat buffer was filled by an <tt>&quot;lstat&quot;</tt> call, <tt>&quot;-T&quot;</tt> and <tt>&quot;-B&quot;</tt> will reset it with the results of <tt>&quot;stat _&quot;</tt>). Example: </p>
<p>print &#8220;Can do.
&#8221; if &#8211; r $a || -w _ || -x _;<br />
stat($filename);<br />
print &#8220;Readable
&#8221; if &#8211; r _;<br />
print &#8220;Writable
&#8221; if &#8211; w _;<br />
print &#8220;Executable
&#8221; if &#8211; x _;<br />
print &#8220;Setuid
&#8221; if &#8211; u _;<br />
print &#8220;Setgid
&#8221; if &#8211; g _;<br />
print &#8220;Sticky
&#8221; if &#8211; k _;<br />
print &#8220;Text
&#8221; if &#8211; T _;<br />
print &#8220;Binary
&#8221; if &#8211; B _;</p>
<p> As of Perl 5.10.0, as a form of purely syntactic sugar, you can stack file test operators, in a way that <tt>&quot;-f -w -x $file&quot;</tt> is equivalent to <tt>&quot;-x $file &amp;&amp; -w _ &amp;&amp; -f _&quot;</tt>. (This is only fancy syntax: if you use the return value of <tt>&quot;-f $file&quot;</tt> as an argument to another filetest operator, no special magic will happen.) </p>
<p> Portability issues: &#8220;-X&#8221; in perlport. </p>
<p> To avoid confusing would-be users of your code with mysterious syntax errors, put something like this at the top of your script: </p>
<pre>
    use 5.010;  # so filetest ops can stack
</pre>
<dt>abs <font SIZE="-1">VALUE</font></p>
<dd>
<dt>abs</p>
<dd> Returns the absolute value of its argument. If <font SIZE="-1">VALUE</font> is omitted, uses <tt>$_</tt>.</p>
<dt>accept <font SIZE="-1">NEWSOCKET,GENERICSOCKET</font></p>
<dd> Accepts an incoming socket connect, just as <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2) does. Returns the packed address if it succeeded, false otherwise. See the example in &#8220;Sockets: Client/Server Communication&#8221; in perlipc. </p>
<p> On systems that support a close-on-exec flag on files, the flag will be set for the newly opened file descriptor, as determined by the value of <tt>$^F</tt>. See &#8220;$^F&#8221; in perlvar.</p>
<dt>alarm <font SIZE="-1">SECONDS</font></p>
<dd>
<dt>alarm</p>
<dd> Arranges to have a <font SIZE="-1">SIGALRM</font> delivered to this process after the specified number of wallclock seconds has elapsed. If <font SIZE="-1">SECONDS</font> is not specified, the value stored in <tt>$_</tt> is used. (On some machines, unfortunately, the elapsed time may be up to one second less or more than you specified because of how seconds are counted, and process scheduling may delay the delivery of the signal even further.) </p>
<p> Only one timer may be counting at once. Each call disables the previous timer, and an argument of <tt>0</tt> may be supplied to cancel the previous timer without starting a new one. The returned value is the amount of time remaining on the previous timer. </p>
<p> For delays of finer granularity than one second, the Time::HiRes module (from <font SIZE="-1">CPAN,</font> and starting from Perl 5.8 part of the standard distribution) provides <tt>&quot;ualarm&quot;</tt>. You may also use Perl&#8217;s four-argument version of <tt>&quot;select&quot;</tt> leaving the first three arguments undefined, or you might be able to use the <tt>&quot;syscall&quot;</tt> interface to access <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) if your system supports it. See perlfaq8 for details. </p>
<p> It is usually a mistake to intermix <tt>&quot;alarm&quot;</tt> and <tt>&quot;sleep&quot;</tt> calls, because <tt>&quot;sleep&quot;</tt> may be internally implemented on your system with <tt>&quot;alarm&quot;</tt>. </p>
<p> If you want to use <tt>&quot;alarm&quot;</tt> to time out a system call you need to use an <tt>&quot;eval&quot;</tt>/<tt>&quot;die&quot;</tt> pair. You can&#8217;t rely on the alarm causing the system call to fail with <tt>$!</tt> set to <tt>&quot;EINTR&quot;</tt> because Perl sets up signal handlers to restart system calls on some systems. Using <tt>&quot;eval&quot;</tt>/<tt>&quot;die&quot;</tt> always works, modulo the caveats given in &#8220;Signals&#8221; in perlipc. </p>
<p>eval<br />
{<br />
    local $SIG{ALRM} = sub{die &#8220;alarm
&#8221;};<br />
#NB : 
 required<br />
        alarm $timeout;<br />
    my $nread = sysread $socket, $buffer, $size;<br />
    alarm 0;<br />
};<br />
if ($ @) {<br />
    die unless $ @eq &#8220;alarm
&#8221;;<br />
#propagate unexpected errors<br />
#timed out<br />
} else {<br />
#didn&#8217;t<br />
}</p>
<p> For more information see perlipc. </p>
<p> Portability issues: &#8220;alarm&#8221; in perlport.</p>
<dt>atan2 Y,X</p>
<dd> Returns the arctangent of Y/X in the range -PI to <font SIZE="-1">PI.</font> </p>
<p> For the tangent operation, you may use the <tt>&quot;Math::Trig::tan&quot;</tt> function, or use the familiar relation: </p>
<p>sub tan<br />
{<br />
    sin($_[0]) / cos($_[0])<br />
}</p>
<p> The return value for <tt>&quot;atan2(0,0)&quot;</tt> is implementation-defined; consult your <code><a href="/docs/linux/man/3-atan2/">atan2</a></code>(3) manpage for more information. </p>
<p> Portability issues: &#8220;atan2&#8221; in perlport.</p>
<dt>bind <font SIZE="-1">SOCKET,NAME</font></p>
<dd> Binds a network address to a socket, just as <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) does. Returns true if it succeeded, false otherwise. <font SIZE="-1">NAME</font> should be a packed address of the appropriate type for the socket. See the examples in &#8220;Sockets: Client/Server Communication&#8221; in perlipc.</p>
<dt>binmode <font SIZE="-1">FILEHANDLE, LAYER</font></p>
<dd>
<dt>binmode <font SIZE="-1">FILEHANDLE</font></p>
<dd> Arranges for <font SIZE="-1">FILEHANDLE</font> to be read or written in &#8220;binary&#8221; or &#8220;text&#8221; mode on systems where the run-time libraries distinguish between binary and text files. If <font SIZE="-1">FILEHANDLE</font> is an expression, the value is taken as the name of the filehandle. Returns true on success, otherwise it returns <tt>&quot;undef&quot;</tt> and sets <tt>$!</tt> (errno). </p>
<p> On some systems (in general, <font SIZE="-1">DOS-</font> and Windows-based systems) <tt>&quot;binmode&quot;</tt> is necessary when you&#8217;re not working with a text file. For the sake of portability it is a good idea always to use it when appropriate, and never to use it when it isn&#8217;t appropriate. Also, people can set their I/O to be by default UTF8-encoded Unicode, not bytes. </p>
<p> In other words: regardless of platform, use <tt>&quot;binmode&quot;</tt> on binary data, like images, for example. </p>
<p> If <font SIZE="-1">LAYER</font> is present it is a single string, but may contain multiple directives. The directives alter the behaviour of the filehandle. When <font SIZE="-1">LAYER</font> is present, using binmode on a text file makes sense. </p>
<p> If <font SIZE="-1">LAYER</font> is omitted or specified as <tt>&quot;:raw&quot;</tt> the filehandle is made suitable for passing binary data. This includes turning off possible <font SIZE="-1">CRLF</font> translation and marking it as bytes (as opposed to Unicode characters). Note that, despite what may be implied in <i>&#8220;Programming Perl&#8221;</i> (the Camel, 3rd edition) or elsewhere, <tt>&quot;:raw&quot;</tt> is <i>not</i> simply the inverse of <tt>&quot;:crlf&quot;</tt>. Other layers that would affect the binary nature of the stream are <i>also</i> disabled. See PerlIO, perlrun, and the discussion about the <font SIZE="-1">PERLIO</font> environment variable. </p>
<p> The <tt>&quot;:bytes&quot;</tt>, <tt>&quot;:crlf&quot;</tt>, <tt>&quot;:utf8&quot;</tt>, and any other directives of the form <tt>&quot;:...&quot;</tt>, are called I/O <i>layers</i>. The open pragma can be used to establish default I/O layers. </p>
<p> <i>The </i><font SIZE="-1"><i>LAYER</i></font><i> parameter of the </i>&quot;binmode&quot;<i> function is described as &#8220;</i><font SIZE="-1"><i>DISCIPLINE&#8221;</i></font><i> in &#8220;Programming Perl, 3rd Edition&#8221;. However, since the publishing of this book, by many known as &#8220;Camel </i><font SIZE="-1"><i>III&#8221;,</i></font><i> the consensus of the naming of this functionality has moved from &#8220;discipline&#8221; to &#8220;layer&#8221;. All documentation of this version of Perl therefore refers to &#8220;layers&#8221; rather than to &#8220;disciplines&#8221;. Now back to the regularly scheduled documentation&#8230;</i> </p>
<p> To mark <font SIZE="-1">FILEHANDLE</font> as <font SIZE="-1">UTF-8,</font> use <tt>&quot;:utf8&quot;</tt> or <tt>&quot;:encoding(UTF-8)&quot;</tt>. <tt>&quot;:utf8&quot;</tt> just marks the data as <font SIZE="-1">UTF-8</font> without further checking, while <tt>&quot;:encoding(UTF-8)&quot;</tt> checks the data for actually being valid <font SIZE="-1">UTF-8.</font> More details can be found in PerlIO::encoding. </p>
<p> In general, <tt>&quot;binmode&quot;</tt> should be called after <tt>&quot;open&quot;</tt> but before any I/O is done on the filehandle. Calling <tt>&quot;binmode&quot;</tt> normally flushes any pending buffered output data (and perhaps pending input data) on the handle. An exception to this is the <tt>&quot;:encoding&quot;</tt> layer that changes the default character encoding of the handle. The <tt>&quot;:encoding&quot;</tt> layer sometimes needs to be called in mid-stream, and it doesn&#8217;t flush the stream. <tt>&quot;:encoding&quot;</tt> also implicitly pushes on top of itself the <tt>&quot;:utf8&quot;</tt> layer because internally Perl operates on UTF8-encoded Unicode characters. </p>
<p> The operating system, device drivers, C libraries, and Perl run-time system all conspire to let the programmer treat a single character (<tt>&quot;
&quot;</tt>) as the line terminator, irrespective of external representation. On many operating systems, the native text file representation matches the internal representation, but on some platforms the external representation of <tt>&quot;
&quot;</tt> is made up of more than one character. </p>
<p> All variants of Unix, Mac <font SIZE="-1">OS</font> (old and new), and Stream_LF files on <font SIZE="-1">VMS</font> use a single character to end each line in the external representation of text (even though that single character is <font SIZE="-1">CARRIAGE RETURN</font> on old, pre-Darwin flavors of Mac <font SIZE="-1">OS,</font> and is <font SIZE="-1">LINE FEED</font> on Unix and most <font SIZE="-1">VMS</font> files). In other systems like <font SIZE="-1">OS/2, DOS,</font> and the various flavors of MS-Windows, your program sees a <tt>&quot;
&quot;</tt> as a simple <tt>&quot;
