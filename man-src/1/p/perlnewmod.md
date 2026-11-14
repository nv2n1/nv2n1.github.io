---
title: "perlnewmod(1)"
name: "perlnewmod"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlnewmod/"
---

<h2 class="name">NAME</h2>
 

 perlnewmod - preparing a new module for distribution 

<h2>DESCRIPTION</h2>

 This document gives you some suggestions about how to go about writing Perl modules, preparing them for distribution, and making them available via <font SIZE="-1">CPAN.</font> 

 One of the things that makes Perl really powerful is the fact that Perl hackers tend to want to share the solutions to problems they've faced, so you and I don't have to battle with the same problem again. 

 The main way they do this is by abstracting the solution into a Perl module. If you don't know what one of these is, the rest of this document isn't going to be much use to you. You're also missing out on an awful lot of useful code; consider having a look at perlmod, perlmodlib and perlmodinstall before coming back here. 

 When you've found that there isn't a module available for what you're trying to do, and you've had to write the code yourself, consider packaging up the solution into a module and uploading it to <font SIZE="-1">CPAN</font> so that others can benefit. 

 You should also take a look at perlmodstyle for best practices in making a module.

<h3>Warning</h3>

 We're going to primarily concentrate on Perl-only modules here, rather than <font SIZE="-1">XS</font> modules. <font SIZE="-1">XS</font> modules serve a rather different purpose, and you should consider different things before distributing them - the popularity of the library you are gluing, the portability to other operating systems, and so on. However, the notes on preparing the Perl side of the module and packaging and distributing it will apply equally well to an <font SIZE="-1">XS</font> module as a pure-Perl one.

<h3>What should I make into a module?</h3>

 You should make a module out of any code that you think is going to be useful to others. Anything that's likely to fill a hole in the communal library and which someone else can slot directly into their program. Any part of your code which you can isolate and extract and plug into something else is a likely candidate. 

 Let's take an example. Suppose you're reading in data from a local format into a hash-of-hashes in Perl, turning that into a tree, walking the tree and then piping each node to an Acme Transmogrifier Server. 

 Now, quite a few people have the Acme Transmogrifier, and you've had to write something to talk the protocol from scratch - you'd almost certainly want to make that into a module. The level at which you pitch it is up to you: you might want protocol-level modules analogous to Net::SMTP which then talk to higher level modules analogous to Mail::Send. The choice is yours, but you do want to get a module out for that server protocol. 

 Nobody else on the planet is going to talk your local data format, so we can ignore that. But what about the thing in the middle? Building tree structures from Perl variables and then traversing them is a nice, general problem, and if nobody's already written a module that does that, you might want to modularise that code too. 

 So hopefully you've now got a few ideas about what's good to modularise. Let's now see how it's done.

<h3>Step-by-step: Preparing the ground</h3>

 Before we even start scraping out the code, there are a few things we'll want to do in advance.
<dl>
<dt>Look around
<dd> Dig into a bunch of modules to see how they're written. I'd suggest starting with Text::Tabs, since it's in the standard library and is nice and simple, and then looking at something a little more complex like File::Copy. For object oriented code, WWW::Mechanize or the <tt>&quot;Email::*&quot;</tt> modules provide some good examples. 

 These should give you an overall feel for how modules are laid out and written.
<dt>Check it's new
<dd> There are a lot of modules on <font SIZE="-1">CPAN,</font> and it's easy to miss one that's similar to what you're planning on contributing. Have a good plough through &lt;<a rel="nofollow" HREF="http://metacpan.org">http://metacpan.org</a>&gt; and make sure you're not the one reinventing the wheel!
<dt>Discuss the need
<dd> You might love it. You might feel that everyone else needs it. But there might not actually be any real demand for it out there. If you're unsure about the demand your module will have, consider asking the <tt>&quot;module-authors [at] perl.org&quot;</tt> mailing list (send an email to <tt>&quot;module-authors-subscribe [at] perl.org&quot;</tt> to subscribe; see &lt;<a rel="nofollow" HREF="http://lists.perl.org/list/module-authors.html">http://lists.perl.org/list/module-authors.html</a>&gt; for more information and a link to the archives).
<dt>Choose a name
<dd> Perl modules included on <font SIZE="-1">CPAN</font> have a naming hierarchy you should try to fit in with. See perlmodlib for more details on how this works, and browse around <font SIZE="-1">CPAN</font> and the modules list to get a feel of it. At the very least, remember this: modules should be title capitalised, (This::Thing) fit in with a category, and explain their purpose succinctly.
<dt>Check again
<dd> While you're doing that, make really sure you haven't missed a module similar to the one you're about to write. 

 When you've got your name sorted out and you're sure that your module is wanted and not currently available, it's time to start coding.</dl>

