---
title: "perlfaq9(1)"
name: "perlfaq9"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq9/"
description: "perlfaq9 – Web, Email and Networking"
---

<h2 class="name">NAME</h2>
<p> perlfaq9 &#8211; Web, Email and Networking </p>
<h2>VERSION</h2>
<p> version 5.20190126</p>
<h2>DESCRIPTION</h2>
<p> This section deals with questions related to running web sites, sending and receiving email as well as general networking.</p>
<h3>Should I use a web framework?</h3>
<p> Yes. If you are building a web site with any level of interactivity (forms / users / databases), you will want to use a framework to make handling requests and responses easier. </p>
<p> If there is no interactivity then you may still want to look at using something like Template Toolkit &lt;<a rel="nofollow" href="https://metacpan.org/module/Template">https://metacpan.org/module/Template</a>&gt; or Plack::Middleware::TemplateToolkit so maintenance of your <font SIZE="-1">HTML</font> files (and other assets) is easier.</p>
<h3>Which web framework should I use?</h3>
<p> There is no simple answer to this question. Perl frameworks can run everything from basic file servers and small scale intranets to massive multinational multilingual websites that are the core to international businesses. </p>
<p> Below is a list of a few frameworks with comments which might help you in making a decision, depending on your specific requirements. Start by reading the docs, then ask questions on the relevant mailing list or <font SIZE="-1">IRC</font> channel.</p>
<dl>
<dt>Catalyst</p>
<dd> Strongly object-oriented and fully-featured with a long development history and a large community and addon ecosystem. It is excellent for large and complex applications, where you have full control over the server.</p>
<dt>Dancer2</p>
<dd> Free of legacy weight, providing a lightweight and easy to learn <font SIZE="-1">API.</font> Has a growing addon ecosystem. It is best used for smaller projects and very easy to learn for beginners.</p>
<dt>Mojolicious</p>
<dd> Self-contained and powerful for both small and larger projects, with a focus on <font SIZE="-1">HTML5</font> and real-time web technologies such as WebSockets.</p>
<dt>Web::Simple</p>
<dd> Strongly object-oriented and minimal, built for speed and intended as a toolkit for building micro web apps, custom frameworks or for tieing together existing Plack-compatible web applications with one central dispatcher.</dl>
<p> All of these interact with or use Plack which is worth understanding the basics of when building a website in Perl (there is a lot of useful Plack::Middleware &lt;<a rel="nofollow" href="https://metacpan.org/search?q=plack%3A%3Amiddleware">https://metacpan.org/search?q=plack%3A%3Amiddleware</a>&gt;).</p>
<h3>What is Plack and <font SIZE="-1">PSGI</font>?</h3>
<p> <font SIZE="-1">PSGI</font> is the Perl Web Server Gateway Interface Specification, it is a standard that many Perl web frameworks use, you should not need to understand it to build a web site, the part you might want to use is Plack. </p>
<p> Plack is a set of tools for using the <font SIZE="-1">PSGI</font> stack. It contains middleware &lt;<a rel="nofollow" href="https://metacpan.org/search?q=plack%3A%3Amiddleware">https://metacpan.org/search?q=plack%3A%3Amiddleware</a>&gt; components, a reference server and utilities for Web application frameworks. Plack is like Ruby&#8217;s Rack or Python&#8217;s Paste for <font SIZE="-1">WSGI.</font> </p>
<p> You could build a web site using Plack and your own code, but for anything other than a very basic web site, using a web framework (that uses Plack) is a better option.</p>
<h3>How do I remove <font SIZE="-1">HTML</font> from a string?</h3>
<p> Use HTML::Strip, or HTML::FormatText which not only removes <font SIZE="-1">HTML</font> but also attempts to do a little simple formatting of the resulting plain text.</p>
<h3>How do I extract URLs?</h3>
<p> HTML::SimpleLinkExtor will extract URLs from <font SIZE="-1">HTML,</font> it handles anchors, images, objects, frames, and many other tags that can contain a <font SIZE="-1">URL.</font> If you need anything more complex, you can create your own subclass of HTML::LinkExtor or HTML::Parser. You might even use HTML::SimpleLinkExtor as an example for something specifically suited to your needs. </p>
<p> You can use URI::Find to extract URLs from an arbitrary text document.</p>
<h3>How do I fetch an <font SIZE="-1">HTML</font> file?</h3>
<p> (contributed by brian d foy) </p>
<p> Use the libwww-perl distribution. The LWP::Simple module can fetch web resources and give their content back to you as a string: </p>
<pre><code>
use LWP::Simple qw(get);
my $html = get("http://www.example.com/index.html");
</code></pre>
<p> It can also store the resource directly in a file: </p>
<p>use LWP::Simple qw(getstore);<br />
getstore(&#8220;http://www.example.com/index.html&#8221;, &#8220;foo.html&#8221;);</p>
<p> If you need to do something more complicated, you can use LWP::UserAgent module to create your own user-agent (e.g. browser) to get the job done. If you want to simulate an interactive web browser, you can use the WWW::Mechanize module.</p>
<h3>How do I automate an <font SIZE="-1">HTML</font> form submission?</h3>
<p> If you are doing something complex, such as moving through many pages and forms or a web site, you can use WWW::Mechanize. See its documentation for all the details. </p>
<p> If you&#8217;re submitting values using the <font SIZE="-1">GET</font> method, create a <font SIZE="-1">URL</font> and encode the form using the <tt>&quot;query_form&quot;</tt> method: </p>
<p>use LWP::Simple;<br />
use URI::URL;<br />
my $url = url(&#8216;L&lt;http://www.perl.com/cgi-bin/cpan_mod&#8217;) &gt; ;<br />
$url-&gt;query_form(module = &gt; &#8216;DB_File&#8217;, readme = &gt; 1);<br />
$content = get($url);</p>
<p> If you&#8217;re using the <font SIZE="-1">POST</font> method, create your own user agent and encode the content appropriately. </p>
<p>use HTTP::Request::Common qw(POST);<br />
use LWP::UserAgent;<br />
my $ua = LWP::UserAgent-&gt;new ();<br />
my $req = POST &#8216;L&lt;http://www.perl.com/cgi-bin/cpan_mod&#8217; &gt;,<br />
   [ module = &gt; &#8216;DB_File&#8217;, readme = &gt; 1 ];<br />
my $content = $ua-&gt;request($req)-&gt;as_string;</p>
<h3>How do I decode or create those %-encodings on the web?</h3>
<p> Most of the time you should not need to do this as your web framework, or if you are making a request, the <font SIZE="-1">LWP</font> or other module would handle it for you. </p>
<p> To encode a string yourself, use the URI::Escape module. The <tt>&quot;uri_escape&quot;</tt> function returns the escaped string: </p>
<p>my $original = &#8220;Colon : Hash # Percent %&#8221;;<br />
my $escaped = uri_escape($original);<br />
print &#8220;$escaped
&#8221;;<br />
#&#8217;Colon%20%3A%20Hash%20%23%20Percent%20%25&#8242;</p>
<p> To decode the string, use the <tt>&quot;uri_unescape&quot;</tt> function: </p>
<p>my $unescaped = uri_unescape($escaped);<br />
print $unescaped;<br />
#back to original</p>
<p> Remember not to encode a full <font SIZE="-1">URI,</font> you need to escape each component separately and then join them together.</p>
<h3>How do I redirect to another page?</h3>
<p> Most Perl Web Frameworks will have a mechanism for doing this, using the Catalyst framework it would be: </p>
<p>$c-&gt;res-&gt;redirect($url);<br />
$c-&gt;detach();</p>
<p> If you are using Plack (which most frameworks do), then Plack::Middleware::Rewrite is worth looking at if you are migrating from Apache or have <font SIZE="-1">URL</font>&#8216;s you want to always redirect.</p>
<h3>How do I put a password on my web pages?</h3>
<p> See if the web framework you are using has an authentication system and if that fits your needs. </p>
<p> Alternativly look at Plack::Middleware::Auth::Basic, or one of the other Plack authentication &lt;<a rel="nofollow" href="https://metacpan.org/search?q=plack+auth">https://metacpan.org/search?q=plack+auth</a>&gt; options.</p>
<h3>How do I make sure users can&#8217;t enter values into a form that causes my <font SIZE="-1">CGI</font> script to do bad things?</h3>
<p> (contributed by brian d foy) </p>
<p> You can&#8217;t prevent people from sending your script bad data. Even if you add some client-side checks, people may disable them or bypass them completely. For instance, someone might use a module such as <font SIZE="-1">LWP</font> to submit to your web site. If you want to prevent data that try to use <font SIZE="-1">SQL</font> injection or other sorts of attacks (and you should want to), you have to not trust any data that enter your program. </p>
<p> The perlsec documentation has general advice about data security. If you are using the <font SIZE="-1">DBI</font> module, use placeholder to fill in data. If you are running external programs with <tt>&quot;system&quot;</tt> or <tt>&quot;exec&quot;</tt>, use the list forms. There are many other precautions that you should take, too many to list here, and most of them fall under the category of not using any data that you don&#8217;t intend to use. Trust no one.</p>
<h3>How do I parse a mail header?</h3>
<p> Use the Email::MIME module. It&#8217;s well-tested and supports all the craziness that you&#8217;ll see in the real world (comment-folding whitespace, encodings, comments, etc.). </p>
<p>use Email::MIME;<br />
my $message = Email::MIME-&gt;new ($rfc2822);<br />
my $subject = $message-&gt;header(&#8216;Subject&#8217;);<br />
my $from = $message-&gt;header(&#8216;From&#8217;);</p>
<p> If you&#8217;ve already got some other kind of email object, consider passing it to Email::Abstract and then using its cast method to get an Email::MIME object: </p>
<p>my $abstract = Email::Abstract-&gt;new ($mail_message_object);<br />
my $email_mime_object = $abstract-&gt;cast(&#8216;Email::MIME&#8217;);</p>
<h3>How do I check a valid mail address?</h3>
<p> (partly contributed by Aaron Sherman) </p>
<p> This isn&#8217;t as simple a question as it sounds. There are two parts: </p>
<p> a) How do I verify that an email address is correctly formatted? </p>
<p> b) How do I verify that an email address targets a valid recipient? </p>
<p> Without sending mail to the address and seeing whether there&#8217;s a human on the other end to answer you, you cannot fully answer part <i>b</i>, but the Email::Valid module will do both part <i>a</i> and part <i>b</i> as far as you can in real-time. </p>
<p> Our best advice for verifying a person&#8217;s mail address is to have them enter their address twice, just as you normally do to change a password. This usually weeds out typos. If both versions match, send mail to that address with a personal message. If you get the message back and they&#8217;ve followed your directions, you can be reasonably assured that it&#8217;s real. </p>
<p> A related strategy that&#8217;s less open to forgery is to give them a <font SIZE="-1">PIN</font> (personal <font SIZE="-1">ID</font> number). Record the address and <font SIZE="-1">PIN</font> (best that it be a random one) for later processing. In the mail you send, include a link to your site with the <font SIZE="-1">PIN</font> included. If the mail bounces, you know it&#8217;s not valid. If they don&#8217;t click on the link, either they forged the address or (assuming they got the message) following through wasn&#8217;t important so you don&#8217;t need to worry about it.</p>
<h3>How do I decode a <font SIZE="-1">MIME/BASE64</font> string?</h3>
<p> The MIME::Base64 package handles this as well as the <font SIZE="-1">MIME/QP</font> encoding. Decoding base 64 becomes as simple as: </p>
<p>use MIME::Base64;<br />
my $decoded = decode_base64($encoded);</p>
<p> The Email::MIME module can decode base 64-encoded email message parts transparently so the developer doesn&#8217;t need to worry about it.</p>
<h3>How do I find the user&#8217;s mail address?</h3>
<p> Ask them for it. There are so many email providers available that it&#8217;s unlikely the local system has any idea how to determine a user&#8217;s email address. </p>
<p> The exception is for organization-specific email (e.g. foo [at] yourcompany.com) where policy can be codified in your program. In that case, you could look at <tt>$ENV</tt>{<font SIZE="-1">USER</font>}, <tt>$ENV</tt>{<font SIZE="-1">LOGNAME</font>}, and getpwuid($&lt;) in scalar context, like so: </p>
<pre>
  my $user_name = getpwuid($&lt;)
</pre>
<p> But you still cannot make assumptions about whether this is correct, unless your policy says it is. You really are best off asking the user.</p>
<h3>How do I send email?</h3>
<p> Use the Email::MIME and Email::Sender::Simple modules, like so: </p>
<p>#first, create your message<br />
my $message = Email::MIME-&gt;create(<br />
    header_str = &gt; [<br />
        From = &gt; &#8216;you [at] example.com&#8217;,<br />
        To = &gt; &#8216;friend [at] example.com&#8217;,<br />
        Subject = &gt; &#8216;Happy birthday!&#8217;,<br />
    ],<br />
    attributes = &gt; {<br />
                       encoding = &gt; &#8216;quoted-printable&#8217;,<br />
                       charset = &gt; &#8216;utf-8&#8217;,<br />
                   },<br />
    body_str = &gt; &#8220;Happy birthday to you!
&#8221;, );<br />
use Email::Sender::Simple qw(sendmail);<br />
sendmail($message);</p>
<p> By default, Email::Sender::Simple will try `sendmail` first, if it exists in your <tt>$PATH</tt>. This generally isn&#8217;t the case. If there&#8217;s a remote mail server you use to send mail, consider investigating one of the Transport classes. At time of writing, the available transports include:</p>
<dl>
<dt>Email::Sender::Transport::Sendmail</p>
<dd> This is the default. If you can use the <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1) or <code><a href="/docs/linux/man/1-mailx/">mailx</a></code>(1) program to send mail from the machine where your code runs, you should be able to use this.</p>
<dt>Email::Sender::Transport::SMTP</p>
<dd> This transport contacts a remote <font SIZE="-1">SMTP</font> server over <font SIZE="-1">TCP.</font> It optionally uses <font SIZE="-1">TLS</font> or <font SIZE="-1">SSL</font> and can authenticate to the server via <font SIZE="-1">SASL.</font></dl>
<p> Telling Email::Sender::Simple to use your transport is straightforward. </p>
<p>sendmail(<br />
    $message,<br />
    {<br />
        transport = &gt; $email_sender_transport_object,<br />
    });</p>
<h3>How do I use <font SIZE="-1">MIME</font> to make an attachment to a mail message?</h3>
<p> Email::MIME directly supports multipart messages. Email::MIME objects themselves are parts and can be attached to other Email::MIME objects. Consult the Email::MIME documentation for more information, including all of the supported methods and examples of their use.</p>
<h3>How do I read email?</h3>
<p> Use the Email::Folder module, like so: </p>
<p>use Email::Folder;<br />
my $folder = Email::Folder-&gt;new (&#8216;/path/to/email/folder&#8217;);<br />
while (my $message = $folder-&gt;next_message) {<br />
#next_message returns Email::Simple objects, but we want<br />
#Email::MIME objects as they&#8217;re more robust<br />
    my $mime = Email::MIME-&gt;new ($message-&gt;as_string);<br />
}</p>
<p> There are different classes in the Email::Folder namespace for supporting various mailbox types. Note that these modules are generally rather limited and only support <code>reading</code> rather than writing.</p>
<h3>How do I find out my hostname, domainname, or <font SIZE="-1">IP</font> address?</h3>
<p> (contributed by brian d foy) </p>
<p> The Net::Domain module, which is part of the Standard Library starting in Perl 5.7.3, can get you the fully qualified domain name (<font SIZE="-1">FQDN</font>), the host name, or the domain name. </p>
<p>use Net::Domain qw(hostname hostfqdn hostdomain);<br />
my $host = hostfqdn();</p>
<p> The Sys::Hostname module, part of the Standard Library, can also get the hostname: </p>
<p>use Sys::Hostname;<br />
$host = hostname();</p>
<p> The Sys::Hostname::Long module takes a different approach and tries harder to return the fully qualified hostname: </p>
<pre><code>
use Sys::Hostname::Long 'hostname_long';
my $hostname = hostname_long();
</code></pre>
<p> To get the <font SIZE="-1">IP</font> address, you can use the <tt>&quot;gethostbyname&quot;</tt> built-in function to turn the name into a number. To turn that number into the dotted octet form (a.b.c.d) that most people expect, use the <tt>&quot;inet_ntoa&quot;</tt> function from the Socket module, which also comes with perl. </p>
<pre>
    use Socket;
    my $address = inet_ntoa(
        scalar gethostbyname( $host || 'localhost' )
    );
</pre>
<h3>How do I fetch/put an (S)FTP file?</h3>
<p> Net::FTP, and Net::SFTP allow you to interact with <font SIZE="-1">FTP</font> and <font SIZE="-1">SFTP</font> (Secure <font SIZE="-1">FTP</font>) servers.</p>
<h3>How can I do <font SIZE="-1">RPC</font> in Perl?</h3>
<p> Use one of the <font SIZE="-1">RPC</font> modules( &lt;<a rel="nofollow" href="https://metacpan.org/search?q=RPC">https://metacpan.org/search?q=RPC</a>&gt; ).</p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Copyright (c) 1997-2010 Tom Christiansen, Nathan Torkington, and other authors as noted. All rights reserved. </p>
<p> This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Irrespective of its distribution, all code examples in this file are hereby placed into the public domain. You are permitted and encouraged to use this code in your own programs for fun or for profit as you see fit. A simple comment in the code giving credit would be courteous but is not required. </p>
<h2>Index</h2>
<dt><a href="#lbAZ">AUTHOR AND COPYRIGHT</a></p>
<dd></dl>
