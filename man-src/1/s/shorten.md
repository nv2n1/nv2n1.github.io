---
title: "shorten(1)"
name: "shorten"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shorten/"
---

<h2 class="name">NAME</h2>
 

 shorten - CLI program to demonstrate use of WWW::Shorten 

<h2>SYNOPSIS</h2>

 <pre>
    # Default shortening service is Metamark
    $ shorten books.perl.org/book/171
    <a rel="nofollow" HREF="http://xrl.us/dv8">http://xrl.us/dv8</a>
    # Change with an environment variable
    $ SHORTEN_SERVICE=TinyURL shorten books.perl.org/book/171
    <a rel="nofollow" HREF="http://tinyurl.com/ye7gjf4">http://tinyurl.com/ye7gjf4</a>
    # Change with command line option
    $ shorten --service=TinyURL books.perl.org/book/171
    <a rel="nofollow" HREF="http://tinyurl.com/ye7gjf4">http://tinyurl.com/ye7gjf4</a>
    # Change using config file
    $ cat ~/.shortenrc 
    service = TinyURL
    $ shorten books.perl.org/book/171
    <a rel="nofollow" HREF="http://tinyurl.com/ye7gjf4">http://tinyurl.com/ye7gjf4</a>
</pre>

<h2>CONFIGURATION</h2>

 The service used can be controlled in various ways. The program will use the first of the following values that it finds:
<dl>
<dt>&bull;
<dd> The value of the <tt>&quot;--service&quot;</tt> command line option.
<dt>&bull;
<dd> The value of the <tt>&quot;SHORTEN_SERVICE&quot;</tt> environment variable.
<dt>&bull;
<dd> The value of the <tt>&quot;service&quot;</tt> option from the configuration file (see below).
<dt>&bull;
<dd> If none of the above options is found, the program defaults to using Metamark.</dl>

<h2>CONFIGURATION FILE</h2>

 As we use the <tt>&quot;Config::Auto&quot;</tt> module for configuration, shorten's fairly flexible when it comes to format. 

 Configuration will be found in whichever of the following files comes first. 

 <pre>
    shortenconfig
    ~/shortenconfig
    /etc/shortenconfig
    shorten.config
    ~/shorten.config
    /etc/shorten.config
    shortenrc
    ~/shortenrc
    /etc/shortenrc
    .shortenrc
    ~/.shortenrc
    /etc/.shortenrc
</pre> 

 Generally, I use the format: 

 <pre>
    service = MakeAShorterLink
</pre> 

 which is simple and works. <tt>&quot;service&quot;</tt> is the only configuration keyword at present. Its value should be a correctly capitalized service name as per WWW::Shorten's documentation.

<h2>BUGS, REQUESTS, COMMENTS</h2>

 Please report any requests, suggestions or bugs via the system at &lt;<a rel="nofollow" HREF="http://rt.cpan.org/">http://rt.cpan.org/</a>&gt;, or email &lt;bug-WWW-Shorten [at] rt.cpan.org&gt;. This makes it much easier for me to track things and thus means your problem is less likely to be neglected.

<h2>LICENSE AND COPYRIGHT</h2>

 Copyright X Magnum Solutions Ltd, 2002 - 2010. All rights reserved. 

 This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>AUTHOR</h2>

 Dave Cross &lt;dave [at] mag-sol.com&gt;, taking over from Iain Truskett &lt;spoon [at] cpan.org&gt;

<h2>SEE ALSO</h2>

 perl 

<h2>Index</h2>