<h3>Step-by-step: Making the module</h3>

<dl>
<dt>Start with <i>module-starter</i> or <i>h2xs</i>
<dd> The <i>module-starter</i> utility is distributed as part of the Module::Starter <font SIZE="-1">CPAN</font> package. It creates a directory with stubs of all the necessary files to start a new module, according to recent ``best practice'' for module development, and is invoked from the command line, thus: 

 <pre><code>
module - starter-- module = Foo::Bar-- author = "Your Name" --email = yourname[at] cpan.org
</code></pre> 

 If you do not wish to install the Module::Starter package from <font SIZE="-1">CPAN,</font> <i>h2xs</i> is an older tool, originally intended for the development of <font SIZE="-1">XS</font> modules, which comes packaged with the Perl distribution. 

 A typical invocation of h2xs for a pure Perl module is: 

 <pre>
    h2xs -AX --skip-exporter --use-new-tests -n Foo::Bar
</pre> 

 The <tt>&quot;-A&quot;</tt> omits the Autoloader code, <tt>&quot;-X&quot;</tt> omits <font SIZE="-1">XS</font> elements, <tt>&quot;--skip-exporter&quot;</tt> omits the Exporter code, <tt>&quot;--use-new-tests&quot;</tt> sets up a modern testing environment, and <tt>&quot;-n&quot;</tt> specifies the name of the module.
<dt>Use strict and warnings
<dd> A module's code has to be warning and strict-clean, since you can't guarantee the conditions that it'll be used under. Besides, you wouldn't want to distribute code that wasn't warning or strict-clean anyway, right?
<dt>Use Carp
<dd> The Carp module allows you to present your error messages from the caller's perspective; this gives you a way to signal a problem with the caller and not your module. For instance, if you say this: 

 <pre>
    warn &quot;No hostname given&quot;;
</pre> 

 the user will see something like this: 

 <pre>
 No hostname given at
 /usr/local/lib/perl5/site_perl/5.6.0/Net/Acme.pm line 123.
</pre> 

 which looks like your module is doing something wrong. Instead, you want to put the blame on the user, and say this: 

 <pre>
    No hostname given at bad_code, line 10.
</pre> 

 You do this by using Carp and replacing your <tt>&quot;warn&quot;</tt>s with <tt>&quot;carp&quot;</tt>s. If you need to <tt>&quot;die&quot;</tt>, say <tt>&quot;croak&quot;</tt> instead. However, keep <tt>&quot;warn&quot;</tt> and <tt>&quot;die&quot;</tt> in place for your sanity checks - where it really is your module at fault.
<dt>Use Exporter - wisely!
<dd> Exporter gives you a standard way of exporting symbols and subroutines from your module into the caller's namespace. For instance, saying <tt>&quot;use Net::Acme qw(&amp;frob)&quot;</tt> would import the <tt>&quot;frob&quot;</tt> subroutine. 

 The package variable <tt>@EXPORT</tt> will determine which symbols will get exported when the caller simply says <tt>&quot;use Net::Acme&quot;</tt> - you will hardly ever want to put anything in there. <tt>@EXPORT_OK</tt>, on the other hand, specifies which symbols you're willing to export. If you do want to export a bunch of symbols, use the <tt>%EXPORT_TAGS</tt> and define a standard export set - look at Exporter for more details.
