---
title: "nocem(5)"
name: "nocem"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nocem/"
description: "perl-nocem – A NoCeM-on-spool implementation for INN 2.x"
---

<p>perl-nocem &#8211; A NoCeM-on-spool implementation for INN 2.x</p>
<h2>Synopsis</h2>
<p>perl-nocem</p>
<h2>Description</h2>
<p>NoCeM, which is pronounced <i>No See &#8216;Em</i>, is a protocol enabling authenticated third-parties to issue notices which can be used to cancel unwanted articles (like spam and articles in moderated newsgroups which were not approved by their moderators). It can also be used by readers as a <i>third-party killfile</i>. It is intended to eventually replace the protocol for third-party cancel messages. </p>
<p> <code>perl-nocem</code> processes third-party, PGP-signed article cancellation notices. It is possible not to honour all NoCeM notices but only those which are sent by people whom you trust (that is to say if you trust the <font SIZE="-1">PGP</font> key they use to sign their NoCeM notices). Indeed, it is up to you to decide whether you wish to honour their notices, depending on the criteria they use. </p>
<p> Processing NoCeM notices is easy to set up:</p>
<dl>
<dt>1.</p>
<dd>Import the keys of the NoCeM issuers you trust in order to check the authenticity of their notices. You can do: </p>
<pre> gpg --no-default-keyring --primary-keyring &lt;pathetc&gt;/pgp/ncmring.gpg --import &lt;key-file&gt;</pre>
<p>where &lt;pathetc&gt; is the value of the <i>pathetc</i> parameter set in <i>inn.conf</i> and &lt;key-file&gt; the file containing the key(s) to import. The keyring must be located in <i>pathetc</i>/pgp/ncmring.gpg (create the directory before using <code>gpg</code>). For old PGP-generated keys, you may have to use <code>&#8211;allow-non-selfsigned-uid</code> if they are not properly self-signed, but anyone creating a key really should self-sign the key. Current <font SIZE="-1">PGP</font> implementations do this automatically. </p>
<p> The keys of NoCeM issuers can be found in the web site of <i>The NoCeM Registry</i>: &lt;<a rel="nofollow" href="http://www.xs4all.nl/~rosalind/nocemreg/nocemreg.html">http://www.xs4all.nl/~rosalind/nocemreg/nocemreg.html</a>&gt;. You can even download there a unique file which contains all the keys.</p>
<dt>2.</p>
<dd>Create a <i>nocem.ctl</i> config file in <i>pathetc</i> indicating the NoCeM issuers and notices you want to follow. This permission file contains lines like: </p>
<pre> annihilator-1:*
 clewis [at] ferret.ocunix:mmf
 stephane [at] asynchrone:mmf,openproxy,spam</pre>
<p>This will remove all articles for which the issuer (first part of the line, before the colon <tt>&quot;:&quot;</tt>) has issued NoCeM notices corresponding to the criteria specified after the colon. </p>
<p> You will also find information about that on the web site of <i>The NoCeM Registry</i>.</p>
<dt>3.</p>
<dd>Add to the <i>newsfeeds</i> file an entry like this one in order to feed <code>perl-nocem</code> the NoCeM notices posted to alt.nocem.misc and news.lists.filters: </p>
<pre> nocem!\
 :!*,alt.nocem.misc,news.lists.filters\
 :Tc,Wf,Ap:&lt;pathbin&gt;/perl-nocem</pre>
<p>with the correct path to <code>perl-nocem</code>, located in &lt;pathbin&gt;. Then, reload the <i>newsfeeds</i> file (<tt>&quot;ctlinnd reload newsfeeds 'NoCeM channel feed'&quot;</tt>). </p>
<p> Note that you should at least carry news.lists.filters on your news server (or other newsgroups where NoCeM notices are sent) if you wish to process them.</p>
<dt>4.</p>
<dd>Everything should now work. However, do not hesitate to manually test <code>perl-nocem</code> with a NoCeM notice, using: </p>
<pre> grephistory '&lt;Message-ID&gt;' | perl-nocem</pre>
<p>Indeed, <code>perl-nocem</code> expects tokens on its standard input, and <code>grephistory</code> can easily give it the token of a known article, thanks to its Message-ID.</dl>
<p> When you have verified that everything works, you can eventually turn off regular spam cancels, if you want, not processing any longer cancels containing <tt>&quot;cyberspam&quot;</tt> in the Path: header (see the <i>refusecybercancels</i> parameter in <i>inn.conf</i>).</p>
<h2>Files</h2>
<dl>
<dt><i>pathbin</i>/perl-nocem</p>
<dd>The Perl script itself used to process NoCeM notices.</p>
<dt><i>pathetc</i>/nocem.ctl</p>
<dd>The configuration file which specifies the NoCeM notices to be processed.</p>
<dt><i>pathetc</i>/pgp/ncmring.gpg</p>
<dd>The keyring which contains the public keys of trusted NoCeM issuers.</dl>
<h2>Bugs</h2>
<p>The Subject: header is not checked for the @@NCM string and there is no check for the presence of the References: header. </p>
<p> The Newsgroups: pseudo header is not checked, but this can be done in <i>local_want_cancel_id()</i>. </p>
<p> The Hierarchies: header is ignored.</p>
<h2>History</h2>
<p>Copyright 2000 by Miquel van Smoorenburg &lt;miquels [at] cistron.nl&gt;. </p>
<p> Copyright 2001 by Marco d&#8217;Itri &lt;md [at] linux.it&gt;. </p>
<p> $Id: perl-nocem.in 8419 2009-04-13 09:10:38Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-gpgv/">gpgv</a></i>(1), <i><a href="/docs/linux/man/1-grephistory/">grephistory</a></i>(1), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/1-pgp/">pgp</a></i>(1). </p>
