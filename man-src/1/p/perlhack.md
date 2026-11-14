---
title: "perlhack(1)"
name: "perlhack"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlhack/"
description: "perlhack – How to hack on Perl"
---

<h2 class="name">NAME</h2>
<p> perlhack &#8211; How to hack on Perl </p>
<h2>DESCRIPTION</h2>
<p> This document explains how Perl development works. It includes details about the Perl 5 Porters email list, the Perl repository, the Perlbug bug tracker, patch guidelines, and commentary on Perl development philosophy.</p>
<h2>SUPER QUICK PATCH GUIDE</h2>
<p> If you just want to submit a single small patch like a pod fix, a test for a bug, comment fixes, etc., it&#8217;s easy! Here&#8217;s how:</p>
<dl>
<dt>&bull;</p>
<dd> Check out the source repository </p>
<p> The perl source is in a git repository. You can clone the repository with the following command: </p>
<pre>
  % git clone <a href="git://perl5.git.perl.org/perl.git">git://perl5.git.perl.org/perl.git</a> perl
</pre>
<dt>&bull;</p>
<dd> Ensure you&#8217;re following the latest advice </p>
<p> In case the advice in this guide has been updated recently, read the latest version directly from the perl source: </p>
<pre>
  % perldoc pod/perlhack.pod
</pre>
<dt>&bull;</p>
<dd> Make your change </p>
<p> Hack, hack, hack. Keep in mind that Perl runs on many different platforms, with different operating systems that have different capabilities, different filesystem organizations, and even different character sets. perlhacktips gives advice on this.</p>
<dt>&bull;</p>
<dd> Test your change </p>
<p> You can run all the tests with the following commands: </p>
<pre>
  % ./Configure -des -Dusedevel
  % make test
</pre>
<p> Keep hacking until the tests pass.</p>
<dt>&bull;</p>
<dd> Commit your change </p>
<p> Committing your work will save the change <i>on your local system</i>: </p>
<pre>
  % git commit -a -m 'Commit message goes here'
</pre>
<p> Make sure the commit message describes your change in a single sentence. For example, &#8220;Fixed spelling errors in perlhack.pod&#8221;.</p>
<dt>&bull;</p>
<dd> Send your change to perlbug </p>
<p> The next step is to submit your patch to the Perl core ticket system via email. </p>
<p> If your changes are in a single git commit, run the following commands to generate the patch file and attach it to your bug report: </p>
<pre>
  % git format-patch -1
  % ./perl -Ilib utils/perlbug -p 0001-*.patch
</pre>
<p> The perlbug program will ask you a few questions about your email address and the patch you&#8217;re submitting. Once you&#8217;ve answered them it will submit your patch via email. </p>
<p> If your changes are in multiple commits, generate a patch file for each one and provide them to perlbug&#8217;s <tt>&quot;-p&quot;</tt> option separated by commas: </p>
<pre>
  % git format-patch -3
  % ./perl -Ilib utils/perlbug -p 0001-fix1.patch,0002-fix2.patch,\
  &gt; 0003-fix3.patch
</pre>
<p> When prompted, pick a subject that summarizes your changes.</p>
<dt>&bull;</p>
<dd> Thank you </p>
<p> The porters appreciate the time you spent helping to make Perl better. Thank you!</p>
<dt>&bull;</p>
<dd> Acknowledgement </p>
<p> All contributors are credited (by name and email address) in the <font SIZE="-1">AUTHORS</font> file, which is part of the perl distribution, as well as the Git commit history. </p>
<p> If you don’t want to be included in the <font SIZE="-1">AUTHORS</font> file, just let us know. Otherwise we will take your submission of a patch as permission to credit you in the <font SIZE="-1">AUTHORS</font> file.</p>
<dt>&bull;</p>
<dd> Next time </p>
<p> The next time you wish to make a patch, you need to start from the latest perl in a pristine state. Check you don&#8217;t have any local changes or added files in your perl check-out which you wish to keep, then run these commands: </p>
<pre>
  % git pull
  % git reset --hard origin/blead
  % git clean -dxf
