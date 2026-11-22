---

title: "mrtg-faq(1)"
name: "mrtg-faq"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-faq/"
description: "mrtg-faq – How to get help if you have problems with MRTG"
---

<p> mrtg-faq &#8211; How to get help if you have problems with MRTG </p>
<h2>SYNOPSIS</h2>
<p> MRTG seems to raise a lot of questions. There are a number of resources apart from the documentation where you can find help for mrtg.</p>
<h2>FAQ</h2>
<p> In the following sections you&#8217;ll find some additonal Frequently Asked Questions, with Answers.</p>
<h3>Why is there no @#$% (my native language) version of MRTG?</h3>
<p> Nobody has contributed a <i>@#$%.pmd</i> file yet. Go into the <i>mrtg-2.17.4/translate</i> directory and create your own translation file. When you are happy with it send it to me for inclusion with the next mrtg release.</p>
<h3>I need a script to make mrtg work with my xyz device.</h3>
<p> Probably this has already been done. Check the stuff in the <i>mrtg-2.17.4/contrib</i> directory. There is a file called <i>00INDEX</i> in that directory which tells what you can find in there.</p>
<h3>How does this SNMP thing work</h3>
<p> There are many resources on the net that explain SNMP. Take a look at this article from the Linux Journal by David Guerrero </p>
<pre>
 <a rel="nofollow" href="http://www.david-guerrero.com/papers/snmp/">http://www.david-guerrero.com/papers/snmp/</a>
</pre>
<p> And at this rather long document from CISCO. </p>
<pre>
 <a rel="nofollow" href="http://www.cisco.com/univercd/cc/td/doc/cisintwk/ito_doc/snmp.htm">http://www.cisco.com/univercd/cc/td/doc/cisintwk/ito_doc/snmp.htm</a>
</pre>
<h3>The images created by MRTG look very strange.</h3>
<p> Remove the *-{week,day,month,year}.png files and start MRTG again. Using MRTG for the first time, you might have to do this twice. This will also help when you introduce new routers into the cfg file.</p>
<h3>What is my Community Name?</h3>
<p> Ask the person in charge of your Router or try &#8216;public&#8217;, as this is the default Community Name.</p>
<h3>My graphs show a flat line during an outage. Why ?</h3>
<p> Well, the short answer is that when an SNMP query goes out and a response doesn&#8217;t come back, MRTG has to assume something to put in the graph, and by default it assumes that the last answer we got back is probably closer to the truth than zero. This assumption is not perfect (as you have noticed). It&#8217;s a trade-off that happens to fail during a total outage. </p>
<p> If this is an unacceptable trade-off, use the <code>unknaszero</code> option. </p>
<p> You may want to know what you&#8217;re trading off, so in the spirit of trade-offs, here&#8217;s the long answer: </p>
<p> The problem is that MRTG doesn&#8217;t know *why* the data didn&#8217;t come back, all it knows is that it didn&#8217;t come back. It has to do something, and it assumes it&#8217;s a stray lost packet rather than an outage. </p>
<p> Why don&#8217;t we always assume the circuit is down and use zero, which will (we think) be more nearly right? Well, it turns out that you may be taking advantage of MRTG&#8216;s &#8220;assume last&#8221; behaviour without being aware of it. </p>
<p> MRTG uses SNMP (Simple Network Management Protocol) to collect data, and SNMP uses UDP (User Datagram Protocol) to ship packets around. UDP is connectionless (not guaranteed) unlike TCP where packets are tracked and acknowledged and, if needed, retransmitted. UDP just throws packets at the network and hopes they arrive. Sometimes they don&#8217;t. </p>
<p> One likely cause of lost SNMP data is congestion; another is busy routers. Other possibilities include transient telecommunications problems, router buffer overflows (which may or may not be congestion-related), &#8220;dirty lines&#8221; (links with high error rates), and acts of God. These things happen all the time; we just don&#8217;t notice because many interactive services are TCP-based and the lost packets get retransmitted automatically. </p>
<p> In the above cases where some SNMP packets are lost but traffic is flowing, assuming zero is the wrong thing to do &#8211; you end up with a graph that looks like it&#8217;s missing teeth whenever the link fills up. MRTG interpolates the lost data to produce a smoother graph which is more accurate in cases of intermittent packet loss. But with V2.8.4 and above, you can use the &#8220;unknaszero&#8221; option to produce whichever graph is best under the conditions typical for your network.</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
