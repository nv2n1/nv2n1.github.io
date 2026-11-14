---
title: "mimedefang-notify(7)"
name: "mimedefang-notify"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mimedefang-notify/"
description: "mimedefang-notify – Conventions used by"
---

<p>mimedefang-notify &#8211; Conventions used by <code></p>
<p><a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a></code>(8) to notify an external program of state changes. </p>
<h2>Description</h2>
<p>If you supply the <code>-O</code> option to <code>mimedefang-multiplexor</code>, then it allows external programs to connect to a socket and be notified of certain state changes in the multiplexor. The external programs can react in whatever way they choose to these state changes. The external program that listens for state changes is referred to as a <i>listener</i>. </p>
<h2>Notification Overview</h2>
<p>From the point of view of a listener, notification works like this: </p>
<p> 1) The listener connects to a TCP or UNIX-domain socket. </p>
<p> 2) The listener informs <code>mimedefang-multiplexor</code> of the <i>message types</i> it is interested in. </p>
<p> 3) The listener loops, reading messages from the socket and reacting to them.</p>
<h2>Messages</h2>
<p>Each message from the multiplexor normally consists of a single upper-case letter, possibly followed by a space and some arguments, and then followed by a newline. </p>
<p> Two special messages are &quot;*OK&quot; followed by a newline, which is issued when a listener first connects, and &quot;*ERR&quot; followed by some text and a newline, which is issued when an error occurs. </p>
<p> The normal messages are: </p>
<dl>
<dt><code>B</code></p>
<dd>This message is issued whenever a slave is killed because of a busy timeout. </p>
<dt><code>F</code> <i>n</i></p>
<dd>This message is issued whenever the number of free slaves changes. The parameter <i>n</i> is the number of free slaves. </p>
<dt><code>R</code></p>
<dd>This message is issued whenever someone has forced a filter reread. </p>
<dt><code>S</code> <i>n</i> <i>nmsg</i></p>
<dd>This message is issued whenever slave <i>n</i>&#8216;s status tag changes. The status tag is a string indicating what the slave is currently doing; the <code>-Z</code> option to the multiplexor allows the Perl code to update the status tag so you have a good idea what each slave is doing. </p>
<dt><code>U</code></p>
<dd>This message is issued whenever a slave has died unexpectedly. </p>
<dt><code>Y</code></p>
<dd>This message is issued whenever the number of free slaves changes from zero to non-zero. </p>
<dt><code>Z</code></p>
<dd>This message is issued whenever the number of free slaves falls to zero. </p>
</dl>
<h2>Expressing Interest</h2>
<p>A listener does not receive any messages until it has <i>expressed interest</i> in various message types. To express interest, the listener should send a question mark (&quot;?&quot;) followed by the types of messages it is interested in, followed by a newline over the socket. For example, a listener interested in the R and F messages would send this line: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>?RF</p>
<p> A listener interested in every possible message type should send: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>?*</p>
<p> Once a listener has expressed interest, it may receive messages at any time, and should monitor the socket for messages. </p>
<p> Note that a listener <i>always</i> receives the special messages &quot;*OK&quot; and &quot;*ERR&quot;, even if it has not expressed interest in them.</p>
<h2>Example</h2>
<p>The following Perl script implements a listener that, on Linux, rejects new SMTP connections if all slaves are busy, and accepts them again once a slave is free. Existing SMTP connections are not shut down; the system merely refuses new connections if all the slaves are busy. This script assumes that you have used the <code>-O inet:4567</code> option to <code>mimedefang-multiplexor</code>. </p>
<pre><code>#!/ usr / bin / perl - w
#
#On Linux, prepare to use this script like this:
#/ sbin / iptables - N smtp_connect
#/ sbin / iptables - A INPUT -- proto tcp -- dport 25 -- syn - j smtp_connect
#Then run the script as root.

use IO::Socket::INET;

sub no_free_slaves
{
    print STDERR &quot;No free slaves!
&quot;;
    system(&quot;/sbin/iptables -A smtp_connect -j REJECT&quot;);
}

sub some_free_slaves
{
    print STDERR &quot;Some free slaves.
&quot;;
    system(&quot;/sbin/iptables -F smtp_connect&quot;);
}

sub main
{
    my $sock;

    $sock = IO::Socket::INET-&gt;new (PeerAddr = &gt; '127.0.0.1',
                                   PeerPort = &gt; '4567',
                                   Proto = &gt; 'tcp');
#We are only interested in Y and Z messages
    print $sock &quot;?YZ
&quot;;
    $sock-&gt;flush();
    while (&lt;$sock&gt;) {
        if (/ ^Z /) {
            no_free_slaves();
        }
        if (/ ^Y /) {
            some_free_slaves();
        }
    }

#EOF from multiplexor ? ? Better undo firewalling
    system(&quot;/sbin/iptables -F smtp_connect&quot;);
}

main();
</code></pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mimedefang-pl/">mimedefang.pl</a>(8), <a href="/docs/linux/man/8-mimedefang/">mimedefang</a>(8), <a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a>(8), <a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a>(5) </p>