</pre>
</dl>
<h2>BUG REPORTING</h2>
<p> If you want to report a bug in Perl, you must use the <i>perlbug</i> command line tool. This tool will ensure that your bug report includes all the relevant system and configuration information. </p>
<p> To browse existing Perl bugs and patches, you can use the web interface at &lt;<a rel="nofollow" href="http://rt.perl.org/">http://rt.perl.org/</a>&gt;. </p>
<p> Please check the archive of the perl5-porters list (see below) and/or the bug tracking system before submitting a bug report. Often, you&#8217;ll find that the bug has been reported already. </p>
<p> You can log in to the bug tracking system and comment on existing bug reports. If you have additional information regarding an existing bug, please add it. This will help the porters fix the bug.</p>
<h2>PERL 5 PORTERS</h2>
<p> The perl5-porters (p5p) mailing list is where the Perl standard distribution is maintained and developed. The people who maintain Perl are also referred to as the &#8220;Perl 5 Porters&#8221;, &#8220;p5p&#8221; or just the &#8220;porters&#8221;. </p>
<p> A searchable archive of the list is available at &lt;<a rel="nofollow" href="http://markmail.org/search/?q=perl5-porters">http://markmail.org/search/?q=perl5-porters</a>&gt;. There is also an archive at &lt;<a rel="nofollow" href="http://archive.develooper.com/perl5-porters@perl.org/">http://archive.develooper.com/perl5-porters@perl.org/</a>&gt;.</p>
<h3>perl-changes mailing list</h3>
<p> The perl5-changes mailing list receives a copy of each patch that gets submitted to the maintenance and development branches of the perl repository. See &lt;<a rel="nofollow" href="http://lists.perl.org/list/perl5-changes.html">http://lists.perl.org/list/perl5-changes.html</a>&gt; for subscription and archive information.</p>
<h3>#p5p on <font SIZE="-1">IRC</font></h3>
<p> Many porters are also active on the &lt;<a href="irc://irc.perl.org/#p5p">irc://irc.perl.org/#p5p</a>&gt; channel. Feel free to join the channel and ask questions about hacking on the Perl core.</p>
<h2>GETTING THE PERL SOURCE</h2>
<p> All of Perl&#8217;s source code is kept centrally in a Git repository at <i>perl5.git.perl.org</i>. The repository contains many Perl revisions from Perl 1 onwards and all the revisions from Perforce, the previous version control system. </p>
<p> For much more detail on using git with the Perl repository, please see perlgit.</p>
<h3>Read access via Git</h3>
<p> You will need a copy of Git for your computer. You can fetch a copy of the repository using the git protocol: </p>
<pre>
  % git clone <a href="git://perl5.git.perl.org/perl.git">git://perl5.git.perl.org/perl.git</a> perl
</pre>
<p> This clones the repository and makes a local copy in the <i>perl</i> directory. </p>
<p> If you cannot use the git protocol for firewall reasons, you can also clone via http, though this is much slower: </p>
<pre>
  % git clone <a rel="nofollow" href="http://perl5.git.perl.org/perl.git">http://perl5.git.perl.org/perl.git</a> perl
