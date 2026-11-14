---
title: "pigeonhole(7)"
name: "pigeonhole"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pigeonhole/"
description: "pigeonhole – Overview of the Pigeonhole project’s Sieve support for the Dovecot secure IMAP and POP3 server"
---

<p>pigeonhole &#8211; Overview of the Pigeonhole project&#8217;s Sieve support for the Dovecot secure IMAP and POP3 server</p>
<h2>Description</h2>
<p>The Pigeonhole project &lt;<a rel="nofollow" href="http://pigeonhole.dovecot.org">http://pigeonhole.dovecot.org</a>&gt; adds support for the Sieve language (RFC 5228) and the ManageSieve protocol (RFC 5804) to the Dovecot Secure IMAP and POP3 Server (<code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1)). In the literal sense, a pigeonhole is a a hole or recess inside a dovecot for pigeons to nest in. It is, however, also the name for one of a series of small, open compartments in a cabinet used for filing or sorting mail. As a verb, it describes the act of putting an item into one of those pigeonholes. The name &quot;Pigeonhole&quot; therefore well describes an important part of the functionality that this project adds to Dovecot: sorting and filing e-mail messages. </p>
<p> The Sieve language is used to specify how e-mail needs to be processed. By writing Sieve scripts, users can customize how messages are delivered, e.g. whether they are forwarded or stored in special folders. Unwanted messages can be discarded or rejected, and, when the user is not available, the Sieve interpreter can send an automated reply. Above all, the Sieve language is meant to be simple, extensible and system independent. And, unlike most other mail filtering script languages, it does not allow users to execute arbitrary programs. This is particularly useful to prevent virtual users from having full access to the mail store. The intention of the language is to make it impossible for users to do anything more complex (and dangerous) than write simple mail filters. </p>
<p> Using the ManageSieve protocol, users can upload their Sieve scripts remotely, without needing direct filesystem access through FTP or SCP. Additionally, a ManageSieve server always makes sure that uploaded scripts are valid, preventing compile failures at mail delivery. </p>
<p> The Pigeonhole project provides the following items:</p>
<dl>
<dt>&bull;</p>
<dd>The LDA Sieve plugin for Dovecot&#8217;s Local Delivery Agent (LDA) (<code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1)) that facilitates the actual Sieve filtering upon delivery.</p>
<dt>&bull;</p>
<dd>The ManageSieve Service that implements the ManageSieve protocol through which users can remotely manage Sieve scripts on the server.</p>
<dt>&bull;</p>
<dd>Command line tools that provide the means to manually compile, analyse and test Sieve scripts.</dl>
<p> The functionality and configuration of the LDA Sieve plugin and the ManageSieve service is described in detail in the README and INSTALL files contained in the Pigeonhole package and in the Dovecot Wiki &lt;<a rel="nofollow" href="http://wiki2.dovecot.org/Pigeonhole">http://wiki2.dovecot.org/Pigeonhole</a>&gt;. </p>
<p> The following command line tools are available:</p>
<dl>
<dt><code><a href="/docs/linux/man/1-sievec/">sievec</a></code>(1)</p>
<dd>Compiles Sieve scripts into a binary representation for later execution.</p>
<dt><code><a href="/docs/linux/man/1-sieve-test/">sieve-test</a></code>(1)</p>
<dd>The universal Sieve test tool for testing the effect of a Sieve script on a particular message.</p>
<dt><code><a href="/docs/linux/man/1-sieve-filter/">sieve-filter</a></code>(1)</p>
<dd>Filters all messages in a particular source mailbox through a Sieve script.</p>
<dt><code><a href="/docs/linux/man/1-sieve-dump/">sieve-dump</a></code>(1)</p>
<dd>Dumps the content of a Sieve binary file for (development) debugging purposes.</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting Dovecot and Pigeonhole bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>Author</h2>
<p>Pigeonhole &lt;<a rel="nofollow" href="http://pigeonhole.dovecot.org">http://pigeonhole.dovecot.org</a>&gt; and its manual pages were written by the Pigeonhole authors &lt;<a rel="nofollow" href="http://pigeonhole.dovecot.org/doc/AUTHORS">http://pigeonhole.dovecot.org/doc/AUTHORS</a>&gt;, mainly Stephan Bosch &lt;stephan at rename-it.nl&gt;, and are licensed under the terms of the LGPLv2.1 license, which is the same license as Dovecot, see &lt;<a rel="nofollow" href="http://dovecot.org/doc/COPYING">http://dovecot.org/doc/COPYING</a>&gt; for details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1), <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1), <code><a href="/docs/linux/man/1-sieve-dump/">sieve-dump</a></code>(1), <code><a href="/docs/linux/man/1-sieve-test/">sieve-test</a></code>(1), <code><a href="/docs/linux/man/1-sieve-filter/">sieve-filter</a></code>(1), <code><a href="/docs/linux/man/1-sievec/">sievec</a></code>(1) Additional resources:</p>
<dl>
<dt>Dovecot website</p>
<dd><a rel="nofollow" href="http://www.dovecot.org">http://www.dovecot.org</a></p>
<dt>Dovecot v2.x Wiki</p>
<dd><a rel="nofollow" href="http://wiki2.dovecot.org/Pigeonhole">http://wiki2.dovecot.org/Pigeonhole</a></p>
<dt>Pigeonhole website</p>
<dd><a rel="nofollow" href="http://pigeonhole.dovecot.org">http://pigeonhole.dovecot.org</a> </p>
