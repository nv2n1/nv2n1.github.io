---
title: "python3m(1)"
name: "python3m"
section: "1"
letter: "p"
url: "/docs/linux/man/1-python3m/"
description: "python – an interpreted, interactive, object-oriented programming language"
---

<h2 class="name">NAME</h2>
<p> python &#8211; an interpreted, interactive, object-oriented programming language </p>
<h2>SYNOPSIS</h2>
<p> <code>python</code> [ <code>-B</code> ] [ <code>-b</code> ] [ <code>-d</code> ] [ <code>-E</code> ] [ <code>-h</code> ] [ <code>-i</code> ] [ <code>-I</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>-m</code> <i>module-name</i> ] [ <code>-q</code> ] [ <code>-O</code> ] [ <code>-OO</code> ] [ <code>-s</code> ] [ <code>-S</code> ] [ <code>-u</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>-v</code> ] [ <code>-V</code> ] [ <code>-W</code> <i>argument</i> ] [ <code>-x</code> ] [ [ <code>-X</code> <i>option</i> ] <code>-?</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>-c</code> <i>command</i> | <i>script</i> | &#8211; ] [ <i>arguments</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax. For an introduction to programming in Python, see the Python Tutorial. The Python Library Reference documents built-in and standard types, constants, functions and modules. Finally, the Python Reference Manual describes the syntax and semantics of the core language in (perhaps too) much detail. (These documents may be located via the <code>INTERNET RESOURCES</code> below; they may be installed on your system as well.) </p>
<p> Python&#8217;s basic power can be extended with your own modules written in C or C++. On most systems such modules may be dynamically loaded. Python is also adaptable as an extension language for existing applications. See the internal documentation for hints. </p>
<p> Documentation for installed Python modules and packages can be viewed by running the <code>pydoc</code> program.</p>
<h2>COMMAND LINE OPTIONS</h2>
<dl>
<dt><code>-B</code></p>
<dd> Don&#8217;t write <i>.pyc</i> files on import. See also PYTHONDONTWRITEBYTECODE.</p>
<dt><code>-b</code></p>
<dd> Issue warnings about str(bytes_instance), str(bytearray_instance) and comparing bytes/bytearray with str. (-bb: issue errors)</p>
<dt><code>-c </code><i>command</i></p>
<dd> Specify the command to execute (see next section). This terminates the option list (following options are passed as arguments to the command).</p>
<dt><code>-d</code></p>
<dd> Turn on parser debugging output (for wizards only, depending on compilation options).</p>
<dt><code>-E</code></p>
<dd> Ignore environment variables like PYTHONPATH and PYTHONHOME that modify the behavior of the interpreter.</p>
<dt><code>-h , -? , &#8211;help</code></p>
<dd> Prints the usage for the interpreter executable and exits.</p>
<dt><code>-i</code></p>
<dd> When a script is passed as first argument or the <code>-c</code> option is used, enter interactive mode after executing the script or the command. It does not read the $PYTHONSTARTUP file. This can be useful to inspect global variables or a stack trace when a script raises an exception.</p>
<dt><code>-I</code></p>
<dd> Run Python in isolated mode. This also implies <code>-E</code> and <code>-s</code>. In isolated mode sys.path contains neither the script&#8217;s directory nor the user&#8217;s site-packages directory. All PYTHON* environment variables are ignored, too. Further restrictions may be imposed to prevent the user from injecting malicious code.</p>
<dt><code>-m </code><i>module-name</i></p>
<dd> Searches <i>sys.path</i> for the named module and runs the corresponding <i>.py</i> file as a script.</p>
<dt><code>-O</code></p>
<dd> Remove assert statements and any code conditional on the value of __debug__; augment the filename for compiled (bytecode) files by adding .opt-1 before the .pyc extension.</p>
<dt><code>-OO</code></p>
<dd> Do <code>-O</code> and also discard docstrings; change the filename for compiled (bytecode) files by adding .opt-2 before the .pyc extension.</p>
<dt><code>-q</code></p>
<dd> Do not print the version and copyright messages. These messages are also suppressed in non-interactive mode.</p>
<dt><code>-s</code></p>
<dd> Don&#8217;t add user site directory to sys.path.</p>
<dt><code>-S</code></p>
<dd> Disable the import of the module <i>site</i> and the site-dependent manipulations of <i>sys.path</i> that it entails. Also disable these manipulations if <i>site</i> is explicitly imported later.</p>
<dt><code>-u</code></p>
<dd> Force the binary I/O layers of stdout and stderr to be unbuffered. stdin is always buffered. The text I/O layer will still be line-buffered.</p>
<dt><code>-v</code></p>
<dd> Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. When given twice, print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.</p>
<dt><code>-V , &#8211;version</code></p>
<dd> Prints the Python version number of the executable and exits. When given twice, print more information about the build.</p>
<dt><code>-W </code><i>argument</i></p>
<dd> Warning control. Python sometimes prints warning message to <i>sys.stderr</i>. A typical warning message has the following form: <i>file</i><code>:</code><i>line</i><code>: </code><i>category</i><code>: </code><i>message.</i> By default, each warning is printed once for each source line where it occurs. This option controls how often warnings are printed. Multiple <code>-W</code> options may be given; when a warning matches more than one option, the action for the last matching option is performed. Invalid <code>-W</code> options are ignored (a warning message is printed about invalid options when the first warning is issued). Warnings can also be controlled from within a Python program using the <i>warnings</i> module. </p>
<p> The simplest form of <i>argument</i> is one of the following <i>action</i> strings (or a unique abbreviation): <code>ignore</code> to ignore all warnings; <code>default</code> to explicitly request the default behavior (printing each warning once per source line); <code>all</code> to print a warning each time it occurs (this may generate many messages if a warning is triggered repeatedly for the same source line, such as inside a loop); <code>module</code> to print each warning only the first time it occurs in each module; <code>once</code> to print each warning only the first time it occurs in the program; or <code>error</code> to raise an exception instead of printing a warning message. </p>
<p> The full form of <i>argument</i> is <i>action</i><code>:</code><i>message</i><code>:</code><i>category</i><code>:</code><i>module</i><code>:</code><i>line.</i> Here, <i>action</i> is as explained above but only applies to messages that match the remaining fields. Empty fields match all values; trailing empty fields may be omitted. The <i>message</i> field matches the start of the warning message printed; this match is case-insensitive. The <i>category</i> field matches the warning category. This must be a class name; the match test whether the actual warning category of the message is a subclass of the specified warning category. The full class name must be given. The <i>module</i> field matches the (fully-qualified) module name; this match is case-sensitive. The <i>line</i> field matches the line number, where zero matches all line numbers and is thus equivalent to an omitted line number.</p>
<dt><code>-X </code><i>option</i></p>
<dd> Set implementation specific option.</p>
<dt><code>-x</code></p>
<dd> Skip the first line of the source. This is intended for a DOS specific hack only. Warning: the line numbers in error messages will be off by one!</dl>
<h2>INTERPRETER INTERFACE</h2>
<p> The interpreter interface resembles that of the UNIX shell: when called with standard input connected to a tty device, it prompts for commands and executes them until an EOF is read; when called with a file name argument or with a file as standard input, it reads and executes a <i>script</i> from that file; when called with <code>-c</code> <i>command</i>, it executes the Python statement(s) given as <i>command</i>. Here <i>command</i> may contain multiple statements separated by newlines. Leading whitespace is significant in Python statements! In non-interactive mode, the entire input is parsed before it is executed. </p>
<p> If available, the script name and additional arguments thereafter are passed to the script in the Python variable <i>sys.argv</i>, which is a list of strings (you must first <i>import sys</i> to be able to access it). If no script name is given, <i>sys.argv[0]</i> is an empty string; if <code>-c</code> is used, <i>sys.argv[0]</i> contains the string <i>&#8216;-c&#8217;.</i> Note that options interpreted by the Python interpreter itself are not placed in <i>sys.argv</i>. </p>
<p> In interactive mode, the primary prompt is `&gt;&gt;&gt;&#8217;; the second prompt (which appears when a command is not complete) is `&#8230;&#8217;. The prompts can be changed by assignment to <i>sys.ps1</i> or <i>sys.ps2</i>. The interpreter quits when it reads an EOF at a prompt. When an unhandled exception occurs, a stack trace is printed and control returns to the primary prompt; in non-interactive mode, the interpreter exits after printing the stack trace. The interrupt signal raises the <i>KeyboardInterrupt</i> exception; other UNIX signals are not caught (except that SIGPIPE is sometimes ignored, in favor of the <i>IOError</i> exception). Error messages are written to stderr.</p>
<h2>FILES AND DIRECTORIES</h2>
<p> These are subject to difference depending on local installation conventions; ${prefix} and ${exec_prefix} are installation-dependent and should be interpreted as for GNU software; they may be the same. On Debian GNU/{Hurd,Linux} the default for both is <i>/usr</i>.</p>
<dl>
<dt><i>${exec_prefix}/bin/python</i></p>
<dd> Recommended location of the interpreter.</dl>
<p> <i>${prefix}/lib/python&lt;version&gt;</i><br />
 <i>${exec_prefix}/lib/python&lt;version&gt;</i></p>
<dl>
<dt>
<dd> Recommended locations of the directories containing the standard modules.</dl>
<p> <i>${prefix}/include/python&lt;version&gt;</i><br />
 <i>${exec_prefix}/include/python&lt;version&gt;</i></p>
<dl>
<dt>
<dd> Recommended locations of the directories containing the include files needed for developing Python extensions and embedding the interpreter.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>PYTHONHOME</p>
<dd> Change the location of the standard Python libraries. By default, the libraries are searched in ${prefix}/lib/python&lt;version&gt; and ${exec_prefix}/lib/python&lt;version&gt;, where ${prefix} and ${exec_prefix} are installation-dependent directories, both defaulting to <i>/usr/local</i>. When $PYTHONHOME is set to a single directory, its value replaces both ${prefix} and ${exec_prefix}. To specify different values for these, set $PYTHONHOME to ${prefix}:${exec_prefix}.</p>
<dt>PYTHONPATH</p>
<dd> Augments the default search path for module files. The format is the same as the shell&#8217;s $PATH: one or more directory pathnames separated by colons. Non-existent directories are silently ignored. The default search path is installation dependent, but generally begins with ${prefix}/lib/python&lt;version&gt; (see PYTHONHOME above). The default search path is always appended to $PYTHONPATH. If a script argument is given, the directory containing the script is inserted in the path in front of $PYTHONPATH. The search path can be manipulated from within a Python program as the variable <i>sys.path</i>.</p>
<dt>PYTHONSTARTUP</p>
<dd> If this is the name of a readable file, the Python commands in that file are executed before the first prompt is displayed in interactive mode. The file is executed in the same name space where interactive commands are executed so that objects defined or imported in it can be used without qualification in the interactive session. You can also change the prompts <i>sys.ps1</i> and <i>sys.ps2</i> in this file.</p>
<dt>PYTHONOPTIMIZE</p>
<dd> If this is set to a non-empty string it is equivalent to specifying the <code>-O</code> option. If set to an integer, it is equivalent to specifying <code>-O</code> multiple times.</p>
<dt>PYTHONDEBUG</p>
<dd> If this is set to a non-empty string it is equivalent to specifying the <code>-d</code> option. If set to an integer, it is equivalent to specifying <code>-d</code> multiple times.</p>
<dt>PYTHONDONTWRITEBYTECODE</p>
<dd> If this is set to a non-empty string it is equivalent to specifying the <code>-B</code> option (don&#8217;t try to write <i>.pyc</i> files).</p>
<dt>PYTHONINSPECT</p>
<dd> If this is set to a non-empty string it is equivalent to specifying the <code>-i</code> option.</p>
<dt>PYTHONIOENCODING</p>
<dd> If this is set before running the interpreter, it overrides the encoding used for stdin/stdout/stderr, in the syntax <i>encodingname</i><code>:</code><i>errorhandler</i> The <i>errorhandler</i> part is optional and has the same meaning as in str.encode. For stderr, the <i>errorhandler</i><br />
&nbsp;part is ignored;&nbsp;the handler will always be&nbsp;&#8216;backslashreplace&#8217;.</p>
<dt>PYTHONNOUSERSITE</p>
<dd> If this is set to a non-empty string it is equivalent to specifying the <code>-s</code> option (Don&#8217;t add the user site directory to sys.path).</p>
<dt>PYTHONUNBUFFERED</p>
<dd> If this is set to a non-empty string it is equivalent to specifying the <code>-u</code> option.</p>
<dt>PYTHONVERBOSE</p>
<dd> If this is set to a non-empty string it is equivalent to specifying the <code>-v</code> option. If set to an integer, it is equivalent to specifying <code>-v</code> multiple times.</p>
<dt>PYTHONWARNINGS</p>
<dd> If this is set to a comma-separated string it is equivalent to specifying the <code>-W</code> option for each separate value.</p>
<dt>PYTHONHASHSEED</p>
<dd> If this variable is set to &quot;random&quot;, a random value is used to seed the hashes of str, bytes and datetime objects. </p>
<p> If PYTHONHASHSEED is set to an integer value, it is used as a fixed seed for generating the hash() of the types covered by the hash randomization. Its purpose is to allow repeatable hashing, such as for selftests for the interpreter itself, or to allow a cluster of python processes to share hash values. </p>
<p> The integer must be a decimal number in the range [0,4294967295]. Specifying the value 0 will disable hash randomization.</dl>
<h2>AUTHOR</h2>
<p> The Python Software Foundation: <a rel="nofollow" href="https://www.python.org/psf/">https://www.python.org/psf/</a></p>
<h2>INTERNET RESOURCES</h2>
<p> Main website: <a rel="nofollow" href="https://www.python.org/">https://www.python.org/</a><br />
 Documentation: <a rel="nofollow" href="https://docs.python.org/">https://docs.python.org/</a><br />
 Developer resources: <a rel="nofollow" href="https://devguide.python.org/">https://devguide.python.org/</a><br />
 Downloads: <a rel="nofollow" href="https://www.python.org/downloads/">https://www.python.org/downloads/</a><br />
 Module repository: <a rel="nofollow" href="https://pypi.org/">https://pypi.org/</a><br />
 Newsgroups: comp.lang.python, comp.lang.python.announce</p>
<h2>LICENSING</h2>
<p> Python is distributed under an Open Source license. See the file &quot;LICENSE&quot; in the Python source distribution for information on terms &amp; conditions for accessing and otherwise using Python and for a DISCLAIMER OF ALL WARRANTIES. </p>
<h2>Index</h2>