</pre>
<h3>Read access via the web</h3>
<p> You may access the repository over the web. This allows you to browse the tree, see recent commits, subscribe to <font SIZE="-1">RSS</font> feeds for the changes, search for particular commits and more. You may access it at &lt;<a rel="nofollow" href="http://perl5.git.perl.org/perl.git">http://perl5.git.perl.org/perl.git</a>&gt;. A mirror of the repository is found at &lt;<a rel="nofollow" href="https://github.com/Perl/perl5">https://github.com/Perl/perl5</a>&gt;.</p>
<h3>Read access via rsync</h3>
<p> You can also choose to use rsync to get a copy of the current source tree for the bleadperl branch and all maintenance branches: </p>
<pre>
  % rsync -avz <a href="rsync://perl5.git.perl.org/perl-current">rsync://perl5.git.perl.org/perl-current</a> .
  % rsync -avz <a href="rsync://perl5.git.perl.org/perl-5.12.x">rsync://perl5.git.perl.org/perl-5.12.x</a> .
  % rsync -avz <a href="rsync://perl5.git.perl.org/perl-5.10.x">rsync://perl5.git.perl.org/perl-5.10.x</a> .
  % rsync -avz <a href="rsync://perl5.git.perl.org/perl-5.8.x">rsync://perl5.git.perl.org/perl-5.8.x</a> .
  % rsync -avz <a href="rsync://perl5.git.perl.org/perl-5.6.x">rsync://perl5.git.perl.org/perl-5.6.x</a> .
  % rsync -avz <a href="rsync://perl5.git.perl.org/perl-5.005xx">rsync://perl5.git.perl.org/perl-5.005xx</a> .
</pre>
<p> (Add the <tt>&quot;--delete&quot;</tt> option to remove leftover files.) </p>
<p> To get a full list of the available sync points: </p>
<pre>
  % rsync perl5.git.perl.org::
</pre>
<h3>Write access via git</h3>
<p> If you have a commit bit, please see perlgit for more details on using git.</p>
<h2>PATCHING PERL</h2>
<p> If you&#8217;re planning to do more extensive work than a single small fix, we encourage you to read the documentation below. This will help you focus your work and make your patches easier to incorporate into the Perl source.</p>
<h3>Submitting patches</h3>
<p> If you have a small patch to submit, please submit it via perlbug. You can also send email directly to perlbug [at] perl.org. Please note that messages sent to perlbug may be held in a moderation queue, so you won&#8217;t receive a response immediately. </p>
<p> You&#8217;ll know your submission has been processed when you receive an email from our ticket tracking system. This email will give you a ticket number. Once your patch has made it to the ticket tracking system, it will also be sent to the perl5-porters [at] perl.org list. </p>
<p> If your patch is related to an already-opened ticket you can also attach your patch to that ticket, without having to use perlbug. </p>
<p> Patches are reviewed and discussed on the p5p list. Simple, uncontroversial patches will usually be applied without any discussion. When the patch is applied, the ticket will be updated and you will receive email. In addition, an email will be sent to the p5p list. </p>
<p> In other cases, the patch will need more work or discussion. That will happen on the p5p list. </p>
<p> You are encouraged to participate in the discussion and advocate for your patch. Sometimes your patch may get lost in the shuffle. It&#8217;s appropriate to send a reminder email to p5p if no action has been taken in a month. Please remember that the Perl 5 developers are all volunteers, and be polite. </p>
<p> Changes are always applied directly to the main development branch, called &#8220;blead&#8221;. Some patches may be backported to a maintenance branch. If you think your patch is appropriate for the maintenance branch (see &#8220;<font SIZE="-1">MAINTENANCE BRANCHES&#8221;</font> in perlpolicy), please explain why when you submit it.</p>
<h3>Getting your patch accepted</h3>
<p> If you are submitting a code patch there are several things that you can do to help the Perl 5 Porters accept your patch. </p>
<p> <i>Patch style</i> </p>
<p> If you used git to check out the Perl source, then using <tt>&quot;git format-patch&quot;</tt> will produce a patch in a style suitable for Perl. The <tt>&quot;format-patch&quot;</tt> command produces one patch file for each commit you made. If you prefer to send a single patch for all commits, you can use <tt>&quot;git diff&quot;</tt>. </p>
<pre>
  % git checkout blead
  % git pull
  % git diff blead my-branch-name
</pre>
<p> This produces a patch based on the difference between blead and your current branch. It&#8217;s important to make sure that blead is up to date before producing the diff, that&#8217;s why we call <tt>&quot;git pull&quot;</tt> first. </p>
<p> We strongly recommend that you use git if possible. It will make your life easier, and ours as well. </p>
<p> However, if you&#8217;re not using git, you can still produce a suitable patch. You&#8217;ll need a pristine copy of the Perl source to diff against. The porters prefer unified diffs. Using <font SIZE="-1">GNU</font> <tt>&quot;diff&quot;</tt>, you can produce a diff like this: </p>
<pre>
  % diff -Npurd perl.pristine perl.mine
