---
title: "svn-bisect(1)"
name: "svn-bisect"
section: "1"
letter: "s"
url: "/docs/linux/man/1-svn-bisect/"
---

<h2 class="name">NAME</h2>
 

 svn-bisect 

<h2>SYNOPSIS</h2>

 <pre><code>
$ svn - bisect-- min 25000 --max 26000 start $ svn - bisect bad $ svn - bisect bad $ svn - bisect good[etc etc] $ svn - bisect reset
</code></pre>

<h2>DESCRIPTION</h2>

 This tool's purpose is to help you determine which revision of a subversion repository contains a change. It does this by employing a binary search. It will manage the current revision of your checkout directory, and narrow in on the target revision, as you give it clues about the current revision such as ``before'' (this revision is before the one you want) or ``after'' (this revision is after the one you want). 

 Start a bisect session with the ``start'' command. Then, walk the binary tree by using the ``before'' and ``after'' commands. When you are done, the tool will tell you the target revision. 

 The most common usage scenario is finding out which rev a bug was introduced in. For this purpose, some command aliases have been added: if the current revision contains the bug, you can use the ``bad'' command (meaning, this revision is ``after'' the change you want to find), otherwise use the ``good'' command (meaning, this revision is ``before'' the change you want to find). 

 All commands should be run from within a subversion checkout directory. After a ``svn-bisect start'', all subsequent svn-bisect commands need to be run from that same directory.

<h2>OPTIONS</h2>

 Options <font SIZE="-1">MUST</font> be specified before subcommands, on the command line. Options specified after the subcommand will be passed to the subcommand; this is currently only useful for the ``run'' subcommand.
<dl>
<dt>--help
<dd> Use anywhere. Output a command list, or specific help for the given command.
<dt>--version
<dd> Use anywhere. Tells you my version number.
<dt>--verbose
<dd> Use anywhere. Enable some additional informational output.
<dt>--min
<dd> Use with ``start''. Specify the beginning revision of the range.
<dt>--max
<dd> Use with ``start''. Specify the ending revision of the range.
<dt>--back
<dd> Use with ``reset''. Restores the original repository version.</dl>

<h2>SUBCOMMANDS</h2>

<h3>start</h3>

 
svn - bisect[--min M][--max N] start
 

 Start a new bisect session. If --min isn't specified, you can specify it later with the ``good'' command. If --max isn't specified, you can specify it later with the ``bad'' command.

<h3>after</h3>

 
svn - bisect after[revision] or : svn - bisect bad[revision]
 

 Inform svn-bisect that the specified revision is *after* the change we're looking for. If you don't specify a revision number, the current revision of the working tree is used. If you are looking for the rev which introduced a bug (which is the common case), the alias ``bad'' might be easier to remember.

<h3>before</h3>

 
svn - bisect before[revision] or : svn - bisect good[revision]
 

 Inform svn-bisect that the specified revision is *before* the change we're looking for. If you don't specify a revision number, the current revision of the working tree is used. If you are looking for the rev which introduced a bug (which is the common case), the alias ``good'' might be easier to remember.

<h3>skip</h3>

 
svn - bisect skip[&lt;rev&gt;[&lt;rev&gt;...]]
 

 Tell svn-bisect to skip the specified revision. If no revision is specified, the current version of the working tree is used. Do this if you can't determine whether the current revision is bad or good, if, for instance, some other issue prevents it from compiling successfully. 

 You may specify more than one revision, and they will all be skipped.

<h3>unskip</h3>

 <pre>
    svn-bisect unskip &lt;rev&gt; [&lt;rev&gt;...]
</pre> 

 Tell svn-bisect to no longer skip the specified revision. You must specify at least one revision to unskip. If you specify more than one, they will all be unskipped.

<h3>run</h3>

 <pre>
    svn-bisect run &lt;command&gt; [arguments...]
</pre> 

 Runs a command repeatedly to automate the bisection process. 

 Examples: 

 <pre>
    svn-bisect run ./mytest.sh
    svn-bisect run test ! -f file
