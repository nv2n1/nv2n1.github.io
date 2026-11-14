---
title: "beakerlib-virtualx(1)"
name: "beakerlib-virtualx"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib-virtualx/"
---

BeakerLib - virtualX - Helpers for handling virtual X server 

<h2>Description</h2>This module provides a simple way to start and stop virtual X server (framebuffer).
<h2>Functions</h2><h3>Virtual X Server</h3>Functions providing simple way how to start and stop virtual X server. 

 <i>rlVirtualXStart</i> 

 Start a virtual X server on a first free display. Tries only first N displays, so you can run out of them. 

 <pre> rlVirtualXStart name</pre><dl><dt>name
<dd>String identifying the X server.</dl>
 

 Returns 0 when the server is started successfully. 

 <i>rlVirtualXGetDisplay</i> 

 Get the <font SIZE="-1">DISPLAY</font> variable for specified virtual X server. 

 <pre> rlVirtualXGetDisplay name</pre><dl><dt>name
<dd>String identifying the X server.</dl>
 

 Displays the number of display where specified virtual X server is running to standard output. Returns 0 on success. 

 <i>rlVirtualXStop</i> 

 Kill the specified X server. 

 <pre> rlVirtualXStop name</pre><dl><dt>name
<dd>String identifying the X server.</dl>
 

 Returns 0 when the server is stopped successfully. 

 <i>Example</i> 

 Below is a simple example of usage. Note that a lot of usefull debugging information is reported on the <font SIZE="-1">DEBUG</font> level, so you can run your test with <tt>&quot;DEBUG=1 make run&quot;</tt> to get them. 

 <pre> rlVirtualXStart $TEST
 rlAssert0 &quot;Virtual X server started&quot; $?
 export DISPLAY=&quot;$( rlVirtualXGetDisplay $TEST )&quot;
 # ...your test which needs X...
 rlVirtualXStop $TEST
 rlAssert0 &quot;Virtual X server killed&quot; $?</pre>These are ``Requires'' lines for your scripts - note different package names for different <font SIZE="-1">RHEL</font> versions: 

 <pre> @echo &quot;Requires: xorg-x11-server-Xvfb&quot; &gt;&gt; $(METADATA) # RHEL-5
 @echo &quot;Requires: xorg-x11-Xvfb&quot; &gt;&gt; $(METADATA) # RHEL-4
 @echo &quot;Requires: XFree86-Xvfb&quot; &gt;&gt; $(METADATA) # RHEL-3</pre><h2>Authors</h2><dl><dt>&bull;
<dd>Jan Hutar &lt;jhutar [at] redhat.com&gt;
<dt>&bull;
<dd>Petr Splichal &lt;psplicha [at] redhat.com&gt; 

</dl>
