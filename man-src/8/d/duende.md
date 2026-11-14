---
title: "duende(8)"
name: "duende"
section: "8"
letter: "d"
url: "/docs/linux/man/8-duende/"
description: "duende – run a child process as a daemon"
---

<p>duende &#8211; run a child process as a daemon</p>
<h2>Description</h2>
<p><code>duende</code> makes a given child process a daemon. The standard output and standard error of the child process is logged via syslog() with a priority of LOG_INFO.</p>
<h2>Usage</h2>
<p><code>duende</code> child_process [ all subsequent arguments passed on to child ]</p>
<h2>Details</h2>
<p>When <code>duende</code> is invoked, it spawns two processes. In addition to spawning the daemonized child process, <code>duende</code> also spawns a process which reads and logs the standard output of the daemonized process. The parent process stays alive so as to monitor the daemonized process. </p>
<p> <code>duende</code> requires a blank directory named /etc/maradns/logger to run. </p>
<p> Should the parent duende process HUP signal, <code>duende</code> will restart the child process. Should the daemonized or logging process received an untrapped HUP signal or exit with an exit code of 8, <code>duende</code> will restart the process. Should the daemonized or logging process exit for any other reason, <code>duende</code> will send the logger process a TERM signal and exit. Should the duende parent process receive a TERM or INT signal, <code>duende</code> sends all of its children TERM signals, then exits. </p>
<p> The duende process must be started as the superuser; this is because Duendeaqs intended child processes (maradns and zoneserver) need to bind to privileged ports, and because duende uses a setuid() call to change the user ID of the logging process to the user with ID 66.</p>
<h2>Logging</h2>
<p><code>duende</code> uses the syslog() facility to log the standard output of the program that it invokes. The name of the program (in other words, the &quot;ident&quot; given to openlog()) is the full path of the first argument given to <code>duende</code>. All messages created by the child process are sent to syslog() with a priority of LOG_INFO and a &quot;facility&quot; of LOG_DAEMON; should duende itself encounter an error, it will send messages to syslog() with a priority of LOG_ALERT. </p>
<p> For example, suppose one invokes duende thusly: </p>
<pre> duende /usr/local/sbin/maradns</pre>
<p>If invoked thusly, duende will log all messages with the &quot;ident&quot; (program name) of &quot;/usr/local/sbin/maradns&quot;. If this is not desired, invoke duende with something like: </p>
<pre> export PATH=$PATH:/usr/local/sbin
 duende maradns</pre>
<p>This will log messages with a (more sensible) &quot;ident&quot; of maradns. </p>
<p> Note: If a non-POSIX Bourne shell (such as csh, es, rc, or fish) is used to invoke MaraDNS, the above syntax needs to be changed. </p>
<p> Also, the directory /etc/maradns/logger, while used by duende, is not used to store any log messages. That is unless, for some reason, one configures syslog to store messages there.</p>
<h2>Examples</h2>
<p>Using duende to start maradns, where the mararc file is /etc/mararc.2 </p>
<pre> duende maradns -f /etc/mararc.3</pre>
<p>Using duende to start zoneserver, where the mararc file is /etc/mararc.4 </p>
<pre> duende zoneserver -f /etc/mararc.4</pre>
<h2>Bugs</h2>
<p><code>Duende</code> assumes that all of its children are well-behaved, eating their vegetables, going to bed when told, and terminating when receiving a TERM signal.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-maradns/">maradns</a>(8)</code>, <code><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</code> </p>
<p> <a rel="nofollow" href="http://www.maradns.org">http://www.maradns.org</a></p>
<h2>Legal Disclaimer</h2>
<p>THIS SOFTWARE IS PROVIDED BY THE AUTHORS aqaqAS ISaqaq AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
<h2>Author</h2>
<p>Duende and this man page are written by Sam Trenholme. D Richard Felker III provided some invaluable assistance with the piping code which <code>duende</code> uses.</p>