</pre> 

 We run the command and arguments until a conclusion is reached. The command (usually a shell script) tells us about the current revision by way of its return code. The following return codes are handled: 

 <pre>
    0: This revision is before the change we're looking for
    1-124, 126-127: This revision includes the change we're looking for
    125: This revision is untestable and should be skipped
    any other value: The command failed to run, abort bisection.
</pre> 

 In other words, ``run'' will automatically find the last revision for which the given command returns success. (Keep in mind that in the shell, ``0'' means ``success''.) 

 The normal caveats apply. In particular, if your script makes any changes, don't forget to clean up afterwards.

<h3>reset</h3>

 <pre>
    svn-bisect reset
</pre> 

 Clean up after a bisect, and return the repository to the revision it was at before you started.

<h3>help</h3>

 <pre>
    svn-bisect help
    svn-bisect help start
</pre> 

 Gives you some useful descriptions and usage information.

<h2>EXAMPLE</h2>

 ...Because, you know, no software documentation is complete without a flashy screenshot, these days. 

 So, lets say you were wondering when the subversion project added the ``Last Changed Rev:'' line to the output of ``svn info''. Determining the existence of this change is a straightforward matter of searching for the text string... if a result was found, the current revision is ``after'', otherwise it was ``before''. So a bisect looks like this: 

 <pre><code>
    $ svn co http://svn.apache.org/repos/asf/subversion/trunk/subversion
    [snip lots of subversion checkout spam]
    Checked out revision 980012.
    
    $ cd subversion
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    svn/info-cmd.c:362:    SVN_ERR(svn_cmdline_printf(pool, _("Last Changed Rev: %ld\n"),
    tests/cmdline/depth_tests.py:2056:      'Last Changed Rev'   : '^1$',
    tests/cmdline/upgrade_tests.py:387:      'Last Changed Rev' : '7'
    tests/cmdline/upgrade_tests.py:396:      'Last Changed Rev' : '10'
    
    $ date
    Wed Jul 28 06:40:03 EDT 2010
    
    $ svn-bisect --min 0 start
    $ svn-bisect after
    Fetching history from r0 to r980012; it may take a while.
    There are 24349 revs left in the pool.  Choosing r862045.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    svn/info-cmd.c:348:    SVN_ERR(svn_cmdline_printf(pool, _("Last Changed Rev: %ld\n"),
    
    $ svn-bisect after
    There are 12174 revs left in the pool.  Choosing r845633.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    clients/cmdline/info-cmd.c:153:    printf ("Last Changed Rev: %" SVN_REVNUM_T_FMT "\n", entry-&gt;cmt_rev);
    
    $ svn-bisect after
    There are 6087 revs left in the pool.  Choosing r840416.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    
    $ svn-bisect before
    There are 3043 revs left in the pool.  Choosing r842636.

#ack-- nocolor-- nogroup 'Last Changed Rev'
    clients/cmdline/info-cmd.c:153:    printf ("Last Changed Rev: %" SVN_REVNUM_T_FMT "\n", entry-&gt;cmt_rev);
    
    $ svn-bisect after
    There are 1521 revs left in the pool.  Choosing r841463.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    
    $ svn-bisect before
    There are 760 revs left in the pool.  Choosing r841993.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    clients/cmdline/info-cmd.c:161:        printf ("Last Changed Rev: %" SVN_REVNUM_T_FMT "\n", entry-&gt;cmt_rev);
    
    $ svn-bisect after
    There are 380 revs left in the pool.  Choosing r841730.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    
    $ svn-bisect before
    There are 189 revs left in the pool.  Choosing r841860.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    
    $ svn-bisect before
    There are 94 revs left in the pool.  Choosing r841933.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    clients/cmdline/info-cmd.c:151:        printf ("Last Changed Rev: %" SVN_REVNUM_T_FMT "\n", entry-&gt;cmt_rev);
    
    $ svn-bisect after
    There are 47 revs left in the pool.  Choosing r841904.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    clients/cmdline/info-cmd.c:150:        printf ("Last Changed Rev: %ld\n", entry-&gt;cmt_rev);
    
    $ svn-bisect after
    There are 23 revs left in the pool.  Choosing r841880.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    
    $ svn-bisect before
    There are 11 revs left in the pool.  Choosing r841890.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    clients/cmdline/info-cmd.c:153:            printf ("Last Changed Rev: %ld\n", entry-&gt;cmt_rev);
    
    $ svn-bisect after
    There are 5 revs left in the pool.  Choosing r841883.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    clients/cmdline/info-cmd.c:153:            printf ("Last Changed Rev: %ld\n", entry-&gt;cmt_rev);
    
    $ svn-bisect after
    There are 2 revs left in the pool.  Choosing r841882.
    
    $ ack --nocolor --nogroup 'Last Changed Rev'
    
    $ svn-bisect before
    This is the end of the road!
    The change occurred in r841883.
    
    $ svn log -r841883
    ------------------------------------------------------------------------
    r841883 | rooneg | 2002-04-27 15:23:38 -0400 (Sat, 27 Apr 2002) | 30 lines
    
    As requested by cmpilato in issue #676, add an 'svn info' command, which 
    prints out the contents of the svn_wc_entry_t for a given versioned resource.
    
    * CHANGES
      note the addition of the 'svn info' command.
    
    * subversion/clients/cmdline/cl.h
      add declaration for svn_cl__info.
    
    * subversion/clients/cmdline/info-cmd.c
      new file implementing the info command.
    
    * subversion/clients/cmdline/main.c
      hook up the info command.
    
    * subversion/clients/cmdline/man/svn.1
      document the info command.
    
    * subversion/tests/clients/cmdline/getopt_tests_data/svn--help_stdout
      update for the addition of info command.
    
    * subversion/tests/clients/cmdline/getopt_tests_data/svn_help_stdout
      ditto.
    
    * subversion/tests/clients/cmdline/getopt_tests_data/svn_stderr
      ditto.
    
    * tools/dev/bash_completion
      add 'info' to the tab completion.
    
    ------------------------------------------------------------------------
    
    $ date
    Wed Jul 28 06:45:27 EDT 2010
</code></pre> 

 So, there it is. In 5 minutes, we've learned that ``Last Changed Rev:'' has been in there since the inception of the ``svn info'' command itself, back in 2002. 

 You can also provide a script command to do all of the work for you: 

 <pre>
    $ svn-bisect --min 0 --max 980012 start
    $ svn-bisect run '! grep -r &quot;Last Changed Rev&quot; .'
</pre>

<h2>REQUIREMENTS</h2>

 This tool requires: 

 * A computer 

 * A brain 

 * An installation of Perl, version 5.8 or above 

 * The IO::All module, installed from <font SIZE="-1">CPAN</font> 

 * The YAML::Syck module, installed from <font SIZE="-1">CPAN</font> 

 * The ``svn'' command somewhere in your <font SIZE="-1">PATH,</font> executable by the current user 

 * A svn checkout with some history to bisect.

<h2>AUTHOR</h2>

 <pre>
    Mark Glines &lt;mark-cpan [at] glines.org&gt;
</pre>

<h2>REPOSITORY</h2>

 Browser: &lt;<a rel="nofollow" HREF="http://github.com/Infinoid/svn-bisect/">http://github.com/Infinoid/svn-bisect/</a>&gt; Clone: &lt;<a HREF="git://github.com/Infinoid/svn-bisect.git">git://github.com/Infinoid/svn-bisect.git</a>&gt;

<h2>THANKS</h2>

 * Thanks to the git-bisect author(s), for coming up with a user interface that 
&nbsp;<wbr>&nbsp;<wbr>I actually like. 

 * Thanks to Will Coleda for inspiring me to actually write and release this. 

 * Thanks to the Parrot project for having so much random stuff going on as to 
&nbsp;<wbr>&nbsp;<wbr>make a tool like this necessary.

<h2>SEE ALSO</h2>

 App::SVNBinarySearch by Will Coleda: &lt;<a rel="nofollow" HREF="http://search.cpan.org/dist/App-SVNBinarySearch/">http://search.cpan.org/dist/App-SVNBinarySearch/</a>&gt;

<h2>COPYRIGHT AND LICENSE</h2>

 This software is copyright (c) 2008 Mark Glines. 

 It is distributed under the terms of the Artistic License 2.0. For details, see the ``<font SIZE="-1">LICENSE''</font> file packaged alongside this tool. 

<h2>Index</h2>


