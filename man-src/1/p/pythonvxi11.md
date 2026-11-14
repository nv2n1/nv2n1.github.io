---
title: "pythonvxi11(1)"
name: "pythonvxi11"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pythonvxi11/"
description: "pythonvxi11 – Python VXI11 Documentation"
---

<h2>NAME</h2>
<p> pythonvxi11 &#8211; Python VXI11 Documentation </p>
<p> This Python package supports the VXI-11 Ethernet instrument control protocol for controlling VXI11 and LXI compatible instruments. </p>
<p> See also:</p>
<dl>
<dt>&bull;</p>
<dd> <i>Python VXI11 home page</i></p>
<dt>&bull;</p>
<dd> <i>GitHub repository</i> </p>
<p> Contents:</dl>
<h2>INTRODUCTION TO PYTHON VXI11</h2>
<h3>Overview</h3>
<p> This Python package supports the VXI-11 Ethernet instrument control protocol for controlling VXI11 and LXI compatible instruments. The implementation is pure Python and highly portable. </p>
<p> It is released under the MIT license, see <i>LICENSE</i> for more details. </p>
<p> Copyright (C) 2012-2013 Alex Forencich &lt;<i>alex [at] alexforencich.com</i>&gt; </p>
<p> See also:</p>
<dl>
<dt>&bull;</p>
<dd> <i>Python VXI11 home page</i></p>
<dt>&bull;</p>
<dd> <i>GitHub repository</i></dl>
<h3>Features</h3>
<dl>
<dt>&bull;</p>
<dd> Supports Python 2 and Python 3</p>
<dt>&bull;</p>
<dd> Pure Python</p>
<dt>&bull;</p>
<dd> Highly portable</p>
<dt>&bull;</p>
<dd> Communicates with instruments over the VXI11 TCP/IP instrument control protocol</dl>
<h3>Requirements</h3>
<dl>
<dt>&bull;</p>
<dd> Python 2 or Python 3</dl>
<h3>Installation</h3>
<p> To install the module for all users on the system, administrator rights (root) are required.</p>
<h3>From source</h3>
<p> Download the archive, extract, and run: </p>
<pre>
python setup.py install
</pre>
<h3>Packages</h3>
<p> There are also packaged versions for some Linux distributions:</p>
<dl>
<dt><code>Arch Linux</code></p>
<dd> Python VXI11 is available under the name &quot;python-vxi11-git&quot; in the AUR.</dl>
<h2>PYTHON VXI11 EXAMPLES</h2>
<h3>Opening a connection</h3>
<p> Connect to an Agilent MSO7104A oscilloscope on IP address 192.168.1.104: </p>
<pre>
&gt;&gt;&gt; import vxi11
&gt;&gt;&gt; instr =  vxi11.Instrument(&quot;192.168.1.104&quot;)
&gt;&gt;&gt; print(instr.ask(&quot;*IDN?&quot;))
'AGILENT TECHNOLOGIES,MSO7104A,MY********,06.16.0001'
</pre>
<p> Connect to an Agilent E3649A via an HP 2050A GPIB bridge: </p>
<pre>
&gt;&gt;&gt; import vxi11
&gt;&gt;&gt; instr = vxi11.Instrument(&quot;192.168.1.105&quot;, &quot;gpib,5&quot;)
&gt;&gt;&gt; print(instr.ask(&quot;*IDN?&quot;))
'Agilent Technologies,E3649A,0,1.4-5.0-1.0'
</pre>
<h3>Configuring connections</h3>
<p> Open a connection and set the timeout: </p>
<pre>
&gt;&gt;&gt; import vxi11
&gt;&gt;&gt; instr = vxi11.Instrument(&quot;192.168.1.104&quot;)
&gt;&gt;&gt; instr.timeout = 60*1000
&gt;&gt;&gt; print(instr.ask(&quot;*TST?&quot;))
'0'
</pre>
<h2>VXI11 &#8212; VXI11 DRIVER</h2>
<p> This module provides a VXI11 TCP/IP instrument driver.</p>
<h3>Functions and Exceptions</h3>
<dl>
<dt><code>exception vxi11.Vxi11Error</code></p>
<dd> Exception raised on various occasions; argument is a string describing what is wrong.</dl>
<h3><code>Instrument</code> class</h3>
<dl>
<dt><code>class vxi11.Instrument(host, name=None, client_id=None, term_char=None)</code></p>
<dd> VXI-11 instrument interface client</p>
<dt><code>abort()</code></p>
<dd> Asynchronous abort</p>
<dt><code>ask(message, num=-1, encoding=&#8217;utf-8&#8242;)</code></p>
<dd> Write then read string</p>
<dt><code>ask_raw(data, num=-1)</code></p>
<dd> Write then read binary data</p>
<dt><code>clear()</code></p>
<dd> Send clear command</p>
<dt><code>close()</code></p>
<dd> Close connection</p>
<dt><code>local()</code></p>
<dd> Send local command</p>
<dt><code>lock()</code></p>
<dd> Send lock command</p>
<dt><code>open()</code></p>
<dd> Open connection to VXI-11 instrument</p>
<dt><code>read(num=-1, encoding=&#8217;utf-8&#8242;)</code></p>
<dd> Read string from instrument</p>
<dt><code>read_raw(num=-1)</code></p>
<dd> Read binary data from instrument</p>
<dt><code>read_stb()</code></p>
<dd> Read status byte</p>
<dt><code>remote()</code></p>
<dd> Send remote command</p>
<dt><code>trigger()</code></p>
<dd> Send trigger command</p>
<dt><code>unlock()</code></p>
<dd> Send unlock command</p>
<dt><code>write(message, encoding=&#8217;utf-8&#8242;)</code></p>
<dd> Write string to instrument</p>
<dt><code>write_raw(data)</code></p>
<dd> Write binary data to instrument</dl>
<h2>APPENDIX</h2>
<h3>License</h3>
<p> Copyright (c) 2012-2014 Alex Forencich and Michael Walle </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. </p>
<p> THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>
<dl>
<dt>&bull;</p>
<dd> <i>genindex</i></p>
<dt>&bull;</p>
<dd> <i>modindex</i></p>
<dt>&bull;</p>
<dd> <i>search</i></dl>
<h2>AUTHOR</h2>
<p> Alex Forencich</p>
<h2>COPYRIGHT</h2>
<p> 2013, Alex Forencich </p>
<h2>Index</h2>
<dt><a href="#lbAP">APPENDIX</a></p>
<dd>
<dt><a href="#lbAR">AUTHOR</a></p>
<dd>
<dt><a href="#lbAS">COPYRIGHT</a></p>
<dd></dl>
