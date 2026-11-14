---
title: "prove(1)"
name: "prove"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prove/"
---

<h2 class="name">NAME</h2>
 

 prove - Run tests through a TAP harness. 

<h2>USAGE</h2>

 <pre><code>
prove[options][files or directories]
</code></pre>

<h2>OPTIONS</h2>

 Boolean options: 

 
 -v,  --verbose         Print all test lines.
 -l,  --lib             Add 'lib' to the path for your tests (-Ilib).
 -b,  --blib            Add 'blib/lib' and 'blib/arch' to the path for
                        your tests
 -s,  --shuffle         Run the tests in random order.
 -c,  --color           Colored test output (default).
      --nocolor         Do not color test output.
      --count           Show the X/Y test count when not verbose
                        (default)
      --nocount         Disable the X/Y test count.
 -D   --dry             Dry run. Show test that would have run.
 -f,  --failures        Show failed tests.
 -o,  --comments        Show comments.
      --ignore-exit     Ignore exit status from test scripts.
 -m,  --merge           Merge test scripts' STDERR with their STDOUT.
 -r,  --recurse         Recursively descend into directories.
      --reverse         Run the tests in reverse order.
 -q,  --quiet           Suppress some test output while running tests.
 -Q,  --QUIET           Only print summary results.
 -p,  --parse           Show full list of TAP parse errors, if any.
      --directives      Only show results with TODO or SKIP directives.
      --timer           Print elapsed time after each test.
      --trap            Trap Ctrl-C and print summary on interrupt.
      --normalize       Normalize TAP output in verbose output
 -T                     Enable tainting checks.
 -t                     Enable tainting warnings.
 -W                     Enable fatal warnings.
 -w                     Enable warnings.
 -h,  --help            Display this help
 -?,                    Display this help
 -V,  --version         Display the version
 -H,  --man             Longer manpage for prove
      --norc            Don't process default .proverc
 

 Options that take arguments: 

 
 -I                     Library paths to include.
 -P                     Load plugin (searches App::Prove::Plugin::*.)
 -M                     Load a module.
 -e,  --exec            Interpreter to run the tests ('' for compiled
                        tests.)
      --ext             Set the extension for tests (default '.t')
      --harness         Define test harness to use.  See TAP::Harness.
      --formatter       Result formatter to use. See FORMATTERS.
      --source          Load and/or configure a SourceHandler. See
                        SOURCE HANDLERS.
 -a,  --archive out.tgz Store the resulting TAP in an archive file.
 -j,  --jobs N          Run N test jobs in parallel (try 9.)
      --state=opts      Control prove's persistent state.
      --statefile=file  Use `file` instead of `.prove` for state
      --rc=rcfile       Process options from rcfile
      --rules           Rules for parallel vs sequential processing.


<h2>NOTES</h2>

<h3>.proverc</h3>

 If <i>~/.proverc</i> or <i>./.proverc</i> exist they will be read and any options they contain processed before the command line options. Options in <i>.proverc</i> are specified in the same way as command line options: 

 <pre>
    # .proverc
    --state=hot,fast,save
    -j9
</pre> 

 Additional option files may be specified with the <tt>&quot;--rc&quot;</tt> option. Default option file processing is disabled by the <tt>&quot;--norc&quot;</tt> option. 

 Under Windows and <font SIZE="-1">VMS</font> the option file is named <i>_proverc</i> rather than <i>.proverc</i> and is sought only in the current directory.

<h3>Reading from STDIN</h3>

 If you have a list of tests (or URLs, or anything else you want to test) in a file, you can add them to your tests by using a '-': 

 <pre>
 prove - &lt; my_list_of_things_to_test.txt
</pre> 

 See the <tt>&quot;README&quot;</tt> in the <tt>&quot;examples&quot;</tt> directory of this distribution.

