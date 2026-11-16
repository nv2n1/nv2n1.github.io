---
title: "ruby2-5(1)"
name: "ruby2-5"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ruby2-5/"
description: "ruby – Interpreted object-oriented scripting language"
---

<p>UNIX</p>
<h2>Name</h2>
<p><code>ruby</code> &#8211; Interpreted object-oriented scripting language </p>
<h2>Synopsis</h2>
<p>[-<code>-copyright</code> ] [-<code>-version</code> ] [-<code>SUacdlnpswvy</code> ] [-<code>0 </code>[<i>octal</i> ] ] [-<code>C </code><i>directory</i> ] [-<code>E </code><i>external </i>[: <i>internal</i> ] ] [-<code>F </code>[<i>pattern</i> ] ] [-<code>I </code><i>directory</i> ] [-<code>K </code>[<i>c</i> ] ] [-<code>T </code>[<i>level</i> ] ] [-<code>W </code>[<i>level</i> ] ] [-<code>e </code><i>command</i> ] [-<code>i </code>[<i>extension</i> ] ] [-<code>r </code><i>library</i> ] [-<code>x </code>[<i>directory</i> ] ] [-<code>&#8211; Bro enable | disable Brc &#8211; </code><i>FEATURE</i> ] [-<code>-dump = </code><i>target</i> ] [-<code>-verbose</code> ] [- ] [<i>program_file</i> ] [<i>argument &#8230;</i> ]</p>
<h2>Description</h2>
<p>Ruby is an interpreted scripting language for quick and easy object-oriented programming. It has many features to process text files and to do system management tasks (like in Perl). It is simple, straight-forward, and extensible. </p>
<p> If you want a language for easy object-oriented programming, or you don&#8217;t like the Perl ugliness, or you do like the concept of LISP, but don&#8217;t like too many parentheses, Ruby might be your language of choice.</p>
<h2>Features</h2>
<p>Ruby&#8217;s features are as follows:</p>
<dl COMPACT>
<dt><code>Interpretive</code></dt>
<dd>Ruby is an interpreted language, so you don&#8217;t have to recompile programs written in Ruby to execute them. </dd>
<dt><code>Variables have no type (dynamic typing)</code></dt>
<dd>Variables in Ruby can contain data of any type. You don&#8217;t have to worry about variable typing. Consequently, it has a weaker compile time check. </dd>
<dt><code>declaration needed</code></dt>
<dd>You can use variables in your Ruby programs without any declarations. Variable names denote their scope &#8211; global, class, instance, or local. </dd>
<dt><code>Simple syntax</code></dt>
<dd>Ruby has a simple syntax influenced slightly from Eiffel. </dd>
<dt><code>user-level memory management</code></dt>
<dd>Ruby has automatic memory management. Objects no longer referenced from anywhere are automatically collected by the garbage collector built into the interpreter. </dd>
<dt><code>Everything is an object</code></dt>
<dd>Ruby is a purely object-oriented language, and was so since its creation. Even such basic data as integers are seen as objects. </dd>
<dt><code>Class, inheritance, and methods</code></dt>
<dd>Being an object-oriented language, Ruby naturally has basic features like classes, inheritance, and methods. </dd>
<dt><code>Singleton methods</code></dt>
<dd>Ruby has the ability to define methods for certain objects. For example, you can define a press-button action for certain widget by defining a singleton method for the button. Or, you can make up your own prototype based object system using singleton methods, if you want to. </dd>
<dt><code>Mix-in by modules</code></dt>
<dd>Ruby intentionally does not have the multiple inheritance as it is a source of confusion. Instead, Ruby has the ability to share implementations across the inheritance tree. This is often called a `Mix-in&#8217; </dd>
<dt><code>Iterators</code></dt>
<dd>Ruby has iterators for loop abstraction. </dd>
<dt><code>Closures</code></dt>
<dd>In Ruby, you can objectify the procedure. </dd>
<dt><code>Text processing and regular expressions</code></dt>
<dd>Ruby has a bunch of text processing features like in Perl. </dd>
<dt><code>M17N, character set independent</code></dt>
<dd>Ruby supports multilingualized programming. Easy to process texts written in many different natural languages and encoded in many different character encodings, without dependence on Unicode. </dd>
<dt><code>Bignums</code></dt>
<dd>With built-in bignums, you can for example calculate factorial(400). </dd>
<dt><code>Reflection and domain specific languages</code></dt>
<dd>Class is also an instance of the Class class. Definition of classes and methods is an expression just as 1+1 is. So your programs can even write and modify programs. Thus you can write your application in your own programming language on top of Ruby. </dd>
<dt><code>Exception handling</code></dt>
<dd>As in Java(tm). </dd>
<dt><code>Direct access to the OS</code></dt>
<dd>Ruby can use most UNIX system calls, often used in system programming. </dd>
<dt><code>Dynamic loading</code></dt>
<dd>On most UNIX systems, you can load object files into the Ruby interpreter on-the-fly.</dd>
<dt><code>Rich libraries</code></dt>
<dd>In addition to the &#8220;builtin libraries&#8221; and &#8220;standard libraries&#8221; that are bundled with Ruby, a vast amount of third-party libraries (&#8220;gems&#8221; ) are available via the package management system called `RubyGems&#8217; namely the <a href="/docs/linux/man/1-gem/">gem</a>(1) command. Visit RubyGems.org (Lk <a rel="nofollow" href="https://rubygems.org/">https://rubygems.org/</a> ) to find the gems you need, and explore GitHub (Lk <a rel="nofollow" href="https://github.com/">https://github.com/</a> ) to see how they are being developed and used.</dd></dl>
<h2>Options</h2>
<p>Ruby interpreter accepts following command-line options (switches). They are quite similar to those of <a href="/docs/linux/man/1-perl/">perl</a>(1).</p>
<dl COMPACT>
<dt><code>&#8211;copyright</code></dt>
<dd>Prints the copyright notice. </dd>
<dt><code>&#8211;version</code></dt>
<dd>Prints the version of Ruby interpreter. </dd>
<dt><code>-0 </code>[<i>octal</i> ]</dt>
<dd>(The digit &#8220;zero .&#8221; Specifies the input record separator ( <code>$/</code> as an octal number. If no digit is given, the null character is taken as the separator. Other switches may follow the digits. &#8211;<code>00</code> turns Ruby into paragraph mode. &#8211;<code>0777</code> makes Ruby read whole file at once as a single string since there is no legal character with that value. </dd>
<dt><code>-C </code><i>directory</i></dt>
<dd>
</dd><dt><code>-X </code><i>directory</i></dt>
<dd>Causes Ruby to switch to the directory. </dd>
<dt><code>-E </code><i>external </i>[: <i>internal</i> ]</dt>
<dd>
</dd><dt><code>&#8211;encoding </code><i>external </i>[: <i>internal</i> ]</dt>
<dd>Specifies the default value(s) for external encodings and internal encoding. Values should be separated with colon (:). </dd>
<p> You can omit the one for internal encodings, then the value ( <code>Encoding.default_internal ) will be nil.</code> </p>
<dt><code>&#8211;external-encoding = </code><i>encoding</i></dt>
<dd>
</dd><dt><code>&#8211;internal-encoding = </code><i>encoding</i></dt>
<dd>Specify the default external or internal character encoding </dd>
<dt><code>-F </code><i>pattern</i></dt>
<dd>Specifies input field separator ( <code>$;</code> </dd>
<dt><code>-I </code><i>directory</i></dt>
<dd>Used to tell Ruby where to load the library scripts. Directory path will be added to the load-path variable ( <code>$:</code> </dd>
<dt><code>-K </code><i>kcode</i></dt>
<dd>Specifies KANJI (Japanese) encoding. The default value for script encodings ( <code>__ENCODING__ ) and external encodings ( Encoding.default_external ) will be the specified one.</code> <i>kcode</i> can be one of</dd>
<dl COMPACT>
<dt><code>e</code></dt>
<dd>EUC-JP </dd>
<dt><code>s</code></dt>
<dd>Windows-31J (CP932) </dd>
<dt><code>u</code></dt>
<dd>UTF-8 </dd>
<dt><code>n</code></dt>
<dd>ASCII-8BIT (BINARY)</dd></dl>
<dt><code>-S</code></dt>
<dd>Makes Ruby use the <code>PATH</code> environment variable to search for script, unless its name begins with a slash. This is used to emulate <code>#!</code> on machines that don&#8217;t support it, in the following manner: </dd>
<blockquote>
<pre>#! /usr/local/bin/ruby
# This line makes the next one a comment in Ruby \
 exec /usr/local/bin/ruby -S $0 $*</pre>
</blockquote>
<p> On some systems <code>$0</code> does not always contain the full pathname, so you need the &#8211;<code>S</code> switch to tell Ruby to search for the script if necessary (to handle embedded spaces and such). A better construct than <code>$*</code> would be <code>${1+$@}</code> but it does not work if the script is being interpreted by <a href="/docs/linux/man/1-csh/">csh</a>(1). </p>
<dt><code>-T </code>[<i>level=1</i> ]</dt>
<dd>Turns on taint checks at the specified level (default 1). </dd>
<dt><code>-U</code></dt>
<dd>Sets the default value for internal encodings ( <code>Encoding.default_internal ) to UTF-8.</code> </dd>
<dt><code>-W </code>[<i>level=2</i> ]</dt>
<dd>Turns on verbose mode at the specified level without printing the version message at the beginning. The level can be;</dd>
<dl COMPACT>
<dt><code>0</code></dt>
<dd>Verbose mode is &quot;silence&quot;. It sets the <code>$VERBOSE</code> to nil. </dd>
<dt><code>1</code></dt>
<dd>Verbose mode is &quot;medium&quot;. It sets the <code>$VERBOSE</code> to false. </dd>
<dt><code>2 (default)</code></dt>
<dd>Verbose mode is &quot;verbose&quot;. It sets the <code>$VERBOSE</code> to true. &#8211;<code>W 2 is same as</code> &#8211;<code>w</code></dd></dl>
<dt><code>-a</code></dt>
<dd>Turns on auto-split mode when used with &#8211;<code>n</code> or &#8211;<code>p</code> In auto-split mode, Ruby executes </dd>
<blockquote><p><tt>$F = $_.split</tt></p></blockquote>
<p> at beginning of each loop. </p>
<dt><code>-c</code></dt>
<dd>Causes Ruby to check the syntax of the script and exit without executing. If there are no syntax errors, Ruby will print &#8220;Syntax OK&#8221; to the standard output. </dd>
<dt><code>-d</code></dt>
<dd>
</dd><dt><code>&#8211;debug</code></dt>
<dd>Turns on debug mode. <code>$DEBUG</code> will be set to true. </dd>
<dt><code>-e </code><i>command</i></dt>
<dd>Specifies script from command-line while telling Ruby not to search the rest of the arguments for a script file name. </dd>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd>Prints a summary of the options. </dd>
<dt><code>-i </code><i>extension</i></dt>
<dd>Specifies in-place-edit mode. The extension, if specified, is added to old file name to make a backup copy. For example: </dd>
<blockquote>
<pre>% echo matz &gt; /tmp/junk
% cat /tmp/junk
matz
% ruby -p -i.bak -e '$_.upcase!' /tmp/junk
% cat /tmp/junk
MATZ
% cat /tmp/junk.bak
matz</pre>
</blockquote>
<dt><code>-l</code></dt>
<dd>(The lowercase letter &#8220;ell .&#8221; Enables automatic line-ending processing, which means to firstly set <code>$\</code> to the value of <code>$/</code> and secondly chops every line read using <code>chop!</code> </dd>
<dt><code>-n</code></dt>
<dd>Causes Ruby to assume the following loop around your script, which makes it iterate over file name arguments somewhat like <code>sed</code> &#8211;<code>n</code> or <code>awk</code> </dd>
<blockquote>
<pre>while gets
 ...
end</pre>
</blockquote>
<dt><code>-p</code></dt>
<dd>Acts mostly same as -n switch, but print the value of variable <code>$_</code> at the each end of the loop. For example: </dd>
<blockquote>
<pre>% echo matz | ruby -p -e '$_.tr! &quot;a-z&quot;, &quot;A-Z&quot;'
MATZ</pre>
</blockquote>
<dt><code>-r </code><i>library</i></dt>
<dd>Causes Ruby to load the library using require. It is useful when using &#8211;<code>n</code> or &#8211;<code>p</code> </dd>
<dt><code>-s</code></dt>
<dd>Enables some switch parsing for switches after script name but before any file name arguments (or before a &#8211;<code>&#8211; )</code> Any switches found there are removed from <code>ARGV</code> and set the corresponding variable in the script. For example: </dd>
<blockquote>
<pre>#! /usr/local/bin/ruby -s
# prints &quot;true&quot; if invoked with `-xyz' switch.
print &quot;true
&quot; if $xyz</pre>
</blockquote>
<dt><code>-v</code></dt>
<dd>Enables verbose mode. Ruby will print its version at the beginning and set the variable <code>$VERBOSE</code> to true. Some methods print extra messages if this variable is true. If this switch is given, and no other switches are present, Ruby quits after printing its version. </dd>
<dt><code>-w</code></dt>
<dd>Enables verbose mode without printing version message at the beginning. It sets the <code>$VERBOSE</code> variable to true. </dd>
<dt><code>-x </code>[<i>directory</i> ]</dt>
<dd>Tells Ruby that the script is embedded in a message. Leading garbage will be discarded until the first line that starts with &#8220;#!&#8221; and contains the string, &#8220;ruby&#8221; Any meaningful switches on that line will be applied. The end of the script must be specified with either <code>EOF</code> <code>^D ( control-D</code> <code>^Z ( control-Z</code> or the reserved word <code>__END__</code> If the directory name is specified, Ruby will switch to that directory before executing script. </dd>
<dt><code>-y</code></dt>
<dd>
</dd><dt><code>&#8211;yydebug</code></dt>
<dd>DO NOT USE. </dd>
<p> Turns on compiler debug mode. Ruby will print a bunch of internal state messages during compilation. Only specify this switch you are going to debug the Ruby interpreter. </p>
<dt><code>&#8211;disable- </code><i>FEATURE</i></dt>
<dd>
</dd><dt><code>&#8211;enable- </code><i>FEATURE</i></dt>
<dd>Disables (or enables) the specified <i>FEATURE</i></dd>
<dl COMPACT>
<dt><code>&#8211;disable-gems</code></dt>
<dd>
</dd><dt><code>&#8211;enable-gems</code></dt>
<dd>Disables (or enables) RubyGems libraries. By default, Ruby will load the latest version of each installed gem. The <code>Gem</code> constant is true if RubyGems is enabled, false if otherwise. </dd>
<dt><code>&#8211;disable-rubyopt</code></dt>
<dd>
</dd><dt><code>&#8211;enable-rubyopt</code></dt>
<dd>Ignores (or considers) the <code>RUBYOPT</code> environment variable. By default, Ruby considers the variable. </dd>
<dt><code>&#8211;disable-all</code></dt>
<dd>
</dd><dt><code>&#8211;enable-all</code></dt>
<dd>Disables (or enables) all features. </dd>
</dl>
<dt><code>&#8211;dump = </code><i>target</i></dt>
<dd>Dump some informations. </dd>
<p> Prints the specified target. <i>target</i> can be one of;</p>
<dl COMPACT>
<dt><code>version</code></dt>
<dd>version description same as &#8211;<code>-version</code></dd>
<dt><code>usage</code></dt>
<dd>brief usage message same as &#8211;<code>h</code></dd>
<dt><code>help</code></dt>
<dd>Show long help message same as &#8211;<code>-help</code></dd>
<dt><code>syntax</code></dt>
<dd>check of syntax same as &#8211;<code>c</code> &#8211;<code>-yydebug</code></dd>
<dt><code>yydebug</code></dt>
<dd>compiler debug mode, same as &#8211;<code>-yydebug</code> </dd>
<p> Only specify this switch if you are going to debug the Ruby interpreter.</p>
<dt><code>parsetree</code></dt>
<dd>
</dd><dt><code>parsetree_with_comment</code></dt>
<dd>AST nodes tree </dd>
<p> Only specify this switch if you are going to debug the Ruby interpreter.</p>
<dt><code>insns</code></dt>
<dd>disassembled instructions </dd>
<p> Only specify this switch if you are going to debug the Ruby interpreter.</dl>
<dt><code>&#8211;verbose</code></dt>
<dd>Enables verbose mode without printing version message at the beginning. It sets the <code>$VERBOSE</code> variable to true. If this switch is given, and no other switches are present, Ruby quits after printing its version.</dd></dl>
<h2>Environment</h2>
<dl COMPACT>
<dt><code>RUBYLIB</code></dt>
<dd>A colon-separated list of directories that are added to Ruby&#8217;s library load path ( <code>$: ) . Directories from this environment variable are searched</code> before the standard load path is searched. </dd>
<p> e.g.: </p>
<blockquote><p><tt>RUBYLIB=&quot;$HOME/lib/ruby:$HOME/lib/rubyext&quot;</tt></p></blockquote>
<dt><code>RUBYOPT</code></dt>
<dd>Additional Ruby options. </dd>
<p> e.g. </p>
<blockquote><p><tt>RUBYOPT=&quot;-w -Ke&quot;</tt></p></blockquote>
<p> Note that RUBYOPT can contain only &#8211;<code>d , -E , -I , -K , -r , -T , -U , -v , -w , -W, &#8211;debug</code> &#8211;<code>-disable- </code><i>FEATURE</i> and &#8211;<code>-enable- </code><i>FEATURE</i> </p>
<dt><code>RUBYPATH</code></dt>
<dd>A colon-separated list of directories that Ruby searches for Ruby programs when the &#8211;<code>S</code> flag is specified. This variable precedes the <code>PATH</code> environment variable. </dd>
<dt><code>RUBYSHELL</code></dt>
<dd>The path to the system shell command. This environment variable is enabled for only mswin32, mingw32, and OS/2 platforms. If this variable is not defined, Ruby refers to <code>COMSPEC</code> </dd>
<dt><code>PATH</code></dt>
<dd>Ruby refers to the <code>PATH</code> environment variable on calling Kernel#system.</dd></dl>
<p> And Ruby depends on some RubyGems related environment variables unless RubyGems is disabled. See the help of <a href="/docs/linux/man/1-gem/">gem</a>(1) as below. </p>
<blockquote>
<pre>% gem help</pre>
</blockquote>
<h2>Gc Environment</h2>
<p>The Ruby garbage collector (GC) tracks objects in fixed-sized slots, but each object may have auxiliary memory allocations handled by the malloc family of C standard library calls ( <a href="/docs/linux/man/3-malloc/">malloc</a>(3), <a href="/docs/linux/man/3-calloc/">calloc</a>(3), and <a href="/docs/linux/man/3-realloc/">realloc</a>(3)). In this documentatation, the &quot;heap&quot; refers to the Ruby object heap of fixed-sized slots, while &quot;malloc&quot; refers to auxiliary allocations commonly referred to as the &quot;process heap&quot;. Thus there are at least two possible ways to trigger GC:</p>
<dl COMPACT>
<dt><code>1</code></dt>
<dd>Reaching the object limit.</dd>
<dt><code>2</code></dt>
<dd>Reaching the malloc limit. </dd>
</dl>
<p> In Ruby 2.1, the generational GC was introduced and the limits are divided into young and old generations, providing two additional ways to trigger a GC:</p>
<dl COMPACT>
<dt><code>3</code></dt>
<dd>Reaching the old object limit.</dd>
<dt><code>4</code></dt>
<dd>Reaching the old malloc limit.</dd></dl>
<p> There are currently 4 possible areas where the GC may be tuned by the following 11 environment variables:</p>
<dl COMPACT>
<dt><code>RUBY_GC_HEAP_INIT_SLOTS</code></dt>
<dd>Initial allocation slots. Introduced in Ruby 2.1, default: 10000. </dd>
<dt><code>RUBY_GC_HEAP_FREE_SLOTS</code></dt>
<dd>Prepare at least this amount of slots after GC. Allocate this number slots if there are not enough slots. Introduced in Ruby 2.1, default: 4096 </dd>
<dt><code>RUBY_GC_HEAP_GROWTH_FACTOR</code></dt>
<dd>Increase allocation rate of heap slots by this factor. Introduced in Ruby 2.1, default: 1.8, minimum: 1.0 (no growth) </dd>
<dt><code>RUBY_GC_HEAP_GROWTH_MAX_SLOTS</code></dt>
<dd>Allocation rate is limited to this number of slots, preventing excessive allocation due to RUBY_GC_HEAP_GROWTH_FACTOR. Introduced in Ruby 2.1, default: 0 (no limit) </dd>
<dt><code>RUBY_GC_HEAP_OLDOBJECT_LIMIT_FACTOR</code></dt>
<dd>Perform a full GC when the number of old objects is more than R * N, where R is this factor and N is the number of old objects after the last full GC. Introduced in Ruby 2.1.1, default: 2.0 </dd>
<dt><code>RUBY_GC_MALLOC_LIMIT</code></dt>
<dd>The initial limit of young generation allocation from the malloc-family. GC will start when this limit is reached. Default: 16MB </dd>
<dt><code>RUBY_GC_MALLOC_LIMIT_MAX</code></dt>
<dd>The maximum limit of young generation allocation from malloc before GC starts. Prevents excessive malloc growth due to RUBY_GC_MALLOC_LIMIT_GROWTH_FACTOR. Introduced in Ruby 2.1, default: 32MB. </dd>
<dt><code>RUBY_GC_MALLOC_LIMIT_GROWTH_FACTOR</code></dt>
<dd>Increases the limit of young generation malloc calls, reducing GC frequency but increasing malloc growth until RUBY_GC_MALLOC_LIMIT_MAX is reached. Introduced in Ruby 2.1, default: 1.4, minimum: 1.0 (no growth) </dd>
<dt><code>RUBY_GC_OLDMALLOC_LIMIT</code></dt>
<dd>The initial limit of old generation allocation from malloc, a full GC will start when this limit is reached. Introduced in Ruby 2.1, default: 16MB </dd>
<dt><code>RUBY_GC_OLDMALLOC_LIMIT_MAX</code></dt>
<dd>The maximum limit of old generation allocation from malloc before a full GC starts. Prevents excessive malloc growth due to RUBY_GC_OLDMALLOC_LIMIT_GROWTH_FACTOR. Introduced in Ruby 2.1, default: 128MB </dd>
<dt><code>RUBY_GC_OLDMALLOC_LIMIT_GROWTH_FACTOR</code></dt>
<dd>Increases the limit of old generation malloc allocation, reducing full GC frequency but increasing malloc growth until RUBY_GC_OLDMALLOC_LIMIT_MAX is reached. Introduced in Ruby 2.1, default: 1.2, minimum: 1.0 (no growth) </dd>
</dl>
<h2>Stack Size Environment</h2>
<p>Stack size environment variables are implementation-dependent and subject to change with different versions of Ruby. The VM stack is used for pure-Ruby code and managed by the virtual machine. Machine stack is used by the operating system and its usage is dependent on C extensions as well as C compiler options. Using lower values for these may allow applications to keep more Fibers or Threads running; but increases the chance of SystemStackError exceptions and segmentation faults (SIGSEGV). These environment variables are available since Ruby 2.0.0. All values are specified in bytes. </p>
<dl COMPACT>
<dt><code>RUBY_THREAD_VM_STACK_SIZE</code></dt>
<dd>VM stack size used at thread creation. default: 131072 (32-bit CPU) or 262144 (64-bit) </dd>
<dt><code>RUBY_THREAD_MACHINE_STACK_SIZE</code></dt>
<dd>Machine stack size used at thread creation. default: 524288 or 1048575 </dd>
<dt><code>RUBY_FIBER_VM_STACK_SIZE</code></dt>
<dd>VM stack size used at fiber creation. default: 65536 or 131072 </dd>
<dt><code>RUBY_FIBER_MACHINE_STACK_SIZE</code></dt>
<dd>Machine stack size used at fiber creation. default: 262144 or 524288 </dd>
</dl>
<h2>See Also</h2>
<dl COMPACT>
<dt><code>Lk </code><a rel="nofollow" href="https://www.ruby-lang.org/">https://www.ruby-lang.org/</a></dt>
<dd>The official web site.</dd>
<dt><code>Lk </code><a rel="nofollow" href="https://www.ruby-toolbox.com/">https://www.ruby-toolbox.com/</a></dt>
<dd>Comprehensive catalog of Ruby libraries.</dd></dl>
<h2>Reporting Bugs</h2>
<ul>
<li> Security vulnerabilities should be reported via an email to Mt security [at] ruby-lang.org . Reported problems will be published after being fixed.
<li> Other bugs and feature requests can be reported via the Ruby Issue Tracking System (Lk <a rel="nofollow" href="https://bugs.ruby-lang.org/">https://bugs.ruby-lang.org/</a> ) Do not report security vulnerabilities via this system because it publishes the vulnerabilities immediately. </ul>
<h2>Authors</h2>
<p>Ruby is designed and implemented by An Yukihiro Matsumoto Aq matz [at] netlab.jp . </p>
<p> See Aq Lk <a rel="nofollow" href="https://bugs.ruby-lang.org/projects/ruby/wiki/Contributors">https://bugs.ruby-lang.org/projects/ruby/wiki/Contributors</a> for contributors to Ruby.</p>
