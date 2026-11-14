---
title: "stompclt(1)"
name: "stompclt"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stompclt/"
description: "stompclt – versatile STOMP client"
---

<h2 class="name">NAME</h2>
<p> stompclt &#8211; versatile STOMP client </p>
<h2>SYNOPSIS</h2>
<p> <code>stompclt</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>stompclt</code> is a versatile tool to interact with messaging brokers speaking <font SIZE="-1">STOMP</font> and/or message queues (see Messaging::Message::Queue) on disk. </p>
<p> It receives messages (see Messaging::Message) from an incoming module, optionally massaging them (i.e. filtering and/or modifying), and sends them to an outgoing module. Depending on which modules are used, the tool can perform different operations. </p>
<p> Here are the supported incoming modules:</p>
<dl>
<dt>&bull;</p>
<dd> broker: connect to a messaging broker using <font SIZE="-1">STOMP,</font> subscribe to one or more destinations and receive the messages sent by the broker</p>
<dt>&bull;</p>
<dd> queue: read messages from a message queue on disk</dl>
<p> Here are the supported outgoing modules:</p>
<dl>
<dt>&bull;</p>
<dd> broker: connect to a messaging broker using <font SIZE="-1">STOMP</font> and send the messages</p>
<dt>&bull;</p>
<dd> queue: store the messages in a message queue on disk</dl>
<p> Here are some frequently used combinations:</p>
<dl>
<dt>&bull;</p>
<dd> <i>incoming broker + outgoing queue</i>: drain some destinations, storing the messages on disk</p>
<dt>&bull;</p>
<dd> <i>incoming queue + outgoing broker</i>: (re-)send messages that have been previously stored on disk, optionally with modifications (such as altering the destination)</p>
<dt>&bull;</p>
<dd> <i>incoming broker + outgoing broker</i>: shovel messages from one broker to another</dl>
<p> See the &#8220;<font SIZE="-1">EXAMPLES&#8221;</font> sections for concrete examples.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;callback-code</code> <i></i><font SIZE="-1"><i>CODE</i></font><i></i></p>
<dd> execute the given Perl code on each message, see the &#8220;<font SIZE="-1">CALLBACK&#8221;</font> section below for more information</p>
<dt><code>&#8211;callback-data</code> <i>KEY=VALUE&#8230;</i></p>
<dd> pass this data to the user supplied callback code, see the &#8220;<font SIZE="-1">CALLBACK&#8221;</font> section below for more information</p>
<dt><code>&#8211;callback-path</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> execute the Perl code in the given file on each message, see the &#8220;<font SIZE="-1">CALLBACK&#8221;</font> section below for more information</p>
<dt><code>&#8211;config</code>, <code>&#8211;conf</code>, <code>&#8211;cfg</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> use the given configuration file, see the &#8220;<font SIZE="-1">CONFIGURATION FILE&#8221;</font> section below for more information</p>
<dt><code>&#8211;config-general</code> <i>KEY=VALUE&#8230;</i></p>
<dd> use the given Config::General options when creating the configuration parser</p>
<dt><code>&#8211;count</code>, <code>-c</code> <i></i><font SIZE="-1"><i>INTEGER</i></font><i></i></p>
<dd> process at most the given number of messages; note: when using an incoming broker, to avoid consuming more messages, it is recommended to enable the <code>&#8211;reliable</code> option</p>
<dt><code>&#8211;daemon</code> | <code>&#8211;no-daemon</code></p>
<dd> detach <code>stompclt</code> so that it becomes a daemon running in the background; debug, warning and error messages will get sent to syslog; this option can be negated</p>
<dt><code>&#8211;debug</code>, <code>-d</code></p>
<dd> show debugging information</p>
<dt><code>&#8211;duration</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> process messages during at most the given number of seconds and then stop; can be fractional</p>
<dt><code>&#8211;heart-beat</code> | <code>&#8211;no-heart-beat</code></p>
<dd> enable <font SIZE="-1">STOMP 1.1</font> heart-beats between <code>stompclt</code> and the broker(s); this option can be negated</p>
<dt><code>&#8211;help</code>, <code>-h</code>, <code>-?</code></p>
<dd> show some help</p>
<dt><code>&#8211;incoming-broker-auth</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> use this authentication string (see Authen::Credential) to authenticate to the incoming broker; this option can be given multiple times</p>
<dt><code>&#8211;incoming-broker-connect</code> <i>KEY=VALUE&#8230;</i></p>
<dd> use these options in the <font SIZE="-1">STOMP CONNECT</font> frame sent to the incoming broker</p>
<dt><code>&#8211;incoming-broker-sockopts</code> <i>KEY=VALUE&#8230;</i></p>
<dd> use these socket options when connecting to the incoming broker</p>
<dt><code>&#8211;incoming-broker-stomp-debug</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> set the <font SIZE="-1">STOMP</font> debug flags (see Net::STOMP::Client) when interacting with the incoming broker</p>
<dt><code>&#8211;incoming-broker-type</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> set the incoming broker type; this can be useful when using <font SIZE="-1">STOMP</font> features which are broker specific</p>
<dt><code>&#8211;incoming-broker-uri</code> <i></i><font SIZE="-1"><i>URI</i></font><i></i></p>
<dd> use this connection <font SIZE="-1">URI </font>(see Net::STOMP::Client) to connect to the incoming broker</p>
<dt><code>&#8211;incoming-queue</code> <i>KEY=VALUE&#8230;</i></p>
<dd> read incoming messages from the given message queue (see Messaging::Message::Queue)</p>
<dt><code>&#8211;lazy</code> | <code>&#8211;no-lazy</code></p>
<dd> initialize the outgoing module only after having received the first message; this option can be negated</p>
<dt><code>&#8211;list</code>, <code>-l</code></p>
<dd> show all supported options</p>
<dt><code>&#8211;loop</code> | <code>&#8211;no-loop</code></p>
<dd> when using an incoming message queue, loop over it; this option can be negated</p>
<dt><code>&#8211;manual</code>, <code>-m</code></p>
<dd> show this manual</p>
<dt><code>&#8211;outgoing-broker-auth</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> use this authentication string (see Authen::Credential) to authenticate to the outgoing broker; this option can be given multiple times</p>
<dt><code>&#8211;outgoing-broker-connect</code> <i>KEY=VALUE&#8230;</i></p>
<dd> use these options in the <font SIZE="-1">STOMP CONNECT</font> frame sent to the outgoing broker</p>
<dt><code>&#8211;outgoing-broker-sockopts</code> <i>KEY=VALUE&#8230;</i></p>
<dd> use these socket options when connecting to the outgoing broker</p>
<dt><code>&#8211;outgoing-broker-stomp-debug</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> set the <font SIZE="-1">STOMP</font> debug flags (see Net::STOMP::Client) when interacting with the outgoing broker</p>
<dt><code>&#8211;outgoing-broker-type</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> set the outgoing broker type; this can be useful when using <font SIZE="-1">STOMP</font> features which are broker specific</p>
<dt><code>&#8211;outgoing-broker-uri</code> <i></i><font SIZE="-1"><i>URI</i></font><i></i></p>
<dd> use this connection <font SIZE="-1">URI </font>(see Net::STOMP::Client) to connect to the outgoing broker</p>
<dt><code>&#8211;outgoing-queue</code> <i>KEY=VALUE&#8230;</i></p>
<dd> store outgoing messages into the given message queue (see Messaging::Message::Queue)</p>
<dt><code>&#8211;pidfile</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> use this pid file</p>
<dt><code>&#8211;prefetch</code> <i></i><font SIZE="-1"><i>INTEGER</i></font><i></i></p>
<dd> set the prefetch value (i.e. the maximum number of messages to received without acknowledging them) on the incoming broker</p>
<dt><code>&#8211;quit</code></p>
<dd> tell another instance of <code>stompclt</code> (identified by its pid file, as specified by the <code>&#8211;pidfile</code> option) to quit</p>
<dt><code>&#8211;reliable</code> | <code>&#8211;no-reliable</code></p>
<dd> use <font SIZE="-1">STOMP</font> features for more reliable messaging (i.e. client side acknowledgments and receipts) at the cost of less performance; this option can be negated</p>
<dt><code>&#8211;remove</code> | <code>&#8211;no-remove</code></p>
<dd> when using an incoming message queue, remove the processed messages; this option can be negated</p>
<dt><code>&#8211;statistics</code>, <code>-s</code> | <code>&#8211;no-statistics</code></p>
<dd> report statistics at the end of the execution; this option can be negated</p>
<dt><code>&#8211;status</code></p>
<dd> get the status of another instance of <code>stompclt</code> (identified by its pid file, as specified by the <code>&#8211;pidfile</code> option); the exit code will be zero if the instance is alive and non-zero otherwise</p>
<dt><code>&#8211;subscribe</code> <i>KEY=VALUE&#8230;</i></p>
<dd> use these options in the <font SIZE="-1">STOMP SUBSCRIBE</font> frame used with the incoming broker; this option can be given multiple times</p>
<dt><code>&#8211;timeout-broker</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> use this timeout when interacting with the broker (e.g. getting receipts back); can be fractional</p>
<dt><code>&#8211;timeout-client</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> use this timeout for the client heart-beat; can be fractional (default: 40)</p>
<dt><code>&#8211;timeout-connect</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> use this timeout when connecting to the broker; can be fractional</p>
<dt><code>&#8211;timeout-disconnect</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> use this timeout when disconnecting from the broker; can be fractional (default: 60)</p>
<dt><code>&#8211;timeout-flush</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> use this timeout when attempting to send the last bytes to the broker just before disconnecting; can be fractional (default: 60)</p>
<dt><code>&#8211;timeout-inactivity</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> use this timeout in the incoming module to stop <code>stompclt</code> when no new messages have been received (aka drain mode); can be fractional</p>
<dt><code>&#8211;timeout-linger</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> when stopping <code>stompclt</code>, use this timeout to finish interacting with the broker; can be fractional</p>
<dt><code>&#8211;timeout-server</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> use this timeout for the server heart-beat; can be fractional (default: 10)</p>
<dt><code>&#8211;timeout-status</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> use this timeout when checking the status with <code>&#8211;status</code>; can be fractional</p>
<dt><code>&#8211;unsubscribe</code> <i>KEY=VALUE&#8230;</i></p>
<dd> use these options in the <font SIZE="-1">STOMP UNSUBSCRIBE</font> frame used with the incoming broker; this option can be given multiple times and should match the <code>&#8211;subscribe</code> options</p>
<dt><code>&#8211;version</code></p>
<dd> display version information</p>
<dt><code>&#8211;window</code> <i></i><font SIZE="-1"><i>INTEGER</i></font><i></i></p>
<dd> keep at most the given number of not-yet-acknowledged messages in memory</dl>
<p> To list all the available options in a compact form, type: </p>
<pre>
  $ stompclt -l
</pre>
<h2>CONFIGURATION FILE</h2>
<p> <code>stompclt</code> can read its options from a configuration file. For this, the Config::General module is used and the option names are the same as on the command line. For instance: </p>
<pre>
  daemon = true
  pidfile = /var/run/stompclt.pid
  incoming-queue = path=/var/spool/stompclt
  outgoing-broker-uri = <a href="stomp://broker.acme.com:6163">stomp://broker.acme.com:6163</a>
  outgoing-broker-auth = &quot;plain name=guest pass=guest&quot;
</pre>
<p> Alternatively, options can be nested: </p>
<pre>
  &lt;outgoing-broker&gt;
      uri = <a href="stomp://broker.acme.com:6163">stomp://broker.acme.com:6163</a>
      auth = &quot;plain name=guest pass=guest&quot;
  &lt;/outgoing-broker&gt;
</pre>
<p> Or even: </p>
<pre>
  &lt;outgoing&gt;
      &lt;broker&gt;
          uri = <a href="stomp://broker.acme.com:6163">stomp://broker.acme.com:6163</a>
          &lt;auth&gt;
              scheme = plain
              name = guest
              pass = guest
          &lt;/auth&gt;
      &lt;/broker&gt;
  &lt;/outgoing&gt;
</pre>
<p> The options specified on the command line have precedence over the ones found in the configuration file.</p>
<h2>CALLBACK</h2>
<p> <code>stompclt</code> can be given Perl code to execute on all processed messages. This can be used for different purposes:</p>
<dl>
<dt>&bull;</p>
<dd> massaging: the code can change any part of the message, including setting or removing header fields</p>
<dt>&bull;</p>
<dd> filtering: the code can decide if the message must be given to the outgoing module or not</p>
<dt>&bull;</p>
<dd> displaying: the code can print any part of the message</p>
<dt>&bull;</p>
<dd> copying: the code can store a copy of the message into files or message queues</dl>
<p> To use callbacks, the <code>&#8211;callback-path</code> or <code>&#8211;callback-code</code> option must be used. The Perl code must provide functions with the following signature:</p>
<dl>
<dt>start(<font SIZE="-1">DATA</font>)</p>
<dd> (optional) this will be called when the program starts, with the supplied data (see the <code>&#8211;callback-data</code> option) as a hash reference</p>
<dt>check(<font SIZE="-1">MESSAGE</font>)</p>
<dd> (mandatory) this will be called when the program has one message to process; it will be given the message (see Messaging::Message) and must return either a message (it could be the same one or a new one) or a string describing why the message has been dropped</p>
<dt><i>idle()</i></p>
<dd> (optional) this will be called when the program has no message to process</p>
<dt><i>stop()</i></p>
<dd> (optional) this will be called when the program stops</dl>
<p> The code can be put in a file, on the command line or in the <code>stompclt</code> configuration file, using the &#8220;here document&#8221; syntax. </p>
<p> Here is an example (to be put in the <code>stompclt</code> configuration file) that prints on stdout a <font SIZE="-1">JSON</font> array of messages: </p>
<pre><code>
callback - code = &lt;&lt; EOF
                      my($count);
sub start($)
{
    $count = 0;
}
sub check($)
{
    my($msg) = @_;
    print($count++ ? "," : "[");
    print($msg-&gt;serialize(), "
");
    return ($msg);
}
sub stop()
{
    print($count ? "]
" : "[]
");
}
EOF
</code></pre>
<p> For simple callback code that only needs the <tt>&quot;check&quot;</tt> subroutine, it is enough to supply the &#8220;inside code&#8221;. If the subroutine definition is missing, the supplied code will be wrapped with: </p>
<p>sub check($)<br />
{<br />
    my($msg) = @_;<br />
    local *hdr = $msg-&gt;header();<br />
    local *bdy = $msg-&gt;body_ref();<br />
    &#8230; your code goes here&#8230; return ($msg);<br />
}</p>
<p> This allows for instance to remove the <tt>&quot;message-id&quot;</tt> header with something like: </p>
<pre>
  $ stompclt ... --callback-code 'delete($hdr{&quot;message-id&quot;})'
</pre>
<p> Or to filter on message bodies with: </p>
<pre>
  $ stompclt ... --callback-code 'return(&quot;skip&quot;) unless $bdy =~ /error/'
</pre>
<h2>SUBSCRIPTIONS</h2>
<p> In the case of an incoming broker, <code>stompclt</code> deals with the subscriptions defined by the <code>&#8211;subscribe</code> option. </p>
<p> Regardless of the <code>&#8211;reliable</code> option, subscriptions are always made using receipts. Also, if missing, an <tt>&quot;id&quot;</tt> header is always added. </p>
<p> Here is for instance how to create a named durable topic subscription using Apollo: </p>
<pre>
  $ stompclt ... --subscribe 'destination=/topic/foo persistent=true id=mysub'
</pre>
<p> By default, when it finishes, <code>stompclt</code> does not unsubscribe. It simply disconnects from the broker and the latter will perform the necessary cleanup when terminating the <font SIZE="-1">STOMP</font> connection. </p>
<p> If the <code>&#8211;unsubscribe</code> option is given, even if it is empty, <code>stompclt</code> will explicitly unsubscribe before disconnecting, also using receipts. </p>
<p> Here is for instance how to destroy, when <code>stompclt</code> ends, the durable topic subscription created above: </p>
<pre>
  $ stompclt ... --unsubscribe 'persistent=true'
</pre>
<p> There is no need to give the subscription <tt>&quot;id&quot;</tt> in the <code>&#8211;unsubscribe</code> option because, by default, it comes from the matching <code>&#8211;subscribe</code> option.</p>
<h2>UDP SUPPORT</h2>
<p> <code>stompclt</code> has experimental <font SIZE="-1">UDP</font> support (outgoing only). This has been tested with Apollo. </p>
<p> To use it, simply specify an outgoing <font SIZE="-1">URI</font> that uses <font SIZE="-1">UDP</font> such as: </p>
<pre>
  $ stompclt ... --outgoing-broker-uri <a href="udp://broker.acme.com:6163">udp://broker.acme.com:6163</a>
</pre>
<p> Features such as authentication, heart beating, reliability and socket options are not supported over <font SIZE="-1">UDP.</font></p>
<h2>EXAMPLES</h2>
<h3><font SIZE="-1">SENDING</font></h3>
<p> Here is an example of a configuration file for a message sender daemon (from queue to broker), forcing the <tt>&quot;persistent&quot;</tt> header to <tt>&quot;true&quot;</tt> (something which is highly recommended for reliable messaging) and setting the destination: </p>
<p>#define the source message queue<br />
&lt;incoming &#8211; queue&gt; path = / var / spool / sender&lt;/ incoming &#8211; queue&gt;<br />
#modify the message header on the fly<br />
                                              callback &#8211;<br />
                          code =<br />
                              &lt;&lt; EOF<br />
                                     $hdr{destination} = &#8220;/queue/app1.data&#8221;;<br />
$hdr{persistent} = &#8220;true&#8221;;<br />
EOF<br />
#define the destination broker<br />
    &lt;outgoing &#8211; broker&gt;<br />
        uri = &#8220;stomp://broker.acme.com:6163&#8221; &lt; / outgoing &#8211; broker &gt;<br />
#miscellaneous options<br />
              reliable = true pidfile = / var / run / sender.pid daemon = true loop = true remove = true</p>
<h3><font SIZE="-1">RECEIVING</font></h3>
<p> Here is an example of a configuration file for a message receiver daemon (from broker to queue): </p>
<p>#define the source broker<br />
&lt;incoming &#8211; broker&gt; uri = &#8220;stomp://broker.acme.com:6163&#8221; &lt; auth &gt;<br />
                          scheme = plain<br />
                              name = receiver<br />
                                  pass = secret&lt;/ auth&gt;<br />
    &lt;/ incoming &#8211; broker&gt;<br />
#define the subscriptions<br />
    &lt;subscribe&gt;<br />
        destination = / queue / app1.data&lt;/ subscribe&gt;&lt;subscribe&gt; destination = / queue / app2.data&lt;/ subscribe&gt;<br />
#define the destination message queue<br />
                                                                                          &lt;outgoing &#8211; queue&gt; path = / var / spool / receiver&lt;/ outgoing &#8211; queue&gt;<br />
#miscellaneous options<br />
                                                                                                                                        pidfile = / var / run / receiver.pid daemon = true</p>
<p> Here is how to use the configuration file above with some options overridden on the command line to drain the queues in the foreground: </p>
<pre>
  $ stompclt --config test.conf --no-daemon --timeout-inactivity 10
</pre>
<h3><font SIZE="-1">SHOVELING</font></h3>
<p> Here is an example of a configuration file for a message shoveler (from broker to broker), clearing some headers on the fly so that messages can be replayed safely: </p>
<p>#define the source broker<br />
&lt;incoming &#8211; broker&gt; uri = &#8220;stomp://broker.acme.com:6163&#8221; &lt; / incoming &#8211; broker &gt;<br />
#define the subscriptions<br />
                          &lt;subscribe&gt;<br />
                              destination = / queue / app1.data&lt;/ subscribe&gt;&lt;subscribe&gt; destination = / queue / app2.data&lt;/ subscribe&gt;<br />
#define the destination broker<br />
                                                                                                                &lt;outgoing &#8211; broker&gt; uri = &#8220;stomp://dev-broker.acme.com:6163&#8221; &lt; / outgoing &#8211; broker &gt;<br />
#modify the message so that it can be replayed<br />
                                                                                                                                          callback &#8211; code =<br />
                                                                                                                                              &lt;&lt; EOF foreach my $name(qw(message &#8211; id timestamp expires))<br />
{<br />
    delete ($hdr{$name});<br />
}<br />
EOF</p>
<h3><font SIZE="-1">TAPPING</font></h3>
<p> Callback code can also be used to tap messages, i.e. get a copy of all messages processed by <code>stompclt</code>. Here is some callback code for this purpose that could for instance be merged with the shoveling code above. It also shows how to use the <code>&#8211;callback-data</code> option: </p>
<pre><code>
callback - code = &lt;&lt; EOF
                      my($queue);
sub start($)
{
    my($data) = @_;
    $queue = Messaging::Message::Queue-&gt;new ($data);
}
sub check($)
{
    my($msg) = @_;
    $queue-&gt;add_message($msg);
    return ($msg);
}
EOF
</code></pre>
<p> Callback data must be given to specify which message queue to use: </p>
<pre>
  $ stompclt --config tap.conf --callback-data &quot;path=/tmp/tap type=DQS&quot;
</pre>
<h2>SEE ALSO</h2>
<p> Authen::Credential, Config::General, Messaging::Message, Messaging::Message::Queue, Net::STOMP::Client.</p>
<h2>AUTHOR</h2>
<p> Lionel Cons &lt;<a rel="nofollow" href="http://cern.ch/lionel.cons">http://cern.ch/lionel.cons</a>&gt; </p>
<p> Copyright (C) <font SIZE="-1">CERN 2012-2016</font> </p>
<h2>Index</h2>
<dt><a href="#lbAO">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAP">AUTHOR</a></p>
<dd></dl>
