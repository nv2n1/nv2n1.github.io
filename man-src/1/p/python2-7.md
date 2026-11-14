---
title: "python2-7(1)"
name: "python2-7"
section: "1"
letter: "p"
url: "/docs/linux/man/1-python2-7/"
description: "python – an interpreted, interactive, object-oriented programming language"
---

<p>python &#8211; an interpreted, interactive, object-oriented programming language </p>
<h2>Synopsis</h2>
<p><code>python</code> [ <code>-B</code> ] [ <code>-d</code> ] [ <code>-E</code> ] [ <code>-h</code> ] [ <code>-i</code> ] [ <code>-m </code> <i>module-name</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>-O</code> ] [ <code>-OO</code> ] [ <code>-R</code> ] [ <code>-Q</code> <i>argument</i> ] [ <code>-s</code> ] [ <code>-S</code> ] [ <code>-t</code> ] [ <code>-u</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>-v</code> ] [ <code>-V</code> ] [ <code>-W</code> <i>argument</i> ] [ <code>-x</code> ] [ <code>-3</code> ] [ <code>-?</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>-c</code> <i>command</i> | <i>script</i> | &#8211; ] [ <i>arguments</i> ]</p>
<h2>Description</h2>
<p>Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax. For an introduction to programming in Python, see the Python Tutorial. The Python Library Reference documents built-in and standard types, constants, functions and modules. Finally, the Python Reference Manual describes the syntax and semantics of the core language in (perhaps too) much detail. (These documents may be located via the <code>INTERNET RESOURCES</code> below; they may be installed on your system as well.) </p>
<p> Python&#8217;s basic power can be extended with your own modules written in C or C++. On most systems such modules may be dynamically loaded. Python is also adaptable as an extension language for existing applications. See the internal documentation for hints. </p>
<p> Documentation for installed Python modules and packages can be viewed by running the <code>pydoc</code> program.</p>
<h2>Command Line Options</h2>
<dl COMPACT>
<dt><code>-B</code></p>
<dd>Don&#8217;t write <i>.py[co]</i> files on import. See also PYTHONDONTWRITEBYTECODE.</p>
<dt><code>-c </code><i>command</i></p>
<dd>Specify the command to execute (see next section). This terminates the option list (following options are passed as arguments to the command).</p>
<dt><code>-d</code></p>
<dd>Turn on parser debugging output (for wizards only, depending on compilation options).</p>
<dt><code>-E</code></p>
<dd>Ignore environment variables like PYTHONPATH and PYTHONHOME that modify the behavior of the interpreter.</p>
<dt><code>-h , -? , &#8211;help</code></p>
<dd>Prints the usage for the interpreter executable and exits.</p>
<dt><code>-i</code></p>
<dd>When a script is passed as first argument or the <code>-c</code> option is used, enter interactive mode after executing the script or the command. It does not read the $PYTHONSTARTUP file. This can be useful to inspect global variables or a stack trace when a script raises an exception.</p>
<dt><code>-m </code><i>module-name</i></p>
<dd>Searches <i>sys.path </i> for the named module and runs the corresponding <i>.py </i> file as a script.</p>
<dt><code>-O</code></p>
<dd>Turn on basic optimizations. This changes the filename extension for compiled (bytecode) files from <i>.pyc</i> to <i>.pyo</i>. Given twice, causes docstrings to be discarded.</p>
<dt><code>-OO</code></p>
<dd>Discard docstrings in addition to the <code>-O</code> optimizations.</p>
<dt><code>-R</code></p>
<dd>Turn on &quot;hash randomization&quot;, so that the hash() values of str, bytes and datetime objects are &quot;salted&quot; with an unpredictable pseudo-random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python.</p>
<dd>This is intended to provide protection against a denial of service caused by carefully-chosen inputs that exploit the worst case performance of a dict construction, O(n^2) complexity. See <a rel="nofollow" href="http://www.ocert.org/advisories/ocert-2011-003.html">http://www.ocert.org/advisories/ocert-2011-003.html</a> for details.</p>
<dt><code>-Q </code><i>argument</i></p>
<dd>Division control; see PEP 238. The argument must be one of &quot;old&quot; (the default, int/int and long/long return an int or long), &quot;new&quot; (new division semantics, i.e. int/int and long/long returns a float), &quot;warn&quot; (old division semantics with a warning for int/int and long/long), or &quot;warnall&quot; (old division semantics with a warning for all use of the division operator). For a use of &quot;warnall&quot;, see the Tools/scripts/fixdiv.py script.</p>
<dt><code>-s</code></p>
<dd>Don&#8217;t add user site directory to sys.path.</p>
<dt><code>-S</code></p>
<dd>Disable the import of the module <i>site</i> and the site-dependent manipulations of <i>sys.path</i> that it entails.</p>
<dt><code>-t</code></p>
<dd>Issue a warning when a source file mixes tabs and spaces for indentation in a way that makes it depend on the worth of a tab expressed in spaces. Issue an error when the option is given twice.</p>
<dt><code>-u</code></p>
<dd>Force stdin, stdout and stderr to be totally unbuffered. On systems where it matters, also put stdin, stdout and stderr in binary mode. Note that there is internal buffering in xreadlines(), readlines() and file-object iterators (&quot;for line in sys.stdin&quot;) which is not influenced by this option. To work around this, you will want to use &quot;sys.stdin.readline()&quot; inside a &quot;while 1:&quot; loop.</p>
<dt><code>-v</code></p>
<dd>Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. When given twice, print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.</p>
<dt><code>-V , &#8211;version</code></p>
<dd>Prints the Python version number of the executable and exits.</p>
<dt><code>-W </code><i>argument</i></p>
<dd>Warning control. Python sometimes prints warning message to <i>sys.stderr</i>. A typical warning message has the following form: <i>file</i><code>:</code><i>line</i><code>: </code><i>category</i><code>: </code><i>message.</i> By default, each warning is printed once for each source line where it occurs. This option controls how often warnings are printed. Multiple <code>-W</code> options may be given; when a warning matches more than one option, the action for the last matching option is performed. Invalid <code>-W</code> options are ignored (a warning message is printed about invalid options when the first warning is issued). Warnings can also be controlled from within a Python program using the <i>warnings</i> module. </p>
<p> The simplest form of <i>argument</i> is one of the following <i>action</i> strings (or a unique abbreviation): <code>ignore</code> to ignore all warnings; <code>default</code> to explicitly request the default behavior (printing each warning once per source line); <code>all</code> to print a warning each time it occurs (this may generate many messages if a warning is triggered repeatedly for the same source line, such as inside a loop); <code>module</code> to print each warning only the first time it occurs in each module; <code>once</code> to print each warning only the first time it occurs in the program; or <code>error</code> to raise an exception instead of printing a warning message. </p>
<p> The full form of <i>argument</i> is <i>action</i><code>:</code><i>message</i><code>:</code><i>category</i><code>:</code><i>module</i><code>:</code><i>line.</i> Here, <i>action</i> is as explained above but only applies to messages that match the remaining fields. Empty fields match all values; trailing empty fields may be omitted. The <i>message</i> field matches the start of the warning message printed; this match is case-insensitive. The <i>category</i> field matches the warning category. This must be a class name; the match test whether the actual warning category of the message is a subclass of the specified warning category. The full class name must be given. The <i>module</i> field matches the (fully-qualified) module name; this match is case-sensitive. The <i>line</i> field matches the line number, where zero matches all line numbers and is thus equivalent to an omitted line number.</p>
<dt><code>-x</code></p>
<dd>Skip the first line of the source. This is intended for a DOS specific hack only. Warning: the line numbers in error messages will be off by one!</p>
<dt><code>-3</code></p>
<dd>Warn about Python 3.x incompatibilities that 2to3 cannot trivially fix.</dl>
<h2>Interpreter Interface</h2>
<p>The interpreter interface resembles that of the UNIX shell: when called with standard input connected to a tty device, it prompts for commands and executes them until an EOF is read; when called with a file name argument or with a file as standard input, it reads and executes a <i>script</i> from that file; when called with <code>-c</code> <i>command</i>, it executes the Python statement(s) given as <i>command</i>. Here <i>command</i> may contain multiple statements separated by newlines. Leading whitespace is significant in Python statements! In non-interactive mode, the entire input is parsed before it is executed. </p>
<p> If available, the script name and additional arguments thereafter are passed to the script in the Python variable <i>sys.argv</i>, which is a list of strings (you must first <i>import sys</i> to be able to access it). If no script name is given, <i>sys.argv[0]</i> is an empty string; if <code>-c</code> is used, <i>sys.argv[0]</i> contains the string <i>&#8216;-c&#8217;.</i> Note that options interpreted by the Python interpreter itself are not placed in <i>sys.argv</i>. </p>
<p> In interactive mode, the primary prompt is `&gt;&gt;&gt;&#8217;; the second prompt (which appears when a command is not complete) is `&#8230;&#8217;. The prompts can be changed by assignment to <i>sys.ps1</i> or <i>sys.ps2</i>. The interpreter quits when it reads an EOF at a prompt. When an unhandled exception occurs, a stack trace is printed and control returns to the primary prompt; in non-interactive mode, the interpreter exits after printing the stack trace. The interrupt signal raises the <i>KeyboardInterrupt</i> exception; other UNIX signals are not caught (except that SIGPIPE is sometimes ignored, in favor of the <i>IOError</i> exception). Error messages are written to stderr.</p>
<h2>Files And Directories</h2>
<p>These are subject to difference depending on local installation conventions; ${prefix} and ${exec_prefix} are installation-dependent and should be interpreted as for GNU software; they may be the same. On Debian GNU/{Hurd,Linux} the default for both is <i>/usr</i>.</p>
<dl COMPACT>
<dt><i>${exec_prefix}/bin/python</i></p>
<dd>Recommended location of the interpreter.</dl>
<p> <i>${prefix}/lib/python&lt;version&gt;</i><br />
 <i>${exec_prefix}/lib/python&lt;version&gt;</i></p>
<dl COMPACT>
<dd>Recommended locations of the directories containing the standard modules.</dl>
<p> <i>${prefix}/include/python&lt;version&gt;</i><br />
 <i>${exec_prefix}/include/python&lt;version&gt;</i></p>
<dl COMPACT>
<dd>Recommended locations of the directories containing the include files needed for developing Python extensions and embedding the interpreter.</dl>
<dl COMPACT>
<dt><i>~/.pythonrc.py</i></p>
<dd>User-specific initialization file loaded by the <i>user</i> module; not used by default or by most applications.</dl>
<h2>Environment Variables</h2>
<dl COMPACT>
<dt>PYTHONHOME</p>
<dd>Change the location of the standard Python libraries. By default, the libraries are searched in ${prefix}/lib/python&lt;version&gt; and ${exec_prefix}/lib/python&lt;version&gt;, where ${prefix} and ${exec_prefix} are installation-dependent directories, both defaulting to <i>/usr/local</i>. When $PYTHONHOME is set to a single directory, its value replaces both ${prefix} and ${exec_prefix}. To specify different values for these, set $PYTHONHOME to ${prefix}:${exec_prefix}.</p>
<dt>PYTHONPATH</p>
<dd>Augments the default search path for module files. The format is the same as the shell&#8217;s $PATH: one or more directory pathnames separated by colons. Non-existent directories are silently ignored. The default search path is installation dependent, but generally begins with ${prefix}/lib/python&lt;version&gt; (see PYTHONHOME above). The default search path is always appended to $PYTHONPATH. If a script argument is given, the directory containing the script is inserted in the path in front of $PYTHONPATH. The search path can be manipulated from within a Python program as the variable <i>sys.path</i>.</p>
<dt>PYTHONSTARTUP</p>
<dd>If this is the name of a readable file, the Python commands in that file are executed before the first prompt is displayed in interactive mode. The file is executed in the same name space where interactive commands are executed so that objects defined or imported in it can be used without qualification in the interactive session. You can also change the prompts <i>sys.ps1</i> and <i>sys.ps2</i> in this file.</p>
<dt>PYTHONY2K</p>
<dd>Set this to a non-empty string to cause the <i>time</i> module to require dates specified as strings to include 4-digit years, otherwise 2-digit years are converted based on rules described in the <i>time</i> module documentation.</p>
<dt>PYTHONOPTIMIZE</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-O</code> option. If set to an integer, it is equivalent to specifying <code>-O</code> multiple times.</p>
<dt>PYTHONDEBUG</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-d</code> option. If set to an integer, it is equivalent to specifying <code>-d</code> multiple times.</p>
<dt>PYTHONDONTWRITEBYTECODE</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-B</code> option (don&#8217;t try to write <i>.py[co]</i> files).</p>
<dt>PYTHONINSPECT</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-i</code> option.</p>
<dt>PYTHONIOENCODING</p>
<dd>If this is set before running the interpreter, it overrides the encoding used for stdin/stdout/stderr, in the syntax <i>encodingname</i><code>:</code><i>errorhandler</i> The <i>errorhandler</i> part is optional and has the same meaning as in str.encode. For stderr, the <i>errorhandler</i><br />
&nbsp;part is ignored;&nbsp;the handler will always be&nbsp;&#8216;backslashreplace&#8217;.</p>
<dt>PYTHONNOUSERSITE</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-s</code> option (Don&#8217;t add the user site directory to sys.path).</p>
<dt>PYTHONUNBUFFERED</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-u</code> option.</p>
<dt>PYTHONVERBOSE</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-v</code> option. If set to an integer, it is equivalent to specifying <code>-v</code> multiple times.</p>
<dt>PYTHONWARNINGS</p>
<dd>If this is set to a comma-separated string it is equivalent to specifying the <code>-W</code> option for each separate value.</p>
<dt>PYTHONHASHSEED</p>
<dd>If this variable is set to &quot;random&quot;, the effect is the same as specifying the <code>-R</code> option: a random value is used to seed the hashes of str, bytes and datetime objects. </p>
<p> If PYTHONHASHSEED is set to an integer value, it is used as a fixed seed for generating the hash() of the types covered by the hash randomization. Its purpose is to allow repeatable hashing, such as for selftests for the interpreter itself, or to allow a cluster of python processes to share hash values. </p>
<p> The integer must be a decimal number in the range [0,4294967295]. Specifying the value 0 will lead to the same hash values as when hash randomization is disabled.</dl>
<h2>Author</h2>
<p>The Python Software Foundation: <a rel="nofollow" href="https://www.python.org/psf/">https://www.python.org/psf/</a></p>
<h2>Internet Resources</h2>
<p>Main website: <a rel="nofollow" href="https://www.python.org/">https://www.python.org/</a><br />
 Documentation: file:///usr/share/doc/python2.7/html/index.html (python-doc package) or <a rel="nofollow" href="https://docs.python.org/2/">https://docs.python.org/2/</a><br />
 Developer resources: <a rel="nofollow" href="https://docs.python.org/devguide/">https://docs.python.org/devguide/</a><br />
 Downloads: <a rel="nofollow" href="https://www.python.org/downloads/">https://www.python.org/downloads/</a><br />
 Module repository: <a rel="nofollow" href="https://pypi.python.org/">https://pypi.python.org/</a><br />
 Newsgroups: comp.lang.python, comp.lang.python.announce</p>
<h2>Licensing</h2>
<p>Python is distributed under an Open Source license. See the file &quot;LICENSE&quot; in the Python source distribution for information on terms &amp; conditions for accessing and otherwise using Python and for a DISCLAIMER OF ALL WARRANTIES.</p>