<dt>Use plain old documentation
<dd> The work isn't over until the paperwork is done, and you're going to need to put in some time writing some documentation for your module. <tt>&quot;module-starter&quot;</tt> or <tt>&quot;h2xs&quot;</tt> will provide a stub for you to fill in; if you're not sure about the format, look at perlpod for an introduction. Provide a good synopsis of how your module is used in code, a description, and then notes on the syntax and function of the individual subroutines or methods. Use Perl comments for developer notes and <font SIZE="-1">POD</font> for end-user notes.
<dt>Write tests
<dd> You're encouraged to create self-tests for your module to ensure it's working as intended on the myriad platforms Perl supports; if you upload your module to <font SIZE="-1">CPAN,</font> a host of testers will build your module and send you the results of the tests. Again, <tt>&quot;module-starter&quot;</tt> and <tt>&quot;h2xs&quot;</tt> provide a test framework which you can extend - you should do something more than just checking your module will compile. Test::Simple and Test::More are good places to start when writing a test suite.
<dt>Write the <i></i><font SIZE="-1"><i>README</i></font><i></i>
<dd> If you're uploading to <font SIZE="-1">CPAN,</font> the automated gremlins will extract the <font SIZE="-1">README</font> file and place that in your <font SIZE="-1">CPAN</font> directory. It'll also appear in the main <i>by-module</i> and <i>by-category</i> directories if you make it onto the modules list. It's a good idea to put here what the module actually does in detail.
<dt>Write <i>Changes</i>
<dd> Add any user-visible changes since the last release to your <i>Changes</i> file.</dl>

<h3>Step-by-step: Distributing your module</h3>

<dl>
<dt>Get a <font SIZE="-1">CPAN</font> user <font SIZE="-1">ID</font>
<dd> Every developer publishing modules on <font SIZE="-1">CPAN</font> needs a <font SIZE="-1">CPAN ID.</font> Visit <tt>&quot;&lt;<a rel="nofollow" HREF="http://pause.perl.org/">http://pause.perl.org/</a>&gt;&quot;</tt>, select ``Request <font SIZE="-1">PAUSE</font> Account'', and wait for your request to be approved by the <font SIZE="-1">PAUSE</font> administrators.
<dt>&quot;perl Makefile.PL; make test; make distcheck; make dist&quot;
<dd> Once again, <tt>&quot;module-starter&quot;</tt> or <tt>&quot;h2xs&quot;</tt> has done all the work for you. They produce the standard <tt>&quot;Makefile.PL&quot;</tt> you see when you download and install modules, and this produces a Makefile with a <tt>&quot;dist&quot;</tt> target. 

 Once you've ensured that your module passes its own tests - always a good thing to make sure - you can <tt>&quot;make distcheck&quot;</tt> to make sure everything looks <font SIZE="-1">OK,</font> followed by <tt>&quot;make dist&quot;</tt>, and the Makefile will hopefully produce you a nice tarball of your module, ready for upload.
<dt>Upload the tarball
<dd> The email you got when you received your <font SIZE="-1">CPAN ID</font> will tell you how to log in to <font SIZE="-1">PAUSE,</font> the Perl Authors Upload SErver. From the menus there, you can upload your module to <font SIZE="-1">CPAN.</font> 

 Alternatively you can use the <i>cpan-upload</i> script, part of the CPAN::Uploader distribution on <font SIZE="-1">CPAN.</font>
<dt>Fix bugs!
<dd> Once you start accumulating users, they'll send you bug reports. If you're lucky, they'll even send you patches. Welcome to the joys of maintaining a software project...</dl>

<h2>AUTHOR</h2>

 Simon Cozens, <tt>&quot;simon [at] cpan.org&quot;</tt> 

 Updated by Kirrily ``Skud'' Robert, <tt>&quot;skud [at] cpan.org&quot;</tt>

<h2>SEE ALSO</h2>

 perlmod, perlmodlib, perlmodinstall, h2xs, strict, Carp, Exporter, perlpod, Test::Simple, Test::More ExtUtils::MakeMaker, Module::Build, Module::Starter &lt;<a rel="nofollow" HREF="http://www.cpan.org/">http://www.cpan.org/</a>&gt;, Ken Williams' tutorial on building your own module at &lt;<a rel="nofollow" HREF="http://mathforum.org/~ken/perl_modules.html">http://mathforum.org/~ken/perl_modules.html</a>&gt; 

<h2>Index</h2>


