---
title: "getzone(1)"
name: "getzone"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getzone/"
description: "getzone – get dns zone from server"
---

<h2 class="name">NAME</h2>
<p> getzone &#8211; get dns zone from server </p>
<h2>DESCRIPTION</h2>
<p> <code>getzone</code> transfers a user-specified dns zone from a zone server and displays it in csv1 format on the standard output. This program is here for compatibility with older setups that use getzone to get zone files; newer setups may wish to consider using the fetchzone tool to obtain csv2-compatible zone files.</p>
<h2>USAGE</h2>
<p> <code>getzone</code> zone_name zone_server_IP [query_class]</p>
<h2>OPTIONS</h2>
<p> <code>zone_name</code> </p>
<p> Name of the dns zone to be transferred. </p>
<p> <code>zone_server_IP</code> </p>
<p> IP address of dns server </p>
<p> <code>query_class</code> </p>
<p> Optional argument which can change the query class from 1 (the default) to 255. This may be needed for some versions of Bind.</p>
<h2>EXAMPLES</h2>
<p> To obtain the zone example.com from the server 192.168.9.8: </p>
<dl>
<dt>
<dd>
<pre>
getzone example.com 192.168.9.8 
</pre>
</dl>
<p> To obtain the zone example.org from the server 10.9.8.78 using a query class of 255: </p>
<dl>
<dt>
<dd>
<pre>
getzone example.com 10.9.8.78 255
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> The man pages <code><a href="/docs/linux/man/8-maradns/">maradns</a>(8)</code> and <code><a href="/docs/linux/man/5-csv1/">csv1</a>(5)</code> </p>
<p> <a rel="nofollow" href="http://www.maradns.org">http://www.maradns.org</a></p>
<h2>LEGAL DISCLAIMER</h2>
<p> THIS SOFTWARE IS PROVIDED BY THE AUTHORS aqaqAS ISaqaq AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
<h2>AUTHOR</h2>
<p> MaraDNS is written by Sam Trenholme. Jaakko Niemi used 5 minutes to put this manpage together. Sam has subsequently made revisions to this manpage. </p>
<h2>Index</h2>