<h3>Default Test Directory</h3>

 If no files or directories are supplied, <tt>&quot;prove&quot;</tt> looks for all files matching the pattern <tt>&quot;t/*.t&quot;</tt>.

<h3>Colored Test Output</h3>

 Colored test output using TAP::Formatter::Color is the default, but if output is not to a terminal, color is disabled. You can override this by adding the <tt>&quot;--color&quot;</tt> switch. 

 Color support requires Term::ANSIColor and, on windows platforms, also Win32::Console::ANSI. If the necessary module(s) are not installed colored output will not be available.

<h3>Exit Code</h3>

 If the tests fail <tt>&quot;prove&quot;</tt> will exit with non-zero status.

<h3>Arguments to Tests</h3>

 It is possible to supply arguments to tests. To do so separate them from prove's own arguments with the arisdottle, '::'. For example 

 <pre>
 prove -v t/mytest.t :: --url <a rel="nofollow" HREF="http://example.com">http://example.com</a>
</pre> 

 would run <i>t/mytest.t</i> with the options '--url <a rel="nofollow" HREF="http://example.com'.">http://example.com'.</a> When running multiple tests they will each receive the same arguments.

<h3>--exec</h3>

 Normally you can just pass a list of Perl tests and the harness will know how to execute them. However, if your tests are not written in Perl or if you want all tests invoked exactly the same way, use the <tt>&quot;-e&quot;</tt>, or <tt>&quot;--exec&quot;</tt> switch: 

 <pre>
 prove --exec '/usr/bin/ruby -w' t/
 prove --exec '/usr/bin/perl -Tw -mstrict -Ilib' t/
 prove --exec '/path/to/my/customer/exec'
</pre>

<h3>--merge</h3>

 If you need to make sure your diagnostics are displayed in the correct order relative to test results you can use the <tt>&quot;--merge&quot;</tt> option to merge the test scripts' <font SIZE="-1">STDERR</font> into their <font SIZE="-1">STDOUT.</font> 

 This guarantees that <font SIZE="-1">STDOUT</font> (where the test results appear) and <font SIZE="-1">STDERR</font> (where the diagnostics appear) will stay in sync. The harness will display any diagnostics your tests emit on <font SIZE="-1">STDERR.</font> 

 Caveat: this is a bit of a kludge. In particular note that if anything that appears on <font SIZE="-1">STDERR</font> looks like a test result the test harness will get confused. Use this option only if you understand the consequences and can live with the risk.

<h3>--trap</h3>

 The <tt>&quot;--trap&quot;</tt> option will attempt to trap <font SIZE="-1">SIGINT</font> (Ctrl-C) during a test run and display the test summary even if the run is interrupted

<h3>--state</h3>

 You can ask <tt>&quot;prove&quot;</tt> to remember the state of previous test runs and select and/or order the tests to be run based on that saved state. 

 The <tt>&quot;--state&quot;</tt> switch requires an argument which must be a comma separated list of one or more of the following options.
<dl>
<dt>&quot;last&quot;
<dd> Run the same tests as the last time the state was saved. This makes it possible, for example, to recreate the ordering of a shuffled test. 

 <pre>
    # Run all tests in random order
    $ prove -b --state=save --shuffle
    # Run them again in the same order
    $ prove -b --state=last
</pre>
<dt>&quot;failed&quot;
<dd> Run only the tests that failed on the last run. 

 <pre>
    # Run all tests
    $ prove -b --state=save
    # Run failures
    $ prove -b --state=failed
</pre> 

 If you also specify the <tt>&quot;save&quot;</tt> option newly passing tests will be excluded from subsequent runs. 

 <pre>
    # Repeat until no more failures
    $ prove -b --state=failed,save
</pre>
<dt>&quot;passed&quot;
<dd> Run only the passed tests from last time. Useful to make sure that no new problems have been introduced.
<dt>&quot;all&quot;
<dd> Run all tests in normal order. Multple options may be specified, so to run all tests with the failures from last time first: 

 <pre>
    $ prove -b --state=failed,all,save
</pre>
<dt>&quot;hot&quot;
<dd> Run the tests that most recently failed first. The last failure time of each test is stored. The <tt>&quot;hot&quot;</tt> option causes tests to be run in most-recent- failure order. 

 <pre>
    $ prove -b --state=hot,save
</pre> 

 Tests that have never failed will not be selected. To run all tests with the most recently failed first use 

 <pre>
    $ prove -b --state=hot,all,save
</pre> 

 This combination of options may also be specified thus 

 <pre>
    $ prove -b --state=adrian
</pre>
<dt>&quot;todo&quot;
<dd> Run any tests with todos.
<dt>&quot;slow&quot;
<dd> Run the tests in slowest to fastest order. This is useful in conjunction with the <tt>&quot;-j&quot;</tt> parallel testing switch to ensure that your slowest tests start running first. 

 <pre>
    $ prove -b --state=slow -j9
</pre>
<dt>&quot;fast&quot;
<dd> Run test tests in fastest to slowest order.
<dt>&quot;new&quot;
<dd> Run the tests in newest to oldest order based on the modification times of the test scripts.
<dt>&quot;old&quot;
<dd> Run the tests in oldest to newest order.
<dt>&quot;fresh&quot;
<dd> Run those test scripts that have been modified since the last test run.
<dt>&quot;save&quot;
<dd> Save the state on exit. The state is stored in a file called <i>.prove</i> (<i>_prove</i> on Windows and <font SIZE="-1">VMS</font>) in the current directory.</dl>
 

 The <tt>&quot;--state&quot;</tt> switch may be used more than once. 

 <pre>
    $ prove -b --state=hot --state=all,save
</pre>

<h3>--rules</h3>

 The <tt>&quot;--rules&quot;</tt> option is used to control which tests are run sequentially and which are run in parallel, if the <tt>&quot;--jobs&quot;</tt> option is specified. The option may be specified multiple times, and the order matters. 

 The most practical use is likely to specify that some tests are not ``parallel-ready''. Since mentioning a file with --rules doesn't cause it to be selected to run as a test, you can ``set and forget'' some rules preferences in your .proverc file. Then you'll be able to take maximum advantage of the performance benefits of parallel testing, while some exceptions are still run in parallel. 

 <i>--rules examples</i> 

 <pre>
    # All tests are allowed to run in parallel, except those starting with &quot;p&quot;
    --rules='seq=t/p*.t' --rules='par=**'
    # All tests must run in sequence except those starting with &quot;p&quot;, which should be run parallel
    --rules='par=t/p*.t'
</pre> 

 <i>--rules resolution</i>
<dl>
<dt>&bull;
<dd> By default, all tests are eligible to be run in parallel. Specifying any of your own rules removes this one.
<dt>&bull;
<dd> ``First match wins''. The first rule that matches a test will be the one that applies.
<dt>&bull;
<dd> Any test which does not match a rule will be run in sequence at the end of the run.
<dt>&bull;
<dd> The existence of a rule does not imply selecting a test. You must still specify the tests to run.
<dt>&bull;
<dd> Specifying a rule to allow tests to run in parallel does not make them run in parallel. You still need specify the number of parallel <tt>&quot;jobs&quot;</tt> in your Harness object.</dl>
 

 <i>--rules Glob-style pattern matching</i> 

 We implement our own glob-style pattern matching for --rules. Here are the supported patterns: 

 <pre>
    ** is any number of characters, including /, within a pathname
    * is zero or more characters within a filename/directory name
    ? is exactly one character within a filename/directory name
    {foo,bar,baz} is any of foo, bar or baz.
    \ is an escape character
</pre> 

 <i>More advanced specifications for parallel vs sequence run rules</i> 

 If you need more advanced management of what runs in parallel vs in sequence, see the associated 'rules' documentation in TAP::Harness and TAP::Parser::Scheduler. If what's possible directly through <tt>&quot;prove&quot;</tt> is not sufficient, you can write your own harness to access these features directly.

<h3>@INC</h3>

 prove introduces a separation between ``options passed to the perl which runs prove'' and ``options passed to the perl which runs tests''; this distinction is by design. Thus the perl which is running a test starts with the default <tt>@INC</tt>. Additional library directories can be added via the <tt>&quot;PERL5LIB&quot;</tt> environment variable, via -Ifoo in <tt>&quot;PERL5OPT&quot;</tt> or via the <tt>&quot;-Ilib&quot;</tt> option to <i>prove</i>.

<h3>Taint Mode</h3>

 Normally when a Perl program is run in taint mode the contents of the <tt>&quot;PERL5LIB&quot;</tt> environment variable do not appear in <tt>@INC</tt>. 

 Because <tt>&quot;PERL5LIB&quot;</tt> is often used during testing to add build directories to <tt>@INC</tt> prove passes the names of any directories found in <tt>&quot;PERL5LIB&quot;</tt> as -I switches. The net effect of this is that <tt>&quot;PERL5LIB&quot;</tt> is honoured even when prove is run in taint mode.

<h2>FORMATTERS</h2>

 You can load a custom TAP::Parser::Formatter: 

 <pre>
  prove --formatter MyFormatter
</pre>

<h2>SOURCE HANDLERS</h2>

 You can load custom TAP::Parser::SourceHandlers, to change the way the parser interprets particular <i>sources</i> of <font SIZE="-1">TAP.</font> 

 <pre>
  prove --source MyHandler --source YetAnother t
</pre> 

 If you want to provide config to the source you can use: 

 <pre><code>
prove-- source MyCustom-- source Perl-- perl - option 'foo=bar baz' --perl - option avg = 0.278 --source File-- file - option extensions =.txt-- file - option extensions =.tmp t-- source pgTAP-- pgtap - option pset = format = html-- pgtap - option pset = border = 2
</code></pre> 

 Each <tt>&quot;--$source-option&quot;</tt> option must specify a key/value pair separated by an <tt>&quot;=&quot;</tt>. If an option can take multiple values, just specify it multiple times, as with the <tt>&quot;extensions=&quot;</tt> examples above. If the option should be a hash reference, specify the value as a second pair separated by a <tt>&quot;=&quot;</tt>, as in the <tt>&quot;pset=&quot;</tt> examples above (escape <tt>&quot;=&quot;</tt> with a backslash). 

 All <tt>&quot;--sources&quot;</tt> are combined into a hash, and passed to ``new'' in TAP::Harness's <tt>&quot;sources&quot;</tt> parameter. 

 See TAP::Parser::IteratorFactory for more details on how configuration is passed to <i>SourceHandlers</i>.

<h2>PLUGINS</h2>

 Plugins can be loaded using the <tt>&quot;-P</tt>plugin<tt>&quot;</tt> syntax, eg: 

 <pre>
  prove -PMyPlugin
</pre> 

 This will search for a module named <tt>&quot;App::Prove::Plugin::MyPlugin&quot;</tt>, or failing that, <tt>&quot;MyPlugin&quot;</tt>. If the plugin can't be found, <tt>&quot;prove&quot;</tt> will complain &amp; exit. 

 You can pass arguments to your plugin by appending <tt>&quot;=arg1,arg2,etc&quot;</tt> to the plugin name: 

 <pre>
  prove -PMyPlugin=fou,du,fafa
</pre> 

 Please check individual plugin documentation for more details.

<h3>Available Plugins</h3>

 For an up-to-date list of plugins available, please check <font SIZE="-1">CPAN:</font> 

 &lt;<a rel="nofollow" HREF="http://search.cpan.org/search?query=App%3A%3AProve+Plugin">http://search.cpan.org/search?query=App%3A%3AProve+Plugin</a>&gt;

<h3>Writing Plugins</h3>

 Please see ``<font SIZE="-1">PLUGINS''</font> in App::Prove. 

<h2>Index</h2>


