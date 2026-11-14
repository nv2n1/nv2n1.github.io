---
title: "zoneserver(8)"
name: "zoneserver"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zoneserver/"
description: "zoneserver – handle zone transfers and other TCP functions for MaraDNS"
---

<p>zoneserver &#8211; handle zone transfers and other TCP functions for MaraDNS</p>
<h2>Description</h2>
<p><code>zoneserver</code> listens on port 53/tcp and handles DNS zone transfers and any DNS query done over TCP instead of UDP. <code>zoneserver</code> uses a configuration file, <code>/etc/mararc</code> by default, to determine its parameters.</p>
<h2>Usage</h2>
<p><code>zoneserver -f</code> pointer_to_mararc_file</p>
<h2>Options</h2>
<dl>
<dt>-f</p>
<dd>Specifies the location of the configuration file. MaraDNS uses the same configuration file for both the main dns server and the zoneserver.</dl>
<h2>Configuration File Format</h2>
<p>The file format for the mararc file can be found in the <code><a href="/docs/linux/man/5-mararc/">mararc</a>(5)</code> manual page. In particular, the zoneserver uses the zone_transfer_acl, tcp_convert_acl, tcp_convert_server, bind_address, and recursive_acl mararc parameters.</p>
<h2>Example Mararc File</h2>
<p>In this example mararc file, which is used both by maradns and zoneserver, we allow 10.1.2.3, 10.1.14.7, and 192.168.116.{any} to transfer zones, and we allow anyone on the internet to perform TCP queries. The only zone served in this example is example.com: </p>
<pre>ipv4_bind_addresses = &quot;10.1.1.1&quot; # Our IP
tcp_convert_server = &quot;10.1.1.1&quot; # IP of UDP DNS server
tcp_convert_acl = &quot;0.0.0.0/0&quot; # Anyone may do DNS-over-TCP
chroot_dir = &quot;/etc/maradns&quot; # Where zone files are
csv2 = {} # Initialize list of zone files
csv2[&quot;example.com.&quot;] = &quot;db.example.com&quot; # example.com zone file
# The next line is a list of who can transfer zones from us
zone_transfer_acl = &quot;10.1.2.3, 10.1.14.7, 192,168.116.0/24&quot;</pre>
<h2>See Also</h2>
<p>The man pages <code><a href="/docs/linux/man/8-maradns/">maradns</a>(8)</code> and <code><a href="/docs/linux/man/5-mararc/">mararc</a>(5)</code> </p>
<p> <a rel="nofollow" href="http://www.maradns.org">http://www.maradns.org</a></p>
<h2>Bugs</h2>
<p><code>zoneserver</code> assumes that the authoritative NS records are immediately after the SOA record, and that there is at least one non-NS between that last authority NS record for the zone and the first delegation NS record. </p>
<p> IXFR requests are incremental zone transfers, meaning that the DNS server should only display records changed since the last IXFR request. <code>zoneserver</code>, however, treats an IXFR as if it were an AXFR request, outputting all of the records for the zone in question. </p>
<p> <code>zoneserver</code> closes the TCP connection after transferring the requested zone. </p>
<p> If an unauthorized client attempts to connect to the zoneserver, <code>zoneserver</code> immediately disconnects the unauthorized client.</p>
<h2>Legal Disclaimer</h2>
<p>THIS SOFTWARE IS PROVIDED BY THE AUTHORS aqaqAS ISaqaq AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
<h2>Author</h2>
<p>MaraDNS is written by Sam Trenholme. Jaakko Niemi used 5 minutes to put the original version this manpage together. Sam has subsequently revised this manual page.</p>