</pre>
<p> Make sure that you <tt>&quot;make realclean&quot;</tt> in your copy of Perl to remove any build artifacts, or you may get a confusing result. </p>
<p> <i>Commit message</i> </p>
<p> As you craft each patch you intend to submit to the Perl core, it&#8217;s important to write a good commit message. This is especially important if your submission will consist of a series of commits. </p>
<p> The first line of the commit message should be a short description without a period. It should be no longer than the subject line of an email, 50 characters being a good rule of thumb. </p>
<p> A lot of Git tools (Gitweb, GitHub, git log &#8211;pretty=oneline, &#8230;) will only display the first line (cut off at 50 characters) when presenting commit summaries. </p>
<p> The commit message should include a description of the problem that the patch corrects or new functionality that the patch adds. </p>
<p> As a general rule of thumb, your commit message should help a programmer who knows the Perl core quickly understand what you were trying to do, how you were trying to do it, and why the change matters to Perl.</p>
<dl>
<dt>&bull;</p>
<dd> Why </p>
<p> Your commit message should describe why the change you are making is important. When someone looks at your change in six months or six years, your intent should be clear. </p>
<p> If you&#8217;re deprecating a feature with the intent of later simplifying another bit of code, say so. If you&#8217;re fixing a performance problem or adding a new feature to support some other bit of the core, mention that.</p>
<dt>&bull;</p>
<dd> What </p>
<p> Your commit message should describe what part of the Perl core you&#8217;re changing and what you expect your patch to do.</p>
<dt>&bull;</p>
<dd> How </p>
<p> While it&#8217;s not necessary for documentation changes, new tests or trivial patches, it&#8217;s often worth explaining how your change works. Even if it&#8217;s clear to you today, it may not be clear to a porter next month or next year.</dl>
<p> A commit message isn&#8217;t intended to take the place of comments in your code. Commit messages should describe the change you made, while code comments should describe the current state of the code. </p>
<p> If you&#8217;ve just implemented a new feature, complete with doc, tests and well-commented code, a brief commit message will often suffice. If, however, you&#8217;ve just changed a single character deep in the parser or lexer, you might need to write a small novel to ensure that future readers understand what you did and why you did it. </p>
<p> <i>Comments, Comments, Comments</i> </p>
<p> Be sure to adequately comment your code. While commenting every line is unnecessary, anything that takes advantage of side effects of operators, that creates changes that will be felt outside of the function being patched, or that others may find confusing should be documented. If you are going to err, it is better to err on the side of adding too many comments than too few. </p>
<p> The best comments explain <i>why</i> the code does what it does, not <i>what it does</i>. </p>
<p> <i>Style</i> </p>
<p> In general, please follow the particular style of the code you are patching. </p>
<p> In particular, follow these general guidelines for patching Perl sources:</p>
<dl>
<dt>&bull;</p>
<dd> 4-wide indents for code, 2-wide indents for nested <font SIZE="-1">CPP</font> <tt>&quot;#define&quot;</tt>s, with 8-wide tabstops.</p>
<dt>&bull;</p>
<dd> Use spaces for indentation, not tab characters. </p>
<p> The codebase is a mixture of tabs and spaces for indentation, and we are moving to spaces only. Converting lines you&#8217;re patching from 8-wide tabs to spaces will help this migration.</p>
<dt>&bull;</p>
<dd> Try hard not to exceed 79-columns</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">ANSI C</font> prototypes</p>
<dt>&bull;</p>
<dd> Uncuddled elses and &#8220;K&amp;R&#8221; style for indenting control constructs</p>
<dt>&bull;</p>
<dd> No C<font SIZE="-2">++</font> style (//) comments</p>
<dt>&bull;</p>
<dd> Mark places that need to be revisited with <font SIZE="-1">XXX</font> (and revisit often!)</p>
<dt>&bull;</p>
<dd> Opening brace lines up with &#8220;if&#8221; when conditional spans multiple lines; should be at end-of-line otherwise</p>
<dt>&bull;</p>
<dd> In function definitions, name starts in column 0 (return value-type is on previous line)</p>
<dt>&bull;</p>
<dd> Single space after keywords that are followed by parens, no space between function name and following paren</p>
<dt>&bull;</p>
<dd> Avoid assignments in conditionals, but if they&#8217;re unavoidable, use extra paren, e.g. &#8220;if (a &amp;&amp; (b = c)) &#8230;&#8221;</p>
<dt>&bull;</p>
<dd> &#8220;return foo;&#8221; rather than &#8220;return(foo);&#8221;</p>
<dt>&bull;</p>
<dd> &#8220;if (!foo) &#8230;&#8221; rather than &#8220;if (foo == <font SIZE="-1">FALSE</font>) &#8230;&#8221; etc.</p>
<dt>&bull;</p>
<dd> Do not declare variables using &#8220;register&#8221;. It may be counterproductive with modern compilers, and is deprecated in C<font SIZE="-2">++</font>, under which the Perl source is regularly compiled.</p>
<dt>&bull;</p>
<dd> In-line functions that are in headers that are accessible to <font SIZE="-1">XS</font> code need to be able to compile without warnings with commonly used extra compilation flags, such as gcc&#8217;s <tt>&quot;-Wswitch-default&quot;</tt> which warns whenever a switch statement does not have a &#8220;default&#8221; case. The use of these extra flags is to catch potential problems in legal C code, and is often used by Perl aggregators, such as Linux distributors.</dl>
<p> <i>Test suite</i> </p>
<p> If your patch changes code (rather than just changing documentation), you should also include one or more test cases which illustrate the bug you&#8217;re fixing or validate the new functionality you&#8217;re adding. In general, you should update an existing test file rather than create a new one. </p>
<p> Your test suite additions should generally follow these guidelines (courtesy of Gurusamy Sarathy &lt;gsar [at] activestate.com&gt;):</p>
<dl>
<dt>&bull;</p>
<dd> Know what you&#8217;re testing. Read the docs, and the source.</p>
<dt>&bull;</p>
<dd> Tend to fail, not succeed.</p>
<dt>&bull;</p>
<dd> Interpret results strictly.</p>
<dt>&bull;</p>
<dd> Use unrelated features (this will flush out bizarre interactions).</p>
<dt>&bull;</p>
<dd> Use non-standard idioms (otherwise you are not testing <font SIZE="-1">TIMTOWTDI</font>).</p>
<dt>&bull;</p>
<dd> Avoid using hardcoded test numbers whenever possible (the <font SIZE="-1">EXPECTED/GOT</font> found in t/op/tie.t is much more maintainable, and gives better failure reports).</p>
<dt>&bull;</p>
<dd> Give meaningful error messages when a test fails.</p>
<dt>&bull;</p>
<dd> Avoid using qx// and <code>system()</code> unless you are testing for them. If you do use them, make sure that you cover _all_ perl platforms.</p>
<dt>&bull;</p>
<dd> Unlink any temporary files you create.</p>
<dt>&bull;</p>
<dd> Promote unforeseen warnings to errors with <tt>$SIG</tt>{__WARN__}.</p>
<dt>&bull;</p>
<dd> Be sure to use the libraries and modules shipped with the version being tested, not those that were already installed.</p>
<dt>&bull;</p>
<dd> Add comments to the code explaining what you are testing for.</p>
<dt>&bull;</p>
<dd> Make updating the &#8216;1..42&#8217; string unnecessary. Or make sure that you update it.</p>
<dt>&bull;</p>
<dd> Test _all_ behaviors of a given operator, library, or function. </p>
<p> Test all optional arguments. </p>
<p> Test return values in various contexts (boolean, scalar, list, lvalue). </p>
<p> Use both global and lexical variables. </p>
<p> Don&#8217;t forget the exceptional, pathological cases.</dl>
<h3>Patching a core module</h3>
<p> This works just like patching anything else, with one extra consideration. </p>
<p> Modules in the <i>cpan/</i> directory of the source tree are maintained outside of the Perl core. When the author updates the module, the updates are simply copied into the core. See that module&#8217;s documentation or its listing on &lt;<a rel="nofollow" href="http://search.cpan.org/">http://search.cpan.org/</a>&gt; for more information on reporting bugs and submitting patches. </p>
<p> In most cases, patches to modules in <i>cpan/</i> should be sent upstream and should not be applied to the Perl core individually. If a patch to a file in <i>cpan/</i> absolutely cannot wait for the fix to be made upstream, released to <font SIZE="-1">CPAN</font> and copied to blead, you must add (or update) a <tt>&quot;CUSTOMIZED&quot;</tt> entry in the <i>&#8220;Porting/Maintainers.pl&#8221;</i> file to flag that a local modification has been made. See <i>&#8220;Porting/Maintainers.pl&#8221;</i> for more details. </p>
<p> In contrast, modules in the <i>dist/</i> directory are maintained in the core.</p>
<h3>Updating perldelta</h3>
<p> For changes significant enough to warrant a <i>pod/perldelta.pod</i> entry, the porters will greatly appreciate it if you submit a delta entry along with your actual change. Significant changes include, but are not limited to:</p>
<dl>
<dt>&bull;</p>
<dd> Adding, deprecating, or removing core features</p>
<dt>&bull;</p>
<dd> Adding, deprecating, removing, or upgrading core or dual-life modules</p>
<dt>&bull;</p>
<dd> Adding new core tests</p>
<dt>&bull;</p>
<dd> Fixing security issues and user-visible bugs in the core</p>
<dt>&bull;</p>
<dd> Changes that might break existing code, either on the perl or C level</p>
<dt>&bull;</p>
<dd> Significant performance improvements</p>
<dt>&bull;</p>
<dd> Adding, removing, or significantly changing documentation in the <i>pod/</i> directory</p>
<dt>&bull;</p>
<dd> Important platform-specific changes</dl>
<p> Please make sure you add the perldelta entry to the right section within <i>pod/perldelta.pod</i>. More information on how to write good perldelta entries is available in the <tt>&quot;Style&quot;</tt> section of <i>Porting/how_to_write_a_perldelta.pod</i>.</p>
<h3>What makes for a good patch?</h3>
<p> New features and extensions to the language can be contentious. There is no specific set of criteria which determine what features get added, but here are some questions to consider when developing a patch: </p>
<p> <i>Does the concept match the general goals of Perl?</i> </p>
<p> Our goals include, but are not limited to:</p>
<dl>
<dt>1.</p>
<dd> Keep it fast, simple, and useful.</p>
<dt>2.</p>
<dd> Keep features/concepts as orthogonal as possible.</p>
<dt>3.</p>
<dd> No arbitrary limits (platforms, data sizes, cultures).</p>
<dt>4.</p>
<dd> Keep it open and exciting to use/patch/advocate Perl everywhere.</p>
<dt>5.</p>
<dd> Either assimilate new technologies, or build bridges to them.</dl>
<p> <i>Where is the implementation?</i> </p>
<p> All the talk in the world is useless without an implementation. In almost every case, the person or people who argue for a new feature will be expected to be the ones who implement it. Porters capable of coding new features have their own agendas, and are not available to implement your (possibly good) idea. </p>
<p> <i>Backwards compatibility</i> </p>
<p> It&#8217;s a cardinal sin to break existing Perl programs. New warnings can be contentious&#8212;some say that a program that emits warnings is not broken, while others say it is. Adding keywords has the potential to break programs, changing the meaning of existing token sequences or functions might break programs. </p>
<p> The Perl 5 core includes mechanisms to help porters make backwards incompatible changes more compatible such as the feature and deprecate modules. Please use them when appropriate. </p>
<p> <i>Could it be a module instead?</i> </p>
<p> Perl 5 has extension mechanisms, modules and <font SIZE="-1">XS,</font> specifically to avoid the need to keep changing the Perl interpreter. You can write modules that export functions, you can give those functions prototypes so they can be called like built-in functions, you can even write <font SIZE="-1">XS</font> code to mess with the runtime data structures of the Perl interpreter if you want to implement really complicated things. </p>
<p> Whenever possible, new features should be prototyped in a <font SIZE="-1">CPAN</font> module before they will be considered for the core. </p>
<p> <i>Is the feature generic enough?</i> </p>
<p> Is this something that only the submitter wants added to the language, or is it broadly useful? Sometimes, instead of adding a feature with a tight focus, the porters might decide to wait until someone implements the more generalized feature. </p>
<p> <i>Does it potentially introduce new bugs?</i> </p>
<p> Radical rewrites of large chunks of the Perl interpreter have the potential to introduce new bugs. </p>
<p> <i>How big is it?</i> </p>
<p> The smaller and more localized the change, the better. Similarly, a series of small patches is greatly preferred over a single large patch. </p>
<p> <i>Does it preclude other desirable features?</i> </p>
<p> A patch is likely to be rejected if it closes off future avenues of development. For instance, a patch that placed a true and final interpretation on prototypes is likely to be rejected because there are still options for the future of prototypes that haven&#8217;t been addressed. </p>
<p> <i>Is the implementation robust?</i> </p>
<p> Good patches (tight code, complete, correct) stand more chance of going in. Sloppy or incorrect patches might be placed on the back burner until the pumpking has time to fix, or might be discarded altogether without further notice. </p>
<p> <i>Is the implementation generic enough to be portable?</i> </p>
<p> The worst patches make use of system-specific features. It&#8217;s highly unlikely that non-portable additions to the Perl language will be accepted. </p>
<p> <i>Is the implementation tested?</i> </p>
<p> Patches which change behaviour (fixing bugs or introducing new features) must include regression tests to verify that everything works as expected. </p>
<p> Without tests provided by the original author, how can anyone else changing perl in the future be sure that they haven&#8217;t unwittingly broken the behaviour the patch implements? And without tests, how can the patch&#8217;s author be confident that his/her hard work put into the patch won&#8217;t be accidentally thrown away by someone in the future? </p>
<p> <i>Is there enough documentation?</i> </p>
<p> Patches without documentation are probably ill-thought out or incomplete. No features can be added or changed without documentation, so submitting a patch for the appropriate pod docs as well as the source code is important. </p>
<p> <i>Is there another way to do it?</i> </p>
<p> Larry said &quot;Although the Perl Slogan is <i>There&#8217;s More Than One Way to Do It</i>, I hesitate to make 10 ways to do something&quot;. This is a tricky heuristic to navigate, though&#8212;one man&#8217;s essential addition is another man&#8217;s pointless cruft. </p>
<p> <i>Does it create too much work?</i> </p>
<p> Work for the pumpking, work for Perl programmers, work for module authors, &#8230; Perl is supposed to be easy. </p>
<p> <i>Patches speak louder than words</i> </p>
<p> Working code is always preferred to pie-in-the-sky ideas. A patch to add a feature stands a much higher chance of making it to the language than does a random feature request, no matter how fervently argued the request might be. This ties into &#8220;Will it be useful?&#8221;, as the fact that someone took the time to make the patch demonstrates a strong desire for the feature.</p>
<h2>TESTING</h2>
<p> The core uses the same testing style as the rest of Perl, a simple &#8220;ok/not ok&#8221; run through Test::Harness, but there are a few special considerations. </p>
<p> There are three ways to write a test in the core: Test::More, <i>t/test.pl</i> and ad hoc <tt>&quot;print $test ? &quot;ok 42
&quot; : &quot;not ok 42
&quot;&quot;</tt>. The decision of which to use depends on what part of the test suite you&#8217;re working on. This is a measure to prevent a high-level failure (such as Config.pm breaking) from causing basic functionality tests to fail. </p>
<p> The <i>t/test.pl</i> library provides some of the features of Test::More, but avoids loading most modules and uses as few core features as possible. </p>
<p> If you write your own test, use the Test Anything Protocol &lt;<a rel="nofollow" href="http://testanything.org">http://testanything.org</a>&gt;.</p>
<dl>
<dt>&bull;</p>
<dd> <i>t/base</i>, <i>t/comp</i> and <i>t/opbasic</i> </p>
<p> Since we don&#8217;t know if <tt>&quot;require&quot;</tt> works, or even subroutines, use ad hoc tests for these three. Step carefully to avoid using the feature being tested. Tests in <i>t/opbasic</i>, for instance, have been placed there rather than in <i>t/op</i> because they test functionality which <i>t/test.pl</i> presumes has already been demonstrated to work.</p>
<dt>&bull;</p>
<dd> <i>t/cmd</i>, <i>t/run</i>, <i>t/io</i> and <i>t/op</i> </p>
<p> Now that basic <code>require()</code> and subroutines are tested, you can use the <i>t/test.pl</i> library. </p>
<p> You can also use certain libraries like Config conditionally, but be sure to skip the test gracefully if it&#8217;s not there.</p>
<dt>&bull;</p>
<dd> Everything else </p>
<p> Now that the core of Perl is tested, Test::More can and should be used. You can also use the full suite of core modules in the tests.</dl>
<p> When you say &#8220;make test&#8221;, Perl uses the <i>t/TEST</i> program to run the test suite (except under Win32 where it uses <i>t/harness</i> instead). All tests are run from the <i>t/</i> directory, <code>not</code> the directory which contains the test. This causes some problems with the tests in <i>lib/</i>, so here&#8217;s some opportunity for some patching. </p>
<p> You must be triply conscious of cross-platform concerns. This usually boils down to using File::Spec, avoiding things like <tt>&quot;fork()&quot;</tt> and <tt>&quot;system()&quot;</tt> unless absolutely necessary, and not assuming that a given character has a particular ordinal value (code point) or that its <font SIZE="-1">UTF-8</font> representation is composed of particular bytes. </p>
<p> There are several functions available to specify characters and code points portably in tests. The always-preloaded functions <tt>&quot;utf8::unicode_to_native()&quot;</tt> and its inverse <tt>&quot;utf8::native_to_unicode()&quot;</tt> take code points and translate appropriately. The file <i>t/charset_tools.pl</i> has several functions that can be useful. It has versions of the previous two functions that take strings as inputs &#8212; not single numeric code points: <tt>&quot;uni_to_native()&quot;</tt> and <tt>&quot;native_to_uni()&quot;</tt>. If you must look at the individual bytes comprising a <font SIZE="-1">UTF-8</font> encoded string, <tt>&quot;byte_utf8a_to_utf8n()&quot;</tt> takes as input a string of those bytes encoded for an <font SIZE="-1">ASCII</font> platform, and returns the equivalent string in the native platform. For example, <tt>&quot;byte_utf8a_to_utf8n(&quot; &quot;)&quot;</tt> returns the byte sequence on the current platform that form the <font SIZE="-1">UTF-8</font> for <tt>&quot;U+00A0&quot;</tt>, since <tt>&quot; &quot;</tt> are the <font SIZE="-1">UTF-8</font> bytes on an <font SIZE="-1">ASCII</font> platform for that code point. This function returns <tt>&quot; &quot;</tt> on an <font SIZE="-1">ASCII</font> platform, and <tt>&quot;�A&quot;</tt> on an <font SIZE="-1">EBCDIC 1047</font> one. </p>
<p> But easiest is, if the character is specifiable as a literal, like <tt>&quot;A&quot;</tt> or <tt>&quot;%&quot;</tt>, to use that; if not so specificable, you can use use <tt>&quot;\N{}&quot;</tt> , if the side effects aren&#8217;t troublesome. Simply specify all your characters in hex, using <tt>&quot;\N{U+ZZ}&quot;</tt> instead of <tt>&quot;
